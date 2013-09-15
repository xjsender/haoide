import sublime
import sublime_plugin
import webbrowser
import urllib
import re
import os
import sys
import shutil
import zipfile

try:
    # Python 3.x
    from . import requests
    from . import processor
    from . import context
    from .salesforce import util, message
    from .salesforce import bulkapi
except:
    # Python 2.x
    import requests
    import processor
    import context
    from salesforce import util, message, bulkapi

class SetCheckPointCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        mark = [s for s in self.view.sel()]
        self.view.add_regions("mark", mark, "red", 'circle',
            sublime.DRAW_NO_FILL | sublime.DRAW_NO_OUTLINE | sublime.DRAW_STIPPLED_UNDERLINE)

class RemoveCheckPointCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.erase_regions('mark')

class ViewCodeCoverageCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Get file_name and component_attribute
        file_name = self.view.file_name()
        component_attribute, component_name = get_component_attribute(file_name)

        # Read file content
        try:
            body = open(file_name, encoding="utf-8").read()
        except:
            body = open(file_name).read()

        # Open Console
        self.view.window().run_command("show_panel", 
            {"panel": "console", "toggle": False})

        # Handle Save Current Component
        processor.handle_view_code_coverage(component_name, component_attribute, body)

    def is_enabled(self):
        return check_enabled(self.view.file_name())

class SwitchProjectCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(SwitchProjectCommand, self).__init__(*args, **kwargs)

    def run(self):
        global projects
        toolingapi_settings = context.get_toolingapi_settings()
        projects = toolingapi_settings["projects"]
        projects = ["(" + ('Active' if projects[p]["default"] else 'Inactive') + ") " + p for p in projects]
        projects = sorted(projects, reverse=False)
        self.window.show_quick_panel(projects, self.on_done)

    def on_done(self, index):
        if index == -1: return

        # Change the chosen project as default
        # Split with ") " and get the second project name
        default_project = projects[index].split(") ")[1]
        context.switch_project(default_project)

class NewViewCommand(sublime_plugin.TextCommand):
    """
    Create a new view with specified input

    @input: user specified input

    Usage: 
        sublime.active_window().run_command("new_view", {
            "name": "ViewName",
            "input": "Example"
        })
    """

    def run(self, edit, name="", input=""):
        view = sublime.active_window().active_view()
        view.set_scratch(True)
        view.set_name(name)
        view.insert(edit, 0, input)

class RefreshFolderCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RefreshFolderCommand, self).__init__(*args, **kwargs)

    def run(self):
        global component_types
        toolingapi_settings = context.get_toolingapi_settings()
        component_types = toolingapi_settings["component_types"]
        self.window.show_quick_panel(component_types, self.on_done)

    def on_done(self, index):
        if index == -1: return

        # Open Console
        self.window.run_command("show_panel", 
            {"panel": "console", "toggle": False})

        processor.handle_refresh_folder(component_types[index])

class RetrieveMetadataCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RetrieveMetadataCommand, self).__init__(*args, **kwargs)

    def run(self):
        # Open Console
        self.window.run_command("show_panel", 
            {"panel": "console", "toggle": False})

        processor.handle_retrieve_all_thread()
        
class ExportValidationRulesCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportValidationRulesCommand, self).__init__(*args, **kwargs)

    def run(self):
        toolingapi_settings = context.get_toolingapi_settings()
        workflow_path = toolingapi_settings["workspace"] + "/metadata/unpackaged/objects"
        if not os.path.exists(workflow_path):
            sublime.error_message(message.SOBJECTS_PATH_CHECK)
            return

        # Open Console
        self.window.run_command("show_panel", 
            {"panel": "console", "toggle": False})

        processor.handle_parse_validation_rule()

class ExportWorkflowsCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportWorkflowsCommand, self).__init__(*args, **kwargs)

    def run(self):
        toolingapi_settings = context.get_toolingapi_settings()
        workflow_path = toolingapi_settings["workspace"] + "/metadata/unpackaged/workflows"
        if not os.path.exists(workflow_path):
            sublime.error_message(message.WORKFLOW_PATH_CHECK)
            return

        self.window.run_command("show_panel", 
            {"panel": "console", "toggle": False})

        processor.handle_parse_workflow()

class DescribeCustomFieldCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DescribeCustomFieldCommand, self).__init__(*args, **kwargs)

    def run(self):
        global sobjects
        sobjects = processor.populate_sobjects()
        sobjects = sorted(sobjects)
        self.window.show_quick_panel(sobjects, self.on_done)

    def on_done(self, index):
        if index == -1: return
        processor.handle_describe_customfield(sobjects[index])
        
class DescribeGlobalCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DescribeGlobalCommand, self).__init__(*args, **kwargs)

    def run(self):
        processor.handle_describe_global()

class DescribeLayoutCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DescribeLayoutCommand, self).__init__(*args, **kwargs)

    def run(self):
        global sobject_recordtypes_attr
        global sobject_recordtypes
        sobject_recordtypes_attr = processor.populate_sobject_recordtypes()
        sobject_recordtypes = sorted(list(sobject_recordtypes_attr.keys()))

        self.window.show_quick_panel(sobject_recordtypes, self.on_done)

    def on_done(self, index):
        if index == -1: return

        # Open Console
        self.window.run_command("show_panel", 
            {"panel": "console", "toggle": False})

        # Get chosen item, sobject name and recordtype id
        sobject_recordtype = sobject_recordtypes[index]
        sobject = sobject_recordtype.split(",")[0].strip()
        recordtype_name = sobject_recordtype.split(",")[1].strip()
        recordtype_id = sobject_recordtypes_attr[sobject_recordtype]

        # handle this describe requst
        print (sobject, recordtype_id)
        processor.handle_describe_layout(sobject, recordtype_name, recordtype_id)

class BackupSobjectsCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(BackupSobjectsCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.window.show_input_panel("Sobjects(* means all, or sobjects seprated with semi-colon)", 
            "*", self.on_input, None, None)

    def on_input(self, input):
        # Open Console
        self.window.run_command("show_panel", 
            {"panel": "console", "toggle": False})

        # Display the fields in a new view
        input = input.replace(" ", "")

        if input == "*":
            processor.handle_backup_all_sobjects(5)
        else:
            sobjects = input.split(";")
            bulkapi.handle_bulkapi_query(sobjects)

class DescribeSobjectCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DescribeSobjectCommand, self).__init__(*args, **kwargs)

    def run(self):
        global sobjects
        sobjects = processor.populate_sobjects()
        sobjects = sorted(sobjects)
        self.window.show_quick_panel(sobjects, self.on_done)

    def on_done(self, index):
        if index == -1: return
        processor.handle_describe_sobject(sobjects[index])

class ExportWorkbookCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportWorkbookCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.window.show_input_panel("Sobjects(* means all, or sobjects seprated with semi-colon)", 
            "*", self.on_input, None, None)

    def on_input(self, input):
        # Open Console
        self.window.run_command("show_panel", 
            {"panel": "console", "toggle": False})

        # Display the fields in a new view
        input = input.replace(" ", "")

        if input == "*":
            processor.handle_generate_all_workbooks(5)
        else:
            sobjects = input.split(";")
            processor.handle_generate_specified_workbooks(sobjects)

class ViewComponentInSfdcCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ViewComponentInSfdcCommand, self).__init__(*args, **kwargs)

    def run(self):
        global all_components
        global all_components_name

        all_components = processor.populate_components()

        if len(all_components) == 0:
            sublime.message_dialog("Please click 'New Project' Firstly.")
            return

        all_components_name = sorted(list(all_components.keys()))
        self.window.show_quick_panel(all_components_name, self.on_done)

    def on_done(self, index):
        if index == -1: return

        # Open Console
        self.window.run_command("show_panel", 
            {"panel": "console", "toggle": False})

        class_id = all_components[all_components_name[index]]
        startURL = "/" + class_id
        self.window.run_command("login_to_sfdc", {"startURL": startURL})

class RunOneTestCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RunOneTestCommand, self).__init__(*args, **kwargs)

    def run(self):
        global classes_attr
        global class_names

        classes_attr = processor.populate_classes()
        classes = classes_attr.keys()
        classes = [c for c in classes if "is_test" in classes_attr[c] and classes_attr[c]["is_test"]]
        class_names = sorted(list(classes))
        self.window.show_quick_panel(class_names, self.on_done)

    def on_done(self, index):
        if index == -1: return

        # Open Console
        self.window.run_command("show_panel", 
            {"panel": "console", "toggle": False})

        class_id = classes_attr[class_names[index]]["id"]
        processor.handle_run_test(class_id)

class RunTestCommand(sublime_plugin.TextCommand):
    def run(self, view):
        # Open Console
        self.view.window().run_command("show_panel", 
            {"panel": "console", "toggle": False})

        # Get component_attribute by file_name
        component_attribute = get_component_attribute(self.view.file_name())[0]

        # Process run test
        processor.handle_run_test(component_attribute["id"])

    def is_enabled(self):
        # Get current file name and Read file content
        file_name = self.view.file_name()
        if file_name == None: return False
        try:
            # Python 3.x
            body = open(file_name, encoding="utf-8").read()
        except:
            # Python 2.x
            body = open(file_name).read().encode()

        if ".cls" not in file_name or "@isTest" not in body:
            return False

        return True

class CreateDebugLogCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateDebugLogCommand, self).__init__(*args, **kwargs)

    def run(self):
        global users
        global users_name
        users = processor.populate_users()
        users_name = sorted(users.keys(), reverse=False)
        self.window.show_quick_panel(users_name, self.on_done)

    def on_done(self, index):
        if index == -1: return

        # Change the chosen project as default
        # Split with ") " and get the second project name
        user_name = users_name[index]
        user_id = users[user_name]
        sublime.active_window().run_command("show_panel", 
            {"panel": "console", "toggle": False})
        processor.handle_create_debug_log(user_id, user_name)

class ListDebugLogsCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ListDebugLogsCommand, self).__init__(*args, **kwargs)

    def run(self):
        # Open Console
        sublime.active_window().run_command("show_panel", 
            {"panel": "console", "toggle": False})

        global users
        global users_name
        users = processor.populate_users()
        users_name = sorted(users.keys(), reverse=False)
        self.window.show_quick_panel(users_name, self.on_done)

    def on_done(self, index):
        if index == -1: return

        # Change the chosen project as default
        # Split with ") " and get the second project name
        user_id = users[users_name[index]]
        sublime.active_window().run_command("show_panel", 
            {"panel": "console", "toggle": False})
        processor.handle_list_debug_logs(user_id)

class ViewDebugLogDetail(sublime_plugin.TextCommand):
    def run(self, view):
        # Open Console
        self.view.window().run_command("show_panel", 
            {"panel": "console", "toggle": False})

        processor.handle_get_debug_log_detail(self.log_id)

    def is_visible(self):
        # Choose the valid Id, you will see this command
        if util.is_python3x():
            self.log_id = self.view.substr(self.view.sel()[0])
        else:
            self.log_id = self.view.substr(self.view.sel()[0]).encode("utf-8")

        if len(self.log_id) != 15 and len(self.log_id) != 18: return False
        if not re.compile(r'^[a-zA-Z0-9]*$').match(self.log_id): return False
        if not self.log_id.startswith("07L"): return False

        return True

class ExecuteSoqlCommand(sublime_plugin.TextCommand):
    def run(self, view):
        # Open Console
        self.view.window().run_command("show_panel", 
            {"panel": "console", "toggle": False})

        # Handle
        processor.handle_execute_query(self.selection)

    def is_enabled(self):
        # Selection must start SELECT, 
        # otherwise you can't see this command
        self.selection = self.view.substr(self.view.sel()[0]).encode('utf-8')

        if not self.selection or not self.selection.upper().startswith(b"SELECT"):
            return False

        return True

class ExecuteAnonymousCommand(sublime_plugin.TextCommand):
    def run(self, view):
        # Open Console
        self.view.window().run_command("show_panel", 
            {"panel": "console", "toggle": False})

        # Handle
        processor.handle_execute_anonymous(self.selection)

    def is_enabled(self):
        # You must select some snippets, otherwise
        # you can't see this command
        self.selection = self.view.substr(self.view.sel()[0])
        if not util.is_python3x():
            self.selection = self.view.substr(self.view.sel()[0]).encode('utf-8')
        
        if not self.selection:
            return False

        return True

class ViewIdInSfdcWebCommand(sublime_plugin.TextCommand):
    def run(self, view):
        startURL = "/" + self.record_id
        if self.record_id.startswith("012"):
            startURL = "/setup/ui/recordtypefields.jsp?id=" + self.record_id

        if self.record_id.startswith("07L"):
            startURL = "/p/setup/layout/ApexDebugLogDetailEdit/d?apex_log_id=" + self.record_id
        
        self.view.window().run_command("login_to_sfdc", {"startURL": startURL})

    def is_enabled(self):
        # Choose the valid Id, you will see this command
        if util.is_python3x():
            self.record_id = self.view.substr(self.view.sel()[0])
        else:
            self.record_id = self.view.substr(self.view.sel()[0]).encode("utf-8")
            
        if len(self.record_id) != 15 and len(self.record_id) != 18:
            return False

        if not re.compile(r'^[a-zA-Z0-9]*$').match(self.record_id):
            return False

        return True

class ShowInSfdcWebCommand(sublime_plugin.TextCommand):
    def run(self, view):
        # Get file_name and component_attribute
        component_attribute = get_component_attribute(self.view.file_name())[0]

        # Open this component in salesforce web
        startURL = "/" + component_attribute["id"]
        self.view.window().run_command("login_to_sfdc", {"startURL": startURL})

    def is_enabled(self):
        return check_enabled(self.view.file_name())

class LoginToSfdcCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(LoginToSfdcCommand, self).__init__(*args, **kwargs)

    def run(self, startURL=""):
        # Get toolingapi settings
        toolingapi_settings = context.get_toolingapi_settings()

        # Combine Login URL
        show_params = {
            "un": toolingapi_settings["username"],
            "pw": toolingapi_settings["password"],
            "startURL": startURL
        }

        if util.is_python3x():
            show_params = urllib.parse.urlencode(show_params)
        else:
            show_params = urllib.urlencode(show_params)

        show_url = toolingapi_settings["login_url"] + '?%s' % show_params

        # Open this component in salesforce web
        webbrowser.open_new_tab(show_url)

class AboutCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(AboutCommand, self).__init__(*args, **kwargs)

    def run(self): 
        webbrowser.open_new_tab("https://github.com/xjsender/SublimeApex")

class DeleteSelectedComponentsCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DeleteSelectedComponentsCommand, self).__init__(*args, **kwargs)

    def run(self, files):
        delete_components(files)

    def is_enabled(self, files):
        """
        1. You must have selected one file or more
        2. All selected file should be visible
        """

        if len(files) == 0: return False
        for file in files:
            if not check_enabled(file):
                return False

        return True

class DeleteComponentCommand(sublime_plugin.TextCommand):
    def run(self, view):
        # Get file_name and component_attribute
        files = []
        files.append(self.view.file_name());
        delete_components(files)

    def is_enabled(self):
        return check_enabled(self.view.file_name())

def delete_components(files):
    # Confirm Delete Action
    confirm = sublime.ok_cancel_dialog(message.DELETE_CONFIRM_MESSAGE)
    if confirm == False: return
    
    # Handle Delete
    for f in files:
        component_attribute = get_component_attribute(f)[0]
        processor.handle_delete_component(component_attribute["url"], f)

class CreateComponentCommand(sublime_plugin.WindowCommand):
    """
    user input, for example,
        1. TestTrigger.trigger, sobject_name
        2. TestClass.cls
        3. TestPage.page
        4. TestComponent.component
    """

    def __init__(self, *args, **kwargs):
        super(CreateComponentCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.window.show_input_panel("Follow [Name.trigger,Sobject | Name.page | Name.cls | Name.component]", 
            "", self.on_input, None, None)

    def on_input(self, input):
        # Valid user input
        if "." not in input:
            sublime.error_message(message.INVALID_NEW_COMPONENT_FORMAT)
            return

        # Get toolingapi settings
        toolingapi_settings = context.get_toolingapi_settings()

        # Create component to local according to user input
        is_success, sobject_name, file_name = context.make_component(input)
        if is_success == False:
            sublime.error_message(message.INVALID_NEW_COMPONENT_FORMAT)
            return

        # Open Console
        self.window.run_command("show_panel", 
            {"panel": "console", "toggle": False})

        self.window.open_file(file_name)

        # Before you save it to server, save it to local
        self.view = self.window.active_view()
        if self.view.is_dirty():
            self.view.run_command("save")

        # Get Current File Name
        file_name = self.view.file_name()
        print(file_name)

        # Read file content
        body = open(file_name).read()
        
        # Get component type and component_name (Class Name, Trigger Name, etc.)
        component_name = util.get_component_name(file_name)
        component_type = util.get_component_type(file_name)

        # There has bug on creating ApexTrigger, but fixed on 2013 May 6 at 21:
        # Create Trigger is different from others, we can't use tooling/sobjects/ApexTrigger,
        # We should use sobjects/ApexTrigger
        # http://salesforce.stackexchange.com/questions/9603/how-do-i-use-the-tooling-api-to-create-a-new-apex-trigger
        # If component type is not in range, just show error message
        if component_type not in toolingapi_settings["component_types"]:
            sublime.error_message(message.INVALID_COMPONENT)
            return

        # Get Component body Metadata Attribute in SFDC
        component_body = toolingapi_settings[component_type]["body"]

        # Compose data
        data = {
            "name": component_name,
            component_body: body,
        }
        if component_type == "ApexClass":
            data["IsValid"] = True
        elif component_type == "ApexTrigger":
            data["TableEnumOrId"] = sobject_name
        elif component_type in ["ApexPage", "ApexComponent"]:
            data["MasterLabel"] = component_name

        processor.handle_create_component(data, component_name, component_type)

class SaveComponentCommand(sublime_plugin.TextCommand):
    def run(self, view):
        # Automatically save current file if dirty
        if self.view.is_dirty():
            self.view.run_command("save")
            
        # Get file_name and component_attribute
        file_name = self.view.file_name()
        component_attribute, component_name = get_component_attribute(file_name)

        # Read file content
        try:
            body = open(file_name, encoding="utf-8").read()
        except:
            body = open(file_name).read()

        # Open Console
        self.view.window().run_command("show_panel", 
            {"panel": "console", "toggle": False})

        # Handle Save Current Component
        processor.handle_save_component(component_name, component_attribute, body)

    def is_enabled(self):
        return check_enabled(self.view.file_name())

class NewProjectCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(NewProjectCommand, self).__init__(*args, **kwargs)

    def run(self): 
        # Create Project Directory
        context.make_dir()

        # Get toolingapi_settings
        toolingapi_settings = context.get_toolingapi_settings()
        context.add_project_to_workspace(toolingapi_settings["workspace"])

        # Open Console
        self.window.run_command("show_panel", 
            {"panel": "console", "toggle": False})

        # Handle Refresh All
        processor.handle_refresh_components(toolingapi_settings)

class RefreshComponentCommand(sublime_plugin.TextCommand):
    def run(self, view):
        # Get file_name and component_attribute
        file_name = self.view.file_name()
        component_attribute = get_component_attribute(file_name)[0]
        
        # Handle Refresh Current Component
        processor.handle_refresh_component(component_attribute, file_name)

    def is_enabled(self):
        return check_enabled(self.view.file_name())

class RefreshSelectedComponentsCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RefreshSelectedComponentsCommand, self).__init__(*args, **kwargs)

    def run(self, files):
        sublime.active_window().run_command("show_panel", {"panel": "console", "toggle": False})
        for file in files:
            component_attribute = get_component_attribute(file)[0]
            processor.handle_refresh_component(component_attribute, file)

    def is_enabled(self, files):
        if len(files) == 0: return False
        for file in files: 
            if not check_enabled(file): return False

        return True

def get_component_attribute(file_name):
    # Get toolingapi settings
    toolingapi_settings = context.get_toolingapi_settings()

    # Get component type
    component_name = util.get_component_name(file_name)
    component_type = util.get_component_type(file_name)

    # If component type is not in range, just show error message
    if component_type not in toolingapi_settings["component_types"]:
        return

    # Get component_url and component_id
    username = toolingapi_settings["username"]
    component_attribute = util.get_component_attribute(username, file_name)

    return (component_attribute, component_name)

def check_enabled(file_name):
    """
    Check whether file is ApexTrigger, ApexComponent, ApexPage or ApexClass

    Parameters:
        file_name: current file name

    Return: 
        Bool
    """
    if file_name == None:
        return False

    # Get toolingapi settings
    toolingapi_settings = context.get_toolingapi_settings()

    # Check Component Type
    component_type = util.get_component_type(file_name)
    if component_type not in toolingapi_settings["component_types"]:
        return False

    # Check whether project of current file is active project
    try:
        project_of_current_file = [p for p in toolingapi_settings["projects"].keys() if p in file_name]
        return toolingapi_settings["projects"][project_of_current_file[0]]["default"]
    except:
        print (message.format('Current Project' + project_of_current_file))
        return False

    # Check whether active component is in active project
    username = toolingapi_settings["username"]
    try:
        component_attribute = util.get_component_attribute(username, file_name)
    except:
        return False

    if component_attribute == None: 
        return False

    return True