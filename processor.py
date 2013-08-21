import sublime
import sublime_plugin
import os
import urllib
import json
import threading
import time
import pprint
import base64
import zipfile
import shutil
import sys

try:
    # Python 3.x
    import urllib.parse
    from . import requests
    from . import context
    from .salesforce import util

    from .context import COMPONENT_METADATA_SETTINGS
    from .salesforce import message
    from .salesforce.api import SalesforceApi
    from xml.sax.saxutils import unescape
    from .salesforce.util import getUniqueElementValueFromXmlString
    from .salesforce import bulkapi
except:
    # Python 2.x
    import urllib
    import requests
    import context
    from salesforce import util
    from context import COMPONENT_METADATA_SETTINGS
    from salesforce import message
    from salesforce.api import SalesforceApi
    from xml.sax.saxutils import unescape
    from salesforce.util import getUniqueElementValueFromXmlString
    from salesforce import bulkapi

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
        if "@isTest" in body or "testMethod" in body or\
            "testmethod" in body or "test" in name or "Test" in name:
            
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

def populate_sobjects():
    """
    Get the sobjects list in org.
    """

    # Get username
    toolingapi_settings = context.get_toolingapi_settings()
    username = toolingapi_settings["username"]

    # If sobjects is exist in sobjects_completion.sublime-settings, just return it
    sobjects_completions = sublime.load_settings("sobjects_completion.sublime-settings")
    if sobjects_completions.has(username):
        return sobjects_completions.get(username).keys()

    # If sobjects is not exist in globals(), post request to pouplate it
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.describe_global, args=())
    thread.start()

    while thread.is_alive() or api.result == None:
        time.sleep(1)

    sobjects = []
    for sobject in api.result["sobjects"]:
        sobjects.append(sobject["name"])

    globals()[username + "sobjects"] = sobjects
    return sobjects

def handle_refresh_folder(component_type, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            print (">", end=''); time.sleep(0.05)
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        elif api.result == None:
            sublime.status_message(message.TOOLING_API_CONNECTING_FAILED)
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
                if "@isTest" in body or "testMethod" in body or\
                    "testmethod" in body or "test" in component_name or\
                    "Test" in component_name:
                    
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

    print (message.WAIT_FOR_A_MOMENT, end='')
    # Get toolingapi_settings
    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)

    # Get component attributes by component_type
    component_type_attrs = toolingapi_settings[component_type]
    component_outputdir = component_type_attrs["outputdir"]
    component_body = component_type_attrs["body"]
    component_extension = component_type_attrs["extension"]
    component_soql = component_type_attrs["soql"]
    thread = threading.Thread(target=api.query_all, args=(component_soql, ))
    thread.start()
    handle_thread(thread, timeout)

def handle_backup_all_sobjects(timeout=120):
    """
    Firstly get all common used sobject names, and then use bulkapi to backup all
    """

    def handle_thread(thread, timeout):
        if thread.is_alive():
            print (">", end=''); time.sleep(0.05)
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        elif api.result == None:
            sublime.status_message(message.TOOLING_API_CONNECTING_FAILED)
            return

        sobjects = api.result
        bulkapi.handle_bulkapi_query(sobjects)

    print (message.WAIT_FOR_A_MOMENT, end='')
    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.describe_global_common, args=())
    thread.start()
    handle_thread(thread, 10)

def handle_initiate_sobjects_completions(timeout=120):
    """
    Save sobject describe to local which is used in completions

    """

    def handle_threads(apis, threads, timeout):
        for thread in threads:
            if thread.is_alive():
                print (">", end=''); time.sleep(0.05)
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
            # Combine fields dict
            fields_dict = {}

            if sobject_describe != None and "fields" not in sobject_describe:
                print ("Things need to check......: " + sobject_describe)
                continue

            for f in sobject_describe["fields"]:
                fields_dict[f["name"] + "\t" + f["type"]] = f["name"]
            
            # Combine sobject fields dict
            sobjects_completion[sobject_describe["name"]] = fields_dict

        # Every project has unique username
        username = toolingapi_settings["username"]
        s.set(username, sobjects_completion)

        # Save settings
        sublime.save_settings("sobjects_completion.sublime-settings")

        # Output message
        print (message.SEPRATE.format('Sobjects completions local history are initiated.'))

    def handle_thread(api, thread, timeout=120):
        if thread.is_alive():
            print (">", end=''); time.sleep(0.05)
            sublime.set_timeout(lambda:handle_thread(api, thread, timeout), timeout)
            return
        elif api.result == None:
            sublime.error_message(message.AUTHORIZATION_FAILED_MESSAGE)
            return

        sobjects = api.result
        threads = []
        apis = []
        for sobject in sobjects:
            print ("describing " + sobject + "......")
            api = SalesforceApi(toolingapi_settings)
            thread = threading.Thread(target=api.describe_sobject, args=(sobject, ))
            thread.start()
            threads.append(thread)
            apis.append(api)

        handle_threads(apis, threads, 10)

    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.describe_global_common, args=())
    thread.start()
    handle_thread(api, thread, timeout)

def handle_retrieve_all_thread(timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            print (">", end=''); time.sleep(0.05)
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        elif api.result == None:
            sublime.error_message(message.AUTHORIZATION_FAILED_MESSAGE)
            return
        
        result = api.result
        status_code = result["status_code"]
        
        if status_code > 399:
            util.sublime_error_message(result)
            return

        base64String = result["zipFile"]
        outputdir = toolingapi_settings["workspace"] + "/metadata"
        if not os.path.exists(outputdir):
            os.makedirs(outputdir)

        output_file_dir = outputdir + "/sobjects.zip"
        with open(output_file_dir, "wb") as fout:
            fout.write(base64.b64decode(base64String))
            fout.close()

        # Unzip sobjects.zip to file
        zipdir = toolingapi_settings["workspace"] + "/metadata/sobjects.zip"
        outputdir = toolingapi_settings["workspace"] + "/metadata"
        f = zipfile.ZipFile(zipdir, 'r')
        for fileinfo in f.infolist():
            path = outputdir
            directories = fileinfo.filename.split('/')
            for directory in directories:
                # replace / to &, because there has problem in open method
                try:
                    quoted_dir = urllib.parse.unquote(directory).replace("/", "&")
                except:
                    quoted_dir = urllib.unquote(directory).replace("/", "&")
                path = os.path.join(path, quoted_dir)
                if directory == directories[-1]: break # the file
                if not os.path.exists(path):
                    os.makedirs(path)

            outputfile = open(path, "wb")
            shutil.copyfileobj(f.open(fileinfo.filename), outputfile)
            outputfile.close()

        # Close zipFile opener
        f.close()

        # Remove this zip file
        # os.remove(zipdir)

        # Output package path
        print("Your objects and workflows are exported to: " + outputdir)

    print (message.WAIT_FOR_A_MOMENT, end='')
    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.retrieve_all, args=())
    thread.start()
    handle_thread(thread, timeout)

def handle_parse_workflow(timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            print (">", end=''); time.sleep(0.05)
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        elif api.result == None:
            sublime.status_message(message.TOOLING_API_CONNECTING_FAILED)
            return
        
        # If succeed
        sobjects = api.result
        for sobject in sobjects:
            util.parse_workflow_metadata(toolingapi_settings, sobject)

        print("Your workflows are exported to " +\
            toolingapi_settings["workspace"] + "/describe/workflows/")

    print (message.WAIT_FOR_A_MOMENT, end='')
    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.describe_global_common, args=())
    thread.start()
    handle_thread(thread, 10)

def handle_parse_validation_rule(timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            print (">", end=''); time.sleep(0.05)
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        elif api.result == None:
            sublime.status_message(message.TOOLING_API_CONNECTING_FAILED)
            return

        # If succeed
        sobjects = api.result
        util.parse_validation_rule(toolingapi_settings, sobjects)

        print("Your validation rules are exported to " +\
            toolingapi_settings["workspace"] + "/describe/validation rules/validation rules.csv")

    print (message.WAIT_FOR_A_MOMENT, end='')
    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.describe_global_common, args=())
    thread.start()
    handle_thread(thread, 10)

def handle_describe_customfield(sobject, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            print (">", end=''); time.sleep(0.05)
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        elif api.result == None:
            sublime.status_message(message.TOOLING_API_CONNECTING_FAILED)
            return
        
        # If succeed
        result = api.result
        # If error
        if result["status_code"] > 399 :
            util.sublime_error_message(result)
            return

        # Get output csv dir
        workspace = context.get_toolingapi_settings().get("workspace")
        outputdir = workspace + "/describe/customfield"
        if not os.path.exists(outputdir):
            os.makedirs(outputdir)

        # Open output csv
        output_file_dir = outputdir + "/" + sobject + ".csv"
        if util.is_python3x():
            fp = open(output_file_dir, "w", newline='')
        else:
            fp = open(output_file_dir, "wb")

        # Write list to csv
        util.list2csv(fp, result["records"])

        # Release fp
        fp.close()

        # Output log
        print (message.SEPRATE.format(output_file_dir))

    print (message.WAIT_FOR_A_MOMENT, end='')
    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    query = """SELECT Id,TableEnumOrId,DeveloperName,NamespacePrefix,FullName 
               FROM CustomField 
               WHERE TableEnumOrId='{sobject}'""".format(sobject=sobject)
    thread = threading.Thread(target=api.query_all, args=(query, True,))
    thread.start()
    handle_thread(thread, 10)

def handle_describe_global(timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            print (">", end=''); time.sleep(0.05)
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        elif api.result == None:
            sublime.status_message(message.TOOLING_API_CONNECTING_FAILED)
            return
        
        # If succeed
        result = api.result
        # If error
        if result["status_code"] > 399 :
            util.sublime_error_message(result)
            return

        # Get output csv dir
        workspace = context.get_toolingapi_settings().get("workspace")
        outputdir = workspace + "/describe/global"
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

        # Output log
        print (message.SEPRATE.format("global describe csv outputdir: " + output_file_dir))

    print (message.WAIT_FOR_A_MOMENT, end='')
    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.describe_global, args=())
    thread.start()
    handle_thread(thread, timeout)

def handle_describe_layout(sobject, recordtype_name, recordtype_id, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            print (">", end=''); time.sleep(0.05)
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        elif api.result == None:
            sublime.status_message(message.TOOLING_API_CONNECTING_FAILED)
            return
        
        # If succeed
        result = api.result
        
        # If error
        if result["status_code"] > 399 :
            util.sublime_error_message(result)
            return

        # If totalSize is 0
        if "totalSize" in result and result["totalSize"] == 0 :
            util.sublime_error_message(result)
            return

        # Get output csv dir
        toolingapi_settings = context.get_toolingapi_settings()
        outputdir = toolingapi_settings["workspace"] + "/describe/layout"

        # If outputdir is not exist, just make it
        if not os.path.exists(outputdir):
            os.makedirs(outputdir)

        output_file_dir = outputdir + "/" + sobject + "-" + recordtype_name + ".csv"

        if util.is_python3x():
            fp = open(output_file_dir, "w", newline='')
        else:
            fp = open(output_file_dir, "wb")
        util.parse_describe_layout_result(fp, result)
        
        print (message.SEPRATE.format("Layout describe outputdir: " + output_file_dir))

    print (message.WAIT_FOR_A_MOMENT, end='')
    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.describe_layout, args=(sobject, recordtype_id, ))
    thread.start()
    handle_thread(thread, 120)

def handle_execute_query(soql, timeout=120):
    def handle_new_view_thread(thread, timeout):
        if thread.is_alive():
            print (">", end=''); time.sleep(0.05)
            sublime.set_timeout(lambda: handle_new_view_thread(thread, timeout), timeout)
            return
        elif api.result == None:
            sublime.status_message(message.TOOLING_API_CONNECTING_FAILED)
            return
        
        # If succeed
        result = api.result
        # If error
        if result["status_code"] > 399:
            util.sublime_error_message(result)
            return None

        # No error, just display log in a new view
        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": "Execute Query Result",
            "input": util.parse_execute_query_result(result)
        })

    print (message.WAIT_FOR_A_MOMENT, end='')
    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.query, args=(soql, ))
    thread.start()
    handle_new_view_thread(thread, timeout)

def handle_execute_anonymous(apex_string, timeout=120):
    def handle_new_view_thread(thread, timeout):
        print (">", end=''); time.sleep(0.05)
        if thread.is_alive():
            sublime.set_timeout(lambda: handle_new_view_thread(thread, timeout), timeout)
            return
        elif api.result == None:
            sublime.status_message(message.TOOLING_API_CONNECTING_FAILED)
            return
        
        # If succeed
        result = api.result
        # If error
        if result["status_code"] > 399:
            errorCode = util.none_value(result["errorCode"])
            message = util.none_value(result["message"])
            sublime.error_message(errorCode + "\n" + message)
            return

        # No error, just display log in a new view
        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": "Execute Anonymous Result",
            "input": util.parse_execute_anonymous_xml(result)
        })

    print (message.WAIT_FOR_A_MOMENT, end='')
    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.execute_anonymous, args=(apex_string, ))
    thread.start()
    handle_new_view_thread(thread, timeout)

def handle_run_test(class_id, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            print (">", end=''); time.sleep(0.05)
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        elif api.result == None:
            sublime.status_message(message.TOOLING_API_CONNECTING_FAILED)
            return
        
        # If succeed
        result = api.result
        # If error
        if "status_code" in result and result["status_code"] > 399:
            util.sublime_error_message(result)
            return

        # No error, just display log in a new view
        test_result = util.parse_test_result(result)

        # Sometimes, the test result will not show
        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": "Test Result",
            "input": test_result
        })

    print (message.WAIT_FOR_A_MOMENT, end='')
    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.run_test, args=(class_id, ))
    thread.start()
    handle_thread(thread, timeout)

def handle_retrieve_fields(sobject, timeout=120):
    def handle_new_view_thread(thread, timeout):
        if thread.is_alive():
            print (">", end=''); time.sleep(0.05)
            sublime.set_timeout(lambda: handle_new_view_thread(thread, timeout), timeout)
            return
        elif api.result == None:
            sublime.status_message(message.TOOLING_API_CONNECTING_FAILED)
            return
        
        # If succeed
        result = api.result
        # If error
        if result["status_code"] > 399:
            util.sublime_error_message(result)
            return

        # No error, just display log in a new view
        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": sobject + " Describe Result",
            "input": util.parse_sobject_field_result(result)
        })

    print (message.WAIT_FOR_A_MOMENT, end='')
    # Combine sobject url
    sobject_url = "/services/data/v28.0/sobjects/" + sobject+ "/describe"
    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.get, args=(sobject_url, ))
    thread.start()
    handle_new_view_thread(thread, timeout)

def handle_generate_specified_workbooks(sobjects, timeout=120):
    print (message.WAIT_FOR_A_MOMENT, end='')
    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    threads = []
    for sobject in sobjects:
        thread = threading.Thread(target=api.generate_workbook, args=(sobject, ))
        threads.append(thread)
        thread.start()

def handle_generate_all_workbooks(timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            print (">", end=''); time.sleep(0.05)
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        elif api.result == None:
            sublime.status_message(message.TOOLING_API_CONNECTING_FAILED)
            return
        
        # If succeed
        result = api.result
        for sobject in result:
            thread = threading.Thread(target=api.generate_workbook, args=(sobject, ))
            thread.start()

    print (message.WAIT_FOR_A_MOMENT, end='')
    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.describe_global_common, args=())
    thread.start()
    handle_thread(thread, timeout)

def handle_refresh_components(toolingapi_settings, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            print (">", end=''); time.sleep(0.05)
            sublime.set_timeout(lambda: handle_thread(thread, timeout), timeout)
            return
        elif api.result == None:
            sublime.status_message(message.TOOLING_API_CONNECTING_FAILED)
            return
        
        # If succeed, something may happen,
        # for example, user password is expired
        if "status_code" in api.result and api.result["status_code"] > 399:
            util.sublime_error_message(api.result)
            return

        # Load COMPONENT_METADATA_SETTINGS Settings and put all result into it
        # Every org has one local repository
        component_metadata = api.result
        component_metadta = sublime.load_settings(COMPONENT_METADATA_SETTINGS)
        component_metadta.set(toolingapi_settings["username"], component_metadata)
        sublime.save_settings(COMPONENT_METADATA_SETTINGS)
        print (message.SEPRATE.format('All code are Downloaded.'))
        sublime.status_message(message.DOWNLOAD_ALL_SUCCESSFULLY)

        # After Refresh all succeed, start initiate sobject completions
        handle_initiate_sobjects_completions(120)

    print (message.WAIT_FOR_A_MOMENT, end='')
    api = SalesforceApi(toolingapi_settings)
    component_types = context.get_toolingapi_settings()["component_types"]
    thread = threading.Thread(target=api.refresh_components, 
        args=(component_types, ))
    thread.start()
    handle_thread(thread, timeout)

def handle_save_component(component_name, component_attribute, body, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            print (">", end=''); time.sleep(0.05)
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        elif api.result == None:
            sublime.error_message(message.AUTHORIZATION_FAILED_MESSAGE)
            return

        result = api.result
        if "success" in result and result["success"]:
            print (message.SEPRATE.format(message.DEPLOY_SUCCESSFULLY), end='')
        elif "message" in result:
            print (message.SEPRATE.format(result["message"]))
            sublime.status_message(result["message"])

    print (message.WAIT_FOR_A_MOMENT, end='')
    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.save_component, args=(component_attribute, body, ))
    thread.start()
    handle_thread(thread, timeout)

def handle_create_component(data, component_name, component_type, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            print (">", end=''); time.sleep(0.05)
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        elif api.result == None:
            sublime.error_message(message.AUTHORIZATION_FAILED_MESSAGE)
            return
        
        # If create Succeed
        result = api.result
        status_code = result["status_code"]
        
        if status_code > 399:
            util.sublime_error_message(result)
            return
        
        # Get the created component id
        component_id = result.get("id")
        
        # Save it to component.sublime-settings
        s = sublime.load_settings(COMPONENT_METADATA_SETTINGS)
        username = toolingapi_settings["username"]
        components_dict = s.get(username)
        components_dict[component_type][component_name] = {
            "id": component_id,
            "url": post_url + "/" + component_id,
            "body": toolingapi_settings[component_type]["body"],
            "extension": toolingapi_settings[component_type]["extension"],
            "type": component_type,
            "is_test": False
        }
        s.set(username, components_dict)

        # Save settings and show success message
        sublime.save_settings(COMPONENT_METADATA_SETTINGS)
        print (message.SEPRATE.format(message.CREATE_SUCCESSFULLY))
        sublime.status_message(message.CREATE_SUCCESSFULLY)
                
    print (message.WAIT_FOR_A_MOMENT, end='')
    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    post_url = "/services/data/v27.0/sobjects/" + component_type
    thread = threading.Thread(target=api.post, args=(post_url, data, ))
    thread.start()
    handle_thread(thread, timeout)

def handle_refresh_component(component_attribute, file_name, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            print (">", end=''); time.sleep(0.05)
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        elif api.result == None:
            sublime.error_message(message.AUTHORIZATION_FAILED_MESSAGE)
            return
        
        result = api.result
        status_code = result["status_code"]
        
        if status_code > 399:
            util.sublime_error_message(result)
            return

        fp = open(file_name, "wb")
        try:
            body = bytes(result[component_body], "UTF-8")
        except:
            body = result[component_body].encode("UTF-8")

        fp.write(body)
        print (message.SEPRATE.format(message.GET_SUCCESSFULLY))
        sublime.status_message(message.GET_SUCCESSFULLY)

    print (message.WAIT_FOR_A_MOMENT, end='')
    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    component_body = component_attribute["body"]
    component_url = component_attribute["url"]
    thread = threading.Thread(target=api.get, args=(component_url, ))
    thread.start()
    handle_thread(thread, timeout)

def handle_delete_component(component_url, file_name, timeout=120):
    def handle_thread(thread, timeout):
        if thread.is_alive():
            print (">", end=''); time.sleep(0.05)
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        elif api.result == None:
            sublime.error_message(message.AUTHORIZATION_FAILED_MESSAGE)
            return

        # If succeed
        result = api.result
        if result["status_code"] > 399:
            util.sublime_error_message(result)
            return

        os.remove(file_name)
        sublime.active_window().run_command("close")
        print (message.SEPRATE.format(message.DELETE_SUCCESSFULLY))
        sublime.status_message(message.DELETE_SUCCESSFULLY)

    print (message.WAIT_FOR_A_MOMENT, end='')
    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    thread = threading.Thread(target=api.delete, args=(component_url, ))
    thread.start()
    handle_thread(thread, timeout)

def handle_push_topic(sobject, timeout=120):      
    def handle_thread(thread, timeout):
        if thread.is_alive():
            print (">", end=''); time.sleep(0.05)
            sublime.set_timeout(lambda:handle_thread(thread, timeout), timeout)
            return
        elif api.result == None:
            sublime.error_message(message.AUTHORIZATION_FAILED_MESSAGE)
            return

        # If succeed
        result = api.result
        if result["status_code"] > 399:
            util.sublime_error_message(result)
            return

        print (result)

    print (message.WAIT_FOR_A_MOMENT, end='')
    toolingapi_settings = context.get_toolingapi_settings()
    api = SalesforceApi(toolingapi_settings)
    post_url = "/services/data/v28.0/sobjects/PushTopic"
    post_data = {
        "Name": sobject + "PushTopic",
        "Query": get_sobject_soql(toolingapi_settings["username"], sobject),
        "ApiVersion": "28.0",
        "NotifyForOperations": "All",
        "NotifyForFields": "Referenced"
    }
    thread = threading.Thread(target=api.post, args=(post_url, post_data, ))
    thread.start()
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