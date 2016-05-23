import sublime
import pprint
import json
import time
import datetime
import os
import re

import urllib.parse
from xml.sax.saxutils import unescape

from ... import requests, util, context
from ..login import soap_login
from ..lib.panel import Printer

class ToolingApi():
    def __init__(self, settings, **kwargs):
        self.settings = settings
        self.api_version = settings["api_version"]
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
        result = soap_login(self.settings, session_id_expired)
        if not result["success"]:
            self.result = result
            return self.result

        self.session = result
        self.headers = result["headers"]
        self.instance_url = result["instance_url"]
        self.base_url = self.instance_url + "/services/data/v%s.0" % self.api_version

        self.result = result
        return result

    def parse_url(self, component_url):
        """ Return the valid salesforce REST URI by specified url

        Arguments:

        * component_url -- the rest URI, this method is designed for `Execute Rest Test` command

        Returns:

        * url -- the valid salesforce REST URI
        """
        # Before parse, trip first
        component_url = component_url.strip()

        if "https://" in component_url:
            url = component_url
        elif "/services" in component_url:
            url = self.instance_url + component_url
        elif component_url.startswith("/apexrest"):
            url = self.instance_url + "/services" + component_url
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
                response_result = {"Error Message": res.text}
            response_result["success"] = False
        else:
            response_result = {}
            try:
                if isinstance(res.json(), list):
                    response_result["list"] = res.json()
                elif isinstance(res.json(), dict):
                    response_result = res.json()
                else:
                    response_result["str"] = res.text
            except:
                response_result["str"] = res.text
            response_result["success"] = True

        return response_result
        
    def head(self, component_url, timeout=120):
        """ 'head' request

        Arguments:

        * component_url -- REST URI
        """
        # Firstly, login
        result = self.login()
        if not result["success"]:
            self.result = result
            return self.result

        url = self.parse_url(component_url)
        try:
            response = requests.head(url, verify=False, 
                headers=self.headers, timeout=timeout)
        except requests.exceptions.RequestException as e:
            self.result = {
                "Error Message":  "Network connection timeout when issue REST HEAD request",
                "success": False
            }
            return self.result

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            result = self.login(True)
            if not result["success"]:
                self.result = result
                return self.result
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
        result = self.login()
        if not result["success"]:
            self.result = result
            return self.result

        url = self.parse_url(component_url)
        headers = self.headers.copy()
        headers["Accept-Encoding"] = 'identity, deflate, compress, gzip'

        try:
            response = requests.get(url, data=None, verify=False, 
                headers=self.headers, timeout=timeout)
        except requests.exceptions.RequestException as e:
            self.result = {
                "Error Message":  "Network connection timeout when issuing REST GET request",
                "success": False
            }
            return self.result

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            result = self.login(True)
            if not result["success"]:
                self.result = result
                return self.result
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
        result = self.login()
        if not result["success"]:
            self.result = result
            return self.result

        url = self.parse_url(put_url)
        
        try:
            response = requests.put(url, data=json.dumps(data), verify=False, 
                headers=self.headers, timeout=timeout)
        except requests.exceptions.RequestException as e:
            self.result = {
                "Error Message":  "Network Network connection timeout when issuing REST PUT request",
                "success": False
            }
            return self.result

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            result = self.login(True)
            if not result["success"]:
                self.result = result
                return self.result
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
        result = self.login()
        if not result["success"]:
            self.result = result
            return self.result

        url = self.parse_url(patch_url)
        
        try:
            response = requests.patch(url, data=json.dumps(data), verify=False, 
                headers=self.headers, timeout=timeout)
        except requests.exceptions.RequestException as e:
            self.result = {
                "Error Message":  "Network connection timeout when issuing REST PATCH request",
                "success": False
            }
            return self.result

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            result = self.login(True)
            if not result["success"]:
                self.result = result
                return self.result
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
        result = self.login()
        if not result["success"]:
            self.result = result
            return self.result

        url = self.parse_url(post_url)
        
        try:
            response = requests.post(url, data=json.dumps(data), verify=False, 
                headers=self.headers, timeout=timeout)
        except requests.exceptions.RequestException as e:
            self.result = {
                "Error Message":  "Network connection timeout when issuing REST POST request",
                "success": False
            }
            return self.result

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            result = self.login(True)
            if not result["success"]:
                self.result = result
                return self.result
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
        result = self.login()
        if not result["success"]:
            self.result = result
            return self.result

        url = self.parse_url(component_url)
        
        try:
            response = requests.delete(url, data=None, verify=False, 
                headers=self.headers, timeout=timeout)
        except requests.exceptions.RequestException as e:
            self.result = {
                "Error Message":  "Network connection timeout when issuing REST DELETE request",
                "success": False
            }
            return self.result

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            result = self.login(True)
            if not result["success"]:
                self.result = result
                return self.result
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
        result = self.login()
        if not result["success"]:
            self.result = result
            return self.result

        url = self.base_url + "/search"
        params = {'q' : sosl}
        try:
            response = requests.get(url, headers=self.headers, verify=False, 
                params=params, timeout=timeout)
        except requests.exceptions.RequestException as e:
            self.result = {
                "Error Message":  "Network connection timeout when issuing REST SEARCH request",
                "success": False
            }
            return self.result

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            result = self.login(True)
            if not result["success"]:
                self.result = result
                return self.result
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

        # If sosl_string contains ``-``, MALFORMED_SEARCH exception
        # We need to escape this special character,
        # Don't know why ?, _
        for ch in ["-", "?", "*"]:
            sosl_string = sosl_string.replace(ch, "\\"+ch)

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
        result = self.login()
        if not result["success"]:
            self.result = result
            return self.result

        # Check whether * in field list
        match = re.compile("select\s+\*\s+from[\s\t]+\w+", re.I).match(soql)
        if match:
            literals = match.group().split()
            sobject = literals[-1]
            result = self.describe_sobject(sobject, is_toolingapi)
            if result["success"]:
                fields = [f["name"] for f in result["fields"]]
                soql = soql.replace("*", ",".join(fields))
            else:
                soql = soql.replace("*", "Id")

        # Just API 28 above support CustomField
        url = self.base_url + ("/tooling" if is_toolingapi else "") + "/query"
        params = {'q' : soql}

        try:
            response = requests.get(url, data=None, verify=False, params=params,
                headers=self.headers, timeout=timeout)
        except requests.exceptions.RequestException as e:
            self.result = {
                "Error Message":  "Network connection timeout when issuing QUERY request",
                "success": False
            }
            return self.result

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            result = self.login(True)
            if not result["success"]:
                self.result = result
                return self.result
            return self.query(soql, is_toolingapi)

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
                # Include the new list of records with the previous list
                previous_result['records'].extend(result['records'])
                result['records'] = previous_result['records']

                # Continue the recursion
                return get_all_result(result)

        if not self.login(): return

        result = self.query(soql, is_toolingapi)
        
        # Database.com not support ApexComponent
        if not result["success"]:
            self.result = result
            return result

        all_result = get_all_result(result)

        # Self.result is used to keep thread result
        self.result = all_result

        # This result is used for invoker
        return all_result

    def query_symbol_table(self, split=30):
        """ Some Tooling Sobject doesn't support query all, for example, ApexClass,
            If we query all ApexClasses, SymbolTable attribute will be null, however, 
            if we query for 200 records at once, SymbolTable will have value

            ** Just query classes in unmanaged package since 2016.3.23
        """

        # Login firstly
        result = self.login();

        # Exception Process
        if not result["success"]:
            self.result = result
            return self.result
        
        offset = 0
        result = {"totalSize": 0, "records": [], "success": result["success"]}
        describe_metadata = util.get_described_metadata(self.settings)
        namespacePrefix = describe_metadata.get("organizationNamespace", '')
        soql =  "SELECT NamespacePrefix, SymbolTable, Name FROM ApexClass " +\
                "WHERE NamespacePrefix = %s " % (
                   "'%s'" % namespacePrefix if namespacePrefix else 'null'
                )
        while True:
            query = soql + "LIMIT %s OFFSET %s""" % (split, offset)
            previous_result = self.query(query, is_toolingapi=True)
            if not previous_result["success"]: continue # Ignore exception
            if previous_result["size"] == 0: break # No result
            if self.settings["debug_mode"]:
                print ('SOQL: %s, ' % query, 'totalSize: %s' % previous_result["size"])
            result['totalSize'] += previous_result['totalSize']
            previous_result['records'].extend(result['records'])
            result['records'] = previous_result['records']
            offset += split
        
        # Invoke for thread
        self.result = result

        # This result is used for invoker
        return self.result

    def query_logs(self, last_n_logs, user_id=None):
        """ Query the latest logs of user

        * last_n_logs -- Latest number of logs
        """

        # Login firstly
        self.login()

        # If user_id is empty, just use current user id
        if not user_id: user_id = self.session["user_id"]

        # Query self logs
        soql = "SELECT Id,LogUserId,LogLength,Request,Operation,Application," +\
            "Status,DurationMilliseconds,StartTime,Location FROM ApexLog " +\
            "WHERE LogUserId='%s' ORDER BY StartTime DESC LIMIT %s" % (user_id, last_n_logs)

        self.result = self.query(soql, is_toolingapi=True)
        return self.result

    def combine_soql(self, sobject, action=None, contains_compound=True):
        """ Get the full field list soql by sobject

        * sobject -- sobject name, for example, Account, Contact
        """
        result = self.describe_sobject(sobject)

        # Exception Process
        if not result["success"]:
            self.result = result
            return self.result

        fields = sorted(result["fields"], key=lambda k : k['custom'])
        field_list = []
        for field in fields:
            # http://www.salesforce.com/us/developer/docs/api/Content/compound_fields_address.htm
            if not contains_compound and field.get("queryByDistance"): continue
            if not action or field[action]: 
                field_list.append(field.get("name"))

        # Id must be included in the field list
        if not field_list:
            field_list.append("Id")

        self.result = {
            "success": result["success"],
            "soql": 'SELECT %s FROM %s' % (", ".join(field_list), sobject)
        }
        return self.result

    def describe_sobject(self, sobject, is_toolingapi=False):
        """ Sends a GET request. Return sobject describe result

        * sobject -- sObjectType
        """

        url = ("/tooling" if is_toolingapi else "") + "/sobjects/%s/describe" % sobject
        result = self.get(url)
        self.result = result
        return result

    def describe_sobjects(self, sobjects):
        """ Sends get requests, return sObjects describe result

        * sobjects -- sObject collection
        """

        result = []
        for sobject in sobjects:
            result.append(self.describe_sobject(sobject))

        self.result = result
        return result

    def get_sobjects(self):
        """ Sends a GET request to get sObjects to describe

        Returns:

        * * -- sobjects describe dict
        """

        # Describe global for tooling and none-tooling
        result = self.describe_global()
        tooling_result = self.describe_global(True)

        # Get all tooling sobjects
        sobjects = {}
        if "sobjects" in tooling_result:
            for sd in tooling_result["sobjects"]:
                if "name" in sd and sd["queryable"]:
                    sobjects[sd["name"]] = {
                        "name": sd["name"],
                        "custom": sd["custom"],
                        "tooling": True
                    }

        # Get all none-tooling sobjects
        # Note: 
        #   because there are cross sObject between tooling and none-tooling,
        #   for example, User, RecordType, etc., however, 
        #   we just choose that non-tooling ones to override tooling sObjects
        if "sobjects" in result:
            for sd in result["sobjects"]:
                if "name" in sd and sd["queryable"]:
                    sobjects[sd["name"]] = {
                        "name": sd["name"],
                        "custom": sd["custom"],
                        "tooling": False
                    }

        self.result = {
            "sobjects": sobjects,
            "success": True
        }
        return self.result

    def describe_global(self, tooling=False):
        """ Describe global for tooling or non-tooling

        Arguments:
        
        * tooling -- indicate whether tooling operation;
        """

        url = "%s/sobjects" % ("/tooling" if tooling else "")
        return self.get(url)

    def manage_password(self, user_id, data):
        """ Change password for user

        Arguments:
        
        * url -- url include userId to change password
        * new_password -- new password to be changed
        """

        url = "/sobjects/User/%s/password" % user_id
        self.result = self.post(url, data)
        return self.result

    def create_trace_flags(self, users):
        """ Create Debug Log Trace by users

        Arguments:
        
        * users -- Required; {
            "User Name": "User Id",
            ...
        }
        """
        for user_name in users:
            result = self.create_trace_flag(users[user_name])

            user_name = user_name.split(" => ")[0]
            if result["success"]:
                message = 'Succeed to create trace flag for %s' % user_name
            else:
                message = 'Failed to create trace flag for %s, due to %s' % (
                    user_name, result.get("message", "Unknown Reason")
                )

            Printer.get("log").write(message)

    def create_trace_flag(self, traced_entity_id=None):
        """ Create Debug Log Trace by traced_entity_id

        Arguments:
        
        * traced_entity_id -- Optional; Component Id or User Id
        """

        if not traced_entity_id:
            self.login()
            traced_entity_id = self.session["user_id"]

        # Check whether traced user already has trace flag
        # If not, just create it for him/her
        query = "SELECT Id, ExpirationDate FROM TraceFlag " +\
                "WHERE TracedEntityId = '%s'" % (traced_entity_id)
        result = self.query(query, True)

        # Exception Process
        if not result["success"]:
            self.result = result
            return self.result

        # If trace flag is exist, just delete it
        if result["totalSize"] > 0:
            self.delete("/tooling/sobjects/TraceFlag/" + result["records"][0]["Id"])
            return self.create_trace_flag(traced_entity_id)
        
        # Start to create Trace Flag
        trace_flag = self.settings["trace_flag"]

        # Create debug level, since 35, new DebugLevelId field is required
        if self.settings["api_version"] > 34:
            debug_level = self.get_debug_level()
            if not debug_level["success"]:
                self.result = debug_level
                return self.result
            
            trace_flag["LogType"] = "USER_DEBUG"
            trace_flag["DebugLevelId"] = debug_level["id"]

        # We must set the expiration date to next day, 
        # otherwise, the debug log record will not be created 
        expiration_date = datetime.datetime.utcnow() + datetime.timedelta(minutes=120)
        trace_flag["ExpirationDate"] = expiration_date.isoformat()
        trace_flag["TracedEntityId"] = traced_entity_id
        post_url = "/tooling/sobjects/TraceFlag"
        result = self.post(post_url, trace_flag)

        # Exception Process
        if not result["success"]:
            self.result = result
            return self.result

        self.result = result
        return result

    def get_debug_level(self, name="haoide"):
        debug_levels = self.query(
            "SELECT Id FROM DebugLevel WHERE DeveloperName = '%s'" % name, 
            is_toolingapi=True
        )
        if debug_levels["success"]:
            if debug_levels["totalSize"] > 0:
                debug_level = debug_levels["records"][0]
                debug_level["id"] = debug_level["Id"] # Prevent keyError problem
                debug_level["success"] = True
                return debug_level

        debug_level = self.settings["trace_flag"].copy()
        debug_level["MasterLabel"] = name;
        debug_level["DeveloperName"] = name;

        result = self.post("/tooling/sobjects/DebugLevel", debug_level)
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
        headers["Accept-Encoding"] = 'gzip'

        try:
            response = requests.get(url, verify=False, headers=headers, timeout=timeout)
            response.encoding = "UTF-8"
        except requests.exceptions.RequestException as e:
            self.result = {
                "Error Message":  "Network connection timeout when issuing RETRIVING BODY request",
                "success": False
            }
            return self.result

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            result = self.login(True)
            return self.retrieve_body(retrieve_url)

        result = self.parse_response(response)
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
        result = self.login()
        if not result["success"]:
            self.result = result
            return self.result

        traced_entity_id = self.session["user_id"]
        self.create_trace_flag(traced_entity_id)

        # Exception Process
        if not result["success"]:
            self.result = result
            return self.result

        time.sleep(2)
        data = {"ApexClassId": class_id}
        result = self.post("/sobjects/ApexTestQueueItem", data)
        
        # Exception Process
        if not result["success"]:
            self.result = result
            return self.result
        
        # Wait for the ApexTestQueueItem is over
        time.sleep(5)
        queue_item_id = result["id"]
        queue_item_soql = "SELECT Id, Status FROM ApexTestQueueItem WHERE Id='%s'" % queue_item_id
        result = self.query(queue_item_soql)

        # Exception Process
        if not result["success"]:
            self.result = result
            return self.result
        
        # If totalSize is Zero, it means we need to wait until test is finished
        while result["totalSize"] == 0 or result["records"][0]["Status"] in ["Queued", "Processing"]:
            time.sleep(2)
            result = self.query(queue_item_soql)

        test_result_soql = """SELECT ApexClass.Id,ApexClass.Name,ApexLogId,
            AsyncApexJobId,Id,Message,MethodName,Outcome,QueueItemId,StackTrace,
            TestTimestamp FROM ApexTestResult WHERE QueueItemId = '%s'""" % queue_item_id

         # After Test is finished, get result
        result = self.query(test_result_soql)

        # Exception Process
        if not result["success"]:
            self.result = result
            return self.result

        result = result["records"]
        
        # Combine these two result
        self.result = result

    def generate_workbook(self, sobjects):
        """ Generate CSV for Sobject Workbook

        Arguments:

        * sobject -- sobject name
        """
        for sobject in sobjects:
            result = self.describe_sobject(sobject)

            # Exception Process
            if not result["success"]:
                self.result = result
                return result

            workspace = self.settings.get("workspace")
            outputdir = util.generate_workbook(result, workspace, 
                self.settings.get("workbook_field_describe_columns"))+"/"+sobject+".csv"
            print (sobject + " workbook outputdir: " + outputdir)

    def save_to_server(self, component_attribute, body, is_check_only, check_save_conflict=True):
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

        # Firstly Login
        result = self.login()
        if not result["success"]:
            self.result = result
            return self.result

        # Component Attribute
        component_type = component_attribute["type"]
        component_id = component_attribute["id"]
        component_body = component_attribute["body"]

        if self.settings["check_save_conflict"] and not is_check_only and check_save_conflict:
            Printer.get('log').write("Start to check saving conflict")
            query = "SELECT Id, LastModifiedById, LastModifiedBy.Id, " +\
                    "LastModifiedBy.Name, LastModifiedDate, SystemModstamp " +\
                    "FROM %s WHERE Id = '%s'" % (component_type, component_id)
            result = self.query(query, True)

            # Exception Process
            if not result["success"]:
                self.result = result
                return result

            # Get Server Date and LastModifiedBy
            class_attr = result["records"][0]
            lastModifiedBy = class_attr["LastModifiedBy"]
            serverDateLiteral = class_attr["LastModifiedDate"]
            serverLastModifiedDateZone = util.local_datetime(serverDateLiteral)

            # Get local lastModifiedDate
            localDateLiteral = component_attribute.get("lastModifiedDate", '')

            # If local date is different with server date or lastModifiedBy is not you,
            # it means there has conflict
            lastModifiedByYou = class_attr["LastModifiedById"] == self.session["user_id"]
            timeStampMatch = serverDateLiteral[:19] == localDateLiteral[:19]
            if not lastModifiedByYou or not timeStampMatch:
                # Used for debug
                if self.settings["debug_mode"]:
                    print ("localDateLiteral: " + localDateLiteral)
                    print ("serverDateLiteral: " + serverDateLiteral)

                message = "Modified by %s at %s, continue?" % (
                    lastModifiedBy["Name"], serverLastModifiedDateZone
                )
                if not sublime.ok_cancel_dialog(message, "Ignore Conflict?"):
                    Printer.get('log').write("Has conflict, comparing with server...")
                    self.result = {
                        "Operation": "cancel",
                        "Message": "Save operation is cancelled by you due to the conflict"
                    }
                    return self.result

            # If no conflict, just outout the lastModified information
            Printer.get('log').write("No conflict, last modified by you at %s" % serverLastModifiedDateZone)

        # Get MetadataContainerId
        Printer.get('log').write("Start to fetch MetadataContainerId")
        data = {  
            "name": "Save" + component_type[4 : len(component_type)] + component_id
        }
        container_url = "/tooling/sobjects/MetadataContainer"
        result = self.post(container_url, data)

        # If status_code < 399, it means post succeed
        if result["success"]:
            container_id = result.get("id")
        else:
            # If DUPLICATE Container Id, just delete it and restart this function
            if "errorCode" in result and result["errorCode"] == "DUPLICATE_VALUE":
                Printer.get('log').write("Start to delete the duplicate MetadataContainerId")
                error_message = result["message"]
                container_id = error_message[error_message.rindex("1dc"): len(error_message)]
                delete_result = self.delete(container_url + "/" + container_id)
                if delete_result["success"]:
                    sublime.set_timeout(lambda:sublime.status_message("container_id is deleted."), 10)
                else:
                    self.result = delete_result
                    return delete_result
                
                # We can't reuse the container_id which caused error
                # Post Request to get MetadataContainerId
                return self.save_to_server(component_attribute, body, is_check_only, False)
            else:
                self.result = result
                return self.result

        # Post ApexComponentMember
        data = {
            "ContentEntityId": component_id,
            "MetadataContainerId": container_id,
            # "Metadata": {
            #     "apiVersion": 34.0,
            #     "status": "Active",
            #     "packageVersions": [{
            #         "majorNumber": 1,
            #         "minorNumber": 2,
            #         "namespace": "haoliu"
            #     }]
            # },
            "Body": body
        }
        url = "/tooling/sobjects/" + component_type + "Member"
        member_result = self.post(url, data)
        
        # Check whether user has privilege of `Author Apex`
        if "errorCode" in member_result and member_result["errorCode"] == "NOT_FOUND":
            # Before return error to console, we need to delete the container_id
            # If delete failed, next saving operation will handle it
            sublime.set_timeout_async(self.delete(container_url + "/" + container_id), 100)
            
            self.result = {
                "success": False,
                "Error Message": "You don't have privilege on 'Author Apex'"
            }
            return self.result

        # Post ContainerAsyncRequest
        Printer.get('log').write("Start to post ContainerAsyncRequest Request")
        data = {
            "MetadataContainerId": container_id,
            # "MetadataContainerMemberId": member_result["id"],
            "IsCheckOnly": is_check_only
        }
        sync_request_url = '/tooling/sobjects/ContainerAsyncRequest'
        result = self.post(sync_request_url, data)
        request_id = result.get("id")

        # Get ContainerAsyncRequest Result
        Printer.get('log').write("Start to get ContainerAsyncRequest result")
        result = self.get(sync_request_url + "/" + request_id)
        state = result["State"]

        while state == "Queued":
            time.sleep(0.5)
            Printer.get('log').write("ContainerAsyncRequest is in Queued, waiting...")
            result = self.get(sync_request_url + "/" + request_id)
            state = result["State"]
        
        return_result = {
            "lastModifiedDate": result["LastModifiedDate"]
        }
        if state == "Completed":
            return_result["success"] = True

        # Fix issue #74
        if state in ["Error", "Aborted", "Invalidated"]:
            if "ErrorMsg" in result:
                problem = result["ErrorMsg"]
            else:
                problem = "This job is " + state
            return_result = {
                "success": False,
                "problem": problem,
                "columnNumber": 0,
                "lineNumber": 0
            }

        if state == "Failed":
            # This error need more process, because of confused single quote
            if self.api_version > 30:
                compile_errors = result["DeployDetails"]["componentFailures"]
            else:
                compile_errors = unescape(result["CompilerErrors"])
                compile_errors = json.loads(compile_errors)
            
            return_result = {}
            if len(compile_errors) > 0:
                return_result = compile_errors[0]
            else:
                return_result["problem"] = result["ErrorMsg"]
                return_result["columnNumber"] = 0
                return_result["lineNumber"] = 0

            # Fix issue github://haoide/issue#7
            if "problem" in return_result:
                problem = return_result["problem"]
                if not problem:
                    problem = "Unknown problem, please try to use `Deploy To This Server` command"
                if isinstance(problem, list):
                    problem = "\n".join(problem)
                return_result["problem"] = urllib.parse.unquote(
                    unescape(problem, {
                        "&apos;": "'", 
                        "&quot;": '"'
                    })
                )

            if "line" in return_result:
                return_result["lineNumber"] = return_result["line"]
                del return_result["line"]

            if "column" in return_result:
                return_result["columnNumber"] = return_result["column"]
                del return_result["column"]

            if "columnNumber" not in return_result:
                return_result["columnNumber"] = 0

            return_result["success"] =  False
        
        if return_result["success"] and component_type == "ApexClass":
            sublime.set_timeout_async(self.write_symbol_table_cache(member_result["id"]), 5)

        # Whatever succeed or failed, just delete MetadataContainerId
        sublime.set_timeout_async(self.delete(container_url + "/" + container_id), 100)

        # Result used in thread invoke
        self.result = return_result

    def write_symbol_table_cache(self, member_id):
        # Get the symbol table from ApexClassMember
        query = "SELECT Id, SymbolTable " +\
                "FROM ApexClassMember WHERE Id ='%s'" % member_id
        member = self.query(query, True)

        # Start to write symbol table to cache
        if not member["records"]: return
        symbol_table = member["records"][0]["SymbolTable"]

        # Get symbolTable from component_metadata.sublime-settings
        symbol_table_cache = sublime.load_settings("symbol_table.sublime-settings")
        symboltable_dict = symbol_table_cache.get(self.settings["username"], {})

        # Outer completions 
        outer = util.parse_symbol_table(symbol_table)

        symboltable_dict[symbol_table["name"].lower()] = {
            "outer" : outer,
            "name": symbol_table["name"]
        }

        # Inner completions
        inners = {}
        for inn in symbol_table["innerClasses"]:
            inner = util.parse_symbol_table(inn)
            inners[inn["name"].lower()] = inner
        symboltable_dict[symbol_table["name"].lower()]["inners"] = inners

        symbol_table_cache.set(self.settings["username"], symboltable_dict)
        sublime.save_settings("symbol_table.sublime-settings")