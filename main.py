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
import time
import pprint

from . import requests
from . import processor
from . import context
from . import util

from .salesforce import xmltodict
from .salesforce import message


class ConvertXmlToDictCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        jsonStr = json.dumps(self.result, indent=4)
        new_view = sublime.active_window().new_file()
        new_view.run_command("new_view", {
            "name": "XML2JSON",
            "input": jsonStr
        })

        # If you have installed the htmljs plugin, below statement will work
        new_view.run_command("htmlprettify")

    def is_visible(self):
        # Visible if has selection
        selection = self.view.substr(self.view.sel()[0])

        # If not selection, just select all
        if not selection:
            selection = self.view.substr(sublime.Region(0, self.view.size()))

        # Check whether selection is valid xml
        try:
            self.result = xmltodict.parse(selection)
        except Exception as ex:
            return False

        return True

class ReloadSobjectCacheCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ReloadSobjectCacheCommand, self).__init__(*args, **kwargs)

    def run(self):
        confirm = sublime.ok_cancel_dialog("Are you sure you really want to update sObject cache?")
        if confirm == False: return
        processor.handle_reload_sobjects_completions()

class ReloadSymbolTableCacheCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ReloadSymbolTableCacheCommand, self).__init__(*args, **kwargs)

    def run(self):
        confirm = sublime.ok_cancel_dialog("Are you sure you really want to update symbol table cache?")
        if confirm == False: return
        processor.handle_reload_symbol_tables()

class ClearCacheCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ClearCacheCommand, self).__init__(*args, **kwargs)

    def run(self, cache_name):
        self.cache_name = cache_name+".sublime-settings"
        self.caches = util.get_sobject_caches(self.cache_name)
        if not self.caches:
            sublime.message_dialog("No cache already")
            return

        self.window.show_quick_panel(self.caches, self.on_done)

    def on_done(self, index):
        if index == -1: return
        confirm = sublime.ok_cancel_dialog("Are you sure you really want to clear this?")
        if confirm == False: return
        util.clear_cache(self.caches[index][1], self.cache_name)

class GenerateSoqlCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(GenerateSoqlCommand, self).__init__(*args, **kwargs)

    def run(self):
        sobjects_describe = util.populate_sobjects_describe()
        self.sobjects = sorted(sobjects_describe.keys())
        self.window.show_quick_panel(self.sobjects, self.on_done)

    def on_done(self, index):
        if index == -1: return
        processor.handle_generate_sobject_soql(self.sobjects[index])

class ExportDataTemplateCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportDataTemplateCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.sobject_recordtypes_attr = processor.populate_sobject_recordtypes()
        if not self.sobject_recordtypes_attr: return # Network Issue Cause
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
        util.check_workspace_available()
        processor.handle_export_data_template_thread(sobject, recordtype_name, recordtype_id)

class ExecuteRestTestCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.items = ["Get", "Post", "Put", "Patch", "Delete", "Tooling Query",
                      "Query", "Query All", "Search", "Quick Search", "Head", "Retrieve Body"]
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
    Move the cursor to the class name, press shift key and double click left mouse, 
    the class file will be open, you can custom the bind key in mousemap path
    """

    def run(self, edit, is_background=False):
        sel = self.view.sel()[0]
        sel_text = self.view.substr(self.view.word(sel.begin()))
        
        settings = context.get_settings()
        for ct in settings["subscribed_meta_types"]:
            folder = settings[ct]["folder"]
            extension = settings[ct]["extension"]
            target_file = settings["workspace"] + "/src/%s/%s%s" % (folder, sel_text, extension)
            if os.path.isfile(target_file):
                self.view.window().open_file(target_file)

        if is_background: self.view.window().focus_view(self.view)

class SetCheckPointCommand(sublime_plugin.TextCommand):
    def run(self, edit, mark):
        sel = [s for s in self.view.sel()]
        self.view.add_regions(mark, sel, "red", "dot",
            sublime.DRAW_SOLID_UNDERLINE | sublime.DRAW_EMPTY_AS_OVERWRITE)

class RemoveCheckPointCommand(sublime_plugin.TextCommand):
    def run(self, edit, mark):
        self.view.erase_regions(mark)

class ViewCodeCoverageCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Get file_name and component_attribute
        file_name = self.view.file_name()
        component_attribute, component_name = util.get_component_attribute(file_name)

        # Handle Save Current Component
        processor.handle_view_code_coverage(component_name, component_attribute, self.body)

    def is_enabled(self):
        # Must Be File
        if not self.view.file_name(): return False

        # Must be valid component
        is_enabled = util.check_enabled(self.view.file_name())
        if not is_enabled: return False

        # Must be class or trigger
        name, extension = util.get_file_attr(self.view.file_name())
        if extension not in [".cls", ".trigger"]: return False

        # Can't be Test Class
        self.body = open(self.view.file_name(), encoding="utf-8").read()
        if "@istest" in self.body.lower(): return False

        return True

class ViewSelectedCodeCoverageCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("goto_component", {"is_background": False})
        view = sublime.active_window().active_view()
        view.run_command("view_code_coverage")
        view.run_command("close")

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
        sublime.active_window().run_command("new_dynamic_view", {
            "view_id": "view_id",
            "point": 0,
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

    def run(self, dirs):
        confirm = sublime.ok_cancel_dialog("Are you sure you want to refresh this folder")
        if not confirm: return

        print (self.folders_dict)
        processor.handle_refresh_folder(self.folders_dict)

    def is_visible(self, dirs):
        if not dirs: return False

        # Get settings
        settings = context.get_settings()

        project_names = []
        self.folders_dict = {}
        for d in dirs:
            project_name, folder_name = util.get_path_attr(d)
            if folder_name not in settings: return False
            if project_name not in settings["default_project_name"]: return False
            project_names.append(project_name)
            self.folders_dict[folder_name] = d

        return True

class RetrieveMetadataCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RetrieveMetadataCommand, self).__init__(*args, **kwargs)

    def run(self, retrieve_all=True):
        confirm = sublime.ok_cancel_dialog("Are your sure you really want to continue?")
        if confirm == False: return
        processor.handle_retrieve_all_thread(retrieve_all=retrieve_all)

class RetrievePackageCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RetrievePackageCommand, self).__init__(*args, **kwargs)

    def run(self):
        path = sublime.get_clipboard()
        if not os.path.isfile(path): path = ""
        self.window.show_input_panel("Input Package.xml Path: ", 
            path, self.on_input, None, None)

    def on_input(self, _file):
        if not _file.lower().endswith('xml'): 
            sublime.error_message("Input file must be valid Package.xml file")
            return

        if not os.path.exists(_file):
            sublime.error_message(_file + " is not valid file")
            return

        path, name = os.path.split(_file)
        package_xml_content = open(_file, "rb").read()
        time_stamp = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
        settings = context.get_settings()
        project_name = settings["default_project_name"]
        extract_to = os.path.join(path, project_name+"-"+time_stamp)
        processor.handle_retrieve_package(package_xml_content, path)

class RetrievePackageFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        path, name = os.path.split(self._file)
        package_xml_content = open(self._file, "rb").read()
        time_stamp = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
        settings = context.get_settings()
        project_name = settings["default_project_name"]
        extract_to = os.path.join(path, project_name+"-"+time_stamp)
        processor.handle_retrieve_package(package_xml_content, extract_to)

    def is_visible(self):
        self._file = self.view.file_name()
        if not self._file: return False
        if not self._file.endswith(".xml"): return False

        return True

class RetrieveFileFromServer(sublime_plugin.TextCommand):
    def run(self, edit):
        files = [self.view.file_name()]
        sublime.active_window().run_command("retrieve_files_from_server", {"files": files})

    def is_enabled(self):
        self.settings = context.get_settings()
        _folder = util.get_meta_folder(self.view.file_name())
        if _folder not in self.settings["meta_folders"]:
            return False

        return True

class RetrieveFilesFromServer(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RetrieveFilesFromServer, self).__init__(*args, **kwargs)

    def run(self, files):
        package_dict = util.build_package_dict(files)
        package_xml_content = util.build_package_xml(self.settings, package_dict)
        processor.handle_retrieve_package(package_xml_content, 
                                          self.settings["workspace"], 
                                          ignore_package_xml=True)

    def is_enabled(self, files):
        if len(files) == 0: return False
        self.settings = context.get_settings()
        for _file in files:
            if not os.path.isfile(_file): continue # Ignore folder
            _folder = util.get_meta_folder(_file)
            if _folder not in self.settings["meta_folders"]:
                return False

        return True

class DeployZipCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DeployZipCommand, self).__init__(*args, **kwargs)

    def run(self):
        path = sublime.get_clipboard()
        if not path or not os.path.isfile(path): path = ""
        if not path.endswith("zip"): path = ""
        self.window.show_input_panel("Input Zip File Path:", 
            path, self.on_input, None, None)

    def on_input(self, zipfile_path):
        if not zipfile_path.endswith('.zip'):
            sublime.error_message("Invalid Zip File")
            return

        processor.handle_deploy_thread(util.base64_encode(zipfile_path))

class DeployPackageToServerCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DeployPackageToServerCommand, self).__init__(*args, **kwargs)

    def run(self, dirs):
        # Get the package path to deploy
        self.package_dir = dirs[0]

        # Choose the target ORG to deploy
        settings = context.get_settings()
        self.projects = settings["projects"]
        self.projects = ["(" + ('Active' if self.projects[p]["default"] else 
            'Inactive') + ") " + p for p in self.projects]
        self.projects = sorted(self.projects, reverse=False)
        self.window.show_quick_panel(self.projects, self.on_done)

    def on_done(self, index):
        if index == -1: return
        # Change the chosen project as default
        # Split with ") " and get the second project name
        default_project = self.projects[index].split(") ")[1]
        util.switch_project(default_project)

        processor.handle_deploy_thread(util.compress_package(self.package_dir));

    def is_enabled(self, dirs):
        if not dirs: return False
        if len(dirs) > 1: return False
        if not os.path.exists(dirs[0]+"/package.xml"):
            sublime.status_message("Not valid package path for deploy")
            return False

        return True

class DeployFileToServer(sublime_plugin.TextCommand):
    def run(self, edit):
        files = [self.view.file_name()]
        sublime.active_window().run_command("deploy_files_to_server", {"files": files})

    def is_enabled(self):
        self.settings = context.get_settings()
        _folder = util.get_meta_folder(self.view.file_name())
        if _folder not in self.settings["meta_folders"]:
            return False

        return True

class DeployFilesToServer(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DeployFilesToServer, self).__init__(*args, **kwargs)

    def run(self, files):
        # Get the package path to deploy
        self.files = files

        # Choose the target ORG to deploy
        settings = context.get_settings()
        self.projects = settings["projects"]
        self.projects = ["(" + ('Active' if self.projects[p]["default"] else 
            'Inactive') + ") " + p for p in self.projects]
        self.projects = sorted(self.projects, reverse=False)
        self.window.show_quick_panel(self.projects, self.on_done)

    def on_done(self, index):
        if index == -1: return
        # Change the chosen project as default
        # Split with ") " and get the second project name
        default_project = self.projects[index].split(") ")[1]
        util.switch_project(default_project)

        base64_encoded_zip = util.build_deploy_package(self.files)
        processor.handle_deploy_thread(base64_encoded_zip)

    def is_enabled(self, files):
        """
        1. You must have selected one file or more
        2. All selected file should be in predefined meta folders
        """

        if len(files) == 0: return False
        self.settings = context.get_settings()
        for _file in files:
            if not os.path.isfile(_file): continue # Ignore folder
            _folder = util.get_meta_folder(_file)
            if _folder not in self.settings["meta_folders"]:
                return False

        return True

class ExportValidationRulesCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportValidationRulesCommand, self).__init__(*args, **kwargs)

    def run(self):
        settings = context.get_settings()
        workflow_path = settings["workspace"] + "/metadata/src/objects"
        if not os.path.exists(workflow_path):
            sublime.error_message(message.METADATA_CHECK)
            return

        processor.handle_export_validation_rules(settings)

class ExportCustomLablesCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportCustomLablesCommand, self).__init__(*args, **kwargs)

    def run(self):
        settings = context.get_settings()
        workspace = settings["workspace"]
        lable_path = workspace + "/metadata/src/labels/CustomLabels.labels"
        if not os.path.isfile(lable_path):
            sublime.error_message(message.METADATA_CHECK)
            return

        outputdir = settings["workspace"] + "/Labels"
        if not os.path.exists(outputdir): os.makedirs(outputdir)
        lables = xmltodict.parse(open(lable_path, "rb").read())
        util.list2csv(outputdir+"/Labels.csv", lables["CustomLabels"]["labels"])

class ExportWorkflowsCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportWorkflowsCommand, self).__init__(*args, **kwargs)

    def run(self):
        settings = context.get_settings()
        workspace = settings["workspace"]
        workflow_path = workspace + "/metadata/src/workflows"
        if not os.path.exists(workflow_path):
            sublime.error_message(message.METADATA_CHECK)
            return

        processor.handle_export_workflows(settings)

class ExportFieldDependencyCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportFieldDependencyCommand, self).__init__(*args, **kwargs)

    def run(self):
        settings = context.get_settings()
        workspace = settings["workspace"]
        workflow_path = workspace + "/metadata/src/objects"
        if not os.path.exists(workflow_path):
            sublime.error_message(message.METADATA_CHECK)
            return

        util.check_workspace_available()
        processor.handle_export_field_dependencies()

class ExportCustomFieldCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportCustomFieldCommand, self).__init__(*args, **kwargs)

    def run(self):
        util.check_workspace_available()
        processor.handle_export_customfield()

class DescribeSobjectCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DescribeSobjectCommand, self).__init__(*args, **kwargs)

    def run(self):
        sobjects_describe = util.populate_sobjects_describe()
        self.sobjects = sorted(sobjects_describe.keys())
        self.window.show_quick_panel(self.sobjects, self.on_done)

    def on_done(self, index):
        if index == -1: return
        processor.handle_describe_sobject(self.sobjects[index])

class ExportWorkbookCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportWorkbookCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.window.show_input_panel("Input Sobjects(* or sobjects separated with semi-colon), Case is Sensitive", 
            "*", self.on_input, None, None)

    def on_input(self, input):
        # Display the fields in a new view
        input = input.replace(" ", "")

        util.check_workspace_available()
        if input == "*":
            processor.handle_generate_all_workbooks(5)
        else:
            # Collect the sobjects
            sobjects = input.split(";")

            # Check whether the input sobjects are valid
            # If any one is not valid, allow user to input again
            sobjects_describe = util.populate_sobjects_describe()
            if not sobjects_describe: return
            for sobject in sobjects:
                if sobject not in sobjects_describe:
                    message = '"%s" is not valid sobject, do you want to try again?' % sobject
                    if not sublime.ok_cancel_dialog(message): return
                    self.window.show_input_panel("Sobjects(* means all, or sobjects seprated with semi-colon)", 
                        input, self.on_input, None, None)
                    return

            # After ensured input is valid, just start to generate workbooks
            processor.handle_generate_specified_workbooks(sobjects)

class ViewComponentInSfdcCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ViewComponentInSfdcCommand, self).__init__(*args, **kwargs)

    def run(self):
        global all_components
        global all_components_name

        all_components = util.populate_components()

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

class PreviewPageCommand(sublime_plugin.TextCommand):
    def run(self, view):
        startURL = "/apex/" + self.filename
        self.view.window().run_command("login_to_sfdc", {"startURL": startURL})

    def is_visible(self):
        if not self.view.file_name(): return False
        self.filename, self.extension = util.get_file_attr(self.view.file_name())
        return self.extension == ".page"

class RunAllTestCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RunAllTestCommand, self).__init__(*args, **kwargs)

    def run(self):
        confirm = sublime.ok_cancel_dialog("Are you sure you really want to continue?")
        if confirm == False: return

        processor.handle_run_all_test()

class RunOneTestCommand(sublime_plugin.WindowCommand):
    """ List the test classes from local cache, after any one is chosen,
        get the attribute of the chosen class and run test, 

        Cache structure is shown as below:
        {
            "ApexClass":
            {
                "accountcontroller":
                {
                    "body": "Body",
                    "extension": ".cls",
                    "id": "01p90000003hdEGAAY",
                    "is_test": false,
                    "name": "AccountController",
                    "type": "ApexClass",
                    "url": "/services/data/v30.0/sobjects/ApexClass/01p90000003hdEGAAY"
                },
                ...
            },
            ...
        }
    """
    def __init__(self, *args, **kwargs):
        super(RunOneTestCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.classes_attr = util.populate_classes()
        self.classmap = {}
        for key in self.classes_attr:
            if not self.classes_attr[key]["is_test"]: continue
            self.classmap[self.classes_attr[key]["name"]] = key

        if not self.classmap:
            sublime.error_message("No Test Class");
            return

        self.class_names = sorted(list(self.classmap.keys()))
        self.window.show_quick_panel(self.class_names, self.on_done)

    def on_done(self, index):
        if index == -1: return

        class_name = self.class_names[index]
        key = self.classmap[class_name]
        class_id = self.classes_attr[key]["id"]
        processor.handle_run_test(class_name, class_id)

class FetchOrgWideCoverageCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(FetchOrgWideCoverageCommand, self).__init__(*args, **kwargs)

    def run(self):
        pass

class RunSyncTestClassesCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RunSyncTestClassesCommand, self).__init__(*args, **kwargs)

    def run(self, files):
        processor.handle_run_sync_test_classes(self.class_names)

    def is_enabled(self, files):
        # Check whether any classes are chosen
        if len(files) == 0: return False

        # Check whether there are test class in chosen classes 
        self.class_names = []
        for f in files:
            component_attribute, name = util.get_component_attribute(f)
            if not component_attribute or not component_attribute["is_test"]:
                continue

            self.class_names.append(name)
        
        return len(self.class_names) > 0

class RunAsyncTestClassesCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RunAsyncTestClassesCommand, self).__init__(*args, **kwargs)

    def run(self, files):
        processor.handle_run_async_test_classes(self.class_ids)

    def is_enabled(self, files):
        # Check whether any classes are chosen
        if len(files) == 0: return False

        # Check whether there are test class in chosen classes 
        self.class_ids = []
        for f in files:
            component_attribute, name = util.get_component_attribute(f)
            if not component_attribute or not component_attribute["is_test"]:
                continue

            self.class_ids.append(component_attribute["id"])
        
        return len(self.class_ids) > 0

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
        if not self.users: return # Network Issue Cause
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
        self.users = processor.populate_users()
        if not self.users: return # Network Issue Cause
        self.users_name = sorted(self.users.keys(), reverse=False)
        self.window.show_quick_panel(self.users_name, self.on_done)

    def on_done(self, index):
        if index == -1: return

        user_name = self.users_name[index]
        user_id = self.users[user_name]
        processor.handle_fetch_debug_logs(user_name, user_id)

class ViewDebugLogDetailCommand(sublime_plugin.TextCommand):
    def run(self, view):
        processor.handle_view_debug_log_detail(self.log_id)

    def is_enabled(self):
        # Choose the valid Id, you will see this command
        sel = self.view.sel()[0]
        self.log_id = self.view.substr(self.view.word(sel.begin()))

        if len(self.log_id) != 15 and len(self.log_id) != 18: return False
        if not re.compile(r'^[a-zA-Z0-9]*$').match(self.log_id): return False
        if not self.log_id.startswith("07L"): return False

        return True

class ExecuteSoqlCommand(sublime_plugin.TextCommand):
    def run(self, view):
        processor.handle_execute_query(self.view.substr(self.view.sel()[0]))

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
        # Enabled if has selection
        self.selection = self.view.substr(self.view.sel()[0])
        if not self.selection: return False

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
        return util.check_enabled(self.view.file_name())

class LoginToSfdcCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(LoginToSfdcCommand, self).__init__(*args, **kwargs)

    def run(self, startURL=""):
        # Get toolingapi settings
        settings = context.get_settings()

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
        util.open_with_browser(show_url)

class AboutCommand(sublime_plugin.ApplicationCommand):
    def run(command):
        package_info = sublime.load_settings("package.sublime-settings")

        version_info = "\n%s\n\n%s\n\nCopyright © 2013-2014 By %s\n\tDev Chanel, Build v%s" % (
            package_info.get("description"),
            package_info.get("homepage"),
            package_info.get("author"),
            package_info.get("version")
        )
        sublime.message_dialog(version_info)

class ReportIssueCommand(sublime_plugin.ApplicationCommand):
    def run(command):
        show_url = "https://github.com/xjsender/SublimeApex/issues"
        util.open_with_browser(show_url)

class DeleteSelectedComponentsCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DeleteSelectedComponentsCommand, self).__init__(*args, **kwargs)

    def run(self, files):
        delete_components(self._files)

    def is_visible(self, files):
        """
        1. You must have selected one file or more
        2. All selected file should be visible
        """

        if len(files) == 0: return False
        self._files = [f for f in files if not f.endswith("-meta.xml")]
        if len(self._files) == 0: return False
        for _file in self._files:
            if not util.check_enabled(_file): return False

        return True

class DeleteComponentCommand(sublime_plugin.TextCommand):
    def run(self, view):
        files = [self.view.file_name()]
        delete_components(files)

    def is_enabled(self):
        if not self.view.file_name(): return False
        if self.view.file_name().endswith("-meta.xml"): return False
        return util.check_enabled(self.view.file_name())

def delete_components(files):
    # Confirm Delete Action
    confirm = sublime.ok_cancel_dialog(message.DELETE_CONFIRM_MESSAGE)
    if confirm == False: return
    
    # Handle Delete
    for f in files:
        component_attribute = util.get_component_attribute(f)[0]
        processor.handle_delete_component(component_attribute["url"], f)

class CreateApexTriggerCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateApexTriggerCommand, self).__init__(*args, **kwargs)

    def run(self):
        sobjects_describe = util.populate_sobjects_describe()

        # Just for tracking issue # 28
        for name in sobjects_describe:
            if "triggerable" not in sobjects_describe[name]:
                print ('Not triggerable sobject: ' + name)

        self.sobjects = sorted([name for name in sobjects_describe\
            if "triggerable" in sobjects_describe[name] and sobjects_describe[name]["triggerable"]])
        self.window.show_quick_panel(self.sobjects, self.on_done)

    def on_done(self, index):
        if index == -1: return
        self.window.run_command("create_component", {
            "component_type": "ApexTrigger",
            "markup_or_body": "Body",
            "sobject_name": self.sobjects[index]
        })

    def is_enabled(self):
        return util.check_new_component_enabled()

class CreateApexPageCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateApexPageCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.window.run_command("create_component", {
            "component_type": "ApexPage",
            "markup_or_body": "Markup"
        })

    def is_enabled(self):
        return util.check_new_component_enabled()

class CreateApexComponentCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateApexComponentCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.window.run_command("create_component", {
            "component_type": "ApexComponent",
            "markup_or_body": "Markup"
        })

    def is_enabled(self):
        return util.check_new_component_enabled()

class CreateApexClassCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateApexClassCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.window.run_command("create_component", {
            "component_type": "ApexClass",
            "markup_or_body": "Body"
        })

    def is_enabled(self):
        return util.check_new_component_enabled()

class CreateComponentCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateComponentCommand, self).__init__(*args, **kwargs)

    def run(self, component_type=None, markup_or_body=None, sobject_name=None):
        self.component_type = component_type
        self.markup_or_body = markup_or_body
        self.sobject_name = sobject_name
        template_settings = sublime.load_settings("template.sublime-settings")
        self.templates = template_settings.get("template")

        self.template_names = []
        templates = self.templates[self.component_type]
        for name in templates:
            self.template_names.append([name, templates[name]["description"]])

        # If component type is ApexTrigger, we need to choose sobject and template,
        # however, sublime Quick panel will be unavailable for the second choose panel,
        if self.component_type == "ApexTrigger" or len(self.template_names) == 1:
            self.on_choose_template(0)
        else:
            self.window.show_quick_panel(self.template_names, self.on_choose_template)

    def on_choose_template(self, index):
        if index == -1: return
        self.template_name = self.template_names[index][0]
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

        self.settings = context.get_settings()
        workspace = self.settings["workspace"]
        component_outputdir = workspace+"/src/"+self.settings[self.component_type]["folder"]
        if not os.path.exists(component_outputdir):
            os.makedirs(component_outputdir)
            self.settings = context.get_settings()
            util.add_project_to_workspace(self.settings)

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
            self.markup_or_body: body,
        }
        if self.component_type == "ApexClass":
            data["IsValid"] = True
        elif self.component_type == "ApexTrigger":
            data["TableEnumOrId"] = self.sobject_name
        elif self.component_type in ["ApexPage", "ApexComponent"]:
            data["MasterLabel"] = name

        processor.handle_create_component(data, name, self.component_type, self.markup_or_body, file_name)

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
        return util.check_enabled(self.view.file_name())

class SwitchProjectCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(SwitchProjectCommand, self).__init__(*args, **kwargs)

    def run(self):
        global projects
        settings = context.get_settings()
        projects = settings["projects"]
        projects = ["(" + ('Active' if projects[p]["default"] else 
            'Inactive') + ") " + p for p in projects]
        projects = sorted(projects, reverse=False)
        self.window.show_quick_panel(projects, self.on_done)

    def on_done(self, index):
        if index == -1: return

        # Change the chosen project as default
        # Split with ") " and get the second project name
        default_project = projects[index].split(") ")[1]
        util.switch_project(default_project)

        # After project is switch, login will be executed
        processor.handle_login_thread(default_project)

class UpdateUserLanguageCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(UpdateUserLanguageCommand, self).__init__(*args, **kwargs)

    def run(self):
        settings = context.get_settings()
        self.languages_settings = settings["user_language"]
        self.languages = sorted(self.languages_settings.keys())
        self.window.show_quick_panel(self.languages, self.on_choose)

    def on_choose(self, index):
        if index == -1: return

        chosen_language = self.languages[index]
        processor.handle_update_user_language(self.languages_settings[chosen_language])

class UpdateProjectPatternsCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(UpdateProjectPatternsCommand, self).__init__(*args, **kwargs)

    def run(self):
        settings = context.get_settings()
        util.add_project_to_workspace(settings)

    def is_enabled(self):
        return util.check_new_component_enabled()

class UpdateProjectCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(UpdateProjectCommand, self).__init__(*args, **kwargs)

    def run(self):
        confirm = sublime.ok_cancel_dialog("Are you sure you really want to update this project?")
        if confirm == False: return
        settings = context.get_settings()
        util.add_project_to_workspace(settings)
        processor.handle_new_project(settings, is_update=True)

    def is_enabled(self):
        return util.check_new_component_enabled()

class CreateNewProjectCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateNewProjectCommand, self).__init__(*args, **kwargs)

    def run(self):
        # Get settings
        settings = context.get_settings()
        dpn = settings["default_project"]["project_name"]
        message = "Are you sure you really want to create new project for %s?" % dpn
        if sublime.ok_cancel_dialog(message):
            util.add_project_to_workspace(settings)
            processor.handle_new_project(settings)

class RefreshComponentCommand(sublime_plugin.TextCommand):
    def run(self, view):
        confirm = sublime.ok_cancel_dialog(message.REFRESH_CONFIRM_MESSAGE)
        if not confirm: return
    
        # Get file_name and component_attribute
        file_name = self.view.file_name()
        component_attribute = util.get_component_attribute(file_name)[0]
        
        # Handle Refresh Current Component
        if component_attribute["type"] == "StaticResource":
            processor.handle_refresh_static_resource(component_attribute, file_name)
        else:
            processor.handle_refresh_component(component_attribute, file_name)

    def is_enabled(self):
        return util.check_enabled(self.view.file_name())

class RefreshSelectedComponentsCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RefreshSelectedComponentsCommand, self).__init__(*args, **kwargs)

    def run(self, files):
        confirm = sublime.ok_cancel_dialog(message.REFRESH_CONFIRM_MESSAGE)
        if not confirm: return

        for file_name in self._files:
            if file_name.endswith("-meta.xml"): continue # Ignore -meta.xml file
            component_attribute = util.get_component_attribute(file_name)[0]

            # Handle Refresh Current Component
            if component_attribute["type"] == "StaticResource":
                processor.handle_refresh_static_resource(component_attribute, file_name)
            else:
                processor.handle_refresh_component(component_attribute, file_name)

    def is_visible(self, files):
        if len(files) == 0: return False
        self._files = [f for f in files if not f.endswith("-meta.xml")]
        if len(self._files) == 0: return False
        for _file in self._files:
            if not util.check_enabled(_file): return False

        return True