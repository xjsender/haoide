import sublime
import time
import pprint
import os
import csv
import json
import datetime
from xml.sax.saxutils import unescape, quoteattr

from .. import xmltodict, soap_bodies
from ..login import soap_login
from ... import requests, util


class MetadataApi():
    def __init__(self, settings, **kwargs):
        self.settings = settings
        self.api_version = settings["api_version"]
        self.username = settings["username"]
        self.session = None
        self.result = None

    def login(self, session_id_expired=False):
        """ Login with default project credentials

        Arguments:

        * session_id_expired -- Optional; generally, session in globals() is expired, 
            if INVALID_SESSION_ID appeared in response requested by session in globals(),
            we need to call this method with expired session flag again

        Returns:

        * result -- Keep the session info, if `output_session_info` in plugin setting is True, 
            session info will be outputted to console
        """
        if self.username not in globals() or session_id_expired:
            result = soap_login(self.settings)

            # If login succeed, display error and return False
            if not result["success"]:
                result["Default Project"] = self.settings["default_project"]["project_name"]
                self.result = result
                return self.result

            result["headers"] = {
                "Authorization": "OAuth " + result["session_id"],
                "Content-Type": "application/json; charset=UTF-8",
                "Accept": "application/json"
            }
            globals()[self.username] = result
        else:
            result = globals()[self.username]

        self.session = result
        self.headers = globals()[self.username]["headers"]
        self.instance_url = result["instance_url"]
        self.partner_url = self.instance_url + "/services/Soap/u/%s.0" % self.api_version
        self.metadata_url = self.instance_url + "/services/Soap/m/%s.0" % self.api_version
        self.apex_url = self.instance_url + "/services/Soap/s/%s.0" % self.api_version

        self.result = result
        return result

    def describe_layout(self, sobject, recordtype_id):
        """ Get Page Layout Describe result, including Edit Layout Elements
            View Layout Elements and Available Picklist Values

        Arguments:

        * sobject -- sobject name
        * recordtype_id -- RecordType Id
        """
        # Firstly Login
        self.login()

        # Combine server_url and headers and soap_body
        headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "SOAPAction": '""'
        }
        soap_body = soap_bodies.describe_layout_body.format(
            session_id=globals()[self.username]["session_id"], 
            sobject=sobject, recordtype_id=recordtype_id)

        try:
            response = requests.post(self.partner_url, soap_body, 
                verify=False, headers=headers)
        except Exception as e:
            self.result = {
                "Error Message":  "Network Issue" if "Max retries exceeded" in str(e) else str(e),
                "URL": self.partner_url,
                "Operation": "DESCRIBE LAYOUT",
                "success": False
            }
            return self.result

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.describe_layout(sobject, recordtype_name)

        content = response.content
        result = xmltodict.parse(content)

        try:
            result = result["soapenv:Envelope"]["soapenv:Body"]["describeLayoutResponse"]["result"]
        except (KeyError):
            result = {}
            result["errorCode"] = "Unknown"
            result["message"] = 'body["describeLayoutResponse"]["result"] KeyError'

        result["success"] = response.status_code < 399

        # Self.result is used to keep thread result
        self.result = result

        # This result is used for invoker
        return result

    def execute_anonymous(self, apex_string):
        """ Generate a new view to display executed reusult of Apex Snippet

        Arguments:

        * apex_string -- Apex Snippet
        """
        # Firstly Login
        self.login()

        # https://gist.github.com/richardvanhook/1245068
        headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "Accept-Encoding": 'identity, deflate, compress, gzip',
            "SOAPAction": '""'
        }

        # If we don't quote <, >, & in body, we will get below exception
        # Element type "String" must be followed by either attribute specifications, ">" or "/>"
        # http://wiki.python.org/moin/EscapingXml
        apex_string = quoteattr(apex_string).replace('"', '')
        log_levels = ""
        for log_level in self.settings["anonymous_log_levels"]:
            log_levels += """
            <apex:categories>
                <apex:category>%s</apex:category>
                <apex:level>%s</apex:level>
            </apex:categories>
            """ % (log_level["log_category"], log_level["log_level"])

        soap_body = soap_bodies.execute_anonymous_body.format(
            log_levels=log_levels,
            session_id=globals()[self.username]["session_id"], 
            apex_string=apex_string)

        try:
            response = requests.post(self.apex_url, soap_body, verify=False, 
                headers=headers)
        except UnicodeEncodeError as ue:
            result = {
                "Error Message": "Anonymous code can't contain non-english character",
                "URL": self.apex_url,
                "Operation": "PUT",
                "success": False
            }
            self.result = result
            return self.result
        except Exception as e:
            self.result = {
                "Error Message":  "Network Issue" if "Max retries exceeded" in str(e) else str(e),
                "URL": url,
                "Operation": "PUT",
                "success": False
            }
            return self.result

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.execute_anonymous(apex_string)

        # If status_code is > 399, which means it has error
        content = response.content
        result = {"success": response.status_code < 399}
        if response.status_code > 399:
            if response.status_code == 500:
                result["errorCode"] = util.getUniqueElementValueFromXmlString(content, "faultcode")
                result["message"] = util.getUniqueElementValueFromXmlString(content, "faultstring")
            else:
                result["errorCode"] = util.getUniqueElementValueFromXmlString(content, "errorCode")
                result["message"] = util.getUniqueElementValueFromXmlString(content, "message")

            self.result = result
            return result
        
        # If execute anonymous succeed, just display message with a new view
        result["debugLog"] = unescape(util.getUniqueElementValueFromXmlString(content, "debugLog"))
        result["column"] = util.getUniqueElementValueFromXmlString(content, "column")
        result["compileProblem"] = unescape(util.getUniqueElementValueFromXmlString(content, "compileProblem"))
        result["compiled"] = util.getUniqueElementValueFromXmlString(content, "compiled")
        result["line"] = util.getUniqueElementValueFromXmlString(content, "line")
        result["success"] = util.getUniqueElementValueFromXmlString(content, "success")
        
        # Self.result is used to keep thread result
        self.result = result

        # This result is used for invoker
        return result

    def check_status(self, async_process_id):
        """ Ensure the retrieve request is done and then we can 
            continue other work

        * async_process_id -- retrieve request asyncProcessId
        """

        # Check the status of retrieve job
        headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "Accept-Encoding": 'identity, deflate, compress, gzip',
            "SOAPAction": '""'
        }
        soap_body = soap_bodies.check_status_body.format(
            session_id=globals()[self.username]["session_id"],
            async_process_id=async_process_id)

        response = requests.post(self.metadata_url, soap_body, verify=False, 
            headers=headers)

        # If status_code is > 399, which means it has error
        content = response.content
        result = {}
        if response.status_code > 399:
            result["errorCode"] = util.getUniqueElementValueFromXmlString(content, "errorCode")
            result["message"] = util.getUniqueElementValueFromXmlString(content, "message")
            result["done"] = "Failed"
            result["success"] = False
            return result

        content = response.content
        result = xmltodict.parse(content)
        try:
            result = result["soapenv:Envelope"]["soapenv:Body"]["checkStatusResponse"]["result"]
        except (KeyError):
            result = {
                "errorCode": "Convert Xml to Dict Exception",
                "message": 'body["checkStatusResponse"]["result"] KeyError'
            }

        # print (json.dumps(result, indent=4))
        result["success"] = response.status_code < 399
        return result

    def check_retrieve_status(self, async_process_id):
        """ After async process is done, post a checkRetrieveStatus to 
            obtain the zipFile(base64)

        Arguments:

        * async_process_id -- asyncProcessId of retrieve request 
        """
        headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "Accept-Encoding": 'identity, deflate, compress, gzip',
            "SOAPAction": '""'
        }
        soap_body = soap_bodies.check_retrieve_status_body.format(
            session_id=globals()[self.username]["session_id"],
            async_process_id=async_process_id)

        response = requests.post(self.metadata_url, soap_body, 
            verify=False, headers=headers)

        # If status_code is > 399, which means it has error
        content = response.content
        result = {"success": response.status_code < 399}
        if response.status_code > 399:
            if response.status_code == 500:
                result["errorCode"] = util.getUniqueElementValueFromXmlString(content, "faultcode")
                result["message"] = util.getUniqueElementValueFromXmlString(content, "faultstring")
            else:
                result["errorCode"] = util.getUniqueElementValueFromXmlString(content, "errorCode")
                result["message"] = util.getUniqueElementValueFromXmlString(content, "message")
            return result

        result = xmltodict.parse(response.content)
        result = result["soapenv:Envelope"]["soapenv:Body"]["checkRetrieveStatusResponse"]["result"]
        result["success"] = response.status_code < 399
        return result

    def retrieve(self, soap_body, types=None):
        """ 1. Issue a retrieve request to start the asynchronous retrieval and asyncProcessId is returned
            2. Thread sleep for a while and then issue a checkStatus request to check whether the async 
               process job is completed.
            3. After the job is completed, issue a checkRetrieveStatus request to obtain the zipFile(base64) 
               in the retrieve result.
            4. Use Python Lib base64 to convert the base64 string to zip file.
            5. Use Python Lib zipFile to unzip the zip file to path

        Arguments:

        * soap_body -- soap_body for retrieving
        """

        # Log the StartTime
        start_time = datetime.datetime.now()

        # Open panel
        panel = sublime.active_window().create_output_panel('panel')  # Create panel

        # Firstly Login
        util.append_message(panel, "[sf:retrieve] Start login...")
        result = self.login()
        if not result["success"]:
            util.append_message(panel, "[sf:retrieve] Login failed...")
            self.result = result
            return self.result
        util.append_message(panel, "[sf:retrieve] Login succeed...")

        # 1. Issue a retrieve request to start the asynchronous retrieval
        headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "SOAPAction": '""'
        }

        # Populate the soap_body with actual session id
        if types:
            soap_body = soap_body.format(
                globals()[self.username]["session_id"], 
                self.api_version, types)
        else:
            soap_body = soap_body.format(
                globals()[self.username]["session_id"], 
                self.api_version)

        # [sf:retrieve]
        util.append_message(panel, "[sf:retrieve] Start request for a retrieve...")

        # Post retrieve request
        try:
            response = requests.post(self.metadata_url, soap_body, verify=False, headers=headers)
        except Exception as e:
            self.result = {
                "Error Message":  "Network Issue" if "Max retries exceeded" in str(e) else str(e),
                "URL": self.metadata_url,
                "Operation": "RETRIEVE",
                "success": False
            }
            return self.result

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.retrieve(soap_body, types)

        # If status_code is > 399, which means it has error
        content = response.content
        result = {"success": response.status_code < 399}
        if response.status_code > 399:
            if response.status_code == 500:
                result["errorCode"] = util.getUniqueElementValueFromXmlString(content, "faultcode")
                result["message"] = util.getUniqueElementValueFromXmlString(content, "faultstring")
            else:
                result["errorCode"] = util.getUniqueElementValueFromXmlString(content, "errorCode")
                result["message"] = util.getUniqueElementValueFromXmlString(content, "message")
            self.result = result
            return

        # [sf:retrieve]
        util.append_message(panel, "[sf:retrieve] Request for a retrieve submitted successfully.")

        # Get async process id
        async_process_id = util.getUniqueElementValueFromXmlString(content, "id")

        # [sf:retrieve]
        util.append_message(panel, "[sf:retrieve] Request ID for the current retrieve task: "+async_process_id)

        # Issue request for retrieving status and waiting for response
        util.append_message(panel, "[sf:retrieve] Request for a retrieve submitted successfully.")
        util.append_message(panel, "[sf:retrieve] Waiting for server to finish processing the request...")

        # 2. issue a check status loop request to assure the async request is done
        result = self.check_status(async_process_id)

        # Catch exception of status retrieving
        if not result["success"]:
            self.result = result
            return self.result
        
        # Output retrieve status
        util.append_message(panel, "[sf:retrieve] Request Status: %s" % result["state"])
        
        # Check status until retrieve request is finished
        while result["done"] == "false":
            sleep_seconds = 2 if result["state"] == "Queued" else 1
            time.sleep(sleep_seconds)

            result = self.check_status(async_process_id)
            sublime.active_window().run_command("show_panel", {"panel": "output.panel"})
            util.append_message(panel, "[sf:retrieve] Request Status: %s" % result["state"])

        # If check status request failed, this will not be done
        if result["state"] == "Failed":
            util.append_message(panel, "[sf:retrieve] Request Failed") # [sf:retrieve]
            self.result = result
            return

        # 3 Obtain zipFile(base64)
        util.append_message(panel, "[sf:retrieve] Start to download package zipFile")
        result = self.check_retrieve_status(async_process_id)
        util.append_message(panel, "[sf:retrieve] Finished zipFile downloading")

        # Output the message if have
        if "messages" in result:
            if isinstance(result["messages"], dict):
                message = result["messages"]
                util.append_message(panel, "[sf:retrieve] %s - %s" % (
                    message["fileName"], 
                    message["problem"]
                ))
            elif isinstance(result["messages"], list):
                for message in result["messages"]:
                    util.append_message(panel, "[sf:retrieve] %s - %s" % (
                        message["fileName"], 
                        message["problem"]
                    ))

        # [sf:retrieve]
        util.append_message(panel, "[sf:retrieve] Finished request %s successfully." % async_process_id)

        # Build Successful
        util.append_message(panel, "\n\nBUILD SUCCESSFUL", False)
        
        # Total time
        total_seconds = (datetime.datetime.now() - start_time).seconds
        util.append_message(panel, "Total time: %s seconds" % total_seconds, False)

        self.result = result

    def check_deploy_status(self, async_process_id): 
        """ After async process is done, post a checkDeployResult to 
            get the deploy result

        Arguments:

        * async_process_id -- retrieve request asyncProcessId
        """
        headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "SOAPAction": '""'
        }
        soap_body = soap_bodies.check_deploy_status.format(
            globals()[self.username]["session_id"], async_process_id)
        response = requests.post(self.metadata_url, soap_body, verify=False, 
            headers=headers)

        # If status_code is > 399, which means it has error
        content = response.content
        result = {"success": response.status_code < 399}
        if response.status_code > 399:
            result["errorCode"] = util.getUniqueElementValueFromXmlString(content, "errorCode")
            result["message"] = util.getUniqueElementValueFromXmlString(content, "message")
            return result

        result = xmltodict.parse(content)
        # print (json.dumps(result, indent=4))
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
                "Message": "Convert Xml to Dict Exception",
                "Detail": 'body["checkDeployStatusResponse"]["result"] KeyError' + str(ke),
                "success": False
            }

        return result
        
    def deploy(self, base64_zip):
        """ Deploy zip file

        Arguments:

        * zipFile -- base64 encoded zipfile 
        """
        # Log the StartTime
        start_time = datetime.datetime.now()

        # Open panel
        panel = sublime.active_window().create_output_panel('panel')  # Create panel

        # Populate the soap_body with actual session id
        deploy_options = self.settings["deploy_options"]
        
        # If just checkOnly, output VALIDATE, otherwise, output DEPLOY
        deploy_or_validate = "validate" if deploy_options["checkOnly"] else "deploy"

        # Firstly Login
        util.append_message(panel, "[sf:%s] Start login..." % deploy_or_validate)
        result = self.login()
        if not result["success"]:
            util.append_message(panel, "[sf:%s] Login failed..." % deploy_or_validate)
            self.result = result
            return self.result
        util.append_message(panel, "[sf:%s] Login succeed..." % deploy_or_validate)

        # 1. Issue a deploy request to start the asynchronous retrieval
        headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "SOAPAction": '""'
        }

        # [sf:%s]
        util.append_message(panel, "[sf:%s] Start request for a deploy..." % deploy_or_validate)

        soap_body = soap_bodies.deploy_package.format(
            globals()[self.username]["session_id"], 
            base64_zip,
            deploy_options["allowMissingFiles"],
            deploy_options["autoUpdatePackage"],
            deploy_options["checkOnly"],
            deploy_options["ignoreWarnings"],
            deploy_options["performRetrieve"],
            deploy_options["purgeOnDelete"],
            deploy_options["rollbackOnError"],
            deploy_options["runAllTests"],
            deploy_options["singlePackage"]
        )

        try:
            response = requests.post(self.metadata_url, soap_body, verify=False, headers=headers)
        except Exception as e:
            self.result = {
                "Error Message":  "Network Issue" if "Max retries exceeded" in str(e) else str(e),
                "URL": self.metadata_url,
                "Operation": "DEPLOY",
                "success": False
            }
            return self.result

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.deploy(panel, zipfile)

        # If status_code is > 399, which means it has error
        content = response.content
        result = {"success": response.status_code < 399}
        if response.status_code > 399:
            if response.status_code == 500:
                result["errorCode"] = util.getUniqueElementValueFromXmlString(content, "faultcode")
                result["message"] = util.getUniqueElementValueFromXmlString(content, "faultstring")
            else:
                result["errorCode"] = util.getUniqueElementValueFromXmlString(content, "errorCode")
                result["message"] = util.getUniqueElementValueFromXmlString(content, "message")
            self.result = result
            return

        # [sf:%s]
        util.append_message(panel, "[sf:%s] Request for a deploy submitted successfully." % deploy_or_validate)

        # Get async process id
        async_process_id = util.getUniqueElementValueFromXmlString(content, "id")

        # [sf:%s]
        util.append_message(panel, "[sf:%s] Request ID for the current deploy task: %s" % (deploy_or_validate, async_process_id))

        # [sf:%s]
        util.append_message(panel, "[sf:%s] Waiting for server to finish processing the request..." % deploy_or_validate)

        # 2. issue a check status loop request to assure the async
        # process is done
        result = self.check_deploy_status(async_process_id)

        body = result["body"]

        index = 1
        failure_dict = {}
        while body["status"] in ["Pending", "InProgress", "Canceling"]:
            if "stateDetail" in body:
                if body["numberComponentsDeployed"] < body["numberComponentsTotal"]:
                    util.append_message(panel, "[sf:%s] Request Status: %s (%s/%s)  -- %s" % (
                        deploy_or_validate,
                        body["status"], 
                        body["numberComponentsDeployed"],
                        body["numberComponentsTotal"],
                        body["stateDetail"]
                    ))
                else:
                    util.append_message(panel, "[sf:%s] TestRun Status: %s (%s/%s)  -- %s" % (
                        deploy_or_validate,
                        body["status"], 
                        body["numberTestsCompleted"],
                        body["numberTestsTotal"],
                        body["stateDetail"]
                    ))
            else:
                util.append_message(panel, "[sf:%s] Request Status: %s" % (
                    deploy_or_validate, body["status"]
                ))

            # Process Test Run Result
            if "runTestResult" in body["details"] and \
                "failures" in body["details"]["runTestResult"]:

                failures = body["details"]["runTestResult"]["failures"]
                if isinstance(failures, dict):
                    if failures["id"] not in failure_dict:
                        failure_dict[failures["id"]] = failures

                        # [sf:deploy] -------------------------------------------------------
                        util.append_message(panel, "-" * 84)

                        # Failure message body
                        util.append_message(panel, "Test Failures: ")
                        util.append_message(panel, "%s.\t%s" % (index, failures["message"]))
                        for msg in failures["stackTrace"].split("\n"):
                            util.append_message(panel, "\t%s" % msg)

                        # [sf:deploy] -------------------------------------------------------
                        util.append_message(panel, "-" * 84)

                        index += index
                        
                elif isinstance(failures, list):
                    for f in failures:
                        if f["id"] not in failure_dict:
                            failure_dict[f["id"]] = f

                            # [sf:deploy] -------------------------------------------------------
                            util.append_message(panel, "-" * 84)

                            util.append_message(panel, "Test Failures: ")
                            util.append_message(panel, "%s.\t%s" % (index, f["message"]))

                            # If compile error, there will no stack trace
                            if isinstance(f["stackTrace"], str):
                                for msg in f["stackTrace"].split("\n"):
                                    util.append_message(panel, "\t%s" % msg)
                                util.append_message(panel, "-" * 84)

                            index += 1

            # Thread Wait
            sleep_seconds = 2 if body["status"] == "Pending" else 1
            time.sleep(sleep_seconds)
            
            result = self.check_deploy_status(async_process_id)
            body = result["body"]

        # Check if job is canceled
        if body["status"] == "Canceled":
            util.append_message(panel, "\nBUILD FAILED", False)
            util.append_message(panel, "*********** DEPLOYMENT FAILED ***********", False)
            util.append_message(panel, "Request ID: %s" % async_process_id, False)
            util.append_message(panel, "\nRequest Canceled", False)
            util.append_message(panel, "*********** DEPLOYMENT FAILED ***********", False)

        # If check status request failed, this will not be done
        elif body["status"] == "Failed":
            # Append failure message
            util.append_message(panel, "[sf:%s] Request Failed\n\nBUILD FAILED" % deploy_or_validate)
            util.append_message(panel, "*********** DEPLOYMENT FAILED ***********", False)
            util.append_message(panel, "Request ID: %s" % async_process_id, False)

            # Output Failure Details
            failures_messages = []
            if "componentFailures" in body["details"]:
                component_failures = body["details"]["componentFailures"]
                if isinstance(component_failures, dict):
                    component_failure = component_failures
                    failures_messages.append("1. %s -- %s: %s (line %s)" % (
                        component_failure["fileName"],
                        component_failure["problemType"],
                        component_failure["problem"].replace("\n", " "),
                        component_failure["lineNumber"] \
                            if "lineNumber" in component_failure else "0"
                    ))
                elif isinstance(component_failures, list):
                    for index in range(len(component_failures)):
                        component_failure = component_failures[index]
                        failures_messages.append("%s. %s -- %s: %s (line %s)" % (
                            index+1, 
                            component_failure["fileName"],
                            component_failure["problemType"],
                            component_failure["problem"],
                            component_failure["lineNumber"] \
                                if "lineNumber" in component_failure else "0"
                        ))

            # Output failure message
            if failures_messages:
                util.append_message(panel, "\n\nAll Component Failures:", False)
                util.append_message(panel, "\n"+"\n\n".join(failures_messages), False)
                util.append_message(panel, "\n[sf:%s] *********** %s Failed ***********" % (
                    deploy_or_validate, deploy_or_validate.upper()), False)
        else:
            # Append succeed message
            util.append_message(panel, "\n[sf:%s] Request Succeed" % deploy_or_validate, False)
            util.append_message(panel, "[sf:%s] *********** %s SUCCEEDED ***********" % (
                deploy_or_validate, deploy_or_validate.upper()), False)
            util.append_message(panel, "[sf:%s] Finished request %s successfully." % (deploy_or_validate, async_process_id), False)

        # Total time
        total_seconds = (datetime.datetime.now() - start_time).seconds
        util.append_message(panel, "\n\nTotal time: %s seconds" % total_seconds, False)

        # Display debug log message in the new view
        if "header" in result and result["header"] and "debugLog" in result["header"]:
            view = sublime.active_window().new_file()
            view.run_command("new_view", {
                "name": "Debugging Information",
                "input": result["header"]["debugLog"]
            })

        self.result = result