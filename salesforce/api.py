import sublime
import pprint
import json
import time
import datetime
import os

import urllib.parse
from .. import requests
from .. import context

from . import xmltodict
from . import soap_bodies
from . import message
from . import util
from .login import soap_login
from .util import getUniqueElementValueFromXmlString
from xml.sax.saxutils import unescape
from xml.sax.saxutils import quoteattr

SEPRATE = "-" * 100
class SalesforceApi():
    def __init__(self, toolingapi_settings, **kwargs):
        self.toolingapi_settings = toolingapi_settings
        self.api_version = toolingapi_settings["api_version"]
        self.username = toolingapi_settings["username"]
        self.result = None

    def login(self, session_id_expired):
        if self.username not in globals() or session_id_expired:
            result = soap_login(self.toolingapi_settings)

            # If login succeed, display error and return False
            if result["status_code"] > 399:
                print (message.SEPRATE.format(util.get_error_message(result)))
                return False

            result["headers"] = {
                "Authorization": "OAuth " + result["session_id"],
                "Content-Type": "application/json; charset=UTF-8",
                "Accept": "application/json"
            }
            globals()[self.username] = result

        # Integration env., we need to reuse this session id in other purpose
        if self.toolingapi_settings["output_session_info"]:
            pprint.pprint(globals()[self.username])

        return True
    
    def get(self, component_url, timeout=120):
        """
        Get component describe result according to component_url

        :component_url: Component URL, for exmaple, /services/data/v28.0/sobjects/Contact/describe
        """
        # Firstly, login
        self.login(False)

        headers = globals()[self.username]["headers"]
        instance_url = globals()[self.username]['instance_url']
        response = requests.get(instance_url + component_url, 
            data=None, verify=False, headers=headers, timeout=timeout)

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.get(component_url)
        
        # If status_code is > 399, which means it has error
        result = {}
        status_code = response.status_code
        if status_code > 399:
            response_result = response.json()[0]
            result["errorCode"] = response_result.get("errorCode")
            result["message"] = response_result.get("message")
        else:
            try:
                result = response.json()
            except:
                result = response.text
        result["status_code"] = status_code
        
        # Self.result is used to keep thread result
        self.result = result

        # This result is used for invoker
        return result

    def post(self, post_url, data, timeout=120):
        # Firstly, login
        self.login(False)

        headers = globals()[self.username]["headers"]
        instance_url = globals()[self.username]['instance_url']
        response = requests.post(instance_url + post_url, 
            data=json.dumps(data), verify=False, headers=headers, timeout=timeout)

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.post(post_url, data)
        
        # If status_code is > 399, which means it has error
        result = {}
        status_code = response.status_code
        if status_code > 399:
            response_result = response.json()[0]
            result["errorCode"] = response_result.get("errorCode")
            result["message"] = response_result.get("message")
        else:
            result = response.json()
        result["status_code"] = status_code

        # Self.result is used to keep thread result
        self.result = result

        # This result is used for invoker
        return result

    def delete(self, component_url, timeout=120):
        # Firstly, login
        self.login(False)

        url = globals()[self.username]['instance_url'] + component_url
        headers = globals()[self.username]["headers"]
        response = requests.delete(url, data=None, 
            verify=False, headers=headers, timeout=timeout)

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.delete(component_url)

        result = {
            "status_code": response.status_code
        }

        if response.status_code > 399:
            response_result = response.json()[0]
            result["message"] = response_result["message"]
            result["errorCode"] = response_result["errorCode"]
        
        # Self.result is used to keep thread result
        self.result = result

        # This result is used for invoker
        return result

    def query(self, soql, is_toolingapi=False, timeout=120):
        # Firstly, login
        self.login(False)

        instance_url = globals()[self.username]['instance_url']
        try:
            soql = urllib.parse.urlencode({'q' : soql})
        except:
            soql = urllib.urlencode({'q' : soql})

        # Just API 28 support CustomField
        if is_toolingapi:
            url = instance_url + '/services/data/v{0}.0/tooling/query?{1}'.format(self.api_version, soql)
        else:
            url = instance_url + '/services/data/v{0}.0/query?{1}'.format(self.api_version, soql)

        headers = globals()[self.username]["headers"]
        response = requests.get(url, data=None, verify=False, timeout=timeout, 
            headers=headers)
            
        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.query(soql)

        # If status_code is > 399, which means it has error
        result = {}
        status_code = response.status_code
        if status_code > 399:
            response_result = response.json()[0]
            result["errorCode"] = response_result.get("errorCode")
            result["message"] = response_result.get("message")
        else:
            result = response.json()
        
        # Save status_code into result
        result["status_code"] = status_code
            
        # Self.result is used to keep thread result
        self.result = result

        # This result is used for invoker
        return result

    def query_more(self, nextRecordUrl, is_toolingapi=False):
        return self.get(nextRecordUrl)

    def query_all(self, soql, is_toolingapi=False):
        def get_all_result(previous_result):
            if "done" in previous_result and previous_result['done']:
                return previous_result
            elif "done" in previous_result and previous_result["done"] == False:
                result = self.query_more(previous_result['nextRecordsUrl'], is_toolingapi=is_toolingapi)
                result['totalSize'] += previous_result['totalSize']
                # Include the new list of records with the previous list
                previous_result['records'].extend(result['records'])
                result['records'] = previous_result['records']
                # Continue the recursion
                return get_all_result(result)

        result = self.query(soql, is_toolingapi=is_toolingapi)
        # Database.com not support ApexComponent
        if result["status_code"] > 399: 
            self.result = result
            return result

        all_result = get_all_result(result)

        # Self.result is used to keep thread result
        self.result = all_result

        # This result is used for invoker
        return all_result

    def describe_sobject(self, sobject):
        """
        Sends a GET request. Return sobject describe result

        :sobject: sObjectType
        """

        url = "/services/data/v{0}.0/sobjects/".format(self.api_version) + sobject + "/describe"
        result = self.get(url)

        # Self.result is used to keep thread result
        self.result = result

        # This result is used for invoker
        return result

    def describe_global(self):
        """
        Sends a GET request. Return global describe

        :return: sobjects 
        :return type: dict
        """

        url = "/services/data/v{0}.0/sobjects/".format(self.api_version)
        result = self.get(url)

        # Self.result is used to keep thread result
        self.result = result

        # This result is used for invoker
        return result

    def describe_global_custom(self):
        """
        Get the custom sobjects in global describe

        :return: sobjects 
        :return type: list
        """

        result = self.describe_global()
        custom_sobjects = [so["name"] for so in result["sobjects"] if so["custom"]]

        self.result = common_sobjects
        return custom_sobjects

    def describe_global_common(self):
        """
        Get the common used sobjects in global describe, 
        including custom sobject and common standard sobjects

        :return: sobjects 
        :return type: list
        """

        standard_sobjects = [
            "Account", "AccountContactRole", "Activity", "Asset", 
            "Campaign", "CampaignMember", "Case", "Contact", 
            "Contract", "Event", "Lead", "Opportunity", 
            "OpportunityLineItem", "Product2", "UserRole", 
            "Task", "User", "CampaignMemberStatus", 'Attachment',
            "OpportunityLineItemSchedule", "Profile"
        ]

        result = self.describe_global()
        common_sobjects = \
            [so["name"] for so in result["sobjects"] if so["custom"] or \
             so["name"] in standard_sobjects]

        self.result = common_sobjects
        return common_sobjects

    def create_trace_flag(self, traced_entity_id=None):
        """
        Create Debug Log Trace by traced_entity_id

        :traced_entity_id: Component Id or User Id
        """
        while traced_entity_id == None and (self.username not in globals()):
            self.login(True)
            traced_entity_id = globals()[self.username]["user_id"]
            
        # Create Trace Flag
        trace_flag = self.toolingapi_settings["trace_flag"]
        trace_flag["TracedEntityId"] = traced_entity_id

        # We must set the expiration date to next day, 
        # otherwise, the debug log record will not be created 
        nextday = datetime.date.today() + datetime.timedelta(1)
        nextday_str = datetime.datetime.strftime(nextday, "%Y-%m-%d")
        trace_flag["ExpirationDate"] = nextday_str

        post_url = "/services/data/v{0}.0/tooling/sobjects/TraceFlag".format(self.api_version)
        result = self.post(post_url, trace_flag)

        return result

    def get_debug_log_detail(self, log_id, timeout=120):
        """
        Retrieve a raw log by ID

        :log_id: ApexLogId
        :return: raw data of log
        """
        # Firstly Login
        self.login(False)

        url = "/services/data/v{0}.0/sobjects/ApexLog/".format(self.api_version) + log_id + "/Body"
        headers = globals()[self.username]["headers"]
        instance_url = globals()[self.username]['instance_url']
        response = requests.get(instance_url + url, 
            verify=False, headers=headers, timeout=timeout)

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.get_debug_log_detail(log_id)

        result = {
            "status_code": response.status_code,
            "result": response.text
        }
        self.result = result
        return result

    def run_test(self, class_id, traced_entity_id=None):
        """
        Run Test according to test class_id, return error if has

        :class_id: Apex Test Class Id
        :traced_entity_id: Component Id or User Id
        """
        # Firstly Login
        self.login(False)

        # Create trace flag
        traced_entity_id = globals()[self.username]["user_id"]
        self.create_trace_flag(traced_entity_id)

        time.sleep(2)
        post_url = "/services/data/v{0}.0/sobjects/ApexTestQueueItem".format(self.api_version)
        data = {"ApexClassId": class_id}
        result = self.post(post_url, data)
        
        if result["status_code"] > 399:
            self.result = result
            return
        
        # Wait for the ApexTestQueueItem is over
        time.sleep(10)
        queue_item_id = result["id"]
        queue_item_soql = """SELECT Id, Status FROM ApexTestQueueItem 
            WHERE Id='%s'""" % queue_item_id
        result = self.query(queue_item_soql)

        if result["status_code"] > 399:
            self.result = result
            return
        
        # If totalSize is Zero, it means we need to wait
        # Until Test is finished
        while result["totalSize"] == 0 or result["records"][0]["Status"] == "Queued":
            time.sleep(10)
            result = self.query(queue_item_soql)

        test_result_soql = """SELECT ApexClass.Id,ApexClass.Name,ApexLogId,
            AsyncApexJobId,Id,Message,MethodName,Outcome,QueueItemId,StackTrace,
            TestTimestamp FROM ApexTestResult 
            WHERE QueueItemId = '%s'""" % queue_item_id

         # After Test is finished, get result
        result = self.query(test_result_soql)
        result = result["records"]
        
        # Combine these two result
        self.result = result

    def describe_layout(self, sobject, recordtype_id):
        """
        Get Page Layout Describe result, including Edit Layout Elements
        View Layout Elements and Available Picklist Values

        :sobject: sObjectType
        :recordtype_name: RecordType Name
        """
        # Firstly Login
        self.login(False)

        # Combine server_url and headers and soap_body
        server_url = globals()[self.username]['instance_url'] + "/services/Soap/u/{0}.0".format(self.api_version)
        headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "SOAPAction": '""'
        }
        soap_body = soap_bodies.describe_layout_body.format(
            session_id=globals()[self.username]["session_id"], 
            sobject=sobject, recordtype_id=recordtype_id)

        response = requests.post(server_url, soap_body, verify=False, 
            headers=headers)

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.describe_layout(sobject, recordtype_name)

        # If status_code is > 399, which means it has error
        content = response.content
        result = xmltodict.parse(content)
        try:
            result = result["soapenv:Envelope"]["soapenv:Body"]["describeLayoutResponse"]["result"]
        except (KeyError):
            result = {}
            result["errorCode"] = "Unknown"
            result["message"] = 'body["describeLayoutResponse"]["result"] KeyError'

        result["status_code"] = response.status_code

        # Self.result is used to keep thread result
        self.result = result

        # This result is used for invoker
        return result

    def execute_anonymous(self, apex_string):
        """
        Generate a new view to display executed reusult of Apex Snippet

        :apex_string: Apex Snippet
        """
        # Firstly Login
        self.login(False)

        server_url = globals()[self.username]['instance_url'] + "/services/Soap/s/{0}.0".format(self.api_version)
        # https://gist.github.com/richardvanhook/1245068
        headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "SOAPAction": '""'
        }

        # If we don't quote <, >, & in body, we will get below exception
        # Element type "String" must be followed by either attribute specifications, ">" or "/>"
        # http://wiki.python.org/moin/EscapingXml
        apex_string = quoteattr(apex_string).replace('"', '')
        soap_body = soap_bodies.execute_anonymous_body.format(
            session_id=globals()[self.username]["session_id"], 
            apex_string = apex_string)

        response = requests.post(server_url, soap_body, verify=False, 
            headers=headers)

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.execute_anonymous(apex_string)

        # If status_code is > 399, which means it has error
        content = response.content
        result = {"status_code": response.status_code}
        if response.status_code > 399:
            if response.status_code == 500:
                result["errorCode"] = getUniqueElementValueFromXmlString(content, "faultcode")
                result["message"] = getUniqueElementValueFromXmlString(content, "faultstring")
            else:
                result["errorCode"] = getUniqueElementValueFromXmlString(content, "errorCode")
                result["message"] = getUniqueElementValueFromXmlString(content, "message")

            self.result = result
            return result
        
        # If execute anonymous succeed, just display message with a new view
        result["debugLog"] = unescape(getUniqueElementValueFromXmlString(content, "debugLog"))
        result["column"] = getUniqueElementValueFromXmlString(content, "column")
        result["compileProblem"] = unescape(getUniqueElementValueFromXmlString(content, "compileProblem"))
        result["compiled"] = getUniqueElementValueFromXmlString(content, "compiled")
        result["line"] = getUniqueElementValueFromXmlString(content, "line")
        result["success"] = getUniqueElementValueFromXmlString(content, "success")
        
        # Self.result is used to keep thread result
        self.result = result

        # This result is used for invoker
        return result

    def check_status(self, async_process_id):
        """
        Ensure the retrieve request is done and then we can continue other work

        @async_process_id: retrieve request asyncProcessId
        """
        # Thread sleep for 10 seconds
        print ("Retrieve is in progress, please wait for 30 seconds.")
        time.sleep(30)

        # Check the status of retrieve job
        server_url = globals()[self.username]['instance_url'] + "/services/Soap/m/{0}.0".format(self.api_version)
        headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "SOAPAction": '""'
        }
        soap_body = soap_bodies.check_status_body.format(
            session_id=globals()[self.username]["session_id"],
            async_process_id=async_process_id)

        response = requests.post(server_url, soap_body, verify=False, 
            headers=headers)

        # If status_code is > 399, which means it has error
        content = response.content
        result = {"status_code": response.status_code}
        if response.status_code > 399:
            result["errorCode"] = getUniqueElementValueFromXmlString(content, "errorCode")
            result["message"] = getUniqueElementValueFromXmlString(content, "message")
            result["done"] = "Failed"
            return result

        # Get the retrieve status
        done = getUniqueElementValueFromXmlString(content, "done")

        # If retrieve is not done, sleep 10s and check again
        if done == "false":
            return self.check_status(async_process_id)

        # If retrieve is done
        result["done"] = True
        result["state"] = getUniqueElementValueFromXmlString(content, "state")

        return result

    def check_retrieve_status(self, async_process_id):
        """
        After async process is done, post a checkRetrieveStatus to 
        obtain the zipFile(base64)

        @async_process_id: retrieve request asyncProcessId
        """
        server_url = globals()[self.username]['instance_url'] + "/services/Soap/m/{0}.0".format(self.api_version)
        headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "SOAPAction": '""'
        }
        soap_body = soap_bodies.check_retrieve_status_body.format(
            session_id=globals()[self.username]["session_id"],
            async_process_id=async_process_id)

        response = requests.post(server_url, soap_body, verify=False, 
            headers=headers)

        # If status_code is > 399, which means it has error
        content = response.content
        result = {"status_code": response.status_code}
        if response.status_code > 399:
            result["errorCode"] = getUniqueElementValueFromXmlString(content, "errorCode")
            result["message"] = getUniqueElementValueFromXmlString(content, "message")
            return result

        result["zipFile"] = getUniqueElementValueFromXmlString(content, "zipFile")

        return result

    def retrieve_all(self):
        """
        1. Issue a retrieve request to start the asynchronous retrieval and asyncProcessId is returned
        2. Thread sleep for a while and then issue a checkStatus request to check whether the async 
           process job is completed.
        3. After the job is completed, issue a checkRetrieveStatus request to obtain the zipFile(base64) 
           in the retrieve result.
        4. Use Python Lib base64 to convert the base64 string to zip file.
        5. Use Python Lib zipFile to unzip the zip file to path
        """
        # Firstly Login
        self.login(False)

        # 1. Issue a retrieve request to start the asynchronous retrieval
        server_url = globals()[self.username]['instance_url'] + "/services/Soap/m/{0}.0".format(self.api_version)
        headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "SOAPAction": '""'
        }

        # Populate the soap_body with actual session id
        soap_body = soap_bodies.retrieve_sobjects_workflow_task_body.format(
            globals()[self.username]["session_id"], self.api_version)

        response = requests.post(server_url, soap_body, verify=False, 
            headers=headers)

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.retrieve_all()

        # If status_code is > 399, which means it has error
        content = response.content
        result = {"status_code": response.status_code}
        if response.status_code > 399:
            result["errorCode"] = getUniqueElementValueFromXmlString(content, "errorCode")
            result["message"] = getUniqueElementValueFromXmlString(content, "message")
            self.result = result
            return

        # Get async process id
        async_process_id = getUniqueElementValueFromXmlString(content, "id")
        print ("asyncProcessId: " + async_process_id)

        # 2. issue a check status loop request to assure the async
        # process is done
        result = self.check_status(async_process_id)

        # If check status request failed, this will not be done
        print (result)
        if result["done"] == "Failed":
            self.result = result
            return

        # 3 Obtain zipFile(base64)
        print ("Downloading zipFile in this retrieve result...")
        result = self.check_retrieve_status(async_process_id)
        self.result = result

    def refresh_components(self, component_types):
        """
        Download the specified components

        @component_types: just support ApexPage, ApexComponent, ApexTrigger and ApexClass
        """
        # Firstly Login
        self.login(True)

        # Put totalSize at first item
        component_metadata = {}
        for component_type in component_types:
            component_type_attrs = self.toolingapi_settings[component_type]
            component_outputdir = component_type_attrs["outputdir"]
            component_body = component_type_attrs["body"]
            component_extension = component_type_attrs["extension"]
            component_soql = component_type_attrs["soql"]

            result = self.query_all(component_soql)
            # The users password has expired, you must call SetPassword 
            # before attempting any other API operations
            # Database.com not support ApexComponent
            if result["status_code"] > 399 and component_type == "ApexComponent":
                continue

            if result["status_code"] > 399:
                self.result = result
                return

            size = len(result["records"])
            print (message.SEPRATE.format(str(component_type) + " Size: " + str(size)))
            records = result["records"]

            component_attributes = {}
            for record in records:
                # Get Component Name of this record
                component_name = record['Name']
                component_url = record['attributes']['url']
                component_id = record["Id"]
                print (str(component_type) + " ==> " + str(record['Name']))

                # Write mapping of component_name with component_url
                # into metadata.sublime-settings
                component_attributes[component_name] = {
                    "url": component_url,
                    "id": component_id
                }

                # Get the body
                body = record[component_body]

                # Save Component Body, Component Type to attribute
                component_attributes[component_name]["body"] = component_body
                component_attributes[component_name]["extension"] = component_extension
                component_attributes[component_name]["type"] = component_type

                # Judge Component is Test Class or not
                if component_type == "ApexClass":
                    if "@isTest" in body or "testMethod" in body or\
                        "testmethod" in body or "test" in component_name or\
                        "Test" in component_name:
                        
                        component_attributes[component_name]["is_test"] = True
                    else:
                        component_attributes[component_name]["is_test"] = False

                # Write body to local file
                fp = open(component_outputdir + "/" + component_name +\
                    component_extension, "wb")
                
                try:
                    body = bytes(body, "UTF-8")
                except:
                    body = body.encode("UTF-8")
                fp.write(body)

                # Set status_message
                util.sublime_status_message(component_name + " ["  + component_type + "] Downloaded")

            component_metadata[component_type] = component_attributes

        # Self.result is used to keep thread result
        self.result = component_metadata

    def generate_workbook(self, sobject):
        result = self.describe_sobject(sobject)

        if result["status_code"] > 399:
            sublime.set_timeout(lambda:sublime.status_message(result["message"]), 10)
        else:
            workspace = self.toolingapi_settings.get("workspace")
            outputdir = util.generate_workbook(result, workspace, 
                self.toolingapi_settings.get("workbook_field_describe_columns")) + \
                "/" + sobject + ".csv"
            print (sobject + " workbook outputdir: " + outputdir)

    def save_component(self, component_attribute, body):
        """
        This method contains 5 steps:
        1. Post classid to get MetadataContainerId
        2. Post Component Member
        3. Post ContainerAsyncRequest to get AsyncRequest Id
        4. Get ContainerAsyncRequest Response by Id in step 3
        5. Delete the MetadataContainerId

        Notes: Because if ContainerAsyncRequest has problem, we can't reuse the 
            MetadataContainerId, so we need to delete it and get it every time.

        @component_attribute
        @body: Code content

        """
        # Component Attribute
        component_type = component_attribute["type"]
        component_id = component_attribute["id"]
        component_body = component_attribute["body"]

        # Get MetadataContainerId
        data = {  
            "name": "Save" + component_type[4 : len(component_type)] + component_id
        }
        container_url = '/services/data/v{0}.0/tooling/sobjects/MetadataContainer'.format(self.api_version)
        result = self.post(container_url, data)
        # print ("MetadataContainer Response: ", result)

        # If status_code < 399, it means post succeed
        if result["status_code"] < 399:
            container_id = result.get("id")
        else:
            # If status_code < 399, it means post failed, 
            # If DUPLICATE Container Id, just delete it and restart this function
            if result["errorCode"] == "DUPLICATE_VALUE":
                error_message = result["message"]
                container_id = error_message[error_message.rindex("1dc"): len(error_message)]
                delete_result = self.delete(container_url + "/" + container_id)
                if delete_result["status_code"] < 399:
                    util.sublime_status_message("container_id is deleted.")
                
                # We can't reuse the container_id which caused error
                # Post Request to get MetadataContainerId
                return self.save_component(component_attribute, body)
            else:
                util.sublime_error_message(result)
                return

        # Post ApexComponentMember
        data = {
            "ContentEntityId": component_id,
            "MetadataContainerId": container_id,
            "Body": body
        }
        url = "/services/data/v{0}.0/tooling/sobjects/".format(self.api_version) + component_type + "Member"
        result = self.post(url, data)
        # print ("Post ApexComponentMember: ", result)

        # Post ContainerAsyncRequest
        data = {
            "MetadataContainerId": container_id,
            "isCheckOnly": False
        }
        sync_request_url = '/services/data/v{0}.0/tooling/sobjects/ContainerAsyncRequest'.format(self.api_version)
        result = self.post(sync_request_url, data)
        request_id = result.get("id")
        # print ("Post ContainerAsyncRequest: ", result)

        # Get ContainerAsyncRequest Result
        
        result = self.get(sync_request_url + "/" + request_id)
        state = result["State"]
        # print ("Get ContainerAsyncRequest: ", result)

        return_result = {}
        if state == "Completed":
            return_result = {
                "success": True 
            }

        while state == "Queued":
            # print ("Async Request is queued, please wait for 5 seconds...")
            time.sleep(5)

            result = self.get(sync_request_url + "/" + request_id)
            state = result["State"]
            if state == "Completed":
                return_result = {
                    "success": True 
                }

        if state == "Failed":
            # This error need more process, because of confused single quote
            compile_errors = unescape(result["CompilerErrors"])
            compile_errors = json.loads(compile_errors)
            if len(compile_errors) > 0:
                compile_error = compile_errors[0]
                error_message = "% 20s " % "Name: "
                error_message += "%-20s " % util.none_value(compile_error["name"]) + "\n"
                error_message += "% 20s " % "Problem: "
                error_message += "%-20s " % util.none_value(compile_error["problem"]) + "\n"
                error_message += "% 20s " % "Line: "
                error_message += "%-20s " % str(util.none_value(compile_error["line"]))
            else:
                error_message = result["ErrorMsg"]
            error_message = unescape(error_message, {"&apos;": "'", "&quot;": '"'})
            
            return_result = {
                "success": False,
                "message": error_message
            }

        # Whatever succeed or failed, just delete MetadataContainerId
        delete_result = self.delete(container_url + "/" + container_id)
        status_code = delete_result["status_code"]
        if status_code < 399:
            util.sublime_status_message("container_id is deleted.")

        # Result used in thread invoke
        self.result = return_result