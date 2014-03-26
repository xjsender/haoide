import sublime
import sublime_plugin
import webbrowser
import urllib
import re
import os
import sys
import shutil
import zipfile
import json

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
        self.items = ["Get", "Post", "Put", "Patch", "Delete", "Tooling Query",
                      "Query", "Query All", "Head", "Retrieve Body"]
        self.view.show_popup_menu(self.items, self.on_choose_action),

    def on_choose_action(self, index):
        if index == -1: return
        self.chosen_action = self.items[index]
        if self.chosen_action in ["Post", "Put", "Patch"]:
            self.view.window().show_input_panel("Input JSON Body: ", "", self.on_input, None, None)
        else:
            processor.handle_execute_rest_test(self.chosen_action, self.sel)

    def on_input(self, data):
        try:
            data = json.loads(data) if data else None
        except:
            message = 'Invalid data, do you want to try again?'
            if not sublime.ok_cancel_dialog(message): return
            self.view.window().show_input_panel("Input JSON Body: ", 
                "", self.on_input, None, None)
            return
        processor.handle_execute_rest_test(self.chosen_action, self.sel, data)

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
        
        settings = context.get_toolingapi_settings()
        for component_type in settings["component_types"]:
            folder = settings[component_type]["folder"]
            extension = settings[component_type]["extension"]
            target_file = settings["workspace"] + "/%s/%s%s" % (folder, sel_text, extension)
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

class RefreshClassFolderCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RefreshClassFolderCommand, self).__init__(*args, **kwargs)

    def run(self, dirs):
        processor.handle_refresh_folder(self.folder_name, self.component_outputdir)

    def is_visible(self, dirs):
        if not dirs: return False
        self.component_outputdir = dirs[0]
        self.project_name, self.folder_name = util.get_path_attr(self.component_outputdir)

        # Check whether the project is exist in settings
        self.settings = context.get_toolingapi_settings()
        if self.folder_name not in self.settings: return False
        component_type = self.settings[self.folder_name]
        if component_type != "ApexClass": return False
        if self.project_name != self.settings["default_project_name"]: return False

        return True

class RefreshComponentFolderCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RefreshComponentFolderCommand, self).__init__(*args, **kwargs)

    def run(self, dirs):
        processor.handle_refresh_folder(self.folder_name, self.component_outputdir)

    def is_visible(self, dirs):
        if not dirs: return False
        self.component_outputdir = dirs[0]
        self.project_name, self.folder_name = util.get_path_attr(self.component_outputdir)

        # Check whether the project is exist in settings
        self.settings = context.get_toolingapi_settings()
        if self.folder_name not in self.settings: return False
        component_type = self.settings[self.folder_name]
        if component_type != "ApexComponent": return False
        if self.project_name != self.settings["default_project_name"]: return False

        return True

class RefreshPageFolderCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RefreshPageFolderCommand, self).__init__(*args, **kwargs)

    def run(self, dirs):
        processor.handle_refresh_folder(self.folder_name, self.component_outputdir)

    def is_visible(self, dirs):
        if not dirs: return False
        self.component_outputdir = dirs[0]
        self.project_name, self.folder_name = util.get_path_attr(self.component_outputdir)

        # Check whether the project is exist in settings
        self.settings = context.get_toolingapi_settings()
        if self.folder_name not in self.settings: return False
        component_type = self.settings[self.folder_name]
        if component_type != "ApexPage": return False
        if self.project_name != self.settings["default_project_name"]: return False

        return True

class RefreshTriggerFolderCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RefreshTriggerFolderCommand, self).__init__(*args, **kwargs)

    def run(self, dirs):
        processor.handle_refresh_folder(self.folder_name, self.component_outputdir)

    def is_visible(self, dirs):
        if not dirs: return False
        self.component_outputdir = dirs[0]
        self.project_name, self.folder_name = util.get_path_attr(self.component_outputdir)

        # Check whether the project is exist in settings
        self.settings = context.get_toolingapi_settings()
        if self.folder_name not in self.settings: return False
        component_type = self.settings[self.folder_name]
        if component_type != "ApexTrigger": return False
        if self.project_name != self.settings["default_project_name"]: return False

        return True

class RefreshStaticResourceFolderCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RefreshStaticResourceFolderCommand, self).__init__(*args, **kwargs)

    def run(self, dirs):
        processor.handle_get_static_resource_body(self.folder_name, self.component_outputdir)

    def is_visible(self, dirs):
        if not dirs: return False
        self.component_outputdir = dirs[0]
        self.project_name, self.folder_name = util.get_path_attr(self.component_outputdir)

        # Check whether the project is exist in settings
        self.settings = context.get_toolingapi_settings()
        if self.folder_name not in self.settings: return False
        component_type = self.settings[self.folder_name]
        if component_type != "StaticResource": return False
        if self.project_name != self.settings["default_project_name"]: return False

        return True

class RetrieveMetadataCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RetrieveMetadataCommand, self).__init__(*args, **kwargs)

    def run(self):
        processor.handle_retrieve_all_thread()

class DeployMetadataCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DeployMetadataCommand, self).__init__(*args, **kwargs)

    def run(self):
        sublime.message_dialog("Ongoing")
        return
        self.window.show_input_panel("Input Zip File Path:", "", self.on_input, None, None)

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

class DescribeSobjectCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DescribeSobjectCommand, self).__init__(*args, **kwargs)

    def run(self):
        sobjects_describe = processor.populate_sobjects_describe()
        self.sobjects = sorted(sobjects_describe.keys())
        self.window.show_quick_panel(self.sobjects, self.on_done)

    def on_done(self, index):
        if index == -1: return
        processor.handle_describe_sobject(self.sobjects[index])

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

class RunAllTestCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RunAllTestCommand, self).__init__(*args, **kwargs)

    def run(self):
        processor.handle_run_all_test()

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
        if not file_name or not file_name.endswith(".cls"): 
            return False

        # Test class must be class firstly
        body = open(file_name, "rb").read()

        # Test class must contains "testMethod" or @isTest notation
        lower_body = body.lower()
        if b"testmethod" not in lower_body and b"@istest" not in lower_body:
            return False

        return True

class TrackDebugLogCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(TrackDebugLogCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.users = processor.populate_users()
        self.users_name = sorted(self.users.keys(), reverse=False)
        self.window.show_quick_panel(self.users_name, self.on_done)

    def on_done(self, index):
        if index == -1: return

        # Change the chosen project as default
        # Split with ") " and get the second project name
        user_name = self.users_name[index]
        user_id = self.users[user_name]
        processor.handle_create_debug_log(user_name, user_id)

class FetchDebugLogCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(FetchDebugLogCommand, self).__init__(*args, **kwargs)

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

    def is_enabled(self):
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
        settings = context.get_toolingapi_settings()

        # Combine Login URL
        show_params = {
            "un": settings["username"],
            "pw": settings["password"],
            "startURL": startURL
        }

        if util.is_python3x():
            show_params = urllib.parse.urlencode(show_params)
        else:
            show_params = urllib.urlencode(show_params)

        show_url = settings["login_url"] + '?%s' % show_params

        browser_path = settings["default_chrome_path"]
        if os.path.exists(browser_path):
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser_path))
            webbrowser.get('chrome').open_new_tab(show_url)
        else:
            webbrowser.open_new_tab(show_url)

class AboutCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(AboutCommand, self).__init__(*args, **kwargs)

    def run(self):
        settings = context.get_toolingapi_settings()
        browser_path = settings["default_chrome_path"]

        plugin_url = "https://github.com/xjsender/SublimeApex#sublime-ide-for-salesforce"
        if os.path.exists(browser_path):
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser_path))
            webbrowser.get('chrome').open_new_tab(plugin_url)
        else:
            webbrowser.open_new_tab(plugin_url)

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

def check_new_component_enabled():
    settings = context.get_toolingapi_settings()
    return os.path.exists(settings["workspace"])

class CreateApexTriggerCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateApexTriggerCommand, self).__init__(*args, **kwargs)

    def run(self):
        sobjects_describe = processor.populate_sobjects_describe()
        self.sobjects = sorted([name for name in sobjects_describe\
            if sobjects_describe[name]["triggerable"]])
        self.window.show_quick_panel(self.sobjects, self.on_done)

    def on_done(self, index):
        if index == -1: return
        self.window.run_command("create_component", {
            "component_type": "ApexTrigger",
            "sobject_name": self.sobjects[index]
        })

    def is_enabled(self):
        return check_new_component_enabled()

class CreateApexPageCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateApexPageCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.window.run_command("create_component", {"component_type": "ApexPage"})

    def is_enabled(self):
        return check_new_component_enabled()

class CreateApexComponentCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateApexComponentCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.window.run_command("create_component", {"component_type": "ApexComponent"})    

    def is_enabled(self):
        return check_new_component_enabled()

class CreateApexClassCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateApexClassCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.window.run_command("create_component", {"component_type": "ApexClass"})

    def is_enabled(self):
        return check_new_component_enabled()

class CreateComponentCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateComponentCommand, self).__init__(*args, **kwargs)

    def run(self, component_type=None, sobject_name=None):
        self.sobject_name = sobject_name
        self.component_type = component_type
        template_settings = sublime.load_settings("template.sublime-settings")
        self.templates = template_settings.get("template")
        self.template_names = sorted(list(self.templates[self.component_type].keys()))

        # If component type is ApexTrigger, we need to choose sobject and template,
        # however, sublime Quick panel will be unavailable for the second choose panel,
        if self.component_type == "ApexTrigger" or len(self.template_names) == 1:
            self.on_choose_template(0)
        else:
            self.window.show_quick_panel(self.template_names, self.on_choose_template)

    def on_choose_template(self, index):
        if index == -1: return
        self.template_name = self.template_names[index]
        self.template_attr = self.templates[self.component_type][self.template_name]
        self.window.show_input_panel("Please Input Name: ", "", self.on_input, None, None)

    def on_input(self, input):
        # Create component to local according to user input
        if not re.match('^[a-zA-Z]+\\w+$', input):
            message = 'Invalid format, are you want to input again?'
            if not sublime.ok_cancel_dialog(message): return
            self.window.show_input_panel("Please Input Name: ", "", self.on_input, None, None)
            return
        name = input
        
        extension = self.template_attr["extension"]
        body = self.template_attr["body"]
        if extension == ".trigger":
            body = body.replace("trigger_name", name).replace("sobject_name", self.sobject_name)
        elif extension == ".cls":
            body = body.replace("class_name", name)

        self.settings = context.get_toolingapi_settings()
        component_type = self.settings[extension]
        component_outputdir = self.settings[component_type]["outputdir"]
        if not os.path.exists(component_outputdir):
            os.makedirs(component_outputdir)
            self.settings = context.get_toolingapi_settings()
            context.add_project_to_workspace(self.settings["workspace"])

        file_name = "%s/%s" % (component_outputdir, name + extension)
        if os.path.isfile(file_name):
            self.window.open_file(file_name)
            sublime.error_message(name + " is already exist")
            return

        with open(file_name, "w") as fp:
            fp.write(body)

        # Compose data
        data = {
            "name": name,
            self.settings[component_type]["body"]: body,
        }
        if component_type == "ApexClass":
            data["IsValid"] = True
        elif component_type == "ApexTrigger":
            data["TableEnumOrId"] = self.sobject_name
        elif component_type in ["ApexPage", "ApexComponent"]:
            data["MasterLabel"] = name

        processor.handle_create_component(data, name, component_type, file_name)

class SaveComponentCommand(sublime_plugin.TextCommand):
    def run(self, edit, is_check_only=False):
        # Automatically save current file if dirty
        if self.view.is_dirty():
            self.view.run_command("save")
            
        # Get file_name and component_attribute
        file_name = self.view.file_name()
        component_attribute, component_name = util.get_component_attribute(file_name)

        # Read file content
        body = open(file_name, encoding="utf-8").read()

        # Handle Save Current Component
        processor.handle_save_component(component_name, component_attribute, body, is_check_only)

    def is_enabled(self):
        return check_enabled(self.view.file_name())

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

class CreateNewProjectCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateNewProjectCommand, self).__init__(*args, **kwargs)

    def run(self, switch_project=True):
        if switch_project:
            global projects
            toolingapi_settings = context.get_toolingapi_settings()
            projects = toolingapi_settings["projects"]
            projects = ["(" + ('Active' if projects[p]["default"] else 
                'Inactive') + ") " + p for p in projects]
            projects = sorted(projects, reverse=False)
            self.window.show_quick_panel(projects, self.on_done)
        else:
            self.on_done(100)

    def on_done(self, index):
        if index == -1: return
        if index != 100:
            # Change the chosen project as default
            # Split with ") " and get the second project name
            default_project = projects[index].split(") ")[1]
            context.switch_project(default_project)

        # Create Project Directory
        context.make_dir()

        # Get toolingapi_settings
        settings = context.get_toolingapi_settings()
        context.add_project_to_workspace(settings["workspace"])

        # Open Console
        self.window.run_command("show_panel", {"panel": "console", "toggle": False})

        # Handle Refresh All
        processor.handle_new_project(settings)

class ReloadCacheCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ReloadCacheCommand, self).__init__(*args, **kwargs)

    def run(self):
        processor.handle_initiate_sobjects_completions()

class ClearCacheCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ClearCacheCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.usernames = util.get_sobject_caches()
        if not self.usernames:
            sublime.message_dialog("No sobject cache already")
            return
        self.window.show_quick_panel(self.usernames, self.on_done)

    def on_done(self, index):
        if index == -1: return
        confirm = sublime.ok_cancel_dialog("Are you sure you really want to clear this?")
        if confirm == False: return
        util.clear_cache(self.usernames[index])

class RefreshComponentCommand(sublime_plugin.TextCommand):
    def run(self, view):
        confirm = sublime.ok_cancel_dialog(message.REFRESH_CONFIRM_MESSAGE)
        if confirm == False: return
    
        # Get file_name and component_attribute
        file_name = self.view.file_name()
        component_attribute = util.get_component_attribute(file_name)[0]
        
        # Handle Refresh Current Component
        if component_attribute["type"] == "StaticResource":
            processor.handle_refresh_static_resource(component_attribute, file_name)
        else:
            processor.handle_refresh_component(component_attribute, file_name)

    def is_enabled(self):
        return check_enabled(self.view.file_name())

class RefreshSelectedComponentsCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RefreshSelectedComponentsCommand, self).__init__(*args, **kwargs)

    def run(self, files):
        sublime.active_window().run_command("show_panel", {"panel": "console", "toggle": False})
        for file_name in files:
            component_attribute = util.get_component_attribute(file_name)[0]

            # Handle Refresh Current Component
            if component_attribute["type"] == "StaticResource":
                processor.handle_refresh_static_resource(component_attribute, file_name)
            else:
                processor.handle_refresh_component(component_attribute, file_name)

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
    if extension not in toolingapi_settings["component_extensions"]: 
        sublime.status_message("This component is not salesforce component")
        return False

    # StaticResource is exclude
    # if component_type == "StaticResource": return False

    # Check whether project of current file is active project
    default_project_name = toolingapi_settings["default_project_name"]
    if not default_project_name in file_name: 
        sublime.status_message('This project is not active project');
        return False

    # Check whether active component is in active project
    username = toolingapi_settings["username"]
    component_attribute, component_name = util.get_component_attribute(file_name)
    if component_attribute == None: 
        sublime.status_message("This component is not active component")
        return False
    
    return True