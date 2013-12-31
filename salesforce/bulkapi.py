import sublime
import threading
import time
import pprint
import os
import csv
import re
import threading
from xml.sax.saxutils import unescape

from .login import soap_login
from . import soap_bodies, xmltodict
from .. import requests, util
from .api import SalesforceApi
from ..util import getUniqueElementValueFromXmlString
from ..progress import ThreadsProgress

class BulkJob():
    def __init__(self, settings, operation, sobject, external_field=None, **kwargs):
        self.settings = settings
        self.username = settings["username"]
        self.operation = operation
        self.sobject = sobject
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
        self.job_id = getUniqueElementValueFromXmlString(response.content, "id")

    # https://instance.salesforce.com/services/async/27.0/job/jobId/batch
    def create_batch(self, records=None):
        url = self.base_url + "/job/%s/batch" % self.job_id

        headers = self.headers
        headers["Content-Type"] = "text/csv; charset=UTF-8"

        if self.operation == "query" and not records:
            api = SalesforceApi(self.settings)
            records = api.combine_soql(self.sobject)

        response = requests.post(url, records, verify=False, headers=headers)
        if response.status_code == 400:
            return self.parse_response(response, url)

        batch_id = getUniqueElementValueFromXmlString(response.content, "id")

        return batch_id

    # Get: https://instance.salesforce.com/services/async/27.0/job/jobId
    def check_job_status(self):
        url = self.base_url + "/job/%s" % self.job_id
        response = requests.get(url, data=None, verify=False, 
            headers=self.headers)
        job_status = getUniqueElementValueFromXmlString(response.content, "state")

        return job_status

    # Get: https://instance.salesforce.com/services/async/27.0/job/jobId/batch/batchId
    def check_batch_status(self, batch_id):
        url = self.base_url + "/job/%s/batch/%s" % (self.job_id, batch_id)
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
    def get_batch_result_id(self, batch_id):
        url = self.base_url + "/job/%s/batch/%s/result" % (self.job_id, batch_id)
        headers = self.headers
        headers["Accept-Encoding"] = 'identity, deflate, compress, gzip'

        response = requests.get(url, data=None, verify=False, headers=headers)
        result_id = getUniqueElementValueFromXmlString(response.content, "result")

        return result_id

    # Get: https://instance.salesforce.com/services/async/27.0/job/jobId/batch/batchId/result/resultId
    def get_batch_result(self, batch_id, result_id=None):
        if result_id != None:
            # Query action
            url = self.base_url + "/job/%s/batch/%s/result/%s" % (self.job_id, batch_id, result_id)
        else:
            # Other actions
            url = self.base_url + "/job/%s/batch/%s/result" % (self.job_id, batch_id)

        headers = self.headers
        headers["Accept-Encoding"] = 'identity, deflate, compress, gzip'

        response = requests.get(url, data=None, verify=False, headers=headers)
        return response.content

    def close_job(self):
        url = self.base_url + "/job/%s" % self.job_id
        body = soap_bodies.close_job
        headers = self.headers
        headers["Content-Type"] = "application/xml; charset=UTF-8"

        response = requests.post(url, body, verify=False, headers=headers)
        return response.status_code

class BulkApi():
    def __init__(self, settings, sobject, inputfile=None, external_field=None):
        self.settings = settings
        self.sobject = sobject
        self.inputfile = inputfile
        self.external_field = external_field
        self.result = None
    
    def query(self):
        # Get batch result
        result = self.do_operation('query')
        self.write_csv_to_file(result, "query")

    def write_csv_to_file(self, result, operation):
        # Write result to csv
        time_stamp = time.strftime("%Y-%m-%d-%H-%M", time.localtime())
        if self.inputfile:
            outputfile = os.path.dirname(self.inputfile) +\
                "/log/%s-%s-%s.csv" % (self.sobject, operation, time_stamp)
        else:
            outputfile = self.settings["workspace"] + "/bulkout/%s.csv" % (self.sobject)

        if not os.path.exists(os.path.dirname(outputfile)):
            os.mkdir(os.path.dirname(outputfile))

        if isinstance(result, dict):
            sublime.active_window().run_command("show_panel", 
                {"panel": "console", "toggle": False})
            util.format_error_message(dict(result))
        else:
            try:
                fp = open(outputfile, "wb")
                fp.write(u'\ufeff'.encode('utf8'))
                fp.write(result)
            except:
                print (sobject + " export is failed")
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
    
    def detect_bom(self, inputfile):
        # Detect BOM Header
        csvfile = open(inputfile, "rb")
        has_bom = True if csvfile.read(3) == b'\xef\xbb\xbf' else False

        return has_bom

    def create_batchs(self, job, inputfile):
        maxBytesPerBatch = self.settings["maximum_batch_bytes"] 
        maxRowsPerBatch = self.settings["maximum_batch_size"] 

        batch_ids = [] # Batch List

        # Reader Content
        currentBytes = 0
        currentLines = 0
        batchRecord = ""
        headerBytesLength = 0
        try:
            # Assume file encoding is utf-8
            csvfile = open(inputfile, encoding="utf-8")
            if self.detect_bom(inputfile): csvfile.seek(3)
            reader = csv.reader(csvfile)
            for row in reader: 
                header = ",".join(row) + "\n"
                headerBytesLength = len(header)
                break
        except:
            reader = csv.reader(open(inputfile))
            for row in reader:
                header = ",".join(row) + "\n"
                headerBytesLength = len(header)
                break
        else:
            pass

        for row in reader:
            rowLength = len(str(row) + "\n")
            if len(batchRecord) > maxBytesPerBatch or currentLines > maxRowsPerBatch:
                batch_id = job.create_batch(batchRecord.encode("utf-8"))
                batch_ids.append(batch_id)
                batchRecord = ""
                currentBytes = 0;
                currentLines = 0;

            if currentBytes == 0:
                batchRecord += header
                currentBytes = headerBytesLength;
                currentLines = 1;

            batchRecord += ",".join(row) + "\n"
            currentBytes += rowLength
            currentLines = currentLines + 1

        if currentLines > 1:
            batch_id = job.create_batch(batchRecord.encode("utf-8"))
            batch_ids.append(batch_id)

        return batch_ids

    def combine_results(self, results):
        combined_result = results[0]
        for result in results[1:]:
            result = result.replace(b'"Id","Success","Created","Error"\n', b"")
            combined_result += result

        return combined_result

    def do_operation(self, operation):
        job = BulkJob(self.settings, operation, self.sobject, self.external_field)
        job.create_job()
        if not self.inputfile:
            batch_ids = [job.create_batch()]
        else:
            batch_ids = self.create_batchs(job, self.inputfile)
        for batch_id in batch_ids:
            if isinstance(batch_id, dict):
                self.result = batch_id
                return self.result
        
        # Close job
        job.close_job()

        # Check batch status until all batchs are finished
        for batch_id in batch_ids:
            while True:
                result = job.check_batch_status(batch_id)
                if isinstance(result, dict):
                    self.result = result
                    return self.result
                if result == "Completed": break
                time.sleep(3)

        if operation == "query":
            result_id = job.get_batch_result_id(batch_id)
            result = job.get_batch_result(batch_id, result_id)
        else:
            results = []
            for batch_id in batch_ids:
                result = job.get_batch_result(batch_id)
                results.append(result)

            result = self.combine_results(results)

        self.result = result
        return result