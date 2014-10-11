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
import datetime

from xml.sax.saxutils import unescape
from . import requests, context, util
from .context import COMPONENT_METADATA_SETTINGS
from .salesforce import soap_bodies, message
from .salesforce.api.bulk import BulkJob
from .salesforce.api.bulk import BulkApi
from .salesforce.api.metadata import MetadataApi
from .salesforce.api.tooling import ToolingApi
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
    settings = context.get_settings()
    username = settings["username"]

    # If sobjects is exist in globals()[], just return it
    if (username + "users") in globals(): 
        return globals()[username + "users"]
        
    # If sobjects is not exist in globals(), post request to pouplate it
    api = ToolingApi(settings)
    query = """SELECT Id, FirstName, LastName FROM User WHERE LastName != null 
               AND IsActive = true"""
    thread = threading.Thread(target=api.query_all, args=(query, ))
    thread.start()

    while thread.is_alive() or not api.result:
        time.sleep(1)

    # Exception Process
    if not api.result["success"]:
        util.show_output_panel(message.SEPRATE.format(util.format_error_message(api.result)))
        return

    records = api.result["records"]
    users = {}
    for user in records:
        if not user["FirstName"]:
            users[user["LastName"]] = user["Id"]
        else:
            users[user["LastName"] + " " + user["FirstName"]] = user["Id"]

    globals()[username + "users"] = users
    return users


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
    settings = context.get_settings()
    username = settings["username"]

    # If sobjects is exist in globals()[], just return it
    if (username + "sobject_recordtypes") in globals(): 
        return globals()[username + "sobject_recordtypes"]

    # If sobjects is not exist in globals(), post request to pouplate it
    api = ToolingApi(settings)
    query = "SELECT Id, Name, SobjectType FROM RecordType"
    thread = threading.Thread(target=api.query_all, args=(query, ))
    thread.start()

    while thread.is_alive() or not api.result:
        time.sleep(1)

    # Exception Process
    if not api.result["success"]:
        util.show_output_panel(message.SEPRATE.format(util.format_error_message(api.result)))
        return

    records = api.result["records"]
    sobject_recordtypes = {}
    for recordtype in records:
        sobject_type = recordtype["SobjectType"]
        recordtype_name = recordtype["Name"]
        recordtype_id = recordtype["Id"]
        sobject_recordtypes[sobject_type + ", " + recordtype_name] = recordtype_id

    # Add Master of every sobject to List
    sobjects_describe = util.populate_sobjects_describe()
    for sobject_type in sobjects_describe:
        sobject_describe = sobjects_describe[sobject_type]
        if not sobject_describe["layoutable"]: continue
        sobject_recordtypes[sobject_type + ", Master"] = "012000000000000AAA"

    globals()[username + "sobject_recordtypes"] = sobject_recordtypes
    return sobject_recordtypes

def handle_update_user_language(language, timeout=120):
    settings = context.get_settings()
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.update_user, args=({"LanguageLocaleKey": language}, ))
    thread.start()
    ThreadProgress(api, thread, "Updating User Language", "User language is updated to " + language)

def handle_login_thread(default_project, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return

        result = api.result
        if result and result["success"]:
            print (message.SEPRATE.format("Login Succeed"))

    settings = context.get_settings()
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.login, args=(False, ))
    thread.start()
    handle_thread(thread, timeout)
    ThreadProgress(api, thread, "Login to switched project", default_project + " Login Succeed")

def handle_view_code_coverage(component_name, component_attribute, body, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return

        result = api.result
        if not result["success"]: return

        if result["totalSize"] == 0:
            util.show_output_panel(message.SEPRATE.format("You should run test class firstly"))
            return

        uncovered_lines = result["records"][0]["Coverage"]["uncoveredLines"]
        covered_lines = result["records"][0]["Coverage"]["coveredLines"]
        covered_lines_count = len(covered_lines)
        uncovered_lines_count = len(uncovered_lines)
        total_lines_count = covered_lines_count + uncovered_lines_count
        if total_lines_count == 0:
            util.show_output_panel(message.SEPRATE.format("You should run test class firstly"))
            return

        # Open new view to display the coverage result
        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": component_name + " Code Coverage",
            "input": body
        })

        all_region_by_line = view.lines(sublime.Region(0, view.size()))
        uncovered_region = []
        for region in all_region_by_line:
            line = view.rowcol(region.begin() + 1)[0] + 1
            if line in uncovered_lines:
                uncovered_region.append(region)

        view.add_regions("mark", uncovered_region, "bookmark", 'markup.inserted',
            sublime.DRAW_NO_FILL | sublime.DRAW_NO_OUTLINE | sublime.DRAW_STIPPLED_UNDERLINE)

        coverage = covered_lines_count / total_lines_count * 100
        print (message.SEPRATE.format("The coverage is %.2f%%(%s/%s), " %\
            (coverage, covered_lines_count, total_lines_count) + 
            "uncovered lines are marked in the new open view"))

    settings = context.get_settings()
    api = ToolingApi(settings)
    query = "SELECT Coverage FROM ApexCodeCoverageAggregate " +\
        "WHERE ApexClassOrTriggerId = '{0}'".format(component_attribute["id"])
    thread = threading.Thread(target=api.query, args=(query, True, ))
    thread.start()
    ThreadProgress(api, thread, "View Code Coverage of " + component_name,
        "View Code Coverage of " + component_name + " Succeed")
    handle_thread(thread, timeout)

def handle_refresh_folder(folders_dict, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        
        # Not succeed
        if not api.result or not api.result["success"]: return

        # Get refresh result
        result = api.result

        # Populate extract_to directory
        extract_to = settings["workspace"]

        # Extract zip, True means not override package.xml
        util.extract_encoded_zipfile(result["zipFile"], extract_to, True)

        util.reload_apex_code_cache(result["fileProperties"], settings)

        # Hide panel 0.5 seconds later
        sublime.set_timeout_async(util.hide_output_panel, 500)

    # Start to request
    settings = context.get_settings()
    api = MetadataApi(settings)
    meta_types = []
    for folder in folders_dict:
        meta_types.append(settings[folder]["type"])
    types = util.build_package_types(meta_types)
    body = soap_bodies.retrieve_body.replace("{{allowed_packages}}", "").replace("{{meta_types}}", types)
    thread = threading.Thread(target=api.retrieve, args=(body, ))
    thread.start()
    handle_thread(thread, timeout)
    message = "Refresh Folder"
    ThreadProgress(api, thread, message, message+" Succeed")

def handle_reload_symbol_tables(timeout=120):
    """
    Reload Symbol Tables to Local Cache
    """

    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return

        result = api.result
        if not result["success"]: return

        # Get the username of default project
        username = settings["username"]

        # Save symbolTable to component_metadata.sublime-settings
        symbol_table_cache = sublime.load_settings("symbol_table.sublime-settings")
        symboltable_dict = symbol_table_cache.get(username, {})
        for record in result["records"]:
            # Sometimes symbolTable is null, just skip
            if not record["SymbolTable"]: continue

            # Outer completions 
            outer = util.parse_symbol_table(record["SymbolTable"])
            symboltable_dict[record["Name"].lower()] = {
                "outer" : outer,
                "name": record["Name"]
            }

            # Inner completions
            inners = {}
            for inn in record["SymbolTable"]["innerClasses"]:
                inner = util.parse_symbol_table(inn)
                inners[inn["name"].lower()] = inner
            symboltable_dict[record["Name"].lower()]["inners"] = inners

        symbol_table_cache.set(settings["username"], symboltable_dict)
        sublime.save_settings("symbol_table.sublime-settings")

    settings = context.get_settings()
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.query_symbol_table, args=(50, ))
    thread.start()
    wating_message = "Reloading Symbol Tables"
    ThreadProgress(api, thread, wating_message, wating_message + " Succeed")
    handle_thread(thread, timeout)

def handle_reload_sobjects_completions(timeout=120):
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
        sobjects_completion = {"sobjects": {}}

        all_parent_relationship_dict = {}
        all_child_relationship_dict = {}
        display_field_name_and_label = settings["display_field_name_and_label"]
        for sobject_describe in results:
            # Initiate Sobject completions
            if "name" not in sobject_describe: continue
            sobject_name = sobject_describe["name"]

            # If sobject is excluded sobject, just continue
            sobject_name = sobject_name.lower()
            sobjects_completion["sobjects"][sobject_name] = {
                "name": sobject_describe["name"],
                "keyPrefix": sobject_describe["keyPrefix"],
                "layoutable": sobject_describe["layoutable"],
                "triggerable": sobject_describe["triggerable"]
            }

            # Combine Fields dict, Picklist Field dict and parent relationship dict
            fields_dict = {}
            picklist_field_dict = {}
            parent_relationship_dict = {}
            child_relationship_dict = {}
            for f in sobject_describe["fields"]:
                field_name = f["name"]
                precision = f["precision"]
                scale = f["scale"]
                field_type = f["type"]

                if f["calculatedFormula"]:
                    capitalize_field = field_type.capitalize()
                    field_desc_dict = {
                        "double": "Formula(%s, %s, %s)" % (capitalize_field, precision, scale),
                        "currency": "Formula(%s, %s, %s)" % (capitalize_field, precision, scale),
                        "date": "Formula(Date)",
                        "datetime": "Formula(Datetime)",
                        "boolean": "Formula(Boolean)",
                        "int": "Formula(Integer)",
                        "reference": "Reference",
                        "other": "Formula(%s, %s)" % (capitalize_field, f["length"])
                    }
                else:
                    field_desc_dict = {
                        "double": "Double(%s, %s)" % (precision, scale),
                        "currency": "Currency(%s, %s)" % (precision, scale),
                        "date": "Date",
                        "datetime": "Datetime",
                        "boolean": "Boolean",
                        "reference": "Reference",
                        "int": "Integer",
                        "other": "%s(%s)" % (field_type.capitalize(), f["length"])
                    }

                # If display_field_name_and_label setting is true, 
                # display both field name and field label
                field_name_desc = "%s(%s)" % (field_name, f["label"]) \
                    if display_field_name_and_label else field_name

                # Display field type with specified format
                field_type_desc = field_desc_dict[field_type] if field_type \
                    in field_desc_dict else field_desc_dict["other"]

                fd = "%s\t%s" % (field_name_desc, field_type_desc)
                fields_dict[fd] = field_name

                # Picklist Dcit
                if f["type"] == "picklist":
                    picklists = []
                    for picklistValue in f["picklistValues"]:
                        picklists.append({
                            "label": picklistValue["label"],
                            "value": picklistValue["value"]
                        })
                    picklist_field_dict[field_name] = picklists

                # List all Reference Field Relationship Name as fields
                # Some fields has two more references, we can't list the fields of it
                if not len(f["referenceTo"]) == 1: continue
                parentRelationshipName = f["relationshipName"]
                if not parentRelationshipName: continue
                parentSobject = f["referenceTo"][0]
                if parentRelationshipName in all_parent_relationship_dict:
                    is_duplicate = False
                    for so in all_parent_relationship_dict[parentRelationshipName]:
                        if parentSobject == so:
                            is_duplicate = True
                            break

                    if not is_duplicate:
                        all_parent_relationship_dict[parentRelationshipName].append(parentSobject)
                else:
                    all_parent_relationship_dict[parentRelationshipName] = [parentSobject]

                # Add Parent Relationship Name
                parent_relationship_dict[f["relationshipName"]] = parentSobject
            
            # Child Relationship dict
            for f in sobject_describe["childRelationships"]:
                childRelationshipName = f["relationshipName"]
                childSobject = f["childSObject"]
                if not childRelationshipName: continue

                # Add Parent Relationship Name as Field
                child_relationship_dict[childRelationshipName] = childSobject

            # Combine sobject fields dict and sobject child relationship dict
            sobjects_completion["sobjects"][sobject_name]["fields"] = fields_dict
            sobjects_completion["sobjects"][sobject_name]["picklist_fields"] = picklist_field_dict
            sobjects_completion["sobjects"][sobject_name]["parentRelationships"] = parent_relationship_dict
            sobjects_completion["sobjects"][sobject_name]["childRelationships"] = child_relationship_dict

        # Populate Child Relationship and Parent Relationship

        sobjects_completion["parentRelationships"] = all_parent_relationship_dict
        # sobjects_completion["childRelationships"] = all_child_relationship_dict

        # Every project has unique username
        username = settings["username"]
        s.set(username, sobjects_completion)

        # Save settings
        sublime.save_settings("sobjects_completion.sublime-settings")

        # Output message
        print (message.SEPRATE.format('sObjects Cache are saved to Local'))

    def handle_thread(api, thread, timeout=120):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(api, thread, timeout), timeout)
            return

        # Exception Process
        if not api.result or not api.result["success"]: return

        sobjects_describe = api.result["sobjects"]
        threads = []
        apis = []
        for sobject in sobjects_describe:
            sobject_describe = sobjects_describe[sobject]
            if sobject in settings["allowed_sobjects"] or sobject_describe["custom"]:
                api = ToolingApi(settings)
                thread = threading.Thread(target=api.describe_sobject, args=(sobject, ))
                thread.start()
                threads.append(thread)
                apis.append(api)

        ThreadsProgress(threads, "Download Cache of Sobjects", "Download Cache of Sobjects Succeed")
        handle_threads(apis, threads, 10)

    settings = context.get_settings()
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.describe_global, args=())
    thread.start()
    ThreadProgress(api, thread, "Global Describe", "Global Describe Succeed")
    handle_thread(api, thread, timeout)

def handle_deploy_thread(base64_encoded_zip, timeout=120):
    settings = context.get_settings()
    api = MetadataApi(settings)
    thread = threading.Thread(target=api.deploy, args=(base64_encoded_zip, ))
    thread.start()
    ThreadProgress(api, thread, "Deploy Metadata", "Deploy Metadata Succeed")

def handle_close_jobs_thread(job_ids, timeout=120):
    settings = context.get_settings()
    bulkjob = BulkJob(settings, None, None)
    for job_id in job_ids:
        thread = threading.Thread(target=bulkjob.close_job, args=(job_id,))
        thread.start()

def handle_bulk_operation_thread(sobject, inputfile, operation, timeout=120):
    settings = context.get_settings()
    bulkapi = BulkApi(settings, sobject, inputfile)
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

def handle_backup_sobject_thread(sobject, soql=None, timeout=120):
    settings = context.get_settings()
    bulkapi = BulkApi(settings, sobject, soql)
    thread = threading.Thread(target=bulkapi.query, args=())
    thread.start()
    wait_message = "Export Records of " + sobject
    ThreadProgress(bulkapi, thread, wait_message, wait_message + " Succeed")

def handle_backup_all_sobjects_thread(timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return

        result = api.result
        if not result or not result["success"]: return
        
        sobjects_describe = api.result["sobjects"]
        threads = []
        for sobject in sobjects_describe:
            bulkapi = BulkApi(settings, sobject)
            thread = threading.Thread(target=bulkapi.query, args=())
            thread.start()
            threads.append(thread)

        wait_message = "Export All Sobjects Records"
        ThreadsProgress(threads, wait_message, wait_message + " Succeed")

    settings = context.get_settings()
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.describe_global, args=())
    thread.start()
    ThreadProgress(api, thread, "Describe Global", "Describe Global Succeed")
    handle_thread(thread, timeout)

def handle_retrieve_all_thread(timeout=120, retrieve_all=True):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return

        result = api.result
        if not result or not result["success"]: return

        # Mkdir for output dir of zip file
        util.add_project_to_workspace(settings)
        outputdir = settings["workspace"] + "/metadata"

        # Extract zip
        util.extract_encoded_zipfile(result["zipFile"], outputdir)

        # Refresh Project Folders
        sublime.active_window().run_command("refresh_folder_list")

    settings = context.get_settings()
    api = MetadataApi(settings)

    if retrieve_all:
        soap_body = soap_bodies.retrieve_all_task_body
    else:
        soap_body = soap_bodies.retrieve_sobjects_workflow_task_body

    thread = threading.Thread(target=api.retrieve, args=(soap_body, ))
    thread.start()
    ThreadProgress(api, thread, "Retrieve Metadata", "Retrieve Metadata Succeed")
    handle_thread(thread, timeout)

def handle_export_workflows(settings, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        
        # If succeed
        sobjects_describe = api.result["sobjects"]
        util.parse_workflow_metadata(settings, sobjects_describe.keys())
        sublime.active_window().run_command("refresh_folder_list")
        print (message.SEPRATE.format("Outputdir: " + outputdir))

    outputdir = settings["workspace"] + "/workflow/"
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.describe_global, args=())
    thread.start()
    ThreadProgress(api, thread, "Export All Workflows", "Outputdir: " + outputdir)
    handle_thread(thread, 10)

def handle_export_validation_rules(settings, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return

        # If succeed
        sobjects_describe = api.result["sobjects"]
        util.parse_validation_rule(settings, sobjects_describe.keys())
        sublime.active_window().run_command("refresh_folder_list")
        print (message.SEPRATE.format("Outputdir: " + outputdir))

    outputdir = settings["workspace"] + "/Validation/Validation Rules.csv"
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.describe_global, args=())
    thread.start()
    ThreadProgress(api, thread, "Export All Validation Rules", "Outputdir: " + outputdir)
    handle_thread(thread, 10)

def handle_export_customfield(timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        
        # If succeed
        result = api.result
        if not result or not result["success"]: return

        # Write list to csv
        if not os.path.exists(outputdir): os.makedirs(outputdir)
        records = sorted(result["records"], key=lambda k : k['TableEnumOrId'])
        util.list2csv(outputdir + "/CustomField.csv", records)
        sublime.active_window().run_command("refresh_folder_list")

        # Output log
        print (message.SEPRATE.format(outputdir))

    settings = context.get_settings()
    workspace = context.get_settings().get("workspace")
    outputdir = workspace + "/CustomField"
    api = ToolingApi(settings)
    query = "SELECT Id,TableEnumOrId,DeveloperName,NamespacePrefix,FullName FROM CustomField"
    thread = threading.Thread(target=api.query, args=(query, True,))
    thread.start()
    ThreadProgress(api, thread, 'Describe CustomField', 
        'Outputdir: ' + outputdir + "/customfield.csv")
    handle_thread(thread, 10)

def handle_export_data_template_thread(sobject, recordtype_name, recordtype_id, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        
        # If succeed
        result = api.result
        if not result or not result["success"]: return

        # If outputdir is not exist, just make it
        if not os.path.exists(outputdir): os.makedirs(outputdir)

        # Write parsed result to csv
        util.parse_data_template(output_file_dir, result)
        sublime.active_window().run_command("refresh_folder_list")
        util.show_output_panel(message.SEPRATE.format("Data Template outputdir: " + output_file_dir))

    settings = context.get_settings()
    outputdir = settings["workspace"] + "/template"
    output_file_dir = outputdir + "/" + sobject + "-" + recordtype_name + ".csv"
    api = ToolingApi(settings)
    url = "/sobjects/%s/describe/layouts/%s" % (sobject, recordtype_id)
    print (url)
    thread = threading.Thread(target=api.get, args=(url, ))
    thread.start()
    wait_message = "Export Data Template of %s=>%s" % (sobject, recordtype_name)
    ThreadProgress(api, thread, wait_message, "Outputdir: " + output_file_dir)
    handle_thread(thread, 120)

def handle_execute_rest_test(operation, url, data=None, timeout=120):
    def handle_new_view_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_new_view_thread(thread, timeout), timeout)
            return
        
        result = api.result
        
        # If succeed
        if "list" in result: result = result["list"]
        if "str"  in result: result = result["str"]

        # If response result is just like '"{\\"name\\":\\"test\\"}"'
        # we will remove the \\ and convert it to json automatically
        try:
            if "\\" in result:
                result = result.replace("\\", "")
                result = result[1:-1]
                result = json.loads(result)
        except:
            pass

        # Remove the useless success attribute
        if isinstance(result, dict) and "success" in result:
            del result["success"]
        
        # No error, just display log in a new view
        view = sublime.active_window().new_file()
        view.set_syntax_file("Packages/JavaScript/JavaScript.tmLanguage")
        view.run_command("new_view", {
            "name": "Execute Rest %s Result" % operation,
            "input": pprint.pformat(result)
        })

        # If you have installed the htmljs plugin, below statement will work
        view.run_command("htmlprettify")

    settings = context.get_settings()
    api = ToolingApi(settings)
    http_methods_target = {
        "Get": api.get,
        "Delete": api.delete,
        "Head": api.head,
        "Put": api.put,
        "Post": api.post,
        "Query": api.query,
        "Tooling Query": api.query,
        "Query All": api.query_all,
        "Retrieve Body": api.retrieve_body,
        "Patch": api.patch,
        "Search": api.search,
        "Quick Search": api.quick_search
    }
    
    target = http_methods_target[operation]
    if operation in ['Put', 'Post', 'Patch']:
        thread = threading.Thread(target=target, args=(url, data,))
    elif operation == "Tooling Query":
        thread = threading.Thread(target=target, args=(url, True))
    else:
        thread = threading.Thread(target=target, args=(url,))
    thread.start()
    progress_message = "Execute Rest %s Test" % operation
    ThreadProgress(api, thread, progress_message, progress_message + " Succeed", open_console=False)
    handle_new_view_thread(thread, timeout)

def handle_execute_query(soql, timeout=120):
    def handle_new_view_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_new_view_thread(thread, timeout), timeout)
            return
        
        # If succeed
        result = api.result
        if not result["success"]: return
        
        # No error, just display log in a new view
        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": "Execute Query Result",
            "input": pprint.pformat(result)
        })

        # Keep the history in the local history rep
        util.add_operation_history('execute_query', soql)

    settings = context.get_settings()
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.query, args=(soql,))
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
        if not result["success"]: return

        # No error, just display log in a new view
        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": "Execute Anonymous Result",
            "input": util.parse_execute_anonymous_xml(result)
        })

        # Keep the history apex script to local
        util.add_operation_history('execute_anonymous', apex_string)

    settings = context.get_settings()
    api = MetadataApi(settings)
    thread = threading.Thread(target=api.execute_anonymous, args=(apex_string, ))
    thread.start()
    ThreadProgress(api, thread, "Execute Anonymous", "Execute Anonymous Succeed")
    handle_new_view_thread(thread, timeout)

def handle_fetch_debug_logs(user_full_name, user_id, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return

        result = api.result
        records = result["records"]
        debug_logs_table = util.format_debug_logs(settings, records)
        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": "Debug Logs",
            "input": debug_logs_table
        })

    settings = context.get_settings()
    api = ToolingApi(settings)
    query = "SELECT Id,LogUserId,LogLength,Request,Operation,Application," +\
            "Status,DurationMilliseconds,StartTime,Location FROM ApexLog " +\
            "WHERE LogUserId='%s' ORDER BY StartTime DESC LIMIT %s" % (user_id, settings["last_n_logs"])
    thread = threading.Thread(target=api.query, args=(query, ))
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
        if not result["success"]: return
        print (message.SEPRATE.format(user_name + " " + result["message"]) )

    settings = context.get_settings()
    api = ToolingApi(settings)
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
        
        if not api.result["success"]: return

        try:
            body = api.result["body"]
            body = body.encode("utf-8")
        except Exception as e:
            print (str(e))
            body = api.result["body"]

        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": "Debug Log Detail",
            "input": api.result["body"]
        })

    settings = context.get_settings()
    api = ToolingApi(settings)
    url = "/sobjects/ApexLog/" + log_id + "/Body"
    thread = threading.Thread(target=api.retrieve_body, args=(url, ))
    thread.start()
    ThreadProgress(api, thread, "Get Log Detail of " + log_id, 
        "Get Log Detail of " + log_id + " Succeed")
    handle_thread(thread, timeout)

def handle_run_all_test(timeout=120):
    def handle_threads(api_threads, timeout):
        for api, thread in api_threads:
            if thread.is_alive():
                sublime.set_timeout(lambda: handle_threads(api_threads, timeout), timeout)
                return
            else:
                result = api.result
                if "success" in result and not result["success"]: continue

                # No error, just display log in a new view
                test_result = util.parse_test_result(result)
                view = util.get_view_by_name("Run All Test Result")
                if not view:
                    view = sublime.active_window().new_file()
                    view.run_command("new_dynamic_view", {
                        "view_id": view.id(),
                        "view_name": "Run All Test Result",
                        "input": util.parse_test_result(result) + "\n" * 4 + "*" * 100
                    })
                else:
                    view.run_command("new_dynamic_view", {
                        "view_id": view.id(),
                        "view_name": "Run All Test Result",
                        "input": "\n" + util.parse_test_result(result) + "\n" * 4 + "*" * 100,
                        "point": view.size()
                    })

                api_threads.remove((api, thread))


        # If Network issue, view will be None
        if not util.get_view_by_name("Run All Test Result"): return

        # After run test succeed, get ApexCodeCoverageAggreate
        query = "SELECT ApexClassOrTrigger.Name, NumLinesCovered, NumLinesUncovered, Coverage " +\
                "FROM ApexCodeCoverageAggregate"
        api = ToolingApi(settings)
        thread = threading.Thread(target=api.query, args=(query, True, ))
        thread.start()
        wait_message = "Get Code Coverage of All Class"
        ThreadProgress(api, thread, wait_message, wait_message + " Succeed")
        handle_code_coverage_thread(thread, api, view, timeout)

    def handle_code_coverage_thread(thread, api, view, timeout=120):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_code_coverage_thread(thread, api, view, timeout), timeout)
            return

        code_coverage = util.parse_code_coverage(api.result)
        view.run_command("new_dynamic_view", {
            "view_id": view.id(),
            "view_name": "Run All Test Result",
            "input": code_coverage,
            "point": view.size()
        })

    class_ids = util.populate_all_test_classes()
    if not class_ids: return

    settings = context.get_settings()

    api_threads = []
    threads = []
    for class_id in class_ids:
        api = ToolingApi(settings)
        thread = threading.Thread(target=api.run_test, args=(class_id, ))
        threads.append(thread)
        api_threads.append((api, thread))
        thread.start()
    ThreadsProgress(threads, "Run All Test", "Run All Test Succeed")
    handle_threads(api_threads, timeout)

def handle_run_test(class_name, class_id, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return

        # If succeed
        result = api.result

        # If error
        if "success" in result and not result["success"]: return

        # No error, just display log in a new view
        test_result = util.parse_test_result(result)
        class_name = result[0]["ApexClass"]["Name"]
        view = sublime.active_window().new_file()
        view.run_command("new_dynamic_view", {
            "view_id": view.id(),
            "view_name": "Test Result",
            "input": test_result
        })
        
        # Keep the history in the local history rep
        util.add_operation_history('Test/' + class_name, test_result)

        # After run test succeed, get ApexCodeCoverageAggreate
        query = "SELECT ApexClassOrTrigger.Name, NumLinesCovered, NumLinesUncovered, Coverage " +\
                "FROM ApexCodeCoverageAggregate"
        thread = threading.Thread(target=api.query, args=(query, True, ))
        thread.start()
        wait_message = "Get Code Coverage of " + class_name
        ThreadProgress(api, thread, wait_message, wait_message + " Succeed")
        handle_code_coverage_thread(thread, view, timeout)

    def handle_code_coverage_thread(thread, view, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_code_coverage_thread(thread, view, timeout), timeout)
            return

        code_coverage = util.parse_code_coverage(api.result)
        view.run_command("new_dynamic_view", {
            "view_id": view.id(),
            "view_name": "Test Result",
            "input": code_coverage,
            "point": view.size()
        })

    settings = context.get_settings()
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.run_test, args=(class_id, ))
    thread.start()
    ThreadProgress(api, thread, "Run Test Class " + class_name, "Run Test for " + class_name + " Succeed")
    handle_thread(thread, timeout)

def handle_run_sync_test_classes(class_names, timeout=120):
    def handle_new_view_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_new_view_thread(thread, timeout), timeout)
            return
        elif not api.result:
            return

        # If succeed
        result = api.result
        pprint.pprint(result)
        pprint.pprint(util.parse_code_coverage(result))

    settings = context.get_settings()
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.run_tests_synchronous, args=(class_names, ))
    thread.start()
    wait_message = 'Run Sync Test Classes for Specified Test Class'
    ThreadProgress(api, thread, wait_message, wait_message + ' Succeed')
    handle_new_view_thread(thread, timeout)

def handle_run_async_test_classes(class_ids, timeout=120):
    def handle_new_view_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_new_view_thread(thread, timeout), timeout)
            return
        elif not api.result:
            return

        # If succeed
        result = api.result
        pprint.pprint(result)

    settings = context.get_settings()
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.run_tests_asynchronous, args=(class_ids, ))
    thread.start()
    wait_message = 'Run Sync Test Classes for Specified Test Class'
    ThreadProgress(api, thread, wait_message, wait_message + ' Succeed')
    handle_new_view_thread(thread, timeout)

def handle_generate_sobject_soql(sobject, timeout=120):
    def handle_new_view_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_new_view_thread(thread, timeout), timeout)
            return

        # If succeed
        result = api.result
        
        # Error Message are prcoessed in ThreadProgress
        if not result["success"]: return

        # No error, just display log in a new view
        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": sobject + " SOQL",
            "input": result["soql"]
        })

        # Keep sobject describe history
        util.add_operation_history('SOQL/' + sobject, result["soql"])

    settings = context.get_settings()
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.combine_soql, args=(sobject, ))
    thread.start()
    wait_message = 'Generate SOQL for ' + sobject
    ThreadProgress(api, thread, wait_message, wait_message + ' Succeed')
    handle_new_view_thread(thread, timeout)

def handle_describe_sobject(sobject, timeout=120):
    def handle_new_view_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_new_view_thread(thread, timeout), timeout)
            return

        # If succeed
        result = api.result
        
        # Error Message are prcoessed in ThreadProgress
        if not result["success"]: return

        # No error, just display log in a new view
        view = sublime.active_window().new_file()
        describe_result = util.parse_sobject_field_result(result)
        view.run_command("new_view", {
            "name": sobject + " Describe Result",
            "input": describe_result
        })

        # Keep sobject describe history
        util.add_operation_history('describe/' + sobject, describe_result)

    settings = context.get_settings()
    api = ToolingApi(settings)
    sobject_url = "/sobjects/" + sobject + "/describe"
    thread = threading.Thread(target=api.get, args=(sobject_url, ))
    thread.start()
    ThreadProgress(api, thread, 'Describe ' + sobject, 'Describe ' + sobject + ' Succeed')
    handle_new_view_thread(thread, timeout)

def handle_export_specified_workbooks(sobjects, timeout=120):
    settings = context.get_settings()
    api = ToolingApi(settings)
    threads = []
    for sobject in sobjects:
        thread = threading.Thread(target=api.generate_workbook, args=(sobject, ))
        threads.append(thread)
        thread.start()

    ThreadsProgress(threads, "Generating Sobjects Workbook", 
        "Sobjects Workbook are Generated")

def handle_export_all_workbooks(timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        
        # Exception Process
        if not api.result["success"]: return

        # If succeed
        sobjects_describe = api.result["sobjects"]
        for sobject in sobjects_describe:
            thread = threading.Thread(target=api.generate_workbook, args=(sobject, ))
            thread.start()

    settings = context.get_settings()
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.describe_global, args=())
    thread.start()
    ThreadProgress(api, thread, "Global Describe Common", "Global Describe Common Succeed")
    handle_thread(thread, timeout)

def handle_new_project(settings, is_update=False, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        
        # If succeed, something may happen,
        # for example, user password is expired
        result = api.result
        if not result or not result["success"]: return

        # Extract the apex code to workspace
        extract_to = settings["workspace"]

        # Just remove the packages folder and src folder
        if os.path.exists(extract_to):
            # Remove packages directory
            if os.path.exists(os.path.join(extract_to, "packages")):
                try:
                    shutil.rmtree(os.path.join(extract_to, "packages"))
                except Exception as e:
                    pass

        # Makedir for subscribed meta types
        for meta_folder in settings["subscribed_meta_folders"]:
            outputdir = os.path.join(extract_to, "src", meta_folder);
            if not os.path.exists(outputdir): os.makedirs(outputdir)

        # Extract the zipFile to extract_to
        util.extract_encoded_zipfile(result["zipFile"], extract_to)

        # Apex Code Cache
        if isinstance(result["fileProperties"], list):
            util.reload_apex_code_cache(result["fileProperties"], settings)

        # Hide panel
        sublime.set_timeout_async(util.hide_output_panel, 500)

        # Reload sObject Cache and SymbolTables
        if not is_update: 
            handle_reload_sobjects_completions(120)
            
            if settings["reload_symbol_tables_when_create_project"]:
                handle_reload_symbol_tables(120)

        # Write the settings to local cache
        if settings["keep_config_history"]:
             # Not keep the confidential info to .settings
            del settings["projects"]
            del settings["password"]
            del settings["default_project"]

            util.add_config_history('settings', str(settings).replace("'", '"'))
            util.add_config_history('session', str(api.session).replace("'", '"'))

        # In windows, folder is not shown in the sidebar, 
        # we need to refresh the sublime workspace to show it
        sublime.active_window().run_command("refresh_folder_list")

    settings = context.get_settings()
    api = MetadataApi(settings)
    types = util.build_package_types(settings["subscribed_meta_types"])
    body = soap_bodies.retrieve_body.replace("{{meta_types}}", types)
    body = body.replace("{{allowed_packages}}", 
        "".join(["<met:packageNames>%s</met:packageNames>" % a for a in settings["allowed_packages"]]))
    thread = threading.Thread(target=api.retrieve, args=(body, ))
    thread.start()
    wating_message = ("Creating New " if not is_update else "Updating ") + " Project"
    ThreadProgress(api, thread, wating_message, wating_message + " Succeed")
    handle_thread(thread, timeout)

def handle_retrieve_package(package_xml_content, extract_to, 
                            ignore_package_xml=False, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        
        # If not succeed, just stop
        if not api.result or not api.result["success"]: return

        # Mkdir for output dir of zip file
        result = api.result

        # Extract zip
        util.extract_encoded_zipfile(result["zipFile"], extract_to, ignore_package_xml)

        # Hide panel 0.5 seconds later
        sublime.set_timeout_async(util.hide_output_panel, 500)

    # Start to request
    settings = context.get_settings()
    api = MetadataApi(settings)
    types = util.parse_package(package_xml_content)
    body = soap_bodies.retrieve_body.replace("{{meta_types}}", types)
    thread = threading.Thread(target=api.retrieve, args=(body, ))
    thread.start()
    handle_thread(thread, timeout)
    ThreadProgress(api, thread, "Retrieve Metadata", "Retrieve Metadata Succeed")

def handle_save_component(component_name, component_attribute, body, is_check_only=False, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return

        # Set Thread alive flag to False
        globals()[username + component_name] = False

        # Process request result
        result = api.result
        extension = component_attribute["extension"]
        file_base_name =  component_name + extension
        if "success" in result and result["success"]:
            # 1. Write succeed body to local change history
            if settings["keep_local_change_history"]:
                # Get current file name and Read file content
                view = sublime.active_window().active_view()

                # Get Workspace, if not exist, make it
                workspace = settings["workspace"]+"/.history/"+component_attribute["type"]
                if not os.path.exists(workspace):
                    os.makedirs(workspace)

                # Backup current file
                time_stamp = time.strftime("%Y-%m-%d-%H-%M", time.localtime())
                outputdir = workspace+"/"+component_name+"-"+time_stamp+"-history"+extension
                with open(outputdir, "wb") as fp:
                    fp.write(body.encode("utf-8"))

            # 2. Write symbol table to local cache
            if "symbol_table" in result:
                symbol_table = result["symbol_table"]

                # Get symbolTable from component_metadata.sublime-settings
                symbol_table_cache = sublime.load_settings("symbol_table.sublime-settings")
                symboltable_dict = symbol_table_cache.get(username, {})

                # Outer completions 
                outer = util.parse_symbol_table(symbol_table)
                symboltable_dict[symbol_table["name"].lower()] = {
                    "outer" : outer,
                    "name": symbol_table["name"]
                }

                # Inner completions
                inners = {}
                for inn in symbol_table["innerClasses"]:
                    inner = util.parse_symbol_table(inn)
                    inners[inn["name"].lower()] = inner
                symboltable_dict[symbol_table["name"].lower()]["inners"] = inners

                symbol_table_cache.set(settings["username"], symboltable_dict)
                sublime.save_settings("symbol_table.sublime-settings")

            # Output succeed message in the console
            save_or_compile = "compiled" if is_check_only else "saved"
            util.show_output_panel(message.SEPRATE.format(
                "%s is %s at %s" % (file_base_name, save_or_compile,
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))))

            # If succeed, just hide it in two seconds later
            delay_seconds = settings["delay_seconds_for_hidden_output_panel_when_succeed"]
            sublime.set_timeout_async(util.hide_output_panel, delay_seconds * 1000)

        # If not succeed, just go to the error line
        # Because error line in page is always at the line 1, so just work in class or trigger
        elif "success" in result and not result["success"]:
            view = sublime.active_window().active_view()
            if file_base_name in view.file_name() and extension in [".trigger", ".cls"]:
                if "line" in result:
                    line = result["line"]
                elif "lineNumber" in result:
                    line = result["lineNumber"]
                else:
                    return
                    
                if isinstance(line, list): line = line[0]
                view.run_command("goto_line", {"line": line})
                view.run_command("expand_selection", {"to":"line"})

                # Add highlight for error line and remove the highlight after several seconds
                component_id = component_attribute["id"]
                view.run_command("set_check_point", {"mark":component_id+"error"})
                delay_seconds = settings["delay_seconds_for_hidden_output_panel_when_failed"]
                sublime.set_timeout_async(view.run_command("remove_check_point", 
                    {"mark":component_id+"error"}), delay_seconds * 1000)

    # If saving is in process, just skip
    settings = context.get_settings()
    username = settings["username"]
    if username + component_name in globals():
        is_thread_alive = globals()[username + component_name]
        if is_thread_alive:
            print ('%s is in process' % component_name);
            return

    api = ToolingApi(settings)
    thread = threading.Thread(target=api.save_component,
        args=(component_attribute, body, is_check_only, ))
    thread.start()

    # If saving thread is started, set the flag to True
    globals()[username + component_name] = True

    # Display thread progress
    wait_message = ("Compiling " if is_check_only else "Saving ") + component_name
    ThreadProgress(api, thread, wait_message, wait_message + " Succeed")
    handle_thread(thread, timeout)

def handle_create_component(data, component_name, component_type, markup_or_body, file_name, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        
        # If create Succeed
        result = api.result

        # If created failed, just remove it
        if not result["success"]:
            os.remove(file_name)
            return

        # If created succeed, just open it
        sublime.active_window().open_file(file_name)

        # Get the created component id
        component_id = result.get("id")
        extension = settings[component_type]["extension"]
        
        # Save it to component.sublime-settings
        s = sublime.load_settings(COMPONENT_METADATA_SETTINGS)
        username = settings["username"]
        components_dict = s.get(username)

        # Prevent exception for creating component if no component in org
        if component_type not in components_dict: 
            components_dict = {component_type : {}}

        # Build components dict
        components_dict[component_type][component_name.lower()] = {
            "id": component_id,
            "name": component_name,
            "url": post_url + "/" + component_id,
            "body": markup_or_body,
            "extension": extension,
            "type": component_type,
            "is_test": False
        }
        s.set(username, components_dict)

        # Save settings and show success message
        sublime.save_settings(COMPONENT_METADATA_SETTINGS)
        file_base_name = component_name + extension
        print (message.SEPRATE.format(
            "{0} is created successfully at {1}".format(file_base_name, 
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))))
                
    settings = context.get_settings()
    api = ToolingApi(settings)
    post_url = "/sobjects/" + component_type
    thread = threading.Thread(target=api.post, args=(post_url, data, ))
    thread.start()
    ThreadProgress(api, thread, "Creating Component " + component_name, 
        "Creating Component " + component_name + " Succeed")
    handle_thread(thread, timeout)

def handle_refresh_static_resource(component_attribute, file_name, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        
        result = api.result

        # If error, just skip, error is processed in ThreadProgress
        if not result["success"]: return

        fp = open(file_name, "wb")
        fp.write(bytes(result["body"], "utf-8"))

    settings = context.get_settings()
    api = ToolingApi(settings)
    url = component_attribute["url"] + "/body"
    thread = threading.Thread(target=api.retrieve_body, args=(url, ))
    thread.start()
    ThreadProgress(api, thread, 'Refresh StaticResource', 'Refresh StaticResource Succeed')
    handle_thread(thread, timeout)

def handle_refresh_component(component_attribute, file_name, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        
        result = api.result
        
        # If error, just skip, error is processed in ThreadProgress
        if not result["success"]: return

        fp = open(file_name, "wb")
        try:
            body = bytes(result[component_body], "UTF-8")
        except:
            body = result[component_body].encode("UTF-8")

        fp.write(body)

    settings = context.get_settings()
    api = ToolingApi(settings)
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
        if not result["success"]: return
        os.remove(file_name)
        sublime.active_window().run_command("close")

        # Remove the related cls-meta.xml
        if os.path.exists(file_name+"-meta.xml"):
            os.remove(file_name+"-meta.xml")

    settings = context.get_settings()
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.delete, args=(component_url, ))
    thread.start()
    file_base_name = os.path.basename(file_name)
    ThreadProgress(api, thread, "Deleting " + file_base_name,
        "Delete " + file_base_name + " Succeed")
    handle_thread(thread, timeout)