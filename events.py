import sublime
import sublime_plugin
import os
import time

from . import context
from .salesforce import util

class SFDCEventListener(sublime_plugin.EventListener):
    def on_new_async(self, view):
        """
        1. Eveytime when you open a new view, default syntax is Apex
        2. Set Status with current default project
        """
        view.set_syntax_file("Packages/SublimeApex/syntaxes/Apex.tmLanguage")
        self.display_active_project(view)

    def on_load_async(self, view):
        """
        1. Set Status with current default project
        """

        self.display_active_project(view)

    def display_active_project(self, view):
        toolingapi_settings = context.get_toolingapi_settings()
        display_message = "Default Project ▄︻┻═┳一 " + toolingapi_settings["default_project_name"]
        view.set_status('default_project', display_message)

    def on_modified_async(self, view):
        """
        Every time when you modified the context, just hide the console, 
        you can close it in sublime settings
        """
        toolingapi_settings = context.get_toolingapi_settings() 

        # If it is not SFDC Component, just return
        component_type = util.get_component_type(view.file_name())
        if component_type not in toolingapi_settings["component_types"]: return

        # If functionality is close, just return
        if not toolingapi_settings["hidden_console_on_modify"]: return

        # Hidden Console
        sublime.active_window().run_command("hide_panel", 
            {"panel": "console", "toggle": False})

    def on_post_save_async(self, view):
        """
        Every time when you save your ApexPage, ApexTrigger, ApexClass, ApexComponent, 
        this class will make a copy with the time_stamp in the history path of current project
        """
        settings = context.get_toolingapi_settings()

        # Check whether need to keep history
        if not settings["keep_local_change_history"]: return

        # Get current file name and Read file content
        file_name = view.file_name()
        try:
            body = open(file_name, encoding="utf-8").read()
        except:
            body = open(file_name, "rb").read()

        # Get component_name amd component_type
        component_name = util.get_component_name(file_name)
        component_type = util.get_component_type(file_name)

        # If this file is not ApexTrigger, ApexComponent, 
        # ApexPage or ApexClass, just return
        if component_type not in settings["component_types"]:
            return

        # Get toolingapi settings
        toolingapi_settings = context.get_toolingapi_settings()

        # Get component extension
        component_extension = toolingapi_settings[component_type]["extension"]

        # Get Workspace, if not exist, make it
        workspace = toolingapi_settings["workspace"] + "/history/" + component_type
        if not os.path.exists(workspace):
            os.makedirs(workspace)

        # Backup current file
        time_stamp = time.strftime("%Y-%m-%d-%H-%M", time.localtime())
        fp = open(workspace + "/" + component_name + "-" +\
            time_stamp + component_extension, "w")

        fp.write(body)
        fp.close()
