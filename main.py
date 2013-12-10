import sublime
import sublime_plugin
import webbrowser
import urllib
import re
import os
import sys
import shutil
import zipfile

from . import requests
from . import processor
from . import context
from . import util
from .salesforce import message
from .salesforce.bulkapi import BulkApi

class ExportDataTemplateCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportDataTemplateCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.sobject_recordtypes_attr = processor.populate_sobject_recordtypes()
        self.sobject_recordtypes = sorted(list(self.sobject_recordtypes_attr.keys()))
        self.window.show_quick_panel(self.sobject_recordtypes, self.on_done)

    def on_done(self, index):
        if index == -1: return

        # Get chosen item, sobject name and recordtype id
        sobject_recordtype = self.sobject_recordtypes[index]
        sobject = sobject_recordtype.split(",")[0].strip()
        recordtype_name = sobject_recordtype.split(",")[1].strip()
        recordtype_id = self.sobject_recordtypes_attr[sobject_recordtype]

        # handle this describe request
        processor.handle_export_data_template_thread(sobject, recordtype_name, recordtype_id)

class ExecuteRestTestCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.items = ["GET", "DELETE", "HEAD", "Retrieve Body"]
        self.view.show_popup_menu(self.items, self.on_done),

    def on_done(self, index):
        if index == -1: return
        processor.handle_execute_rest_test(self.items[index], self.sel)

    def is_enabled(self):
        self.sel = self.view.substr(self.view.sel()[0])
        if not self.sel: return False
        return True

class GotoComponentCommand(sublime_plugin.TextCommand):
    """
    Move the cursor to the class name, press shift key and left mouse, 
    the class file will be open, you can custom the bind key in mousemap path
    """

    def run(self, edit, is_background=False):
        sel = self.view.sel()[0]
        sel_text = self.view.substr(sel)
        sel_text = self.view.substr(self.view.word(sel.begin()))
        
        project_folder = os.path.split(os.path.split(self.view.file_name())[0])[0]
        toolingapi_settings = context.get_toolingapi_settings()
        for component_type in toolingapi_settings["component_types"]:
            folder = toolingapi_settings[component_type]["folder"]
            extension = toolingapi_settings[component_type]["extension"]
            target_file = project_folder + "/%s/%s%s" % (folder, sel_text, extension)
            if os.path.isfile(target_file):
                self.view.window().open_file(target_file)

        if is_background: self.view.window().focus_view(self.view)

class SetCheckPointCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        mark = [s for s in self.view.sel()]
        self.view.add_regions("mark", mark, "red", 'circle',
            sublime.DRAW_NO_FILL | sublime.DRAW_NO_OUTLINE | sublime.DRAW_STIPPLED_UNDERLINE)

class RemoveCheckPointCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.erase_regions('mark')

class ListCodeCoverageCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ListCodeCoverageCommand, self).__init__(*args, **kwargs)

    def run(self):
        pass

class ViewCodeCoverageCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Get file_name and component_attribute
        file_name = self.view.file_name()
        component_attribute, component_name = util.get_component_attribute(file_name)

        # Handle Save Current Component
        processor.handle_view_code_coverage(component_name, component_attribute, self.body)

    def is_visible(self):
        # Must Be File
        if not self.view.file_name(): return False

        # Must be valid component
        is_enabled = check_enabled(self.view.file_name())
        if not is_enabled: return False

        # Must be class or trigger
        name, extension = util.get_file_attr(self.view.file_name())
        if extension not in [".cls", ".trigger"]: return False

        # Can't be Test Class
        self.body = open(self.view.file_name(), encoding="utf-8").read()
        if "@istest" in self.body.lower(): return False

        return True

class SwitchProjectCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(SwitchProjectCommand, self).__init__(*args, **kwargs)

    def run(self):
        global projects
        toolingapi_settings = context.get_toolingapi_settings()
        projects = toolingapi_settings["projects"]
        projects = ["(" + ('Active' if projects[p]["default"] else 
            'Inactive') + ") " + p for p in projects]
        projects = sorted(projects, reverse=False)
        self.window.show_quick_panel(projects, self.on_done)

    def on_done(self, index):
        if index == -1: return

        # Change the chosen project as default
        # Split with ") " and get the second project name
        default_project = projects[index].split(") ")[1]
        context.switch_project(default_project)

        # After project is switch, login will be executed
        processor.handle_login_thread(default_project)

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

    def run(self, edit, point=0, name="", input=""):
        view = sublime.active_window().active_view()
        view.set_scratch(True)
        view.set_name(name)
        view.insert(edit, point, input)

class NewDynamicViewCommand(sublime_plugin.TextCommand):
    """
    Create a new view with specified input

    @input: user specified input

    Usage: 
        sublime.active_window().run_command("new_view", {
            "name": "ViewName",
            "input": "Example"
        })
    """

    def run(self, edit, view_id=None, view_name="", input="", point=0, erase_all=False):
        # Get the view which name match the name paramter
        view = sublime.active_window().active_view()
        if view_id and not view.id() == view_id:
            for v in sublime.active_window().views():
                if v.id() == view_id: 
                    view = v

        view.set_scratch(True)
        view.set_name(view_name)
        if erase_all: view.erase(edit, sublime.Region(0, view.size()))
        view.insert(edit, point, input)

class RefreshFolderCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RefreshFolderCommand, self).__init__(*args, **kwargs)

    def run(self):
        global folders
        toolingapi_settings = context.get_toolingapi_settings()
        folders = sorted(list(toolingapi_settings["component_folders"]))
        self.window.show_quick_panel(folders, self.on_done)

    def on_done(self, index):
        if index == -1: return
        processor.handle_refresh_folder(folders[index])

class RetrieveMetadataCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RetrieveMetadataCommand, self).__init__(*args, **kwargs)

    def run(self):
        processor.handle_retrieve_all_thread()

class DeployMetadataCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DeployMetadataCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.window.show_input_panel("Input Zip File Path:", 
            "C:/Users/Administrator/Dropbox/workspace/pro-exericse-20130924/metadata/src.zip", self.on_input, None, None)

    def on_input(self, input):
        if not input.endswith('.zip'):
            sublime.error_message("Invalid Zip File")
            return
        processor.handle_deploy_metadata_thread(input)

class ExportValidationRulesCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportValidationRulesCommand, self).__init__(*args, **kwargs)

    def run(self):
        toolingapi_settings = context.get_toolingapi_settings()
        workflow_path = toolingapi_settings["workspace"] + "/metadata/unpackaged/objects"
        if not os.path.exists(workflow_path):
            sublime.error_message(message.METADATA_CHECK)
            return

        processor.handle_export_validation_rules()

class ExportWorkflowsCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportWorkflowsCommand, self).__init__(*args, **kwargs)

    def run(self):
        toolingapi_settings = context.get_toolingapi_settings()
        workspace = toolingapi_settings["workspace"]
        workflow_path = workspace + "/metadata/unpackaged/workflows"
        if not os.path.exists(workflow_path):
            sublime.error_message(message.METADATA_CHECK)
            return

        processor.handle_export_workflows()

class ExportFieldDependencyCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportFieldDependencyCommand, self).__init__(*args, **kwargs)

    def run(self):
        toolingapi_settings = context.get_toolingapi_settings()
        workspace = toolingapi_settings["workspace"]
        workflow_path = workspace + "/metadata/unpackaged/objects"
        if not os.path.exists(workflow_path):
            sublime.error_message(message.METADATA_CHECK)
            return

        processor.handle_export_field_dependencies()

class ExportCustomFieldCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportCustomFieldCommand, self).__init__(*args, **kwargs)

    def run(self):
        processor.handle_export_customfield()
        
class DescribeGlobalCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DescribeGlobalCommand, self).__init__(*args, **kwargs)

    def run(self):
        processor.handle_describe_global()

class DescribeSobjectCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DescribeSobjectCommand, self).__init__(*args, **kwargs)

    def run(self):
        global sobjects
        sobjects_describe = processor.populate_sobjects_describe()
        sobjects = sorted(sobjects_describe.keys())
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

        class_name = class_names[index]
        class_id = classes_attr[class_name]["id"]
        processor.handle_run_test(class_name, class_id)

class RunTestCommand(sublime_plugin.TextCommand):
    def run(self, view):
        # Get component_attribute by file_name
        name, extension = util.get_file_attr(self.view.file_name())
        component_attribute = util.get_component_attribute(self.view.file_name())[0]

        # Process run test
        processor.handle_run_test(name, component_attribute["id"])

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
        processor.handle_create_debug_log(user_name, user_id)

class ListDebugLogsCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ListDebugLogsCommand, self).__init__(*args, **kwargs)

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
        processor.handle_list_debug_logs(user_name, user_id)

class ViewDebugLogDetail(sublime_plugin.TextCommand):
    def run(self, view):
        processor.handle_view_debug_log_detail(self.log_id)

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
        component_attribute = util.get_component_attribute(self.view.file_name())[0]

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
        for _file in files:
            if not check_enabled(_file):
                return False

        return True

class DeleteComponentCommand(sublime_plugin.TextCommand):
    def run(self, view):
        files = [self.view.file_name()]
        delete_components(files)

    def is_enabled(self):
        return check_enabled(self.view.file_name())

def delete_components(files):
    # Confirm Delete Action
    confirm = sublime.ok_cancel_dialog(message.DELETE_CONFIRM_MESSAGE)
    if confirm == False: return
    
    # Handle Delete
    for f in files:
        component_attribute = util.get_component_attribute(f)[0]
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

        self.window.open_file(file_name)

        # Before you save it to server, save it to local
        self.view = self.window.active_view()
        if self.view.is_dirty():
            self.view.run_command("save")

        # Get Current File Name
        file_name = self.view.file_name()

        # Read file content
        body = open(file_name).read()
        
        # Get component type and component_name (Class Name, Trigger Name, etc.)
        name, extension = util.get_file_attr(file_name)
        component_type = toolingapi_settings[extension]

        # There has bug on creating ApexTrigger, but fixed on 2013 May 6 at 21:
        # Create Trigger is different from others, we can't use tooling/sobjects/ApexTrigger,
        # We should use sobjects/ApexTrigger
        # http://salesforce.stackexchange.com/questions/9603/how-do-i-use-the-tooling-api-to-create-a-new-apex-trigger
        # If component type is not in range, just show error message
        if extension not in toolingapi_settings["component_extensions"]:
            sublime.error_message(message.INVALID_COMPONENT)
            return

        # Get Component body Metadata Attribute in SFDC
        component_body = toolingapi_settings[component_type]["body"]

        # Compose data
        data = {
            "name": name,
            component_body: body,
        }
        if component_type == "ApexClass":
            data["IsValid"] = True
        elif component_type == "ApexTrigger":
            data["TableEnumOrId"] = sobject_name
        elif component_type in ["ApexPage", "ApexComponent"]:
            data["MasterLabel"] = name

        processor.handle_create_component(data, name, component_type, self.view.id())

class SaveComponentCommand(sublime_plugin.TextCommand):
    def run(self, view):
        # Automatically save current file if dirty
        if self.view.is_dirty():
            self.view.run_command("save")
            
        # Get file_name and component_attribute
        file_name = self.view.file_name()
        component_attribute, component_name = util.get_component_attribute(file_name)

        # Read file content
        try:
            body = open(file_name, encoding="utf-8").read()
        except:
            body = open(file_name).read()

        # Handle Save Current Component
        processor.handle_save_component(component_name, component_attribute, body)

    def is_enabled(self):
        return check_enabled(self.view.file_name())

class CreateNewProjectCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateNewProjectCommand, self).__init__(*args, **kwargs)

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
        processor.handle_new_project(toolingapi_settings)

class RefreshComponentCommand(sublime_plugin.TextCommand):
    def run(self, view):
        # Get file_name and component_attribute
        file_name = self.view.file_name()
        component_attribute = util.get_component_attribute(file_name)[0]
        
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
            component_attribute = util.get_component_attribute(file)[0]
            processor.handle_refresh_component(component_attribute, file)

    def is_enabled(self, files):
        if len(files) == 0: return False
        for file in files: 
            if not check_enabled(file): return False

        return True

def check_enabled(file_name):
    """
    Check whether file is ApexTrigger, ApexComponent, ApexPage or ApexClass

    Parameters:
        file_name: current file name

    Return: 
        Bool
    """
    if file_name == None: return False

    # Get toolingapi settings
    toolingapi_settings = context.get_toolingapi_settings()

    # Check Component Type
    name, extension = util.get_file_attr(file_name)
    if extension not in toolingapi_settings["component_extensions"]: return False

    # StaticResource is exclude
    # if component_type == "StaticResource": return False

    # Check whether project of current file is active project
    default_project_name = toolingapi_settings["default_project_name"]
    if not default_project_name in file_name: return False

    # Check whether active component is in active project
    username = toolingapi_settings["username"]
    component_attribute, component_name = util.get_component_attribute(file_name)
    if component_attribute == None: return False
    
    return True