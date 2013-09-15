import urllib

from .. import requests
from . import soap_bodies
from .util import getUniqueElementValueFromXmlString

# https://github.com/xjsender/simple-salesforce/blob/master/simple_salesforce/login.py
def soap_login(settings, timeout=120):
    login_soap_request_body = soap_bodies.login_body.format(
        username = settings["username"], 
        password = settings["password"] + settings["security_token"])

    login_soap_request_headers = {
        'content-type': 'text/xml',
        'charset': 'UTF-8',
        'SOAPAction': 'login'
    }

    response = requests.post(settings["soap_login_url"], login_soap_request_body, 
        verify=False, headers=login_soap_request_headers, timeout=timeout)

    result = {}
    if response.status_code != 200:
        except_code = getUniqueElementValueFromXmlString(response.content,
                                                         'sf:exceptionCode')
        except_msg = getUniqueElementValueFromXmlString(response.content,
                                                        'sf:exceptionMessage')
        result["errorCode"] = except_code
        result["message"] = except_msg
        result["status_code"] = response.status_code
        return result

    session_id = getUniqueElementValueFromXmlString(response.content, 'sessionId')
    server_url = getUniqueElementValueFromXmlString(response.content, 'serverUrl')
    sf_instance = server_url[ : server_url.find('/services')]
    user_id = getUniqueElementValueFromXmlString(response.content, 'userId')

    result = {
        "session_id": session_id,
        "server_url": server_url,
        "instance_url": sf_instance,
        "user_id": user_id,
        "status_code": response.status_code
    }
    return result