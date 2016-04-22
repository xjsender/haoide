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
from .salesforce import soap, message, login
from .salesforce.login import soap_login
from .salesforce.api.bulk import BulkJob
from .salesforce.api.bulk import BulkApi
from .salesforce.api.metadata import MetadataApi
from .salesforce.api.tooling import ToolingApi
from .salesforce.api.apex import ApexApi
from .salesforce.lib.panel import Printer
from .progress import ThreadProgress, ThreadsProgress
from .salesforce.lib import diff


def handle_populate_users(callback_command, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        
        if api.result or api.result["success"]:
            records = api.result["records"]
            users = {}
            for record in records:
                if not record["FirstName"]:
                    name = "%s => %s" % (record["LastName"], record["Username"])
                else:
                    name = "%s => %s" % (
                        "%s %s" % (record["LastName"], record["FirstName"]), 
                        record["Username"]
                    )

                users[name] = record["Id"]

            util.add_config_history("users", users, settings)
            sublime.active_window().run_command(callback_command)

    # If sobjects is exist in `/.config/users.json`, just return it
    settings = context.get_settings()
    user_cache = os.path.join(settings["workspace"], ".config", "users.json")
    if os.path.isfile(user_cache): return json.loads(open(user_cache).read())

    # If not exist, we need to use callback function
    api = ToolingApi(settings)
    query = "SELECT Id, FirstName, LastName, Username FROM User WHERE IsActive = true"
    thread = threading.Thread(target=api.query_all, args=(query, ))
    thread.start()
    handle_thread(thread, timeout)
    ThreadProgress(api, thread, "Downloading Users List", "Succeed to download users list")

def populate_sobject_recordtypes():
    """
    Get dict ([sobject, recordtype name] => recordtype id) in whole org

    @return: {
        username ,  "sobject_recordtypes": {
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
        return recordtype

    # If sobjects is not exist in globals(), post request to pouplate it
    api = ToolingApi(settings)
    query = "SELECT Id, Name, SobjectType FROM RecordType"
    thread = threading.Thread(target=api.query_all, args=(query, ))
    thread.start()

    while thread.is_alive() or not api.result:
        time.sleep(1)

    # Exception Process
    if not api.result["success"]:
        Printer.get('error').write(message.SEPRATE.format(util.format_error_message(api.result)))
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

    util.add_config_history("recordtype", sobject_recordtypes, settings)
    return sobject_recordtypes

def handle_update_user_language(language, timeout=120):
    settings = context.get_settings()
    api = ToolingApi(settings)
    session = util.get_session_info(settings)
    if not session:
        return Printer.get('error').write("Login is required before this action")

    patch_url = "/sobjects/User/%s" % session["user_id"]
    thread = threading.Thread(target=api.patch, 
        args=(patch_url, {"LanguageLocaleKey": language}, ))
    thread.start()
    ThreadProgress(api, thread, "Updating User Language to " + language,  
        "User language is updated to " + language)

def handle_enable_development_mode(user_id, timeout=120):
    settings = context.get_settings()
    api = ToolingApi(settings)

    patch_url = "/sobjects/User/%s" % user_id
    thread = threading.Thread(target=api.patch, 
        args=(patch_url, {"UserPreferencesApexPagesDeveloperMode": True}, ))
    thread.start()
    ThreadProgress(api, thread, "Enabling User Development Mode",
        "Succeed to Enabling User Development Mode")

def handle_update_user_password(user_id, new_password, timeout=120):
    settings = context.get_settings()
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.manage_password, args=(
        user_id, {"NewPassword": new_password}, 
    ))
    thread.start()
    masked_password = new_password[:5] + "*" * len(new_password[3:])
    ThreadProgress(api, thread, "Updating User Password to " + masked_password,  
        "Succeed to update user password to " + masked_password)

def handle_login_thread(callback_options={}, force=False, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return

        result = api.result
        if result and result["success"]:
            if "callback_command" in callback_options:
                callback_command = callback_options["callback_command"]
                args = callback_options["args"] if "args" in callback_options else {}
                sublime.active_window().run_command(callback_command, args)

    settings = context.get_settings()
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.login, args=(force, ))
    thread.start()
    handle_thread(thread, timeout)

    default_project_name = settings["default_project_name"]
    ThreadProgress(api, thread, "Login to %s" % default_project_name, 
        default_project_name + " Login Succeed")

def handle_view_code_coverage(component_name, component_id, body, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return

        result = api.result
        if not result["success"]: 
            return

        if result["totalSize"] == 0:
            Printer.get("log").write("There is no available code coverage")
            return

        # Populate the coverage info from server
        uncovered_lines = result["records"][0]["Coverage"]["uncoveredLines"]
        covered_lines = result["records"][0]["Coverage"]["coveredLines"]
        covered_lines_count = len(covered_lines)
        uncovered_lines_count = len(uncovered_lines)
        total_lines_count = covered_lines_count + uncovered_lines_count
        if total_lines_count == 0:
            Printer.get("log").write("There is no available code coverage")
            return
        coverage_percent = covered_lines_count / total_lines_count * 100

        # Append coverage statistic info
        coverage_statistic = "%s Coverage: %.2f%%(%s/%s)" % (
            component_name, coverage_percent, 
            covered_lines_count, total_lines_count
        )
        
        # If has coverage, just add coverage info to new view
        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": coverage_statistic,
            "input": body
        })
        
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

    settings = context.get_settings()
    api = ToolingApi(settings)
    query = "SELECT Coverage FROM ApexCodeCoverageAggregate " +\
        "WHERE ApexClassOrTriggerId = '{0}'".format(component_id)
    thread = threading.Thread(target=api.query, args=(query, True, ))
    thread.start()
    ThreadProgress(api, thread, "View Code Coverage of " + component_name,
        "View Code Coverage of " + component_name + " Succeed")
    handle_thread(thread, timeout)

def handle_refresh_folder(types, ignore_package_xml=True, timeout=120):
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
            args=(result["zipFile"], extract_to, ignore_package_xml, ))
        thread.start()

        util.reload_file_attributes(result["fileProperties"], settings)

        # Hide panel 0.5 seconds later
        sublime.set_timeout_async(Printer.get("log").hide_panel, 500)

    # Start to request
    settings = context.get_settings()
    api = MetadataApi(settings)
    thread = threading.Thread(target=api.retrieve, args=({"types": types}, ))
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
    thread = threading.Thread(target=api.query_symbol_table, args=(30, ))
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
        for sobject_describe in results:
            # Initiate Sobject completions
            if "name" not in sobject_describe: 
                continue
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
                referenceTo = f["referenceTo"] if "referenceTo" in f else []

                if f["calculatedFormula"]:
                    capitalize_field = field_type.capitalize()
                    field_desc_dict = {
                        "double": "Formula(%s, %s, %s)" % (capitalize_field, precision, scale),
                        "currency": "Formula(%s, %s, %s)" % (capitalize_field, precision, scale),
                        "date": "Formula(Date)",
                        "datetime": "Formula(Datetime)",
                        "boolean": "Formula(Boolean)",
                        "int": "Formula(Integer)",
                        "reference": ("Reference(%s)" % ",".join(referenceTo)) if referenceTo else "Reference",
                        "other": "Formula(%s, %s)" % (capitalize_field, f["length"])
                    }
                else:
                    field_desc_dict = {
                        "double": "Double(%s, %s)" % (precision, scale),
                        "currency": "Currency(%s, %s)" % (precision, scale),
                        "date": "Date",
                        "datetime": "Datetime",
                        "boolean": "Boolean",
                        "reference": ("Reference(%s)" % ",".join(referenceTo)) if referenceTo else "Reference",
                        "int": "Integer",
                        "other": "%s(%s)" % (field_type.capitalize(), f["length"])
                    }

                # External Or not
                externalUniqueNotation = ""
                if f["externalId"] or f["unique"]:
                    externalUniqueNotation = "[%s%s%s] " % (
                        "E" if f["externalId"] else "",
                        "U" if f["unique"] else "",
                        "R" if not f["nillable"] else ""
                    )

                # If display_field_name_and_label setting is true, 
                # display both field name and field label
                field_name_desc = "%s(%s)" % (field_name, f["label"]) \
                    if settings["display_field_name_and_label"] else field_name

                # Display field type with specified format
                field_type_desc = field_desc_dict[field_type] if field_type \
                    in field_desc_dict else field_desc_dict["other"]

                fd = "%s%s\t%s" % (externalUniqueNotation, field_name_desc, field_type_desc)
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

        # Reload cache for completions
        from . import completions
        completions.reload_globals(username)

    def handle_thread(api, thread, timeout=120):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(api, thread, timeout), timeout)
            return

        # Exception Process
        if not api.result or not api.result["success"]: 
            return

        # Get describe result of all sObjects
        sobjects_describe = api.result["sobjects"]
        sobjects = list(sobjects_describe.keys())
        
        mcc = settings["maximum_concurrent_connections"]
        chunked_sobjects = util.list_chunks(sobjects, math.ceil(len(sobjects) / mcc))

        threads = []
        apis = []
        for sobjects in chunked_sobjects:
            api = ToolingApi(settings)
            thread = threading.Thread(target=api.describe_sobjects, args=(sobjects, ))
            thread.start()
            threads.append(thread)
            apis.append(api)

        ThreadsProgress(threads, "Download Cache of Sobjects", "Download Cache of Sobjects Succeed")
        handle_threads(apis, threads, 10)

    settings = context.get_settings()
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.get_sobjects, args=())
    thread.start()
    ThreadProgress(api, thread, "Global Describe", "Global Describe Succeed")
    handle_thread(api, thread, timeout)

def handle_destructive_files(dirs_or_files, ignore_folder=True, timeout=120):
    def handle_thread(thread, timeout=120):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return

        # After succeed, remove dirs_or_files and related *-meta.xml from local
        if "body" in api.result and api.result["body"]["status"] == "Succeeded":
            win = sublime.active_window()
            for _file_or_dir in dirs_or_files:
                # Remove file from local disk and close the related view
                view = util.get_view_by_file_name(_file_or_dir)
                if view: 
                    win.focus_view(view)
                    win.run_command("close")

                if os.path.isfile(_file_or_dir):
                    os.remove(_file_or_dir)
                else:
                    shutil.rmtree(_file_or_dir)

                # Remove related *-meta.xml file from local disk and close the related view
                if ignore_folder and os.path.isfile(_file_or_dir+"-meta.xml"):
                    view = util.get_view_by_file_name(_file_or_dir+"-meta.xml")
                    if view: 
                        win.focus_view(view)
                        win.run_command("close")

                    os.remove(_file_or_dir+"-meta.xml")

    settings = context.get_settings()
    api = MetadataApi(settings)
    base64_encoded_zip = util.build_destructive_package_by_files(dirs_or_files, ignore_folder)
    thread = threading.Thread(target=api.deploy, args=(base64_encoded_zip, ))
    thread.start()
    ThreadProgress(api, thread, "Destructing Files", "Destructing Files Succeed")
    handle_thread(thread, timeout)

def handle_destructive_package_xml(types, timeout=120):
    def handle_thread(thread, timeout=120):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return

    settings = context.get_settings()
    api = MetadataApi(settings)
    base64_encoded_zip = util.build_destructive_package_by_package_xml(types)
    thread = threading.Thread(target=api.deploy, args=(base64_encoded_zip, ))
    thread.start()
    ThreadProgress(api, thread, "Destructing Package.xml", "Destructing Package.xml Succeed")
    handle_thread(thread, timeout)

def handle_deploy_thread(base64_encoded_zip, 
        source_org=None, chosen_classes=[], timeout=120):
    def handle_thread(thread, timeout=120):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return

        # If source_org is not None, we need to switch project back
        if settings["switch_back_after_migration"] and source_org:
            util.switch_project(source_org)

    settings = context.get_settings()
    api = MetadataApi(settings)
    thread = threading.Thread(target=api.deploy, args=(
        base64_encoded_zip, 
        chosen_classes, 
    ))
    thread.start()
    ThreadProgress(api, thread, "Deploy Metadata to %s" % settings["default_project_name"], 
        "Metadata Deployment Finished")
    handle_thread(thread, timeout)

def handle_track_all_debug_logs_thread(users, timeout=120):
    settings = context.get_settings()
    api = ToolingApi(settings)

    # Divide users into pieces of dict
    pieces = []
    maximum_concurrent_connections = settings["maximum_concurrent_connections"]
    split = math.ceil(len(users) / maximum_concurrent_connections)
    for item in util.dict_chunks(users, split):
        pieces.append(item)
    
    threads = []
    for users in pieces:
        api = ToolingApi(settings)
        thread = threading.Thread(target=api.create_trace_flags, args=(users, ))
        thread.start()
        threads.append(thread)

    ThreadsProgress(threads, "Creating Trace Flags", "Creating Trace Flags Finished")

def handle_cancel_deployment_thread(async_process_id, timeout=120):
    settings = context.get_settings()
    api = MetadataApi(settings)
    thread = threading.Thread(target=api._invoke_method, args=(
        "cancelDeploy", {
            "async_process_id": async_process_id, 
        }
    ))
    thread.start()
    ThreadProgress(api, thread, "Canceling Deploy", "Canceling Deploy Succeed")

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
        
        threads = []
        for sobject_describe in api.result["sobjects"]:
            if "name" not in sobject_describe: continue
            bulkapi = BulkApi(settings, sobject_describe["name"])
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

def handle_export_workflows(settings, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        
        # If succeed
        sObjects = []
        for sd in api.result["sobjects"]:
            if "name" not in sd: continue
            sObjects.append(sd["name"])

        util.parse_workflow_metadata(settings, sObjects)
        sublime.active_window().run_command("refresh_folder_list")

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
        sObjects = []
        for sd in api.result["sobjects"]:
            if "name" not in sd: continue
            sObjects.append(sd["name"])

        util.parse_validation_rule(settings, sObjects)
        sublime.active_window().run_command("refresh_folder_list")

    api = ToolingApi(settings)
    thread = threading.Thread(target=api.describe_global, args=())
    thread.start()
    ThreadProgress(api, thread, "Export All Validation Rules", "Validation Rules Export Succeed")
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
        outputdir = os.path.join(settings["workspace"], ".export")
        if not os.path.exists(outputdir): os.makedirs(outputdir)
        records = sorted(result["records"], key=lambda k : k['TableEnumOrId'])
        outputfile = os.path.join(outputdir, "CustomField.csv")
        util.list2csv(outputfile, records)

        # Open the csv file
        view = sublime.active_window().open_file(outputfile)

    settings = context.get_settings()
    api = ToolingApi(settings)
    query = "SELECT Id,TableEnumOrId,DeveloperName,NamespacePrefix FROM CustomField"
    thread = threading.Thread(target=api.query, args=(query, True,))
    thread.start()
    ThreadProgress(api, thread, 'Exporting CustomFields', "Exporting CustomFields Succeed")
    handle_thread(thread, 10)

def handle_export_role_hierarchy(timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        
        # If succeed
        result = api.result
        if not result or not result["success"]: return

        records = result["records"]
        outputfile = util.export_role_hierarchy(records)
        sublime.active_window().run_command("refresh_folder_list")

        # Open file
        view = sublime.active_window().open_file(outputfile)

    settings = context.get_settings()
    api = ToolingApi(settings)
    soql = "SELECT Id, ParentRoleId, Name, " +\
        "(SELECT Id, FirstName, LastName, Username FROM Users " +\
        " WHERE IsActive = true AND Profile.UserLicense.Name = 'Salesforce') " +\
        "FROM UserRole WHERE PortalType = 'None'"
    thread = threading.Thread(target=api.query_all, args=(soql,))
    thread.start()
    ThreadProgress(api, thread, 'Exporting Role Hierarchy', "Role Hierarchy Exporting Succeed")
    handle_thread(thread, 10)

def handle_export_data_template_thread(sobject, recordtype_name, recordtype_id, vertical, timeout=120):
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
        if vertical:
            util.parse_data_template_vertical(output_file_dir, result)
        else:
            util.parse_data_template_horizontal(output_file_dir, result)
        sublime.active_window().run_command("refresh_folder_list")
        Printer.get("log").write("Data Template for %s: %s" % (sobject, output_file_dir))

    settings = context.get_settings()
    outputdir = settings["workspace"] + "/.export/layoutWorkbooks"
    output_file_dir = "%s/%s-%s.csv" % (
        outputdir, sobject, recordtype_name
    )
    api = ToolingApi(settings)
    url = "/sobjects/%s/describe/layouts/%s" % (sobject, recordtype_id)
    thread = threading.Thread(target=api.get, args=(url, ))
    thread.start()
    wait_message = "Export Data Template of %s=>%s" % (sobject, recordtype_name)
    ThreadProgress(api, thread, wait_message, "Outputdir: " + output_file_dir)
    handle_thread(thread, 120)

def handle_export_query_to_csv(tooling, soql, csv_name, data=None, timeout=120):
    def handle_new_view_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_new_view_thread(thread, timeout), timeout)
            return
        
        result = api.result
        if "success" in result and not result["success"]:
            return

        outputdir = os.path.join(settings["workspace"], ".export", "Query2CSV")
        if not os.path.exists(outputdir): os.makedirs(outputdir)
        time_stamp = time.strftime("%Y-%m-%d-%H-%M", time.localtime())
        outputfile = os.path.join(outputdir, "%s.csv" % csv_name)
        with open(outputfile, "wb") as fp:
            fp.write(util.query_to_csv(result, soql))
            
        view = sublime.active_window().open_file(outputfile)

    settings = context.get_settings()
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.query_all, args=(soql, tooling, ))
    thread.start()
    progress_message = "Export Query To %s.csv" % csv_name
    ThreadProgress(api, thread, progress_message, progress_message + " Succeed")
    handle_new_view_thread(thread, timeout)

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
        if settings.get("remove_slash_for_rest_response", False):
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
        view.set_syntax_file("Packages/JavaScript/JSON.tmLanguage")
        time_stamp = time.strftime("%H:%M:%S", time.localtime(time.time()))
        view.run_command("new_view", {
            "name": "Rest %s-%s" % (operation, time_stamp), 
            "input": json.dumps(result, ensure_ascii=False, indent=4)
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
    ThreadProgress(api, thread, progress_message, progress_message + " Succeed", show_error=False)
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
            Printer.get('error').write(util.parse_execute_anonymous_xml(result))
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
        if not result or "records" not in result: 
            return

        records = result["records"]
        debug_logs_table = util.format_debug_logs(settings, records)
        Printer.get("log").write_start().write(debug_logs_table)

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
        print (result)

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

def handle_run_test(class_name, class_id, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return

        # If succeed
        result = api.result

        # If error
        if "success" in result and not result["success"]: return

        if not result:
            return Printer.get("error").write("%s is not a test class" % class_name)

        # No error, just display log in a new view
        test_result = util.parse_test_result(result)
        view = sublime.active_window().new_file()
        view.settings().set("word_wrap", "false")
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

        # If error, just skip
        result = api.result
        if "success" in result and not result["success"]: return

        code_coverage = util.parse_code_coverage(result)
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

def handle_run_sync_test(class_names, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return

        # If succeed
        result = api.result
        print (result)
        if "success" in result and not result["success"]:
            return

        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": "Sync Test Coverage Report",
            "input": util.parse_sync_test_coverage(result)
        })

        if settings["debug_mode"]:
            view = sublime.active_window().new_file()
            view.run_command("new_view", {
                "name": "Sync Test Raw Response",
                "input": json.dumps(result, indent=4)
            })

        # Keep the coverage to local cache
        codeCoverages = result["codeCoverage"]
        cache_dir = os.path.join(settings["workspace"], ".config")
        cache_file = os.path.join(cache_dir, "coverage.json")

        coverages = {}
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
        elif os.path.isfile(cache_file):
            coverages = json.loads(open(cache_file).read())

        # Upsert exist code coverage info
        for codeCoverage in codeCoverages:
            lowerName = codeCoverage["name"].lower()
            coverages[lowerName] = codeCoverage

        with open(cache_file, "w") as fp:
            fp.write(json.dumps(coverages, indent=4))

    settings = context.get_settings()
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.run_tests_synchronous, args=(class_names, ))
    thread.start()
    wait_message = "Running Sync Test Classes%s" % (
        " for %s" % class_names[0] if len(class_names) == 1 else ""
    )
    ThreadProgress(api, thread, wait_message, wait_message + " Succeed")
    handle_thread(thread, timeout)

def handle_generate_sobject_soql(sobject, filter, timeout=120):
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
    if filter != "all":
        args = (sobject, filter, )
    else:
        args = (sobject, )
    thread = threading.Thread(target=api.combine_soql, args=args)
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
        view.settings().set("word_wrap", False)
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

    mcc = settings["maximum_concurrent_connections"]
    chunked_sobjects = util.list_chunks(sobjects, math.ceil(len(sobjects) / mcc))

    for cs in chunked_sobjects:
        thread = threading.Thread(target=api.generate_workbook, args=(cs, ))
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
        sobjects = []
        for sd in api.result["sobjects"]:
            if "name" not in sd: continue
            sobjects.append(sd["name"])

        mcc = settings["maximum_concurrent_connections"]
        chunked_sobjects = util.list_chunks(sobjects, math.ceil(len(sobjects) / mcc))

        for sobjects in chunked_sobjects:
            thread = threading.Thread(target=api.generate_workbook, args=(sobjects, ))
            thread.start()

    settings = context.get_settings()
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.describe_global, args=())
    thread.start()
    ThreadProgress(api, thread, "Describe Global", "Describe Global Succeed")
    handle_thread(thread, timeout)

def handle_new_project(is_update=False, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        
        # If failed, but something may happen,
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
        for metadata_folder in settings["subscribed_metadata_folders"]:
            outputdir = os.path.join(extract_to, "src", metadata_folder);
            if not os.path.exists(outputdir): os.makedirs(outputdir)

        # Extract the zipFile to extract_to
        thread = threading.Thread(target=util.extract_encoded_zipfile, 
            args=(result["zipFile"], extract_to, ))
        thread.start()

        # Apex Code Cache
        if "fileProperties" in result and isinstance(result["fileProperties"], list):
            util.reload_file_attributes(result["fileProperties"], settings)
        else:
            if settings["debug_mode"]:
                print ('[Debug] fileProperties:\n' + json.dumps(result, indent=4))

        # Hide panel
        sublime.set_timeout_async(Printer.get("log").hide_panel, 500)

        # Reload sObject Cache and SymbolTables
        if not is_update: 
            handle_reload_sobjects_completions()
            
            if settings["reload_symbol_tables_when_create_project"]:
                handle_reload_symbol_tables()

        # Write the settings to local cache
        # Not keep the confidential info to .settings
        # Since 2015.11.26, stop to keep settings.json
        # del settings["projects"]
        # del settings["password"]
        # del settings["default_project"]
        # util.add_config_history('settings', settings, settings)

    settings = context.get_settings()
    api = MetadataApi(settings)
    types = {}
    for xml_name in settings["subscribed_metadata_objects"]:
        types[xml_name] = ["*"]

    thread = threading.Thread(target=api.retrieve, args=({
        "types": types,
        "package_names": settings["allowed_packages"]
    }, ))
    thread.start()
    wating_message = ("Creating New " if not is_update else "Updating ") + " Project"
    ThreadProgress(api, thread, wating_message, wating_message + " Finished")
    handle_thread(thread, timeout)

def handle_describe_metadata(callback_options, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return

        # Exception is processed in ThreadProgress
        if not api.result or not api.result["success"]: return
        result = api.result
        del result["success"]

        settings = context.get_settings()
        cache_dir = os.path.join(settings["workspace"], ".config")
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
        cache_file = os.path.join(cache_dir, "metadata.json")
        with open(cache_file, "w") as fp:
            fp.write(json.dumps(result, indent=4))

        if "callback_command" in callback_options:
            settings = context.get_settings()
            callback_command = callback_options["callback_command"]
            args = callback_options["args"] if "args" in callback_options else {}

            # If project already have subscribed_metadata_objects, just stop
            if "subscribed_metadata_objects" in settings["default_project"] and \
                    settings["default_project"]["subscribed_metadata_objects"]:
                return sublime.active_window().run_command(callback_command, args)

            # If project doesn't have subscribed_metadata_objects, we need
            # to choose which metadata_objects to subscribe, which will be saved
            # into default project
            sublime.active_window().run_command("toggle_metadata_objects", {
                "callback_options": callback_options
            })

    # Start to request
    settings = context.get_settings()
    api = MetadataApi(settings)
    thread = threading.Thread(target=api._invoke_method, args=("describeMetadata", ))
    thread.start()
    handle_thread(thread, timeout)
    ThreadProgress(api, thread, "Describe Metadata of v%s.0" % settings["api_version"], 
        "Describe Metadata Finished")

def handle_rename_metadata(file_name, meta_type, old_name, new_name, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        
        # If not succeed, just stop
        if not api.result or not api.result["success"]: return
        result = api.result

        if "errors" in result:
            return Printer.get("error").write(result["errors"]["message"])

        os.rename(file_name, file_name.replace(old_name, new_name))

    # Start to request
    settings = context.get_settings()
    api = MetadataApi(settings)
    options = {"type": meta_type, "old_name": old_name, "new_name": new_name}
    thread = threading.Thread(target=api._invoke_method, args=("renameMetadata", options, ))
    thread.start()
    handle_thread(thread, timeout)
    message = "Renaming %s from %s to %s" % (
        meta_type, old_name, new_name
    )
    ThreadProgress(api, thread, message, "Renaming Finished")

def handle_reload_project_cache(types, callback_command, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return

        if not api.result or not api.result["success"]: return

        types = api.result["types"]
        cache_dir = os.path.join(settings["workspace"], ".config")
        cache_file = os.path.join(cache_dir, "package.json")

        cache = types
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
        elif os.path.isfile(cache_file):
            cache = json.loads(open(cache_file).read())
            for _type in types:
                cache[_type] = types[_type]

        with open(cache_file, "w") as fp:
            fp.write(json.dumps(cache, indent=4))

        if callback_command:
            sublime.active_window().run_command(callback_command)

    # Start to request
    settings = context.get_settings()
    api = MetadataApi(settings)
    thread = threading.Thread(target=api.prepare_members, args=(types, True, ))
    thread.start()
    handle_thread(thread, timeout)
    ThreadProgress(api, thread, "Reloading Project Cache", "Reload Project Cache Succeed")

def handle_retrieve_package(types, extract_to, source_org=None, ignore_package_xml=False, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        
        # If source_org is not None, we need to switch project back
        if settings["switch_back_after_migration"] and source_org:
            util.switch_project(source_org)
        
        # Extract the zipFile to extract_to
        if api.result and api.result["success"]:
            thread = threading.Thread(target=util.extract_encoded_zipfile, 
                args=(api.result["zipFile"], extract_to, ignore_package_xml, ))
            thread.start()

            # Apex Code Cache
            if isinstance(api.result.get("fileProperties", None), list):
                util.reload_file_attributes(
                    api.result["fileProperties"], 
                    settings, append=True
                )

    # Start to request
    settings = context.get_settings()
    api = MetadataApi(settings)
    thread = threading.Thread(target=api.retrieve, args=({"types": types}, ))
    thread.start()
    handle_thread(thread, timeout)
    ThreadProgress(api, thread, "Retrieve File From Server", 
        "Retrieve File From Server Succeed")

def handle_save_to_server(file_name, is_check_only=False, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return

        # Set Thread alive flag to False
        globals()[username + file_base_name] = False

        # Process request result
        result = api.result

        # If cancel, just diff with server
        if "Operation" in result and result["Operation"] == "cancel":
            handle_diff_with_server(component_attribute, file_name)
            return

        if "success" in result and result["success"]:
            # 1. Write succeed body to local change history
            if settings["keep_local_change_history"] and not is_check_only:
                # Append message to output panel
                Printer.get('log').write("Start to keep local change history")

                # Get Workspace, if not exist, make it
                workspace = settings["workspace"]+"/.history/"+component_attribute["type"]
                if not os.path.exists(workspace):
                    os.makedirs(workspace)

                # Backup current file
                time_stamp = time.strftime("%Y-%m-%d-%H-%M", time.localtime())
                outputdir = workspace+"/"+component_name+"-"+time_stamp+"-history"+extension
                with open(outputdir, "wb") as fp:
                    fp.write(body.encode("utf-8"))

            # Output succeed message in the console
            save_or_compile = "Compiled" if is_check_only else "Saved"
            Printer.get('log').write("%s %s successfully" % (save_or_compile, file_base_name))

            # Add total seconds message
            total_seconds = (datetime.datetime.now() - start_time).seconds
            Printer.get('log').write("\nTotal time: %s seconds" % total_seconds, False)

            # Remove highlight
            view = util.get_view_by_file_name(file_name)
            if view:
                component_id = component_attribute["id"]
                view.run_command("remove_check_point", {"mark":component_id+"build_error"})

            # If succeed, just hide it in several seconds later
            delay_seconds = settings["delay_seconds_for_hidden_output_panel_when_succeed"]
            sublime.set_timeout_async(Printer.get("log").hide_panel, delay_seconds * 1000)

            # If track_log_after_saved is true, track self debug log asynchronously
            if settings["track_log_after_saved"]:
                thread = threading.Thread(target=api.create_trace_flag)
                thread.start()

            # After all are finished, keep the LastModifiedDate
            handle_set_component_attribute(component_attribute)

        # If not succeed, just go to the error line
        # Because error line in page is always at the line 1, so just work in class or trigger
        elif "success" in result and not result["success"]:
            # Maybe network issue
            if "problem" not in result: return

            message = "Compile Error for %s: %s at line %s column %s" % (
                file_base_name, 
                result["problem"], 
                result["lineNumber"],
                result["columnNumber"]
            )
            Printer.get('log').write(message)

            # Get the active view
            view = util.get_view_by_file_name(file_name)

            # Check current view the saving code file
            if not view or not view.file_name(): return
            if not file_base_name in view.file_name(): return
            if not extension in [".trigger", ".cls", ".page"]: return

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

            if hasattr(view, 'show_popup'):
                error = """
                    <div>
                        <h3>Compile Error for %s</h3>
                        <p style="color: red">
                            <b>%s</b> at line <b>%s</b> column <b>%s</b>
                        </p>
                    </div>
                """ % (
                    file_base_name, 
                    result["problem"], 
                    result["lineNumber"],
                    result["columnNumber"]
                )
                view.show_popup(error)

            # Add highlight for error line and remove the highlight after several seconds
            component_id = component_attribute["id"]
            view.run_command("set_check_point", {"mark":component_id+"build_error"})

    component_attribute, component_name = util.get_component_attribute(file_name)
    body = open(file_name, encoding="utf-8").read()

    # Component Full Name
    extension = component_attribute["extension"]
    file_base_name =  component_name + extension

    # Log start_time
    start_time = datetime.datetime.now()

    # If saving is in process, just skip
    settings = context.get_settings()
    username = settings["username"]
    if username + file_base_name in globals():
        is_thread_alive = globals()[username + file_base_name]
        if is_thread_alive:
            print ('%s is in process' % file_base_name);
            return

    # Open panel
    compile_or_save = "compile" if is_check_only else "save"
    Printer.get('log').write_start().write("Start to %s %s" % (compile_or_save, file_base_name))

    api = ToolingApi(settings)
    thread = threading.Thread(target=api.save_to_server,
        args=(component_attribute, body, is_check_only, ))
    thread.start()

    # If saving thread is started, set the flag to True
    globals()[username + file_base_name] = True

    # Display thread progress
    wait_message = ("Compiling " if is_check_only else "Saving ") + component_name
    ThreadProgress(api, thread, wait_message, wait_message + " Succeed", show_error=False)
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
        extension = "." + settings[component_type]["suffix"]
        
        # Save it to component.sublime-settings
        s = sublime.load_settings(COMPONENT_METADATA_SETTINGS)
        username = settings["username"]
        components_dict = s.get(username, {})

        # Prevent exception for creating component if no component in org
        if component_type not in components_dict: 
            components_dict = {component_type : {}}

        # Build components dict
        lower_name = component_name.lower()
        attributes = {
            "id": component_id,
            "name": component_name,
            "url": post_url + "/" + component_id,
            "body": markup_or_body,
            "extension": extension,
            "type": component_type,
            "is_test": lower_name.startswith("test") or lower_name.endswith("test")
        }
        components_dict[component_type][fullName.lower()] = attributes
        s.set(username, components_dict)

        # Save settings and show success message
        sublime.save_settings(COMPONENT_METADATA_SETTINGS)

        # Create Meta.xml File
        if component_type in ["ApexClass", "ApexTrigger"]:
            meta_file_content = ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" +\
                "<{0} xmlns=\"http://soap.sforce.com/2006/04/metadata\">\n" +\
                "    <apiVersion>{1}.0</apiVersion>\n" +\
                "    <status>Active</status>\n" +\
                "</{0}>").format(component_type, settings["api_version"])

        elif component_type in ["ApexPage", "ApexComponent"]:
            meta_file_content = ("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" +\
                "<{0} xmlns=\"http://soap.sforce.com/2006/04/metadata\">\n" +\
                "    <apiVersion>{1}.0</apiVersion>\n" +\
                "    <label>{2}</label>\n" +\
                "</{0}>").format(component_type, settings["api_version"], component_name)

        # Generate new meta.xml file
        with open(file_name+"-meta.xml", "w") as fp:
            fp.write(meta_file_content)

        # After all are finished, we need to keep the lastModifiedDate
        handle_set_component_attribute(attributes)
    
    settings = context.get_settings()
    api = ToolingApi(settings)
    post_url = "/sobjects/" + component_type
    thread = threading.Thread(target=api.post, args=(post_url, data, ))
    thread.start()
    fullName = os.path.basename(file_name)
    ThreadProgress(api, thread, "Creating Component %s" % fullName, 
        "Creating Component %s Succeed" % fullName)
    handle_thread(thread, timeout)

def handle_set_component_attribute(attributes, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        
        result = api.result
        if result["success"] and result["records"]:
            lastModifiedDate = result["records"][0]["LastModifiedDate"]
            util.set_component_attribute(attributes, lastModifiedDate)
        elif settings["debug_mode"]:
            pprint.pprint(result)

    settings = context.get_settings()
    api = ToolingApi(settings)
    soql = "SELECT LastModifiedDate FROM %s WHERE Id = '%s'" % (
        attributes["type"], attributes["id"]
    )
    thread = threading.Thread(target=api.query, args=(soql, True, ))
    thread.start()
    handle_thread(thread, timeout)

def handle_refresh_static_resource(component_attribute, file_name, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        
        if not api.result["success"]: return
        with open (file_name, "wb") as fp:
            fp.write(api.result["body"].encode("utf-8"))

    settings = context.get_settings()
    api = ToolingApi(settings)
    url = component_attribute["url"] + "/body"
    thread = threading.Thread(target=api.retrieve_body, args=(url, ))
    thread.start()
    ThreadProgress(api, thread, 'Refresh StaticResource', 'Refresh StaticResource Succeed')
    handle_thread(thread, timeout)
    
def handle_create_static_resource(data, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        
        if not api.result["success"]: 
            return
        print (api.result)

    settings = context.get_settings()
    api = ToolingApi(settings)
    url = "/tooling/sobjects/StaticResource"
    thread = threading.Thread(target=api.post, args=(url, data, ))
    thread.start()
    ThreadProgress(api, thread, 'Creating StaticResource', 'Creating StaticResource Succeed')
    handle_thread(thread, timeout)

def handle_diff_with_server(component_attribute, file_name, source_org=None, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        
        result = api.result
        
        # If error, just skip, error is processed in ThreadProgress
        if not result["success"]: return

        # Diff Change Compare
        diff.diff_changes(file_name, result)

        # If source_org is not None, we need to switch project back
        if settings["switch_back_after_migration"] and source_org:
            util.switch_project(source_org)

    settings = context.get_settings()
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.get, args=(component_attribute["url"], ))
    thread.start()
    handle_thread(thread, timeout)
    ThreadProgress(api, thread, 'Diff With Server', 'Diff With Server Succeed')

def handle_refresh_file_from_server(attr, file_name, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        
        result = api.result
        if not result["success"]: 
            return
        
        with open(file_name, "wb") as fp:
            fp.write(result[attr["body"]].encode("utf-8"))

    settings = context.get_settings()
    api = ToolingApi(settings)
    thread = threading.Thread(target=api.get, args=(attr["url"], ))
    thread.start()
    ThreadProgress(api, thread, 'Refreshing %s' % os.path.basename(file_name), 'Refresh Succeed')
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