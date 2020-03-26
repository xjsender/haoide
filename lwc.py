import sublime
import sublime_plugin
import os
import re

from . import context
from . import util
from . import processor
from .salesforce.lib.panel import Printer


class CreateLightningWebComponent(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateLightningWebComponent, self).__init__(*args, **kwargs)
        # Get settings
        self._settings = context.get_settings()
        self._workspace = self._settings["workspace"]

    def run(self, *args):
        if self._settings["api_version"] < 45:
            message = "Lightning Web Component only available for API Version >= 45, current is %s"
            sublime.error_message(message % self._settings["api_version"])
            return
        self.window.show_input_panel("Please Input Lightning Web Component Name: ",
                                     "", self.on_input, None, None)

    def on_input(self, lwc_name):
        # Create component to local according to user input
        if not re.match('^[a-z]+\\w*[A-Za-z0-9]$', lwc_name) or re.match('__+', lwc_name):
            message = 'Invalid format, do you want to try again?'
            if not sublime.ok_cancel_dialog(message):
                return
            self.window.show_input_panel("Please Input Lightning Web Component Name: ",
                                         "", self.on_input, None, None)
            return

        # Build dir for new Lightning web component
        component_dir = os.path.join(self._workspace, "src", "lwc", lwc_name)
        if not os.path.exists(component_dir):
            os.makedirs(component_dir)
        else:
            message = "%s is already exist, do you want to try again?" % lwc_name
            if not sublime.ok_cancel_dialog(message, "Try Again?"):
                return
            self.window.show_input_panel("Input Lightning Web Component Name: ",
                                         "", self.on_input, None, None)
            return

        # Get template attribute
        templates = util.load_templates()
        template_bundle = templates.get("lwc")
        for tpl_name in template_bundle:
            template = template_bundle.get(tpl_name)
            with open(os.path.join(self._workspace, ".templates", template["directory"])) as fp:
                body = fp.read()
                # Insert lwc name and api version into files
                body = body.replace('{class_name__c}', lwc_name)
                body = body.replace('{api_version}', str(self._settings["api_version"]))

            lwc_file = os.path.join(component_dir, lwc_name + template["extension"])

            # Create Aura Lightning file
            with open(lwc_file, "w") as fp:
                fp.write(body)

            # If created succeed, just open it and refresh project
            window = sublime.active_window()
            window.open_file(lwc_file)
            window.run_command("refresh_folder_list")

        # Deploy Lightning Web Component to server
        self.window.run_command("deploy_lwc_to_server", {
            "dirs": [component_dir],
            "switch_project": False,
            "update_meta": True
        })

    def is_enabled(self):
        return util.check_action_enabled()

    def is_visible(self):
        if self._settings["api_version"] < 45:
            return False
        return True


class DeployLwcToServer(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DeployLwcToServer, self).__init__(*args, **kwargs)
        self.settings = context.get_settings()

    def run(self, dirs, switch_project=True, source_org=None, update_meta=False):
        if switch_project:
            return self.window.run_command("switch_project", {
                "callback_options": {
                    "callback_command": "deploy_lwc_to_server",
                    "args": {
                        "switch_project": False,
                        "source_org": self.settings["default_project_name"],
                        "dirs": dirs,
                        "update_meta": update_meta
                    }
                }
            })

        base64_package = util.build_lightning_package(dirs, 'lwc')
        processor.handle_deploy_thread(base64_package, source_org=source_org, update_meta=update_meta)

    def is_visible(self, dirs, switch_project=True):
        visible = True
        if not dirs or len(dirs) == 0:
            visible = False

        for _dir in dirs:
            attributes = util.get_file_attributes(_dir)
            metadata_folder = attributes["metadata_folder"]
            if metadata_folder != "lwc":
                visible = False
            if self.settings["default_project_name"] not in _dir:
                visible = False

        return visible
