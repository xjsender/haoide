import sublime, sublime_plugin
import os
import time
import json
import xml

from . import util
from . import context
from . import processor

from .salesforce.lib.panel import Printer


class CombinePackageFiles(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CombinePackageFiles, self).__init__(*args, **kwargs)

    def run(self, files):
        package_xmls = []
        for _file in files:
            if _file.endswith("-meta.xml"):
                continue
            
            if _file.endswith(".xml"):
                package_xmls.append(_file)

        target_dir = os.path.split(files[0])[0]
        self.window.run_command('combine_package_folder', {
            "dirs": [],
            "package_xmls": package_xmls,
            "target_dir": target_dir
        })


    def is_visible(self, files):
        if not files: return False
        return True

class CombinePackageFolder(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CombinePackageFolder, self).__init__(*args, **kwargs)

    def run(self, dirs, package_xmls=None, target_dir=None):
        self.settings = context.get_settings()

        # If combine package by folder
        if not package_xmls:
            package_xmls = []
            for _dir in dirs:
                for dirpath, dirnames, filenames in os.walk(_dir):
                    for filename in filenames:
                        if filename.endswith("-meta.xml"): continue
                        if not filename.endswith(".xml"): continue

                        # Package file name
                        package_xmls.append(os.path.join(dirpath, filename))

        all_types = {}
        for package_xml in package_xmls:
            # Read package.xml content
            with open(package_xml, "rb") as fp:
                content = fp.read()

            """ Combine types sample: [
                {"ApexClass": ["test"]},
                {"ApexTrigger": ["test"]}
            ]
            """
            try:
                _types = util.build_package_types(content)
            except xml.parsers.expat.ExpatError as ee:
                message = "%s parse error: %s" % (package_xml, str(ee))
                Printer.get("error").write(message)
                if not sublime.ok_cancel_dialog(message, "Skip?"): return
                continue
            except KeyError as ex:
                if self.settings["debug_mode"]:
                    print ("%s is not valid package.xml" % package_xml)
                continue

            for _type in _types:
                members = _types[_type]

                if _type in all_types:
                    members.extend(all_types[_type])
                    members = list(set(members))
                
                all_types[_type] = sorted(members)

        if not all_types:
            Printer.get("error").write_start().write("No available package.xml to combine")
            return

        # print (json.dumps(all_types, indent=4))
        metadata_objects = []
        for _type in all_types:
            metadata_objects.append(
                "<types>%s<name>%s</name></types>" % (
                    "".join(["<members>%s</members>" % m for m in all_types[_type]]),
                    _type
                )
            )

        self.package_xml_content = """<?xml version="1.0" encoding="UTF-8"?>
            <Package xmlns="http://soap.sforce.com/2006/04/metadata">
                {metadata_objects}
                <version>{api_version}.0</version>
            </Package>
        """.format(
            metadata_objects="".join(metadata_objects),
            api_version=self.settings["api_version"]
        )

        # Define target dir to contain the combined xml
        if len(dirs) > 0: target_dir = dirs[0]

        package_path = os.path.join(target_dir, "All.xml")
        sublime.active_window().show_input_panel("Input Package.xml Path", 
            package_path, self.on_input_package_path, None, None)

    def on_input_package_path(self, package_path):
        # Check input
        if not package_path:
            message = 'Invalid path, do you want to try again?'
            if not sublime.ok_cancel_dialog(message, "Try Again?"): return
            self.window.show_input_panel("Please Input Name: ", "", 
                self.on_input_extractto, None, None)
            return

        base = os.path.split(package_path)[0]
        if not os.path.exists(base):
            os.makedirs(base)

        with open(package_path, "wb") as fp:
            fp.write(util.format_xml(self.package_xml_content))

        view = sublime.active_window().open_file(package_path)
    
    def is_visible(self, dirs):
        if not dirs: return False
        return True

class ReloadProjectCache(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(ReloadProjectCache, self).__init__(*args, **kwargs)

    def run(self, callback_command=None):
        self.callback_command = callback_command
        self.settings = context.get_settings()
        self.metadata_objects = []
        for m in self.settings["all_metadata_objects"]:
            # Add parent metadata object
            self.metadata_objects.append(m)

            # Add child metadata object
            child_types = util.get_child_types(m)
            self.metadata_objects.extend(child_types)

        self.selected_index = 0
        self.chosen_types = []
        self.build_items();

    def build_items(self):
        self.items = []

        if self.chosen_types:
            self.items.append("[√]All")
        else:
            self.items.append("[x]All")

        for m in sorted(self.settings["all_metadata_objects"]):
            # Add parent to items
            if m in self.chosen_types:
                self.items.append("    [%s]%s" % ("√", m))
            else:
                self.items.append("    [%s]%s" % ("x", m))

            # Add children to items
            child_types = util.get_child_types(m)
            for c in child_types:
                if c in self.chosen_types:
                    self.items.append("        [%s]%s" % ("√", c))
                else:
                    self.items.append("        [%s]%s" % ("x", c))

        sublime.set_timeout(lambda:self.window.show_quick_panel(self.items, 
            self.on_choose, sublime.MONOSPACE_FONT, self.selected_index), 10)

    def on_choose(self, index):
        if index == -1:
            # Just when you select one metadata_object at least,
            # start to reload cache, otherwise, do nothing
            if self.chosen_types:
                chosen_types = {}
                for c in self.chosen_types:
                    chosen_types[c] = ["*"]

                processor.handle_reload_project_cache(chosen_types, 
                    self.callback_command)
            return

        # Store the index and chosen metadata
        self.selected_index = index
        selected_item = self.items[index]
        if selected_item == "[x]All":
            self.chosen_types = self.metadata_objects[:]
        elif selected_item == "[√]All":
            if len(self.chosen_types) == len(self.metadata_objects):
                self.chosen_types = []
            else:
                self.chosen_types = self.metadata_objects[:]
        else:
            chosen_type = selected_item.strip()[3:]

            # Get all children for chosen_type
            # If chosen_type is child, child can't have children
            attr = self.settings[chosen_type]
            parent_type = attr["xmlName"]
            child_types = util.get_child_types(parent_type)

            if "[x]" in selected_item:
                if chosen_type == parent_type:
                    if chosen_type not in self.chosen_types:
                        self.chosen_types.append(chosen_type)
                    for c in child_types:
                        self.chosen_types.append(c)
                else:
                    # Add chosen selected child metadata object
                    if chosen_type not in self.chosen_types:
                        self.chosen_types.append(chosen_type)

                    # Add parent metadata object of selected child
                    if parent_type not in self.chosen_types:
                        self.chosen_types.append(parent_type)
            else:
                # Get all chosen child xml names
                parent_type = parent_type
                child_types = util.get_child_types(parent_type)

                chosen_child_types = []
                for c in child_types:
                    if c in self.chosen_types:
                        chosen_child_types.append(c)

                if parent_type == chosen_type:
                    if len(child_types) == len(chosen_child_types):
                        self.chosen_types.remove(chosen_type)

                        for c in child_types:
                            if c in self.chosen_types:
                                self.chosen_types.remove(c)
                    else:
                        for c in child_types:
                            if c not in self.chosen_types:
                                self.chosen_types.append(c)
                else:
                    # Remove child
                    self.chosen_types.remove(chosen_type)

                    # If all siblings are also not exist in selected list,
                    # parent should also be removed from selected list
                    if len(chosen_child_types) == 1:
                        self.chosen_types.remove(parent_type)

        self.build_items()

    def is_enabled(self):
        self.settings = context.get_settings()
        described_metadata = util.get_described_metadata(self.settings)
        return described_metadata is not None

class BuildPackageXml(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(BuildPackageXml, self).__init__(*args, **kwargs)

    def run(self):
        if not hasattr(self, "filters"):
            sublime.active_window().show_input_panel(
                "Input filters for members separated with comma: ", 
                "", self.on_input_filters, None, None
            )
        else:
            self.on_input_filters(",".join(self.filters))
        
    def on_input_filters(self, filters):
        self.filters = filters.split(",") if filters else []

        package_cache = os.path.join(self.settings["workspace"], ".config", "package.json")
        if not os.path.exists(package_cache):
            return self.window.run_command("reload_project_cache", {
                "callback_command": "build_package_xml"
            })

        self.cache = json.loads(open(package_cache).read())

        # Get types from settings of current view,
        # if current view doesn't have the `types` setting,
        # try to build the types from content of current file
        """ types format: {
                "ApexClass": [
                    "AClass", 
                    "BClass",
                    ...
                ],
                "ApexTrigger": [
                    "ATrigger", 
                    "BTrigger",
                    ...
                ]
            }
        """
        view = self.window.active_view()
        types = view.settings().get("types") if view else {}
        if view and not types:
            try:
                with open(view.file_name(), "rb") as fp:
                    content = fp.read()
                types = util.build_package_types(content)
            except Exception as ex:
                types = {}
        
        self.members = []
        self.matched_package = {}
        for metadata_object in sorted(self.cache.keys()):
            members = self.cache.get(metadata_object)
            if not members: continue
            
            if metadata_object in types:
                display = "[√]" + metadata_object
            else:
                display = "[x]" + metadata_object
            self.members.append(display)

            matched_members = []
            for mem in members:
                if self.filters and not self.is_filter_match(mem):
                    continue
                matched_members.append(mem)

                if mem in types.get(metadata_object, []):
                    mem = "[√]" + metadata_object + " => " + mem
                else:
                    mem = "[x]" + metadata_object + " => " + mem
                self.members.append("    %s" % mem)

             # If no matched member, just skip
            if not matched_members:
                self.members.remove(display)
                continue

            self.matched_package[metadata_object] = matched_members

        if not self.members:
            message = "No matched member found by filters('%s'), do you want to retry" % ",".join(self.filters)
            if sublime.ok_cancel_dialog(message, "Retry"):
                return sublime.active_window().show_input_panel(
                    "Input filters for members separated with comma: ", 
                    "", self.on_input_filters, None, None
                )
            return

        # Get the last subscribe index
        selected_index = view.settings().get("selected_index") if view else 0
        if not selected_index: selected_index = 0

        self.window.show_quick_panel(self.members, self.on_done, 
            sublime.MONOSPACE_FONT, selected_index)

    def is_filter_match(self, member):
        isFilterMatch = False
        for _filter in self.filters:
            _filter = _filter.strip()
            if _filter.lower() in member.lower():
                isFilterMatch = True
                break

        return isFilterMatch

    def on_done(self, index):
        if index == -1:
            del self.filters
            return

        chosen_element = self.members[index]

        if " => " in chosen_element:
            chosen_type, chosen_member = chosen_element.split(" => ")
            is_chosen = "[√]" in chosen_type
            chosen_type = chosen_type[7:]
        else:
            chosen_type, chosen_member = chosen_element, None
            is_chosen = "[√]" in chosen_type
            chosen_type = chosen_type[3:]

        view = self.window.active_view()
        if not view or not view.settings().has("types"): 
            view = self.window.new_file()
            view.set_syntax_file("Packages/XML/XML.sublime-syntax")
            view.run_command("new_view", {
                "name": "package.xml",
                "input": ""
            })
        view.settings().set("selected_index", index)
        self.window.focus_view(view)
        types = view.settings().get("types", {})

        if not chosen_member:
            if not is_chosen or len(types[chosen_type]) != len(self.matched_package[chosen_type]):
                types[chosen_type] = self.matched_package[chosen_type]
            else:
                del types[chosen_type]
        elif chosen_type in types:
            if not is_chosen:
                if chosen_member not in types[chosen_type]:
                    types[chosen_type].append(chosen_member)
            else:
                if len(types[chosen_type]) > 1:
                    # If there has more than one member, just remove the chosen member
                    types[chosen_type].remove(chosen_member)
                else:
                    # If there is only one member, just remove the type
                    del types[chosen_type]
        else:
            types[chosen_type] = [chosen_member]

        view.settings().set("types", types)

        # Build package.xml content
        metadata_objects = []
        for _type in types:
            metadata_objects.append(
                "<types>%s<name>%s</name></types>" % (
                    "".join(["<members>%s</members>" % m for m in types[_type]]),
                    _type
                )
            )

        self.package_xml_content = """<?xml version="1.0" encoding="UTF-8"?>
            <Package xmlns="http://soap.sforce.com/2006/04/metadata">
                {metadata_objects}
                <version>{api_version}.0</version>
            </Package>
        """.format(
            metadata_objects="".join(metadata_objects),
            api_version=self.settings["api_version"]
        )

        view.run_command("new_dynamic_view", {
            "view_name": "package.xml",
            "erase_all": True,
            "input": util.format_xml(self.package_xml_content).decode("UTF-8")
        })

        sublime.set_timeout(lambda:self.on_input_filters(",".join(self.filters)), 10)

    def is_enabled(self):
        self.settings = context.get_settings()
        described_metadata = util.get_described_metadata(self.settings)
        return described_metadata is not None

class BuildOrganizationPackageXml(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(BuildOrganizationPackageXml, self).__init__(*args, **kwargs)

    def run(self):
        settings = context.get_settings()
        package_cache = os.path.join(settings["workspace"], ".config", "package.json")
        if not os.path.exists(package_cache):
            return self.window.run_command("reload_project_cache", {
                "callback_command": "build_organization_package_xml"
            })

        # Get package cache in JSON format
        package = json.loads(open(package_cache).read())

        # Build package.xml content
        metadata_objects = []
        for metadata_object, members in package.items():
            # If there is no members, just skip
            if not members: continue
            
            metadata_objects.append(
                "<types>%s<name>%s</name></types>" % (
                    "".join(["<members>%s</members>" % m for m in members]),
                    metadata_object
                )
            )

        package_xml_content = """<?xml version="1.0" encoding="UTF-8"?>
            <Package xmlns="http://soap.sforce.com/2006/04/metadata">
                {metadata_objects}
                <version>{api_version}.0</version>
            </Package>
        """.format(
            metadata_objects="".join(metadata_objects),
            api_version=settings["api_version"]
        )

        import threading
        thread = threading.Thread(target=self.write_package_xml, 
            args=(package_xml_content, ))
        thread.start()

    def write_package_xml(self, content):
        settings = context.get_settings()
        package_xml_dir = os.path.join(settings["workspace"], ".config", "package.xml")
        Printer.get("log").write("Start to prepare package.xml file, which will be opened as a new view")
        with open(package_xml_dir, "wb") as fp:
            fp.write(util.format_xml(content))

        self.window.open_file(package_xml_dir)

class CreatePackageXml(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CreatePackageXml, self).__init__(*args, **kwargs)

    def run(self, dirs):
        _dir = dirs[0]
        settings = context.get_settings()
        package_xml_content = """<?xml version="1.0" encoding="UTF-8"?>
            <Package xmlns="http://soap.sforce.com/2006/04/metadata">
                <types>
                    <members>*</members>
                    <name>ApexClass</name>
                </types>
                <version>{0}.0</version>
            </Package>
        """.format(settings["api_version"])
        file_name = os.path.join(_dir, "package-%s.xml" % \
            time.strftime("%Y%m%d", time.localtime(time.time())))
        if os.path.isfile(file_name):
            message = "Package.xml is already exist, override?"
            if not sublime.ok_cancel_dialog(message, "Override?"):
                return

        with open(file_name, "wb") as fp:
            fp.write(util.format_xml(package_xml_content))

        # If created succeed, just open it
        sublime.active_window().open_file(file_name)

    def is_visible(self, dirs):
        if not dirs or len(dirs) > 1: return False
        return True

class DestructPackageXmlFromServer(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DestructPackageXmlFromServer, self).__init__(*args, **kwargs)

    def run(self, files=None):
        message = "Confirm to destruct elements in this package.xml from server?"
        if not sublime.ok_cancel_dialog(message, "Confirm?"): return

        try:
            with open(self._file, "rb") as fp:
                content = fp.read()
            self.types = util.build_package_types(content)
        except Exception as ex:
            Printer.get('error').write(str(ex))
            return

        processor.handle_destructive_package_xml(self.types)

    def is_visible(self, files=None):
        self._file = None
        
        if files and len(files) > 1: 
            return False
        elif files and len(files) == 1:
            # Invoked from sidebar menu
            self._file = files[0]
        else:
            # Invoked from context menu
            view = sublime.active_window().active_view()
            self._file = view.file_name()

        if not self._file or not self._file.endswith(".xml"):
            return False

        return True

class DeployPackage(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(DeployPackage, self).__init__(*args, **kwargs)

    def run(self, dirs, switch=True, source_org=None, chosen_classes=[]):
        settings = context.get_settings()
        source_org = settings["default_project_name"]

        if switch:
            return self.window.run_command("switch_project", {
                "callback_options": {
                    "callback_command": "deploy_package", 
                    "args": {
                        "dirs": dirs,
                        "switch": False,
                        "source_org": source_org
                    }
                }
            })

        deploy_options = settings["deploy_options"]
        testLevel = deploy_options.get("testLevel", "NoTestRun") 
        if testLevel == "RunSpecifiedTests" and not chosen_classes:
            return self.window.run_command("choose_test_classes", {
                "callback_options": {
                    "callback_command": "deploy_package", 
                    "args": {
                        "dirs": dirs,
                        "switch": False,
                        "source_org": source_org
                    }
                }
            })

        processor.handle_deploy_thread(
            util.compress_package(self.package_dir), 
            source_org=source_org,
            chosen_classes=chosen_classes
        );

    def is_visible(self, dirs):
        if not dirs: return False
        if len(dirs) > 1: return False

        if os.path.exists(dirs[0]+"/package.xml"):
            self.package_dir = dirs[0]
        elif os.path.exists(dirs[0]+"/src/package.xml"):
            self.package_dir = dirs[0] + "/src"
        else:
            return False

        return True

class RefreshPackage(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RefreshPackage, self).__init__(*args, **kwargs)

    def run(self, dirs):
        try:
            with open(self.package_xml, "rb") as fp:
                content = fp.read()
            types = util.build_package_types(content)
        except Exception as ex:
            Printer.get('error').write(str(ex))
            return

        processor.handle_retrieve_package(types, self.extract_to)

    def is_enabled(self, dirs):
        if not dirs or len(dirs) > 1:
            return False

        settings = context.get_settings()
        _dir = dirs[0]
        pname = settings["default_project_name"]
        if pname.lower() not in _dir.lower(): 
            return False

        if os.path.exists(_dir + "/src/package.xml"):
            self.package_xml = _dir + "/src/package.xml"
            self.extract_to = _dir
        elif os.path.exists(_dir + "/package.xml"):
            self.package_xml = _dir + "/package.xml"
            # <base_path>/<project_name>/src/package.xml
            # <base_path>/<project_name>/package.xml
            self.extract_to = _dir
            if _dir.endswith("src"):
                self.extract_to = os.path.split(_dir)[0] 
        else:
            return False

        return True

    def is_visible(self, dirs):
        return self.is_enabled(dirs)

class RetrievePackageXmlFromServer(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(RetrievePackageXmlFromServer, self).__init__(*args, **kwargs)

    def run(self, files=None):
        # Build types
        try:
            with open(self._file, "rb") as fp:
                content = fp.read()
            self.types = util.build_package_types(content)
        except Exception as ex:
            Printer.get('error').write(str(ex))
            return

        # Initiate extract_to
        path, name = os.path.split(self._file)
        name = name[:name.rfind(".")]
        time_stamp = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
        settings = context.get_settings()
        project_name = settings["default_project_name"]
        self.extract_to = os.path.join(path, "%s-%s-%s" % (
            project_name, name, time_stamp
        ))

        sublime.active_window().show_input_panel("Input ExtractedTo Path", 
            self.extract_to, self.on_input_extractto, None, None)

    def on_input_extractto(self, extract_to):
        # Check input
        if not extract_to or not os.path.isabs(extract_to):
            message = 'Invalid path, do you want to try again?'
            if not sublime.ok_cancel_dialog(message, "Try Again?"): return
            self.window.show_input_panel("Please Input Name: ", "", 
                self.on_input_extractto, None, None)
            return

        # Start retrieve
        processor.handle_retrieve_package(self.types, extract_to)

    def is_enabled(self, files=None):
        self._file = None
        
        if files and len(files) > 1: 
            return False
        elif files and len(files) == 1:
            # Invoked from sidebar menu
            self._file = files[0]
        else:
            # Invoked from context menu
            view = sublime.active_window().active_view()
            self._file = view.file_name()

        if not self._file or not self._file.endswith(".xml"):
            return False

        return True

    def is_visible(self, files=None):
        return self.is_enabled(files)