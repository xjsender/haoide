import sublime
import pprint
import json
import time
import datetime
import os

try:
    # Python 3.x
    import urllib.parse
    from .. import requests
    from .. import context

    from . import xmltodict
    from . import soap_bodies
    from . import message
    from . import util
    from .login import soap_login
    from .util import getUniqueElementValueFromXmlString
except:
    # Python 2.x
    import urllib
    import requests
    import context

    import xmltodict
    import soap_bodies
    import message
    import util
    from login import soap_login
    from util import getUniqueElementValueFromXmlString

from xml.sax.saxutils import unescape
from xml.sax.saxutils import quoteattr

SEPRATE = "-" * 100
SESSION_ID_EXPIRED = SEPRATE + "\nInvalid Session or Session Id is expired\n" + SEPRATE + "\n"

class SalesforceApi():
    def __init__(self, toolingapi_settings, **kwargs):
        self.toolingapi_settings = toolingapi_settings
        self.username = toolingapi_settings["username"]
        self.result = None

    def login(self, session_id_expired):
        if self.username + "access_token" not in globals() or session_id_expired:
            instance_url, access_token, server_url, user_id = soap_login(self.toolingapi_settings)
            globals()[self.username + "access_token"] = access_token
            globals()[self.username + "instance_url"] = instance_url
            globals()[self.username + "user_id"] = user_id
            globals()[self.username + "headers"] = {
                "Authorization": "OAuth " + access_token,
                "Content-Type": "application/json; charset=UTF-8",
                "Accept": "application/json"
            }
    
    def get(self, component_url, timeout=120):
        """
        Get component describe result according to component_url

        :component_url: Component URL, for exmaple, /services/data/v28.0/sobjects/Contact/describe
        """
        # Firstly, login
        self.login(False)

        headers = globals()[self.username + "headers"]
        response = requests.get(globals()[self.username + 'instance_url'] + component_url, 
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

        headers = globals()[self.username + "headers"]
        response = requests.post(globals()[self.username + 'instance_url'] + post_url, 
            data = json.dumps(data), verify = False, headers = headers, timeout=timeout)

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            print (SESSION_ID_EXPIRED)
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

        url = globals()[self.username + 'instance_url'] + component_url
        headers = globals()[self.username + "headers"]
        response = requests.delete(url, data = None, verify = False, 
            headers = headers, timeout=timeout)

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            print (SESSION_ID_EXPIRED)
            self.login(True)
            return self.delete(component_url)

        result = {
            "status_code": response.status_code
        }

        if response.status_code > 399:
            response_result = response.json()[0]
            result["errorCode"] = response_result.get("errorCode")
            result["message"] = response_result.get("message")
        
        # Self.result is used to keep thread result
        self.result = result

        # This result is used for invoker
        return result

    def query(self, soql, is_toolingapi=False, timeout=120):
        # Firstly, login
        self.login(False)

        instance_url = globals()[self.username + 'instance_url']
        try:
            soql = urllib.parse.urlencode({'q' : soql})
        except:
            soql = urllib.urlencode({'q' : soql})

        # Just API 28 support CustomField
        if is_toolingapi:
            url = instance_url + '/services/data/v28.0/tooling/query?%s' % soql
        else:
            url = instance_url + '/services/data/v28.0/query?%s' % soql

        response = requests.get(url, data = None, verify = False, timeout=timeout, 
            headers = globals()[self.username + "headers"])
            
        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            print (SESSION_ID_EXPIRED)
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
        all_result = get_all_result(result)

        # Self.result is used to keep thread result
        self.result = result

        # This result is used for invoker
        return result

    def describe_sobject(self, sobject):
        """
        Sends a GET request. Return sobject describe result

        :sobject: sObjectType
        """

        url = "/services/data/v28.0/sobjects/" + sobject + "/describe"
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

        url = "/services/data/v28.0/sobjects/"
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
            "OpportunityLineItem", "Product2", 
            "Task", "User"
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
        while traced_entity_id == None and (self.username + "user_id" not in globals()):
            self.login(True)
            traced_entity_id = globals()[self.username + "user_id"]
            
        # Create Trace Flag
        trace_flag = self.toolingapi_settings["trace_flag"]
        trace_flag["TracedEntityId"] = traced_entity_id

        # We must set the expiration date to next day, 
        # otherwise, the debug log record will not be created 
        nextday = datetime.date.today() + datetime.timedelta(1)
        nextday_str = datetime.datetime.strftime(nextday, "%Y-%m-%d")
        trace_flag["ExpirationDate"] = nextday_str

        post_url = "/services/data/v28.0/tooling/sobjects/TraceFlag"
        result = self.post(post_url, trace_flag)
        print ("Create TraceFlag Result: ", result)

        return result

    def get_debug_log(self, log_id, timeout=120):
        """
        Retrieve a raw log by ID

        :log_id: ApexLogId
        :return: raw data of log
        """

        url = "/services/data/v28.0/sobjects/ApexLog/" + log_id + "/Body"
        headers = globals()[self.username + "headers"]
        response = requests.get(globals()[self.username + 'instance_url'] + url, 
            verify=False, headers=headers, timeout=timeout)

        return response.text

    def run_test(self, class_id, traced_entity_id=None):
        """
        Run Test according to test class_id, return error if has

        :class_id: Apex Test Class Id
        :traced_entity_id: Component Id or User Id
        """
        # Firstly Login
        self.login(False)

        # Create trace flag
        traced_entity_id = globals()[self.username + "user_id"]
        print ("Start creating debug log...")
        self.create_trace_flag(traced_entity_id)

        print ("Start running test...")
        time.sleep(2)
        post_url = "/services/data/v28.0/sobjects/ApexTestQueueItem"
        data = {"ApexClassId": class_id}
        result = self.post(post_url, data)
        
        if result["status_code"] > 399:
            self.result = result
            return
        
        # Wait for the ApexTestQueueItem is over
        print ("Test is in Queue, please wait for 10 seconds......")
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
            print ("Test is still in queued, please continue waiting for 10 seconds.")
            time.sleep(10)
            result = self.query(queue_item_soql)

        test_result_soql = """SELECT ApexClass.Id,ApexClass.Name,ApexLogId,
            AsyncApexJobId,Id,Message,MethodName,Outcome,QueueItemId,StackTrace,
            TestTimestamp FROM ApexTestResult 
            WHERE QueueItemId = '%s'""" % queue_item_id

         # After Test is finished, get result
        result = self.query(test_result_soql)
        result = result["records"]

        # Get Debug Log
        print ("Start retrieve debug log detail...")
        time.sleep(3)
        log_id = result[0]["ApexLogId"]
        if log_id == None:
            debug_log = "Something Happened"
        else:
            debug_log = self.get_debug_log(log_id)
        
        # Combine these two result
        self.result = {
            "test_result": result,
            "debug_log": debug_log
        }

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
        server_url = globals()[self.username + 'instance_url'] + "/services/Soap/u/27.0"
        headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "SOAPAction": '""'
        }
        soap_body = soap_bodies.describe_layout_body.format(
            session_id=globals()[self.username + "access_token"], 
            sobject=sobject, recordtype_id=recordtype_id)

        response = requests.post(server_url, soap_body, verify = False, 
            headers = headers)

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

        server_url = globals()[self.username + 'instance_url'] + "/services/Soap/s/27.0"
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
            session_id=globals()[self.username + "access_token"], 
            apex_string = apex_string)

        response = requests.post(server_url, soap_body, verify = False, 
            headers = headers)

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.execute_anonymous(apex_string)

        # If status_code is > 399, which means it has error
        content = response.content
        result = {"status_code": response.status_code}
        if response.status_code > 399:
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
        pprint.pprint (result)

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
        server_url = globals()[self.username + 'instance_url'] + "/services/Soap/m/28.0"
        headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "SOAPAction": '""'
        }
        soap_body = soap_bodies.check_status_body.format(
            session_id=globals()[self.username + "access_token"],
            async_process_id=async_process_id)

        response = requests.post(server_url, soap_body, verify = False, 
            headers = headers)

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
        server_url = globals()[self.username + 'instance_url'] + "/services/Soap/m/28.0"
        headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "SOAPAction": '""'
        }
        soap_body = soap_bodies.check_retrieve_status_body.format(
            session_id=globals()[self.username + "access_token"],
            async_process_id=async_process_id)

        response = requests.post(server_url, soap_body, verify = False, 
            headers = headers)

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
        server_url = globals()[self.username + 'instance_url'] + "/services/Soap/m/28.0"
        headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "SOAPAction": '""'
        }

        # Populate the soap_body with actual session id
        soap_body = soap_bodies.retrieve_sobjects_workflow_task_body.format(
            session_id=globals()[self.username + "access_token"])

        response = requests.post(server_url, soap_body, verify = False, 
            headers = headers)

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
            size = len(result["records"])
            print (SEPRATE)
            print (str(component_type) + " Size: " + str(size))
            print (SEPRATE)
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
                    "component_url": component_url,
                    "component_id": component_id
                }

                # Get the body
                body = record[component_body]

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

    def save_component(self, data, component_type, component_id, body):
        """
        This method contains 5 steps:
        1. Post classid to get MetadataContainerId
        2. Post Component Member
        3. Post ContainerAsyncRequest to get AsyncRequest Id
        4. Get ContainerAsyncRequest Response by Id in step 3
        5. Delete the MetadataContainerId

        Notes: Because if ContainerAsyncRequest has problem, we can't reuse the 
            MetadataContainerId, so we need to delete it and get it every time.

        @data: {
            "name":  "[SaveClass, SaveTrigger, SaveComponent, SavePage]<ComponentId>"
        }

        @component_type: [SaveClass, SaveTrigger, SaveComponent, SavePage]

        @component_id: component_id

        @body: component body

        @Return: No return result

        """
        # Get MetadataContainerId
        url = '/services/data/v28.0/tooling/sobjects/MetadataContainer'
        result = self.post(url, data)
        print ("MetadataContainer Response: ", result)

        # If status_code < 399, it means post succeed
        status_code = result["status_code"]
        if status_code < 399:
            container_id = result.get("id")
        else:
            # If status_code < 399, it means post failed, 
            # If DUPLICATE Container Id, just delete it and restart this function
            if result["errorCode"] == "DUPLICATE_VALUE":
                # If there has duplicate container_id, just delete it
                # and then, restart it again
                error_message = result["message"]
                container_id = error_message[error_message.rindex("1dc"): len(error_message)]
                url = '/services/data/v28.0/tooling/sobjects/MetadataContainer/' + container_id

                delete_result = self.delete(url)
                status_code = delete_result["status_code"]
                if status_code < 399:
                    util.sublime_status_message("container_id is deleted.")
                
                # Restart this function
                self.save_component(data, component_type, component_id, body)
            else:
                util.sublime_error_message(result)
                return

        # Post ApexComponentMember
        data = {
            "ContentEntityId": component_id,
            "MetadataContainerId": container_id,
            "Body": body
        }
        url = "/services/data/v28.0/tooling/sobjects/" + component_type + "Member"

        result = self.post(url, data)
        print ("Post ApexComponentMember: ", result)

        # Post ContainerAsyncRequest
        data = {
            "MetadataContainerId": container_id,
            "isCheckOnly": False
        }
        url = '/services/data/v28.0/tooling/sobjects/ContainerAsyncRequest'
        result = self.post(url, data)
        request_id = result.get("id")
        print ("Post ContainerAsyncRequest: ", result)

        # Get ContainerAsyncRequest Result
        url = '/services/data/v28.0/tooling/sobjects/ContainerAsyncRequest/' + request_id

        result = self.get(url)
        state = result["State"]
        print ("Get ContainerAsyncRequest: ")
        pprint.pprint (result)

        if state == "Completed":
            sublime.message_dialog(message.DEPLOY_SUCCESSFULLY)
        elif state == "Queued":
            while (state == "Queued"):
                print ("Async Request is queued, please wait for 5 seconds.....")
                time.sleep(5)

                result = self.get(url)
                state = result["State"]
                print ("async_request_get_response State: ", state)

                if state == "Completed":
                    sublime.message_dialog(message.DEPLOY_SUCCESSFULLY)

        if state == "Failed":
            # This error need more process, because of confused single quote
            compile_errors = unescape(result["CompilerErrors"])
            print ("compile_errors: ", compile_errors)

            # encode compile_errors from unicode to json format
            compile_errors = json.loads(compile_errors)

            for compile_error in compile_errors:
                # Parse compile_error
                extend = compile_error["extent"]
                line = compile_error["line"]
                problem = compile_error["problem"]
                name = compile_error["name"]
                error_message = extend + ": " + name + " has problem: " +\
                    problem + " at line " + str(line)
                error_message = unescape(error_message, {"&apos;": "'", "&quot;": '"'})

                # Show message
                print (SEPRATE)
                print (error_message)
                print (SEPRATE + "\n")
                sublime.message_dialog(error_message)

        # Whatever succeed or failed, just delete MetadataContainerId
        url = '/services/data/v28.0/tooling/sobjects/MetadataContainer/' + container_id
        result = self.delete(url)

        status_code = result["status_code"]
        print ("Delete MetadataContainerId: ", status_code)
        if status_code < 399:
            util.sublime_status_message("container_id is deleted.")