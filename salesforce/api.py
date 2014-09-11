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

        sosl = urllib.parse.urlencode({'q' : sosl})
        url = self.base_url + "/search?" + sosl
        if "search?q=q=" in url: url.replace("search?q=q=", "search?q=")

        try:
            response = requests.get(url, data=None, verify=False, 
                headers=self.headers, timeout=timeout)
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
        soql = urllib.parse.quote(soql)
        url = self.base_url + ("/tooling" if is_toolingapi else "") + "/query?q=" + soql

        # Here has a bug, this is used to prevent this exception
        if "query?q=q=" in url: url = url.replace("query?q=q=", "query?q=")

        try:
            response = requests.get(url, data=None, verify=False, 
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

    def update_user(self, data):
        """ Use the data to update the detail of running user

        * sobject -- sobject name, for example, Account, Contact
        """
        self.login()
        patch_url = "/sobjects/User/%s" % globals()[self.username]["user_id"]
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

        traced_entity_id = globals()[self.username]["user_id"]
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
                "URL": url,
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
            result["errorCode"] = getUniqueElementValueFromXmlString(content, "errorCode")
            result["message"] = getUniqueElementValueFromXmlString(content, "message")
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
                result["errorCode"] = getUniqueElementValueFromXmlString(content, "faultcode")
                result["message"] = getUniqueElementValueFromXmlString(content, "faultstring")
            else:
                result["errorCode"] = getUniqueElementValueFromXmlString(content, "errorCode")
                result["message"] = getUniqueElementValueFromXmlString(content, "message")
            return result

        result = xmltodict.parse(response.content)
        result = result["soapenv:Envelope"]["soapenv:Body"]["checkRetrieveStatusResponse"]["result"]
        result["success"] = response.status_code < 399
        return result

    def retrieve(self, soap_body, package_path=None):
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
        if package_path:
            try:
                types = util.parse_package(package_path)
            except Exception as e:
                self.result = {
                    "success": False,
                    "Message": "Package.xml File Parse Problem",
                    "RootCause": str(e)
                }
                return self.result

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
            return self.retrieve(panel, soap_body)

        # If status_code is > 399, which means it has error
        content = response.content
        result = {"success": response.status_code < 399}
        if response.status_code > 399:
            if response.status_code == 500:
                result["errorCode"] = getUniqueElementValueFromXmlString(content, "faultcode")
                result["message"] = getUniqueElementValueFromXmlString(content, "faultstring")
            else:
                result["errorCode"] = getUniqueElementValueFromXmlString(content, "errorCode")
                result["message"] = getUniqueElementValueFromXmlString(content, "message")
            self.result = result
            return

        # [sf:retrieve]
        util.append_message(panel, "[sf:retrieve] Request for a retrieve submitted successfully.")

        # Get async process id
        async_process_id = getUniqueElementValueFromXmlString(content, "id")

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

        # Output directory
        if package_path:
            base_path, file_name = os.path.split(package_path)
        else:
            base_path = self.settings["workspace"]
        util.append_message(panel, "[sf:retrieve] Output directory: "+base_path)

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
        print (content)
        result = {"success": response.status_code < 399}
        if response.status_code > 399:
            result["errorCode"] = getUniqueElementValueFromXmlString(content, "errorCode")
            result["message"] = getUniqueElementValueFromXmlString(content, "message")
            return result

        result = xmltodict.parse(content)
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
        except (KeyError):
            result = {
                "errorCode": "Convert Xml to Dict Exception",
                "message": 'body["checkDeployStatusResponse"]["result"] KeyError',
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
                result["errorCode"] = getUniqueElementValueFromXmlString(content, "faultcode")
                result["message"] = getUniqueElementValueFromXmlString(content, "faultstring")
            else:
                result["errorCode"] = getUniqueElementValueFromXmlString(content, "errorCode")
                result["message"] = getUniqueElementValueFromXmlString(content, "message")
            self.result = result
            return

        # [sf:%s]
        util.append_message(panel, "[sf:%s] Request for a deploy submitted successfully." % deploy_or_validate)

        # Get async process id
        async_process_id = getUniqueElementValueFromXmlString(content, "id")

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
        while body["status"] in ["Pending", "InProgress"]:
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
                            for msg in f["stackTrace"].split("\n"):
                                util.append_message(panel, "\t%s" % msg)

                            # [sf:deploy] -------------------------------------------------------
                            util.append_message(panel, "-" * 84)

                            index += index

            # Thread Wait
            sleep_seconds = 2 if body["status"] == "Pending" else 1
            time.sleep(sleep_seconds)
            
            result = self.check_deploy_status(async_process_id)
            body = result["body"]

        # Check if job is canceled
        if body["status"] == "Canceled":
            util.append_message(panel, "BUILD FAILED", False)
            util.append_message(panel, "*********** DEPLOYMENT FAILED ***********", False)
            util.append_message(panel, "Request ID: %s" % async_process_id, False)
            util.append_message(panel, "\nRequest Canceled", False)
            util.append_message(panel, "*********** DEPLOYMENT FAILED ***********", False)

        # Check if job is canceling
        if body["status"] == "Canceling":
            util.append_message(panel, "BUILD FAILED", False)
            util.append_message(panel, "*********** DEPLOYMENT FAILED ***********", False)
            util.append_message(panel, "Request ID: %s" % async_process_id, False)
            util.append_message(panel, "\nRequest is in canceling", False)
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
                        component_failure["problem"],
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
                util.append_message(panel, "\n"+"\n".join(failures_messages), False)
                util.append_message(panel, "[sf:%s] *********** %s Failed ***********" % (
                    deploy_or_validate, deploy_or_validate.upper()))
        else:
            # Append succeed message
            util.append_message(panel, "[sf:%s] Request Succeed" % deploy_or_validate)
            util.append_message(panel, "[sf:%s] *********** %s SUCCEEDED ***********" % (
                deploy_or_validate, deploy_or_validate.upper()))
            util.append_message(panel, "[sf:%s] Finished request %s successfully." % (deploy_or_validate, async_process_id))

        # Total time
        total_seconds = (datetime.datetime.now() - start_time).seconds
        util.append_message(panel, "\n\nTotal time: %s seconds" % total_seconds, False)

        # Display debug log message in the new view
        if "header" in result and result["header"]:
            view = sublime.active_window().new_file()
            view.run_command("new_view", {
                "name": "Debugging Information",
                "input": header
            })

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

            # Exception Process
            if not result["success"]:
                self.result = result
                return result

            user_id = globals()[self.username]["user_id"]
            class_attr = result["records"][0]
            if not class_attr["LastModifiedById"] == user_id:
                # Get modified user name by Id
                # C2P relationship query is not available, it's a bug?
                last_modified_id = class_attr["LastModifiedById"]
                last_modified_date = class_attr["LastModifiedDate"][:19]
                try:
                    user_details = self.query("SELECT Id, FirstName, LastName FROM User WHERE Id = '%s'" % last_modified_id)
                    user_detail = user_details["records"][0]
                    last_modified_name = "%s %s" % (user_detail["LastName"], user_detail["FirstName"])
                except:
                    last_modified_name = last_modified_id

                message = "Modified by %s at %s, continue?" % (last_modified_name, last_modified_date.replace("T", " "))
                confirm = sublime.ok_cancel_dialog(message)
                if confirm == False: return

        # Get MetadataContainerId
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
                return self.save_component(component_attribute, body, is_check_only)

        # Post ApexComponentMember
        data = {
            "ContentEntityId": component_id,
            "MetadataContainerId": container_id,
            "Body": body
        }
        url = "/tooling/sobjects/" + component_type + "Member"
        member_result = self.post(url, data)

        # Post ContainerAsyncRequest
        data = {
            "MetadataContainerId": container_id,
            "IsCheckOnly": is_check_only,
            "IsRunTests": False
        }
        sync_request_url = '/tooling/sobjects/ContainerAsyncRequest'
        result = self.post(sync_request_url, data)
        request_id = result.get("id")

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
            query = "SELECT Id, SymbolTable " +\
                    "FROM ApexClassMember WHERE Id ='%s'" % member_result["id"]
            member = self.query(query, True)
            if member["records"]:
                return_result["symbol_table"] = member["records"][0]["SymbolTable"]

        # Whatever succeed or failed, just delete MetadataContainerId
        delete_result = self.delete(container_url + "/" + container_id)

        # Result used in thread invoke
        self.result = return_result