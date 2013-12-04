import sublime
import threading
import time
import pprint
import os
import threading
from xml.sax.saxutils import unescape

from .login import soap_login
from . import soap_bodies, xmltodict
from .. import requests, util
from .api import SalesforceApi
from ..util import getUniqueElementValueFromXmlString
from ..progress import ThreadsProgress

class BulkJob():
    def __init__(self, settings, operation, sobject, records=None, external_field=None, **kwargs):
        self.settings = settings
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
                "X-SFDC-Session": result["session_id"],
            }
            globals()[self.username] = result
        else:
            result = globals()[self.username]

        self.base_url = result["instance_url"]  + "/services/async/%s.0" % self.settings["api_version"]
        self.headers = result["headers"]
        self.result = result
        return result

    # Post: https://instance.salesforce.com/services/async/27.0/job
    def create_job(self):
        if not self.login(False): return

        url = self.base_url + "/job"
        body = soap_bodies.create_job.format(operation=self.operation, sobject=self.sobject)
        headers = self.headers 
        headers["Content-Type"] = "application/xml; charset=UTF-8"

        response = requests.post(url, body, verify=False, headers=headers)
        job_id = getUniqueElementValueFromXmlString(response.content, "id")

        return job_id

    # https://instance.salesforce.com/services/async/27.0/job/jobId/batch
    def create_batch(self, job_id):
        url = self.base_url + "/job/%s/batch" % job_id

        headers = self.headers
        headers["Content-Type"] = "text/csv; charset=UTF-8"

        if self.operation == "query" and self.records == None:
            api = SalesforceApi(self.settings)
            self.records = api.combine_soql(self.sobject)

        response = requests.post(url, self.records, verify=False, headers=headers)
        if response.status_code == 400:
            return self.parse_response(response, url)

        batch_id = getUniqueElementValueFromXmlString(response.content, "id")

        return batch_id

    # Get: https://instance.salesforce.com/services/async/27.0/job/jobId
    def check_job_status(self, job_id):
        url = self.base_url + "/job/%s" % job_id
        response = requests.get(url, data=None, verify=False, 
            headers=self.headers)
        job_status = getUniqueElementValueFromXmlString(response.content, "state")

        return job_status

    # Get: https://instance.salesforce.com/services/async/27.0/job/jobId/batch/batchId
    def check_batch_status(self, job_id, batch_id):
        url = self.base_url + "/job/%s/batch/%s" % (job_id, batch_id)
        response = requests.get(url, data=None, verify=False, 
            headers=self.headers)

        # Convert xml to dict
        result = xmltodict.parse(response.content)
        if response.status_code == 400:
            return self.parse_response(response, url)

        result = result["batchInfo"]
        batch_status = result["state"]
        if batch_status == "Failed":
            result["success"] = False
            return result

        return batch_status

    def parse_response(self, response, url):
        result = xmltodict.parse(response.content)
        result = result["error"]
        result["URL"] = url
        result["status_code"] = response.status_code
        result["Operation"] = self.operation
        result["Sobject"] = self.sobject
        return result

    # Get: https://instance.salesforce.com/services/async/27.0/job/jobId/batch/batchId/result
    def get_batch_result_id(self, job_id, batch_id):
        url = self.base_url + "/job/%s/batch/%s/result" % (job_id, batch_id)
        headers = self.headers
        headers["Accept-Encoding"] = 'identity, deflate, compress, gzip'

        response = requests.get(url, data=None, verify=False, headers=headers)
        result_id = getUniqueElementValueFromXmlString(response.content, "result")

        return result_id

    # Get: https://instance.salesforce.com/services/async/27.0/job/jobId/batch/batchId/result/resultId
    def get_batch_result(self, job_id, batch_id, result_id=None):
        if result_id != None:
            # Query action
            url = self.base_url + "/job/%s/batch/%s/result/%s" % (job_id, batch_id, result_id)
        else:
            # Other actions
            url = self.base_url + "/job/%s/batch/%s/result" % (job_id, batch_id)

        headers = self.headers
        headers["Accept-Encoding"] = 'identity, deflate, compress, gzip'

        response = requests.get(url, data=None, verify=False, headers=headers)
        return response.content

    def close_job(self, job_id):
        url = self.base_url + "/job/%s" % job_id
        body = soap_bodies.close_job
        headers = self.headers
        headers["Content-Type"] = "application/xml; charset=UTF-8"

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
        self.write_csv_to_file(result, "query")

    def write_csv_to_file(self, result, operation):
        # Write result to csv
        path = "bulkout" if operation == "query" else "bulkin/log"
        outputdir = self.settings["workspace"] + "/%s" % path
        if not os.path.exists(outputdir):
            os.makedirs(outputdir)

        time_stamp = time.strftime("%Y-%m-%d-%H-%M", time.localtime())
        if operation == "query":
            outputfile = outputdir + "/%s.csv" % (self.sobject)
        else:
            outputfile = outputdir + "/%s-%s-%s.csv" % (self.sobject, operation, time_stamp)
        fp = open(outputfile, "wb")
        try:
            fp = open(outputfile, "wb")
            fp.write(result)
        except:
            if isinstance(result, dict):
                util.format_error_message(dict(result))
            else:
                print (result)
        finally:
            fp.close()

    def insert(self):
        result = self.do_operation('insert')
        self.write_csv_to_file(result, "insert")

    def update(self):
        result = self.do_operation("update")
        self.write_csv_to_file(result, "update")

    def upsert(self):
        result = self.do_operation('upsert')
        self.write_csv_to_file(result, "upsert")

    def delete(self):
        result = self.do_operation('delete')
        self.write_csv_to_file(result, "delete")

    def do_operation(self, operation):
        job = BulkJob(self.settings, operation, self.sobject, self.records, self.external_field)
        job_id = job.create_job()
        result = job.create_batch(job_id)
        if isinstance(result, dict):
            self.result = result
            return result
        
        batch_id = result
        job.close_job(job_id)

        # Check batch status util batch is finished
        while True:
            result = job.check_batch_status(job_id, batch_id)
            if isinstance(result, dict):
                self.result = result
                return self.result
            if result == "Completed": break
            time.sleep(3)

        if operation == "query":
            result_id = job.get_batch_result_id(job_id, batch_id)
            result = job.get_batch_result(job_id, batch_id, result_id)
        else:
            result = job.get_batch_result(job_id, batch_id)

        self.result = result
        return result