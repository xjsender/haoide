import sublime, sublime_plugin
import os
import re

from . import context
from . import util
from . import processor
from .salesforce.lib.panel import Printer


class CreateLightningWebComponent(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateLightningWebComponent, self).__init__(*args, **kwargs)

    def run(self):
        self.window.show_input_panel("Please Input Your Component Name: ", 
            "", self.on_input, None, None)

    def on_input(self, lwc_name):
        # Create component to local according to user input
        if not re.match('^[a-zA-Z]+\\w+$', lwc_name):
            message = 'Invalid format, do you want to try again?'
            if not sublime.ok_cancel_dialog(message): 
                return
            return self.window.show_input_panel(
                "Please Input Your Component Name: ", 
                "", self.on_input, None, None
            )

        # Update first letter to lower case
        lwc_name = lwc_name[0].lower() + lwc_name[1:]

        # Get settings
        settings = context.get_settings()
        workspace = settings["workspace"]

        # Get template attribute
        templates = util.load_templates()
        template = templates.get("lwc")

        # Build dir for new LWC
        component_dir = os.path.join(workspace, "src", "lwc", lwc_name)
        if not os.path.exists(component_dir):
            os.makedirs(component_dir)
        else:
            message = "%s is already exist, do you want to try again?" % lwc_name
            if not sublime.ok_cancel_dialog(message, "Try Again?"): return
            self.window.show_input_panel("Please Input Lighting Name: ", 
                "", self.on_input, None, None)
            return

        # Create lwc init files
        for k, v in template.items():
            with open(os.path.join(workspace, ".templates", v["directory"])) as fp:
                body = fp.read()

                # Update dynamic parameters in the template
                body = body.replace("{class_name__c}", lwc_name[:1].upper() + lwc_name[1:])
                body = body.replace("{api_version}", str(settings["api_version"]))
            
            lwc_file = os.path.join(component_dir, lwc_name + v["extension"])

            # Create Aura lightning file
            with open(lwc_file, "w") as fp:
                fp.write(body)

            # If created succeed, open lwc html
            if v["extension"] == ".html":
                window = sublime.active_window()
                window.open_file(lwc_file)

        # Refresh sidebar folder list
        window.run_command("refresh_folder_list")

        # Deploy Aura to server
        self.window.run_command("deploy_lighting_to_server", {
            "dirs": [component_dir],
            "switch_project": False,
            "element": "LightningComponentBundle",
            "update_meta": True
        })

    def is_enabled(self):
        return util.check_action_enabled()
