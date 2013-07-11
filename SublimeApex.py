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
        projects = list(projects.keys())
        self.window.show_quick_panel(projects, self.on_done)

    def on_done(self, index):
        if index == -1: return

        # Change the chosen project as default
        default_project = projects[index]
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

        processor.handle_refresh_folder(component_types[index], 120)

class retrieveallCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(retrieveallCommand, self).__init__(*args, **kwargs)

    def run(self):
        # Open Console
        self.window.run_command("show_panel", 
            {"panel": "console", "toggle": False})

        processor.handle_retrieve_all_thread(120)
        
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

        processor.handle_parse_validation_rule(120)

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

        processor.handle_parse_workflow(120)

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

        processor.handle_describe_customfield(sobjects[index], 120)
        
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

        processor.handle_retrieve_fields(sobjects[index], 120)

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
            processor.handle_generate_specified_workbooks(sobjects, 120)

class runonetestCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(runonetestCommand, self).__init__(*args, **kwargs)

    def run(self):
        global classes_attr
        global class_names

        classes_attr = processor.populate_classes()
        classes = classes_attr.keys()
        classes = [c for c in classes if classes_attr[c]["is_test"]]
        class_names = sorted(list(classes))
        self.window.show_quick_panel(class_names, self.on_done)

    def on_done(self, index):
        if index == -1: return

        # Open Console
        self.window.run_command("show_panel", 
            {"panel": "console", "toggle": False})

        class_id = classes_attr[class_names[index]]["component_id"]
        processor.handle_run_test(class_id, 120)

class runtestCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(runtestCommand, self).__init__(*args, **kwargs)

    def run(self): 
        # Get current file name and Read file content
        file_name = self.window.active_view().file_name()
        try:
            # Python 3.x
            body = open(file_name, encoding="utf-8").read()
        except:
            # Python 2.x
            body = open(file_name).read().encode()

        if ".cls" not in file_name or "@isTest" not in body:
            sublime.error_message(message.INVALID_TEST_CLASS)
            return

        # Open Console
        self.window.run_command("show_panel", 
            {"panel": "console", "toggle": False})

        # Get component_url and component_id
        toolingapi_settings = context.get_toolingapi_settings()
        username = toolingapi_settings["username"]
        component_url, class_id = util.get_component_url_and_id(username, file_name)

        processor.handle_run_test(class_id, 120)

class executesoqlCommand(sublime_plugin.TextCommand):
    def run(self, view):
        selection = self.view.substr(self.view.sel()[0]).encode('utf-8')

        if selection == "" or not selection.upper().startswith(b"SELECT"):
            sublime.error_message("Not Valid SOQL.")
            return

        # Open Console
        self.view.window().run_command("show_panel", 
            {"panel": "console", "toggle": False})

        # Handle
        processor.handle_execute_query(selection, 120)

class executeanonymousCommand(sublime_plugin.TextCommand):
    def run(self, view):
        selection = self.view.substr(self.view.sel()[0])

        if selection == "":
            sublime.error_message("Apex Snippet can't be empty.")
            return

        # Open Console
        self.view.window().run_command("show_panel", 
            {"panel": "console", "toggle": False})

        # Handle
        processor.handle_execute_anonymous(selection, 120)

class viewidinsfdcwebCommand(sublime_plugin.TextCommand):
    def run(self, view):
        if util.is_python3x():
            record_id = self.view.substr(self.view.sel()[0])
        else:
            record_id = self.view.substr(self.view.sel()[0]).encode("utf-8")
            
        if len(record_id) != 15 and len(record_id) != 18:
            sublime.error_message("Salesforce Id should be 15d or 18d")
            return

        if not re.compile(r'^[a-zA-Z0-9]*$').match(record_id):
            sublime.error_message("Invalid Salesforce Id")
            return

        startURL = "/" + record_id
        if record_id.startswith("012"):
            startURL = "/setup/ui/recordtypefields.jsp?id=" + record_id
        
        self.view.window().run_command("loginintosfdc", {"startURL": startURL})

class showinsfdcwebCommand(sublime_plugin.TextCommand):
    def run(self, view):
        # Get toolingapi settings
        toolingapi_settings = context.get_toolingapi_settings()

        # Get current file name
        file_name = self.view.file_name()

        print (file_name)

        # Get component type
        component_type = util.get_component_type(file_name)

        # If component type is not in range, just show error message
        if component_type not in toolingapi_settings["component_types"]:
            sublime.error_message(message.INVALID_COMPONENT)
            return

        # Get component_url and component_id
        username = toolingapi_settings["username"]
        component_url, component_id = util.get_component_url_and_id(username, file_name)

        # Open this component in salesforce web
        startURL = "/" + component_id
        self.view.window().run_command("loginintosfdc", {"startURL": startURL})

class loginintosfdcCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(loginintosfdcCommand, self).__init__(*args, **kwargs)

    def run(self, startURL=""):
        # Get toolingapi settings
        toolingapi_settings = context.get_toolingapi_settings()

        # Combine Login URL
        if util.is_python3x():
            # Python 3.x
            show_params = urllib.parse.urlencode({
                "un": toolingapi_settings["username"],
                "pw": toolingapi_settings["password"],
                "startURL": startURL
            })
        else:
            # Python 2.x
            show_params = urllib.urlencode({
                "un": toolingapi_settings["username"],
                "pw": toolingapi_settings["password"],
                "startURL": startURL
            })

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
        # Get toolingapi settings
        toolingapi_settings = context.get_toolingapi_settings()

        # Get current file name
        file_name = self.view.file_name()

        # Get component type
        component_type = util.get_component_type(file_name)

        # If component type is not in range, just show error message
        if component_type not in toolingapi_settings["component_types"]:
            sublime.error_message(message.INVALID_COMPONENT)
            return

        # Confirm Delete Action
        confirm = sublime.ok_cancel_dialog(message.DELETE_CONFIRM_MESSAGE)
        if confirm == False:
            return

        # Open Console
        self.view.window().run_command("show_panel", 
            {"panel": "console", "toggle": False})

        # Get component_url and component_id
        username = toolingapi_settings["username"]
        component_url, component_id = util.get_component_url_and_id(username, file_name)

        if component_id == None: return
        
        # Handle Delete
        processor.handle_delete_component(component_url, file_name, 120)

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
        if component_type == "ApexClass":
            data = {
                "name": component_name,
                component_body: body,
                "IsValid": True
            }
        elif component_type == "ApexTrigger":
            data = {
                "name": component_name,
                "TableEnumOrId": sobject_name,
                component_body: body
            }
        elif component_type in ["ApexPage", "ApexComponent"]:
            data = {
                "name": component_name,
                "MasterLabel": component_name,
                component_body: body
            }

        processor.handle_create_component(data, component_name, 
            component_type, 120)

class deployCommand(sublime_plugin.TextCommand):
    def run(self, view):
        # Automatically save current file if dirty
        if self.view.is_dirty():
            self.view.run_command("save")

        # Get toolingapi settings
        toolingapi_settings = context.get_toolingapi_settings()

        file_name = self.view.file_name()
        print(file_name)

        # Read file content
        try:
            body = open(file_name, encoding="utf-8").read()
        except:
            body = open(file_name).read()
        
        # Get component_name (Class Name, Trigger Name, etc.)
        component_name = util.get_component_name(file_name)

        # Get component type
        component_type = util.get_component_type(file_name)

        # If component type is not in range, just show error message
        if component_type not in toolingapi_settings["component_types"]:
            sublime.error_message(message.INVALID_COMPONENT)
            return

        # Open Console
        self.view.window().run_command("show_panel", 
            {"panel": "console", "toggle": False})

        # Get Component body name in response
        component_body = toolingapi_settings[component_type]["body"]

        # Get component_url and component_id
        username = toolingapi_settings["username"]
        component_url, component_id = util.get_component_url_and_id(username, file_name)

        # "Name", "SaveClass" + id
        # For example {"name": "SaveClass<ClassId>"}
        data = {"name": "Save" + component_type[4 : len(component_type)] + component_id}

        # Handle Save Current Component
        processor.handle_save_component(data, component_type, component_id, body, 120)

class refreshallCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(refreshallCommand, self).__init__(*args, **kwargs)

    def run(self): 
        # Open Project
        self.window.run_command("open_project")

        # Create Project Directory
        context.make_dir()

        # Open Console
        self.window.run_command("show_panel", 
            {"panel": "console", "toggle": False})

        toolingapi_settings = context.get_toolingapi_settings()

        # Handle Refresh All
        print(message.WAIT_FOR_A_MOMENT)
        processor.handle_refresh_components(toolingapi_settings, 120)
        processor.handle_initiate_sobjects_completions(120)

class refreshcurrentCommand(sublime_plugin.TextCommand):
    def run(self, view): 
        # Get toolingapi settings
        toolingapi_settings = context.get_toolingapi_settings()

        # Get file_name
        file_name = self.view.file_name()
        print(file_name)
        
        # Get component_name (Class Name, Trigger Name, etc.)
        component_name = util.get_component_name(file_name)

        # Get component_type
        component_type = util.get_component_type(file_name)

        # If component type is not in range, just show error message
        if component_type not in toolingapi_settings["component_types"]:
            sublime.error_message(message.INVALID_COMPONENT)
            return

        # Open Console
        self.view.window().run_command("show_panel", 
            {"panel": "console", "toggle": False})
        
        # Get Component body name in response
        component_body = toolingapi_settings[component_type]["body"]

        # Get component_url and component_id
        username = toolingapi_settings["username"]
        component_url, component_id = util.get_component_url_and_id(username ,
            file_name)

        # If component_url is None, just alert message
        if component_url == None:
            return

        # Handle Refresh Current Component
        processor.handle_refresh_component(component_url, file_name, 
            component_body, 120)
