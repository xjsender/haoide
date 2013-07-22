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

class switchprojectCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(switchprojectCommand, self).__init__(*args, **kwargs)

    def run(self):
        global projects
        toolingapi_settings = context.get_toolingapi_settings()
        projects = toolingapi_settings["projects"]
        projects = ["(" + str(projects[p]["default"]) + ") " + p for p in projects]
        projects = sorted(projects, reverse=True)
        self.window.show_quick_panel(projects, self.on_done)

    def on_done(self, index):
        if index == -1: return

        # Change the chosen project as default
        # Split with ") " and get the second project name
        default_project = projects[index].split(") ")[1]
        context.switch_project(default_project)

class newviewCommand(sublime_plugin.TextCommand):
    """
    Create a new view with specified input

    @input: user specified input

    Usage: 
        sublime.active_window().run_command("newview", {
            "input": "Example"
        })
    """

    def run(self, edit, name="", input=""):
        print ("Open new file...")
        n = sublime.active_window().new_file()
        n.set_name(name)
        n.set_scratch(True)
        n.insert(edit, 0, input)

class refreshfolderCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(refreshfolderCommand, self).__init__(*args, **kwargs)

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

class retrieveallCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(retrieveallCommand, self).__init__(*args, **kwargs)

    def run(self):
        # Open Console
        self.window.run_command("show_panel", 
            {"panel": "console", "toggle": False})

        processor.handle_retrieve_all_thread()
        
class exportvalidationrulesCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(exportvalidationrulesCommand, self).__init__(*args, **kwargs)

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

class exportworkflowCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(exportworkflowCommand, self).__init__(*args, **kwargs)

    def run(self):
        toolingapi_settings = context.get_toolingapi_settings()
        workflow_path = toolingapi_settings["workspace"] + "/metadata/unpackaged/workflows"
        if not os.path.exists(workflow_path):
            sublime.error_message(message.WORKFLOW_PATH_CHECK)
            return

        self.window.run_command("show_panel", 
            {"panel": "console", "toggle": False})

        processor.handle_parse_workflow()

class describecustomfieldCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(describecustomfieldCommand, self).__init__(*args, **kwargs)

    def run(self):
        global sobjects
        sobjects = processor.populate_sobjects()
        sobjects = sorted(sobjects)
        self.window.show_quick_panel(sobjects, self.on_done)

    def on_done(self, index):
        if index == -1: return

        # Open Console
        self.window.run_command("show_panel", 
            {"panel": "console", "toggle": False})

        processor.handle_describe_customfield(sobjects[index])
        
class describeglobalCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(describeglobalCommand, self).__init__(*args, **kwargs)

    def run(self):
        # Open Console
        self.window.run_command("show_panel", 
            {"panel": "console", "toggle": False})

        processor.handle_describe_global()

class describelayoutCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(describelayoutCommand, self).__init__(*args, **kwargs)

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

class backupsobjectsCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(backupsobjectsCommand, self).__init__(*args, **kwargs)

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

class describesobjectCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(describesobjectCommand, self).__init__(*args, **kwargs)

    def run(self):
        global sobjects
        sobjects = processor.populate_sobjects()
        sobjects = sorted(sobjects)
        self.window.show_quick_panel(sobjects, self.on_done)

    def on_done(self, index):
        if index == -1: return

        # Open Console
        self.window.run_command("show_panel", 
            {"panel": "console", "toggle": False})

        processor.handle_retrieve_fields(sobjects[index])

class exportworkbookCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(exportworkbookCommand, self).__init__(*args, **kwargs)

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

class runonetestCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(runonetestCommand, self).__init__(*args, **kwargs)

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

class runtestCommand(sublime_plugin.TextCommand):
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
        try:
            # Python 3.x
            body = open(file_name, encoding="utf-8").read()
        except:
            # Python 2.x
            body = open(file_name).read().encode()

        if ".cls" not in file_name or "@isTest" not in body:
            return False

        return True

class executesoqlCommand(sublime_plugin.TextCommand):
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

class executeanonymousCommand(sublime_plugin.TextCommand):
    def run(self, view):
        # Open Console
        self.view.window().run_command("show_panel", 
            {"panel": "console", "toggle": False})

        # Handle
        processor.handle_execute_anonymous(selection)

    def is_enabled(self):
        # You must select some snippets, otherwise
        # you can't see this command
        self.selection = self.view.substr(self.view.sel()[0]).encode('utf-8')
        if not self.selection:
            return False

        return True

class viewidinsfdcwebCommand(sublime_plugin.TextCommand):
    def run(self, view):
        startURL = "/" + self.record_id
        if self.record_id.startswith("012"):
            startURL = "/setup/ui/recordtypefields.jsp?id=" + self.record_id
        
        self.view.window().run_command("loginintosfdc", {"startURL": startURL})

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

class showinsfdcwebCommand(sublime_plugin.TextCommand):
    def run(self, view):
        # Get file_name and component_attribute
        component_attribute = get_component_attribute(self.view.file_name())[0]

        # Open this component in salesforce web
        startURL = "/" + component_attribute["id"]
        self.view.window().run_command("loginintosfdc", {"startURL": startURL})

    def is_enabled(self):
        return check_visible(self.view.file_name())

class loginintosfdcCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(loginintosfdcCommand, self).__init__(*args, **kwargs)

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

class aboutCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(aboutCommand, self).__init__(*args, **kwargs)

    def run(self): 
        webbrowser.open_new_tab("https://github.com/xjsender/SublimeApex")

class deleteCommand(sublime_plugin.TextCommand):
    def run(self, view):
        # Get file_name and component_attribute
        file_name = self.view.file_name()
        component_attribute = get_component_attribute(file_name)[0]

        # Confirm Delete Action
        confirm = sublime.ok_cancel_dialog(message.DELETE_CONFIRM_MESSAGE)
        if confirm == False:
            return

        # Open Console
        self.view.window().run_command("show_panel", 
            {"panel": "console", "toggle": False})
        
        # Handle Delete
        processor.handle_delete_component(component_attribute["url"], file_name)

    def is_enabled(self):
        return check_visible(self.view.file_name())

class createCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(createCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.window.show_input_panel("component_name.extension, Sobject_Name:", 
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
            data["MasterLabel"] = component_name,

        processor.handle_create_component(data, component_name, component_type)

class deployCommand(sublime_plugin.TextCommand):
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
        return check_visible(self.view.file_name())

class refreshallCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(refreshallCommand, self).__init__(*args, **kwargs)

    def run(self): 
        # Create Project Directory
        context.make_dir()

        # Open Console
        self.window.run_command("show_panel", 
            {"panel": "console", "toggle": False})

        # Handle Refresh All
        processor.handle_refresh_components(context.get_toolingapi_settings())

class refreshcurrentCommand(sublime_plugin.TextCommand):
    def run(self, view): 
        # Get file_name and component_attribute
        file_name = self.view.file_name()
        component_attribute = get_component_attribute(file_name)[0]

        # Open Console
        self.view.run_command("show_panel", 
            {"panel": "console", "toggle": False})

        # Handle Refresh Current Component
        processor.handle_refresh_component(component_attribute, file_name)

    def is_enabled(self):
        return check_visible(self.view.file_name())

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

def check_visible(file_name):
    """
    Check whether file is ApexTrigger, ApexComponent, ApexPage or ApexClass

    Parameters:
        file_name: current file name

    Return: 
        Bool
    """

    # Get toolingapi settings
    toolingapi_settings = context.get_toolingapi_settings()

    # Get component_type
    component_type = util.get_component_type(file_name)

    # If component type is not in range, just show error message
    if component_type not in toolingapi_settings["component_types"]:
        return False

    # Get component_url and component_id
    username = toolingapi_settings["username"]
    component_attribute = util.get_component_attribute(username, file_name)
    if component_attribute == None: 
        return False

    return True