import sublime
import time
import pprint
import os
import csv

from ..login import soap_login, rest_login
from ..soap import SOAP
from .. import xmltodict
from ... import requests, util
from ..api.tooling import ToolingApi
from ..lib.panel import Printer

class BulkApi():
    def __init__(self, settings, sobject, input=None, external_field=None):
        self.settings = settings
        self.sobject = sobject
        self.input = input
        self.external_field = external_field
        self.result = None
        self.job = None
    
    def query(self):
        # Get batch result
        result = self.do_operation('query')
        self.write_csv_to_file(result, "query")

    def write_csv_to_file(self, result, operation):
        # Write result to csv
        time_stamp = time.strftime("%Y%m%d%H%M", time.localtime())
        if operation != "query":
            outputfile = os.path.dirname(self.input) +\
                "/log/%s-%s-%s.csv" % (self.sobject, operation, time_stamp)
        else:
            outputfile = self.settings["workspace"] + "/bulkout/%s.csv" % (self.sobject)

        if not os.path.exists(os.path.dirname(outputfile)):
            os.mkdir(os.path.dirname(outputfile))

        if isinstance(result, dict):
            Printer.get("error").write(result["stateMessage"])
        else:
            try:
                fp = open(outputfile, "wb")
                fp.write(u'\ufeff'.encode('utf8'))
                fp.write(result)
            except:
                print(self.sobject + " export is failed")
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
    
    def read_csv(self, input):
        from ...requests.packages import chardet
        with open(input, "rb") as csvfile:
            if csvfile.read(3) == b'\xef\xbb\xbf':
                encoding = 'utf-8'
            else:
                chardet_result = chardet.detect(csvfile.read(1000))
                encoding = chardet_result["encoding"]

        if encoding and "utf" in encoding.lower():
            csvfile = open(input, encoding=encoding)
            reader = csv.reader(csvfile)
        else:
            reader = csv.reader(open(input))

        return reader

    def create_batchs(self, job, input):
        maxBytesPerBatch = self.settings["maximum_batch_bytes"] 
        maxRowsPerBatch = self.settings["maximum_batch_size"] 

        # Reader Content
        currentBytes = 0
        currentLines = 0
        batchRecord = ""
        batch_ids = []
        reader = self.read_csv(input)
        for row in reader:
            if reader.line_num == 1:
                if "\ufeff" in row[0]:
                    row[0] = row[0].replace("\ufeff", "").replace('"', '')
                header = ",".join(row) + "\n"
                headerBytesLength = len(header)
                continue

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
        self.job = BulkJob(self.settings, operation, self.sobject, self.external_field)
        self.job.create_job()
        if operation == "query" and self.input:
            batch_ids = [self.job.create_batch(self.input)]
        elif operation == "query" and not self.input:
            batch_ids = [self.job.create_batch()]
        else:
            batch_ids = self.create_batchs(self.job, self.input)

        for batch_id in batch_ids:
            if isinstance(batch_id, dict):
                self.result = batch_id
                return self.result
        
        # Close job
        self.job.close_job()

        # Check batch status until all batchs are finished
        for batch_id in batch_ids:
            while True:
                result = self.job.check_batch_status(batch_id)
                if isinstance(result, dict):
                    self.result = result
                    return self.result
                if result: break

        if operation == "query":
            result_id = self.job.get_batch_result_id(batch_id)
            result = self.job.get_batch_result(batch_id, result_id)
        else:
            results = []
            for batch_id in batch_ids:
                result = self.job.get_batch_result(batch_id)
                results.append(result)

            result = self.combine_results(results)

        self.result = result
        return result

class BulkJob():
    def __init__(self, settings, operation, sobject, external_field=None, **kwargs):
        self.settings = settings
        self.operation = operation
        self.sobject = sobject
        self.soap = SOAP(settings)
        self.batchs = []
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
        if self.settings["login_type"] == "REST":
            result = rest_login(self.settings, session_id_expired)
        else:
            result = soap_login(self.settings, session_id_expired)
        if not result["success"]:
            self.result = result
            return self.result

        self.base_url = result["instance_url"]  + "/services/async/%s.0" % self.settings["api_version"]
        self.headers = {
            "X-SFDC-Session": result["session_id"],
            "Content-Type": "application/xml; charset=UTF-8"
        }
        self.result = result
        return result

    # Post: https://instance.salesforce.com/services/async/27.0/job
    def create_job(self):
        result = self.login()
        if not result["success"]:
            self.result = result
            return self.result

        url = self.base_url + "/job"
        body = self.soap.create_request('new_job', {
            "operation": self.operation, 
            "sobject": self.sobject,
            "mode": "Parallel",
            "content_type": "CSV"
        })
        response = requests.post(url, body, verify=False, headers=self.headers)
        self.job_id = util.getUniqueElementValueFromXmlString(response.content, "id")

    # https://instance.salesforce.com/services/async/27.0/job/jobId/batch
    def create_batch(self, records=None):
        url = self.base_url + "/job/%s/batch" % self.job_id

        headers = self.headers
        headers["Content-Type"] = "text/csv; charset=UTF-8"

        if self.operation == "query" and not records:
            api = ToolingApi(self.settings)
            result = api.combine_soql(self.sobject, contains_compound=False)
            records = result["soql"]

        if not isinstance(records, bytes): records = records.encode("utf-8")
        response = requests.post(url, records, verify=False, headers=headers)
        if response.status_code == 400:
            result = self.parse_response(response, url)
            result["operation"] = self.operation
            result["action"] = "Create Batch"
            result["success"] = False
            return result

        self.batchs.append(xmltodict.parse(response.text))
        batch_id = util.getUniqueElementValueFromXmlString(response.content, "id")

        return batch_id

    # Get: https://instance.salesforce.com/services/async/27.0/job/jobId
    def check_job_status(self):
        url = self.base_url + "/job/%s" % self.job_id
        response = requests.get(url, data=None, verify=False, headers=self.headers)
        job_status = util.getUniqueElementValueFromXmlString(response.content, "state")

        return job_status

    # Get: https://instance.salesforce.com/services/async/27.0/job/jobId/batch/batchId
    def check_batch_status(self, batch_id):
        url = self.base_url + "/job/%s/batch/%s" % (self.job_id, batch_id)
        response = requests.get(url, data=None, verify=False, headers=self.headers)

        # Convert xml to dict
        result = xmltodict.parse(response.content)
        if response.status_code == 400:
            result = self.parse_response(response, url)
            result["success"] = False
            result["action"] = "Check Batch Status"
            result["success"] = False
            return result

        result = result["batchInfo"]
        batch_status = result["state"]
        if batch_status == "Failed":
            result["success"] = False
            result["operation"] = self.operation
            result["action"] = "Check Batch Status"
            result["success"] = False
            return result

        return batch_status == "Completed"

    def parse_response(self, response, url):
        result = xmltodict.parse(response.content)
        result = result["error"]
        result["URL"] = url
        result["operation"] = self.operation
        result["sobject"] = self.sobject
        result["success"] = False
        return result

    # Get: https://instance.salesforce.com/services/async/27.0/job/jobId/batch/batchId/result
    def get_batch_result_id(self, batch_id):
        url = self.base_url + "/job/%s/batch/%s/result" % (self.job_id, batch_id)
        headers = self.headers
        headers["Accept-Encoding"] = 'identity, deflate, compress, gzip'

        response = requests.get(url, data=None, verify=False, headers=headers)
        result_id = util.getUniqueElementValueFromXmlString(response.content, "result")

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

    def close_job(self, job_id=None):
        # Login firstly
        result = self.login()
        if not result["success"]:
            self.result = result
            return self.result

        if job_id: self.job_id = job_id
        
        url = self.base_url + "/job/%s" % self.job_id
        soap_body = self.soap.create_request("close_job", {"state": "Closed"})

        response = requests.post(url, soap_body, verify=False, headers=self.headers)
        return response.status_code