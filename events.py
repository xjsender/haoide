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

    def on_activated(self, view):
        """
        Set Status with current default project
        """

        context.display_active_project(view)

    def on_modified_async(self, view):
        """
        Every time when you modified the context, just hide the console, 
        you can close it in sublime settings
        """
        settings = context.get_settings() 

        # If it is not SFDC Component, just return
        if not view.file_name(): return
        name, extension = util.get_file_attr(view.file_name())
        if extension not in settings["component_extensions"]: return

        if settings["hidden_console_on_modify"]: util.hide_panel()
