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
        util.display_active_project(view)

    def on_load_async(self, view):
        """
        1. Set Status with current default project
        """

        util.display_active_project(view)

    def on_activated(self, view):
        """
        Set Status with current default project
        """

        util.display_active_project(view)
