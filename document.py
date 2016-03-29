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
        if not sublime.ok_cancel_dialog(message, "Continue Reloading?"): 
            return

        settings = context.get_settings()
        self.rd = ReloadDocument(settings["docs"])
        thread = threading.Thread(target=self.rd.reload_document)
        thread.start()
        message = "Reloading SFDC Document Reference"
        ThreadProgress(self.rd, thread, message, message + " Succeed")
        self.handle_thread(thread)

    def handle_thread(self, thread, timeout=120):
        if thread.is_alive():
            sublime.set_timeout(lambda:self.handle_thread(thread), timeout)
            return

        # Exception Process
        if not self.rd.result: return

        result = self.rd.result
        references = sublime.load_settings("references.sublime-settings")
        references.set("references", result)
        sublime.save_settings("references.sublime-settings")

class ReloadDocument():
    def __init__(self, docs, **kwargs):
        self.docs = docs
        self.url = "https://developer.salesforce.com/docs"
        self.toc_url = "%s/get_document/atlas.en-us.{toc_type}.meta" % self.url
        self.base_url = "%s/atlas.en-us.{toc_type}.meta/{toc_type}/" % self.url
        self.result = None

    def reload_document(self):
        # Log the StartTime
        start_time = datetime.datetime.now()

        references = {}
        for toc_label, toc_type in self.docs.items():
            Printer.get("log").write("Reloading %s" % toc_label)
            toc_url = self.toc_url.format(toc_type=toc_type)
            try: 
                res = requests.get(toc_url, verify=False)
                result = res.json()
            except Exception as e: 
                Printer.get("log").write("----->Failed to reload %s, reason: %s" % (
                    toc_label, str(e)
                ))
                continue

            doc_references = [] # Define list for this toc

            # Add home page
            base_url = self.base_url.format(toc_type=toc_type)
            doc_references.append({
                "title": result["doc_title"],
                "href": base_url
            })

            # Add PDF page
            doc_references.append({
                "title": "PDF Url",
                "href": result["pdf_url"]
            })

            # Add children
            for toc in result["toc"]:
                # Add root path
                href = ""
                if "a_attr" in toc:
                    href = base_url + toc["a_attr"]["href"]
                doc_references.append({
                    "title": toc["text"],
                    "href": href
                })

                # Add children
                if "children" in toc:
                    self.add_children(doc_references, toc["children"], base_url)

            references[toc_label] = doc_references
    
        # Build Successful
        Printer.get("log").write("RELOADING FINISHED")
        
        # Total time
        total_seconds = (datetime.datetime.now() - start_time).seconds
        Printer.get("log").write("Total time: %s seconds" % total_seconds)

        # Hide panel
        sublime.set_timeout_async(Printer.get("log").hide_panel, 500)

        self.result = references

    def add_children(self, doc_references, children, base_url, level=1, prefix=""):
        for child in children:
            href = ""
            if "a_attr" in child:
                href = base_url + child["a_attr"]["href"]
            title = child["text"]
            doc_references.append({
                "title": "%s%s%s" % (level * "   ", prefix, title),
                "href": href
            })

            # Prefix is used for class methods
            if title.endswith(" Methods"):
                prefix = title.replace(" Methods", ".")

            if "children" in child:
                self.add_children(doc_references, child["children"], 
                    base_url, level + 1, prefix)

class OpenDocumentation(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(OpenDocumentation, self).__init__(*args, **kwargs)

    def run(self, show_all=True):
        self.show_all = show_all
        self.references = self.reference_settings.get("references")
        self.titles = []; self.title_link = {}

        if not show_all:
            # Open document reference of chosen toc type
            self.toc_lables = sorted(list(self.references.keys()))
            self.window.show_quick_panel(self.toc_lables, 
                self.on_choose_toc_type, sublime.MONOSPACE_FONT)
        else:
            # Open all document reference
            for toc_label, values in self.references.items():
                for v in values:
                    self.titles.append(v["title"])
                    self.title_link[v["title"]] = v["href"]
            self.window.show_quick_panel(self.titles, 
                self.on_open_document, sublime.MONOSPACE_FONT)

    def on_choose_toc_type(self, index):
        if index == -1:
            return

         # Get chosen document type
        self.toc_label = self.toc_lables[index]

        self.titles.append("Return to First Step")
        for v in self.references.get(self.toc_label, []):
            self.titles.append(v["title"])
            self.title_link[v["title"]] = v["href"]

        sublime.set_timeout(lambda:self.window.show_quick_panel(self.titles, 
            self.on_open_document, sublime.MONOSPACE_FONT), 10)

    def on_open_document(self, index):
        if index == -1:
            return

        if self.titles[index] == "Return to First Step":
            return sublime.active_window().run_command(
                "open_documentation", {
                    "show_all": False
                }
            )

        href = self.title_link[self.titles[index]]
        if not href:
            sublime.set_timeout(lambda:self.window.show_quick_panel(self.titles, 
                self.on_open_document, sublime.MONOSPACE_FONT, index), 10)
            return
        util.open_with_browser(href)

    def is_enabled(self):
        self.reference_settings = sublime.load_settings("references.sublime-settings")
        return self.reference_settings.has("references")