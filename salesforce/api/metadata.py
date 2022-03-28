import sublime
import time
import pprint
import os
import csv
import json
import datetime
from xml.sax.saxutils import unescape, quoteattr

from .. import xmltodict
from ..soap import SOAP
from ..login import soap_login, rest_login
from ... import requests, util
from ..lib.panel import Printer


class MetadataApi:
    def __init__(self, settings, **kwargs):
        self.settings = settings
        self.api_version = settings["api_version"]
        self.deploy_options = settings["deploy_options"]
        self.soap = SOAP(settings)
        self.session = None
        self.result = None

    def login(self, session_id_expired=False):
        """ Login with default project credentials

        Arguments:

        * session_id_expired -- Optional; generally, session in .config/session.json is expired, 
            if INVALID_SESSION_ID appeared in response requested by session in session.json,
            we need to call this method with expired session flag again

        Returns:

        * result -- Keep the session info, if `output_session_info` in plugin setting is True, 
            session info will be outputted to console
        """
        if self.settings["login_type"] == "REST":
            result = rest_login(self.settings, session_id_expired)
        else:
            result = soap_login(self.settings, session_id_expired)
        if not result["success"]:
            self.result = result
            return self.result

        self.metadata_url = result["instance_url"] + "/services/Soap/m/%s.0" % self.api_version
        self.headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "SOAPAction": '""'
        }

        self.result = result
        return result

    def _invoke_method(self, _method, options={}):
        """ Support below methods:
            * describeMetadata
            * readMetadata
            * renameMetadata
            * deleteMetadata
            * cancelDeployment
        """

        result = self.login()
        if not result["success"]:
            self.result = result
            return self.result

        # Build soap_body
        body = self.soap.create_request(_method, options)
        try:
            response = requests.post(self.metadata_url, 
                body, verify=False, headers=self.headers)
        except requests.exceptions.RequestException as e:
            self.result = {
                "Error Message":  "Connection Timeout",
                "success": False
            }
            return self.result

        # If status_code is > 399, which means it has error
        if response.status_code > 399:
            # If session is invalid, force to login and execute this again
            if "INVALID_SESSION_ID" in response.text:
                Printer.get("log").write("Session is expired, need login again")
                self.login(True)
                return self._invoke_method(_method, options)

            self.result = util.get_response_error(response)
            return self.result

        result = xmltodict.parse(response.content)
        self.result = result["soapenv:Envelope"]["soapenv:Body"][_method + "Response"]["result"]
        self.result["success"] = True

        return self.result

    def check_status(self, async_process_id, timeout=120):
        """ Ensure the retrieve request is done and then we can 
            continue other work

        * async_process_id -- retrieve request asyncProcessId
        """

        # Headers and Body
        headers = self.headers.copy()
        headers["Accept-Encoding"] = "identity, deflate, compress, gzip"
        soap_body = self.soap.create_request('check_status', {
            "async_process_id": async_process_id
        })

        try:
            session = requests.Session()
            adapter = requests.adapters.HTTPAdapter(max_retries=10)
            session.mount(self.metadata_url, adapter)
            response = session.post(self.metadata_url, soap_body, verify=False,
                                    headers=headers, timeout=timeout)
        except requests.exceptions.RequestException as e:
            self.result = {
                "Error Message":  "Network connection timeout when checking status for retrieve",
                "success": False
            }
            return self.result

        # If status_code is > 399, which means it has error
        if response.status_code > 399:
            self.result = util.get_response_error(response)
            return self.result

        result = xmltodict.parse(response.content)
        self.result = result["soapenv:Envelope"]["soapenv:Body"]["checkStatusResponse"]["result"]
        self.result["success"] = True
        return self.result

    def check_retrieve_status(self, async_process_id):
        """ After async process is done, post a checkRetrieveStatus to 
            obtain the zipFile(base64)

        Arguments:

        * async_process_id -- asyncProcessId of retrieve request 
        """
        headers = self.headers.copy()
        headers["Accept-Encoding"] = "identity, deflate, compress, gzip"
        soap_body = self.soap.create_request('check_retrieve_status', {
            "async_process_id": async_process_id
        })

        try:
            session = requests.Session()
            adapter = requests.adapters.HTTPAdapter(max_retries=10)
            session.mount(self.metadata_url, adapter)
            response = session.post(self.metadata_url, soap_body, 
                                    verify=False, headers=headers, timeout=120)
        except requests.exceptions.RequestException as e:
            self.result = {
                "Error Message":  "Network connection timeout when checking retrieve status",
                "success": False
            }
            return self.result

        # If status_code is > 399, which means it has error
        if response.status_code > 399:
            self.result = util.get_response_error(response)
            return self.result

        result = xmltodict.parse(response.content)
        result = result["soapenv:Envelope"]["soapenv:Body"]["checkRetrieveStatusResponse"]["result"]
        result["success"] = response.status_code < 399
        return result

    def retrieve(self, options, timeout=120):
        """ 1. Issue a retrieve request to start the asynchronous retrieval and asyncProcessId is returned
            2. Issue a checkRetrieveStatus request to check whether the async process job is completed.
            3. After the job is completed, you will get the zipFile(base64) 
            4. Use Python Lib base64 to convert the base64 string to zip file.
            5. Use Python Lib zipFile to unzip the zip file to path

        Arguments:

        * options -- {"types" : types_dict, "package_names": package_names}
        """
        result = self.login()
        if not result or not result["success"]: 
            self.result = result
            return self.result

        # Log the StartTime
        start_time = datetime.datetime.now()

        # Write a separate line
        Printer.get('log').write_start()

        # Before build soap_body, we need to check type supports *,
        # if not, we need to list package for it
        list_package_for_all = False
        if "list_package_for_all" in options and options["list_package_for_all"]:
            list_package_for_all = True
        records = self.prepare_members(options["types"], list_package_for_all)

        # Add types for options
        _types = {}
        for k, values in records.items():
            if "*" in values:
                _types[k] = values
            else:
                members = []
                for v in values:
                    if isinstance(v, str):
                        members.append(v)
                    elif isinstance(v, dict):
                        members.append(v["fullName"])
                _types[k] = members

        options["types"] = _types
        
        # [sf:retrieve]
        Printer.get('log').write("[sf:retrieve] Start request for a retrieve...")

        # Build soap_body
        soap_body = self.soap.create_request('retrieve', options)

        # Post retrieve request
        try:
            response = requests.post(self.metadata_url, soap_body, verify=False,
                                     headers=self.headers, timeout=120)
        except requests.exceptions.RequestException as e:
            self.result = {
                "Error Message":  "Network connection timeout when issuing retrieve request",
                "success": False
            }
            return self.result

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            Printer.get('log').write("[sf:retrieve] Session expired, need login again")
            result = self.login(True)
            if not result["success"]:
                self.result = result
                return self.result
                
            return self.retrieve(options)

        # If status_code is > 399, which means it has error
        if response.status_code > 399:
            self.result = util.get_response_error(response)
            return self.result

        # [sf:retrieve]
        Printer.get('log').write("[sf:retrieve] Request for a retrieve submitted successfully.")

        # Get async process id
        async_process_id = util.getUniqueElementValueFromXmlString(response.content, "id")

        # [sf:retrieve]
        Printer.get('log').write("[sf:retrieve] Request ID for the current retrieve task: "+async_process_id)
        Printer.get('log').write("[sf:retrieve] Waiting for server to finish processing the request...")
        
        # Check status until retrieve request is finished
        done = "false"
        while done == "false":
            # Issue a check_status request to retrieve retrieve result
            # Since version 31 before, we need to invoke check_status before check_retrieve_status
            if self.settings["api_version"] >= 31:
                result = self.check_retrieve_status(async_process_id)
            else:
                result = self.check_status(async_process_id)

            # Catch exception of status retrieving
            if not result or not result["success"]:
                self.result = result
                return self.result

            status = result["state"] if self.api_version < 31 else result["status"]
            done = result["done"]

            # Display retrieve status in the output panel
            Printer.get('log').write("[sf:retrieve] Request Status: %s" % status)

            # Defer to issue request according to status
            sleep_seconds = 2 if status in ["Queued", "Pending", "Succeeded"] else self.settings["metadata_polling_frequency"]
            time.sleep(sleep_seconds)

        # If check status request failed, this will not be done
        if status == "Failed":
            Printer.get('log').write("[sf:retrieve] Request Failed") # [sf:retrieve]
            self.result = {
                "success": False,
                "Error Message": result["errorMessage"]
            }
            return self.result

        # Since version 31, checkRetrieveStatus request is not required
        if self.api_version < 31:
            Printer.get('log').write("[sf:retrieve] Obtaining ZipFile...")
            result = self.check_retrieve_status(async_process_id)

            # Catch exception of status retrieve
            if not result["success"]:
                self.result = result
                return self.result

        # Output the message if have
        if "messages" in result:
            messages = result["messages"]
            if isinstance(messages, dict): 
                messages = [messages]

            for message in messages:
                Printer.get('log').write("[sf:retrieve] %s - %s" % (
                    message["fileName"], 
                    message["problem"]
                ))

        # [sf:retrieve]
        Printer.get('log').write("[sf:retrieve] Finished request %s successfully." % async_process_id)

        # Build Successful
        Printer.get('log').write("\n\nBUILD SUCCESSFUL", False)
        
        # Total time
        total_seconds = (datetime.datetime.now() - start_time).seconds
        Printer.get('log').write("Total time: %s seconds" % total_seconds, False)
        # print('meta retrive result', result)

        self.result = result

    def prepare_members(self, _types, list_package_for_all=False):
        if not self.login():
            return

        if list_package_for_all:
            Printer.get("log").write_start()

        # List package for metadata objects which 'inFolder' is true
        # EmailFolder, DocumentFolder, DashboardFolder and ReportFolder
        records = []
        for _type in _types:
            if "*" not in _types[_type]:
                continue
            if _type in self.settings["metadata_objects_in_folder"]:
                # List package for ``suffix.capitalize() + 'Folder'``
                metadata_object = _type + "Folder" if _type != "EmailTemplate" else "EmailFolder"

                # Waiting message in output console
                Printer.get("log").write("[sf:retrieve] List Folders for %s" % metadata_object)

                # Collect all folders into records
                folders = []
                elements = []
                for record in self.list_package({metadata_object : [""]}):
                    elements.append({
                        "id": record["id"],
                        "fullName": record["fullName"],
                        "lastModifiedDate": record["lastModifiedDate"],
                        "lastModifiedById": record["lastModifiedById"],
                        "lastModifiedByName": record["lastModifiedByName"]
                    })
                    folders.append(record["fullName"])

                for _folders in util.list_chunks(folders, 3):
                    Printer.get("log").write("[sf:retrieve] Fetching component metadata for %s Folder: %s" % (
                        _type, ", ".join(_folders)
                    ))

                    # Add file in folders into retrieve list
                    for record in self.list_package({_type : _folders}):
                        detail = {
                            "id": record["id"],
                            "fullName": record["fullName"],
                            "lastModifiedDate": record["lastModifiedDate"],
                            "lastModifiedById": record["lastModifiedById"],
                            "lastModifiedByName": record["lastModifiedByName"]
                        }
                        elements.append(detail)

                elements = sorted(elements, key=lambda k : k['fullName'])
                _types[_type] = elements

        # In order to speed up retrieve request, we will not list package for them
        # just when we want to get full copy or build package.xml, we will list_package for all
        # Note: CustomObject must be retrieved by ``list_package`` request
        # list package for metadata object which supports wildcard retrieve
        _types_list = []
        # print("retrieve types: ", _types)
        if not list_package_for_all:
            if "CustomObject" in _types and "*" in _types["CustomObject"]:
                _types_list.append("CustomObject")

            if "InstalledPackage" in _types and "*" in _types["InstalledPackage"]:
                _types_list.append("InstalledPackage")
        else:
            for _type in _types:
                if "*" not in _types[_type]:
                    continue
                if _type not in self.settings["metadata_objects_in_folder"]:
                    _types_list.append(_type)

        # Sort _types_list
        _types_list = sorted(_types_list)

        # Maximum number of every list_package request is 3
        # so we need to chunk list to little pieces
        for _trunked_types_list in util.list_chunks(_types_list, 3):
            _trunked_types = {}
            for t in _trunked_types_list:
                _trunked_types[t] = [""]

            # Define type_with_elements for keeping files for _trunked_types
            type_with_elements = {}

            # list package for all non-folder metadata types
            Printer.get("log").write("[sf:retrieve] Fetching component metadata for %s" % (
                ", ".join(_trunked_types)
            ))
            for record in self.list_package(_trunked_types):
                _type = record["type"]

                # StandardValueSetTranslation doesn't have type?
                if isinstance(record["type"], dict):
                    _type = "StandardValueSetTranslation"
                
                detail = {
                    "id": record.get("id", ""),
                    "fullName": record["fullName"],
                    "lastModifiedDate": record["lastModifiedDate"],
                    "lastModifiedById": record["lastModifiedById"],
                    "lastModifiedByName": record["lastModifiedByName"]
                }

                if _type not in type_with_elements:
                    type_with_elements[_type] = [detail]
                else:
                    type_with_elements[_type].append(detail)

            # Order elements
            for t in type_with_elements:
                type_with_elements[t] = sorted(type_with_elements[t], key=lambda k : k['fullName'])

            # Update _types with result of list_package request
            for _type in _trunked_types:
                if _type in type_with_elements:
                    _types[_type] = type_with_elements[_type]
                else:
                    _types[_type] = []

        # After reload is finished
        if list_package_for_all:
            Printer.get("log").write("Project cache is saved to local .config/package.json")

        # Invoked by thread
        self.result = {
            "success": True,
            "types": _types
        }

        # Invoked by retrieve request
        return _types

    def list_package(self, _types):
        # Build soap_body
        soap_body = self.soap.create_request('list_package', {"types": _types})

        try:
            response = requests.post(self.metadata_url, soap_body, 
                                     verify=False, headers=self.headers)
        except requests.exceptions.RequestException as e:
            Printer.get("log").write("Connection timeout when list package for %s" % (
                ", ".join(list(_types.keys()))
            ))
            return []

        # If status_code is > 399, which means it has error
        if response.status_code > 399:
            if "INVALID_SESSION_ID" in response.text:
                Printer.get("log").write("Session is expired, need login again")
                self.login(True)
                return self.list_package(_types)

            result = util.get_response_error(response)
            Printer.get("log").write("Error happened when list package for %s, detail reason: %s" % (
                ", ".join(list(_types.keys())), result.get("Error Message", "Unknown Reason")
            ))

            return []

        result = xmltodict.parse(response.content)
        result = result["soapenv:Envelope"]["soapenv:Body"]["listMetadataResponse"]
        if not result or "result" not in result: 
            return []
        result = result["result"]
        if isinstance(result, dict): 
            result = [result]
        
        self.result = result
        return result

    def check_deploy_status(self, async_process_id): 
        """ After async process is done, post a checkDeployResult to 
            get the deploy result

        Arguments:

        * async_process_id -- retrieve request asyncProcessId
        """
        soap_body = self.soap.create_request('check_deploy_status', {
            "async_process_id": async_process_id
        })

        response = requests.post(self.metadata_url, soap_body,
            headers=self.headers, verify=False, timeout=120)

        # If status_code is > 399, which means it has error
        if response.status_code > 399:
            self.result = util.get_response_error(response)
            return self.result
            
        result = xmltodict.parse(response.content)
        try:
            header = None
            if "soapenv:Header" in result["soapenv:Envelope"]:
                header = result["soapenv:Envelope"]["soapenv:Header"]["DebuggingInfo"]

            result = result["soapenv:Envelope"]["soapenv:Body"]["checkDeployStatusResponse"]["result"]
            result = {
                "success": True,
                "header": header,
                "body": result
            }
        except KeyError as ke:
            result = {
                "Message": "Convert Xml to JSON Exception: " + str(ke),
                "success": False
            }

        return result
        
    def deploy(self, base64_zip, test_classes=[]):
        """ Deploy zip file

        Arguments:

        * zipFile -- base64 encoded zipfile 
        """
        result = self.login()
        if not result or not result["success"]: return

        # Log the StartTime
        start_time = datetime.datetime.now()

        # Populate the soap_body with actual options
        # move the deploy options in to class attributes from better manipulate
        # deploy_options = self.settings["deploy_options"]

        # If just checkOnly, output VALIDATE, otherwise, output DEPLOY
        deploy_or_validate = "validate" if self.deploy_options["checkOnly"] else "deploy"

        # [sf:deploy]
        Printer.get('log').write_start().write("[sf:%s] Start request for a deploy..." % deploy_or_validate)
        options = self.deploy_options
        options["zipfile"] = base64_zip

        # If testLevel is Run Specified Test, 
        # we need to specify the runTests
        testLevel = options.get("testLevel", "NoTestRun") 
        if testLevel == "RunSpecifiedTests":
            options["runTests"] = "\n".join([
                "<met:runTests>%s</met:runTests>" % c for c in test_classes
            ])
        soap_body = self.soap.create_request('deploy', options)

        try:
            response = requests.post(self.metadata_url, soap_body, 
                verify=False, headers=self.headers)
        except requests.exceptions.RequestException as e:
            self.result = {
                "Error Message":  "Network connection timeout when issuing deploy request",
                "success": False
            }
            return self.result

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            Printer.get('log').write("[sf:%s] Session expired, need login again" % deploy_or_validate)
            result = self.login(True)
            if not result["success"]:
                self.result = result
                return self.result
            return self.deploy(base64_zip)

        # If status_code is > 399, which means it has error
        # If status_code is > 399, which means it has error
        if response.status_code > 399:
            self.result = util.get_response_error(response)
            return self.result

        # [sf:deploy]
        Printer.get('log').write("[sf:%s] Request for a deploy submitted successfully." % deploy_or_validate)

        # Get async process id
        async_process_id = util.getUniqueElementValueFromXmlString(response.content, "id")

        # [sf:deploy]
        Printer.get('log').write("[sf:%s] Request ID for the current deploy task: %s" % (deploy_or_validate, async_process_id))
        Printer.get('log').write("[sf:%s] Waiting for server to finish processing the request..." % deploy_or_validate)

        # 2. issue a check status loop request to assure the async
        # process is done
        result = self.check_deploy_status(async_process_id)

        body = result["body"]

        index = 1
        failure_dict = {}
        while body["status"] in ["Pending", "InProgress", "Canceling"]:
            if "stateDetail" in body:
                if int(body["numberComponentsDeployed"]) < int(body["numberComponentsTotal"]):
                    Printer.get('log').write("[sf:%s] Request Status: %s (%s/%s)  -- %s" % (
                        deploy_or_validate,
                        body["status"], 
                        body["numberComponentsDeployed"],
                        body["numberComponentsTotal"],
                        body["stateDetail"]
                    ))
                else:
                    Printer.get('log').write("[sf:%s] TestRun Status: %s (%s/%s)  -- %s" % (
                        deploy_or_validate,
                        body["status"], 
                        body["numberTestsCompleted"],
                        body["numberTestsTotal"],
                        body["stateDetail"]
                    ))
            else:
                Printer.get('log').write("[sf:%s] Request Status: %s" % (
                    deploy_or_validate, body["status"]
                ))

            # Process Test Run Result
            if "runTestResult" in body["details"] and \
                "failures" in body["details"]["runTestResult"]:

                failures = body["details"]["runTestResult"]["failures"]
                if isinstance(failures, dict):
                    if failures["id"] not in failure_dict:
                        failure_dict[failures["id"]] = failures

                        Printer.get('log').write("-" * 84).write("Test Failures: ")
                        Printer.get('log').write("%s.\t%s" % (index, failures["message"]))
                        for msg in failures["stackTrace"].split("\n"):
                            Printer.get('log').write("\t%s" % msg)

                        # [sf:deploy]
                        Printer.get('log').write("-" * 84)

                        index += index
                        
                elif isinstance(failures, list):
                    for f in failures:
                        if f["id"] not in failure_dict:
                            failure_dict[f["id"]] = f

                            Printer.get('log').write("-" * 84).write("Test Failures: ")
                            Printer.get('log').write("%s.\t%s" % (index, f["message"]))

                            # If compile error, there will no stack trace
                            if isinstance(f["stackTrace"], str):
                                for msg in f["stackTrace"].split("\n"):
                                    Printer.get('log').write("\t%s" % msg)
                                Printer.get('log').write("-" * 84)

                            index += 1

            # Thread Wait
            sleep_seconds = 2 if body["status"] == "Pending" else self.settings["metadata_polling_frequency"]
            time.sleep(sleep_seconds)
            
            result = self.check_deploy_status(async_process_id)
            body = result["body"]

        # Check if job is canceled
        if body["status"] == "Canceled":
            Printer.get('log').write("\nBUILD FAILED", False)
            Printer.get('log').write("*********** DEPLOYMENT FAILED ***********", False)
            Printer.get('log').write("Request ID: %s" % async_process_id, False)
            Printer.get('log').write("\nRequest Canceled", False)
            Printer.get('log').write("*********** DEPLOYMENT FAILED ***********", False)

        # If check status request failed, this will not be done
        elif body["status"] == "Failed":
            # Append failure message
            Printer.get('log').write("[sf:%s] Request Failed\n\nBUILD FAILED" % deploy_or_validate)
            Printer.get('log').write("*********** DEPLOYMENT FAILED ***********", False)
            Printer.get('log').write("Request ID: %s" % async_process_id, False)
            
            # Output Failure Details
            failures_messages = []
            if "componentFailures" in body["details"]:
                component_failures = body["details"]["componentFailures"]
                if isinstance(component_failures, dict):
                    component_failures = [component_failures]

                for index in range(len(component_failures)):
                    component_failure = component_failures[index]
                    failures_messages.append("%s. %s -- %s: %s (line %s column %s)" % (
                        index + 1, 
                        component_failure["fileName"],
                        component_failure["problemType"],
                        component_failure["problem"],
                        component_failure["lineNumber"] \
                            if "lineNumber" in component_failure else "N/A",
                        component_failure["columnNumber"] \
                            if "columnNumber" in component_failure else "N/A"
                    ))
            elif "runTestResult" in body["details"]:
                failures = body["details"]["runTestResult"].get("failures", [])
                if isinstance(failures, dict):
                    failures = [failures]

                for index in range(len(failures)):
                    failure = failures[index]
                    failures_messages.append("%s. %s -- %s: %s" % (
                        index + 1, 
                        failure.get("type"),
                        failure.get("name"),
                        failure.get("message")
                    ))

            # Unknown exception printer
            if "errorMessage" in body:
                Printer.get('log').write("\n" + body["errorMessage"], False)

            warning_messages = []
            if "runTestResult" in body["details"]:
                runTestResult = body["details"]["runTestResult"]
                if "codeCoverageWarnings" in runTestResult:
                    coverage_warnings = runTestResult["codeCoverageWarnings"]
                    if isinstance(runTestResult["codeCoverageWarnings"], dict):
                        coverage_warnings = [coverage_warnings]
                    elif isinstance(runTestResult["codeCoverageWarnings"], list):
                        coverage_warnings = coverage_warnings

                    for warn in coverage_warnings:
                        if not isinstance(warn["name"], str): continue
                        warning_messages.append("%s -- %s" % (warn["name"], warn["message"]))

            # Output failure message
            if failures_messages:
                Printer.get('log').write("\n\nAll Component Failures:", False)
                Printer.get('log').write("\n"+"\n\n".join(failures_messages), False)

            # Output warning message
            if warning_messages:
                Printer.get('log').write("\n\nTest Coverage Warnings:", False)
                Printer.get('log').write("\n"+"\n".join(warning_messages), False)
            
            # End for Deploy Result
            Printer.get('log').write("\n*********** %s FAILED ***********" % (
                deploy_or_validate.upper()), False)
        else:
            # Append succeed message
            Printer.get('log').write("\n[sf:%s] Request Succeed" % deploy_or_validate, False)
            Printer.get('log').write("[sf:%s] *********** %s SUCCEEDED ***********" % (
                deploy_or_validate, deploy_or_validate.upper()), False)
            Printer.get('log').write("[sf:%s] Finished request %s successfully." % (
                deploy_or_validate, async_process_id), False)

        # Total time
        total_seconds = (datetime.datetime.now() - start_time).seconds
        Printer.get('log').write("\n\nTotal time: %s seconds" % total_seconds, False)

        # # Display debug log message in the new view
        # view = sublime.active_window().new_file()
        # view.run_command("new_view", {
        #     "name": "Debugging Information",
        #     "input": result.get("header", {}).get("debugLog", "")
        # })

        self.result = result