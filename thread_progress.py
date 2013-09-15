import sublime
from .salesforce import message
from .salesforce import util

class ThreadProgress():
    """
    Stolen from Package Control Source Code, ni dong de
    
    Animates an indicator, [=   ], in the status area while a thread runs

    :param thread:
        The thread to track for activity

    :param message:
        The message to display next to the activity indicator

    :param success_message:
        The message to display once the thread is complete
    """

    def __init__(self, api, thread, message, success_message):
        self.api = api
        self.thread = thread
        self.message = message
        self.success_message = success_message
        self.addend = 1
        self.size = 15
        sublime.set_timeout(lambda: self.run(0), 100)

    def run(self, i):
        if not self.thread.is_alive():
            if hasattr(self.thread, 'result') and not self.thread.result:
                sublime.status_message('')
                return

            # After thread is end, display feedback to end user
            # according to response
            result = self.api.result
            if self.api != None and isinstance(result, dict) and result["status_code"] > 399:
                sublime.active_window().run_command("show_panel", 
                    {"panel": "console", "toggle": False})
                print (message.SEPRATE.format(util.format_error_message(result)))
            else:
                sublime.status_message(self.success_message)
            return

        before = i % self.size
        after = (self.size - 1) - before

        sublime.status_message('%s [%s=%s]' % \
            (self.message, ' ' * before, ' ' * after))

        if not after:
            self.addend = -1
        if not before:
            self.addend = 1
        i += self.addend

        sublime.set_timeout(lambda: self.run(i), 100)
