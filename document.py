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
import urllib
from . import requests, context
from .progress import ThreadProgress

class ReloadSalesforceDocumentCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ReloadSalesforceDocumentCommand, self).__init__(*args, **kwargs)

    def run(self):
        message = "Generally, you should reload it every salesforce release, " +\
                  "do you really want to continue?"
        confirm = sublime.ok_cancel_dialog(message)
        if not confirm: return

        settings = context.get_toolingapi_settings()
        self.rd = ReloadDocument(settings["docs"])
        thread = threading.Thread(target=self.rd.reload_document)
        thread.start()
        message = "Reloading Salesforce Document Reference"
        ThreadProgress(self.rd, thread, message, message + " Succeed")
        self.handle_thread(thread)

    def handle_thread(self, thread, timeout=120):
        if thread.is_alive():
            sublime.set_timeout(lambda:self.handle_thread(thread), timeout)
            return

        result = self.rd.result
        salesforce_reference = sublime.load_settings("salesforce_reference.sublime-settings")
        salesforce_reference.set("salesforce_reference", result)
        sublime.save_settings("salesforce_reference.sublime-settings")

class ReloadDocument():
    def __init__(self, docs, **kwargs):
        self.docs = docs
        self.result = None

    def reload_document(self):
        title_link = {}
        for prefix in self.docs:
            doc_attr = self.docs[prefix]
            sublime.status_message("Processing %s..." % prefix)
            print ("Processing %s" % prefix)
            xml_url = 'http://www.salesforce.com/us/developer/docs/%s/Data/Toc.xml' % doc_attr["keyword"]
            try: 
                res = requests.get(xml_url, headers={"Accept": "application/xml"})
            except: 
                continue
            tree = ElementTree.fromstring(res.content)
            leaf_parents = tree.findall(doc_attr["pattern"])
            for parent in leaf_parents:
                parent_title = parent.attrib["Title"]
                title_link[prefix + "=>" + parent_title] = {
                    "url": parent.attrib["Link"],
                    "attr": doc_attr["keyword"]
                }
                
                if " Methods" in parent_title:
                    parent_title = parent_title.replace(" Methods", ".")
                else:
                    parent_title = parent_title + " "
                    
                for child in parent.getchildren():
                    title_link[prefix + "=>" + parent_title + child.attrib["Title"]] = {
                        "url": child.attrib["Link"],
                        "attr": doc_attr["keyword"]
                    }

        self.result = title_link

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

        link = self.title_link[self.titles[index]]
        show_url= 'http://www.salesforce.com/us/developer/docs/%s%s' % (link["attr"], link["url"])
        settings = context.get_toolingapi_settings()
        browser_path = settings["default_chrome_path"]
        if os.path.exists(browser_path):
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser_path))
            webbrowser.get('chrome').open_new_tab(show_url)
        else:
            webbrowser.open_new_tab(show_url)

    def is_enabled(self):
        reference_settings = sublime.load_settings("salesforce_reference.sublime-settings")
        return reference_settings.has("salesforce_reference")