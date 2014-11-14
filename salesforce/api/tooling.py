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
                response_result = {"errorMessage": res.text}

            response_result["url"] = res.url
            response_result["success"] = False
        else:
            try:
                response_result = {}
                if isinstance(res.json(), list):
                    response_result["list"] = res.json()
                elif isinstance(res.json(), dict):
                    response_result = res.json()
                else:
                    response_result["str"] = res.text
            except:
                response_result = {}
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
        except Exception as e:
            self.result = {
                "Error Message":  "Network Issue" if "Max retries exceeded" in str(e) else str(e),
                "URL": url,
                "Operation": "HEAD",
                "success": False
            }
            return self.result

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
        except Exception as e:
            self.result = {
                "Error Message":  "Network Issue" if "Max retries exceeded" in str(e) else str(e),
                "URL": url,
                "Operation": "GET",
                "success": False
            }
            return self.result

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
        result = self.login()
        if not result["success"]:
            self.result = result
            return self.result

        url = self.parse_url(put_url)
        
        try:
            response = requests.put(url, data=json.dumps(data), verify=False, 
                headers=self.headers, timeout=timeout)
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
        except Exception as e:
            self.result = {
                "Error Message":  "Network Issue" if "Max retries exceeded" in str(e) else str(e),
                "URL": url,
                "Operation": "PATCH",
                "success": False
            }
            return self.result

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
        result = self.login()
        if not result["success"]:
            self.result = result
            return self.result

        url = self.parse_url(post_url)
        
        try:
            response = requests.post(url, data=json.dumps(data), verify=False, 
                headers=self.headers, timeout=timeout)
        except Exception as e:
            self.result = {
                "Error Message":  "Network Issue" if "Max retries exceeded" in str(e) else str(e),
                "URL": url,
                "Operation": "POST",
                "success": False
            }
            return self.result

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
        result = self.login()
        if not result["success"]:
            self.result = result
            return self.result

        url = self.parse_url(component_url)
        
        try:
            response = requests.delete(url, data=None, verify=False, 
                headers=self.headers, timeout=timeout)
        except Exception as e:
            self.result = {
                "Error Message":  "Network Issue" if "Max retries exceeded" in str(e) else str(e),
                "URL": url,
                "Operation": "POST",
                "success": False
            }
            return self.result

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
        result = self.login()
        if not result["success"]:
            self.result = result
            return self.result

        url = self.base_url + "/search"
        params = {'q' : sosl}
        try:
            response = requests.get(url, headers=self.headers, verify=False, 
                params=params, timeout=timeout)
        except Exception as e:
            self.result = {
                "Error Message":  "Network Issue" if "Max retries exceeded" in str(e) else str(e),
                "URL": url,
                "SOSL": sosl,
                "Operation": "SEARCH",
                "success": False
            }
            return self.result

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
        except Exception as e:
            self.result = {
                "Error Message":  "Network Issue" if "Max retries exceeded" in str(e) else str(e),
                "URL": url,
                "SOQL": soql,
                "Operation": "QUERY",
                "success": False
            }
            return self.result

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
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

    def query_symbol_table(self, split=200):
        """ Some Tooling Sobject doesn't support query all, for example, ApexClass,
            If we query all ApexClasses, SymbolTable attribute will be null, however, 
            if we query for 200 records at once, SymbolTable will have value
        """

        # GET the totalSize
        result = self.query("SELECT COUNT() FROM ApexClass", is_toolingapi=True)

        # Exception Process
        if not result["success"]:
            self.result = result
            return self.result

        totalSize = result["totalSize"]
        
        offset = 0
        result = {"totalSize": 0, "records": [], "success": result["success"]}
        while totalSize >= offset:
            soql = """SELECT NamespacePrefix, SymbolTable, Name 
                      FROM ApexClass ORDER BY Name 
                      LIMIT %s OFFSET %s""" % (split, offset)
            previous_result = self.query(soql, is_toolingapi=True)
            if not previous_result["success"]: continue
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

    def update_user(self, data):
        """ Use the data to update the detail of running user

        * sobject -- sobject name, for example, Account, Contact
        """
        self.login()
        patch_url = "/sobjects/User/%s" % self.session["user_id"]
        result = self.patch(patch_url, data)
        self.result = result
        return self.result

    def combine_soql(self, sobject, contains_compound=True):
        """ Get the full field list soql by sobject

        * sobject -- sobject name, for example, Account, Contact
        """
        result = self.describe_sobject(sobject)

        # Exception Process
        if not result["success"]:
            self.result = result
            return self.result

        fields = sorted(result["fields"], key=lambda k : k['custom'])
        sobject_fields = ""
        for field in fields:
            # http://www.salesforce.com/us/developer/docs/api/Content/compound_fields_address.htm
            if not contains_compound and field.get("queryByDistance"): continue
            sobject_fields += field.get("name") + ", "

        self.result = {
            "success": result["success"],
            "soql": 'SELECT ' + sobject_fields[ : -2] + ' FROM ' + sobject
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

    def describe_global(self):
        """ Sends a GET request. Return global describe

        Returns:

        * * -- sobjects describe dict
        """

        result = self.get("/sobjects")

        # Exception Process
        if not result["success"]:
            self.result = result
            return self.result

        describe_result = {
            "sobjects": {},
            "success": True
        }
        for sobject_describe in result.get("sobjects"):
            if "name" in sobject_describe:
                describe_result["sobjects"][sobject_describe["name"]] = sobject_describe
        self.result = describe_result
        return self.result

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
        time_stamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime(time.time()))
        query = "SELECT Id, ExpirationDate FROM TraceFlag " +\
                "WHERE TracedEntityId = '%s' AND ExpirationDate >= %s" % (traced_entity_id, time_stamp)
        result = self.query(query, True)

        # Exception Process
        if not result["success"]:
            self.result = result
            return self.result

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

        # Exception Process
        if not result["success"]:
            self.result = result
            return self.result

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

        try:
            response = requests.get(url, verify=False, headers=headers, timeout=timeout)
        except Exception as e:
            self.result = {
                "Error Message":  "Network Issue" if "Max retries exceeded" in str(e) else str(e),
                "URL": url,
                "Operation": "RETRIEVE BODY",
                "success": False
            }
            return self.result

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.retrieve_body(retrieve_url)

        result = {
            "success": response.status_code < 399,
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

        if not result["success"]:
            self.result = result
            return
        
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
            time.sleep(5)
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

    def generate_workbook(self, sobject):
        """ Generate CSV for Sobject Workbook

        Arguments:

        * sobject -- sobject name
        """
        result = self.describe_sobject(sobject)

        # Exception Process
        if not result["success"]:
            self.result = result
            return result

        workspace = self.settings.get("workspace")
        outputdir = util.generate_workbook(result, workspace, 
            self.settings.get("workbook_field_describe_columns"))+"/"+sobject+".csv"
        print (sobject + " workbook outputdir: " + outputdir)

    def save_component(self, panel, component_attribute, body, is_check_only):
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
        util.append_message(panel, "Start login...")
        result = self.login()
        if not result["success"]:
            util.append_message(panel, "Login failed")
            self.result = result
            return self.result
        util.append_message(panel, "Login succeed")

        # Component Attribute
        component_type = component_attribute["type"]
        component_id = component_attribute["id"]
        component_body = component_attribute["body"]

        if self.settings["check_save_conflict"]:
            util.append_message(panel, "Start to check saving conflict")
            query = "SELECT Id, LastModifiedById, LastModifiedDate " +\
                    "FROM %s WHERE Id = '%s'" % (component_type, component_id)
            result = self.query(query, True)

            # Exception Process
            if not result["success"]:
                self.result = result
                return result

            # Get modified user name by Id
            # C2P relationship query is not available, it's a bug?
            class_attr = result["records"][0]
            last_modified_id = class_attr["LastModifiedById"]
            last_modified_date = class_attr["LastModifiedDate"][:19]
            
            if not class_attr["LastModifiedById"] == self.session["user_id"]:
                try:
                    soql = "SELECT Id, FirstName, LastName, TimeZoneSidKey " +\
                           "FROM User WHERE Id = '%s'" % last_modified_id
                    user_details = self.query(soql)
                    user_detail = user_details["records"][0]
                    last_modified_name = "%s %s" % (user_detail["LastName"], user_detail["FirstName"])
                except:
                    last_modified_name = last_modified_id

                message = "Modified by %s at %s, continue?" % (last_modified_name, last_modified_date.replace("T", " "))
                if not sublime.ok_cancel_dialog(message):
                    self.result = {
                        "success": False,
                        "Message": "Save operation is cancelled by you due to the conflict"
                    }
                    return self.result
            else:
                util.append_message(panel, "No conflict, last modified by you at %s" % 
                    last_modified_date.replace("T", " "))

        # Get MetadataContainerId
        util.append_message(panel, "Start to fetch MetadataContainerId")
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
            if result["errorCode"] == "DUPLICATE_VALUE":
                util.append_message(panel, "Start to delete the duplicate MetadataContainerId")
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
                return self.save_component(panel, component_attribute, body, is_check_only)

        # Post ApexComponentMember
        data = {
            "ContentEntityId": component_id,
            "MetadataContainerId": container_id,
            "Body": body
        }
        url = "/tooling/sobjects/" + component_type + "Member"
        member_result = self.post(url, data)

        # Post ContainerAsyncRequest
        util.append_message(panel, "Start to post ContainerAsyncRequest")
        data = {
            "MetadataContainerId": container_id,
            "IsCheckOnly": is_check_only,
            "IsRunTests": False
        }
        sync_request_url = '/tooling/sobjects/ContainerAsyncRequest'
        result = self.post(sync_request_url, data)
        request_id = result.get("id")

        # Get ContainerAsyncRequest Result
        util.append_message(panel, "Start to get ContainerAsyncRequest result")
        result = self.get(sync_request_url + "/" + request_id)
        state = result["State"]
        # print ("Get ContainerAsyncRequest: ", result)

        return_result = {}
        if state == "Completed":
            return_result = {
                "success": True
            }

        while state == "Queued":
            util.append_message(panel, "ContainerAsyncRequest is in Queued, Waiting...")
            time.sleep(2)

            result = self.get(sync_request_url + "/" + request_id)
            state = result["State"]
            if state == "Completed":
                return_result = {"success": True}

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
                return_result["Error Message"] = result["ErrorMsg"]

            return_result["success"] =  False
        
        if return_result["success"] and component_type == "ApexClass":
            util.append_message(panel, "Start to fetch symbol table")
            query = "SELECT Id, SymbolTable " +\
                    "FROM ApexClassMember WHERE Id ='%s'" % member_result["id"]
            member = self.query(query, True)
            if member["records"]:
                return_result["symbol_table"] = member["records"][0]["SymbolTable"]

        # Whatever succeed or failed, just delete MetadataContainerId
        delete_result = self.delete(container_url + "/" + container_id)

        # Result used in thread invoke
        self.result = return_result