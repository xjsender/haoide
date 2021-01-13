import sublime
import sublime_plugin
import os
import re

from . import context
from . import util
from . import processor
from .salesforce.lib.panel import Printer


class OpenLightningDocReferences(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(OpenLightningDocReferences, self).__init__(*args, **kwargs)

    def run(self):
        instance = util.get_instance(self.settings)
        if instance == "emea": instance = "eu0"
        start_url = "https://%s.lightning.force.com/docs/component-library" % instance
        self.window.run_command("login_to_sfdc", {"startURL": start_url})

    def is_enabled(self):
        self.settings = context.get_settings()
        metadata = util.get_described_metadata(self.settings)
        if not metadata:
            return False

        return True


class DeployLightningToServer(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DeployLightningToServer, self).__init__(*args, **kwargs)
        self.meta_type = ''

    def run(self, dirs, switch_project=True, source_org=None, element=None, update_meta=False):
        if switch_project:
            return self.window.run_command("switch_project", {
                "callback_options": {
                    "callback_command": "deploy_lightning_to_server",
                    "args": {
                        "switch_project": False,
                        "source_org": self.settings["default_project_name"],
                        "dirs": dirs,
                        "element": element,
                        "update_meta": update_meta
                    }
                }
            })

        base64_package = util.build_lightning_package(dirs, meta_type=self.meta_type)
        processor.handle_deploy_thread(
            base64_package,
            source_org=source_org,
            element=element,
            update_meta=update_meta
        )

    def is_visible(self, dirs, switch_project=True):
        if not dirs or len(dirs) == 0:
            return False

        self.settings = context.get_settings()
        for _dir in dirs:
            attributes = util.get_file_attributes(_dir)
            meta_folder = attributes["metadata_folder"]
            if meta_folder not in ["aura", "lwc"]:
                return False
            self.meta_type = 'AuraDefinitionBundle' if meta_folder == 'aura' else 'LightningComponentBundle'
            if self.settings["default_project_name"] not in _dir:
                return False

        return True


class PreviewLightningAppInServer(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(PreviewLightningAppInServer, self).__init__(*args, **kwargs)

    def run(self, app_name=None):
        if app_name:
            return self.preview_app(app_name)

        # Get all available apps to preview in the local aura path
        aura_dir = os.path.join(self.settings["workspace"], "src", "aura")
        self.app_names = []
        for dirpath, dirnames, filenames in os.walk(aura_dir):
            for filename in filenames:
                attributes = util.get_file_attributes(filename)
                if attributes["extension"] == "app":
                    self.app_names.append(attributes["name"])
        self.app_names = sorted(self.app_names)

        # Check whether has available app to preview
        if not self.app_names:
            return Printer.get("error").write("No available app to preview")

        self.window.show_quick_panel(self.app_names, self.on_chosen)

    def on_chosen(self, index):
        if index == -1: return
        self.preview_app(self.app_names[index])

    def preview_app(self, app_name):
        instance = util.get_instance(self.settings)
        start_url = "https://%s.lightning.force.com/%s/%s.app" % (
            instance, self.namespace, app_name
        )
        self.window.run_command("login_to_sfdc", {"startURL": start_url})

    def is_enabled(self):
        self.settings = context.get_settings()
        metadata = util.get_described_metadata(self.settings)
        if not metadata:
            return False

        self.namespace = metadata["organizationNamespace"]
        if not self.namespace:
            self.namespace = 'c'

        return True


class PreviewThisAppInServer(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.window().run_command('preview_lightning_app_in_server', {
            "app_name": self.app_name
        })

    def is_enabled(self):
        if not self.view.file_name():
            return False

        attrs = util.get_file_attributes(self.view.file_name())
        if attrs["metadata_folder"] != 'aura' or attrs["extension"] != "app":
            return False
        self.app_name = attrs["name"]

        return True

    def is_visible(self):
        return self.is_enabled()


class RetrieveLightningFromServer(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RetrieveLightningFromServer, self).__init__(*args, **kwargs)

    def run(self, dirs):
        message = "Are you sure you really want to continue refreshing"
        if sublime.ok_cancel_dialog(message, "Confirm?"):
            processor.handle_retrieve_package(
                self.types,
                self.settings["workspace"],
                ignore_package_xml=True
            )

    def is_visible(self, dirs):
        self.settings = context.get_settings()
        self.types = {}
        if len(dirs) == 0:
            return False
        for _dir in dirs:
            if os.path.isfile(_dir):
                continue
            base, _name = os.path.split(_dir)
            base, _folder = os.path.split(base)

            # Check Metadata Type
            if _folder not in ["aura", "lwc"]:
                continue

            # Check Project Name
            pn = self.settings["default_project_name"]
            if pn not in _dir:
                continue

            if "AuraDefinitionBundle" in self.types:
                self.types["AuraDefinitionBundle"].append(_name)
            elif "LightningComponentBundle" in self.types:
                self.types["LightningComponentBundle"].append(_name)
            elif _folder == 'aura':
                self.types["AuraDefinitionBundle"] = [_name]
            elif _folder == 'lwc':
                self.types["LightningComponentBundle"] = [_name]

        # Check whether any aura components are chosen
        if not self.types:
            return False

        return True


class DestructLightningFromServer(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DestructLightningFromServer, self).__init__(*args, **kwargs)

    def run(self, dirs):
        _, bundle_name = os.path.split(dirs[0])
        if sublime.ok_cancel_dialog("This will Delete %s !" % bundle_name + " Confirm to continue?"):
            processor.handle_destructive_files(dirs, ignore_folder=False)

    def is_visible(self, dirs):
        if len(dirs) == 0:
            return False
        self.settings = context.get_settings()
        for _dir in dirs:
            attributes = util.get_file_attributes(_dir)
            if attributes["metadata_folder"] not in ["aura", "lwc"]:
                return False
            if not util.check_enabled(_dir, check_cache=False):
                return False

        return True


class CreateLightningElement(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateLightningElement, self).__init__(*args, **kwargs)

    def run(self, dirs, element=""):
        """ element: Component, Controller, Helper, Style, Documentation, Render
        """

        # Get template attribute
        templates = util.load_templates()
        template = templates.get("AuraElement").get(element)
        settings = context.get_settings()
        templates_path = os.path.join(settings["workspace"],
                                      ".templates", template["directory"])
        with open(templates_path) as fp:
            body = fp.read()

        # JS Component is different with others
        extension = template["extension"]
        element_name = "%s%s%s" % (
            self.aura_name,
            element if extension == ".js" else "",
            extension
        )

        # Combine Aura element component name
        element_file = os.path.join(self._dir, element_name)

        # If element file is already exist, just alert
        if os.path.isfile(element_file):
            return self.window.open_file(element_file)

        # Create Aura Element file
        with open(element_file, "w") as fp:
            fp.write(body)

        # If created succeed, just open it and refresh project
        self.window.open_file(element_file)
        self.window.run_command("refresh_folder_list")

        # Deploy Aura to server
        self.window.run_command("deploy_lightning_to_server", {
            "dirs": [self._dir],
            "switch_project": False,
            "element": element,
            "update_meta": True
        })

    def is_visible(self, dirs, element=""):
        if not dirs or len(dirs) != 1: return False
        self._dir = dirs[0]

        # Check whether project is the active one
        settings = context.get_settings()
        if settings["default_project_name"] not in self._dir:
            return False

        # Check metadata folder
        attributes = util.get_file_attributes(self._dir)
        if attributes["metadata_folder"] != "aura":
            return False
        self.aura_name = attributes["name"]

        # Check lightning type
        lightning_extensions = []
        for dirpath, dirnames, filenames in os.walk(self._dir):
            for filename in filenames:
                extension = filename[filename.find("."):]
                lightning_extensions.append(extension)

        # Just Component and Application can have child elements
        if ".cmp" in lightning_extensions or ".app" in lightning_extensions:
            return True

        return False


class CreateLightningDefinition(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreateLightningDefinition, self).__init__(*args, **kwargs)

    def run(self, _type=""):
        self._type = _type
        self.window.show_input_panel("Please Input %s Name: " % _type,
                                     "", self.on_input, None, None)

    def on_input(self, lightning_name):
        # Create component to local according to user input
        if not re.match('^[a-zA-Z]+\\w+$', lightning_name):
            message = 'Invalid format, do you want to try again?'
            if not sublime.ok_cancel_dialog(message): return
            self.window.show_input_panel("Please Input %s Name: " % self._type,
                                         "", self.on_input, None, None)
            return

        # Get settings
        settings = context.get_settings()
        workspace = settings["workspace"]

        # Get template attribute
        templates = util.load_templates()
        template = templates.get("Aura").get(self._type)
        with open(os.path.join(workspace, ".templates", template["directory"])) as fp:
            body = fp.read()

        # Build dir for new lightning component
        component_dir = os.path.join(workspace, "src", "aura", lightning_name)
        if not os.path.exists(component_dir):
            os.makedirs(component_dir)
        else:
            message = "%s is already exist, do you want to try again?" % lightning_name
            if not sublime.ok_cancel_dialog(message, "Try Again?"): return
            self.window.show_input_panel("Please Input Lightning Name: ",
                                         "", self.on_input, None, None)
            return

        lightning_file = os.path.join(component_dir, lightning_name + template["extension"])

        # Create Aura lightning file
        with open(lightning_file, "w") as fp:
            fp.write(body)

        # If created succeed, just open it and refresh project
        window = sublime.active_window()
        window.open_file(lightning_file)
        window.run_command("refresh_folder_list")

        # Deploy Aura to server
        self.window.run_command("deploy_lightning_to_server", {
            "dirs": [component_dir],
            "switch_project": False,
            "element": self._type,
            "update_meta": True
        })

    def is_enabled(self):
        return util.check_action_enabled()
