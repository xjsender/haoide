import os
import json

from .. import util
from .. import context
from .lib import xmlformatter
from .login import soap_login
from .lib.panel import Printer

"""
from .salesforce.soap import SOAP
from . import context

settings = context.get_settings()
soap = SOAP(settings)
soap.create_request('readMetadata', {
    "types": {
        "CustomObject": ["haoliu__Expense__c"]
    }
})
"""

class SOAP():
    def __init__(self, settings, indent=4, **kwargs):
        self.settings = settings
        self.indent = indent

    def get_session_id(self):
        session = util.get_session_info(self.settings)
        if not session:
            print (session)
            result = soap_login(self.settings, True)
            if not result["success"]:
                Printer.get('error').write(result["message"])
            session_id = None
        else:
            session_id = session["session_id"]

        return session_id

    # Format the request body
    def format_request_envelope(self, request_body):
        try:
            formatter = xmlformatter.Formatter(indent=self.indent)
            formatted_body = formatter.format_string(request_body)
        except Exception as ex:
            if self.settings["debug_mode"]: 
                print ("[Format Request Body] " + str(ex))
            formatted_body = request_body

        return formatted_body

    # Dynamically invoke function by name
    def create_request(self, request_type, options={}):
        soap_body = getattr(self, "create_%s_request" % request_type)(options)
        if self.settings["debug_mode"]:
            print ("[Debug for {request_type}]: \n{seprate}\n{content}\n{seprate}".format(
                seprate="~" * 100,
                request_type=request_type,
                content=soap_body.decode("UTF-8")
            ))
        return soap_body

    ##############################################
    # Metadata API Request
    ##############################################
    def create_metadata_envelope(self, body):
        metadata_request_envelope = """<?xml version="1.0" encoding="UTF-8"?>
            <soapenv:Envelope 
                xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
                xmlns:met="http://soap.sforce.com/2006/04/metadata">
            <soapenv:Header>
                <met:SessionHeader>
                    <met:sessionId>{session_id}</met:sessionId>
                </met:SessionHeader>
            </soapenv:Header>
            <soapenv:Body>
                {body}
            </soapenv:Body>
        </soapenv:Envelope>""".format(session_id=self.get_session_id(), body=body)
        
        return self.format_request_envelope(metadata_request_envelope)

    def create_check_status_request(self, options):
        check_status_body = """
            <met:checkStatus>
               <met:asyncProcessId>{async_process_id}</met:asyncProcessId>
            </met:checkStatus>
        """.format(**options)

        return self.create_metadata_envelope(check_status_body)

    def create_check_retrieve_status_request(self, options):
        check_retrieve_status_request_body = """
            <met:checkRetrieveStatus>
               <met:asyncProcessId>{async_process_id}</met:asyncProcessId>
            </met:checkRetrieveStatus>
        """.format(**options)

        return self.create_metadata_envelope(check_retrieve_status_request_body)

    def create_cancelDeploy_request(self, options):
        cancel_deploy_request_body = """
            <met:cancelDeploy>
                <met:String>{async_process_id}</met:String>
            </met:cancelDeploy>
        """.format(**options)

        return self.create_metadata_envelope(cancel_deploy_request_body)

    def create_check_deploy_status_request(self, options):
        check_deploy_status_request_body = """
            <met:checkDeployStatus>
                <met:asyncProcessId>{async_process_id}</met:asyncProcessId>
                <met:includeDetails>true</met:includeDetails>
            </met:checkDeployStatus>
        """.format(**options)

        return self.create_metadata_envelope(check_deploy_status_request_body)

    def create_deleteMetadata_request(self, options):
        """ Just support deletion of components of one type, for example,

            {
                "ApexClass": ["TestClass", "TestClass2"]
            }

        Has below exception, why?
            INVALID_TYPE: This type of metadata is not available for this organization
        """
        types = options["types"]
        for t in types:
            meta_type = t
            elements = ["<met:fullNames>%s</met:fullNames>" % e for e in types[t]]

        delete_metadata_body = """
            <met:deleteMetadata>
                <met:type>{0}</met:type>
                {1}
            </met:deleteMetadata>
        """.format(meta_type, "".join(elements))

        return self.create_metadata_envelope(delete_metadata_body)

    def create_readMetadata_request(self, options):
        """ Just support deletion of components of one type, for example,

            {
                "ApexClass": ["TestClass", "TestClass2"]
            }

        Has below exception, why?
            INVALID_TYPE: This type of metadata is not available for this organization
        """
        types = options["types"]
        for t in types:
            meta_type = t
            elements = ["<met:fullNames>%s</met:fullNames>" % e for e in types[t]]

        read_metadata_body = """
            <met:readMetadata>
                <met:type>{0}</met:type>
                {1}
            </met:readMetadata>
        """.format(meta_type, "".join(elements))

        return self.create_metadata_envelope(read_metadata_body)

    def create_renameMetadata_request(self, options):
        """ Just support deletion of components of one type, for example,

            {
                "type": "ApexClass",
                "old_name": "TestClass",
                "new_name": "TestClass1"
            }

        Has below exception, why?
            INVALID_TYPE: This type of metadata is not available for this organization
        """
        rename_metadata_body = """
            <met:renameMetadata>
                <met:type>{type}</met:type>
                <met:oldFullName>{old_name}</met:oldFullName>
                <met:newFullName>{new_name}</met:newFullName>
            </met:renameMetadata>
        """.format(**options)

        return self.create_metadata_envelope(rename_metadata_body)

    def create_describeMetadata_request(self, options):
        describe_metadata_body = """
            <met:describeMetadata>
                <met:asOfVersion>%s</met:asOfVersion>
            </met:describeMetadata>
        """ % self.settings["api_version"]

        return self.create_metadata_envelope(describe_metadata_body)

    def create_deploy_request(self, options):
        deploy_request_body = """
            <met:deploy>
                <met:ZipFile>{zipfile}</met:ZipFile>
                <met:DeployOptions>
                    <met:allowMissingFiles>{allowMissingFiles}</met:allowMissingFiles>
                    <met:autoUpdatePackage>{autoUpdatePackage}</met:autoUpdatePackage>
                    <met:checkOnly>{checkOnly}</met:checkOnly>
                    <met:ignoreWarnings>{ignoreWarnings}</met:ignoreWarnings>
                    <met:performRetrieve>{performRetrieve}</met:performRetrieve>
                    <met:purgeOnDelete>{purgeOnDelete}</met:purgeOnDelete>
                    <met:rollbackOnError>{rollbackOnError}</met:rollbackOnError>
                    <met:testLevel>{testLevel}</met:testLevel>
                    {runTests}
                    <met:singlePackage>{singlePackage}</met:singlePackage>
                </met:DeployOptions>
            </met:deploy>
        """.format(**options)

        return self.create_metadata_envelope(deploy_request_body)

    def create_sobjects_workflow_request(self, options):
        types = {} # Define types
        for xml_name in ["Workflow", "CustomObject"]:
            types[xml_name] = ["*"]

        return self.create_retrieve_request(types)

    def create_list_package_request(self, options):
        queries = []
        types = options["types"]
        for _type in types:
            for folder in types[_type]:
                if not folder:
                    queries.append(
                        """
                            <met:queries>
                                <met:type>%s</met:type>
                            </met:queries>
                        """ % _type
                    )
                else:
                    queries.append(
                        """
                            <met:queries>
                                <met:type>%s</met:type>
                                <met:folder>%s</met:folder>
                            </met:queries>
                        """ % (_type, folder)
                    )

        list_package_request_body = """
            <met:listMetadata>
                {queries}
                <met:asOfVersion>{api_version}.0</met:asOfVersion>
            </met:listMetadata>
        """.format(
            queries="".join(queries), 
            api_version=self.settings["api_version"]
        )

        return self.create_metadata_envelope(list_package_request_body)

    def create_retrieve_request(self, options):
        packages = ""
        if "package_names" in options:
            packages = "".join(["<met:packageNames>%s</met:packageNames>" % pn \
                for pn in options["package_names"]])

        metadata_objects = []
        types = options["types"]
        for _type in types:
            metadata_objects.append(
                "<met:types>%s<name>%s</name></met:types>" % (
                    "".join(["<met:members>%s</met:members>" % m for m in types[_type]]),
                    _type
                )
            )

        retrieve_request_body = """
            <met:retrieve>
                <met:retrieveRequest>
                    <met:apiVersion>{api_version}.0</met:apiVersion>
                    {packages}
                    <met:unpackaged>{metadata_objects}</met:unpackaged>
                </met:retrieveRequest>
            </met:retrieve>
        """.format(
            api_version=self.settings["api_version"],
            packages=packages,
            metadata_objects="".join(metadata_objects)
        )

        return self.create_metadata_envelope(retrieve_request_body)

    ##############################################
    # Bulk API Request
    ##############################################
    def create_close_job_request(self, options):
        close_job_request_envelope = """<?xml version="1.0" encoding="UTF-8"?>
            <jobInfo xmlns="http://www.force.com/2009/06/asyncapi/dataload">
                <state>{state}</state>
            </jobInfo>
        """.format(**options)

        return self.format_request_envelope(close_job_request_envelope)

    def create_new_job_request(self, options):
        new_job_request_envelope = """<?xml version="1.0" encoding="UTF-8"?>
            <jobInfo xmlns="http://www.force.com/2009/06/asyncapi/dataload">
                <operation>{operation}</operation>
                <object>{sobject}</object>
                <concurrencyMode>{mode}</concurrencyMode>
                <contentType>{content_type}</contentType>
            </jobInfo>
        """.format(**options)

        return self.format_request_envelope(new_job_request_envelope)

    ##############################################
    # Apex API Request
    ##############################################
    def create_apex_envelope(self, body, need_format=True):
        log_levels = ""
        for log_level in self.settings["anonymous_log_levels"]:
            log_levels += """
                <apex:categories>
                    <apex:category>%s</apex:category>
                    <apex:level>%s</apex:level>
                </apex:categories>
            """ % (log_level["log_category"], log_level["log_level"])

        apex_request_envelope = """<soapenv:Envelope 
            xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
            xmlns:apex="http://soap.sforce.com/2006/08/apex">
            <soapenv:Header>
                <apex:DebuggingHeader>
                    {log_levels}
                </apex:DebuggingHeader>
                <apex:SessionHeader>
                    <apex:sessionId>{session_id}</apex:sessionId>
                </apex:SessionHeader>
            </soapenv:Header>
            <soapenv:Body>
                {body}
            </soapenv:Body>
        </soapenv:Envelope>
        """.format(log_levels=log_levels, session_id=self.get_session_id(), body=body)

        if need_format:
            return_body = self.format_request_envelope(apex_request_envelope)
        else:
            return_body = apex_request_envelope.encode("utf-8")

        return return_body

    def create_execute_anonymous_request(self, options):
        execute_anonymous_request_body = """
            <apex:executeAnonymous>
                <apex:String>{apex_string}</apex:String>
            </apex:executeAnonymous>
        """.format(**options)

        return self.create_apex_envelope(execute_anonymous_request_body, False)

    def create_run_all_test_request(self, options):
        run_all_test_request_body = """
            <apex:runTests>
                <apex:RunTestsRequest>
                    <apex:allTests>true</apex:allTests>
                </apex:RunTestsRequest>
            </apex:runTests>
        """

        return self.create_apex_envelope(run_all_test_request_body)

    ##############################################
    # Partner API Request
    ##############################################
    def create_partner_envelope(self, body):
        apex_request_envelope = """<soapenv:Envelope 
            xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
            xmlns:urn="urn:partner.soap.sforce.com">
            <soapenv:Header>
                <urn:SessionHeader>
                    <urn:sessionId>{session_id}</urn:sessionId>
                </urn:SessionHeader>
            </soapenv:Header>
            <soapenv:Body>
                {body}
            </soapenv:Body>
        </soapenv:Envelope>
        """.format(session_id=self.get_session_id(), body=body)

        return self.format_request_envelope(apex_request_envelope)

    def create_describe_layout_request(self, options):
        describe_layout_request_body = """
            <urn:describeLayout>
                <urn:sObjectType>{sobject}</urn:sObjectType>
                <urn:recordTypeIds>{recordtype_id}</urn:recordTypeIds>
            </urn:describeLayout>
        """.format(**options)

        return self.create_partner_envelope(describe_layout_request_body)