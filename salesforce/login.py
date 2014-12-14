import urllib
import os
import json
import time
from xml.sax.saxutils import escape

from .. import requests
from . import soap
from .. import util

# https://github.com/xjsender/simple-salesforce/blob/master/simple_salesforce/login.py
def soap_login(settings, session_id_expired=False, timeout=120):
    if not session_id_expired:
        session_path = settings["workspace"]+"/.config/session.json"
        if os.path.isfile(session_path):
            session = json.loads(open(session_path).read())
            return session

    login_soap_request_body = soap.login_body.format(
        username = settings["username"], 
        password = escape(settings["password"]) + settings["security_token"])

    login_soap_request_headers = {
        'content-type': 'text/xml',
        'charset': 'UTF-8',
        'SOAPAction': 'login'
    }

    try:
        response = requests.post(settings["soap_login_url"], login_soap_request_body, 
            verify=False, headers=login_soap_request_headers, timeout=timeout)
    except Exception as e:
        result = {
            "Error Message":  "Network Issue" if "Max retries exceeded" in str(e) else str(e),
            "URL": settings["soap_login_url"],
            "Operation": "LOGIN",
            "success": False
        }
        return result

    result = {}
    if response.status_code != 200:
        except_code = util.getUniqueElementValueFromXmlString(response.content,
                                                         'sf:exceptionCode')
        except_msg = util.getUniqueElementValueFromXmlString(response.content,
                                                        'sf:exceptionMessage')
        result["errorCode"] = except_code
        result["message"] = except_msg
        result["success"] = response.status_code < 399
        return result

    session_id = util.getUniqueElementValueFromXmlString(response.content, 'sessionId')
    server_url = util.getUniqueElementValueFromXmlString(response.content, 'serverUrl')
    sf_instance = server_url[ : server_url.find('/services')]
    user_id = util.getUniqueElementValueFromXmlString(response.content, 'userId')

    result = {
        "project name": settings["default_project"]["project_name"],
        "session_id": session_id,
        "X-SFDC-Session": session_id,
        "server_url": server_url,
        "instance_url": sf_instance,
        "user_id": user_id,
        "time_stamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),
        "headers": {
            "Authorization": "OAuth " + session_id,
            "Content-Type": "application/json; charset=UTF-8",
            "Accept": "application/json"
        },
        "success": response.status_code < 399,
    }

    # If session is expired, just write session 
    # to .config/session.json
    util.add_config_history('session', result)

    return result