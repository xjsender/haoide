import sublime
import sublime_plugin
import os
import time

from .salesforce import message

COMPONENT_METADATA_SETTINGS = "component_metadata.sublime-settings"
TOOLING_API_SETTINGS = "toolingapi.sublime-settings"

def get_settings():
    """ Load all settings in toolingapi.sublime-settings

    @return: dict that contains all settings
    """

    # Used for keeping all settings
    settings = {}

    # Load sublime-settings
    s = sublime.load_settings(TOOLING_API_SETTINGS)
    projects = s.get("projects")

    default_project = None
    default_project_name = None
    usernames = []
    for project_name in projects.keys():
        project_attr = projects[project_name]
        if project_attr["default"]: 
            default_project_name = project_name
            default_project = project_attr
            default_project["project_name"] = default_project_name
        else:
            usernames.append(project_attr["username"])

    if not default_project:
        sublime.error_message("You should have at least one default project - please, review your settings.")
        return

    # Default Project Part
    settings["usernames"] = usernames
    settings["default_project"] = default_project
    settings["default_project_name"] = default_project_name

    # User Settings Part
    settings["projects"] = projects
    workspace = s.get("workspace") + "/" + default_project_name +\
        ("-" + time.strftime('%Y%m%d') if s.get("keep_project_name_time_suffix") else "")
    settings["workspace"] = workspace
    settings["username"] = default_project.get("username")
    settings["password"] = default_project["password"]
    if "security_token" in default_project:
        settings["security_token"] = default_project["security_token"]
    else:
        settings["security_token"] = ""

    login_url = default_project.get("login_url")
    settings["login_url"] = login_url
    settings["soap_login_url"] = login_url + "/services/Soap/u/v{0}.0".format(s.get("api_version", "29"))

    # This flag indicate whether output session id
    settings["output_session_info"] = s.get("output_session_info", False)

    # Indicate whether keep local change history
    settings["keep_local_change_history"] = s.get("keep_local_change_history", True)

    # Check whether the LastModifiedById is current user
    settings["check_save_conflict"] = s.get("check_save_conflict", True)

    # Trace Flag
    settings["trace_flag"] = s.get("trace_flag")
    settings["last_n_logs"] = s.get("last_n_logs", 10)

    # User Language
    settings["user_language"] = s.get("user_language")

    # Every time when you save component and error happened, the console will be open.
    # When you edit the code according to the error message, this flag used to indicate
    # whether the console will be hidden automatically
    settings["hidden_console_on_modify"] = s.get("hidden_console_on_modify", True)

    # Every time when you save component and error happened, the console will be open.
    # however, you want it to be hidden automatically after several seconds
    settings["delay_seconds_for_hidden_output_panel_when_failed"] =\
        s.get("delay_seconds_for_hidden_output_panel_when_failed", 6)

    # Every time when you save component and succeed, the output panel will be open.
    # however, you want it to be hidden automatically after several seconds
    settings["delay_seconds_for_hidden_output_panel_when_succeed"] =\
        s.get("delay_seconds_for_hidden_output_panel_when_succeed", 1)

    # Indicate whether download StaticResource body, it is very time-consuming.
    # If you open this functionality and your StaticResources are very large
    # It may stop your work
    settings["get_static_resource_body"] = s.get("get_static_resource_body", True)

    # Set API Version
    settings["api_version"] = s.get("api_version", "28")

    # Browser Path
    settings["default_chrome_path"] = s.get("default_chrome_path")

    # Indicate whether keep history to local
    settings["keep_operation_history"] = s.get("keep_operation_history", True)

    # Indicate whether keep history to local
    settings["keep_config_history"] = s.get("keep_config_history", True)

    # Completions Part
    settings["disable_fields_completion"] = s.get("disable_fields_completion", False)
    settings["disable_keyword_completion"] = s.get("disable_keyword_completion", False)
    settings["disable_picklist_value_completion"] = s.get("disable_picklist_value_completion", False)
    settings["disable_relationship_completion"] = s.get("disable_relationship_completion", False)
    settings["disable_soql_field_completion"] = s.get("disable_soql_field_completion", False)
    settings["display_field_name_and_label"] = s.get("display_field_name_and_label", True)
    settings["allowed_sobjects"] = s.get("allowed_sobjects", [])

    # Bulk Api batch size and batch bytes
    settings["maximum_batch_size"] = s.get("maximum_batch_size", 10000)
    settings["maximum_batch_bytes"] = s.get("maximum_batch_bytes", 100000)

    # Log Levels of Anonymous Code
    settings["anonymous_log_levels"] = s.get("anonymous_log_levels")

    # Deploy Option
    settings["deploy_options"] = s.get("deploy_options")

    # Workbook columns
    settings["workbook_field_describe_columns"] = s.get("workbook_field_describe_columns")
    settings["workflow_rule_columns"] = s.get("workflow_rule_columns")
    settings["workflow_field_update_columns"] = s.get("workflow_field_update_columns")
    settings["workflow_email_alert_columns"] = s.get("workflow_email_alert_columns")
    settings["workflow_task_columns"] = s.get("workflow_task_columns")
    settings["workflow_outbound_message_columns"] = s.get("workflow_outbound_message_columns")
    settings["validation_rule_columns"] = s.get("validation_rule_columns")

    # Combine the allowed packages SOQL expression
    allowed_packages = s.get("allowed_packages", [])
    allowed_packages_soql = '('
    for pa in allowed_packages:
        allowed_packages_soql += "'%s'" % pa + ","
    allowed_packages_soql = allowed_packages_soql[:-1] + ")"
    
    # Document Reference Attrs
    settings["docs"] = s.get("docs", {})

    # Proxy
    settings["proxies"] = s.get("proxies", {})

    # Populate all global variables
    components = s.get("components")
    for component_type in components:
        component_attribute = components[component_type]

        # Combine soql
        component_soql = "SELECT Id, Name, " + component_attribute["body"] +\
            (", ContentType" if component_type == "StaticResource" else "") +\
            " FROM " + component_type +\
            " WHERE NamespacePrefix = null " +\
            (" OR NamespacePrefix in " + allowed_packages_soql if allowed_packages else "") +\
            " ORDER BY Name"

        component_attribute["soql"] = component_soql
        component_attribute["outputdir"] = workspace + "/" + component_attribute["folder"]
        settings[component_type] = component_attribute
        settings[component_attribute["extension"]] = component_type
        settings[component_attribute["folder"]] = component_type

    settings["component_types"] = list(components.keys())
    settings["component_folders"] = [components[ct]["folder"] for ct in components]
    settings["component_extensions"] = [components[ct]["extension"] for ct in components]
    settings["component_outputdirs"] = [workspace + "/" + components[ct]["folder"] for ct in components]

    return settings

def make_dir():
    """
    Load settings from toolingapi.sublime-settings and then create project directory

    @Return: No return
    """

    # Create Components Directory
    # I.E. d:/Tooling API/pro-exercise-20130416/ApexClass
    component_outputdirs = get_settings()["component_outputdirs"]
    for component_outputdir in component_outputdirs:
        if not os.path.exists(component_outputdir):
            os.makedirs(component_outputdir)

def display_active_project(view):
    settings = get_settings()
    display_message = "Default Project => " + settings["default_project_name"]
    view.set_status('default_project', display_message)

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

    # Set all active views status with "default project"
    for view in sublime.active_window().views():
        display_active_project(view)

def add_project_to_workspace(workspace):
    """
    Add new project folder to workspace
    """

    # Just ST3 supports, ST2 is not
    project_data = sublime.active_window().project_data()
    if not project_data: project_data = {}
    folders = []
    if "folders" in project_data:
        folders = project_data["folders"]

    folders.append({
        "path": workspace
    })

    project_data["folders"] = folders
    sublime.active_window().set_project_data(project_data)
