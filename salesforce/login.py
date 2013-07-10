import urllib

try:
    # Python 3.x
    from .. import requests
    from . import soap_bodies
    from .util import getUniqueElementValueFromXmlString
except:
    # Python 2.x
    import requests
    import soap_bodies
    from util import getUniqueElementValueFromXmlString

# https://github.com/xjsender/simple-salesforce/blob/master/simple_salesforce/login.py
def soap_login(settings):
    login_soap_request_body = soap_bodies.login_body.format(
        username = settings["username"], 
        password = settings["password"])

    login_soap_request_headers = {
        'content-type': 'text/xml',
        'charset': 'UTF-8',
        'SOAPAction': 'login'
    }

    response = requests.post(settings["soap_login_url"], login_soap_request_body, 
        verify = False, headers = login_soap_request_headers)

    if response.status_code != 200:
        except_code = getUniqueElementValueFromXmlString(response.content,
                                                         'sf:exceptionCode')
        except_msg = getUniqueElementValueFromXmlString(response.content,
                                                        'sf:exceptionMessage')
        raise SalesforceAuthenticationFailed('%s: %s' % (except_code,
                                                         except_msg))

    session_id = getUniqueElementValueFromXmlString(response.content, 'sessionId')
    print("session_id: " + session_id)
    server_url = getUniqueElementValueFromXmlString(response.content, 'serverUrl')
    sf_instance = server_url[ : server_url.find('/services')]
    user_id = getUniqueElementValueFromXmlString(response.content, 'userId')

    return sf_instance, session_id, server_url, user_id


class SalesforceAuthenticationFailed(Exception):
    '''
    Thrown to indicate that authentication with Salesforce failed.
    '''
    pass