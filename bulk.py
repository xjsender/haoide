import sublime
import sublime_plugin
import os
from . import processor

class BulkExportSingleCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(BulkExportSingleCommand, self).__init__(*args, **kwargs)

    def run(self):
        sobjects_describe = processor.populate_sobjects_describe()
        self.sobjects = sorted(sobjects_describe.keys())
        self.window.show_quick_panel(self.sobjects, self.on_done)

    def on_done(self, index):
        if index == -1: return
        processor.handle_backup_sobject_thread(self.sobjects[index])

class BulkExportAllCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(BulkExportAllCommand, self).__init__(*args, **kwargs)

    def run(self):
        processor.handle_backup_all_sobjects_thread()

class BulkOperationCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(BulkOperationCommand, self).__init__(*args, **kwargs)

    def run(self, operation=None):
        self.operation = operation
        sobjects_describe = processor.populate_sobjects_describe()
        self.sobjects = sorted(sobjects_describe.keys())
        self.window.show_quick_panel(self.sobjects, self.on_done)

    def on_done(self, index):
        if index == -1: return
        self.sobject = self.sobjects[index]
        path = sublime.get_clipboard()
        if not os.path.isfile(path): path = ""
        self.window.show_input_panel("Input CSV Path: ", 
            path, self.on_input, None, None)

    def on_input(self, file_path):
        if not file_path.endswith('csv'): 
            sublime.error_message("Input file must be CSV")
            return

        if not os.path.exists(file_path):
            sublime.error_message(file_path + " is not valid file")
            return

        processor.handle_bulk_operation_thread(self.sobject, file_path, self.operation)

class BulkUpsertCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(BulkUpsertCommand, self).__init__(*args, **kwargs)

    def run(self):
        sublime.message_dialog("This command is ongoing")