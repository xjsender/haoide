import sublime
import sublime_plugin
import os
import urllib
import json
import threading
import time
import pprint
import urllib.parse
import shutil

from xml.sax.saxutils import unescape
from . import requests, context, util
from .context import COMPONENT_METADATA_SETTINGS
from .util import getUniqueElementValueFromXmlString
from .salesforce import bulkapi, soap_bodies, message
from .salesforce.bulkapi import BulkApi
from .salesforce.api import SalesforceApi
from .progress import ThreadProgress, ThreadsProgress


def populate_users():
    """
    Get dict (LastName + FirstName => UserId) in whole org

    @return: {
        username + users: {
            LastName + FirstName => UserId
        }
        ...
    }
    """

    # Get username
    toolingapi_settings = context.get_toolingapi_settings()
    username = toolingapi_settings["username"]

    # If sobjects is exist in globals()[], just return it
    if (username + "users") in globals(): 
        return globals()[username + "users"]

    # If sobjects is not exist in globals(), post request to pouplate it
    api = SalesforceApi(toolingapi_settings)
    query = """SELECT Id, FirstName, LastName 
               FROM User WHERE LastName != null 
               AND FirstName != null
               AND IsActive = true"""
    thread = threading.Thread(target=api.query_all, args=(query, ))
    thread.start()

    while thread.is_alive() or api.result == None:
        time.sleep(1)

    records = api.result["records"]
    users = {}
    for user in records:
        user_first_name = user["FirstName"]
        user_last_name = user["LastName"]
        user_id = user["Id"]
        users[user_last_name + " " + user_first_name] = user_id

    globals()[username + "users"] = users
    return users  

def populate_components():
    """
    Get all components which NamespacePrefix is null in whole org
    """

    # Get username
    toolingapi_settings = context.get_toolingapi_settings()
    username = toolingapi_settings["username"]

    # If sobjects is exist in globals()[], just return it
    component_metadata = sublime.load_settings("component_metadata.sublime-settings")
    if not component_metadata.has(username):
        return []

    return_component_attributes = {}
    for component_type in component_metadata.get(username).keys():
        component_attributes = component_metadata.get(username)[component_type]
        for component_name in component_attributes.keys():
            component_id = component_attributes[component_name]["id"]
            component_type = component_attributes[component_name]["type"]
            return_component_attributes[component_type + "-->" + component_name] = component_id

    return return_component_attributes

def populate_classes():
    """
    Get dict (Class Name => Class Id) which NamespacePrefix is null in whole org

    @return: {
        classname: classid
        ...
    }
    """
    # Get username
    toolingapi_settings = context.get_toolingapi_settings()
    username = toolingapi_settings["username"]

    # If sobjects is exist in globals()[], just return it
    component_metadata = sublime.load_settings("component_metadata.sublime-settings")
    if component_metadata.has(username):
        return component_metadata.get(username).get("ApexClass")

    if username + "classes" in globals():
        return globals()[username + "classes"]

    # If sobjects is not exist in globals(), post request to pouplate it
    api = SalesforceApi(toolingapi_settings)
    query = "SELECT Id, Name, Body FROM ApexClass WHERE NamespacePrefix = null"
    thread = threading.Thread(target=api.query_all, args=(query, ))
    thread.start()

    while thread.is_alive() or api.result == None:
        time.sleep(1)

    classes = {}
    for record in api.result["records"]:
        name = record["Name"]
        body = record["Body"]
        component_attr = {"id": record["Id"]}
        if "@isTest" in body or "testMethod" in body or "testmethod" in body:
            component_attr["is_test"] = True
        else:
            component_attr["is_test"] = False

        classes[name] = component_attr

    globals()[username + "classes"] = classes
    return classes

def populate_sobject_recordtypes():
    """
    Get dict ([sobject, recordtype name] => recordtype id) in whole org

    @return: {
        username + "sobject_recordtypes": {
            sobject + rtname: rtid
        }
        ...
    }
    """

    # Get username
    toolingapi_settings = context.get_toolingapi_settings()
    username = toolingapi_settings["username"]

    # If sobjects is exist in globals()[], just return it
    if (username + "sobject_recordtypes") in globals(): 
        return globals()[username + "sobject_recordtypes"]

    # If sobjects is not exist in globals(), post request to pouplate it
    api = SalesforceApi(toolingapi_settings)
    query = "SELECT Id, Name, SobjectType FROM RecordType"
    thread = threading.Thread(target=api.query_all, args=(query, ))
    thread.start()

    while thread.is_alive() or api.result == None:
        time.sleep(1)

    records = api.result["records"]
    sobject_recordtypes = {}
    for recordtype in records:
        sobjectype = recordtype["SobjectType"]
        rtname = recordtype["Name"]
        rtid = recordtype["Id"]
        sobject_recordtypes[sobjectype + ", " + rtname] = rtid

    globals()[username + "sobject_recordtypes"] = sobject_recordtypes
    return sobject_recordtypes  

def populate_sobjects_describe():
    """
    Get the sobjects list in org.
    """

    # Get username
    toolingapi_settings = context.get_toolingapi_settings()
    username = toolingapi_settings["username"]

    # If sobjects is exist in sobjects_completion.sublime-settings, just return it
    sobjects_completions = sublime.load_settings("sobjects_completion.sublime-settings")
    if sobjects_completions.has(username):
        return sobjects_completions.get(username)

    if (username + "sobjects") in globals():
        return globals()[username + "sobjects"]

    # If sobjects is not exist in globals(), post request to pouplate it
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.describe_global, args=())
    thread.start()

    while thread.is_alive() or api.result == None:
        time.sleep(1)

    sobjects_describe = {}
    for sd in api.result["sobjects"]:
        sobjects_describe[sd["name"]] = {
            "keyPrefix": sd["keyPrefix"]
        }

    globals()[username + "sobjects"] = sobjects_describe
    return sobjects_describe

def handle_login_thread(default_project, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return

        result = api.result
        if result["status_code"] > 399: return
        if toolingapi_settings["output_session_info"]:
            pprint.pprint(result)

        print (message.SEPRATE.format("Login Succeed"))

    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.login, args=(False, ))
    thread.start()
    handle_thread(thread, timeout)
    ThreadProgress(api, thread, "Login to switched project", default_project + " Login Succeed")

def handle_retrieve_static_resource_body(file, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return

        result = api.result
        body = result["body"]
        workspace = toolingapi_settings["workspace"]
        if component_attribute["ContentType"] == "application/zip":
            outputdir = workspace + "/StaticResource/" + component_name
            util.extract_zip(result, outputdir)
        else:
            fp = open(file, "wb")
            try:
                body = bytes(body, "UTF-8")
            except:
                body = body.encode("UTF-8")

            fp.write(body)

    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    component_attribute, component_name = util.get_component_attribute(file)
    url = "/services/data/v{0}.0/sobjects/StaticResource/" + component_attribute["id"] + "/Body"
    thread = threading.Thread(target=api.retrieve_body, args=(url, True, ))
    thread.start()
    handle_thread(thread, timeout)
    ThreadProgress(api, thread, "Retrieve StaticResource Body", 
        "Retrieve StaticResource Body Succeed")

def handle_view_code_coverage(component_name, component_attribute, body, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return

        result = api.result
        if result["status_code"] > 399:
            error_message = "% 20s\t" % "Component Name: "
            error_message += "%-30s\t" % component_name + "\n"
            error_message += util.format_error_message(result)
            print (message.SEPRATE.format(error_message))
            return

        sublime.active_window().run_command("show_panel", 
            {"panel": "console", "toggle": False})
        if result["totalSize"] == 0:
            print (message.SEPRATE.format("You should run test class firstly."))
            return

        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": component_name + " Code Coverage",
            "input": body
        })

        uncovered_lines = result["records"][0]["Coverage"]["uncoveredLines"]
        covered_lines = result["records"][0]["Coverage"]["coveredLines"]
        all_region_by_line = view.lines(sublime.Region(0, view.size()))
        uncovered_region = []
        for region in all_region_by_line:
            line = view.rowcol(region.begin() + 1)[0] + 1
            if line in uncovered_lines:
                uncovered_region.append(region)

        view.add_regions("mark", uncovered_region, "bookmark", 'cross',
            sublime.DRAW_NO_FILL | sublime.DRAW_NO_OUTLINE | sublime.DRAW_STIPPLED_UNDERLINE)

        covered_count = len(covered_lines)
        total_count = len(covered_lines) + len(uncovered_lines)
        coverage = covered_count / total_count * 100
        print (message.SEPRATE.format("The coverage is %.2f%%(%s/%s)" % (coverage, covered_count, total_count)))

    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    query = "SELECT Coverage FROM ApexCodeCoverageAggregate " +\
        "WHERE ApexClassOrTriggerId = '{0}'".format(component_attribute["id"])
    thread = threading.Thread(target=api.query, args=(query, True, ))
    thread.start()
    ThreadProgress(api, thread, "View Code Coverage of " + component_name,
        "View Code Coverage of " + component_name + " Succeed")
    handle_thread(thread, timeout)

def handle_refresh_folder(folder, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return

        result = api.result

        # Output component size
        size = len(result["records"])
        print (message.SEPRATE.format(str(component_type) + " Size: " + str(size)))

        # Write Components to local
        components = {}
        for record in result["records"]:
            # Get Component Name of this record
            component_name = record['Name']
            component_url = record['attributes']['url']
            component_id = record["Id"]
            print (str(component_type) + " ==> " + str(record['Name']))

            # Write mapping of component_name with component_url
            # into component_metadata.sublime-settings
            components[component_name] = {
                "url": component_url,
                "id": component_id,
                "type": component_type,
                "body": component_body,
                "extension": component_extension
            }
            
            # Judge Component is Test Class or not
            body = record[component_body]
            if component_type == "ApexClass":
                if "@isTest" in body or "testMethod" in body or "testmethod" in body:
                    components[component_name]["is_test"] = True
                else:
                    components[component_name]["is_test"] = False

            # Write body to local file
            fp = open(component_outputdir + "/" + component_name +\
                component_extension, "wb")
            try:
                body = bytes(body, "UTF-8")
            except:
                body = body.encode("UTF-8")
            fp.write(body)

            # Set status_message
            sublime.status_message(component_name + " ["  + component_type + "] Downloaded")

        # Save Refreshed Component Attributes to component_metadata.sublime-settings
        s = sublime.load_settings(COMPONENT_METADATA_SETTINGS)
        username = toolingapi_settings["username"]
        components_dict = s.get(username)
        components_dict[component_type] = components
        s.set(username, components_dict)

        sublime.save_settings(context.COMPONENT_METADATA_SETTINGS)

    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)

    # Get component attributes by component_type
    component_type = toolingapi_settings[folder]
    component_attribute = toolingapi_settings[component_type]
    component_outputdir = component_attribute["outputdir"]
    component_body = component_attribute["body"]
    component_extension = component_attribute["extension"]
    component_soql = component_attribute["soql"]
    thread = threading.Thread(target=api.query_all, args=(component_soql, ))
    thread.start()
    ThreadProgress(api, thread, "Refreshing " + component_type, 
        "Refreshing " + component_type + " Succeed")
    handle_thread(thread, timeout)

def handle_initiate_sobjects_completions(timeout=120):
    """
    Save sobject describe to local which is used in completions

    """

    def handle_threads(apis, threads, timeout):
        for thread in threads:
            if thread.is_alive():
                sublime.set_timeout(lambda: handle_threads(apis, threads, timeout), timeout)
                return
        
        # If succeed, get the all sobject describe result
        results = []
        for api in apis:
            results.append(api.result)

        # Save all sobject describe result to sublime settings
        s = sublime.load_settings("sobjects_completion.sublime-settings")
        sobjects_completion = {}
        for sobject_describe in results:
            # Initiate Sobject completions
            sobject_name = sobject_describe["name"]
            sobjects_completion[sobject_name] = {
                "keyPrefix": sobject_describe["keyPrefix"]
            }

            # Combine fields dict
            fields_dict = {}
            parent_relationship_dict = {}
            for f in sobject_describe["fields"]:
                fields_dict[f["name"] + "\t" + f["type"] + "(" + format(f["length"]) + ")"] = f["name"]

                # List all Reference Field Relationship Name as fields
                # Some fields has two more references, we can't list the fields of it
                if not len(f["referenceTo"]) == 1: continue
                if not f["relationshipName"]: continue
                parent_relationship_dict[f["relationshipName"]] = {
                    "parentSobject": f["referenceTo"][0],
                    "relationshipName": f["relationshipName"],
                    "field": f["name"]
                }
            
            # Child Relationship dict
            child_relationship_dict = {}
            for f in sobject_describe["childRelationships"]:
                if not f["relationshipName"]: continue

                child_relationship_dict[f["relationshipName"]] = {
                    "childSobject": f["childSObject"],
                    "field": f["field"],
                    "relationshipName": f["relationshipName"]
                }

            # Combine sobject fields dict and sobject child relationship dict
            sobjects_completion[sobject_name]["fields"] = fields_dict
            sobjects_completion[sobject_name]["parentRelationships"] = parent_relationship_dict
            sobjects_completion[sobject_name]["childRelationships"] = child_relationship_dict

        # Every project has unique username
        username = toolingapi_settings["username"]
        s.set(username, sobjects_completion)

        # Save settings
        sublime.save_settings("sobjects_completion.sublime-settings")

        # Output message
        print (message.SEPRATE.format('Sobjects completions local history are initiated.'))

    def handle_thread(api, thread, timeout=120):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(api, thread, timeout), timeout)
            return

        sobjects = api.result
        threads = []
        apis = []
        for sobject in sobjects:
            api = SalesforceApi(toolingapi_settings)
            thread = threading.Thread(target=api.describe_sobject, args=(sobject, ))
            thread.start()
            threads.append(thread)
            apis.append(api)

        ThreadsProgress(threads, "Describe All Sobjects", "Describe All Sobjects Succeed")
        handle_threads(apis, threads, 10)

    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.describe_global_common, args=())
    thread.start()
    ThreadProgress(api, thread, "Global Describe", "Global Describe Succeed")
    handle_thread(api, thread, timeout)

def handle_deploy_metadata_thread(zipfile, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        
        result = api.result
        status_code = result["status_code"]
        if status_code > 399: return
        print (message.SEPRATE.format("Deploy Metadata Succeed"))

    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.deploy_metadata, args=(zipfile, ))
    thread.start()
    ThreadProgress(api, thread, "Deploy Metadata", "Deploy Metadata Succeed")
    handle_thread(thread, timeout)

def handle_bulk_operation_thread(sobject, operation, timeout=120):
    settings = context.get_toolingapi_settings()
    csv_file = settings["workspace"] + "/bulkin/%s.csv" % sobject
    if not os.path.exists(csv_file):
        sublime.error_message(csv_file + " is not exist")
        return

    records = open(csv_file, "rb").read()
    bulkapi = BulkApi(settings, sobject, records)
    if operation == "insert":
        target = bulkapi.insert
    elif operation == "update":
        target = bulkapi.update
    elif operation == "upsert":
        target = bulkapi.upsert
    elif operation == "delete":
        target = bulkapi.delete
    thread = threading.Thread(target=target, args=())
    thread.start()
    progress_message = operation + " " + sobject
    ThreadProgress(bulkapi, thread, progress_message, progress_message + " Succeed")

def handle_backup_sobject_thread(sobject, timeout=120):
    settings = context.get_toolingapi_settings()
    bulkapi = BulkApi(settings, sobject)
    thread = threading.Thread(target=bulkapi.query, args=())
    thread.start()
    ThreadProgress(bulkapi, thread, "Export Records of " + sobject, 
        "Export Records of " + sobject + " Succeed")

def handle_backup_all_sobjects_thread(timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return

        sobjects = api.result
        threads = []
        for sobject in sobjects:
            bulkapi = BulkApi(settings, sobject)
            thread = threading.Thread(target=bulkapi.query, args=())
            thread.start()
            threads.append(thread)

        ThreadsProgress(threads, "Export All Sobjects Records", 
            "Export All Sobjects Records Succeed")

    settings = context.get_toolingapi_settings()
    api = SalesforceApi(settings)
    thread = threading.Thread(target=api.describe_global_common, args=())
    thread.start()
    ThreadProgress(api, thread, "Describe Global", "Describe Global Succeed")
    handle_thread(thread, timeout)

def handle_retrieve_all_thread(timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        
        if api.result == None: return
        if api.result["status_code"] > 399: return

        # Mkdir for output dir of zip file
        result = api.result
        outputdir = toolingapi_settings["workspace"] + "/metadata"
        if not os.path.exists(outputdir):
            os.makedirs(outputdir)

        # Define zip file path and extracted zip file path
        outputdir = toolingapi_settings["workspace"] + "/metadata"

        # Extract zip
        util.extract_zip(result["zipFile"], outputdir)

        # Remove this zip file
        # os.remove(zipdir)

        # Output package path
        sublime.status_message("Your objects and workflows are exported to: " + outputdir)

    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.retrieve, args=(soap_bodies.retrieve_all_task_body, ))
    thread.start()
    ThreadProgress(api, thread, "Retrieve Metadata", "Retrieve Metadata Succeed")
    handle_thread(thread, timeout)

def handle_export_workflows(timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        
        # If succeed
        sobjects = api.result
        for sobject in sobjects:
            util.parse_workflow_metadata(toolingapi_settings, sobject)

        print (message.SEPRATE.format("Outputdir: " + outputdir))

    toolingapi_settings = context.get_toolingapi_settings()
    outputdir = toolingapi_settings["workspace"] + "/describe/workflows/"
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.describe_global_common, args=())
    thread.start()
    ThreadProgress(api, thread, "Export All Workflows", "Outputdir: " + outputdir)
    handle_thread(thread, 10)

def handle_export_validation_rules(timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return

        # If succeed
        sobjects = api.result
        util.parse_validation_rule(toolingapi_settings, sobjects)

        print (message.SEPRATE.format("Outputdir: " + outputdir))

    toolingapi_settings = context.get_toolingapi_settings()
    outputdir = toolingapi_settings["workspace"] + "/describe/validation rules/validation rules.csv"
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.describe_global_common, args=())
    thread.start()
    ThreadProgress(api, thread, "Export All Validation Rules", "Outputdir: " + outputdir)
    handle_thread(thread, 10)

def handle_describe_customfield(timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        
        # If succeed
        result = api.result
        if result["status_code"] > 399 : return

        if not os.path.exists(outputdir): os.makedirs(outputdir)
        output_file_dir = outputdir + "/customfield.csv"
        if util.is_python3x():
            fp = open(output_file_dir, "w", newline='')
        else:
            fp = open(output_file_dir, "wb")

        # Write list to csv
        records = sorted(result["records"], key=lambda k : k['TableEnumOrId'])
        util.list2csv(fp, records)

        # Release fp
        fp.close()

        # Output log
        print (message.SEPRATE.format(output_file_dir))

    toolingapi_settings = context.get_toolingapi_settings()
    workspace = context.get_toolingapi_settings().get("workspace")
    outputdir = workspace + "/describe/customfield"
    api = SalesforceApi(toolingapi_settings)
    query = "SELECT Id,TableEnumOrId,DeveloperName,NamespacePrefix,FullName FROM CustomField"
    thread = threading.Thread(target=api.query_all, args=(query, True,))
    thread.start()
    ThreadProgress(api, thread, 'Describe CustomField', 
        'Outputdir: ' + outputdir + "/customfield.csv")
    handle_thread(thread, 10)

def handle_describe_global(timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return

        result = api.result

        # Error Message are prcoessed in ThreadProgress
        if result["status_code"] > 399 :return

        if not os.path.exists(outputdir):
            os.makedirs(outputdir)

        # Open output csv
        output_file_dir = outputdir + "/sobjects.csv"
        if util.is_python3x():
            fp = open(output_file_dir, "w", newline='')
        else:
            fp = open(output_file_dir, "wb")

        # Write list to csv
        util.list2csv(fp, result["sobjects"])

        # Console Log
        print ("Output Directory: " + outputdir + "sobjects.csv")

    toolingapi_settings = context.get_toolingapi_settings()
    workspace = context.get_toolingapi_settings().get("workspace")
    outputdir = workspace + "/describe/global"
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.describe_global, args=())
    thread.start()
    ThreadProgress(api, thread, 'Describe Global...', "Output Directory: " + outputdir + "sobjects.csv")
    handle_thread(thread, timeout)

def handle_describe_layout(sobject, recordtype_name, recordtype_id, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        
        # If succeed
        result = api.result
        if result["status_code"] > 399 : return

        # If totalSize is 0
        if "totalSize" in result and result["totalSize"] == 0 :
            util.sublime_error_message(result)
            return

        # If outputdir is not exist, just make it
        if not os.path.exists(outputdir):
            os.makedirs(outputdir)

        if util.is_python3x():
            fp = open(output_file_dir, "w", newline='')
        else:
            fp = open(output_file_dir, "wb")
        util.parse_describe_layout_result(fp, result)
        
        print (message.SEPRATE.format("Layout describe outputdir: " + output_file_dir))

    toolingapi_settings = context.get_toolingapi_settings()
    outputdir = toolingapi_settings["workspace"] + "/describe/layout"
    output_file_dir = outputdir + "/" + sobject + "-" + recordtype_name + ".csv"
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.describe_layout, args=(sobject, recordtype_id, ))
    thread.start()
    ThreadProgress(api, thread, "Desicrbing Layout of " + sobject, 
        "Outputdir: " + output_file_dir)
    handle_thread(thread, 120)

def handle_execute_query(soql, timeout=120):
    def handle_new_view_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_new_view_thread(thread, timeout), timeout)
            return
        
        # If succeed
        result = api.result
        pprint.pprint(result)
        if result["status_code"] > 399: return

        # No error, just display log in a new view
        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": "Execute Query Result",
            "input": pprint.pformat(result)
        })

    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.query, args=(soql, ))
    thread.start()
    ThreadProgress(api, thread, "Execute Query", "Execute Query Succeed")
    handle_new_view_thread(thread, timeout)

def handle_execute_anonymous(apex_string, timeout=120):
    def handle_new_view_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_new_view_thread(thread, timeout), timeout)
            return
        
        # If succeed
        result = api.result
        if result["status_code"] > 399: return

        # No error, just display log in a new view
        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": "Execute Anonymous Result",
            "input": util.parse_execute_anonymous_xml(result)
        })

    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.execute_anonymous, args=(apex_string, ))
    thread.start()
    ThreadProgress(api, thread, "Execute Anonymous", "Execute Anonymous Succeed")
    handle_new_view_thread(thread, timeout)

def handle_list_debug_logs(user_full_name, user_id, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return

        result = api.result
        records = result["records"]
        debug_logs_table = util.format_debug_logs(toolingapi_settings, records)
        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": "Debug Logs",
            "input": debug_logs_table
        })

    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    query = "SELECT Id,LogUserId,LogLength,Request,Operation,Application," +\
            "Status,DurationMilliseconds,StartTime,Location FROM ApexLog " +\
            "WHERE LogUserId='{0}'".format(user_id)
    thread = threading.Thread(target=api.query_all, args=(query, ))
    thread.start()
    ThreadProgress(api, thread, "List Debug Logs for " + user_full_name, 
        "List Debug Logs for " + user_full_name + " Succeed")
    handle_thread(thread, timeout)    

def handle_create_debug_log(user_name, user_id, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return

        result = api.result
        if result["status_code"] > 399: return
        print (message.SEPRATE.format("Create Debug Log for '{0}' Succeed.".format(user_name)))

    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.create_trace_flag, args=(user_id, ))
    thread.start()
    ThreadProgress(api, thread, "Create Debug Log for " + user_name, 
        "Create Debug Log for " + user_name + " Succeed")
    handle_thread(thread, timeout)

def handle_view_debug_log_detail(log_id, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        
        if api.result["status_code"] > 399: return
        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": "Debug Log Detail",
            "input": api.result["body"]
        })

    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    url = "/services/data/v{0}.0/sobjects/ApexLog/" + log_id + "/Body"
    thread = threading.Thread(target=api.retrieve_body, args=(url, ))
    thread.start()
    ThreadProgress(api, thread, "Get Log Detail of " + log_id, 
        "Get Log Detail of " + log_id + " Succeed")
    handle_thread(thread, timeout)

def handle_run_test(class_name, class_id, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return

        # If succeed
        result = api.result
        # If error
        if "status_code" in result and result["status_code"] > 399: return

        # No error, just display log in a new view
        test_result = util.parse_test_result(result)
        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": "Test Result",
            "input": test_result
        })

    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.run_test, args=(class_id, ))
    thread.start()
    ThreadProgress(api, thread, "Run Test Class " + class_name, "Run Test for " + class_name + " Succeed")
    handle_thread(thread, timeout)

def handle_describe_sobject(sobject, timeout=120):
    def handle_new_view_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_new_view_thread(thread, timeout), timeout)
            return

        # If succeed
        result = api.result
        
        # Error Message are prcoessed in ThreadProgress
        if result["status_code"] > 399: return

        # No error, just display log in a new view
        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": sobject + " Describe Result",
            "input": util.parse_sobject_field_result(result)
        })

    toolingapi_settings = context.get_toolingapi_settings()
    api_version = toolingapi_settings["api_version"]
    api = SalesforceApi(toolingapi_settings)
    sobject_url = "/services/data/v{0}.0/sobjects/".format(api_version) + sobject + "/describe"
    thread = threading.Thread(target=api.get, args=(sobject_url, ))
    thread.start()
    ThreadProgress(api, thread, 'Describe ' + sobject, 'Describe ' + sobject + ' Succeed')
    handle_new_view_thread(thread, timeout)

def handle_generate_specified_workbooks(sobjects, timeout=120):
    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    threads = []
    for sobject in sobjects:
        thread = threading.Thread(target=api.generate_workbook, args=(sobject, ))
        threads.append(thread)
        thread.start()

    ThreadsProgress(threads, "Generating Sobjects Workbook", 
        "Sobjects Workbook are Generated")

def handle_generate_all_workbooks(timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        
        # If succeed
        result = api.result
        for sobject in result:
            thread = threading.Thread(target=api.generate_workbook, args=(sobject, ))
            thread.start()

    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.describe_global_common, args=())
    thread.start()
    ThreadProgress(api, thread, "Global Describe Common", "Global Describe Common Succeed")
    handle_thread(thread, timeout)

def handle_new_project(toolingapi_settings, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        
        # If succeed, something may happen,
        # for example, user password is expired
        result = api.result
        if result == None: return
        if "status_code" in result and result["status_code"] > 399: return

        # Load COMPONENT_METADATA_SETTINGS Settings and put all result into it
        # Every org has one local repository
        component_metadata = result
        component_settings = sublime.load_settings(COMPONENT_METADATA_SETTINGS)
        component_settings.set(toolingapi_settings["username"], component_metadata)
        sublime.save_settings(COMPONENT_METADATA_SETTINGS)
        print (message.SEPRATE.format('All code are Downloaded.'))
        sublime.status_message(message.DOWNLOAD_ALL_SUCCESSFULLY)

        # After Refresh all succeed, start initiate sobject completions
        handle_initiate_sobjects_completions(120)

        # If get_static_resource_body is true, 
        # start to get all binary body of static resource
        if toolingapi_settings["get_static_resource_body"]:
            handle_get_static_resource_body(toolingapi_settings)

    api = SalesforceApi(toolingapi_settings)
    component_types = toolingapi_settings["component_types"]
    thread = threading.Thread(target=api.refresh_components, args=(component_types, ))
    thread.start()
    ThreadProgress(api, thread, "Initiate Project, Please Wait...", "New Project Succeed")
    handle_thread(thread, timeout)

def handle_get_static_resource_body(toolingapi_settings, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        
        if api.result == None: return
        if api.result["status_code"] > 399: return

        # Mkdir for output dir of zip file
        result = api.result
        outputdir = toolingapi_settings["workspace"] + "/staticresources"
        if not os.path.exists(outputdir): os.makedirs(outputdir)

        # Extract zip
        util.extract_zip(result["zipFile"], outputdir)

        # Move the file to staticresources path
        root_src_dir = outputdir + "/unpackaged/staticresources"
        root_dst_dir = toolingapi_settings["workspace"] + "/staticresources"
        for x in os.walk(root_src_dir):
            if not x[-1]: continue
            for _file in x[-1]:
                if not _file.endswith("resource"): continue
                if os.path.exists(root_dst_dir + '/' + _file):
                    os.remove(root_dst_dir + '/' + _file)
                os.rename(x[0] + '/' + _file, root_dst_dir + '/' + _file) 

        shutil.rmtree(outputdir + "/unpackaged", ignore_errors=True)
        os.remove(outputdir + "/package.zip")

    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.retrieve, 
        args=(soap_bodies.retrieve_static_resources_body, ))
    thread.start()
    ThreadProgress(api, thread, "Retrieve StaticResource", "Retrieve StaticResource Succeed")
    handle_thread(thread, timeout)

def handle_save_component(component_name, component_attribute, body, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return

        result = api.result
        file_base_name = component_name + component_attribute["extension"]
        if "success" in result and result["success"]:
            print (message.SEPRATE.format(message.SAVE_SUCCESSFULLY.format(file_base_name)))

    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.save_component, args=(component_attribute, body, ))
    thread.start()
    ThreadProgress(api, thread, "Save Component " + component_name,
        "Save Component " + component_name + " Succeed")
    handle_thread(thread, timeout)

def handle_create_component(data, component_name, component_type, view_id, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        
        # If create Succeed
        result = api.result

        # If created failed, just remove it
        if result["status_code"] > 399:
            view = util.get_view_by_id(view_id)
            os.remove(view.file_name())
            view.run_command("close")
            return
        
        # Get the created component id
        component_id = result.get("id")
        body = toolingapi_settings[component_type]["body"]
        extension = toolingapi_settings[component_type]["extension"]
        
        # Save it to component.sublime-settings
        s = sublime.load_settings(COMPONENT_METADATA_SETTINGS)
        username = toolingapi_settings["username"]
        components_dict = s.get(username)
        components_dict[component_type][component_name] = {
            "id": component_id,
            "url": post_url + "/" + component_id,
            "body": body,
            "extension": extension,
            "type": component_type,
            "is_test": False
        }
        s.set(username, components_dict)

        # Save settings and show success message
        sublime.save_settings(COMPONENT_METADATA_SETTINGS)
        file_base_name = component_name + extension
        print (message.SEPRATE.format(message.CREATE_SUCCESSFULLY.format(file_base_name)))
                
    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    post_url = "/services/data/v{0}.0/sobjects/".format(toolingapi_settings["api_version"]) + component_type
    thread = threading.Thread(target=api.post, args=(post_url, data, ))
    thread.start()
    ThreadProgress(api, thread, "Creating Component " + component_name, 
        "Creating Component " + component_name + " Succeed")
    handle_thread(thread, timeout)

def handle_refresh_component(component_attribute, file_name, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        
        result = api.result
        status_code = result["status_code"]
        
        # If error, just skip, error is processed in ThreadProgress
        if status_code > 399: return

        fp = open(file_name, "wb")
        try:
            body = bytes(result[component_body], "UTF-8")
        except:
            body = result[component_body].encode("UTF-8")

        fp.write(body)
        file_base_name = os.path.basename(file_name)

    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    component_body = component_attribute["body"]
    component_url = component_attribute["url"]
    thread = threading.Thread(target=api.get, args=(component_url, ))
    thread.start()
    ThreadProgress(api, thread, 'Refresh Component', 'Refresh Succeed')
    handle_thread(thread, timeout)

def handle_delete_component(component_url, file_name, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return

        # If succeed
        result = api.result
        if result["status_code"] > 399: return
        os.remove(file_name)
        sublime.active_window().run_command("close")

    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.delete, args=(component_url, ))
    thread.start()
    file_base_name = os.path.basename(file_name)
    ThreadProgress(api, thread, "Deleting " + file_base_name,
        "Delete " + file_base_name + " Succeed")
    handle_thread(thread, timeout)

def handle_push_topic(sobject, timeout=120):      
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return

        # If succeed
        result = api.result
        if result["status_code"] > 399: return

        print (result)

    toolingapi_settings = context.get_toolingapi_settings()
    api_version = toolingapi_settings["api_version"]
    api = SalesforceApi(toolingapi_settings)
    post_url = "/services/data/v{0}.0/sobjects/PushTopic".format(api_version)
    post_data = {
        "Name": sobject + "PushTopic",
        "Query": get_sobject_soql(toolingapi_settings["username"], sobject),
        "ApiVersion": "{0}.0".format(api_version),
        "NotifyForOperations": "All",
        "NotifyForFields": "Referenced"
    }
    thread = threading.Thread(target=api.post, args=(post_url, post_data, ))
    thread.start()
    ThreadProgress(api, thread, "Creating PushTopic", "PushTopic is created.")
    handle_thread(thread, timeout)

def get_sobject_soql(username, sobject):
    sobject_fields = get_sobject_fields(username, sobject)
    sobject_soql = 'SELECT ' + ",".join(sobject_fields) + " FROM " + sobject
    return sobject_soql

def get_sobject_fields(username, sobject):
    # If sobjects is exist in globals()[], just return it
    sobjects_completions = sublime.load_settings("sobjects_completion.sublime-settings")
    if not sobjects_completions.has(username):
        return ['Id', 'Name']

    sobject_fields_describe = sobjects_completions.get(username)[sobject].keys()
    sobject_fields = []
    for des in sobject_fields_describe:
        field_name, field_type = tuple(des.split("\t"))
        if field_type in ["textarea", "location"]: continue
        sobject_fields.append(field_name)

    return sobject_fields
