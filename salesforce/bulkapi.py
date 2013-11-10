import sublime
import threading
import time
import pprint
import os
import threading
from xml.sax.saxutils import unescape

from .login import soap_login
from . import soap_bodies
from ..util import getUniqueElementValueFromXmlString
from .. import requests
from .api import SalesforceApi
from ..progress import ThreadsProgress


class BulkApi():
    def __init__(self, toolingapi_settings, **kwargs):
        self.toolingapi_settings = toolingapi_settings
        self.api_version = toolingapi_settings["api_version"]
        self.username = toolingapi_settings["username"]
        self.outputdir = toolingapi_settings["workspace"] + "/bulkapi"
        if not os.path.exists(self.outputdir):
            os.makedirs(self.outputdir)
        self.result = None

    def login(self, session_id_expired):
        if self.username not in globals() or session_id_expired:
            result = soap_login(self.toolingapi_settings)

            # If login succeed, display error and return False
            if result["status_code"] > 399:
                result["default_project"] = self.toolingapi_settings["default_project"]["project_name"]
                self.result = result
                return False

            result["headers"] = {
                "Authorization": "OAuth " + result["session_id"],
                "Content-Type": "application/json; charset=UTF-8",
                "Accept": "application/json"
            }
            globals()[self.username] = result
        else:
            result = globals()[self.username]

        self.result = result
        return result

    # Post: https://instance.salesforce.com/services/async/27.0/job
    def create_job(self, sobject, operation):
        url = globals()[self.username]["instance_url"] +\
            "/services/async/%s.0/job" % self.api_version
        body = soap_bodies.create_job.format(operation=operation, sobject=sobject)
        headers = {
            "X-SFDC-Session": globals()[self.username]["session_id"],
            "Content-Type": "application/xml; charset=UTF-8",
            "Accept": "text/plain"
        }

        response = requests.post(url, body, verify=False, headers=headers)
        job_id = getUniqueElementValueFromXmlString(response.content, "id")

        if job_id == None:
            print (sobject + " is not valid sobject, please check.")

        return job_id

    # https://instance.salesforce.com/services/async/27.0/job/jobId/batch
    def create_batch(self, job_id, sobject, sobject_soql):
        url = globals()[self.username]["instance_url"] +\
            "/services/async/%s.0/job/%s/batch" % (self.api_version, job_id)

        headers = {
            "X-SFDC-Session": globals()[self.username]["session_id"],
            "Content-Type": "text/csv; charset=UTF-8"
        }
        
        response = requests.post(url, sobject_soql, verify=False, headers=headers)
        batch_id = getUniqueElementValueFromXmlString(response.content, "id")

        return batch_id

    # Get: https://instance.salesforce.com/services/async/27.0/job/jobId
    def check_job_status(self, job_id):
        url = globals()[self.username]["instance_url"] + "/services/async/%s.0/job/%s" % (self.api_version, job_id)

        headers = {
            "X-SFDC-Session": globals()[self.username]["session_id"]
        }

        response = requests.get(url, data=None, verify=False, headers=headers)
        job_status = getUniqueElementValueFromXmlString(response.content, "state")

        while job_status != "Completed":
            print(job_id + " is not completed, please continue waiting...")
            time.sleep(15)
            check_job_status(job_id)

        return True

    # Get: https://instance.salesforce.com/services/async/27.0/job/jobId/batch/batchId
    def check_batch_status(self, job_id, batch_id, sobject):
        url = globals()[self.username]["instance_url"] +\
            "/services/async/%s.0/job/%s/batch/%s" % (self.api_version, job_id, batch_id)

        headers = {
            "X-SFDC-Session": globals()[self.username]["session_id"]
        }

        response = requests.get(url, data=None, verify=False, headers=headers)
        batch_status = getUniqueElementValueFromXmlString(response.content, "state")

        if batch_status == "Failed":
            error_message = getUniqueElementValueFromXmlString(response.content, "stateMessage")
            print(batch_id + " failed, because " + error_message)
            return False

        while batch_status != "Completed":
            print(sobject + " is not completed, please continue waiting...")
            time.sleep(15)
            return self.check_batch_status(job_id, batch_id, sobject)

        return True

    # Get: https://instance.salesforce.com/services/async/27.0/job/jobId/batch/batchId/result
    def get_batch_result_id(self, sobject, job_id, batch_id):
        url = globals()[self.username]["instance_url"] +\
            "/services/async/%s.0/job/%s/batch/%s/result" % (self.api_version, job_id, batch_id)

        headers = {
            "X-SFDC-Session": globals()[self.username]["session_id"],
        }

        response = requests.get(url, data=None, verify=False, headers=headers)
        result_id = getUniqueElementValueFromXmlString(response.content, "result")

        return result_id

    # Get: https://instance.salesforce.com/services/async/27.0/job/jobId/batch/batchId/result/resultId
    def get_batch_result(self, job_id, batch_id, result_id):
        url = globals()[self.username]["instance_url"] +\
            "/services/async/%s.0/job/%s/batch/%s/result/%s" %\
                (self.api_version, job_id, batch_id, result_id)

        headers = {
            "X-SFDC-Session": globals()[self.username]["session_id"],
            "Accept-Encoding": 'identity, deflate, compress, gzip'
        }

        response = requests.get(url, data=None, verify=False, headers=headers)
        return response.content

    def close_job(self, job_id):
        url = globals()[self.username]["instance_url"] + "/services/async/%s.0/job/%s" % (self.api_version, job_id)
        body = soap_bodies.close_job
        headers = {
            "X-SFDC-Session": globals()[self.username]["session_id"],
            "Content-Type": "application/xml; charset=UTF-8",
            "Accept": "text/plain"
        }

        response = requests.post(url, body, verify=False, headers=headers)
        return response.status_code

    def do_operation(self, operation, sobject, api):
        sobject_soql = api.combine_soql(sobject)
        job_id = self.create_job(sobject, operation)
        batch_id = self.create_batch(job_id, sobject, sobject_soql)
        
        # Check the batch status, if it is completed, continue
        if self.check_batch_status(job_id, batch_id, sobject):
            # Get result id and get result by it
            result_id = self.get_batch_result_id(sobject, job_id, batch_id)
            result = self.get_batch_result(job_id, batch_id, result_id)

            # Write result into local file
            outputfile = self.outputdir + "/" + sobject + ".csv"
            fp = open(outputfile, "wb")

            try:
                fp.write(result)
                print (outputfile)
            except:
                print(sobject + " is not backuped.")
            finally:
                fp.close()

        # Whatever succeed or not, just delete the job
        status_code = self.close_job(job_id)
        if status_code < 399:
            sublime.set_timeout(lambda:sublime.status_message("job is deleted."), 10)
        else:
            print(job_id + " is not deleted due to some reason.")

    def do_query_all(self, sobjects=None):
        if not self.login(False): return
        api = SalesforceApi(self.toolingapi_settings)
        if sobjects == None:
            sobjects = api.describe_global_common()

        threads = []
        for sobject in sobjects:
            thread = threading.Thread(target=self.do_operation, args=('query', sobject, api, ))
            thread.start()
            threads.append(thread)

        ThreadsProgress(threads, "Exporting Records", "Exporting Records Succeed")