import sublime
import sublime_plugin
import os
import xml
import urllib
import json
import threading
import time
import pprint
import urllib.parse
import shutil
import datetime
import math

from xml.sax.saxutils import unescape
from . import requests, context, util
from .context import COMPONENT_METADATA_SETTINGS
from .salesforce import soap_bodies, message
from .salesforce.api.bulk import BulkJob
from .salesforce.api.bulk import BulkApi
from .salesforce.api.metadata import MetadataApi
from .salesforce.api.tooling import ToolingApi
from .salesforce.api.apex import ApexApi
from .progress import ThreadProgress, ThreadsProgress
from .salesforce.lib import diff


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

    # Get settings
    settings = context.get_settings()

    # If sobjects is exist in `/.config/session.json`, just return it
    users_path = settings["workspace"]+"/.config/users.json"
    if os.path.isfile(users_path):
        users = json.loads(open(users_path).read())
        return users
        
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

    util.add_config_history("users", json.dumps(users, indent=4))
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

    # Get settings
    settings = context.get_settings()

    # If sobjects is exist in `/.config/recordtype.json`, just return it
    recordtype_path = settings["workspace"]+"/.config/recordtype.json"
    if os.path.isfile(recordtype_path):
        recordtype = json.loads(open(recordtype_path).read())
        return users

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

    util.add_config_history("recordtype", json.dumps(sobject_recordtypes, indent=4))
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

        win = sublime.active_window()
        view = win.create_output_panel('code_coverage')
        view.assign_syntax('Packages/Java/Java.tmLanguage')

        if result["totalSize"] == 0:
            view.run_command('append', {'characters': "No Code Coverage"})
            win.run_command("show_panel", {"panel": "output.code_coverage"})
            return

        # Populate the coverage info from server
        uncovered_lines = result["records"][0]["Coverage"]["uncoveredLines"]
        covered_lines = result["records"][0]["Coverage"]["coveredLines"]
        covered_lines_count = len(covered_lines)
        uncovered_lines_count = len(uncovered_lines)
        total_lines_count = covered_lines_count + uncovered_lines_count
        if total_lines_count == 0:
            view.run_command('append', {'characters': "No Code Coverage"})
            win.run_command("show_panel", {"panel": "output.code_coverage"})
            return
        coverage_percent = covered_lines_count / total_lines_count * 100

        # Append coverage statistic info
        coverage_statistic = message.SEPRATE.format(
            "The coverage percent is %.2f%%(%s/%s), uncovered lines marked as red background" % (
                coverage_percent, covered_lines_count, total_lines_count
            )
        ) + "\n"
        view.run_command('append', {'characters': coverage_statistic})

        # Because the first few lines are occupied by the coverage statistic info
        uncovered_lines = [l+5 for l in uncovered_lines]
        
        # If has coverage, just append body to the output panel
        view.run_command('append', {'characters': body})
        
        # Calculate line coverage
        split_lines = view.lines(sublime.Region(0, view.size()))
        uncovered_region = []
        for region in split_lines:
            # The first four Lines are the coverage info
            line = view.rowcol(region.begin() + 1)[0] + 1
            if line in uncovered_lines:
                uncovered_region.append(region)

        # Append body with uncovered line
        view.add_regions("uncovered_lines", uncovered_region, "invalid", "dot",
            sublime.DRAW_SOLID_UNDERLINE | sublime.DRAW_EMPTY_AS_OVERWRITE)

        # Show output panel
        win.run_command("show_panel", {"panel": "output.code_coverage"})

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
        thread = threading.Thread(target=util.extract_encoded_zipfile, 
            args=(result["zipFile"], extract_to, True, ))
        thread.start()

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
            results.extend(api.result)

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
        sobjects = []
        for sobject in sobjects_describe:
            sobject_describe = sobjects_describe[sobject]
            if sobject in settings["allowed_sobjects"] or sobject_describe["custom"]:
                sobjects.append(sobject)
        
        maximum_concurrent_connections = settings["maximum_concurrent_connections"]
        chunked_sobjects = list(util.chunks(sobjects, math.ceil(len(sobjects) / maximum_concurrent_connections)))

        for sl in chunked_sobjects:
            api = ToolingApi(settings)
            thread = threading.Thread(target=api.describe_sobjects, args=(sl, ))
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

def handle_destructive_files(files, timeout=120):
    def handle_thread(thread, timeout=120):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return

        # After succeed, remove files and related *-meta.xml from local
        if "body" in api.result and api.result["body"]["status"] == "Succeeded":
            win = sublime.active_window()
            for _file in files:
                # Remove file from local disk and close the related view
                view = util.get_view_by_file_name(_file)
                if view: 
                    win.focus_view(view)
                    win.run_command("close")

                os.remove(_file)

                # Remove related *-meta.xml file from local disk and close the related view
                if os.path.isfile(_file+"-meta.xml"):
                    view = util.get_view_by_file_name(_file+"-meta.xml")
                    if view: 
                        win.focus_view(view)
                        win.run_command("close")

                    os.remove(_file+"-meta.xml")

    settings = context.get_settings()
    api = MetadataApi(settings)
    base64_encoded_zip = util.build_destructive_package(files)
    thread = threading.Thread(target=api.deploy, args=(base64_encoded_zip, ))
    thread.start()
    ThreadProgress(api, thread, "Destructing Files", "Destructing Files Succeed")
    handle_thread(thread, timeout)

def handle_deploy_thread(base64_encoded_zip, timeout=120):
    settings = context.get_settings()
    api = MetadataApi(settings)
    thread = threading.Thread(target=api.deploy, args=(base64_encoded_zip, ))
    thread.start()
    ThreadProgress(api, thread, "Deploy Metadata", "Deploy Metadata Succeed")

def handle_cancel_deployment_thread(async_process_id, timeout=120):
    settings = context.get_settings()
    api = MetadataApi(settings)
    thread = threading.Thread(target=api.cancel_deployment, args=(async_process_id, ))
    thread.start()
    ThreadProgress(api, thread, "Canceling Deployment", "Canceling Deployment Succeed")

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

        # Extract the zipFile to extract_to
        thread = threading.Thread(target=util.extract_encoded_zipfile, 
            args=(result["zipFile"], outputdir, ))
        thread.start()

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
        time_stamp = time.strftime("%H:%M:%S", time.localtime(time.time()))
        view.run_command("new_view", {
            "name": "Rest %s-%s" % (operation, time_stamp), 
            "input": json.dumps(result, indent=4)
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
            "input": json.dumps(result, indent=4)
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

        if result["compiled"] == "false":
            util.show_output_panel(util.parse_execute_anonymous_xml(result))
        else:
            # No error, just display log in a new view
            view = sublime.active_window().new_file()
            view.run_command("new_view", {
                "name": "Execute Anonymous Result",
                "input": util.parse_execute_anonymous_xml(result)
            })

        # Keep the history apex script to local
        util.add_operation_history('execute_anonymous', apex_string)

    settings = context.get_settings()
    api = ApexApi(settings)
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
        util.show_output_panel(debug_logs_table)

    settings = context.get_settings()
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.query_logs, args=(settings["last_n_logs"], user_id, ))
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
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return

    pass

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
        print (result)
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
        thread = threading.Thread(target=util.extract_encoded_zipfile, 
            args=(result["zipFile"], extract_to, ))
        thread.start()

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

            util.add_config_history('settings', json.dumps(settings, indent=4))
            util.add_config_history('session', json.dumps(api.session, indent=4))

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
        result = api.result

        # Extract the zipFile to extract_to
        thread = threading.Thread(target=util.extract_encoded_zipfile, 
            args=(result["zipFile"], extract_to, ignore_package_xml, ))
        thread.start()

    # Start to request
    settings = context.get_settings()
    api = MetadataApi(settings)
    try:
        types = util.parse_package(package_xml_content)
    except xml.parsers.expat.ExpatError as err:
        sublime.error_message("XML Parse Error: "+str(err))
        return
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
        if "success" in result and result["success"]:
            # 1. Write succeed body to local change history
            if settings["keep_local_change_history"] and not is_check_only:
                # Append message to output panel
                util.append_message(panel, "Start to keep local change history")

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
                # Append message to output panel
                util.append_message(panel, "Start to write symbol table to local cache")

                # Start to write
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
            save_or_compile = "Compiled" if is_check_only else "Saved"
            util.append_message(panel, "%s %s successfully" % (save_or_compile, file_base_name))

            # Add total seconds message
            total_seconds = (datetime.datetime.now() - start_time).seconds
            util.append_message(panel, "\nTotal time: %s seconds" % total_seconds, False)

            # Remove highlight
            view = sublime.active_window().active_view()
            component_id = component_attribute["id"]
            view.run_command("remove_check_point", {"mark":component_id+"build_error"})

            # If succeed, just hide it in two seconds later
            delay_seconds = settings["delay_seconds_for_hidden_output_panel_when_succeed"]
            sublime.set_timeout_async(util.hide_output_panel, delay_seconds * 1000)

        # If not succeed, just go to the error line
        # Because error line in page is always at the line 1, so just work in class or trigger
        elif "success" in result and not result["success"]:
            view = sublime.active_window().active_view()
            if file_base_name in view.file_name() and extension in [".trigger", ".cls", ".page"]:
                if "line" in result:
                    line = result["line"]
                elif "lineNumber" in result:
                    line = result["lineNumber"]
                else:
                    return
                    
                if isinstance(line, list): line = line[0]
                if extension == ".page" and line < 2: return
                view.run_command("goto_line", {"line": line})
                view.run_command("expand_selection", {"to":"line"})

                # Add highlight for error line and remove the highlight after several seconds
                component_id = component_attribute["id"]
                view.run_command("set_check_point", {"mark":component_id+"build_error"})

    # Component Full Name
    extension = component_attribute["extension"]
    file_base_name =  component_name + extension

    # Log start_time
    start_time = datetime.datetime.now()

    # If saving is in process, just skip
    settings = context.get_settings()
    username = settings["username"]
    if username + component_name in globals():
        is_thread_alive = globals()[username + component_name]
        if is_thread_alive:
            print ('%s is in process' % component_name);
            return

    # Open panel
    panel = sublime.active_window().create_output_panel('log')  # Create panel
    compile_or_save = "compile" if is_check_only else "save"
    util.append_message(panel, "Start to %s %s" % (compile_or_save, file_base_name))

    api = ToolingApi(settings)
    thread = threading.Thread(target=api.save_component,
        args=(panel, component_attribute, body, is_check_only, ))
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

def handle_diff_with_server(component_attribute, file_name, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        
        result = api.result
        
        # If error, just skip, error is processed in ThreadProgress
        if not result["success"]: return

        # Diff Change Compare
        diff.diff_changes(file_name, result)

    settings = context.get_settings()
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.get, args=(component_attribute["url"], ))
    thread.start()
    handle_thread(thread, timeout)
    ThreadProgress(api, thread, 'Diff With Server', 'Diff With Server Succeed')

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

        # Get active window
        window = sublime.active_window()

        # Remove file from disk and close related view
        view = util.get_view_by_file_name(file_name)
        if view:
            window.focus_view(view)
            window.run_command("close")
        os.remove(file_name)

        # Remove the related cls-meta.xml
        if os.path.exists(file_name+"-meta.xml"):
            view = util.get_view_by_file_name(file_name+"-meta.xml")
            if view:
                window.focus_view(view)
                window.run_command("close")
            os.remove(file_name+"-meta.xml")

    settings = context.get_settings()
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.delete, args=(component_url, ))
    thread.start()
    file_base_name = os.path.basename(file_name)
    ThreadProgress(api, thread, "Deleting " + file_base_name,
        "Delete " + file_base_name + " Succeed")
    handle_thread(thread, timeout)