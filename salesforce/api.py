import sublime
import pprint
import json
import time
import datetime
import os
import re

import urllib.parse
from .. import requests
from .. import context
from .. import util

from . import xmltodict, soap_bodies, message

from ..util import getUniqueElementValueFromXmlString
from .login import soap_login
from xml.sax.saxutils import unescape, quoteattr

class SalesforceApi():
    def __init__(self, settings, **kwargs):
        self.settings = settings
        self.api_version = settings["api_version"]
        self.username = settings["username"]
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
            if result["status_code"] > 399:
                result["default_project"] = self.settings["default_project"]["project_name"]
                self.result = result
                return False

            result["headers"] = {
                "Authorization": "OAuth " + result["session_id"],
                "Content-Type": "application/json; charset=UTF-8",
                "Accept": "application/json"
            }
            globals()[self.username] = result
        else:
            result = globals()[self.username]

        self.headers = globals()[self.username]["headers"]
        self.instance_url = result["instance_url"]
        self.base_url = self.instance_url + "/services/data/v%s.0" % self.api_version
        self.partner_url = self.instance_url + "/services/Soap/u/%s.0" % self.api_version
        self.metadata_url = self.instance_url + "/services/Soap/m/%s.0" % self.api_version
        self.apex_url = self.instance_url + "/services/Soap/s/%s.0" % self.api_version
        self.result = result
        return result

    def parse_url(self, component_url):
        """ Return the valid salesforce REST URI by specified url

        Arguments:

        * component_url -- the rest URI, this method is designed for `Execute Rest Test` command

        Returns:

        * url -- the valid salesforce REST URI
        """
        if "https://" in component_url:
            url = component_url
        elif "/services" in component_url:
            url = self.instance_url + component_url
        else:
            url = self.base_url + component_url

        return url

    def parse_response(self, res):
        """ parse the response with json format

        Arguments:

        * res -- response by request

        Returns:

        * response_result -- json formatted response
        """
        if res.status_code > 399:
            try:
                response_result = res.json()
                if isinstance(response_result, list):
                    response_result = response_result[0]
            except:
                response_result = {"errorMessage": res.text}

            response_result["url"] = res.url
        else:
            try:
                response_result = {}
                if isinstance(res.json(), list):
                    response_result["list"] = res.json()
                elif isinstance(res.json(), dict):
                    response_result = res.json()
            except:
                response_result = {}

        response_result["status_code"] = res.status_code
        return response_result
        
    def head(self, component_url, timeout=120):
        """ 'head' request

        Arguments:

        * component_url -- REST URI
        """
        # Firstly, login
        self.login()

        url = self.parse_url(component_url)
        response = requests.head(url, verify=False, 
            headers=self.headers, timeout=timeout)

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.head(component_url)
        
        result = self.parse_response(response)
        self.result = result

        # This result is used for invoker
        return result

    def get(self, component_url, timeout=120):
        """ 'get' request

        Arguments:

        * component_url -- REST URI
        """
        # Firstly, login
        self.login()

        url = self.parse_url(component_url)
        response = requests.get(url, data=None, verify=False, 
            headers=self.headers, timeout=timeout)

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.get(component_url)
        
        result = self.parse_response(response)
        self.result = result

        # This result is used for invoker
        return result

    def put(self, put_url, data, timeout=120):
        """ 'put' request

        Arguments:

        * put_url -- REST URI
        * data -- form data needed to send to server
        """
        # Firstly, login
        self.login()

        url = self.parse_url(put_url)
        response = requests.put(url, data=json.dumps(data), verify=False, 
            headers=self.headers, timeout=timeout)

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.put(put_url, data)
        
        result = self.parse_response(response)
        self.result = result

        # This result is used for invoker
        return result

    def patch(self, patch_url, data, timeout=120):
        """ 'patch' request

        Arguments:

        * patch_url -- REST URI
        * data -- form data needed to send to server
        """
        # Firstly, login
        self.login()

        url = self.parse_url(patch_url)
        response = requests.patch(url, data=json.dumps(data), verify=False, 
            headers=self.headers, timeout=timeout)

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.patch(patch_url, data)
        
        result = self.parse_response(response)
        self.result = result

        # This result is used for invoker
        return result

    def post(self, post_url, data, timeout=120):
        """ 'post' request

        Arguments:

        * post_url -- REST URI
        * data -- form data needed to send to server
        """
        # Firstly, login
        self.login()

        url = self.parse_url(post_url)
        response = requests.post(url, data=json.dumps(data), verify=False,
            headers=self.headers, timeout=timeout)

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.post(post_url, data)
        
        result = self.parse_response(response)
        self.result = result

        # This result is used for invoker
        return result

    def delete(self, component_url, timeout=120):
        """ 'delete' request

        Arguments:

        * component_url -- REST URI
        """
        # Firstly, login
        self.login()

        url = self.parse_url(component_url)
        response = requests.delete(url, data=None, verify=False, 
            headers=self.headers, timeout=timeout)

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.delete(component_url)

        result = self.parse_response(response)
        self.result = result

        # This result is used for invoker
        return result

    def search(self, sosl, timeout=120):
        """ Returns the result of a Salesforce search as a dict decoded from
            the Salesforce response JSON payload.

        Arguments:

        * search -- the fully formatted SOSL search string, e.g.
                    `FIND {test}`
        """

        # Firstly, login
        self.login()

        sosl = urllib.parse.urlencode({'q' : sosl})
        url = self.base_url + "/search?" + sosl
        if "search?q=q=" in url: url.replace("search?q=q=", "search?q=")

        response = requests.get(url, data=None, verify=False, 
            headers=self.headers, timeout=timeout)
            
        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.search(sosl)

        result = self.parse_response(response)
        self.result = result
        return self.result

    def quick_search(self, sosl_string, timeout=120):
        """ Returns the result of a Salesforce search as a dict decoded from
            the Salesforce response JSON payload.

        Arguments:

        * search -- the non-SOSL search string, e.g. `test`. This search
                    string will be wrapped to read `FIND {test}` before being
                    sent to Salesforce
        """

        sosl_string = 'FIND {%s}' % sosl_string
        result = self.search(sosl_string)
        self.result = result
        return self.result

    def query(self, soql, is_toolingapi=False, timeout=120):
        """ Returns the result of a Salesforce query as a dict decoded from
            the Salesforce response JSON payload.

        Arguments:

        * soql -- the query string, e.g. SELECT Id FROM Account
        *
        """
        # Firstly, login
        self.login()

        # Check whether * in field list
        match = re.compile("select\s+\*\s+from[\s\t]+\w+", re.I).match(soql)
        if match:
            literals = match.group().split()
            sobject = literals[-1]
            result = self.describe_sobject(sobject, is_toolingapi)
            if result["status_code"] < 399:
                fields = [f["name"] for f in result["fields"]]
                soql = soql.replace("*", ",".join(fields))
            else:
                soql = soql.replace("*", "Id")

        # Just API 28 above support CustomField
        soql = urllib.parse.quote(soql)
        url = self.base_url + ("/tooling" if is_toolingapi else "") + "/query?q=" + soql

        # Here has a bug, this is used to prevent this exception
        if "query?q=q=" in url: url = url.replace("query?q=q=", "query?q=")

        response = requests.get(url, data=None, verify=False, 
            headers=self.headers, timeout=timeout)
            
        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.query(soql)

        result = self.parse_response(response)
        self.result = result

        # This result is used for invoker
        return result

    def query_more(self, nextRecordUrl, is_toolingapi=False):
        return self.get(nextRecordUrl)

    def query_all(self, soql, is_toolingapi=False, timeout=120):
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

        if not self.login(): return

        soql = urllib.parse.urlencode({'q' : soql})
        url = self.base_url + ("/tooling" if is_toolingapi else "") + "/queryAll?" + soql
        response = requests.get(url, data=None, verify=False, 
            headers=self.headers, timeout=timeout)

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.query_all(soql)

        result = self.parse_response(response)
        
        # Database.com not support ApexComponent
        if result["status_code"] > 399: 
            self.result = result
            return result

        all_result = get_all_result(result)

        # Self.result is used to keep thread result
        self.result = all_result

        # This result is used for invoker
        return all_result

    def combine_soql(self, sobject, contains_compound=True):
        """ Get the full field list soql by sobject

        * sobject -- sobject name, for example, Account, Contact
        """
        result = self.describe_sobject(sobject)
        fields = sorted(result["fields"], key=lambda k : k['custom'])
        sobject_fields = ""
        for field in fields:
            # http://www.salesforce.com/us/developer/docs/api/Content/compound_fields_address.htm
            if not contains_compound and field.get("queryByDistance"): continue
            sobject_fields += field.get("name") + ", "

        self.result = {
            "status_code": result["status_code"],
            "soql": 'SELECT ' + sobject_fields[ : -2] + ' FROM ' + sobject
        }
        return self.result

    def describe_sobject(self, sobject, is_toolingapi=False):
        """ Sends a GET request. Return sobject describe result

        :sobject: sObjectType
        """

        url = ("/tooling" if is_toolingapi else "") + "/sobjects/%s/describe" % sobject
        result = self.get(url)

        # Self.result is used to keep thread result
        self.result = result

        # This result is used for invoker
        return result

    def describe_global(self):
        """ Sends a GET request. Return global describe

        Returns:

        * * -- sobjects describe dict
        """

        result = {}
        sobjects_describe = self.get("/sobjects").get("sobjects")
        for sobject_describe in sobjects_describe:
            if "name" in sobject_describe:
                result[sobject_describe["name"]] = sobject_describe
        self.result = result
        return self.result

    def create_trace_flag(self, traced_entity_id=None):
        """ Create Debug Log Trace by traced_entity_id

        Arguments:

        * traced_entity_id -- Optional; Component Id or User Id
        """

        # If traced_entity_id is none, just set it as current user
        while not traced_entity_id and (self.username not in globals()):
            self.login(True)
            traced_entity_id = globals()[self.username]["user_id"]

        # Check whether traced user already has trace flag
        # If not, just create it for him/her
        time_stamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime(time.time()))
        query = "SELECT Id, ExpirationDate FROM TraceFlag " +\
                "WHERE TracedEntityId = '%s' AND ExpirationDate >= %s" % (traced_entity_id, time_stamp)
        result = self.query(query, True)

        # If trace flag is exist, just delete it
        if result["totalSize"] > 0:
            self.delete("/tooling/sobjects/TraceFlag/" + result["records"][0]["Id"])
            return self.create_trace_flag(traced_entity_id)

        # Create Trace Flag
        trace_flag = self.settings["trace_flag"]
        trace_flag["TracedEntityId"] = traced_entity_id

        # We must set the expiration date to next day, 
        # otherwise, the debug log record will not be created 
        nextday = datetime.date.today() + datetime.timedelta(1)
        nextday_str = datetime.datetime.strftime(nextday, "%Y-%m-%d")
        trace_flag["ExpirationDate"] = nextday_str
        post_url = "/tooling/sobjects/TraceFlag"
        result = self.post(post_url, trace_flag)

        result["message"] = "TraceFlag creation succeed"
        self.result = result
        return result

    def retrieve_body(self, retrieve_url, timeout=120):
        """ Retrieve a raw log by ID

        Arguments:

        * retrieve_url -- retrieve url

        Returns:

        * raw data -- raw data of log
        """
        # Firstly Login
        self.login()

        url = self.parse_url(retrieve_url)
        headers = self.headers.copy()
        headers["Accept-Encoding"] = 'identity, deflate, compress, gzip'
        print (time.strftime("StartTime: %Y-%m-%d %H:%M:%S", time.localtime(time.time())))
        response = requests.get(url, verify=False, headers=headers, timeout=timeout)
        print (time.strftime("End  Time: %Y-%m-%d %H:%M:%S", time.localtime(time.time())))

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.retrieve_body(retrieve_url)

        result = {
            "status_code": response.status_code,
            "body": response.text
        }
        self.result = result
        return result

    def run_tests_asynchronous(self, class_ids):
        """ Run asynchronous test for specified class ids

        Arguments:

        * class_ids -- Apex Test Class Id List
        """
        url = "/tooling/runTestsAsynchronous/?classids=" + ",".join(class_ids)
        self.result = self.get(url)
        return self.result

    def run_tests_synchronous(self, class_names):
        """ Run synchronous test for specified class ids

        Arguments:

        * class_names -- Apex Test Class Name List
        """
        url = "/tooling/runTestsSynchronous/?classnames=" + ",".join(class_names)
        self.result = self.get(url)
        return self.result

    def run_test(self, class_id):
        """ Run Test according to test class_id, return error if has

        Arguments:

        * class_id -- Apex Test Class Id
        * traced_entity_id -- Component Id or User Id
        """
        # Firstly Login
        self.login()

        traced_entity_id = globals()[self.username]["user_id"]
        self.create_trace_flag(traced_entity_id)

        time.sleep(2)
        data = {"ApexClassId": class_id}
        result = self.post("/sobjects/ApexTestQueueItem", data)
        
        if result["status_code"] > 399:
            self.result = result
            return
        
        # Wait for the ApexTestQueueItem is over
        time.sleep(5)
        queue_item_id = result["id"]
        queue_item_soql = "SELECT Id, Status FROM ApexTestQueueItem WHERE Id='%s'" % queue_item_id
        result = self.query(queue_item_soql)

        if result["status_code"] > 399:
            self.result = result
            return
        
        # If totalSize is Zero, it means we need to wait until test is finished
        while result["totalSize"] == 0 or result["records"][0]["Status"] in ["Queued", "Processing"]:
            time.sleep(5)
            result = self.query(queue_item_soql)

        test_result_soql = """SELECT ApexClass.Id,ApexClass.Name,ApexLogId,
            AsyncApexJobId,Id,Message,MethodName,Outcome,QueueItemId,StackTrace,
            TestTimestamp FROM ApexTestResult WHERE QueueItemId = '%s'""" % queue_item_id

         # After Test is finished, get result
        result = self.query(test_result_soql)
        result = result["records"]
        
        # Combine these two result
        self.result = result

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

        response = requests.post(self.partner_url, soap_body, verify=False, 
            headers=headers)

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

        result["status_code"] = response.status_code

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
                "Error Code": "Customize",
                "status_code": 500
            }
            self.result = result
            return self.result

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
        """ Ensure the retrieve request is done and then we can 
            continue other work

        * async_process_id -- retrieve request asyncProcessId
        """

        # Check the status of retrieve job
        headers = {
            "Content-Type": "text/xml;charset=UTF-8",
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
            result["errorCode"] = getUniqueElementValueFromXmlString(content, "errorCode")
            result["message"] = getUniqueElementValueFromXmlString(content, "message")
            result["done"] = "Failed"
            result["status_code"] = response.status_code
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

        result["status_code"] = response.status_code
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
        result = {"status_code": response.status_code}
        if response.status_code > 399:
            result["errorCode"] = getUniqueElementValueFromXmlString(content, "errorCode")
            result["message"] = getUniqueElementValueFromXmlString(content, "message")
            return result

        result["zipFile"] = getUniqueElementValueFromXmlString(content, "zipFile")
        return result

    def retrieve(self, soap_body):
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
        # Firstly Login
        self.login()

        # 1. Issue a retrieve request to start the asynchronous retrieval
        headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "SOAPAction": '""'
        }

        # Populate the soap_body with actual session id
        soap_body = soap_body.format(
            globals()[self.username]["session_id"], self.api_version)

        response = requests.post(self.metadata_url, soap_body, verify=False, 
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
        result["CurrenTime"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        view = sublime.active_window().new_file()
        header = "Progress Monitor: Retrieve Metadata Status(Keep This View Open, Auto Refreshed Every 6 seconds)"
        view.run_command("new_dynamic_view", {
            "view_name": "Progress Monitor: Retrieve Metadata",
            "input": util.format_waiting_message(result, header)
        })
        while result["done"] == "false":
            time.sleep(5)
            result = self.check_status(async_process_id)
            result["CurrenTime"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            view.run_command("new_dynamic_view", {
                "view_id": view.id(),
                "view_name": "Progress Monitor: Retrieve Metadata",
                "input": util.format_waiting_message(result, header),
                "erase_all": True
            })
        # If check status request failed, this will not be done
        if result["done"] == "Failed":
            self.result = result
            return

        # 3 Obtain zipFile(base64)
        sublime.set_timeout(lambda:sublime.status_message("Downloading zipFile"), 10)
        view.run_command("new_dynamic_view", {
            "view_id": view.id(),
            "view_name": "Progress Monitor: Retrieve Metadata",
            "input": message.SEPRATE.format("Downloading the zipFile, it will be very time-consuming"),
            "point": view.size()
        })
        result = self.check_retrieve_status(async_process_id)
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
        result = {"status_code": response.status_code}
        if response.status_code > 399:
            result["errorCode"] = getUniqueElementValueFromXmlString(content, "errorCode")
            result["message"] = getUniqueElementValueFromXmlString(content, "message")
            return result

        result = xmltodict.parse(content)
        try:
            result = result["soapenv:Envelope"]["soapenv:Body"]["checkDeployStatusResponse"]["result"]
        except (KeyError):
            result = {
                "errorCode": "Convert Xml to Dict Exception",
                "message": 'body["checkDeployStatusResponse"]["result"] KeyError'
            }

        result["status_code"] = response.status_code
        return result
        
    def deploy_metadata(self, zipfile):
        """ Deploy zip file

        Arguments:

        * zipFile -- base64 encoded zipfile 
        """
        # Firstly Login
        self.login()

        # 1. Issue a retrieve request to start the asynchronous retrieval
        headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "SOAPAction": '""'
        }

        # Populate the soap_body with actual session id
        deploy_options = self.settings["deploy_options"]
        soap_body = soap_bodies.deploy_package.format(
            globals()[self.username]["session_id"], 
            util.base64_zip(zipfile),
            deploy_options["allowMissingFiles"],
            deploy_options["autoUpdatePackage"],
            deploy_options["checkOnly"],
            deploy_options["ignoreWarnings"],
            deploy_options["performRetrieve"],
            deploy_options["purgeOnDelete"],
            deploy_options["rollbackOnError"],
            deploy_options["runAllTests"],
            deploy_options["runTests"],
            deploy_options["singlePackage"])
        response = requests.post(self.metadata_url, soap_body, verify=False, 
            headers=headers)

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.deploy_metadata()

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
            return

        # Get async process id
        async_process_id = getUniqueElementValueFromXmlString(content, "id")
        print ("asyncProcessId: " + async_process_id)

        # 2. issue a check status loop request to assure the async
        # process is done
        result = self.check_status(async_process_id)
        result["CurrenTime"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        view = sublime.active_window().new_file()
        header = "Deploy Metadata Status(Keep This View Open, Auto Refreshed Every 6 seconds)"
        view.run_command("new_dynamic_view", {
            "view_id": view.id(),
            "view_name": "Progress Monitor: Deploy Metadata",
            "input": util.format_waiting_message(result, header)
        })
        while result["done"] == "false":
            time.sleep(5)
            result = self.check_status(async_process_id)
            result["CurrenTime"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            view.run_command("new_dynamic_view", {
                "view_id": view.id(),
                "view_name": "Progress Monitor: Deploy Metadata",
                "input": util.format_waiting_message(result, header),
                "erase_all": True
            })

        self.result = result

        # Display Deploy Result
        result = self.check_deploy_status(async_process_id)
        view.run_command("new_dynamic_view", {
            "view_id": view.id(),
            "view_name": "Deploy Metadata Status",
            "input": util.format_waiting_message(result, "Deploy Result") + "\n",
            "point": view.size()
        })

    def refresh_components(self, component_types):
        """ Download the specified components

        Arguments:

        * component_types -- Just support ApexPage, ApexComponent, ApexTrigger and ApexClass
        """
        # Firstly Login
        self.login(True)

        # Put totalSize at first item
        component_metadata = {}
        for component_type in component_types:
            component_type_attrs = self.settings[component_type]
            component_outputdir = component_type_attrs["outputdir"]
            component_body = component_type_attrs["body"]
            component_extension = component_type_attrs["extension"]
            component_soql = component_type_attrs["soql"]

            result = self.query_all(component_soql)
            # The users password has expired, you must call SetPassword 
            # before attempting any other API operations
            # Database.com not support StaticResource, ApexComponent and ApexPage
            if not result: return
            if result["status_code"] == 400: continue

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

                # If Component Type is StaticResource,
                if component_type == "StaticResource":
                    component_attributes[component_name]["ContentType"] = record['ContentType']

                # Judge Component is Test Class or not
                if component_type == "ApexClass":
                    if "@istest" in body.lower() or "testmethod" in body.lower():
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
                sublime.set_timeout(lambda:sublime.status_message(component_name +\
                    " ["  + component_type + "] Downloaded"), 10)

            component_metadata[component_type] = component_attributes

        # Self.result is used to keep thread result
        self.result = component_metadata

    def generate_workbook(self, sobject):
        """ Generate CSV for Sobject Workbook

        Arguments:

        * sobject -- sobject name
        """
        result = self.describe_sobject(sobject)

        if result["status_code"] > 399:
            sublime.set_timeout(lambda:sublime.status_message(result["message"]), 10)
        else:
            workspace = self.settings.get("workspace")
            outputdir = util.generate_workbook(result, workspace, 
                self.settings.get("workbook_field_describe_columns")) + \
                "/" + sobject + ".csv"
            print (sobject + " workbook outputdir: " + outputdir)

    def save_component(self, component_attribute, body, is_check_only):
        """ This method contains 5 steps:
            1. Post classid to get MetadataContainerId
            2. Post Component Member
            3. Post ContainerAsyncRequest to get AsyncRequest Id
            4. Get ContainerAsyncRequest Response by Id in step 3
            5. Delete the MetadataContainerId

        Notes: Because if ContainerAsyncRequest has problem, we can't reuse the 
            MetadataContainerId, so we need to delete it and get it every time.

        Arguments:

        * component_attribute - attribute of component, e.g., component id, url
        * body -- Code content
        * is_check_only -- indicate compile or save
        """

        # Component Attribute
        component_type = component_attribute["type"]
        component_id = component_attribute["id"]
        component_body = component_attribute["body"]

        if self.settings["check_save_conflict"]:
            query = "SELECT Id, LastModifiedById, LastModifiedDate " +\
                    "FROM %s WHERE Id = '%s'" % (component_type, component_id)
            result = self.query(query, True)
            user_id = globals()[self.username]["user_id"]
            class_attr = result["records"][0]
            if not class_attr["LastModifiedById"] == user_id:
                last_modified_id = class_attr["LastModifiedById"]
                last_modified_date = class_attr["LastModifiedDate"]
                message = "Modified at %s, continue?" % last_modified_date
                confirm = sublime.ok_cancel_dialog(message)
                if confirm == False: return

        # Get MetadataContainerId
        data = {  
            "name": "Save" + component_type[4 : len(component_type)] + component_id
        }
        container_url = "/tooling/sobjects/MetadataContainer"
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
                    sublime.set_timeout(lambda:sublime.status_message("container_id is deleted."), 10)
                else:
                    self.result = delete_result
                    return delete_result
                
                # We can't reuse the container_id which caused error
                # Post Request to get MetadataContainerId
                return self.save_component(component_attribute, body)

        # Post ApexComponentMember
        data = {
            "ContentEntityId": component_id,
            "MetadataContainerId": container_id,
            "Body": body
        }
        url = "/tooling/sobjects/" + component_type + "Member"
        member_result = self.post(url, data)
        # print ("Post ApexComponentMember: ", result)

        # Post ContainerAsyncRequest
        data = {
            "MetadataContainerId": container_id,
            "IsCheckOnly": is_check_only,
            "IsRunTests": False
        }
        sync_request_url = '/tooling/sobjects/ContainerAsyncRequest'
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
                    "success": True,
                }

        if state == "Failed":
            # This error need more process, because of confused single quote
            compile_errors = unescape(result["CompilerErrors"])
            compile_errors = json.loads(compile_errors)
            return_result = {}
            if len(compile_errors) > 0:
                return_result = compile_errors[0]
            else:
                return_result["Error Message"] = result["ErrorMsg"]
            
            return_result["success"] =  False
        
        if return_result["success"]:
            query = "SELECT Id, SymbolTable " +\
                    "FROM ApexClassMember WHERE Id ='%s'" % member_result["id"]
            member = self.query(query, True)
            if member["records"]:
                return_result["symbol_table"] = member["records"][0]["SymbolTable"]

        # Whatever succeed or failed, just delete MetadataContainerId
        delete_result = self.delete(container_url + "/" + container_id)

        # Result used in thread invoke
        self.result = return_result