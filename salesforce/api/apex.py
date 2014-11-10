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


class ApexApi():
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

    def run_all_test(self):
        # Firstly Login
        self.login()

        # https://gist.github.com/richardvanhook/1245068
        headers = {
            "Content-Type": "text/xml;charset=UTF-8",
            "Accept-Encoding": 'identity, deflate, compress, gzip',
            "SOAPAction": '""'
        }

        soap_body = soap_bodies.run_all_test.format(
            session_id=globals()[self.username]["session_id"])

        try:
            response = requests.post(self.apex_url, soap_body, verify=False, 
                headers=headers)
        except Exception as e:
            self.result = {
                "Error Message":  "Network Issue" if "Max retries exceeded" in str(e) else str(e),
                "URL": url,
                "Operation": "Execute Anonymous",
                "success": False
            }
            return self.result

        # Check whether session_id is expired
        if "INVALID_SESSION_ID" in response.text:
            self.login(True)
            return self.run_all_test()

        # If status_code is > 399, which means it has error
        content = response.content
        result = {"success": response.status_code < 399}
        if response.status_code > 399:
            if response.status_code == 500:
                result["Error Code"] = util.getUniqueElementValueFromXmlString(content, "faultcode")
                result["Error Message"] = util.getUniqueElementValueFromXmlString(content, "faultstring")
            else:
                result["Error Code"] = util.getUniqueElementValueFromXmlString(content, "errorCode")
                result["Error Message"] = util.getUniqueElementValueFromXmlString(content, "message")

            self.result = result
            return result

        content = response.content
        result = xmltodict.parse(content)
        try:
            result = result["soapenv:Envelope"]["soapenv:Body"]["runTestsResponse"]["result"]
        except (KeyError):
            result = {
                "errorCode": "Convert Xml to JSON Exception",
                "message": 'body["runTestsResponse"]["result"] KeyError'
            }

        # print (json.dumps(result, indent=4))
        result["success"] = response.status_code < 399
        self.result = result
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
                "Operation": "Execute Anonymous",
                "success": False
            }
            self.result = result
            return self.result
        except Exception as e:
            self.result = {
                "Error Message":  "Network Issue" if "Max retries exceeded" in str(e) else str(e),
                "URL": url,
                "Operation": "Execute Anonymous",
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
                result["Error Code"] = util.getUniqueElementValueFromXmlString(content, "faultcode")
                result["Error Message"] = util.getUniqueElementValueFromXmlString(content, "faultstring")
            else:
                result["Error Code"] = util.getUniqueElementValueFromXmlString(content, "errorCode")
                result["Error Message"] = util.getUniqueElementValueFromXmlString(content, "message")

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