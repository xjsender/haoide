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

class ReloadSalesforceDocumentCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ReloadSalesforceDocumentCommand, self).__init__(*args, **kwargs)

    def run(self):
        self.retrieve_index_async()
        
    def retrieve_index_async(self):
        sublime.status_message('Retrieving Salesforce Reference Index...')
        sublime.set_timeout_async(self.retrieve_index, 200)
    
    def retrieve_index(self):
        # Retrieve the apex code tree
        title_link = {}
        docs = {
            "apexcode": {
               "catalog": "Apex",
               "pattern": "*[@Title='Reference'].//TocEntry[@DescendantCount='0'].."
            },
            "pages": {
                "catalog": "Visualforce",
                "pattern": "*[@Title='Standard Component Reference'].//TocEntry[@DescendantCount='0'].."
            },
            "chatterapi": {
               "catalog": "Chatter Api",
               "pattern": ".//TocEntry[@DescendantCount='0']"
            },
            "api_streaming": {
               "catalog": "Streaming Api",
               "pattern": ".//TocEntry[@DescendantCount='0']"
            },
            "api_asynch": {
               "catalog": "Bulk Api",
               "pattern": "*[@Link].//TocEntry[@DescendantCount='0'].."
            },
            "api_rest": {
               "catalog": "Rest Api",
               "pattern": ".//TocEntry[@DescendantCount='0']"
            },
            "api_tooling": {
               "catalog": "Tooling Api",
               "pattern": ".//TocEntry[@DescendantCount='0']"
            },
            "api_console": {
               "catalog": "Console Toolkit",
               "pattern": ".//TocEntry[@DescendantCount='0']"
            },
            "object_reference": {
               "catalog": "Standard Objects",
               "pattern": "*.//TocEntry[@DescendantCount='0'].."
            }
        }

        for doc in docs:
            doc_attr = docs[doc]
            xml_url = 'http://www.salesforce.com/us/developer/docs/%s/Data/Toc.xml' % doc
            res = requests.get(xml_url, headers={"Accept": "application/xml"})
            tree = ElementTree.fromstring(res.content)
            leaf_parents = tree.findall(doc_attr["pattern"])
            for parent in leaf_parents:
                parent_title = parent.attrib["Title"]
                title_link[doc_attr["catalog"] + "=>" + parent_title] = {
                    "url": parent.attrib["Link"],
                    "attr": doc
                }
                
                if " Methods" in parent_title:
                    parent_title = parent_title.replace(" Methods", ".")
                else:
                    parent_title = parent_title + " "
                    
                for child in parent.getchildren():
                    title_link[doc_attr["catalog"] + "=>" + parent_title + child.attrib["Title"]] = {
                        "url": child.attrib["Link"],
                        "attr": doc
                    }

        salesforce_reference = sublime.load_settings("salesforce_reference.sublime-settings")
        salesforce_reference.set("salesforce_reference", title_link)
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



