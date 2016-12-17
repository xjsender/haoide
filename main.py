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
import xml
import urllib.request

from . import requests
from . import processor
from . import context
from . import util


from .salesforce.lib import xmlformatter
from .salesforce.lib.jsontoapex import JSONConverter
from .salesforce.lib.panel import Printer
from .salesforce import xmltodict
from .salesforce import message


class RemoveComments(sublime_plugin.TextCommand):
    def run(self, edit):
        comments = self.view.find_by_selector('comment')
        for region in reversed(comments):
            region = self.view.full_line(region)
            self.view.erase(edit, region)

class Haoku(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(Haoku, self).__init__(*args, **kwargs)

    def run(self, router=""):
        settings = context.get_settings()
        session = util.get_session_info(settings)
        if not session:
            Printer.get("error").write("Please Login Firstly")
            return

        heroku_host = "https://haoku.herokuapp.com"
        # heroku_host = "http://localhost:3000"
        show_params = {
            "accessToken": session["session_id"],
            "instanceUrl": session["instance_url"],
            "username": settings["username"],
            "router": router
        }

        show_params = urllib.parse.urlencode(show_params)
        open_url = heroku_host + '?%s' % show_params
        util.open_with_browser(open_url)

class BaseSelection(object):
    def is_enabled(self):
        if not self.view.size(): return False
        self.selection = self.view.substr(self.view.sel()[0])
        if not self.selection:
            self.selection = self.view.substr(sublime.Region(0, 
                self.view.size()))

        return True

class BuildCustomLabelsMetadata(sublime_plugin.TextCommand):
    def run(self, edit):
        try:
            file_name = self.view.file_name()
            lables_metadata = util.build_metadata(file_name, {
                "root": "CustomLabels",
                "leaf": "labels",
                "xmlNodes": [
                    "shortDescription", "fullName",
                    "categories", "protected",
                    "language", "value"
                ]
            })

            formatter = xmlformatter.Formatter(indent=4)
            lables_metadata = formatter.format_string(lables_metadata)
        except ValueError as ve:
            return Printer.get('error').write(str(ve))
            
        view = sublime.active_window().new_file()
        view.set_syntax_file("Packages/XML/XML.tmLanguage")
        view.run_command("new_view", {
            "name": "CustomLabels.labels",
            "input": lables_metadata.decode("utf-8")
        })

class BuildCustomLabelsTranslationMetadata(sublime_plugin.TextCommand):
    def run(self, edit):
        try:
            file_name = self.view.file_name()
            translations = util.build_metadata(file_name, {
                "root": "Translations",
                "leaf": "customLabels",
                "xmlNodes": ["name", "label"]
            })

            formatter = xmlformatter.Formatter(indent=4)
            translations = formatter.format_string(translations)
        except ValueError as ve:
            raise ve
            return Printer.get('error').write(str(ve))
            
        view = sublime.active_window().new_file()
        view.set_syntax_file("Packages/XML/XML.tmLanguage")
        view.run_command("new_view", {
            "name": "Translations.translation",
            "input": translations.decode("utf-8")
        })

class JsonFormat(BaseSelection, sublime_plugin.TextCommand):
    def run(self, edit):
        try:
            formatted_json = json.dumps(json.loads(self.selection), 
                ensure_ascii=False, indent=4)
        except ValueError as ve:
            return Printer.get('error').write(str(ve))
            
        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": "FormattedJSON",
            "input": formatted_json
        })

class JsonSerialization(BaseSelection, sublime_plugin.TextCommand):
    def run(self, edit):
        try:
            self.data = json.loads(self.selection)
        except ValueError as ve:
            return Printer.get('error').write(str(ve))

        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": "SerializedJSON",
            "input": json.dumps(self.data)
        })

class JsonToApex(BaseSelection, sublime_plugin.TextCommand):
    def run(self, edit):
        try:
            self.data = json.loads(self.selection)
        except ValueError as ve:
            return Printer.get('error').write(str(ve))

        sublime.active_window().show_input_panel("Input Class Name: ", 
            "JSON2Apex", self.on_input_name, None, None)
        
    def on_input_name(self, name):
        if not name: name = "JSON2Apex"

        # Start converting
        snippet = JSONConverter(scope="global").convert2apex(name, self.data).snippet
        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": "JSON2APEX",
            "input": snippet
        })

class JsonToXml(BaseSelection, sublime_plugin.TextCommand):
    def run(self, edit):
        try:
            data = json.loads(self.selection)
            result = xmltodict.unparse(data)
        except ValueError as ve:
            return Printer.get("error").write(str(ve))
        except xml.parsers.expat.ExpatError as ex:
            return Printer.get("error").write(str(ex))

        new_view = sublime.active_window().new_file()
        new_view.set_syntax_file("Packages/XML/XML.tmLanguage")
        new_view.run_command("new_view", {
            "name": "JSON2XML",
            "input": util.format_xml(result).decode("UTF-8")
        })

class XmlToJson(BaseSelection, sublime_plugin.TextCommand):
    def run(self, edit):
        try:
            result = xmltodict.parse(self.selection)
        except xml.parsers.expat.ExpatError as ex:
            message = "You should open a XML file or choose any valid XML content"
            if "line 1, column 0" in str(ex):
                return Printer.get("error").write(message)
            return Printer.get("error").write(str(ex))

        new_view = sublime.active_window().new_file()
        new_view.run_command("new_view", {
            "name": "XML2JSON",
            "input": json.dumps(result, indent=4)
        })

class XmlFormat(BaseSelection, sublime_plugin.TextCommand):
    def run(self, edit):
        try:
            formatter = xmlformatter.Formatter(indent=4)
            formatted_xml = formatter.format_string(self.selection)
        except xml.parsers.expat.ExpatError as ex:
            message = "You should open a XML file or choose any valid XML content"
            if "line 1, column 0" in str(ex):
                return Printer.get("error").write(message)
            return Printer.get("error").write(str(ex))

        new_view = sublime.active_window().new_file()
        new_view.set_syntax_file("Packages/XML/XML.tmLanguage")
        new_view.run_command("new_view", {
            "name": "XMLFormat",
            "input": formatted_xml.decode("utf-8")
        })

class DiffWithServer(sublime_plugin.TextCommand):
    def run(self, edit, switch=True, source_org=None):
        if not source_org:
            source_org = self.settings["default_project_name"]
        
        if switch:
            return self.view.window().run_command("switch_project", {
                "callback_options": {
                    "callback_command": "diff_with_server", 
                    "args": {                        
                        "switch": False,
                        "source_org": source_org
                    }
                }
            })
        
        file_name = self.view.file_name()
        attr = util.get_component_attribute(file_name, False, reload_cache=True)[0]

        # If this component is not exist in chosen project, just stop
        if not attr:
            Printer.get("error").write("This component is not exist in chosen project")
            return util.switch_project(source_org)

        processor.handle_diff_with_server(attr, file_name, source_org)

    def is_enabled(self):
        self.file_name = self.view.file_name()
        if not self.file_name: 
            return False

        self.settings = context.get_settings()
        self.attributes = util.get_file_attributes(self.file_name)
        if self.attributes["metadata_folder"] not in ["classes", "triggers", "pages", "components"]:
            return False

        return True

    def is_visible(self):
        return self.is_enabled()

class ShowMyPanel(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ShowMyPanel, self).__init__(*args, **kwargs)

    def run(self, panel):
        Printer.get(panel).show_panel()

class ToggleMetadataObjects(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ToggleMetadataObjects, self).__init__(*args, **kwargs)

    def run(self, callback_options={}):
        self.settings = context.get_settings()
        self.callback_options = callback_options
        described_metadata = util.get_described_metadata(self.settings)
        if not described_metadata:
            return self.window.run_command("describe_metadata", {
                "callback_options": {
                    "callback_command": "toggle_metadata_objects"
                }
            })

        self.metadata_objects = described_metadata["metadataObjects"]
        smo = self.settings["subscribed_metadata_objects"]

        # Key pair between item and metdataObjects
        self.item_property = {}

        # Add all metadata objects to list
        has_subscribed = False
        subscribed_items = []
        unsubscripted_items = []
        for mo in self.metadata_objects:
            if mo["xmlName"] in smo:
                item = "%s[√] %s" % (" " * 4, mo["xmlName"])
                subscribed_items.append(item)
                has_subscribed = True
            else:
                item = "%s[x] %s" % (" " * 4, mo["xmlName"])
                unsubscripted_items.append(item)
            self.item_property[item] = mo["xmlName"]

        # Add item `Select All` to list
        item_all = "[%s] All" % ("√" if has_subscribed else "x")
        self.items = [item_all]
        self.item_property[item_all] = [m["xmlName"] for m in self.metadata_objects]

        # Add subscribed ones and unsubscribed ones to list
        self.items.extend(sorted(subscribed_items))
        self.items.extend(sorted(unsubscripted_items))
        self.window.show_quick_panel(self.items, self.on_done, 
            sublime.MONOSPACE_FONT)

    def on_done(self, index):
        if index == -1:
            if "callback_command" in self.callback_options:
                self.window.run_command(self.callback_options["callback_command"])
            return

        # Get chosen type
        chosen_item = self.items[index]
        chosen_metadata_objects = self.item_property[chosen_item]

        # Get already subscribed metadata objects
        s = sublime.load_settings(context.TOOLING_API_SETTINGS)
        projects = s.get("projects")
        default_project = projects[self.settings["default_project_name"]]
        if "subscribed_metadata_objects" in default_project:
            subscribed_metadata_objects = default_project["subscribed_metadata_objects"]
        else:
            subscribed_metadata_objects = []

        # Assign new subscribed metadata objects to subscribed list
        if isinstance(chosen_metadata_objects, list):
            # If already subscribed all, and we click choose all item,
            # all subscribed ones will be unsubscripted
            if len(subscribed_metadata_objects) == len(self.metadata_objects):
                subscribed_metadata_objects = []
            else:
                subscribed_metadata_objects = chosen_metadata_objects
        elif isinstance(chosen_metadata_objects, str):
            if chosen_metadata_objects in subscribed_metadata_objects:
                subscribed_metadata_objects.remove(chosen_metadata_objects)
            else:
                subscribed_metadata_objects.append(chosen_metadata_objects)

        default_project["subscribed_metadata_objects"] = subscribed_metadata_objects
        projects[self.settings["default_project_name"]] = default_project

        # Save the updated settings
        s.set("projects", projects)
        sublime.save_settings(context.TOOLING_API_SETTINGS)

        sublime.set_timeout(lambda:sublime.active_window().run_command("toggle_metadata_objects", {
            "callback_options": self.callback_options
        }), 10)

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
        self.cache_name = cache_name
        self.cache_settings = self.cache_name+".sublime-settings"
        self.caches = util.get_sobject_caches(self.cache_settings)
        if not self.caches:
            Printer.get('error').write("No cache already")
            return

        self.window.show_quick_panel(self.caches, self.on_done)

    def on_done(self, index):
        if index == -1: return
        message = "Are you sure you really want to clear this cache?"
        if not sublime.ok_cancel_dialog(message, "Confirm Clear"): return
        util.clear_cache(self.caches[index][1], self.cache_settings)

        sublime.set_timeout(lambda:sublime.active_window().run_command("clear_cache", {
            "cache_name": self.cache_name
        }), 10)

class Convert15Id218Id(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(Convert15Id218Id, self).__init__(*args, **kwargs)

    def run(self):
        self.window.show_input_panel("Input 15 Id: ", 
            "", self.on_input, None, None)

    def on_input(self, input):
        c18Id = util.convert_15_to_18(input)
        Printer.get('log').write("Converted 18 Digit Id: " + c18Id);

class DecodeUrl(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DecodeUrl, self).__init__(*args, **kwargs)

    def run(self):
        self.window.show_input_panel("Input your URL to be decoded: ", 
            "", self.on_input, None, None)

    def on_input(self, input):
        decodedUrl = urllib.request.unquote(input)
        Printer.get('log').write("Decoded URL: " + decodedUrl);

class EncodeUrl(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(EncodeUrl, self).__init__(*args, **kwargs)

    def run(self):
        self.window.show_input_panel("Input your URL to be encoded: ", 
            "", self.on_input, None, None)

    def on_input(self, input):
        encodedUrl = urllib.request.quote(input)
        Printer.get('log').write("Encoded URL: " + encodedUrl);

class GenerateSoqlCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(GenerateSoqlCommand, self).__init__(*args, **kwargs)

    def run(self):
        sobjects_describe = util.populate_sobjects_describe()
        self.sobjects = sorted(sobjects_describe.keys())
        self.window.show_quick_panel(self.sobjects, self.on_done)

    def on_done(self, index):
        if index == -1: return
        self.sobject = self.sobjects[index]

        self.filters = ["all", "updateable", "createable", "custom"]
        self.display_filters = [a.capitalize() for a in self.filters]
        sublime.set_timeout(lambda:self.window.show_quick_panel(self.display_filters, self.on_choose_action), 10)

    def on_choose_action(self, index):
        if index == -1: return
        processor.handle_generate_sobject_soql(self.sobject, self.filters[index])

class ExportQueryToCsv(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportQueryToCsv, self).__init__(*args, **kwargs)

    def run(self, tooling=False):
        self.tooling = tooling
        sublime.active_window().show_input_panel('Input Your %s SOQL:' % 
            ('Tooling' if tooling else ''), "", self.on_input_soql, None, None)

    def on_input_soql(self, soql):
        self.soql = soql

        # Check whether the soql is valid and not parent-to-child query
        match = re.match("SELECT\\s+[*\\w\\n,.:_\\s()]+\\s+FROM\\s+\\w+", 
            self.soql, re.IGNORECASE)
        if not match:
            Printer.get("error").write("Your input SOQL is not valid")
            if sublime.ok_cancel_dialog("Want to try again?"):
                self.window.show_input_panel('Input Your SOQL:', 
                    "", self.on_input_soql, None, None)
            return 

        # If () in match, it means there has parent-to-child query
        if "(" in match.group(0):
            Printer.get("error").write("This feature does not support parent-to-child query")
            if sublime.ok_cancel_dialog("Want to try again?"):
                self.window.show_input_panel('Input Your SOQL:', 
                    "", self.on_input_soql, None, None)
            return 

        # Parse the sObject Name for CSV name
        matchstr = match.group(0)
        self.sobject = matchstr[matchstr.rfind(" ")+1:]

        sublime.active_window().show_input_panel('Input CSV Name:', 
            self.sobject, self.on_input_name, None, None)

    def on_input_name(self, name):
        if not name: return
        processor.handle_export_query_to_csv(self.tooling, self.soql, name)

class ExportDataTemplateCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportDataTemplateCommand, self).__init__(*args, **kwargs)

    def run(self, vertical=True):
        self.vertical = vertical
        self.sobject_recordtypes_attr = processor.populate_sobject_recordtypes()
        if not self.sobject_recordtypes_attr: return # Network Issue Cause
        self.sobject_recordtypes = sorted(list(self.sobject_recordtypes_attr.keys()))
        self.window.show_quick_panel(self.sobject_recordtypes, self.on_choose_recordtype)

    def on_choose_recordtype(self, index):
        if index == -1: return

        # Get chosen item, sobject name and recordtype id
        sobject_recordtype = self.sobject_recordtypes[index]
        sobject = sobject_recordtype.split(",")[0].strip()
        recordtype_name = sobject_recordtype.split(",")[1].strip()
        recordtype_id = self.sobject_recordtypes_attr[sobject_recordtype]

        # handle this describe request
        processor.handle_export_data_template_thread(sobject, 
            recordtype_name, recordtype_id, self.vertical)

    def is_enabled(self):
        return util.check_action_enabled()

class ExecuteRestTest(sublime_plugin.TextCommand):
    def run(self, edit):
        self.items = ["Get", "Post", "Put", "Patch", "Delete", "Tooling Query",
                      "Query", "Query All", "Search", "Quick Search", 
                      "Head", "Retrieve Body"]
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

    def run(self, edit, is_background=False, allowed_folders=None):
        sel = self.view.sel()[0]
        sel_text = self.view.substr(self.view.word(sel.begin()))
        settings = context.get_settings()
        for ct in settings["subscribed_metadata_objects"]:
            if "suffix" not in settings[ct]: 
                continue
            suffix = settings[ct]["suffix"]
            folder = settings[ct]["directoryName"]
            target_file = os.path.join(settings["workspace"] + \
                "/src/%s/%s.%s" % (folder, sel_text, suffix)
            )
            if os.path.isfile(target_file):
                if allowed_folders:
                    if folder in allowed_folders:
                        self.view.window().open_file(target_file)
                else:
                    self.view.window().open_file(target_file)
            else:
                sublime.status_message("You may forget to download the code")

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
        util.view_coverage(self.attributes["name"], self.file_name, self.body)

    def is_enabled(self):
        # Must Be File
        if not self.view.file_name(): 
            return False
        self.file_name = self.view.file_name()

        # Must be valid component
        if not util.check_enabled(self.file_name):
            return False

        # Must be class or trigger
        self.attributes = util.get_file_attributes(self.file_name)
        if not self.attributes["extension"]: 
            return False
        if self.attributes["metadata_folder"] not in ["classes", "triggers"]: 
            return False


        # Can't be Test Class
        with open(self.file_name, encoding="utf-8") as fp:
            self.body = fp.read()

        if "@istest" in self.body.lower(): 
            return False

        return True

    def is_visible(self):
        return self.is_enabled()

class ViewSelectedCodeCoverageCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Keep all open views
        openViewIds = [v.id() for v in sublime.active_window().views()]

        # Open the related code file
        self.view.run_command("goto_component", {
            "is_background": False,
            "allowed_folders": ["classes", "triggers"]
        })

        # 1. Open the view of related code file
        # 2. Run command `view_code_coverage` to open coverage view
        # 3. Close the view of related code file
        # 4. Focus on the coverage view
        view = sublime.active_window().active_view()
        view.run_command("view_code_coverage")
        coverage_view = sublime.active_window().active_view()

        # If there is no available code file
        if coverage_view.id() == view.id():
            return

        if view.id() not in openViewIds:
            sublime.active_window().focus_view(view)
            sublime.active_window().run_command("close")

        # Move focus to the coverage view
        sublime.active_window().focus_view(coverage_view)

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

class RefreshFolder(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RefreshFolder, self).__init__(*args, **kwargs)

    def run(self, dirs):
        message = "Are you sure you really want to refresh these folders"
        if sublime.ok_cancel_dialog(message, "Refresh Folders"):
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
        types = {}
        if not retrieve_all:
            types = {
                "CustomObject": ["*"],
                "Workflow": ["*"]
            }
        else:
            for m in settings["all_metadata_objects"]:
                types[m] = ["*"]

        processor.handle_refresh_folder(types, not retrieve_all)

class RenameMetadata(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.window().show_input_panel("Input New Name", 
            self.filename, self.on_input, None, None)

    def on_input(self, new_name):
        if not new_name or not re.match("\w+[a-zA-Z0-9]+", new_name):
            Printer.get('error').write("Input name is not valid")
            return

        processor.handle_rename_metadata(self.file_name, self.xml_name, self.filename, new_name)

    def is_enabled(self):
        if not self.view or not self.view.file_name(): return False
        self.settings = context.get_settings()
        self.file_name = self.view.file_name()
        base, filename = os.path.split(self.file_name)
        base, folder = os.path.split(base)
        if folder not in self.settings["all_metadata_folders"]:return False
        if not util.check_enabled(self.view.file_name(), check_cache=False): 
            return False

        self.filename = filename.split(".")[0]
        self.xml_name = self.settings[folder]["xmlName"]

        return True

class RetrieveFileFromServer(sublime_plugin.TextCommand):
    def run(self, edit, switch=True):
        files = [self.view.file_name()]
        sublime.active_window().run_command("retrieve_files_from_server", {
            "files": files, 
            "switch": switch
        })

    def is_enabled(self):
        if not self.view or not self.view.file_name(): return False
        self.settings = context.get_settings()
        attributes = util.get_file_attributes(self.view.file_name())
        metadata_folder = attributes["metadata_folder"]
        if metadata_folder not in self.settings["all_metadata_folders"]: return False
        if not util.check_enabled(self.view.file_name(), check_cache=False): 
            return False

        return True

    def is_visible(self):
        return self.is_enabled()

class RetrieveFilesFromServer(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RetrieveFilesFromServer, self).__init__(*args, **kwargs)

    def run(self, files, switch=True, source_org=None, confirmed=False, extract_to=None):
        # Prevent duplicate confirmation
        if not confirmed:
            message = "Confirm retrieving %s from server?" % (
                "these files" if len(files) > 1 else "this file"
            )
            if not sublime.ok_cancel_dialog(message, "Confirm?"): 
                return

        settings = context.get_settings()
        if not extract_to:
            extract_to = settings["workspace"]

        if switch:
            return self.window.run_command("switch_project", {
                "callback_options": {
                    "callback_command": "retrieve_files_from_server", 
                    "args": {
                        "files": files,
                        "switch": False,
                        "source_org": settings["default_project_name"],
                        "confirmed": True,
                        "extract_to": extract_to
                    }
                }
            })

        types = {}
        for _file in files:
            attributes = util.get_file_attributes(_file)
            name = attributes["name"]
            metadata_folder = attributes["metadata_folder"]

            metadata_object_attr = settings[metadata_folder]
            metadata_object = metadata_object_attr["xmlName"]

            # If file is in folder, we need to add folder/
            if metadata_object_attr["inFolder"] == "true":
                name = "%s/%s" % (attributes["folder"], attributes["name"])

            # If file is AuraDefinitionBundle, we need to add folder
            if metadata_folder == "aura":
                name = "%s" % attributes["folder"]

            if metadata_object in types:
                types[metadata_object].append(name)
            else:
                types[metadata_object] = [name]

        processor.handle_retrieve_package(types, extract_to, 
            source_org=source_org, ignore_package_xml=True)

    def is_visible(self, files):
        if not files: return False
        settings = context.get_settings()
        for _file in files:
            if not os.path.isfile(_file): continue # Ignore folder
            metadata_folder = util.get_metadata_folder(_file)
            if metadata_folder not in settings["all_metadata_folders"]: return False
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
        sublime.active_window().run_command("destruct_files_from_server", {
            "files": files
        })

    def is_enabled(self):
        if not self.view or not self.view.file_name(): return False
        self.settings = context.get_settings()
        metadata_folder = util.get_metadata_folder(self.view.file_name())
        if metadata_folder not in self.settings["all_metadata_folders"]:return False
        if not util.check_enabled(self.view.file_name(), check_cache=False): 
            return False

        return True

    def is_visible(self):
        return self.is_enabled()

class DestructFilesFromServer(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DestructFilesFromServer, self).__init__(*args, **kwargs)

    def run(self, files):
        message = "Confirm destructing %s from server?" % (
            "these files" if len(files) > 1 else "this file"
        )
        if sublime.ok_cancel_dialog(message, "Confirm"):
            processor.handle_destructive_files(files)

    def is_visible(self, files):
        if len(files) == 0: return False
        self.settings = context.get_settings()
        for _file in files:
            if not os.path.isfile(_file): continue # Ignore folder
            _folder = util.get_metadata_folder(_file)
            if _folder not in self.settings["all_metadata_folders"]: return False
            if not util.check_enabled(_file, check_cache=False): 
                return False

        return True

class DeployZip(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DeployZip, self).__init__(*args, **kwargs)

    def run(self, zipfile_path=None, chosen_classes=[]):
        self.zipfile_path = zipfile_path
        self.chosen_classes = chosen_classes

        if self.zipfile_path:
            return self.execute_deploy()

        path = sublime.get_clipboard()
        if not path or not os.path.isfile(path): path = ""
        if not path.endswith("zip"): path = ""
        self.window.show_input_panel("Input Zip File Path:", 
            path, self.on_input, None, None)

    def on_input(self, zipfile_path):
        if not zipfile_path.endswith('.zip'):
            return Printer.get("error").write("Invalid Zip File")
        self.zipfile_path = zipfile_path

        # Start deployment
        self.execute_deploy()

    def execute_deploy(self):
        settings = context.get_settings()
        deploy_options = settings["deploy_options"]
        testLevel = deploy_options.get("testLevel", "NoTestRun") 
        if testLevel == "RunSpecifiedTests" and not self.chosen_classes:
            return self.window.run_command("choose_test_classes", {
                "callback_options": {
                    "callback_command": "deploy_zip", 
                    "args": {
                        "zipfile_path": self.zipfile_path,
                        "chosen_classes": self.chosen_classes
                    }
                }
            })


        processor.handle_deploy_thread(util.base64_encode(self.zipfile_path), 
            chosen_classes=self.chosen_classes)

class DeployOpenFilesToServer(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DeployOpenFilesToServer, self).__init__(*args, **kwargs)

    def run(self, select_all=True):
        # If deploy all open files
        if select_all:
            return sublime.active_window().run_command("deploy_files_to_server", 
                {"files": list(self.file_attributes.values())})
        
        # If just deploy some files
        if not hasattr(self, "chosen_files"):
            self.chosen_files = []

        self.populate_items()
        self.window.show_quick_panel(self.items, self.on_choose)

    def populate_items(self):
        self.items = []
        for fileName in list(self.file_attributes.keys()):
            if fileName in self.chosen_files:
                self.items.append("[√] %s" % fileName)
            else:
                self.items.append("[x] %s" % fileName)

    def on_choose(self, index):
        if index == -1:
            chosen_files = []
            for item in self.items:
                if item.startswith("[√] "):
                    chosen_files.append(self.file_attributes[item[4:]])

            if chosen_files:
                sublime.active_window().run_command("deploy_files_to_server", 
                    {"files": chosen_files}
                )
            return

        # Get chosen file name
        chosen_item = self.items[index]
        chosen_file_name = chosen_item[4:]

        # Add or remove chosen file from list
        if chosen_file_name in self.chosen_files:
            self.chosen_files.remove(chosen_file_name)
        else:
            self.chosen_files.append(chosen_file_name)

        # Start next round
        self.populate_items()
        sublime.set_timeout(lambda:self.window.show_quick_panel(self.items, 
            self.on_choose, sublime.MONOSPACE_FONT), 10)

    def is_enabled(self):
        """
        1. You must have selected one file or more
        2. All selected file should be in predefined meta folders
        """

        # If no views, just disable this command
        views = sublime.active_window().views();
        if not views or len(views) == 0: return False

        self.settings = context.get_settings()
        self.file_attributes = {};
        for _view in views:
            _file = _view.file_name()
            # Ignore folder
            if not _file or not os.path.isfile(_file): 
                continue
            attributes = util.get_file_attributes(_file)
            # Ignore non-sfdc files
            if attributes["metadata_folder"] not in self.settings["all_metadata_folders"]:
                continue

            self.file_attributes[attributes["fullName"]] = _file

        # If there is no sfdc code file, just disable this command
        if not self.file_attributes: 
            return False

        return True

class DeployFileToServer(sublime_plugin.TextCommand):
    def run(self, edit, switch=True):
        files = [self.view.file_name()]
        sublime.active_window().run_command("deploy_files_to_server", {
            "files": files, "switch": switch
        })

    def is_enabled(self):
        if not self.view or not self.view.file_name(): return False
        self.settings = context.get_settings()
        attributes = util.get_file_attributes(self.view.file_name())
        if attributes["metadata_folder"] not in self.settings["all_metadata_folders"]:
            return False

        return True

    def is_visible(self):
        return self.is_enabled()

class DeployFileToThisServer(sublime_plugin.TextCommand):
    def run(self, edit):
        files = [self.view.file_name()]
        sublime.active_window().run_command("deploy_files_to_server", {
            "files": files, "switch": False
        })

    def is_enabled(self):
        return util.check_enabled(self.view.file_name(), check_cache=False)

    def is_visible(self):
        return self.is_enabled()

class DeployFilesToServer(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DeployFilesToServer, self).__init__(*args, **kwargs)

    def run(self, files, switch=True, source_org=None, chosen_classes=[]):
        settings = context.get_settings()
        if not source_org:
            source_org = settings["default_project_name"]

        if switch:
            return self.window.run_command("switch_project", {
                "callback_options": {
                    "callback_command": "deploy_files_to_server", 
                    "args": {
                        "files": files,
                        "switch": False,
                        "source_org": source_org
                    }
                }
            })

        deploy_options = settings["deploy_options"]
        testLevel = deploy_options.get("testLevel", "NoTestRun") 
        if testLevel == "RunSpecifiedTests" and not chosen_classes:
            return self.window.run_command("choose_test_classes", {
                "callback_options": {
                    "callback_command": "deploy_files_to_server", 
                    "args": {
                        "files": files,
                        "switch": False,
                        "source_org": source_org
                    }
                }
            })

        # Before deploy, save files to local
        # Enhancement for issue SublimeApex#67
        for _file in files:
            view = util.get_view_by_file_name(_file)
            if not view: continue
            view.run_command("save")

        # Keep the files to deploy
        base64_encoded_zip = util.build_deploy_package(files)
        processor.handle_deploy_thread(
            base64_encoded_zip, 
            source_org=source_org,
            chosen_classes=chosen_classes
        )

    def is_visible(self, files):
        """
        1. You must have selected one file or more
        2. All selected file should be in predefined meta folders
        """

        if not files: return False
        self.settings = context.get_settings()
        for _file in files:
            if not os.path.isfile(_file): continue # Ignore folder
            attributes = util.get_file_attributes(_file)
            if attributes["metadata_folder"] not in self.settings["all_metadata_folders"]:
                return False

        return True

class CopyFileToProject(sublime_plugin.TextCommand):
    def run(self, edit, switch=True, source_org=None):
        sublime.active_window().run_command("copy_files_to_project", {
            "files": [self.view.file_name()]
        })

    def is_enabled(self):
        return self.view.file_name() is not None

class CopyFilesToProject(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CopyFilesToProject, self).__init__(*args, **kwargs)

    def run(self, files, switch=True, source_org=None):
        settings = context.get_settings()
        if not source_org:
            source_org = settings["default_project_name"]

        if switch:
            return self.window.run_command("switch_project", {
                "callback_options": {
                    "callback_command": "copy_files_to_project", 
                    "args": {
                        "files": files,
                        "switch": False,
                        "source_org": source_org
                    }
                }
            })

        target_dir = settings["workspace"]
        util.copy_files(self.attributes, target_dir)

        # If succeed, just show the succeed message
        Printer.get("log").write("Files are copied to " + source_org)

        # we need to switch project back to original
        if settings["switch_back_after_migration"]:
            util.switch_project(source_org)

    def is_enabled(self, files, **kwargs):
        if not files: return False
        self.settings = context.get_settings()
        self.attributes = []
        for _file in files:
            if not os.path.isfile(_file): continue # Ignore folder
            if _file.endswith("-meta.xml"): continue # Ignore meta file 
            attribute = util.get_file_attributes(_file)
            if attribute["metadata_folder"] not in self.settings["all_metadata_folders"]:
                continue

            attribute["fileDir"] = _file
            self.attributes.append(attribute)

        if not self.attributes:
            return False

        return True

    def is_visible(self, files, **kwargs):
        return self.is_enabled(files)

class ExportProfile(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportProfile, self).__init__(*args, **kwargs)

    def run(self):
        import threading
        thread = threading.Thread(target=util.export_profile_settings)
        thread.start()

    def is_enabled(self):
        return util.check_action_enabled()

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
        return util.check_action_enabled()

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
        return util.check_action_enabled()

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
        return util.check_action_enabled()

class ExportCustomFieldCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportCustomFieldCommand, self).__init__(*args, **kwargs)

    def run(self):
        processor.handle_export_customfield()
        
    def is_enabled(self):
        return util.check_action_enabled()

class ExportRoleHierarchyCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExportRoleHierarchyCommand, self).__init__(*args, **kwargs)

    def run(self):
        processor.handle_export_role_hierarchy()
        
    def is_enabled(self):
        return util.check_action_enabled()

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
        return util.check_action_enabled()

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
        startURL = "/apex/" + self.attributes["name"]
        self.view.window().run_command("login_to_sfdc", {"startURL": startURL})

    def is_visible(self):
        if not self.view.file_name(): return False
        self.attributes = util.get_file_attributes(self.view.file_name())
        if not self.attributes["extension"]: return False
        if self.attributes["extension"] != "page": return False

        return util.check_enabled(self.view.file_name())

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

class ChooseTestClasses(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ChooseTestClasses, self).__init__(*args, **kwargs)

    def run(self, callback_options={}):
        self.callback_options = callback_options

        if not hasattr(self, "chosen_classes"):
            self.chosen_classes = []

        # Get all classes
        self.classes_attr = util.populate_components("ApexClass")

        self.classmap = {}
        selected_items = []; unselected_items = []
        for key, item in self.classes_attr.items():
            if not item["is_test"]:
                continue
            if "namespacePrefix" in item and item["namespacePrefix"]:
                cname = "%s.%s" % (
                    item["namespacePrefix"], item["name"]
                )
            else:
                cname = item["name"]

            classItem = "%s[%s] %s" % (
                " " * 4, 
                "√" if cname in self.chosen_classes else "x", 
                cname
            )
            if cname in self.chosen_classes:
                selected_items.append(classItem)
            else:
                unselected_items.append(classItem)
            self.classmap[classItem] = cname

        if not self.classmap:
            settings = context.get_settings()
            return Printer.get('error').write(
                "No available test class in {org_name} org".format(
                    org_name=settings["default_project_name"]
                )
            );
        
        # Add `All` Item
        allItem = "[%s] All" % (
            "√" if self.chosen_classes else "x"
        )
        self.items = [allItem]

        # Add class items
        selected_items = sorted(selected_items)
        unselected_items = sorted(unselected_items)
        self.items.extend(selected_items)
        self.items.extend(unselected_items)

        selected_index = 0
        if hasattr(self, "index"):
            selected_index = self.index

        self.window.show_quick_panel(self.items, self.on_done, 
            sublime.MONOSPACE_FONT, selected_index)

    def on_done(self, index):
        if index == -1:
            callback_command = self.callback_options["callback_command"]
            if self.chosen_classes:
                args = self.callback_options.get("args", {})
                args["chosen_classes"] = self.chosen_classes
                return sublime.active_window().run_command(
                    callback_command, args
                )
            if callback_command == "deploy_package":
                Printer.get("error").write(
                    "You should choose at least one test class"
                )
            return

        self.index = index
        chosen_item = self.items[index]

        if chosen_item.endswith(" All"):
            if len(self.chosen_classes) == len(self.items) - 1:
                self.chosen_classes = []
            else:
                self.chosen_classes = []
                for k, v in self.classmap.items():
                    if v == "*": continue
                    self.chosen_classes.append(v)
        else:
            class_attr = self.classmap[chosen_item]
            class_name = class_attr
            if class_name in self.chosen_classes:
                self.chosen_classes.remove(class_name)
            else:
                self.chosen_classes.append(class_name)

        sublime.set_timeout_async(self.run(
            callback_options=self.callback_options
        ), 10)

class RunSyncTests(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RunSyncTests, self).__init__(*args, **kwargs)

    def run(self, chosen_classes=[]):
        if not chosen_classes:
            return self.window.run_command('choose_test_classes', {
                "callback_options": {
                    "callback_command": "run_sync_tests"
                }
            })
        processor.handle_run_sync_test(chosen_classes)

class RunSyncTest(sublime_plugin.TextCommand):
    def run(self, edit):
        processor.handle_run_sync_test([self.cname])

    def is_enabled(self):
        # Get current file name and Read file content
        file_name = self.view.file_name()
        if not file_name or not file_name.endswith(".cls"): 
            return False
        if not util.check_enabled(file_name): 
            return False

        # Test class must be class firstly
        body = open(file_name, "rb").read()

        # Test class must contains "testMethod" or @isTest notation
        lower_body = body.lower()
        if b"testmethod" not in lower_body and b"@istest" not in lower_body:
            return False

        component_attribute, self.cname = util.get_component_attribute(file_name)
        if "namespacePrefix" in component_attribute and \
                component_attribute["namespacePrefix"]:
            self.cname = "%s.%s" % (
                component_attribute["namespacePrefix"],
                self.cname
            )
            
        return True

    def is_visible(self):
        return self.is_enabled()

class RunAsyncTest(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RunAsyncTest, self).__init__(*args, **kwargs)

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

    def is_visible(self):
        return self.is_enabled()

class RunTestCommand(sublime_plugin.TextCommand):
    def run(self, view):
        # Get component_attribute by file_name
        attributes = util.get_file_attributes(self.view.file_name())
        component_attribute = util.get_component_attribute(self.view.file_name())[0]

        # Process run test
        processor.handle_run_test(attributes["name"], component_attribute["id"])

    def is_enabled(self):
        # Get current file name and Read file content
        file_name = self.view.file_name()
        if not file_name or not file_name.endswith(".cls"): 
            return False
        if not util.check_enabled(file_name): 
            return False

        # Test class must be class firstly
        body = open(file_name, "rb").read()

        # Test class must contains "testMethod" or @isTest notation
        lower_body = body.lower()
        if b"testmethod" not in lower_body and b"@istest" not in lower_body:
            return False

        return True

    def is_visible(self):
        return self.is_enabled()

class TrackAllDebugLogs(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(TrackAllDebugLogs, self).__init__(*args, **kwargs)

    def run(self):
        users = processor.handle_populate_users("track_all_debug_logs")
        if not users: return
        if sublime.ok_cancel_dialog("Confirm to track logs for all users?", "Continue"):
            processor.handle_track_all_debug_logs_thread(users)

class TrackDebugLog(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(TrackDebugLog, self).__init__(*args, **kwargs)

    def run(self, track_self=False):
        if track_self:
            processor.handle_create_debug_log('Me', None)
            return
            
        self.users = processor.handle_populate_users("track_debug_log")
        if not self.users: return
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

        self.users = processor.handle_populate_users("fetch_debug_log")
        if not self.users: return # Network Issue Cause
        self.users_name = sorted(self.users.keys(), reverse=False)
        self.window.show_quick_panel(self.users_name, self.on_done)

    def on_done(self, index):
        if index == -1: return

        user_name = self.users_name[index]
        user_id = self.users[user_name]
        processor.handle_fetch_debug_logs(user_name, user_id)

class ViewDebugLogDetail(sublime_plugin.TextCommand):
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

class ViewDebugOnly(sublime_plugin.TextCommand):
    def run(self, view):
        whole_region = sublime.Region(0, self.view.size())
        debug_content = []
        for line in self.view.lines(whole_region):
            line_content = self.view.substr(line)
            if "|USER_DEBUG|" in line_content:
                debug_content.append(line_content)

        self.view.window().run_command("new_dynamic_view", {
            "view_id": self.view.id(),
            "view_name": self.view.name(),
            "point": 0,
            "erase_all": True,
            "input": "\n".join(debug_content)
        })

    def is_enabled(self):
        return self.view.settings().get("is_debug_log") is True

class ExecuteQuery(sublime_plugin.TextCommand):
    def run(self, view):
        sublime.active_window().run_command("haoku", {
            "router": "query?param=" + self.selection
        })

    def is_enabled(self):
        # Selection must start SELECT, 
        # otherwise you can't see this command
        self.selection = self.view.substr(self.view.sel()[0])
        if not self.selection or not self.selection.upper().startswith("SELECT"):
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

    def run(self, startURL="", copy_url=False):
        # Get toolingapi settings
        settings = context.get_settings()
        session = util.get_session_info(settings)

        # If .config/session.json is not exist, login firstly
        if not session: 
            return self.window.run_command('login', 
                {
                    "callback_options": {
                        "callback_command": "login_to_sfdc",
                        "args": {
                            "startURL": startURL
                        }
                    }
                }
            )

        # If .config/session.json is exist, use frontdoor method
        show_url = "%s/secur/frontdoor.jsp?sid=%s&retURL=%s" % (
            session["instance_url"], session["session_id"], startURL
        )

        if not copy_url:
            return util.open_with_browser(show_url)

        sublime.set_clipboard(show_url)

class AboutCommand(sublime_plugin.ApplicationCommand):
    def run(command):
        package_info = sublime.load_settings("package.sublime-settings")

        version_info = "\n%s\n\n%s\n\nCopyright © 2013-2016 By %s\n\tDev Channel, Build v%s" % (
            package_info.get("description"),
            package_info.get("homepage"),
            package_info.get("author"),
            package_info.get("version")
        )
        sublime.message_dialog(version_info)

class ReportIssueCommand(sublime_plugin.ApplicationCommand):
    def run(command):
        package_info = sublime.load_settings("package.sublime-settings")
        util.open_with_browser(package_info.get("issue_url"))

class HaoideHelp(sublime_plugin.ApplicationCommand):
    def run(command, url=""):
        package_info = sublime.load_settings("package.sublime-settings")
        util.open_with_browser(package_info.get("homepage") + url)

class ReleaseNotesCommand(sublime_plugin.ApplicationCommand):
    def run(command):
        package_info = sublime.load_settings("package.sublime-settings")
        util.open_with_browser(package_info.get("history_url"))

class DeleteFilesFromServer(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DeleteFilesFromServer, self).__init__(*args, **kwargs)

    def run(self, files):
        # Confirm Delete Action
        if sublime.ok_cancel_dialog("Confirm to delete?"):
            for f in files:
                component_attribute = util.get_component_attribute(f)[0]
                processor.handle_delete_component(component_attribute["url"], f)

    def is_visible(self, files):
        """
        1. You must have selected one file or more
        2. All selected file should be visible
        """

        if len(files) == 0: return False
        self._files = [f for f in files if not f.endswith("-meta.xml")]
        if len(self._files) == 0: return False
        for _file in self._files:
            attr = util.get_component_attribute(_file)[0]
            if not attr or "url" not in attr:
                return False

        return True

class DeleteFileFromServer(sublime_plugin.TextCommand):
    def run(self, view):
        files = [self.view.file_name()]
        self.view.window().run_command("delete_files_from_server", {
            "files" : [self.view.file_name()]
        })

    def is_enabled(self):
        self.file_name = self.view.file_name()
        if not self.file_name: return False
        if self.file_name.endswith("-meta.xml"): return False

        attr = util.get_component_attribute(self.file_name)[0]
        if not attr or "url" not in attr:
            return False
        
        return True

    def is_visible(self):
        return self.is_enabled()

class CreateApexTriggerCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateApexTriggerCommand, self).__init__(*args, **kwargs)

    def run(self):
        sobjects_describe = util.populate_sobjects_describe()
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
        return util.check_action_enabled()

class CreateApexPageCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateApexPageCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.window.run_command("create_component", {
            "component_type": "ApexPage",
            "markup_or_body": "Markup"
        })

    def is_enabled(self):
        return util.check_action_enabled()

class CreateApexComponentCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateApexComponentCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.window.run_command("create_component", {
            "component_type": "ApexComponent",
            "markup_or_body": "Markup"
        })

    def is_enabled(self):
        return util.check_action_enabled()

class CreateApexClassCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateApexClassCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.window.run_command("create_component", {
            "component_type": "ApexClass",
            "markup_or_body": "Body"
        })

    def is_enabled(self):
        return util.check_action_enabled()

class CreateStaticResource(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateStaticResource, self).__init__(*args, **kwargs)

    def run(self):
        settings = context.get_settings()
        self.content_types = settings["content_types"]
        self.window.show_quick_panel(self.content_types, self.on_choose)

    def on_choose(self, index):
        if index == -1: return

        self.content_type = self.content_types[index]
        
        self.input_name_message = "Please Input StaticResource Name: "
        self.window.show_input_panel(self.input_name_message, 
            "", self.on_input_name, None, None)

    def on_input_name(self, input):
        # Create component to local according to user input
        if not re.match('^[a-zA-Z]+\\w+$', input):
            message = 'Invalid name, do you want to try again?'
            if not sublime.ok_cancel_dialog(message, "Try Again?"): return
            self.window.show_input_panel(self.input_name_message, 
                "", self.on_input_name, None, None)
            return
        
        self.resource_name = input

        # Input file location
        self.input_location_message = "Please Input File or Path for StaticResource: "
        self.window.show_input_panel(self.input_location_message, 
            "", self.on_input_location, None, None)

    def on_input_location(self, location):
        # Get file or path from user input, allow trying agin
        if not os.path.exists(location) and not os.path.isfile(location):
            if not sublime.ok_cancel_dialog("Invalid file or path", "Try Again?"):
                return
            self.window.show_input_panel(self.input_location_message, 
                "", self.on_input_location, None, None)
            return
        
        if os.path.isfile(location):
            body = open(location, "r").read()

        data = {
            "Name": self.resource_name,
            "ContentType": self.content_type,
            "CacheControl": "Private",
            "Body": body
        }

        processor.handle_create_static_resource(data)

    def is_enabled(self):
        return util.check_action_enabled()

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

        self.templates = util.load_templates()
        templates = self.templates[self.component_type]
        self.template_names = [[n, templates[n]["description"]] for n in templates]
        self.template_names = sorted(self.template_names)

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
            message = "Please Input %s Name %s: " % (
                self.component_type,
                "for %s" % self.sobject_name if self.component_type == "ApexTrigger" else ""
            )
            self.window.show_input_panel(message, "", self.on_input, None, None)

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
        self.settings = context.get_settings()
        workspace = self.settings["workspace"]

        extension = self.template_attr["extension"]
        directory = self.template_attr["directory"]
        with open(os.path.join(workspace, ".templates", directory)) as fp:
            body = fp.read()
        if extension == ".trigger":
            body = body.replace("Trigger_Name__c", self.component_name).replace("Sobject_Name__c", self.sobject_name)
        elif extension == ".cls":
            body = body.replace("Class_Name__c", self.component_name)

        component_outputdir = os.path.join(workspace, "src", self.settings[self.component_type]["directoryName"])
        if not os.path.exists(component_outputdir):
            os.makedirs(component_outputdir)
            self.settings = context.get_settings()
            util.add_project_to_workspace(self.settings)

        file_name = "%s/%s" % (component_outputdir, self.component_name + extension)
        if os.path.isfile(file_name):
            message = '"%s" is already exist, do you want to try again?' % self.component_name
            if not sublime.ok_cancel_dialog(message, "Continue?"):
                self.window.open_file(file_name)
                return
            self.window.show_input_panel("Please Input Name: ", "", self.on_input, None, None)
            return

        with open(file_name, "w") as fp:
            fp.write(body)

        # In windows, new file is not shown in the sidebar, 
        # we need to refresh the sublime workspace to show it
        sublime.active_window().run_command("refresh_folder_list")

        # Build Post body
        data = {
            "name": self.component_name, 
            self.markup_or_body: body
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

class SaveToServer(sublime_plugin.TextCommand):
    def run(self, edit, is_check_only=False):
        # Check whether need confirm
        settings = context.get_settings()
        if settings["confirm_on_save"]:
            message = "Confirm to continue save operation?"
            if not sublime.ok_cancel_dialog(message, "Save to Server?"): 
                return

        # Automatically save current file if dirty
        if self.view.is_dirty():
            self.view.run_command("save")

        # Handle Save Current Component
        processor.handle_save_to_server(self.view.file_name(), is_check_only)

    def is_enabled(self):
        if not self.view or not self.view.file_name(): return False
        attributes = util.get_file_attributes(self.view.file_name())
        if attributes["metadata_folder"] not in ["classes", "components", "pages", "triggers"]:
            return False
            
        return util.check_enabled(self.view.file_name())

    def is_visible(self):
        return self.is_enabled()

class ViewFileAttributes(sublime_plugin.TextCommand):
    def run(self, edit):
        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": self.cname + " Attributes",
            "input": json.dumps(self.component_attribute, indent=4)
        })

    def is_enabled(self):
        if not self.view or not self.view.file_name(): return False
        self.file_name = self.view.file_name()
        self.settings = context.get_settings()
        self.component_attribute, self.cname = util.get_component_attribute(self.file_name)
        if not self.component_attribute:
            return False
            
        return True

class SwitchProjectCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(SwitchProjectCommand, self).__init__(*args, **kwargs)

    def run(self, callback_options={}):
        self.callback_options = callback_options
        settings = context.get_settings()
        projects = settings["projects"]
        self.projects = ["(" + ('Active' if projects[p]["default"] else 
            'Inactive') + ") " + p for p in projects]
        self.projects = sorted(self.projects, reverse=False)
        self.window.show_quick_panel(self.projects, self.on_done)

    def on_done(self, index):
        if index == -1: return

        # Switch to chosen project
        default_project = self.projects[index].split(") ")[1]
        util.switch_project(default_project)

        settings = context.get_settings()
        described_metadata = util.get_described_metadata(settings)
        if not described_metadata:
            return self.window.run_command("describe_metadata", {
                "callback_options": self.callback_options
            })

        # Execute callback command
        if "callback_command" in self.callback_options:
            callback_command = self.callback_options["callback_command"]
            args = self.callback_options["args"] if "args" in self.callback_options else {}
            self.window.run_command(callback_command, args)

class Login(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(Login, self).__init__(*args, **kwargs)

    def run(self, callback_options={}, force=False):
        processor.handle_login_thread(callback_options, force=force)

class UpdateUserLanguage(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(UpdateUserLanguage, self).__init__(*args, **kwargs)

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
        return util.check_action_enabled()

class EnableDevelopmentMode(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(EnableDevelopmentMode, self).__init__(*args, **kwargs)

    def run(self):
        self.users = processor.handle_populate_users("enable_development_mode")
        if not self.users: return # Network Issue Cause
        self.users_name = sorted(self.users.keys(), reverse=False)
        self.window.show_quick_panel(self.users_name, self.on_done)

    def on_done(self, index):
        if index == -1: return

        user_name = self.users_name[index]
        user_id = self.users[user_name]
        processor.handle_enable_development_mode(user_id)

    def is_enabled(self):
        return util.check_action_enabled()

class UpdateUserPassword(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(UpdateUserPassword, self).__init__(*args, **kwargs)

    def run(self):
        self.users = processor.handle_populate_users("update_user_password")
        if not self.users: return # Network Issue Cause
        self.users_name = sorted(self.users.keys(), reverse=False)
        self.window.show_quick_panel(self.users_name, self.on_done)

    def on_done(self, index):
        if index == -1: return

        user_name = self.users_name[index]
        self.user_id = self.users[user_name]

        sublime.active_window().show_input_panel("Input New Password: ", 
            "", self.on_input, None, None)

    def on_input(self, password):
        if not re.match('[\s\S]{5,22}', password):
            message = 'Invalid password, do you want to try again?'
            if not sublime.ok_cancel_dialog(message, "Try Again?"): return
            return sublime.active_window().show_input_panel("Input New Password: ", 
                "", self.on_input, None, None)

        processor.handle_update_user_password(self.user_id, password)

    def is_enabled(self):
        return util.check_action_enabled()

class UpdateProjectPatternsCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(UpdateProjectPatternsCommand, self).__init__(*args, **kwargs)

    def run(self):
        settings = context.get_settings()
        util.add_project_to_workspace(settings)

    def is_enabled(self):
        return util.check_action_enabled()

class UpdateProjectCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(UpdateProjectCommand, self).__init__(*args, **kwargs)

    def run(self):
        message = "Are you sure you really want to update this project?"
        if not sublime.ok_cancel_dialog(message, "Update Project?"): return
        processor.handle_new_project(is_update=True)

    def is_enabled(self):
        return util.check_action_enabled()

class CreateNewProject(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateNewProject, self).__init__(*args, **kwargs)

    def run(self):
        settings = context.get_settings()
        described_metadata = util.get_described_metadata(settings)
        if not described_metadata:
            return self.window.run_command("describe_metadata", {
                "callback_options": {
                    "callback_command": "create_new_project"
                }
            })

        # Check whether default project has subscribed_metadata_objects attribute
        # Check whether default project has one subscribed_metadata_objects at least
        if "subscribed_metadata_objects" not in settings["default_project"] or \
                not settings["default_project"]["subscribed_metadata_objects"]:
            return self.window.run_command("toggle_metadata_objects", {
                "callback_options": {
                    "callback_command": "create_new_project"
                }
            })
        
        dpn = settings["default_project"]["project_name"]
        message = "Are you sure you really want to create new project for %s?" % dpn
        if not sublime.ok_cancel_dialog(message, "Create New Project?"): return
        
        util.add_project_to_workspace(settings)
        processor.handle_new_project()

class DescribeMetadata(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DescribeMetadata, self).__init__(*args, **kwargs)

    def run(self, callback_options={}):
        processor.handle_describe_metadata(callback_options)

class ExtractToHere(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ExtractToHere, self).__init__(*args, **kwargs)

    def run(self, files):
        extract_to, name = os.path.split(self._file)
        name, extension = name.split(".")

        extract_to = os.path.join(extract_to, name)
        try:
            util.extract_zipfile(self._file, extract_to)
        except BaseException as ex:
            return Printer.get("error").write(ex)

        Printer.get("log").write_start().write("Extracted to " + extract_to)

    def is_visible(self, files):
        if not files or len(files) > 1: 
            return False

        self._file = files[0]
        return zipfile.is_zipfile(self._file)

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

class RefreshFileFromServer(sublime_plugin.TextCommand):
    def run(self, view):
        self.view.window().run_command("refresh_files_from_server", {
            "files": [self.view.file_name()]
        })

    def is_enabled(self):
        file_name = self.view.file_name()
        if not file_name: return False
        attr = util.get_component_attribute(file_name)[0]
        if not attr or "url" not in attr: 
            return False

        return True

    def is_visible(self):
        return self.is_enabled()

class RefreshFilesFromServer(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RefreshFilesFromServer, self).__init__(*args, **kwargs)

    def run(self, files):
        message = "Are you sure you really want to continue?"
        if not sublime.ok_cancel_dialog(message, "Refresh Files?"): return

        for file_name in files:
            if file_name.endswith("-meta.xml"): continue # Ignore -meta.xml file
            attr = util.get_component_attribute(file_name)[0]

            # Handle Refresh Current Component
            if attr["type"] == "StaticResource":
                processor.handle_refresh_static_resource(attr, file_name)
            else:
                processor.handle_refresh_file_from_server(attr, file_name)

    def is_visible(self, files):
        if len(files) == 0: return False
        self._files = [f for f in files if not f.endswith("-meta.xml")]
        if len(self._files) == 0: return False
        for _file in self._files:
            attr = util.get_component_attribute(_file)[0]
            if not attr or "url" not in attr:
                return False

        return True