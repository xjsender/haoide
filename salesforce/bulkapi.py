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

class BulkJob():
    def __init__(self, settings, operation, sobject, records=None, external_field=None, **kwargs):
        self.settings = settings
        self.api_version = settings["api_version"]
        self.username = settings["username"]
        self.operation = operation
        self.sobject = sobject
        self.records = records
        self.result = None
        
    def login(self, session_id_expired):
        if self.username not in globals() or session_id_expired:
            result = soap_login(self.settings)

            # If login succeed, display error and return False
            if result["status_code"] > 399:
                result["default_project"] = self.settings["default_project"]["project_name"]
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
    def create_job(self):
        if not self.login(False): return
        url = "%s/services/async/%s.0/job" %\
            (globals()[self.username]["instance_url"], self.api_version)
        body = soap_bodies.create_job.format(operation=self.operation, sobject=self.sobject)
        headers = {
            "X-SFDC-Session": globals()[self.username]["session_id"],
            "Content-Type": "application/xml; charset=UTF-8",
            "Accept": "text/plain"
        }

        response = requests.post(url, body, verify=False, headers=headers)
        job_id = getUniqueElementValueFromXmlString(response.content, "id")

        return job_id

    # https://instance.salesforce.com/services/async/27.0/job/jobId/batch
    def create_batch(self, job_id):
        url = "%s/services/async/%s.0/job/%s/batch" %\
            (globals()[self.username]["instance_url"], self.api_version, job_id)

        headers = {
            "X-SFDC-Session": globals()[self.username]["session_id"],
            "Content-Type": "text/csv; charset=UTF-8"
        }

        if self.operation == "query" and self.records == None:
            api = SalesforceApi(self.settings)
            self.records = api.combine_soql(self.sobject)

        response = requests.post(url, self.records, verify=False, headers=headers)
        batch_id = getUniqueElementValueFromXmlString(response.content, "id")

        return batch_id

    # Get: https://instance.salesforce.com/services/async/27.0/job/jobId
    def check_job_status(self, job_id):
        url = "%s/services/async/%s.0/job/%s" %\
            (globals()[self.username]["instance_url"], self.api_version, job_id)

        headers = {
            "X-SFDC-Session": globals()[self.username]["session_id"]
        }

        response = requests.get(url, data=None, verify=False, headers=headers)
        job_status = getUniqueElementValueFromXmlString(response.content, "state")

        return job_status

    # Get: https://instance.salesforce.com/services/async/27.0/job/jobId/batch/batchId
    def check_batch_status(self, job_id, batch_id):
        url = "%s/services/async/%s.0/job/%s/batch/%s" %\
            (globals()[self.username]["instance_url"], self.api_version, job_id, batch_id)
        headers = {
            "X-SFDC-Session": globals()[self.username]["session_id"]
        }

        response = requests.get(url, data=None, verify=False, headers=headers)
        batch_status = getUniqueElementValueFromXmlString(response.content, "state")
        if batch_status == "Failed":
            error_message = getUniqueElementValueFromXmlString(response.content, "stateMessage")
            return (batch_status, error_message)

        return (batch_status, None)

    # Get: https://instance.salesforce.com/services/async/27.0/job/jobId/batch/batchId/result
    def get_batch_result_id(self, job_id, batch_id):
        url = "%s/services/async/%s.0/job/%s/batch/%s/result" %\
            (globals()[self.username]["instance_url"], self.api_version, job_id, batch_id)

        headers = {
            "X-SFDC-Session": globals()[self.username]["session_id"],
        }

        response = requests.get(url, data=None, verify=False, headers=headers)
        result_id = getUniqueElementValueFromXmlString(response.content, "result")

        return result_id

    # Get: https://instance.salesforce.com/services/async/27.0/job/jobId/batch/batchId/result/resultId
    def get_batch_result(self, job_id, batch_id, result_id):
        url = "%s/services/async/%s.0/job/%s/batch/%s/result/%s" %\
            (globals()[self.username]["instance_url"], self.api_version, job_id, batch_id, result_id)
        headers = {
            "X-SFDC-Session": globals()[self.username]["session_id"],
            "Accept-Encoding": 'identity, deflate, compress, gzip'
        }

        response = requests.get(url, data=None, verify=False, headers=headers)
        return response.content

    def close_job(self, job_id):
        url = "%s/services/async/%s.0/job/%s" %\
            (globals()[self.username]["instance_url"], self.api_version, job_id)
        body = soap_bodies.close_job
        headers = {
            "X-SFDC-Session": globals()[self.username]["session_id"],
            "Content-Type": "application/xml; charset=UTF-8",
            "Accept": "text/plain"
        }

        response = requests.post(url, body, verify=False, headers=headers)
        return response.status_code

class BulkApi():
    def __init__(self, settings, sobject, records=None, external_field=None):
        self.settings = settings
        self.sobject = sobject
        self.records = records
        self.external_field = external_field
        self.result = None
    
    def query(self):
        # Get batch result
        result = self.do_operation('query')

        # Write result to csv
        outputdir = self.settings["workspace"] + "/bulkout"
        if not os.path.exists(outputdir):
            os.makedirs(outputdir)
        outputfile = outputdir + "/%s.csv" % self.sobject
        fp = open(outputfile, "wb")
        try:
            fp.write(result)
            sublime.status_message(outputfile)
        except:
            print (self.sobject + ".csv failed")
        finally:
            fp.close()

    def create(self):
        result = self.do_operation('create')

    def update(self):
        result = self.do_operation('update')

    def upsert(self):
        result = self.do_operation('upsert')

    def delete(self):
        result = self.do_operation('delete')

    def do_operation(self, operation):
        job = BulkJob(self.settings, operation, self.sobject, self.records, self.external_field)
        job_id = job.create_job()
        batch_id = job.create_batch(job_id)
        job.close_job(job_id)

        # Check batch status util batch is finished
        while True:
            state, message = job.check_batch_status(job_id, batch_id)
            if state == "Completed": break
            time.sleep(3)

        result_id = job.get_batch_result_id(job_id, batch_id)
        result = job.get_batch_result(job_id, batch_id, result_id)

        self.result = result
        return result