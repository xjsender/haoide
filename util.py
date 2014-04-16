import sublime
import os
import sys
import json
import csv
import urllib
import pprint
import sys
import time
import base64
import zipfile
import shutil
import xml.dom.minidom
 
from .salesforce import message
from .salesforce import xmltodict
from . import context
from xml.sax.saxutils import unescape


def get_sobject_caches():
    """
    Get the usernames which has cache
    """

    settings = context.get_toolingapi_settings()
    usernames = settings["usernames"]
    settings = sublime.load_settings("sobjects_completion.sublime-settings")
    caches = []
    for username in usernames:
        if settings.has(username):
            caches.append(username)

    return caches

def clear_cache(username):
    settings = sublime.load_settings("sobjects_completion.sublime-settings")
    settings = settings.erase(username)
    sublime.save_settings("sobjects_completion.sublime-settings")
    sublime.status_message(username + " cache is cleared")

def get_sobject_completions(username):
    """
    This method is used in completions.py
    """

    # Load sobjects compoletions
    settings = sublime.load_settings("sobjects_completion.sublime-settings")

    # If current username is in settings, it means project is initiated
    if not settings.has(username):
        return {}

    return settings.get(username)

def get_sobject_completion_list(sobject_describe, prefix="", 
    display_child_relationships=True):
    """
    This method is used in completions.py
    """

    completion_list = []

    # Fields Describe
    fields = sobject_describe["fields"]
    for field_name_desc in sorted(fields):
        field_name = fields[field_name_desc]
        completion = ("%s%s" % (prefix, field_name_desc), field_name)
        completion_list.append(completion)

    # Parent Relationship Describe
    for key in sorted(sobject_describe["parentRelationships"]):
        parent_sobject = sobject_describe["parentRelationships"][key]
        completion_list.append((prefix + key + "\t" + parent_sobject + "(c2p)", key)) 

    # Child Relationship Describe
    if display_child_relationships:
        for key in sorted(sobject_describe["childRelationships"]):
            child_sobject = sobject_describe["childRelationships"][key]
            completion_list.append((prefix + key + "\t" + child_sobject + "(p2c)", key))

    return completion_list

def hide_panel(toggle=False):
    """
    uSed for hiding pandel

    :toggle: if true, just toggle, else, just hiden panel
    """
    sublime.active_window().run_command("hide_panel", 
        {"panel": "console", "toggle": toggle})

def show_panel(toggle=False):
    """
    uSed for showing pandel

    :toggle: if true, just toggle, else, just show panel
    """
    sublime.active_window().run_command("show_panel", 
        {"panel": "console", "toggle": toggle})

def advance_to_first_non_white_space_on_line(view, pt):
    while True:
        c = view.substr(pt)
        if c == " " or c == "\t":
            pt += 1
        else:
            break

    return pt

def has_non_white_space_on_line(view, pt):
    while True:
        c = view.substr(pt)
        if c == " " or c == "\t":
            pt += 1
        else:
            return c != "\n"

def build_comment_data(view, pt):
    shell_vars = view.meta_info("shellVariables", pt)
    if not shell_vars:
        return ([], [])

    # transform the list of dicts into a single dict
    all_vars = {}
    for v in shell_vars:
        if 'name' in v and 'value' in v:
            all_vars[v['name']] = v['value']

    line_comments = []
    block_comments = []

    # transform the dict into a single array of valid comments
    suffixes = [""] + ["_" + str(i) for i in range(1, 10)]
    for suffix in suffixes:
        start = all_vars.setdefault("TM_COMMENT_START" + suffix)
        end = all_vars.setdefault("TM_COMMENT_END" + suffix)
        mode = all_vars.setdefault("TM_COMMENT_MODE" + suffix)
        disable_indent = all_vars.setdefault("TM_COMMENT_DISABLE_INDENT" + suffix)

        if start and end:
            block_comments.append((start, end, disable_indent == 'yes'))
            block_comments.append((start.strip(), end.strip(), disable_indent == 'yes'))
        elif start:
            line_comments.append((start, disable_indent == 'yes'))
            line_comments.append((start.strip(), disable_indent == 'yes'))

    return (line_comments, block_comments)

def is_entirely_line_commented(view, comment_data, region):
    (line_comments, block_comments) = comment_data

    start_positions = [advance_to_first_non_white_space_on_line(view, r.begin())
        for r in view.lines(region)]

    start_positions = list(filter(lambda p: has_non_white_space_on_line(view, p),
        start_positions))

    if len(start_positions) == 0:
        return False

    for pos in start_positions:
        found_line_comment = False
        for c in line_comments:
            (start, disable_indent) = c
            comment_region = sublime.Region(pos,
                pos + len(start))
            if view.substr(comment_region) == start:
                found_line_comment = True
        if not found_line_comment:
            return False

    return True

def get_variable_type(view, pt, pattern):
    """
    Get the variable type by variable name in the view
    """

    # Get the matched variable type
    matched_regions = view.find_all(pattern, sublime.IGNORECASE)
    variable_type = ""

    comment_data = build_comment_data(view, pt)
    match_region = None
    for match_region in matched_regions:
        # Skip comment line
        match_str = view.substr(match_region)
        is_comment = is_entirely_line_commented(view, comment_data, match_region)
        if not is_comment: break

    if not match_region: return ""
    matched_block = view.substr(match_region).strip()
    
    # If list, map, set
    if "<" in matched_block and ">" in matched_block:
        variable_type = matched_block.split("<")[0].strip()
    # String[] strs;
    elif "[]" in matched_block:
        variable_type = 'list'
    # String str;
    else:
        variable_type = matched_block.split(" ")[0]

    return variable_type

def get_symbol_table_completions(symbol_table):
    """
    Copy from MavensMate, need update in future
    """
    
    completions = []
    if 'constructors' in symbol_table:
        for c in symbol_table['constructors']:
            params = []
            visibility = c["visibility"].capitalize() if "visibility" in c else "Public"

            if 'parameters' in c and type(c['parameters']) is list and len(c['parameters']) > 0:
                for p in c['parameters']:
                    params.append(p["type"].capitalize() + " " + p["name"])
                paramStrings = []
                for i, p in enumerate(params):
                    paramStrings.append("${"+str(i+1)+":"+params[i]+"}")
                paramString = ", ".join(paramStrings)
                completions.append((visibility + " " + c["name"]+"("+", ".join(params)+")", 
                    c["name"]+"("+paramString+")"))
            else:
                completions.append((visibility + " " + c["name"]+"()", c["name"]+"()${1:}"))

    if 'properties' in symbol_table:
        for c in symbol_table['properties']:
            visibility = c["visibility"].capitalize() if "visibility" in c else "Public"
            property_type = c["type"].capitalize() if "type" in c and c["type"] else ""
            completions.append((visibility + " " + c["name"] + "\t" + property_type, c["name"]))

    if 'methods' in symbol_table:
        for c in symbol_table['methods']:
            params = []
            visibility = c["visibility"].capitalize() if "visibility" in c else "Public"
            if 'parameters' in c and type(c['parameters']) is list and len(c['parameters']) > 0:
                for p in c['parameters']:
                    params.append(p["type"] + " " + p["name"])
            if len(params) == 1:
                completions.append((visibility + " " + c["name"]+"("+", ".join(params)+") \t"+c['returnType'], c["name"]+"(${1:"+", ".join(params)+"})"))
            elif len(params) > 1:
                paramStrings = []
                for i, p in enumerate(params):
                    paramStrings.append("${"+str(i+1)+":"+params[i]+"}")
                paramString = ", ".join(paramStrings)
                completions.append((visibility + " " + c["name"]+"("+", ".join(params)+") \t"+c['returnType'], c["name"]+"("+paramString+")"))
            else:
                completions.append((visibility + " " + c["name"]+"("+", ".join(params)+") \t"+c['returnType'], c["name"]+"()${1:}"))

    if 'innerClasses' in symbol_table:
        for c in symbol_table["innerClasses"]:
            if 'constructors' in c and len(c['constructors']) > 0:
                for con in c['constructors']:
                    visibility = con["visibility"].capitalize() if "visibility" in con else "Public"
                    params = []
                    if 'parameters' in con and type(con['parameters']) is list and len(con['parameters']) > 0:
                        for p in con['parameters']:
                            params.append(p["type"].capitalize() + " " + p["name"])
                        paramStrings = []
                        for i, p in enumerate(params):
                            paramStrings.append("${"+str(i+1)+":"+params[i]+"}")
                        paramString = ", ".join(paramStrings)
                        completions.append((visibility + " " + con["name"]+"("+", ".join(params)+")", c["name"]+"("+paramString+")"))
                    else:
                        completions.append((visibility + " " + con["name"]+"()", c["name"]+"()${1:}"))
            else:
                completions.append(("Inner Class " + c["name"] + "\t", c["name"] + "$1"))
    return sorted(completions)

def add_operation_history(operation, history_content):
    """
    Keep the history in the local history rep

    :operation: the operation source
    :history_content: the content needed to keep
    """
    settings = context.get_toolingapi_settings()
    if not settings["keep_operation_history"]: return

    splits = operation.split("/")
    if len(splits) == 1:
        folder, operation = "", splits[0]
    elif len(splits) == 2:
        folder, operation = splits
    outputdir = settings["workspace"] + "/.history/" + folder
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)

    time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    seprate = "\n" + 100 * "-" + "\n"
    history = time_stamp + seprate + history_content + "\n" * 2
    fp = open(outputdir + "/%s.txt" % operation, "a")
    fp.write(history)
    fp.close()

def check_new_component_enabled():
    settings = context.get_toolingapi_settings()
    return os.path.exists(settings["workspace"])
    
def check_workspace_available(settings=None):
    """
    Check workspace is available, if not make it
    """
    if not settings: settings = context.get_toolingapi_settings()
    if not os.path.exists(settings["workspace"]):
        sublime.active_window().run_command('create_new_project', {
            "switch_project": False
        })

def get_view_by_name(view_name):
    """
    Get the view in the active window by the view_name

    @view_id: view name
    @return: view
    """

    view = None
    for v in sublime.active_window().views():
        if v.name() == view_name:
            view = v

    return view

def get_view_by_file_name(file_name):
    """
    Get the view in the active window by the view_name

    @view_id: view name
    @return: view
    """

    view = None
    for v in sublime.active_window().views():
        if file_name in v.file_name():
            view = v

    return view

def get_view_by_id(view_id):
    """
    Get the view in the active window by the view_id

    @view_id: id of view
    @return: view
    """

    view = None
    for v in sublime.active_window().views():
        if v.id() == view_id:
            view = v

    return view

def base64_zip(zipfile):
    with open(zipfile, "rb") as f:
        bytes = f.read()
        base64String = base64.b64encode(bytes)

    return base64String.decode('UTF-8')

def extract_zip(base64String, outputdir):
    """
    1. Decode base64String to zip
    2. Extract zip to files
    """

    # Decode base64String to zip
    if not os.path.exists(outputdir): os.makedirs(outputdir)
    zipdir = outputdir + "/package.zip"
    with open(zipdir, "wb") as fout:
        fout.write(base64.b64decode(base64String))
        fout.close()

    # Unzip sobjects.zip to file
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

def format_debug_logs(toolingapi_settings, records):
    if len(records) == 0: return "No available logs."

    # Used to list debug logs as below format
    debug_log_headers = [
        "Id", "StartTime", "Operation", "Status"
    ]
    debug_log_headers_properties = {
        "Id": {
            "width": 20,
            "label": "Log Id"
        },
        "StartTime": {
            "width": 22,
            "label": "Start Time"
        },
        "Request": {
            "width": 13,
            "label": "Request Type"
        },
        "Application": {
            "width": 12,
            "label": "Application"
        },
        "Status": {
            "width": 10,
            "label": "Status"
        },
        "LogLength": {
            "width": 8,
            "label": "Size(b)"
        },
        "DurationMilliseconds": {
            "width": 13,
            "label": "Duration(ms)"
        },
        "Operation": {
            "width": 50,
            "label": "Operation"
        }
    }

    # Headers
    headers = ""
    for header in debug_log_headers:
        headers += "%-*s" % (debug_log_headers_properties[header]["width"], 
            debug_log_headers_properties[header]["label"])

    # Content
    content = ""
    records = reversed(sorted(records, key=lambda k : k['StartTime']))
    for record in records:
        for header in debug_log_headers:
            if header == "StartTime":
                content += "%-*s" % (debug_log_headers_properties[header]["width"],
                    record[header][0:19].replace('T', ' '))
                continue
            content += "%-*s" % (debug_log_headers_properties[header]["width"], record[header])
        content += "\n"

    return headers + "\n" + content[:len(content)-1]

def format_error_message(result):
    """
    Format message as below format
           message:     The requested resource does not exist   
               url:     url
         errorCode:     NOT_FOUND                       
       status_code:     404     

    @result: dict error when request status code > 399
    @return: formated error message   
    """
    # Add time stamp
    result["Time Stamp"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    error_message = ""
    for key, value in result.items():
        error_message += "% 30s\t" % "{0}: ".format(key)
        value = urllib.parse.unquote(unescape(none_value(value), 
            {"&apos;": "'", "&quot;": '"'}))
        error_message += "%-30s\t" % value + "\n"

    return error_message[:len(error_message)-1]

def format_waiting_message(result, header=""):
    error_message = header + "\n" + "-" * 100 + "\n"
    for key in result:
        if isinstance(result[key], list): continue
        error_message += "% 30s\t" % "{0}: ".format(key)
        error_message += "%-30s\t" % none_value(result[key]) + "\n"

    if "messages" in result:
        messages = result["messages"]
        error_message += message.SEPRATE.format("Deploy Messages")
        for key in messages[0].keys():
            error_message += "%-30s" % key.capitalize()
        error_message += "\n"
        for msg in messages:
            for key in msg:
                error_message += "%-30s" % none_value(msg[key])
            error_message += "\n"

    return error_message

def none_value(value):
    """
    If value is None, return "", if not, return value

    @value: value
    """

    if not value: return ""
    return "%s" % value
    
def is_python3x():
    """
    If python version is 3.x, return True
    """

    return sys.version > '3'

"""
Below three functions are used to parse completions out of box.
"""
def parse_namespace(publicDeclarations):
    """
    from . import util
    import json
    namespace_json = util.parse_namespace(publicDeclarations["publicDeclarations"])
    json.dump(namespace_json, open("c:/namespace.json",'w'))
    """

    namespaces_dict = {}
    for namespace in publicDeclarations:
        namespaces_dict[namespace] = list(publicDeclarations[namespace].keys())

    return namespaces_dict

def parse_method(methods, is_method=True):
    if not methods: return {}

    methods_dict = {}
    for method in methods:
        if not method["name"]: continue
        if not is_method:
            returnType = ''
        else:
            returnType = method["returnType"]
        if not method["parameters"]:
            methods_dict["%s()\t%s" % (method["name"], returnType)] = method["name"] + "()$0"
        else:
            display_parameters = []
            for parameter in method["parameters"]:
                display_parameters.append(parameter["type"] + " " + parameter["name"])

            return_parameters = []
            for i in range(len(display_parameters)):
                return_parameters.append("${%s:%s}" % (i + 1, display_parameters[i]))

            methods_dict["%s(%s)\t%s" % (method["name"], ','.join(display_parameters), returnType)] =\
                "%s(%s)$0" % (method["name"], ','.join(return_parameters))

    return methods_dict

def parse_properties(properties):
    if not properties: return {}
    properties_dict = {}
    for property in properties:
        properties_dict[property["name"]] = property["name"] + "$0"

    return properties_dict

def parse_all(apex):
    """
    Usage:
        from . import util
        import json
        apex_json = util.parse_all(publicDeclarations["publicDeclarations"])
        json.dump(apex_json, open("c:/apex.json",'w'))

        from .salesforce.support import apex
        return_apex = {}
        for lib in apex.apex_completions:
            if "customize" in apex.apex_completions[lib]:
                return_apex[lib] = apex.apex_completions[lib]

        json.dump(return_apex, open("c:/customize.json",'w'))

    """

    apex_completions = {}
    for namespace in apex.keys():
        for class_name in apex[namespace]:
            class_detail = apex[namespace][class_name]

            constructors_dict = parse_method(class_detail["constructors"], False)
            methods_dict = parse_method(class_detail["methods"])
            properties_dict = parse_properties(class_detail["properties"])

            # all_dict = dict(list(methods_dict.items()) + list(properties_dict.items()))

            # Parse constructor, methods and properties
            apex_completions[class_name.lower()] = {}
            apex_completions[class_name.lower()]["constructors"] = constructors_dict
            apex_completions[class_name.lower()]["methods"] = methods_dict
            apex_completions[class_name.lower()]["properties"] = properties_dict
            apex_completions[class_name.lower()]["namespace"] = namespace

            # Class Name Full Name Attribute
            apex_completions[class_name.lower()]["name"] = class_name
            
    return apex_completions

def parse_code_coverage(result):
    records = {}
    for record in result["records"]:
        name = record["ApexClassOrTrigger"]["Name"]
        records[name] = {
            "NumLinesCovered" : record["NumLinesCovered"],
            "NumLinesUncovered": record["NumLinesUncovered"]
        }

    code_coverage_desc = message.SEPRATE.format("TriggerOrClass Code Coverage:")

    columns = ""
    for column in ["ApexClassOrTrigger", "Percent", "Lines"]:
        columns += "%-*s" % (40, column)

    code_coverage = ""
    for name in sorted(records):
        row = ""
        row += "%-*s" % (40, name)
        coverage = records[name]
        if not coverage["NumLinesCovered"] or not coverage["NumLinesUncovered"]:
            continue
        covered_lines = coverage["NumLinesCovered"]
        total_lines = covered_lines + coverage["NumLinesUncovered"]
        coverage = covered_lines / total_lines * 100 if total_lines != 0 else 0
        row += "%-*s" % (40, "%.2f%%" % coverage)
        row += "%-*s" % (40, "%s/%s" % (covered_lines, total_lines))
        code_coverage += row + "\n"

    return message.SEPRATE.format(code_coverage_desc + columns + "\n" + code_coverage)

def parse_test_result(test_result):
    """
    format test result as specified format

    @result: Run Test Request result
    @return: formated string
    """

    # Parse Test Result
    if len(test_result) == 0: return "It's not test class"
    test_result_desc = ' Test Result\n'
    test_result_content = ""
    for record in test_result:
        test_result_content += "-" * 100 + "\n"
        test_result_content += "% 30s    " % "MethodName: "
        test_result_content += "%-30s" % none_value(record["MethodName"]) + "\n"
        test_result_content += "% 30s    " % "TestTimestamp: "
        test_result_content += "%-30s" % none_value(record["TestTimestamp"]) + "\n"
        test_result_content += "% 30s    " % "ApexClass: "
        class_name = record["ApexClass"]["Name"]
        test_result_content += "%-30s" % class_name + "\n"
        test_result_content += "% 30s    " % "Pass/Fail: "
        test_result_content += "%-30s" % none_value(record["Outcome"]) + "\n"
        test_result_content += "% 30s    " % "Error Message: "
        test_result_content += "%-30s" % none_value(record["Message"]) + "\n"
        test_result_content += "% 30s    " % "Stack Trace: "
        test_result_content += "%-30s" % none_value(record["StackTrace"]) + "\n"

    return_result = class_name + test_result_desc + test_result_content[:-1]

    # Parse Debug Log Part
    debug_log_desc = message.SEPRATE.format("You can choose the LogId and view log detail in Sublime or Salesforce by context menu")
    debug_log_content = "LogId: "
    if len(test_result) > 0 and test_result[0]["ApexLogId"] != None:
        debug_log_content += test_result[0]["ApexLogId"]

    return_result += debug_log_desc + debug_log_content

    return return_result

def parse_validation_rule(toolingapi_settings, sobjects):
    """
    Parse the validation rule in Sobject.object to csv

    @toolingapi_settings: toolingapi.sublime-settings reference
    @sobject: sobject name
    @validation_rule_path: downloaded objects path by Force.com IDE or ANT
    """

    # Open target file
    outputdir = toolingapi_settings["workspace"] + "/validation"
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)

    # Create or Edit csv File
    if is_python3x():
        fp_validationrules = open(outputdir + "/validation rules.csv", "a", newline='')
    else:
        fp_validationrules = open(outputdir + "/validation rules.csv", "ab")

    # Initiate CSV Writer and Write headers
    columns = toolingapi_settings["validation_rule_columns"]
    dict_write = csv.DictWriter(fp_validationrules, columns)
    dict_write.writer.writerow([v.capitalize() for v in columns])

    # Open workflow source file
    validation_rule_path = toolingapi_settings["workspace"] + "/metadata/unpackaged/objects"
    for sobject in sobjects:
        try:
            fp = open(validation_rule_path + "/" + sobject + ".object", "rb")
        except IOError:
            # If one sobject is not exist, We don't need do anything
            continue

        result = xmltodict.parse(fp.read())
        fp.close()
        
        ######################################
        # Rules Part
        ######################################
        try:
            rules = result["CustomObject"]["validationRules"]
            write_metadata_to_csv(dict_write, columns, rules, sobject)
        except KeyError:
            # If one sobject doesn't have vr, We don't need do anything
            pass

    # Close fp
    fp_validationrules.close()

def parse_workflow_metadata(toolingapi_settings, sobject):
    """
    Parse Sobject.workflow to csv, including rule, field update and alerts

    @toolingapi_settings: toolingapi.sublime-settings reference
    @sobject: sobject name
    @workflow_metadata_path: downloaded workflow path by Force.com IDE or ANT
    """
    # Open workflow source file
    workflow_metadata_path = toolingapi_settings["workspace"] + "/metadata/unpackaged/workflows"
    try:
        fp = open(workflow_metadata_path + "/" + sobject + ".workflow", "rb")
    except IOError:
        return

    # Outputdir for save workflow rule, field update, email alert
    # and outbound message and task
    outputdir = toolingapi_settings["workspace"] + "/workflow"
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)

    # Convert xml to dict
    result = xmltodict.parse(fp.read())
    fp.close()

    ######################################
    # Rules Part
    ######################################
    try:
        rules = result["Workflow"]["rules"]
    except KeyError:
        return

    # Initiate CSV Writer and Write headers
    columns = toolingapi_settings["workflow_rule_columns"]
    try:
        # Python 3.x
        fp = open(outputdir + "/" + sobject + " workflow rule.csv", "wt", newline='')
    except:
        # Python 2.x
        fp = open(outputdir + "/" + sobject + " workflow rule.csv", "wb")
    dict_write = csv.DictWriter(fp, columns, dialect=csv.excel)
    dict_write.writer.writerow([v.capitalize() for v in columns])

    # Write rows
    write_metadata_to_csv(dict_write, columns, rules, sobject)

    # Close fp
    fp.close()

    ######################################
    # Field Update Part
    ######################################
    try:
        fieldUpdates = result["Workflow"]["fieldUpdates"]
    except KeyError:
        return

    # Initiate CSV Writer and Write headers
    columns = toolingapi_settings["workflow_field_update_columns"]
    try:
        # Python 3.x
        fp = open(outputdir + "/" + sobject + " workflow field update.csv", "wt", newline='')
    except:
        # Python 2.x
        fp = open(outputdir + "/" + sobject + " workflow field update.csv", "wb")
    dict_write = csv.DictWriter(fp, columns)
    dict_write.writer.writerow([v.capitalize() for v in columns])

    # Write rows
    write_metadata_to_csv(dict_write, columns, fieldUpdates, sobject)

    # Close fp
    fp.close()

    ######################################
    # Email Alert Part
    ######################################
    try:
        alerts = result["Workflow"]["alerts"]
    except KeyError:
        return

    # Initiate CSV Writer and Write headers
    columns = toolingapi_settings["workflow_email_alert_columns"]
    try:
        # Python 3.x
        fp = open(outputdir + "/" + sobject + " email alert.csv", "wt", newline='')
    except:
        # Python 2.x
        fp = open(outputdir + "/" + sobject + " email alert.csv", "wb")
    dict_write = csv.DictWriter(fp, columns)
    dict_write.writer.writerow([v.capitalize() for v in columns])

    # Write rows
    write_metadata_to_csv(dict_write, columns, alerts, sobject)

    # Close fp
    fp.close()

    ######################################
    # Outbound Message Part
    ######################################
    try:
        outboundMessages = result["Workflow"]["outboundMessages"]
    except KeyError:
        return

    # Initiate CSV Writer and Write headers
    columns = toolingapi_settings["workflow_outbound_message_columns"]
    try:
        # Python 3.x
        fp = open(outputdir + "/" + sobject + " outbound message.csv", "wt", newline='')
    except:
        # Python 2.x
        fp = open(outputdir + "/" + sobject + " outbound message.csv", "wb")
    dict_write = csv.DictWriter(fp, columns)
    dict_write.writer.writerow([v.capitalize() for v in columns])

    # Write rows
    write_metadata_to_csv(dict_write, columns, outboundMessages, sobject)

    # Close fp
    fp.close()

    ######################################
    # Task Part
    ######################################
    try:
        tasks = result["Workflow"]["tasks"]
    except KeyError:
        return

    # Initiate CSV Writer and Write headers
    columns = toolingapi_settings["workflow_task_columns"]
    try:
        # Python 3.x
        fp = open(outputdir + "/" + sobject + " task.csv", "wt", newline='')
    except:
        # Python 2.x
        fp = open(outputdir + "/" + sobject + " task.csv", "wb")
    dict_write = csv.DictWriter(fp, columns)
    dict_write.writer.writerow([v.capitalize() for v in columns])

    # Write rows
    write_metadata_to_csv(dict_write, columns, tasks, sobject)

    # Close fp
    fp.close()

def write_metadata_to_csv(dict_write, columns, metadata, sobject):
    """
    this method is invoked by function in this module

    @fp: output csv file open reference
    @columns: your specified metadata workbook columns in settings file
    @metadata: metadata describe
    """

    # If sobject has only one rule, it will be dict
    # so we need to convert it to list
    if isinstance(metadata, dict):
        metadata_temp = [metadata]
        metadata = metadata_temp

    # We just use sobject as column, 
    # it's value is assigned with sobject parameter
    columns = [col for col in columns if col != "sobject"]

    for rule in metadata:
        row_value = [sobject]
        for key in columns:
            # Because Workflow rule criteria has different type
            # If key is not in rule, just append ""
            if key not in rule.keys():
                row_value.append("")
                continue

            cell_value = rule[key]
            if isinstance(cell_value, list):
                value = ''
                if len(cell_value) > 0:
                    if isinstance(cell_value[0], dict):
                        values = []
                        for cell_dict in cell_value:
                            for cell_dict_key in cell_dict.keys():
                                values.append(cell_dict[cell_dict_key])
                            value += " ".join(values) + "\n"
                    else:
                        value = " ".join(cell_value) + "\n"

                    cell_value = value[ : -1]
                else:
                    cell_value = ""

            elif isinstance(cell_value, dict):
                value = ''
                for cell_key in cell_value.keys():
                    if not cell_value[cell_key]:
                        value += cell_key + ": ' '" + "\n"
                    else:
                        value += cell_key + ": " + cell_value[cell_key] + "\n"

                cell_value = value[ : -1]

            elif not cell_value:
                cell_value = ""

            else:
                cell_value = "%s" % cell_value

            # Unescape special code to normal
            try:
                # Python 3.x
                cell_value = urllib.parse.unquote(unescape(cell_value, 
                    {"&apos;": "'", "&quot;": '"'}))
            except:
                # Python 2.x
                cell_value = urllib.unquote(unescape(cell_value, 
                    {"&apos;": "'", "&quot;": '"'}))

            # Append cell_value to list in order to write list to csv
            if is_python3x():
                row_value.append(cell_value)
            else:
                row_value.append(cell_value.encode("utf-8"))

        # Write row
        dict_write.writer.writerow(row_value)

NOT_INCLUDED_COLUMNS = ["urls", "attributes"]
def list2csv(file_path, records):
    """
    convert simple dict in list to csv

    @records: [{"1": 1}, {"2": 2}]
    """
    # If records size is 0, just return
    if len(records) == 0: return "No Custom Fields"

    header = [k.encode('utf-8') for k in records[0] if k not in NOT_INCLUDED_COLUMNS]
    with open(file_path, "wb") as fp:
        fp.write(b",".join(header) + b"\n")
        for record in records:
            values = []
            for k, v in record.items():
                if k.encode('utf-8') in header:
                    values.append(none_value(v).encode("utf-8"))
            fp.write(b",".join(values) + b"\n")

def parse_field_dependencies(settings, sobject):
    if sobject != "VCC_Product_Configuration__c": return
    # Open workflow source file
    workspace = settings["workspace"]
    path = workspace + "/metadata/unpackaged/objects/%s.object" % sobject
    try:
        fp = open(path, "rb")
    except IOError:
        return

    # Outputdir
    outputdir = "%s/fieldDependencies" % workspace
    if not os.path.exists(outputdir): os.makedirs(outputdir)

    # Convert xml to dict
    result = xmltodict.parse(fp.read())
    fp.close()

    pprint.pprint(result)

def parse_data_template(output_file_dir, result):
    # Get all layoutItems
    field_lables = []
    field_apis = []
    fields_required = []
    fields_type = []
    fields_picklist_labels = []
    fields_picklist_values = []
    for edit_layout_section in result["editLayoutSections"]:
        if isinstance(edit_layout_section["layoutRows"], list):
            layout_rows = edit_layout_section["layoutRows"]
        elif isinstance(edit_layout_section["layoutRows"], dict):
            layout_rows = [edit_layout_section["layoutRows"]]

        for layout_row in layout_rows:
            if isinstance(layout_row["layoutItems"], list):
                layout_items = layout_row["layoutItems"]
            elif isinstance(layout_row["layoutItems"], dict):
                layout_items = [layout_row["layoutItems"]]

            for layout_item in layout_items:
                if not layout_item["label"]: continue
                for layout_component in layout_item["layoutComponents"]:
                    # Some layout_component is blank
                    if "details" not in layout_component: continue

                    # Get field describe
                    details = layout_component["details"]

                    # If field type is AutoNumber, just skip
                    if details["autoNumber"]: continue

                    field_lables.append(details["label"])
                    field_apis.append(details["name"])
                    fields_required.append("Required" if layout_item["required"] else "")
                    fields_type.append(details["type"].capitalize())

                    picklist_labels = []
                    picklist_values = []
                    for picklist in details["picklistValues"]:
                        picklist_labels.append(picklist["label"])
                        picklist_values.append(picklist["value"])
                        
                    fields_picklist_labels.append('"%s"' % "\n".join(picklist_labels))
                    fields_picklist_values.append('"%s"' % "\n".join(picklist_values))

    # Write field_lables and field apis
    # Create new csv
    with open(output_file_dir, "wb") as fp:
        fp.write(u'\ufeff'.encode('utf8'))
        fp.write(",".join(field_lables).encode("utf-8") + b"\n")
        fp.write(",".join(field_apis).encode("utf-8") + b"\n")
        fp.write(",".join(fields_type).encode("utf-8") + b"\n")
        fp.write(",".join(fields_required).encode("utf-8") + b"\n")
        fp.write(",".join(fields_picklist_labels).encode("utf-8") + b"\n")
        fp.write(",".join(fields_picklist_values).encode("utf-8") + b"\n")

def parse_execute_anonymous_xml(result):
    """
    Get the compile result in the xml result

    @result: execute anonymous result, it's a xml

    @return: formated string
    """

    compiled = result["compiled"]
    debugLog = result["debugLog"]

    view_result = ''
    if compiled == "true":
        view_result = debugLog
    elif compiled == "false":
        line = result["line"]
        column = result["column"]
        compileProblem = result["compileProblem"]
        view_result = compileProblem + " at line " + line +\
            " column " + column

    view_result = urllib.parse.unquote(unescape(view_result, 
        {"&apos;": "'", "&quot;": '"'}))

    return view_result

def generate_workbook(result, workspace, workbook_field_describe_columns):
    """
    generate workbook for sobject according to user customized columns
    you can change the workbook_field_describe_columns in default settings

    @result: sobject describe result
    @workspace: your specified workspace in toolingapi.sublime-settings
    @workflow_field_update_columns: your specified workbook columns in toolingapi.sublime-settings
    """
    # Get sobject name
    sobject = result.get("name")

    # Get fields
    fields = result.get("fields")
    fields_key = workbook_field_describe_columns

    # If workbook path is not exist, just make it
    outputdir = workspace + "/workbooks"
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)

    # Create new csv file for this workbook
    # fp = open(outputdir + "/" + sobject + ".csv", "wb", newline='')
    if is_python3x():
        fp = open(outputdir + "/" + sobject + ".csv", "w", newline='')
    else:
        fp = open(outputdir + "/" + sobject + ".csv", "wb")
    
    #------------------------------------------------------------
    # Headers, all headers are capitalized
    #------------------------------------------------------------
    headers = [column.capitalize() for column in fields_key]
    dict_write = csv.DictWriter(fp, headers, quoting=csv.QUOTE_ALL)
    dict_write.writer.writerow(headers)

    #------------------------------------------------------------
    # Fields Part (All rows are sorted by field label)
    #------------------------------------------------------------
    fields = sorted(fields, key=lambda k : k['label'])
    for field in fields:
        row = []
        for key in fields_key:
            # Get field value by field API(key)
            row_value = field.get(key)
            
            if isinstance(row_value, list):
                if key == "picklistValues":
                    value = ''
                    if len(row_value) > 0:
                        for item in row_value:
                            value += item.get("value") + "\n"
                        row_value = value
                    else:
                        row_value = ""
                elif key == "referenceTo":
                    if len(row_value) > 0:
                        row_value = row_value[0]
                    else:
                        row_value = ""
            elif not row_value:
                row_value = ""
            else:
                row_value = "%s" % row_value

            if  is_python3x():
                row.append(row_value)
            else:
                row.append(row_value.encode('utf-8'))

        # Write row to csv
        dict_write.writer.writerow(row)

    # Close fp
    fp.close()

    # Display Success Message
    sublime.set_timeout(lambda:sublime.status_message(sobject + " workbook is generated"), 10)

    # Return outputdir
    return outputdir

record_keys = ["label", "name", "type", "length"]
record_key_width = {
    "label": 40, 
    "name": 40, 
    "type": 15, 
    "length": 10
}
recordtype_key_width = {
    "available": 10,
    "recordTypeId": 20,
    "name": 35,
    "defaultRecordTypeMapping": 15
}
childrelationship_key_width = {
    "field": 35,
    "relationshipName": 35,
    "childSObject": 30,
    "cascadeDelete": 12
}

seprate = 100 * "-" + "\n"
def parse_sobject_field_result(result):
    """
    According to sobject describe result, display recordtype information, child sobjects 
    information and the field information.

    @result: sobject describe information, it's a dict

    @return: formated string including the three parts
    """

    # Get sobject name
    sobject = result.get("name")

    # View Name or Header
    view_result = sobject + " Describe:\n"

    #------------------------------------------------
    # Fields Part
    #------------------------------------------------
    # Output totalSize Part
    fields = result.get("fields")
    view_result += seprate
    view_result += "Total Fields: \t" + str(len(fields)) + "\n"
    view_result += seprate

    # Ouput Title and seprate line
    columns = ""
    for key in record_keys:
        key_width = record_key_width[key]
        columns += "%-*s" % (key_width, key.capitalize())

    view_result += columns + "\n"
    view_result += len(columns) * "-" + "\n"

    # Sort fields list by lable of every field
    fields = sorted(fields, key=lambda k : k['label'])

    # Output field values
    for record in fields:
        row = ""
        for key in record_keys:
            row_value = record.get(key)
            if not row_value:
                row_value = ""

            key_width = record_key_width[key]
            row_value = "%-*s" % (key_width, row_value)
            row += row_value

        view_result += row + "\n"
    view_result += "\n"

    #------------------------------------------------
    # Record Type Part
    #------------------------------------------------
    recordtypes = result.get("recordTypeInfos")
    view_result += seprate
    view_result += "Record Type Info: \t" + str(len(recordtypes)) + "\n"
    view_result += seprate

    # Get Record Type Info Columns
    recordtype_keys = []
    if len(recordtypes) > 0:
        recordtype_keys = recordtypes[0].keys()

    columns = ""
    for key in recordtype_keys:
        if not key in recordtype_key_width: continue
        key_width = recordtype_key_width[key]
        if key == "defaultRecordTypeMapping": key = "default"
        columns += "%-*s" % (key_width, key.capitalize())

    view_result += columns + "\n"
    view_result += len(columns) * "-" + "\n"

    for recordtype in recordtypes:
        row = ""
        for key in recordtype_keys:
            if key not in recordtype_key_width: continue
            
            # Get field value by field API
            # and convert it to str
            row_value = recordtype.get(key)
            if not row_value:
                row_value = ""

            key_width = recordtype_key_width[key]
            row_value = "%-*s" % (key_width, row_value)
            row += row_value
            
        view_result += row + "\n"

    view_result += "\n"

    #------------------------------------------------
    # Child Relationship
    #------------------------------------------------
    childRelationships = result.get("childRelationships")
    view_result += seprate
    view_result += "ChildRelationships Info: \t" + str(len(childRelationships)) + "\n"
    view_result += seprate

    # Get Record Type Info Columns
    childRelationships_keys = childrelationship_key_width.keys()
    columns = ""
    for key in childRelationships_keys:
        columns += "%-*s" % (30, key.capitalize())

    view_result += columns + "\n"
    view_result += len(columns) * "-" + "\n"

    for childRelationship in childRelationships:
        row = ""
        for key in childRelationships_keys:
            # Get field value by field API
            # and convert it to str
            row_value = childRelationship.get(key)
            if not row_value:
                row_value = ""

            row_value = "%-*s" % (30, row_value)
            row += row_value
            
        view_result += row + "\n"

    view_result += "\n"

    return view_result

def getUniqueElementValueFromXmlString(xmlString, elementName):
    """
    Extracts an element value from an XML string.
    
    For example, invoking 
    getUniqueElementValueFromXmlString('<?xml version="1.0" encoding="UTF-8"?><foo>bar</foo>', 'foo')
    should return the value 'bar'.
    """
    xmlStringAsDom = xml.dom.minidom.parseString(xmlString)
    elementsByName = xmlStringAsDom.getElementsByTagName(elementName)
    elementValue = None
    if len(elementsByName) > 0:
        elementValue = elementsByName[0].toxml().replace('<' + elementName + '>','').replace('</' + elementName + '>','')
    return elementValue

def get_path_attr(path_dir):
    # Get the Folder Name and Project Name
    path, folder = os.path.split(path_dir)
    path, src = os.path.split(path)
    
    if "src" not in src:
        project_name = src
    else:
        path, project_name = os.path.split(path)
        folder = src + "/" + folder

    # Assume the project name has time suffix, 
    year = get_current_year()
    if year in project_name: project_name = project_name[:-9]

    return project_name, folder

def get_current_year():
    """
    Get the current year
    """
    return time.strftime("%Y", time.localtime())

def get_file_attr(file_name):
    try:
        folder, extension = os.path.splitext(file_name)
        name = ""
        if "\\" in folder:
            name = folder[folder.rfind("\\")+1:]
        elif "/" in folder:
            name = folder[folder.rfind("/")+1:]
        return name, extension
    except:
        pass

def get_component_attribute(file_name):
    """
    get the component name by file_name, and then get the component_url and component_id
    by component name and local settings

    @file_name: local component full file name, for example:
    D:\ForcedotcomWorkspace\pro-exercise-20130625\ApexClass\AccountChartController.cls

    @return: for example, component_attribute = {
        "body": "Body",
        "extension": ".cls",
        "id": "01pO00000009isEIAQ",
        "is_test": false,
        "type": "ApexClass",
        "url": "/services/data/v28.0/sobjects/ApexClass/01pO00000009isEIAQ"
    }
    """
    # Get toolingapi settings
    toolingapi_settings = context.get_toolingapi_settings()

    # Get component type
    name, extension = get_file_attr(file_name)

    # If extension is None, just return
    if not extension or extension not in toolingapi_settings["component_extensions"]:
        return

    component_type = toolingapi_settings[extension]
    username = toolingapi_settings["username"]
    component_settings = sublime.load_settings(context.COMPONENT_METADATA_SETTINGS)

    try:
        component_attribute = component_settings.get(username)[component_type][name]
    except:
        return (None, None)

    # Return tuple
    return (component_attribute, name)