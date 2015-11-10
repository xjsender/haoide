import urllib
import os
import json
import time
from xml.sax.saxutils import escape

from .. import requests
from .. import util

# https://github.com/xjsender/simple-salesforce/blob/master/simple_salesforce/login.py
def soap_login(settings, session_id_expired=False, timeout=10):
    if not session_id_expired:
        session = util.get_session_info(settings)
        if session: return session

    login_soap_request_body = """<?xml version="1.0" encoding="utf-8" ?>
        <env:Envelope
            xmlns:xsd="http://www.w3.org/2001/XMLSchema"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xmlns:env="http://schemas.xmlsoap.org/soap/envelope/">
            <env:Body>
                <n1:login xmlns:n1="urn:partner.soap.sforce.com">
                    <n1:username>{username}</n1:username>
                    <n1:password>{password}</n1:password>
                </n1:login>
            </env:Body>
        </env:Envelope>
    """.format(
        username = settings["username"], 
        password = escape(settings["password"]) + settings["security_token"]
    )

    headers = {
        'content-type': 'text/xml',
        'charset': 'UTF-8',
        'SOAPAction': 'login'
    }

    try:
        response = requests.post(settings["soap_login_url"], login_soap_request_body, 
            verify=False, headers=headers, timeout=timeout)
    except requests.exceptions.RequestException as e:
        if "repeat_times" not in globals():
            globals()["repeat_times"] = 1
        else:
            globals()["repeat_times"] += 1

        if settings["debug_mode"]:
            print ("Login Exception: " + str(e))
            print ("repeat_times: " + str(globals()["repeat_times"]))

        if globals()["repeat_times"] <= 12:
            return soap_login(settings, True, timeout)

        result = {
            "Error Message":  "Network connection timeout",
            "success": False
        }
        return result

    # If request succeed, just clear repeat_times
    if "repeat_times" in globals():
        del globals()["repeat_times"]

    result = {}
    if response.status_code != 200:
        except_msg = util.getUniqueElementValueFromXmlString(response.content, 'sf:exceptionMessage')
        result["Error Message"] = except_msg
        result["success"] = False
        return result

    session_id = util.getUniqueElementValueFromXmlString(response.content, 'sessionId')
    server_url = util.getUniqueElementValueFromXmlString(response.content, 'serverUrl')
    instance_url = server_url[ : server_url.find('/services')]
    user_id = util.getUniqueElementValueFromXmlString(response.content, 'userId')

    result = {
        "project name": settings["default_project"]["project_name"],
        "session_id": session_id,
        "X-SFDC-Session": session_id,
        "server_url": server_url,
        "metadata_url": instance_url + "/services/Soap/m/%s.0" % settings["api_version"],
        "rest_url": instance_url + "/services/data/v%s.0" % settings["api_version"],
        "apex_url": instance_url + "/services/Soap/s/%s.0" % settings["api_version"],
        "partner_url": instance_url + "/services/Soap/u/%s.0" % settings["api_version"],
        "instance_url": instance_url,
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
    util.add_config_history('session', result, settings)

    return result