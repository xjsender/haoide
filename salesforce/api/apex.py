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
from ..login import soap_login
from ... import requests, util


class ApexApi():
    def __init__(self, settings, **kwargs):
        self.settings = settings
        self.soap = SOAP(settings)
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

        soap_body = soap.run_all_test.format(session_id=self.session["session_id"])

        body = self.soap.create_request('run_all_test')
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
        body = self.soap.create_request('execute_anonymous', {"apex_string": apex_string})

        try:
            response = requests.post(self.apex_url, body, verify=False, 
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
        result["debugLog"] = util.getUniqueElementValueFromXmlString(content, "debugLog")
        result["column"] = util.getUniqueElementValueFromXmlString(content, "column")
        result["compileProblem"] = util.getUniqueElementValueFromXmlString(content, "compileProblem")
        result["compiled"] = util.getUniqueElementValueFromXmlString(content, "compiled")
        result["line"] = util.getUniqueElementValueFromXmlString(content, "line")
        result["success"] = util.getUniqueElementValueFromXmlString(content, "success")
        
        # Self.result is used to keep thread result
        self.result = result

        # This result is used for invoker
        return result