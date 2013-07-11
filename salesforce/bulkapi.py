import sublime
import threading
import time
import pprint
import os
import threading
from xml.sax.saxutils import unescape

try:
    # Python 3.x
    from .login import soap_login
    from . import soap_bodies
    from . import message
    from .util import getUniqueElementValueFromXmlString

    from .. import context
    from .. import requests
except:
    # Python 2.x
    from login import soap_login
    from salesforce import soap_bodies
    import message
    from util import getUniqueElementValueFromXmlString

    import context
    import requests

# Used in output log
SEPARATE = "-" * 100

def login(toolingapi_settings, session_id_expired):
    if "access_token" not in globals() or session_id_expired:
        instance_url, access_token, server_url, user_id = soap_login(toolingapi_settings)
        globals()["access_token"] = access_token
        globals()["instance_url"] = instance_url
        globals()["server_url"] = server_url
        globals()["user_id"] = user_id

# Post: https://instance.salesforce.com/services/async/27.0/job
def create_job(sobject, operation):
    url = globals()["instance_url"] + "/services/async/27.0/job"
    body = soap_bodies.create_job.format(operation=operation, sobject=sobject)
    headers = {
        "X-SFDC-Session": globals()["access_token"],
        "Content-Type": "application/xml; charset=UTF-8",
        "Accept": "text/plain"
    }

    response = requests.post(url, body, verify = False, headers = headers)
    job_id = getUniqueElementValueFromXmlString(response.content, "id")

    if job_id == None:
        print(sobject + " is not valid sobject, please check.")

    return job_id

def create_batch(job_id, sobject, sobject_soql):
    url = globals()["instance_url"] +\
        "/services/async/27.0/job/{job_id}/batch".format(job_id = job_id)

    headers = {
        "X-SFDC-Session": access_token,
        "Content-Type": "text/csv; charset=UTF-8"
    }
    
    response = requests.post(url, sobject_soql, verify = False, headers = headers)
    batch_id = getUniqueElementValueFromXmlString(response.content, "id")

    return batch_id

# Get: https://instance.salesforce.com/services/async/27.0/job/jobId
def check_job_status(job_id):
    url = globals()["instance_url"] + "/services/async/27.0/job/" + job_id

    headers = {
        "X-SFDC-Session": access_token
    }

    response = requests.get(url, data = None, verify = False, headers = headers)
    job_status = getUniqueElementValueFromXmlString(response.content, "state")

    if job_status != "Completed":
        print(job_id + " is not completed, please continue waiting...")
        time.sleep(15)
        check_job_status(job_id)

    return True

# Get: https://instance.salesforce.com/services/async/27.0/job/jobId/batch/batchId
def check_batch_status(job_id, batch_id, sobject):
    url = globals()["instance_url"] +\
        "/services/async/27.0/job/{job_id}/batch/{batch_id}".format(job_id = job_id,
            batch_id = batch_id)

    headers = {
        "X-SFDC-Session": access_token
    }

    response = requests.get(url, data = None, verify = False, headers = headers)
    batch_status = getUniqueElementValueFromXmlString(response.content, "state")

    if batch_status == "Failed":
        error_message = getUniqueElementValueFromXmlString(response.content, "stateMessage")
        print(batch_id + " failed, because " + error_message)
        return False

    if batch_status != "Completed":
        print(sobject + " is not completed, please continue waiting...")
        time.sleep(15)
        check_batch_status(job_id, batch_id, sobject)

    return True

# Get: https://instance.salesforce.com/services/async/27.0/job/jobId/batch/batchId/result
def get_batch_result_id(sobject, job_id, batch_id):
    url = globals()["instance_url"] +\
        "/services/async/27.0/job/{job_id}/batch/{batch_id}/result".format(job_id = job_id,
            batch_id = batch_id)

    headers = {
        "X-SFDC-Session": access_token
    }

    response = requests.get(url, data = None, verify = False, headers = headers)
    result_id = getUniqueElementValueFromXmlString(response.content, "result")

    return result_id

# Get: https://instance.salesforce.com/services/async/27.0/job/jobId/batch/batchId/result/resultId
def get_batch_result(job_id, batch_id, result_id):
    url = globals()["instance_url"] +\
        "/services/async/27.0/job/{job_id}/batch/{batch_id}/result/{result_id}".format(job_id = job_id,
            batch_id = batch_id, result_id = result_id)

    headers = {
        "X-SFDC-Session": access_token
    }

    response = requests.get(url, data = None, verify = False, headers = headers)

    return response.content

def close_job(job_id):
    url = globals()["instance_url"] + "/services/async/27.0/job/" + job_id
    body = soap_bodies.close_job
    headers = {
        "X-SFDC-Session": globals()["access_token"],
        "Content-Type": "application/xml; charset=UTF-8",
        "Accept": "text/plain"
    }

    response = requests.post(url, body, verify = False, headers = headers)
    return response.status_code

def describe_sobject(sobject):
    print ("describing " + sobject + "......")
    url = globals()["instance_url"] +\
        "/services/data/v27.0/sobjects/{sobject}/describe".format(sobject = sobject)
    headers = {
        "Authorization": "OAuth " + access_token,
        "Content-Type": "application/json",
        "Accept": "text/plain"
    }

    response = requests.get(url, data = None, verify = False, 
        headers = headers)

    return response.json()

NOT_QUERIABLE_FIELD_TYPE = ["location"]
def parse_sobject_describe(sobject_describe):
    sobject_fields = ""
    sobject_name = sobject_describe["name"]
    for field in sobject_describe["fields"]:
        if field.get("type") in NOT_QUERIABLE_FIELD_TYPE:
            continue

        sobject_fields += field.get("name") + ", "

    return 'SELECT ' + sobject_fields[ : -2] + ' FROM ' + sobject_name

def process_bulk_query(sobject, workspace):
    print (SEPARATE)
    sobject_describe = describe_sobject(sobject)
    sobject_soql = parse_sobject_describe(sobject_describe)
    job_id = create_job(sobject, "query")
    batch_id = create_batch(job_id, sobject, sobject_soql)
    
    # Check the batch status, if it is completed, continue
    if check_batch_status(job_id, batch_id, sobject):
        # Get result id and get result by it
        result_id = get_batch_result_id(sobject, job_id, batch_id)
        result = get_batch_result(job_id, batch_id, result_id)

        # Write result into local file
        outputdir = workspace + "/" + sobject + ".csv"
        fp = open(outputdir, "wb")

        try:
            fp.write(result)
        except:
            print(sobject + " is not backuped.")
        finally:
            fp.close()

    # Whatever succeed or not, just delete the job
    status_code = close_job(job_id)
    if status_code < 399:
        sublime.set_timeout(lambda:sublime.status_message("job is deleted."), 10)
    else:
        print(job_id + " is not deleted due to some reason.")

    # Print(these outputdirs to console)
    print(sobject + ": " + outputdir)
    print (SEPARATE)
    
def handle_bulkapi_query(sobjects):
    # Login by user credential in toolingapi_settings
    toolingapi_settings = context.get_toolingapi_settings()
    login(toolingapi_settings, True)
    
    # Create workspace direcotry
    workspace = toolingapi_settings["workspace"] + "/bulkapi"
    if not os.path.exists(workspace):
        os.makedirs(workspace)

    for sobject in sobjects:
        thread = threading.Thread(target=process_bulk_query, args=(sobject, workspace, ))
        thread.start()