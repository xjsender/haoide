import sublime, sublime_plugin
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

class BulkInsertCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(BulkInsertCommand, self).__init__(*args, **kwargs)

    def run(self):
        sobjects_describe = processor.populate_sobjects_describe()
        self.sobjects = sorted(sobjects_describe.keys())
        self.window.show_quick_panel(self.sobjects, self.on_done)

    def on_done(self, index):
        if index == -1: return
        processor.handle_bulk_insert_thread(self.sobjects[index])

class BulkUpdateCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(BulkUpdateCommand, self).__init__(*args, **kwargs)

    def run(self):
        sublime.message_dialog("This command is ongoing")

class BulkUpsertCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(BulkUpsertCommand, self).__init__(*args, **kwargs)

    def run(self):
        sublime.message_dialog("This command is ongoing")

class BulkDeleteCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(BulkDeleteCommand, self).__init__(*args, **kwargs)

    def run(self):
        sublime.message_dialog("This command is ongoing")