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
import pprint
import time

from . import requests
from . import processor
from . import context
from . import util

from .salesforce.lib.jsontoapex import JSONConverter
from .salesforce.lib.panel import Printer
from .salesforce import xmltodict
from .salesforce import message


class ConvertJsonToApex(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ConvertJsonToApex, self).__init__(*args, **kwargs)

    def run(self):
        sublime.active_window().show_input_panel("Input JSON Body: ", "", 
            self.on_input_json, None, None)

    def on_input_json(self, data):
        try:
            self.data = json.loads(data) if data else None
        except ValueError as ve:
            Printer.get('error').write(str(ve))
            if not sublime.ok_cancel_dialog("Do you want to try again?", "Yes?"): return
            sublime.active_window().show_input_panel("Input JSON Body: ", 
                "", self.on_input_json, None, None)
            return

        sublime.active_window().show_input_panel("Input Class Name: ", 
            "JSON2Apex", self.on_input_name, None, None)
        
    def on_input_name(self, name):
        if not name: name = "JSON2Apex"

        # Start converting
        converter = JSONConverter()
        converter.convert2apex(name, self.data)
        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": "JSON2APEX",
            "input": "\n".join(converter.classes)
        })

class PrettyJson(sublime_plugin.TextCommand):
    def run(self, view):
        try:
            pretty_json = json.dumps(json.loads(self.selection), 
                ensure_ascii=False, indent=4)
        except ValueError as ex:
            Printer.get('error').write(str(ex))
            return
            
        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": "PrettyJson",
            "input": pretty_json
        })

        # If you have installed the htmljs plugin, below statement will work
        view.run_command("htmlprettify")

    def is_enabled(self):
        # Enabled if has selection
        self.selection = self.view.substr(self.view.sel()[0])
        if not self.selection: return False

        return True

class DiffWithServerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        processor.handle_diff_with_server(self.component_attribute, self.file_name)

    def is_enabled(self):
        self.file_name = self.view.file_name()
        if not self.file_name: return False
        self.component_attribute = util.get_component_attribute(self.file_name)[0]
        if not self.component_attribute: return False
        return True

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

class ShowMyPanel(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ShowMyPanel, self).__init__(*args, **kwargs)

    def run(self, panel):
        Printer.get(panel).show_panel()

class ToggleMetadataObjects(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ToggleMetadataObjects, self).__init__(*args, **kwargs)

    def run(self):
        self.s = sublime.load_settings("toolingapi.sublime-settings")
        self.components = self.s.get("metadataObjects")
        self.components = sorted(self.components, key=lambda k : k['subscribe'])
        self.component_types = ["%s=>%s" % ("Subscribed" if c["subscribe"] else "Unsubscribed", 
            c["xmlName"]) for c in self.components]
        self.component_types = sorted(self.component_types)
        self.window.show_quick_panel(self.component_types, self.on_done)

    def on_done(self, index):
        if index == -1: return

        chosen_type = self.component_types[index].split("=>")[1]
        subscribe_type, is_subscribe = None, False
        for c in self.components:
            if c["xmlName"] == chosen_type:
                c["subscribe"] = is_subscribe = not c["subscribe"]
                subscribe_type = c["xmlName"]
                break

        self.s.set("metadataObjects", self.components)
        sublime.save_settings("toolingapi.sublime-settings")
        sublime.status_message("%s is %s" % (subscribe_type, 
            "subscribed" if is_subscribe else "unsubscribed"))

        if not is_subscribe: return
        settings = context.get_settings()
        _dir = os.path.join(settings["workspace"], "src", settings[chosen_type]["directoryName"])
        types = util.build_folder_types([_dir])
        processor.handle_refresh_folder(types)

class ReloadSobjectCacheCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ReloadSobjectCacheCommand, self).__init__(*args, **kwargs)

    def run(self):
        message = "Are you sure you really want to update sObject cache?"
        if not sublime.ok_cancel_dialog(message, "Confirm Reload?"): return
        processor.handle_reload_sobjects_completions()

class ReloadSymbolTableCacheCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ReloadSymbolTableCacheCommand, self).__init__(*args, **kwargs)

    def run(self):
        message = "Are you sure you really want to reload symbol table cache?"
        if not sublime.ok_cancel_dialog(message, "Confirm Reload"): return
        processor.handle_reload_symbol_tables()

class ClearSessionCacheCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ClearSessionCacheCommand, self).__init__(*args, **kwargs)

    def run(self):
        message = "Are you sure you really want to clear session?"
        if not sublime.ok_cancel_dialog(message, "Confirm Clear?"): return

        settings = context.get_settings()
        session_path = settings["workspace"]+"/.config/session.json"
        try:
            os.remove(session_path)
            sublime.status_message("Session cache is cleared")
        except:
            sublime.status_message("Session cache clear failed")

class ClearCacheCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ClearCacheCommand, self).__init__(*args, **kwargs)

    def run(self, cache_name):
        self.cache_name = cache_name+".sublime-settings"
        self.caches = util.get_sobject_caches(self.cache_name)
        if not self.caches:
            Printer.get('error').write("No cache already")
            return

        self.window.show_quick_panel(self.caches, self.on_done)

    def on_done(self, index):
        if index == -1: return
        message = "Are you sure you really want to clear this cache?"
        if not sublime.ok_cancel_dialog(message, "Confirm Clear"): return
        util.clear_cache(self.caches[index][1], self.cache_name)

class Convert15Id218IdCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(Convert15Id218IdCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.window.show_input_panel("Input 15 Id: ", 
            "", self.on_input, None, None)

    def on_input(self, input):
        c18Id = util.convert_15_to_18(input)
        Printer.get('log').write("Converted 18 Digit Id: " + c18Id);

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

    def is_enabled(self):
        return util.check_new_component_enabled()

class ExecuteRestTest(sublime_plugin.TextCommand):
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
        except ValueError as ve:
            Printer.get('error').write(str(ve))
            if not sublime.ok_cancel_dialog("Do you want to try again?", "Yes?"): return
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
        for ct in settings["subscribed_metadata_objects"]:
            if "suffix" not in settings[ct]: continue
            suffix = settings[ct]["suffix"]
            folder = settings[ct]["directoryName"]
            target_file = settings["workspace"] + "/src/%s/%s.%s" % (folder, sel_text, suffix)
            if os.path.isfile(target_file):
                self.view.window().open_file(target_file)

        if is_background: self.view.window().focus_view(self.view)

class SetCheckPointCommand(sublime_plugin.TextCommand):
    def run(self, edit, mark):
        sel = [s for s in self.view.sel()]
        self.view.add_regions(mark, sel, "invalid", "dot",
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
        message = "Are you sure you really want to refresh these folders"
        if not sublime.ok_cancel_dialog(message, "Refresh Folders"): return

        # Retrieve file from server
        processor.handle_refresh_folder(self.types)

    def is_visible(self, dirs):
        if not dirs: return False
        self.types = util.build_folder_types(dirs)
        if not self.types: return False

        return True

class RetrieveMetadataCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RetrieveMetadataCommand, self).__init__(*args, **kwargs)

    def run(self, retrieve_all=True):
        message = "Are your sure you really want to continue?"
        if not sublime.ok_cancel_dialog(message, "Retrieve Metadata"): return
        settings = context.get_settings()
        dirs = []
        if not retrieve_all:
            for c in ["CustomObject", "Workflow"]:
                metadata_folder = settings[c]["directoryName"]
                _dir = os.path.join(settings["workspace"], "src", metadata_folder)
                dirs.append(_dir)
        else:
            for c in settings["metadata_objects"]:
                metadata_folder = c["directoryName"]
                _dir = os.path.join(settings["workspace"], "src", metadata_folder)
                dirs.append(_dir)

        # Build folders_dict and Refresh these folder
        types = util.build_folder_types(dirs)
        processor.handle_refresh_folder(types, not retrieve_all)

class CreatePackageXml(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreatePackageXml, self).__init__(*args, **kwargs)

    def run(self, dirs):
        _dir = dirs[0]
        settings = context.get_settings()
        package_xml_content = """<?xml version="1.0" encoding="UTF-8"?>
            <Package xmlns="http://soap.sforce.com/2006/04/metadata">
                <types>
                    <members>*</members>
                    <name>ApexClass</name>
                </types>
                <version>{0}.0</version>
            </Package>
        """.format(settings["api_version"])
        file_name = os.path.join(_dir, "package.xml")
        if os.path.isfile(file_name):
            message = "Package.xml is already exist, override?"
            if not sublime.ok_cancel_dialog(message, "Override?"):
                return

        with open(file_name, "wb") as fp:
            fp.write(util.format_xml(package_xml_content))

        # If created succeed, just open it
        sublime.active_window().open_file(file_name)

    def is_visible(self, dirs):
        if not dirs or len(dirs) > 1: return False
        return True

class RetrievePackageXml(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RetrievePackageXml, self).__init__(*args, **kwargs)

    def run(self, files=None):
        _file = files[0]

        # Build types
        try:
            with open(_file, "rb") as fp:
                content = fp.read()
            types = util.build_package_types(content)
        except Exception as ex:
            Printer.get('error').write(str(ex))
            return

        # Initiate extract_to
        path, name = os.path.split(_file)
        time_stamp = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
        settings = context.get_settings()
        project_name = settings["default_project_name"]
        extract_to = os.path.join(path, project_name+"-"+time_stamp+"-"+name)

        # Start retrieve
        processor.handle_retrieve_package(types, extract_to)

    def is_visible(self, files=None):
        if not files: return False
        if files and len(files) > 1: return False
        if files and not files[0].endswith(".xml"): return False

        return True

class RetrievePackageFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Build types
        try:
            with open(self._file, "rb") as fp:
                content = fp.read()
            types = util.build_package_types(content)
        except Exception as ex:
            Printer.get('error').write(str(ex))
            return

        # Initiate extract_to
        path, name = os.path.split(self._file)
        time_stamp = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
        settings = context.get_settings()
        project_name = settings["default_project_name"]
        extract_to = os.path.join(path, project_name+"-"+time_stamp+"-"+name)

        # Start retrieve
        processor.handle_retrieve_package(types, extract_to)

    def is_visible(self):
        self._file = self.view.file_name()
        if not self._file: return False
        if not self._file.endswith(".xml"): return False

        return True

class RenameMetadata(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.window().show_input_panel("Input New Name", 
            "", self.on_input, None, None)

    def on_input(self, new_name):
        if not new_name or not re.match("\w+[a-zA-Z0-9]+", new_name):
            Printer.get('error').write("Input name is not valid")
            return

        processor.handle_rename_metadata(self.xml_name, self.filename, new_name)

    def is_enabled(self):
        if not self.view or not self.view.file_name(): return False
        self.settings = context.get_settings()
        base, filename = os.path.split(self.view.file_name())
        base, folder = os.path.split(base)
        if folder not in self.settings["metadata_folders"]:return False
        if not util.check_enabled(self.view.file_name(), check_cache=False): 
            return False

        self.filename = filename.split(".")[0]
        self.xml_name = self.settings[folder]["xmlName"]

        return True

class RetrieveFileFromServer(sublime_plugin.TextCommand):
    def run(self, edit):
        files = [self.view.file_name()]
        sublime.active_window().run_command("retrieve_files_from_server", {"files": files})

    def is_enabled(self):
        if not self.view or not self.view.file_name(): return False
        self.settings = context.get_settings()
        metadata_folder = util.get_meta_folder(self.view.file_name())
        if metadata_folder not in self.settings["metadata_folders"]: return False
        if not util.check_enabled(self.view.file_name(), check_cache=False): 
            return False

        return True

class RetrieveFilesFromServer(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RetrieveFilesFromServer, self).__init__(*args, **kwargs)

    def run(self, files):
        settings = context.get_settings()
        types = {}
        for _file in files:
            base, filename = os.path.split(_file)
            base, folder = os.path.split(base)

            name = filename.split(".")[0]
            xmlName = settings[folder]["xmlName"]
            if xmlName in types:
                types[xmlName].append(name)
            else:
                types[xmlName] = [name]

        processor.handle_retrieve_package(types, settings["workspace"], ignore_package_xml=True)

    def is_visible(self, files):
        if not files: return False
        settings = context.get_settings()
        for _file in files:
            if not os.path.isfile(_file): continue # Ignore folder
            metadata_folder = util.get_meta_folder(_file)
            if metadata_folder not in settings["metadata_folders"]: return False
            if not util.check_enabled(_file, check_cache=False): 
                return False

        return True

class CancelDeployment(sublime_plugin.TextCommand):
    def run(self, edit):
        processor.handle_cancel_deployment_thread(self.sel_text)

    def is_enabled(self):
        sel = self.view.sel()[0]
        self.sel_text = self.view.substr(self.view.word(sel.begin()))
        return self.sel_text.startswith("0Af")

class DestructFileFromServer(sublime_plugin.TextCommand):
    def run(self, edit):
        files = [self.view.file_name()]
        sublime.active_window().run_command("destruct_files_from_server", {"files": files})

    def is_enabled(self):
        if not self.view or not self.view.file_name(): return False
        self.settings = context.get_settings()
        metadata_folder = util.get_meta_folder(self.view.file_name())
        if metadata_folder not in self.settings["metadata_folders"]:return False
        if not util.check_enabled(self.view.file_name(), check_cache=False): 
            return False

        return True

class DestructFilesFromServer(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DestructFilesFromServer, self).__init__(*args, **kwargs)

    def run(self, files):
        message = "Are you sure you really want to destruct these files?"
        if not sublime.ok_cancel_dialog(message, "Destruct Files From Server"): return
        processor.handle_destructive_files(files)

    def is_visible(self, files):
        if len(files) == 0: return False
        self.settings = context.get_settings()
        for _file in files:
            if not os.path.isfile(_file): continue # Ignore folder
            _folder = util.get_meta_folder(_file)
            if _folder not in self.settings["metadata_folders"]: return False
            if not util.check_enabled(_file, check_cache=False): 
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
            Printer.get("error").write("Invalid Zip File")
            return

        processor.handle_deploy_thread(util.base64_encode(zipfile_path))

class DeployOpenFilesToServer(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DeployOpenFilesToServer, self).__init__(*args, **kwargs)

    def run(self):
        # Get the package path to deploy
        sublime.active_window().run_command("deploy_files_to_server", 
            {"files": self.files})

    def is_enabled(self):
        """
        1. You must have selected one file or more
        2. All selected file should be in predefined meta folders
        """

        # If no views, just disable this command
        views = sublime.active_window().views();
        if not views or len(views) == 0: return False

        self.settings = context.get_settings()
        self.files = [];
        for _view in views:
            _file = _view.file_name()
            if not _file or not os.path.isfile(_file): continue # Ignore folder
            _folder = util.get_meta_folder(_file) # Ignore non-sfdc files
            if _folder not in self.settings["metadata_folders"]:
                continue

            self.files.append(_file)

        # If there is no sfdc code file, just disable this command
        if not self.files: return False

        return True

class DeployPackageToServerCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DeployPackageToServerCommand, self).__init__(*args, **kwargs)

    def run(self, dirs):
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

    def is_visible(self, dirs):
        if not dirs: return False
        if len(dirs) > 1: return False

        if os.path.exists(dirs[0]+"/package.xml"):
            self.package_dir = dirs[0]
        elif os.path.exists(dirs[0]+"/src/package.xml"):
            self.package_dir = dirs[0] + "/src"
        else:
            return False

        return True

class DeployFileToServer(sublime_plugin.TextCommand):
    def run(self, edit):
        files = [self.view.file_name()]
        sublime.active_window().run_command("deploy_files_to_server", {"files": files})

    def is_enabled(self):
        if not self.view or not self.view.file_name(): return False
        self.settings = context.get_settings()
        _folder = util.get_meta_folder(self.view.file_name())
        if _folder not in self.settings["metadata_folders"]:
            return False

        return True

class DeployFilesToServer(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DeployFilesToServer, self).__init__(*args, **kwargs)

    def run(self, files):
        # Before deploy, save files to local
        # Enhancement for issue #67
        for _file in files:
            view = util.get_view_by_file_name(_file)
            if not view: continue
            view.run_command("save")

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

    def is_visible(self, files):
        """
        1. You must have selected one file or more
        2. All selected file should be in predefined meta folders
        """

        if len(files) == 0: return False
        self.settings = context.get_settings()
        for _file in files:
            if not os.path.isfile(_file): continue # Ignore folder
            _folder = util.get_meta_folder(_file)
            if _folder not in self.settings["metadata_folders"]:
                return False

        return True

class ExportProfile(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportProfile, self).__init__(*args, **kwargs)

    def run(self):
        import threading
        thread = threading.Thread(target=util.export_profile_settings)
        thread.start()

    def is_enabled(self):
        return util.check_new_component_enabled()

class ExportValidationRulesCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportValidationRulesCommand, self).__init__(*args, **kwargs)

    def run(self):
        settings = context.get_settings()
        workflow_path = settings["workspace"] + "/src/objects"
        if not os.path.exists(workflow_path):
            Printer.get('error').write(message.METADATA_CHECK)
            return

        processor.handle_export_validation_rules(settings)

    def is_enabled(self):
        return util.check_new_component_enabled()

class ExportCustomLablesCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportCustomLablesCommand, self).__init__(*args, **kwargs)

    def run(self):
        settings = context.get_settings()
        workspace = settings["workspace"]
        lable_path = workspace + "/src/labels/CustomLabels.labels"
        if not os.path.isfile(lable_path):
            Printer.get('error').write(message.METADATA_CHECK)
            return

        outputdir = settings["workspace"] + "/.export/labels"
        if not os.path.exists(outputdir): os.makedirs(outputdir)
        lables = xmltodict.parse(open(lable_path, "rb").read())
        util.list2csv(outputdir+"/Labels.csv", lables["CustomLabels"]["labels"])

    def is_enabled(self):
        return util.check_new_component_enabled()

class ExportWorkflowsCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportWorkflowsCommand, self).__init__(*args, **kwargs)

    def run(self):
        settings = context.get_settings()
        workspace = settings["workspace"]
        workflow_path = workspace + "/src/workflows"
        if not os.path.exists(workflow_path):
            Printer.get('error').write(message.METADATA_CHECK)
            return

        processor.handle_export_workflows(settings)

    def is_enabled(self):
        return util.check_new_component_enabled()

class ExportCustomFieldCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportCustomFieldCommand, self).__init__(*args, **kwargs)

    def run(self):
        util.check_workspace_available()
        processor.handle_export_customfield()
        
    def is_enabled(self):
        return util.check_new_component_enabled()

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
            processor.handle_export_all_workbooks(5)
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
                    if not sublime.ok_cancel_dialog(message, "Continue?"): return
                    self.window.show_input_panel("Sobjects(* means all, or sobjects seprated with semi-colon)", 
                        input, self.on_input, None, None)
                    return

            # After ensured input is valid, just start to generate workbooks
            processor.handle_export_specified_workbooks(sobjects)

    def is_enabled(self):
        return util.check_new_component_enabled()

class ViewComponentInSfdcCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ViewComponentInSfdcCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.all_components = util.populate_all_components()
        if not self.all_components:
            Printer.get("error").write("No components cache")
            return

        self.all_components_name = sorted(list(self.all_components.keys()))
        self.window.show_quick_panel(self.all_components_name, self.on_done)

    def on_done(self, index):
        if index == -1: return
        class_id = self.all_components[self.all_components_name[index]]
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
        self.classes_attr = util.populate_components("ApexClass")
        self.classmap = {}
        for key in self.classes_attr:
            if not self.classes_attr[key]["is_test"]: continue
            self.classmap[self.classes_attr[key]["name"]] = key

        if not self.classmap:
            Printer.get('error').write("No Test Class");
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
        if not file_name or not file_name.endswith(".cls"): return False
        if not util.check_enabled(file_name): return False

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

    def run(self, track_self=False):
        if track_self:
            processor.handle_create_debug_log('Me', None)
            return
            
        self.users = processor.populate_users()
        if not self.users: return # Network Issue Cause
        self.users_name = sorted(self.users.keys(), reverse=False)
        self.window.show_quick_panel(self.users_name, self.on_done)

    def on_done(self, index):
        if index == -1: return

        user_name = self.users_name[index]
        user_id = self.users[user_name]
        processor.handle_create_debug_log(user_name, user_id)

class FetchDebugLogCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(FetchDebugLogCommand, self).__init__(*args, **kwargs)

    def run(self, fetch_self=False):
        if fetch_self:
            processor.handle_fetch_debug_logs('Me', None)
            return

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
        session = util.get_session_info(settings)

        # If .config/session.json is exist, just use frontdoor method
        if not session:
            show_params = {
                "un": settings["username"],
                "pw": settings["password"],
                "startURL": startURL
            }
            show_params = urllib.parse.urlencode(show_params)
            show_url = settings["login_url"] + '?%s' % show_params

        # If .config/session.json is not exist, use credentials to login
        else:
            show_url = "%s/secur/frontdoor.jsp?sid=%s&retURL=%s" % (
                session["instance_url"], session["session_id"], startURL
            )

        util.open_with_browser(show_url)

class AboutCommand(sublime_plugin.ApplicationCommand):
    def run(command):
        package_info = sublime.load_settings("package.sublime-settings")

        version_info = "\n%s\n\n%s\n\nCopyright © 2013-2015 By %s\n\tDev Channel, Build v%s" % (
            package_info.get("description"),
            package_info.get("homepage"),
            package_info.get("author"),
            package_info.get("version")
        )
        sublime.message_dialog(version_info)

class ReportIssueCommand(sublime_plugin.ApplicationCommand):
    def run(command):
        show_url = "https://github.com/xjsender/haoide/issues"
        util.open_with_browser(show_url)

class ViewReleaseNotesCommand(sublime_plugin.ApplicationCommand):
    def run(command):
        show_url = "https://github.com/xjsender/haoide/blob/master/HISTORY.rst"
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
    confirm = sublime.ok_cancel_dialog("Are you sure you really want to delete this?")
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

    def run(self, template_name=None,
                  component_name=None, 
                  component_type=None, 
                  markup_or_body=None, 
                  sobject_name=None):
        self.template_name = template_name
        self.component_name = component_name
        self.component_type = component_type
        self.markup_or_body = markup_or_body
        self.sobject_name = sobject_name

        template_settings = sublime.load_settings("template.sublime-settings")
        self.templates = template_settings.get("template")
        templates = self.templates[self.component_type]
        self.template_names = [[n, templates[n]["description"]] for n in templates]

        # After input # in visualforce page, we can get 
        # the component name and template name, no need to choose again
        if self.component_name and self.template_name: 
            self.template_attr = templates[self.template_name]
            self.create_component()
        else:
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

        if self.component_name:
            self.create_component()
        else:
            self.window.show_input_panel("Please Input Name: ", "", self.on_input, None, None)

    def on_input(self, input):
        # Create component to local according to user input
        if not re.match('^[a-zA-Z]+\\w+$', input):
            message = 'Invalid format, do you want to try again?'
            if not sublime.ok_cancel_dialog(message, "Try Again?"): return
            self.window.show_input_panel("Please Input Name: ", "", self.on_input, None, None)
            return
        
        self.component_name = input
        self.create_component()

    def create_component(self):
        extension = self.template_attr["extension"]
        body = self.template_attr["body"]
        if extension == ".trigger":
            body = body.replace("trigger_name", self.component_name).replace("sobject_name", self.sobject_name)
        elif extension == ".cls":
            body = body.replace("class_name", self.component_name)

        self.settings = context.get_settings()
        workspace = self.settings["workspace"]
        component_outputdir = os.path.join(workspace, "src", self.settings[self.component_type]["directoryName"])
        if not os.path.exists(component_outputdir):
            os.makedirs(component_outputdir)
            self.settings = context.get_settings()
            util.add_project_to_workspace(self.settings)

        file_name = "%s/%s" % (component_outputdir, self.component_name + extension)
        if os.path.isfile(file_name):
            message = '"%s" is already exist, do you want to try again?' % self.component_name
            if not sublime.ok_cancel_dialog(message, "Continue?"): return
            self.window.show_input_panel("Please Input Name: ", "", self.on_input, None, None)
            return

        with open(file_name, "w") as fp:
            fp.write(body)

        # In windows, new file is not shown in the sidebar, 
        # we need to refresh the sublime workspace to show it
        sublime.active_window().run_command("refresh_folder_list")

        # Build Post body
        data = {
            "name": self.component_name, self.markup_or_body: body
        }

        if self.component_type == "ApexClass":
            data["IsValid"] = True
        elif self.component_type == "ApexTrigger":
            data["TableEnumOrId"] = self.sobject_name
        elif self.component_type in ["ApexPage", "ApexComponent"]:
            data["MasterLabel"] = self.component_name

        processor.handle_create_component(data, self.component_name, 
                                                self.component_type, 
                                                self.markup_or_body, 
                                                file_name)

class DeployLightingElementToServer(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.view.is_dirty(): self.view.run_command("save")
        processor.handle_deploy_thread(util.build_aura_package([self.lightning_dir]))

    def is_visible(self):
        if not self.view or not self.view.file_name(): return False
        self.settings = context.get_settings()
        _file = self.view.file_name()
        self.lightning_dir, lighting_component_name = os.path.split(_file)
        aura_path, lighting_name = os.path.split(self.lightning_dir)
        base, meta_type = os.path.split(aura_path)

        if meta_type != "aura": return False
        if self.settings["default_project_name"] not in _file:
            return False

        return True

class DeployLightingToServer(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DeployLightingToServer, self).__init__(*args, **kwargs)

    def run(self, dirs, switch_project=True):
        # Get the package path to deploy
        self.dirs = dirs

        if not switch_project:
            base64_package = util.build_aura_package(dirs)
            processor.handle_deploy_thread(base64_package)
            return

        # Choose the target ORG to deploy
        self.settings = context.get_settings()
        self.projects = self.settings["projects"]
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

        base64_package = util.build_aura_package(self.dirs)
        processor.handle_deploy_thread(base64_package)

    def is_visible(self, dirs, switch_project=True):
        if not dirs or len(dirs) == 0: return False

        self.settings = context.get_settings()
        for _dir in dirs:
            base, aura_name = os.path.split(_dir)
            base, meta_type = os.path.split(base)
            if meta_type != "aura": return False
            if self.settings["default_project_name"] not in _dir:
                return False

        return True

class PreviewLightingAppInServer(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(PreviewLightingAppInServer, self).__init__(*args, **kwargs)

    def run(self):
        self.aura_attrs = util.populate_lighting_applications()
        self.app_names = list(self.aura_attrs.keys())
        self.window.show_quick_panel(self.app_names, self.on_chosen)

    def on_chosen(self, index):
        if index == -1: return
        app_name = self.app_names[index]
        app_attr = self.aura_attrs[app_name]

        settings = context.get_settings()
        session = util.get_session_info(settings)
        instance_url = session["instance_url"]
        instance = instance_url[8:instance_url.index(".")]
        if instance == "emea": instance = "eu0"
        start_url = "https://%s.lightning.force.com/%s/%s.app" % (
            instance, app_attr["namespacePrefix"], app_name
        )
        self.window.run_command("login_to_sfdc", {"startURL": start_url})

class RetrieveLightingFromServer(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RetrieveLightingFromServer, self).__init__(*args, **kwargs)

    def run(self, dirs):
        processor.handle_retrieve_package(
            self.types, 
            self.settings["workspace"], 
            ignore_package_xml=True
        )

    def is_visible(self, dirs):
        if len(dirs) == 0: return False
        self.settings = context.get_settings()
        self.types = {}
        for _dir in dirs:
            if os.path.isfile(_dir): continue
            base, _name = os.path.split(_dir)
            base, _folder = os.path.split(base)

            # Check Metadata Type
            if _folder != "aura": continue

            # Check Project Name
            pn = self.settings["default_project_name"]
            if pn not in _dir: continue

            if "AuraDefinitionBundle" in self.types:
                self.types["AuraDefinitionBundle"].append(_name)
            else:
                self.types["AuraDefinitionBundle"] = [_name]
        
        # Check whether any aura components are chosen
        if not self.types: return False

        return True

class DestructLightingFromServer(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DestructLightingFromServer, self).__init__(*args, **kwargs)

    def run(self, dirs):
        confirm = sublime.ok_cancel_dialog("Are you sure you really want to continue?")
        if not confirm: return
        processor.handle_destructive_files(dirs, ignore_folder=False)

    def is_visible(self, dirs):
        if len(dirs) == 0: return False
        self.settings = context.get_settings()
        for _dir in dirs:
            base, name = os.path.split(_dir)
            base, _folder = os.path.split(base)
            if _folder != "aura": return False
            if not util.check_enabled(_dir, check_cache=False): 
                return False

        return True

class CreateLightingElement(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateLightingElement, self).__init__(*args, **kwargs)

    def run(self, dirs, element=""):
        """ element: Component, Controller, Helper, Style, Documentation, Render
        """

        # Get template attribute
        template_settings = sublime.load_settings("template.sublime-settings")
        template = template_settings.get("template").get("AuraEelement").get(element)
        extension = template["extension"]
        body = template["body"]

        # JS Component is different with others
        element_name = "%s%s%s" % (
            self.aura_name,
            element if extension == ".js" else "", 
            extension
        )

        # Combine Aura element component name
        element_file = os.path.join(self._dir, element_name)

        # If element file is already exist, just alert
        if os.path.isfile(element_file):
            Printer.get('error').write(element_name+" is already exist")
            return

        # Create Aura Element file
        with open(element_file, "w") as fp:
            fp.write(body)

        # If created succeed, just open it and refresh project
        window = sublime.active_window()
        window.open_file(element_file)
        window.run_command("refresh_folder_list")

        # Deploy Aura to server
        self.window.run_command("deploy_lighting_to_server", {
            "dirs": [self._dir],
            "switch_project": False
        })

    def is_visible(self, dirs, element=""):
        if not dirs or len(dirs) != 1: return False
        self._dir = dirs[0]

        # Check whether project is the active one
        settings = context.get_settings()
        if settings["default_project_name"] not in self._dir:
            return False

        base, self.aura_name = os.path.split(self._dir)
        base, meta_type = os.path.split(base)
        if meta_type != "aura": return False

        lighting_extensions = []
        for dirpath, dirnames, filenames in os.walk(self._dir):
            for filename in filenames:
                extension = filename[filename.find("."):]
                lighting_extensions.append(extension)

        # Just Component and Application can have child elements
        if ".cmp" in lighting_extensions or ".app" in lighting_extensions:
            return True

        return False

class CreateLightingDefinition(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateLightingDefinition, self).__init__(*args, **kwargs)

    def run(self, _type=""):
        self._type = _type
        self.window.show_input_panel("Please Input Lighting Name: ", 
            "", self.on_input, None, None)

    def on_input(self, lighting_name):
        # Create component to local according to user input
        if not re.match('^[a-zA-Z]+\\w+$', lighting_name):
            message = 'Invalid format, do you want to try again?'
            if not sublime.ok_cancel_dialog(message): return
            self.window.show_input_panel("Please Input Lighting Name: ", 
                "", self.on_input, None, None)
            return

        # Get template attribute
        template_settings = sublime.load_settings("template.sublime-settings")
        template = template_settings.get("template").get("Aura").get(self._type)

        # Build dir for new lighting component
        settings = context.get_settings()
        component_dir = os.path.join(settings["workspace"], "src", "aura", lighting_name)
        if not os.path.exists(component_dir):
            os.makedirs(component_dir)
        else:
            message = lighting_name+" is already exist, do you want to try again?"
            if not sublime.ok_cancel_dialog(message, "Try Again?"): return
            self.window.show_input_panel("Please Input Lighting Name: ", 
                "", self.on_input, None, None)
            return
        
        lihghting_file = os.path.join(component_dir, lighting_name+template["extension"])

        # Create Aura lighting file
        with open(lihghting_file, "w") as fp:
            fp.write(template["body"])

        # If created succeed, just open it and refresh project
        window = sublime.active_window()
        window.open_file(lihghting_file)
        window.run_command("refresh_folder_list")

        # Deploy Aura to server
        self.window.run_command("deploy_lighting_to_server", {
            "dirs": [component_dir],
            "switch_project": False
        })

class CreateLightingApplication(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateLightingApplication, self).__init__(*args, **kwargs)

    def run(self):
        self.window.run_command("create_lighting_definition", {
            "_type": "Application"
        })

    def is_enabled(self):
        return util.check_new_component_enabled()

class CreateLightingComponent(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateLightingComponent, self).__init__(*args, **kwargs)

    def run(self):
        self.window.run_command("create_lighting_definition", {
            "_type": "Component"
        })

    def is_enabled(self):
        return util.check_new_component_enabled()

class CreateLightingInterface(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateLightingInterface, self).__init__(*args, **kwargs)

    def run(self):
        self.window.run_command("create_lighting_definition", {
            "_type": "Interface"
        })

    def is_enabled(self):
        return util.check_new_component_enabled()

class CreateLightingEvent(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateLightingEvent, self).__init__(*args, **kwargs)

    def run(self):
        self.window.run_command("create_lighting_definition", {
            "_type": "Event"
        })

    def is_enabled(self):
        return util.check_new_component_enabled()

class SaveComponentCommand(sublime_plugin.TextCommand):
    def run(self, edit, is_check_only=False):
        # Automatically save current file if dirty
        if self.view.is_dirty():
            self.view.run_command("save")

        # Handle Save Current Component
        processor.handle_save_component(self.view.file_name(), is_check_only)

    def is_enabled(self):
        if not self.view or not self.view.file_name(): return False
        _folder = util.get_meta_folder(self.view.file_name())
        if _folder not in ["classes", "components", "pages", "triggers"]:
            return False
            
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

    def is_enabled(self):
        return util.check_new_component_enabled()

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
        message = "Are you sure you really want to update this project?"
        if not sublime.ok_cancel_dialog(message, "Update Project?"): return
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
        if sublime.platform() == "osx" and "c:/salesforce/workspace" in settings["workspace"]:
            sublime.active_window().open_file(sublime.packages_path()+"/User/toolingapi.sublime-settings")
            message = "Do you want to take a look at how to config your workspace"
            if not sublime.ok_cancel_dialog(message, "Go to Github"): return
            util.open_with_browser("https://github.com/xjsender/haoide#worspace")
            return

        dpn = settings["default_project"]["project_name"]
        message = "Are you sure you really want to create new project for %s?" % dpn
        if not sublime.ok_cancel_dialog(message, "Create New Project?"): return
        
        util.add_project_to_workspace(settings)
        processor.handle_new_project(settings)

class ExtractToHere(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExtractToHere, self).__init__(*args, **kwargs)

    def run(self, files):
        extract_to, name = os.path.split(self._file)
        name, extension = name.split(".")

        extract_to = os.path.join(extract_to, name)
        util.extract_zipfile(self._file, extract_to)

    def is_visible(self, files):
        if not files or len(files) > 1: 
            return False

        self._file = files[0]
        try:
            base, name = os.path.split(self._file)
            name, extension = name.split(".")
            if extension not in ["zip", "resource"]:
                return False
        except:
            return False

        return True

class UpdateStaticResource(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(UpdateStaticResource, self).__init__(*args, **kwargs)

    def run(self, dirs):
        base64_package = util.compress_resource_folder(self.resource_dir)
        processor.handle_deploy_thread(base64_package)

    def is_visible(self, dirs):
        if not dirs or len(dirs) > 1: return False
        self.resource_dir = dirs[0]

        static_resource_folder, resource_name = os.path.split(self.resource_dir)
        if not static_resource_folder.endswith("staticresources"):
            return False

        return True

class RefreshComponentCommand(sublime_plugin.TextCommand):
    def run(self, view):
        message = "Are you sure you want to continue?"
        if not sublime.ok_cancel_dialog(message, "Refresh This?"): return
    
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
        message = "Are you sure you really want to continue?"
        if not sublime.ok_cancel_dialog(message, "Refresh Selected?"): return

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