import sublime, sublime_plugin
import xml.etree.ElementTree as ElementTree
import os
import datetime
import threading
import urllib
from . import requests, context, util
from .progress import ThreadProgress
from .salesforce.lib.panel import Printer

class ReloadSalesforceDocumentCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ReloadSalesforceDocumentCommand, self).__init__(*args, **kwargs)

    def run(self):
        message = "Generally, you should reload it every salesforce release, " +\
                  "do you really want to continue?"
        if not sublime.ok_cancel_dialog(message, "Continue Reloading?"): return

        settings = context.get_settings()
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

        # Exception Process
        if not self.rd.result: return

        result = self.rd.result
        salesforce_reference = sublime.load_settings("salesforce_reference.sublime-settings")
        salesforce_reference.set("salesforce_reference", result)
        sublime.save_settings("salesforce_reference.sublime-settings")

class ReloadDocument():
    def __init__(self, docs, **kwargs):
        self.docs = docs
        self.result = None

    def reload_document(self):
        # Log the StartTime
        start_time = datetime.datetime.now()

        # Start retriving docs
        Printer.get("log").write_start().write("Start to reload document reference")

        title_link = {}
        for prefix in self.docs:
            doc_attr = self.docs[prefix]
            Printer.get("log").write("Reloading %s" % prefix)
            xml_url = 'http://www.salesforce.com/us/developer/docs/%s/Data/Toc.xml' % doc_attr["keyword"]
            try: 
                res = requests.get(xml_url, headers={"Accept": "application/xml"})
            except Exception as e: 
                Printer.get("log").write("Reloading %s Failed" % prefix)
                continue

            tree = ElementTree.fromstring(res.content)
            leaf_parents = tree.findall(doc_attr["pattern"])
            for parent in leaf_parents:
                parent_title = parent.attrib["Title"]
                if "Link" not in parent.attrib: continue
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

        # Build Successful
        Printer.get("log").write("RELOADING SUCCESSFUL")
        
        # Total time
        total_seconds = (datetime.datetime.now() - start_time).seconds
        Printer.get("log").write("Total time: %s seconds" % total_seconds)

        # Hide panel
        sublime.set_timeout_async(Printer.get("log").hide_panel, 500)

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
        util.open_with_browser(show_url)

    def is_enabled(self):
        reference_settings = sublime.load_settings("salesforce_reference.sublime-settings")
        return reference_settings.has("salesforce_reference")