import sublime
import sublime_plugin
import pprint
import os
import time

try:
    from .salesforce import message
except:
    from salesforce import message

COMPONENT_METADATA_SETTINGS = "component_metadata.sublime-settings"
TOOLING_API_SETTINGS = "toolingapi.sublime-settings"

def get_toolingapi_settings():
    """
    Load all settings in toolingapi.sublime-settings

    @return: dict that contains all settings
    """

    # Load sublime-settings
    s = sublime.load_settings(TOOLING_API_SETTINGS)
    settings = {}

    if not s.has("projects"):
        sublime.error_message("You should set your user credentials.")
        return

    projects = s.get("projects")

    default_project = None
    default_project_name = None
    for project_name in projects.keys():
        project_attr = projects[project_name]
        if project_attr["default"]: 
            default_project_name = project_name
            default_project = project_attr

    if default_project == None:
        sublime.error_message("You should has one default project at least. please check you settings.")
        return

    # Default Project Part
    settings["active_project"] = default_project
    settings["active_project_name"] = default_project_name

    # User Settings Part
    settings["projects"] = projects
    settings["workspace"] = s.get("workspace") + "/" + default_project_name + "-" + time.strftime('%Y%m%d')
    settings["username"] = default_project.get("username")
    settings["password"] = default_project["password"]
    if "security_token" in default_project:
        settings["security_token"] = default_project["security_token"]
    else:
        settings["security_token"] = ""

    login_url = default_project.get("login_url")
    settings["login_url"] = login_url
    settings["soap_login_url"] = login_url + "/services/Soap/u/v{0}.0".format(s.get("api_version", "28"))

    # This flag indicate whether output session id
    settings["output_session_info"] = s.get("output_session_info", False)

    # Indicate whether keep local change history
    settings["keep_local_change_history"] = s.get("keep_local_change_history", True)

    # The thread wait interval time
    settings["thread_sleep_time_of_waiting"] = s.get("thread_sleep_time_of_waiting", 0.05)

    # Trace Flag
    settings["trace_flag"] = s.get("trace_flag")

    # Trace Flag Headers
    settings["trace_flag_headers"] = s.get("trace_flag_headers")

    # Set API Version
    settings["api_version"] = s.get("api_version", "28")

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
        2. TestClass.cls
        3. TestPage.page
        4. TestComponent.component
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
    if component_extension not in toolingapi_settings["component_extensions"]:
        return False, None, None

    # Get component_type and corresponding component outpudir
    component_type = toolingapi_settings[component_extension]
    component_outputdir = toolingapi_settings[component_type]["outputdir"]

    if not os.path.exists(component_outputdir):
        os.makedirs(component_outputdir)
        add_project_to_workspace(toolingapi_settings["workspace"])

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

def switch_project(chosen_project):
    s = sublime.load_settings(TOOLING_API_SETTINGS)
    projects = s.get("projects")

    # Set the chosen project as default and others as not default
    for project in projects:
        project_attr = projects[project]
        if chosen_project == project:
            project_attr["default"] = True
        else:
            project_attr["default"] = False

    # Save the updated settings
    s.set("projects", projects)
    sublime.save_settings(TOOLING_API_SETTINGS)
    print (message.SEPRATE.format(chosen_project + " is the default project now."))

def add_project_to_workspace(workspace):
    """
    Add new project folder to workspace
    """

    try:
        # Just ST3 supports, ST2 is not
        project_data = sublime.active_window().project_data()
        folders = []
        if "folders" in project_data:
            folders = project_data["folders"]

        folders.append({
            "path": workspace
        })

        project_data["folders"] = folders
        sublime.active_window().set_project_data(project_data)
    except:
        pass