# Body for creating job and closing job
create_job = """<?xml version="1.0" encoding="UTF-8"?>
                <jobInfo xmlns="http://www.force.com/2009/06/asyncapi/dataload">
                    <operation>{operation}</operation>
                    <object>{sobject}</object>
                    <concurrencyMode>Parallel</concurrencyMode>
                    <contentType>CSV</contentType>
                </jobInfo>"""

close_job = """<?xml version="1.0" encoding="UTF-8"?>
                <jobInfo xmlns="http://www.force.com/2009/06/asyncapi/dataload">
                    <state>Closed</state>
                </jobInfo>"""

# Body for login
login_body = """<?xml version="1.0" encoding="utf-8" ?>
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
    </env:Envelope>"""

# Body for executing anonymous apex
execute_anonymous_body = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:apex="http://soap.sforce.com/2006/08/apex">
       <soapenv:Header>
          <apex:DebuggingHeader>
            {log_levels}
          </apex:DebuggingHeader>
          <apex:SessionHeader>
            <sessionId>{session_id}</sessionId>
          </apex:SessionHeader>
       </soapenv:Header>
       <soapenv:Body>
          <apex:executeAnonymous>
             <apex:String>{apex_string}</apex:String>
          </apex:executeAnonymous>
       </soapenv:Body>
    </soapenv:Envelope>"""

# Body for describing layout
describe_layout_body = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
        xmlns:urn="urn:partner.soap.sforce.com">
        <soapenv:Header>
            <urn:SessionHeader>
                <urn:sessionId>{session_id}</urn:sessionId>
            </urn:SessionHeader>
        </soapenv:Header>
        <soapenv:Body>
            <urn:describeLayout>
                <urn:sObjectType>{sobject}</urn:sObjectType>
                <urn:recordTypeIds>{recordtype_id}</urn:recordTypeIds>
            </urn:describeLayout>
        </soapenv:Body>
    </soapenv:Envelope>"""

# Body for checking status of retrieve or deploy
check_status_body = """
  <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
  xmlns:met="http://soap.sforce.com/2006/04/metadata">
     <soapenv:Header>
        <met:SessionHeader>
           <met:sessionId>{session_id}</met:sessionId>
        </met:SessionHeader>
     </soapenv:Header>
     <soapenv:Body>
        <met:checkStatus>
           <met:asyncProcessId>{async_process_id}</met:asyncProcessId>
        </met:checkStatus>
     </soapenv:Body>
  </soapenv:Envelope>
  """

# Body for retrieving status
check_retrieve_status_body = """
  <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
  xmlns:met="http://soap.sforce.com/2006/04/metadata">
     <soapenv:Header>
        <met:SessionHeader>
           <met:sessionId>{session_id}</met:sessionId>
        </met:SessionHeader>
     </soapenv:Header>
     <soapenv:Body>
        <met:checkRetrieveStatus>
           <met:asyncProcessId>{async_process_id}</met:asyncProcessId>
        </met:checkRetrieveStatus>
     </soapenv:Body>
  </soapenv:Envelope>
  """

# Body for retrieve metadata by specified package.xml
retrieve_body = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
        xmlns:met="http://soap.sforce.com/2006/04/metadata">
        <soapenv:Header>
            <met:SessionHeader>
                <met:sessionId>{0}</met:sessionId>
            </met:SessionHeader>
        </soapenv:Header>
        <soapenv:Body>
            <met:retrieve>
                <met:retrieveRequest>
                    <met:apiVersion>{1}.0</met:apiVersion>
                    <met:unpackaged>
                        {2}
                    </met:unpackaged>
                </met:retrieveRequest>
            </met:retrieve>
        </soapenv:Body>
    </soapenv:Envelope>
"""

# Body for checking deploy status
check_deploy_status = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:met="http://soap.sforce.com/2006/04/metadata">
       <soapenv:Header>
          <met:SessionHeader>
             <met:sessionId>{0}</met:sessionId>
          </met:SessionHeader>
       </soapenv:Header>
       <soapenv:Body>
          <met:checkDeployStatus>
             <met:asyncProcessId>{1}</met:asyncProcessId>
             <met:includeDetails>true</met:includeDetails>
          </met:checkDeployStatus>
       </soapenv:Body>
    </soapenv:Envelope>"""

# Body for deploying base64 zipfile
deploy_package = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:met="http://soap.sforce.com/2006/04/metadata">
        <soapenv:Header>
            <met:SessionHeader>
               <met:sessionId>{0}</met:sessionId>
            </met:SessionHeader>
        </soapenv:Header>
       <soapenv:Body>
          <met:deploy>
             <met:ZipFile>{1}</met:ZipFile>
             <met:DeployOptions>
                <met:allowMissingFiles>{2}</met:allowMissingFiles>
                <met:autoUpdatePackage>{3}</met:autoUpdatePackage>
                <met:checkOnly>{4}</met:checkOnly>
                <met:ignoreWarnings>{5}</met:ignoreWarnings>
                <met:performRetrieve>{6}</met:performRetrieve>
                <met:purgeOnDelete>{7}</met:purgeOnDelete>
                <met:rollbackOnError>{8}</met:rollbackOnError>
                <met:runAllTests>{9}</met:runAllTests>
                <met:singlePackage>{10}</met:singlePackage>
             </met:DeployOptions>
          </met:deploy>
       </soapenv:Body>
    </soapenv:Envelope>"""

# Body for retrieving Metadata of sObjects and Workflow
retrieve_sobjects_workflow_task_body = """
  <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
  xmlns:met="http://soap.sforce.com/2006/04/metadata">
     <soapenv:Header>
        <met:SessionHeader>
           <met:sessionId>{0}</met:sessionId>
        </met:SessionHeader>
     </soapenv:Header>
     <soapenv:Body>
        <met:retrieve>
           <met:retrieveRequest>
              <met:apiVersion>{1}.0</met:apiVersion>
              <met:unpackaged>
                  <met:types>
                      <met:members>*</met:members>
                      <met:members>Account</met:members>
                      <met:members>AccountContactRole</met:members>
                      <met:members>Activity</met:members>
                      <met:members>Asset</met:members>
                      <met:members>Campaign</met:members>
                      <met:members>CampaignMember</met:members>
                      <met:members>Case</met:members>
                      <met:members>CaseContactRole</met:members>
                      <met:members>Contact</met:members>
                      <met:members>ContentVersion</met:members>
                      <met:members>Contract</met:members>
                      <met:members>ContractContactRole</met:members>
                      <met:members>Event</met:members>
                      <met:members>Idea</met:members>
                      <met:members>Lead</met:members>
                      <met:members>Opportunity</met:members>
                      <met:members>OpportunityContactRole</met:members>
                      <met:members>OpportunityLineItem</met:members>
                      <met:members>PartnerRole</met:members>
                      <met:members>Product2</met:members>
                      <met:members>Site</met:members>
                      <met:members>Solution</met:members>
                      <met:members>Task</met:members>
                      <met:members>User</met:members>
                      <name>CustomObject</name>
                  </met:types>
                  <met:types>
                      <met:members>*</met:members>
                      <name>Workflow</name>
                  </met:types>
                  <met:version>{1}.0</met:version>
              </met:unpackaged>
           </met:retrieveRequest>
        </met:retrieve>
     </soapenv:Body>
  </soapenv:Envelope>"""

# Body for retrieving static resource
retrieve_static_resource_body = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:met="http://soap.sforce.com/2006/04/metadata">
        <soapenv:Header>
            <met:SessionHeader>
               <met:sessionId>{0}</met:sessionId>
            </met:SessionHeader>
        </soapenv:Header>
        <soapenv:Body>
            <met:retrieve>
                <met:retrieveRequest>
                    <met:apiVersion>{1}.0</met:apiVersion>
                    <met:unpackaged>
                        <met:types>
                            <met:members>*</met:members>
                            <name>StaticResource</name>
                        </met:types>
                        <met:version>{1}.0</met:version>
                    </met:unpackaged>
                </met:retrieveRequest>
            </met:retrieve>
        </soapenv:Body>
    </soapenv:Envelope>"""

# Body for retrieving static resource
retrieve_apex_code_body = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:met="http://soap.sforce.com/2006/04/metadata">
        <soapenv:Header>
            <met:SessionHeader>
               <met:sessionId>{0}</met:sessionId>
            </met:SessionHeader>
        </soapenv:Header>
        <soapenv:Body>
            <met:retrieve>
                <met:retrieveRequest>
                    <met:apiVersion>{1}.0</met:apiVersion>
                    <met:unpackaged>
                        <met:types>
                            <met:members>*</met:members>
                            <name>StaticResource</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>ApexClass</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>ApexPage</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>ApexTrigger</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>ApexComponent</name>
                        </met:types>
                        <met:version>{1}.0</met:version>
                    </met:unpackaged>
                </met:retrieveRequest>
            </met:retrieve>
        </soapenv:Body>
    </soapenv:Envelope>"""

# Body for retrieving all metadata
retrieve_all_task_body = """
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
    xmlns:met="http://soap.sforce.com/2006/04/metadata">
        <soapenv:Header>
            <met:SessionHeader>
               <met:sessionId>{0}</met:sessionId>
            </met:SessionHeader>
        </soapenv:Header>
        <soapenv:Body>
            <met:retrieve>
                <met:retrieveRequest>
                    <met:apiVersion>{1}.0</met:apiVersion>
                    <met:unpackaged>
                        <met:types>
                            <met:members>*</met:members>
                            <name>AccountCriteriaBasedSharingRule</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>AccountOwnerSharingRule</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>AnalyticSnapshot</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>ApexClass</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>ApexComponent</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>ApexPage</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>ApexTrigger</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>ApprovalProcess</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>AuthProvider</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>CallCenter</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>CampaignCriteriaBasedSharingRule</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>CampaignOwnerSharingRule</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>CaseCriteriaBasedSharingRule</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>CaseOwnerSharingRule</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>Community</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>ContactCriteriaBasedSharingRule</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>ContactOwnerSharingRule</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>CustomApplication</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>CustomApplicationComponent</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>CustomLabels</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <met:members>Account</met:members>
                            <met:members>AccountContactRole</met:members>
                            <met:members>Activity</met:members>
                            <met:members>Asset</met:members>
                            <met:members>Campaign</met:members>
                            <met:members>CampaignMember</met:members>
                            <met:members>Case</met:members>
                            <met:members>CaseContactRole</met:members>
                            <met:members>Contact</met:members>
                            <met:members>ContentVersion</met:members>
                            <met:members>Contract</met:members>
                            <met:members>ContractContactRole</met:members>
                            <met:members>Event</met:members>
                            <met:members>Idea</met:members>
                            <met:members>Lead</met:members>
                            <met:members>Opportunity</met:members>
                            <met:members>OpportunityCompetitor</met:members>
                            <met:members>OpportunityContactRole</met:members>
                            <met:members>OpportunityLineItem</met:members>
                            <met:members>PartnerRole</met:members>
                            <met:members>Pricebook2</met:members>
                            <met:members>Product2</met:members>
                            <met:members>Site</met:members>
                            <met:members>Solution</met:members>
                            <met:members>Task</met:members>
                            <met:members>User</met:members>
                            <name>CustomObject</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>CustomObjectTranslation</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>criteriaBasedRules</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>ownerRules</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>CustomPageWebLink</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>CustomSite</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>CustomTab</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>Dashboard</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>DataCategoryGroup</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <met:members>SharedDocuments</met:members>
                            <name>Document</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>EmailTemplate</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>Flow</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>Group</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>HomePageComponent</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>HomePageLayout</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>InstalledPackage</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>Layout</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>LeadCriteriaBasedSharingRule</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>LeadOwnerSharingRule</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>Letterhead</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>OpportunityCriteriaBasedSharingRule</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>OpportunityOwnerSharingRule</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>PermissionSet</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>Profile</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>Queue</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>QuickAction</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>Report</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>ReportType</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>Role</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>Scontrol</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>StaticResource</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>Workflow</name>
                        </met:types>
                        <met:types>
                            <met:members>*</met:members>
                            <name>Settings</name>
                        </met:types>
                      <met:version>{1}.0</met:version>
                    </met:unpackaged>
                </met:retrieveRequest>
            </met:retrieve>
        </soapenv:Body>
    </soapenv:Envelope>"""