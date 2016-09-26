import sublime
import sublime_plugin
import os
import time
import json

from .salesforce.lib.panel import Printer

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
        Printer.get('error').write("You should have at least one default project - please, review your settings.")
        return

    # Default Project Part
    settings["usernames"] = usernames
    settings["default_project"] = default_project
    settings["default_project_name"] = default_project_name

    # User Settings Part
    settings["projects"] = projects

    # Workspace, if workspace is empty, set it as <package_path>/User/HaoIDE
    workspace = default_project["workspace"] if "workspace" in default_project else s.get("workspace")
    if not workspace:
        workspace = os.path.join(sublime.packages_path(), "User", "HaoIDE")

    project_name = default_project_name + ("-" + time.strftime('%Y%m%d') if s.get("keep_project_name_time_suffix") else "")
    settings["keep_project_name_time_suffix"] = s.get("keep_project_name_time_suffix", True)
    settings["workspace"] = workspace + "/" + project_name
    settings["file_exclude_patterns"] = s.get("file_exclude_patterns", [])
    settings["folder_exclude_patterns"] = s.get("folder_exclude_patterns", [])
    settings["username"] = default_project.get("username")
    settings["password"] = default_project["password"]
    if "security_token" in default_project:
        settings["security_token"] = default_project["security_token"]
    else:
        settings["security_token"] = ""

    # Get the default api version
    api_version = default_project.get("api_version")
    if not api_version:
        api_version = s.get("api_version", 37)

    # Set deploy options
    deploy_options = default_project.get("deploy_options")
    if not deploy_options:
        deploy_options = s.get("deploy_options")
    settings["deploy_options"] = deploy_options

    login_url = default_project.get("login_url")
    settings["login_url"] = login_url
    settings["soap_login_url"] = login_url + "/services/Soap/u/v{0}.0".format(api_version)

    # Indicate whether keep local change history
    settings["keep_local_change_history"] = s.get("keep_local_change_history", True)

    # Login again every n minutes as below
    settings["force_login_interval"] = s.get("force_login_interval", 120)

    # Automatically update change to server when save file
    settings["auto_update_on_save"] = s.get("auto_update_on_save", False)

    # Indicate whether need confirmation for save operation
    settings["confirm_on_save"] = s.get("confirm_on_save", False)

    # Check whether the LastModifiedById is current user
    settings["check_save_conflict"] = s.get("check_save_conflict", True)

    # After component save succeed, flag for controlling whether track debug log for running user
    settings["track_log_after_saved"] = s.get("track_log_after_saved", False);

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
    settings["api_version"] = api_version

    # Browser Path
    settings["default_chrome_path"] = s.get("default_chrome_path")

    # Indicate whether keep history to local
    settings["keep_operation_history"] = s.get("keep_operation_history", True)

    # Debug Mode
    settings["debug_mode"] = s.get("debug_mode", False)

    # Content Types
    settings["content_types"] = s.get("content_types", [])

    # Indicate whether switch project back to original 
    # after `deploy` or `retrieve from other server` is executed
    settings["switch_back_after_migration"] = s.get("switch_back_after_migration", True)

    # Completions Part
    settings["disable_fields_completion"] = s.get("disable_fields_completion", False)
    settings["disable_keyword_completion"] = s.get("disable_keyword_completion", False)
    settings["disable_picklist_value_completion"] = s.get("disable_picklist_value_completion", False)
    settings["disable_relationship_completion"] = s.get("disable_relationship_completion", False)
    settings["disable_soql_field_completion"] = s.get("disable_soql_field_completion", False)
    settings["display_field_name_and_label"] = s.get("display_field_name_and_label", True)
    settings["disable_html_completion"] = s.get("disable_html_completion", True)
    settings["disable_bootstrap_completion"] = s.get("disable_bootstrap_completion", False)
    settings["disable_custom_component_completion"] = s.get("disable_custom_component_completion", False)
    settings["disable_component_attribute_completion"] = s.get("disable_component_attribute_completion", False)
    settings["disable_component_attribute_value_completion"] = s.get("disable_component_attribute_value_completion", False)
    settings["disable_apex_completion_in_visualforce"] = s.get("disable_apex_completion_in_visualforce", False)

    # Bulk Api batch size and batch bytes
    settings["maximum_batch_size"] = s.get("maximum_batch_size", 10000)
    settings["maximum_batch_bytes"] = s.get("maximum_batch_bytes", 100000)

    # Log Levels of Anonymous Code
    settings["anonymous_log_levels"] = s.get("anonymous_log_levels")

    # Settings for controlling action when file is activated
    settings["auto_switch_project_on_file_activated"] = s.get("auto_switch_project_on_file_activated", True)
    settings["reveal_file_in_sidebar_on_file_activated"] = s.get("reveal_file_in_sidebar_on_file_activated", True)

    # Workbook columns
    settings["workbook_field_describe_columns"] = s.get("workbook_field_describe_columns")
    settings["workflow_rule_columns"] = s.get("workflow_rule_columns")
    settings["workflow_field_update_columns"] = s.get("workflow_field_update_columns")
    settings["workflow_email_alert_columns"] = s.get("workflow_email_alert_columns")
    settings["workflow_task_columns"] = s.get("workflow_task_columns")
    settings["workflow_outbound_message_columns"] = s.get("workflow_outbound_message_columns")
    settings["validation_rule_columns"] = s.get("validation_rule_columns")

    # Indicate whether include users in role when export role hierarchy
    settings["include_users_in_role_hierarchy"] = s.get("include_users_in_role_hierarchy", True)

    # Indicate whether automatically remove slash in the response 
    # when execute REST Test
    settings["remove_slash_for_rest_response"] = s.get("remove_slash_for_rest_response", False)

    # Set the polling interval for checking metadata job status
    settings["metadata_polling_frequency"] = s.get("metadata_polling_frequency", 1)
    
    # Document Reference Attrs
    settings["docs"] = s.get("docs", {})

    # Parse the allowed packages SOQL expression
    allowed_packages = []
    if "allowed_packages" in settings["default_project"]:
        allowed_packages = settings["default_project"]["allowed_packages"]

    settings["allowed_packages"] = allowed_packages
    settings["all_metadata_folders"] = []
    settings["all_metadata_objects"] = []
    
    # Populate all metadata_objects settings
    # 1. Check `metadata_objects`` setting in project
    if "subscribed_metadata_objects" in default_project:
        settings["subscribed_metadata_objects"] = default_project["subscribed_metadata_objects"]
    else:
        settings["subscribed_metadata_objects"] = []

    # 2. Check `.config/metadata_objects.json`, priority of 1 is higher than 2
    cache_file = os.path.join(
        settings["workspace"], ".config", "metadata.json"
    )
    described_metadata = None
    if os.path.isfile(cache_file):
        with open(cache_file) as fp:
            described_metadata = json.loads(fp.read())
    if described_metadata and "metadataObjects" in described_metadata:
        settings = build_metadata_objects_settings(settings, described_metadata["metadataObjects"])
        settings["organizationNamespace"] = described_metadata["organizationNamespace"]

    return settings

def get_setting(key):
    return get_settings().get(key)

def get_default_project_name():
    s = sublime.load_settings("toolingapi.sublime-settings")
    projects = s.get("projects")

    default_project_name = None
    for project_name in projects.keys():
        if projects[project_name]["default"]: 
            default_project_name = project_name
            break

    return default_project_name

def build_metadata_objects_settings(settings, metadata_objects):
    settings["all_metadata_folders"] = [c["directoryName"] for c in metadata_objects]
    settings["all_metadata_objects"] = [c["xmlName"] for c in metadata_objects]
    settings["subscribed_metadata_folders"] = [c["directoryName"] for c in metadata_objects \
        if c["xmlName"] in settings["subscribed_metadata_objects"]]
    settings["metadata_objects_in_folder"] = [c["xmlName"] for c in metadata_objects \
        if c["inFolder"] == "true"]
    for mo in metadata_objects:
        settings[mo["xmlName"]] = mo
        settings[mo["directoryName"]] = mo

        if "childXmlNames" in mo:
            childXmlNames = mo["childXmlNames"]
            if isinstance(childXmlNames, str):
                childXmlNames = [childXmlNames]
            
            mcopy = mo.copy(); del mcopy["childXmlNames"]
            for child in childXmlNames:
                settings[child] = mcopy

    return settings