import sublime
import time
from datetime import date

class Printer(object):
    """ Based on printer of Mavensmate
    """
    printers = {}

    def __init__(self, name):
        self.name = name
        self.visible = False

    @classmethod
    def get(cls, name, window_id=None):
        if not window_id: window_id = sublime.active_window().id()
        printer = cls.printers.get(str(window_id)+name)
        if not printer:
            printer = Printer(name)
            printer.window_id = window_id
            printer.init()
            cls.printers[str(window_id)+name] = printer
            package_info = sublime.load_settings("package.sublime-settings")
            version_info = "Copyright © 2013-%s By %s, Dev Channel, Build v%s\n" % (
                date.today().year,
                package_info.get("author"),
                package_info.get("version")
            )
            printer.write(version_info, False)
        return printer

    def init(self):
        if not hasattr(self, "panel"):
            self.window = sublime.active_window()
            self.panel = self.window.get_output_panel(self.name)
            self.panel.settings().set('syntax', 'Packages/Java/Java.tmLanguage')
            self.panel.settings().set('color_scheme', 'Packages/Color Scheme - Default/Monokai.tmTheme')
            self.panel.settings().set('word_wrap', True)
            self.panel.settings().set('gutter', True)
            self.panel.settings().set('line_numbers', True)

    def hide_panel(self):
        self.visible = False
        self.window.run_command('hide_panel', {
            'panel': 'output.' + self.name
        })

        return self

    def show_panel(self):
        self.visible = True
        self.window.run_command('show_panel', {
            'panel': 'output.' + self.name
        })

        return self

    def scroll_to_bottom(self):
        size = self.panel.size()
        sublime.set_timeout(lambda : self.panel.show(size, True), 2)

    def write_start(self, message="~"*100):
        return self.write(message, False)

    def write(self, message, prefix=True):
        # Show Panel
        self.show_panel()
        
        # Append message to panel
        from ...context import get_default_project_name
        panel_message = message + "\n" if not prefix else "%s: %s: %s\n" % (
            get_default_project_name(),
            time.strftime("%Y.%m.%d %H:%M:%S", time.localtime(time.time())), 
            message
        )

        self.panel.run_command("append", {
            "characters": panel_message
        })

        # Scroll to bottom
        self.scroll_to_bottom()
        
        return self

    def write_end(self, message=None):
        return self.write(message, False)
