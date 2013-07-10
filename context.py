import sublime
import sublime_plugin
import pprint
import os
import time

COMPONENT_METADATA_SETTINGS = "component_metadata.sublime-settings"
TOOLING_API_SETTINGS = "toolingapi.sublime-settings"

def get_toolingapi_settings():
    """
    Load all settings in toolingapi.sublime-settings

    @return: dict that contains all settings
    """

    # Load sublime-settings
    s = sublime.load_settings(TOOLING_API_SETTINGS)
    if not s.has("workspace"):
        sublime.error_message("""Before you start work, you should config your settings by 
            click [SublimeApex > Setting - Default]""")
        return

    settings = {}

    # User Settings Part
    settings["workspace"] = s.get("workspace") + "-" + time.strftime('%Y%m%d')
    settings["username"] = s.get("username")
    settings["password"] = s.get("password")
    login_url = s.get("login_url")
    settings["login_url"] = login_url
    settings["soap_login_url"] = login_url + "/services/Soap/u/v27.0"
    settings["login_url"] = s.get("login_url")

    # Trace Flag
    settings["trace_flag"] = s.get("trace_flag")

    # Workbook columns
    settings["workbook_field_describe_columns"] = s.get("workbook_field_describe_columns")
    settings["workflow_rule_columns"] = s.get("workflow_rule_columns")
    settings["workflow_field_update_columns"] = s.get("workflow_field_update_columns")
    settings["workflow_email_alert_columns"] = s.get("workflow_email_alert_columns")
    settings["workflow_task_columns"] = s.get("workflow_task_columns")
    settings["workflow_outbound_message_columns"] = s.get("workflow_outbound_message_columns")
    settings["validation_rule_columns"] = s.get("validation_rule_columns")

    # Populate all global variables
    component_types = []
    component_extensions = []
    component_outputdirs = []
    for component in s.get("components"):
        component_type = component["type"]
        component_types.append(component_type)
        component_extensions.append(component["extension"])

        component_outputdir = settings["workspace"] + "/" + component_type
        component_outputdirs.append(component_outputdir)

        # Combine soql
        component_body = component["body"]
        component_soql = "SELECT Id, Name, " + component_body +\
            " FROM " + component_type +\
            " WHERE NamespacePrefix = null ORDER BY Name"

        settings[component_type] =  {
            "body" : component["body"],
            "extension": component["extension"],
            "outputdir": component_outputdir,
            "soql": component_soql
        }

        settings[component["extension"]] = component_type

    settings["component_types"] = component_types
    settings["component_extensions"] = component_extensions
    settings["component_outputdirs"] = component_outputdirs

    return settings

def make_component(input):
    """
    According to user input, make the sample body

    @input: user input, for example,
        1. TestTrigger.trigger, sobject_name
        2. TestClass
        3. TestPage
        4. TestComponent
    """

    # Repace space in user input to empty
    input = input.replace(" ", "")

    # ApexClass, ApexComponent, ApexPage
    if "," not in input:
        component_name, component_extension = input.split(".")
        component_extension = "." + component_extension
        sobject_name = ""
    # If ApexTrigger
    else:
        component_name_extension, sobject_name =\
            input.split(",")[0].split("."), input.split(",")[1]
        component_name, component_extension =\
            component_name_extension[0], "." + component_name_extension[1]
    
    # judge whether component_extension is valid
    toolingapi_settings = get_toolingapi_settings()
    print (component_extension)
    print (toolingapi_settings["component_extensions"])
    if component_extension not in toolingapi_settings["component_extensions"]:
        return False, None, None

    # Get component_type and corresponding component outpudir
    component_type = toolingapi_settings[component_extension]
    component_outputdir = toolingapi_settings[component_type]["outputdir"]

    file_name = component_outputdir + "/" + component_name + component_extension

    # Write body to local file
    fp = open(file_name, "w")
    component_sample = get_component_sample(component_name, 
        component_type, sobject_name);

    # Write sample into new component
    fp.write(component_sample)

    return True, sobject_name, file_name

# Get component sample code by component_type
def get_component_sample(component_name, component_type, sobject_name):
    """
    Used in make_component function before

    @component_name: Trigger Name, Class Name...
    @component_type: ApexTrigger, ApexClass, ApexPage...
    @sobject_name: Sobject Name
    """
    metadata = {
        "ApexTrigger": "trigger " + component_name + " on " +\
            sobject_name + "(before insert) {\n    \n}",
        "ApexClass": "public class " + component_name + " {\n    \n}",
        "ApexPage": "<apex:page>\n    \n</apex:Page>",
        "ApexComponent": "<apex:component>\n    \n</apex:component>"
    }

    return metadata.get(component_type)

# According to component_types to create path under workspace
# After dir is made, save component_type_2_outputdir
def make_dir():
    """
    Load settings from toolingapi.sublime-settings and then create project directory

    @Return: No return
    """

    # Create Components Directory
    # I.E. d:/Tooling API/pro-exercise-20130416/ApexClass
    component_outputdirs = get_toolingapi_settings()["component_outputdirs"]
    for component_outputdir in component_outputdirs:
        if not os.path.exists(component_outputdir):
            os.makedirs(component_outputdir)
