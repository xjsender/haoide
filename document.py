"""SublimeSalesforceReference: Quick access to Salesforce Documentation from Sublime Text"""
__version__ = "1.0.0"
__author__ = "James Hill (oblongmana@gmail.com)"
__copyright__ = "SublimeSalesforceReference: (C) 2014 James Hill. GNU GPL 3."
__credits__ = ["All Salesforce Documentation is © Copyright 2000–2014 salesforce.com, inc."]

import sublime, sublime_plugin
import xml.etree.ElementTree as ElementTree
import webbrowser
import os
import threading
from . import requests, context

class ReloadSalesforceReferenceCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ReloadSalesforceReferenceCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.retrieve_index_async()
        
    def retrieve_index_async(self):
        sublime.status_message('Retrieving Salesforce Reference Index...')
        sublime.set_timeout_async(self.retrieve_index, 200)
    
    def retrieve_index(self):
        sf_xml_url = 'http://www.salesforce.com/us/developer/docs/apexcode/Data/Toc.xml'
        res = requests.get(sf_xml_url, headers={"Accept": "application/xml"})

        sf_tree = ElementTree.fromstring(res.content)
        leaf_parents = sf_tree.findall("*[@Title='Reference'].//TocEntry[@DescendantCount='0']..")

        self.title_link = {}
        for parent in leaf_parents:
            self.title_link[parent.attrib["Title"]] = parent.attrib["Link"]

        salesforce_reference = sublime.load_settings("salesforce_reference.sublime-settings")
        salesforce_reference.set("salesforce_reference", self.title_link)
        sublime.save_settings("salesforce_reference.sublime-settings")

class OpenDocumentationCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(OpenDocumentationCommand, self).__init__(*args, **kwargs)

    def run(self):
        reference_settings = sublime.load_settings("salesforce_reference.sublime-settings")
        self.title_link = reference_settings.get("salesforce_reference")
        self.titles = sorted(self.title_link.keys())
        self.window.show_quick_panel(self.titles, self.open_documentation)

    def open_documentation(self, index):
        if index == -1: return

        base_url= 'http://www.salesforce.com/us/developer/docs/apexcode'
        show_url = base_url + self.title_link[self.titles[index]]
        settings = context.get_toolingapi_settings()
        browser_path = settings["default_chrome_path"]
        if os.path.exists(browser_path):
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser_path))
            webbrowser.get('chrome').open_new_tab(show_url)
        else:
            webbrowser.open_new_tab(show_url)

    def is_visible(self):
        reference_settings = sublime.load_settings("salesforce_reference.sublime-settings")
        return reference_settings.has("salesforce_reference")



