import sublime
import sublime_plugin
import os
import time

from . import context
from . import util

class SFDCEventListener(sublime_plugin.EventListener):
    def on_new(self, view):
        """
        1. Eveytime when you open a new view, default syntax is Apex
        2. Set Status with current default project
        """
        view.set_syntax_file("Packages/Java/Java.tmLanguage")
        context.display_active_project(view)

    def on_load_async(self, view):
        """
        1. Set Status with current default project
        """

        context.display_active_project(view)

    def on_modified_async(self, view):
        """
        Every time when you modified the context, just hide the console, 
        you can close it in sublime settings
        """
        toolingapi_settings = context.get_toolingapi_settings() 

        # If it is not SFDC Component, just return
        if view.file_name() == None: return
        name, extension = util.get_file_attr(view.file_name())
        if extension not in toolingapi_settings["component_extensions"]: return

        # If functionality is close, just return
        if not toolingapi_settings["hidden_console_on_modify"]: return

        # Hidden Console
        sublime.active_window().run_command("hide_panel", 
            {"panel": "console", "toggle": False})

    def on_pre_save_async(self, view):
        """
        Every time when you save your ApexPage, ApexTrigger, ApexClass, ApexComponent, 
        this class will make a copy with the time_stamp in the history path of current project
        """
        toolingapi_settings = context.get_toolingapi_settings()

        # Check whether need to keep history
        if not toolingapi_settings["keep_local_change_history"]: return

        # Get current file name and Read file content
        file_name = view.file_name()
        if not os.path.isfile(file_name): return
        body = open(file_name, "rb").read()

        # Get component_name amd component_type
        name, extension = util.get_file_attr(file_name)

        # If this file is not ApexTrigger, ApexComponent, 
        # ApexPage or ApexClass, just return
        if extension not in toolingapi_settings["component_extensions"]: return

        # Get Workspace, if not exist, make it
        folder = toolingapi_settings[toolingapi_settings[extension]]["folder"]
        workspace = toolingapi_settings["workspace"] + "/history/" + folder
        if not os.path.exists(workspace):
            os.makedirs(workspace)

        # Backup current file
        time_stamp = time.strftime("%Y-%m-%d-%H-%M", time.localtime())
        fp = open(workspace + "/" + name + "-" + time_stamp + extension, "wb")

        fp.write(body)
        fp.close()
