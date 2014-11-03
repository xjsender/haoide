import sublime
import sublime_plugin
import os
import time

COMPONENT_METADATA_SETTINGS = "component_metadata.sublime-settings"
TOOLING_API_SETTINGS = "toolingapi.sublime-settings"

def get_settings():
    """ Load all settings in toolingapi.sublime-settings

    @return: dict that contains all settings
    """

    # Used for keeping all settings
    settings = {}

    # Load sublime-settings
    s = sublime.load_settings("toolingapi.sublime-settings")
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
    settings["file_exclude_patterns"] = s.get("file_exclude_patterns", [])
    settings["folder_exclude_patterns"] = s.get("folder_exclude_patterns", [])
    settings["username"] = default_project.get("username")
    settings["password"] = default_project["password"]
    if "security_token" in default_project:
        settings["security_token"] = default_project["security_token"]
    else:
        settings["security_token"] = ""

    login_url = default_project.get("login_url")
    settings["login_url"] = login_url
    settings["soap_login_url"] = login_url + "/services/Soap/u/v{0}.0".format(s.get("api_version", "29"))

    # Indicate whether keep local change history
    settings["keep_local_change_history"] = s.get("keep_local_change_history", True)

    # Check whether the LastModifiedById is current user
    settings["check_save_conflict"] = s.get("check_save_conflict", True)

    # Trace Flag
    settings["trace_flag"] = s.get("trace_flag")
    settings["last_n_logs"] = s.get("last_n_logs", 10)

    # User Language
    settings["user_language"] = s.get("user_language")

    # Setting for controlling maximum concurrent connections with salesforce
    settings["maximum_concurrent_connections"] = s.get("maximum_concurrent_connections", 999)

    # Every time when you save component and error happened, the console will be open.
    # When you edit the code according to the error message, this flag used to indicate
    # whether the console will be hidden automatically
    settings["hidden_console_on_modify"] = s.get("hidden_console_on_modify", True)

    # Every time when you save component and succeed, the output panel will be open.
    # however, you want it to be hidden automatically after several seconds
    settings["delay_seconds_for_hidden_output_panel_when_succeed"] =\
        s.get("delay_seconds_for_hidden_output_panel_when_succeed", 1)

    # Indicate whether need to reload symbol tables when creating new project
    settings["reload_symbol_tables_when_create_project"] =\
        s.get("reload_symbol_tables_when_create_project", True)

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
    
    # Document Reference Attrs
    settings["docs"] = s.get("docs", {})

    # Parse the allowed packages SOQL expression
    if "allowed_packages" in settings["default_project"]:
        allowed_packages = settings["default_project"]["allowed_packages"]
    else:
        allowed_packages = []

    settings["allowed_packages"] = allowed_packages
    
    # Populate all global variables
    components = s.get("components")
    settings["meta_types"] = [c["type"] for c in components]
    settings["meta_folders"] = [c["folder"] for c in components]
    settings["subscribed_meta_types"] = [c["type"] for c in components if c["subscribe"]]
    settings["subscribed_meta_folders"] = [c["folder"] for c in components if c["subscribe"]]
    for component in components:
        settings[component["type"]] = component
        settings[component["folder"]] = component

    return settings