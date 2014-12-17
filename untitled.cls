import sublime
import sublime_plugin
import os

from . import context
from . import util
from .salesforce import xmltodict
from .salesforce.lib import apex
from .salesforce.lib import vf
from .salesforce.lib import html

class PackageCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0], "text.xml"):
            return []

        # Check whether current file is package file
        pattern = "<types>[\s.*<>\w/]+</types>"
        if not view.find_all(pattern): return

        location = locations[0]
        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))
        variable_name = view.substr(view.word(pt-1))

        # Get plugin settings
        s = sublime.load_settings("toolingapi.sublime-settings")
        settings = context.get_settings()

        completion_list = []

        # <name></name> completion
        full_line = view.full_line(pt)
        if "<name>" in view.substr(full_line):
            for component in s.get("metadata_types"):
                display = "%s\t%s" % (component["type"], "Metadata Type")
                completion_list.append((display, component["type"]))

                # Component Child
                if component["children"]:
                    for child in component["children"]:
                        display = "%s\t%s" % (child, component["type"])
                        completion_list.append((display, child))
            return completion_list

        # <members></members> completion
        if "<members>" in view.substr(full_line):
            matched_region = view.find("<name>\\w+</name>", full_line.begin())
            if not matched_region: return []
            matched_content = view.substr(matched_region)
            meta_type = matched_content[6:-7].strip()
            
            # Get the _dir, for example: <workspace>/src/classes
            if meta_type not in settings: return []
            folder = settings[meta_type]["folder"]
            _type = settings[meta_type]["type"]
            _dir = os.path.join(settings["workspace"], "src", folder)

            # File name completion
            if ch != ".":
                # List File Names
                for parent, dirnames, filenames in os.walk(_dir):
                    for _file in filenames:
                        if _file.endswith("-meta.xml"): continue
                        base, name = os.path.split(_file)
                        name, extension = name.split(".")
                        display = "%s\t%s" % (name, _type)
                        completion_list.append((display, name))

            # Child content of file name completion
            if ch == ".":
                # Object properties completion
                parent = settings[meta_type]
                parent_type = parent["type"]
                children = settings[meta_type]["children"]
                try:
                    file_name = os.path.join(_dir, variable_name+parent["extension"])
                    if os.path.isfile(file_name):
                        result = xmltodict.parse(open(file_name, "rb"))
                        key = children[meta_type]
                        childs = result[parent_type][key]
                        if isinstance(childs, dict): childs = [childs]
                        for child in childs:
                            if "fullName" not in child: continue
                            display = "%s\t%s" % (child["fullName"], meta_type)
                            completion_list.append((display, child["fullName"]))
                except KeyError as e:
                    if settings["debug_mode"]:
                        print ('[] Completion KeyError: %s' % str(e))

        return completion_list

class ApexCompletions(sublime_plugin.EventListener):
    """ There are two type of completions:
    1. Keyword Completion, including Standard Class Names, Custom Class Names and All Sobject Names
    2. Method and Properties Completion of Apex Standard Class and Custom Class
    3. Sobject Completion, e.g. 
        2.1 Field Completion, including fields, parentRelationships and childRelationships
        2.2 Picklist Value Completion
        2.3 Fields of parentRelationships
        2.4 SOQL Field List Completion
    """

    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0], "source.java"):
            return []

        location = locations[0]
        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))
        variable_name = view.substr(view.word(pt-1))

        # Get plugin settings
        settings = context.get_settings()

        # Get sobjects metadata and symbol tables
        metadata, symbol_tables = util.get_sobject_metadata_and_symbol_tables(settings["username"])

        # Get Sobjects Describe and ParentRelationships Describe
        sobjects_describe = {}
        parentRelationships = {}
        if metadata and "sobjects" in metadata: 
            sobjects_describe = metadata["sobjects"]
            parentRelationships = metadata.get("parentRelationships")

        completion_list = []
        if ch not in [".", "="]:
            if not settings["disable_keyword_completion"]:
                # Check whether has SOQL Completion
                is_between_start_and_from = False
                if not settings["disable_soql_field_completion"]:
                    matched_region, is_between_start_and_from, sobject_name =\
                        util.get_soql_match_region(view, pt)

                if not is_between_start_and_from:
                    # Add namespace to  keyword completions
                    for namespace in apex.apex_namespaces:
                        completion_list.append(("%s\tNameSpace" % namespace, namespace))

                    # Add all object name to keyword completions
                    for key in sorted(sobjects_describe.keys()):
                        sobject_name = sobjects_describe[key]["name"]
                        completion_list.append((sobject_name + "\tSobject", sobject_name))

                    # Add all standard class to keyword completions
                    for key in sorted(apex.apex_completions):
                        class_attrs = apex.apex_completions[key]
                        if isinstance(class_attrs, dict):
                            completion_list.append(("%s\t%s" % (class_attrs["name"], 
                                class_attrs["namespace"]), class_attrs["name"]))
                        elif isinstance(class_attrs, list):
                            for class_attr in class_attrs:
                                completion_list.append(("%s\t%s" % (class_attr["name"], 
                                    class_attr["namespace"]), class_attr["name"]))

                    # Add all custom class to keyword completions
                    apex_class_completion = util.get_component_completion(settings["username"], "ApexClass")
                    if apex_class_completion: 
                        completion_list.extend(apex_class_completion)

                    return completion_list

        # SOQL Field List Completion
        if ch == " ":
            if not settings["disable_soql_field_completion"]:
                matched_region, is_between_start_and_from, sobject_name = util.get_soql_match_region(view, pt)
                if not is_between_start_and_from or not sobject_name: return []

                # Check whether there has fields completions
                sobject_name = sobject_name.lower()

                if sobject_name in sobjects_describe:
                    sobject_describe = sobjects_describe.get(sobject_name)
                    completion_list = util.get_sobject_completion_list(sobject_describe)

        elif ch == ".":
            # Input Page., list all custom ApexPages
            if variable_name.lower() == 'page': 
                return util.get_component_completion(settings["username"], "ApexPage")

            # Get the variable type by variable name
            pattern = "([a-zA-Z_1-9]+[\\[\\]]*|(map+|list|set)[^\\n][<,.\\s>a-zA-Z_1-9]*)\\s+%s[,;\\s:=){]" % variable_name
            variable_type = util.get_variable_type(view, pt, pattern)
            variable_type = variable_type.lower()

            if not settings["disable_fields_completion"]:
                if variable_type.lower() in sobjects_describe:
                    sobject_name = variable_type.lower()
                elif variable_name.lower() in sobjects_describe:
                    sobject_name = variable_name.lower()
                else:
                    sobject_name = ""

                if sobject_name != "" and sobject_name in sobjects_describe:
                    sobject_describe = sobjects_describe.get(sobject_name)
                    completion_list = util.get_sobject_completion_list(sobject_describe)
                    
                    # If variable_name is not empty, show the methods extended from sobject
                    if variable_type: 
                        methods = apex.apex_completions["sobject"]["methods"]
                        for key in sorted(methods.keys()):
                            completion_list.append(("Sobject." + key, methods[key]))

            if not settings["disable_relationship_completion"] and parentRelationships:
                # Parent sobject Field completions
                if variable_name in parentRelationships:
                    # Because relationship name is not unique, so we need to display sobject name prefix
                    matched_sobjects = parentRelationships[variable_name]
                    if len(matched_sobjects) == 1:
                        sobject_name = matched_sobjects[0].lower()
                        if sobject_name in sobjects_describe:
                            completion_list = util.get_sobject_completion_list(
                                sobjects_describe[sobject_name],
                                display_child_relationships=False)
                    else:
                        for sobject in matched_sobjects:
                            if sobject.lower() not in sobjects_describe: continue
                            completion_list.extend(util.get_sobject_completion_list(
                                sobjects_describe[sobject.lower()],
                                prefix=sobject+".", 
                                display_child_relationships=False))

            # Add standard class in specified namespace to completions
            if variable_name in apex.apex_namespaces:
                for standard_class in apex.apex_namespaces[variable_name]:
                    completion_list.append(("%s\t%s" % (standard_class, variable_name), standard_class))

            # Check whether variable is standard class
            if variable_name.lower() in apex.apex_completions:
                class_name = variable_name.lower()
            elif variable_type.lower() in apex.apex_completions:
                class_name = variable_type.lower()
            else:
                class_name = None

            # If variable is standard class
            if class_name:
                class_attrs = apex.apex_completions[class_name]
                if isinstance(class_attrs, dict):
                    class_attr = class_attrs

                    # Get the methods by class_name
                    methods = class_attr["methods"]
                    for key in sorted(methods.keys()):
                        completion_list.append((key, methods[key]))

                    # Get the properties by class_name
                    properties = class_attr["properties"]
                    if isinstance(properties, dict):
                        for key in sorted(properties.keys()):
                            completion_list.append((key if "\t" in key else (key + "\tProperty"), properties[key]))

                elif isinstance(class_attrs, list):
                    for class_attr in class_attrs:
                        # Get the methods by class_name
                        methods = class_attr["methods"]
                        for key in sorted(methods.keys()):
                            left = "%s.%s.%s" % (class_attr["namespace"], class_attr["name"], key)
                            right = methods[key]
                            completion_list.append((left, right))

                        # Get the properties by class_name
                        properties = class_attr["properties"]
                        if isinstance(properties, dict):
                            for key in sorted(properties.keys()): 
                                left = "%s.%s.%s\tProperty" % (class_attr["namespace"], class_attr["name"], key)
                                right = properties[key]
                                completion_list.append((left, right))
            else:
                try:
                    # Check whether inner class property completion
                    matched_region = view.find_all("[a-zA-Z_1-9]+\\.[a-zA-Z_1-9]+\\s+%s[,;\\s:=){]" % variable_name)
                    if matched_region:
                        matched_str = view.substr(matched_region[0])
                        namespace, innerclass = matched_str[:matched_str.find(" ")].split(".")
                        if namespace.lower() in symbol_tables:
                            inners = symbol_tables[namespace.lower()]["inners"]
                            if innerclass.lower() in inners:
                                for key in inners[innerclass.lower()]:
                                    completion_list.append((key, inners[innerclass.lower()][key]))

                    # Not inner class completion
                    else:
                        if variable_name.lower() in symbol_tables:
                            outer = symbol_tables[variable_name.lower()]["outer"]
                        elif variable_type.lower() in symbol_tables:
                            outer = symbol_tables[variable_type.lower()]["outer"]
                        else:
                            outer = None

                        # Call Custom Class from different class
                        if outer:
                            for key in sorted(outer):
                                completion_list.append((key, outer[key]))

                        # Call Inner Class in the same class
                        elif view.file_name():
                            namespace, extension = util.get_file_attr(view.file_name())
                            if namespace and namespace.lower() in symbol_tables:
                                inners = symbol_tables[namespace.lower()]["inners"]

                                if variable_type.lower() in inners:
                                    inner = inners[variable_type.lower()]
                                    for key in sorted(inner):
                                        completion_list.append((key, inner[key]))
                except KeyError as ke:
                    pass

        elif ch == "=":
            if not settings["disable_picklist_value_completion"]:
                # Get the begin point of current line
                begin = view.full_line(pt).begin()

                # Get Sobject Variable Name and Field Name
                matched_region = view.find("[a-zA-Z_1-9]+\\.[a-zA-Z_1-9]+", begin)
                if not matched_region: return []
                variable_name, field_name = view.substr(matched_region).split(".")

                # Get Sobject Name
                pattern = "([a-zA-Z_1-9]+[\\[\\]]*|(map+|list|set)[<,.\\s>a-zA-Z_1-9]*)\\s+%s[,;\\s:=){]" % variable_name
                variable_type = util.get_variable_type(view, pt, pattern)
                variable_type = variable_type.lower()

                # Get sobject describe
                if variable_type.lower() in sobjects_describe:
                    sobject_name = variable_type.lower()
                elif variable_name.lower() in sobjects_describe:
                    sobject_name = variable_name.lower()
                else:
                    sobject_name = ""

                sobject_describe = sobjects_describe.get(sobject_name)

                # Get sobject picklist field describe
                if not sobject_describe: return []
                if field_name not in sobject_describe["picklist_fields"]: return []
                picklist_values = sobject_describe["picklist_fields"][field_name]

                completion_list = []
                for pv in picklist_values:
                    completion_list.append(("%s(%s)\t%s" % (pv["value"], pv["label"], field_name), " '%s'" % pv["value"]))

        return completion_list

class PageCompletions(sublime_plugin.EventListener):
    """ There are two kinds of completion, Visualforce and Html
    Visualforce Lib is based on Mavensmate
    Html Lib is based on EMMET
    
    1. input <, list all Tags of Visualforce and Html
    2. input :, list suffix of all Visualforce Components
    3. input space, list all attributes of tags, if tag attribute has predefined values, 
       output attr, otherwise, output attr="$1"
    4. input =, list all values of this corresponding attribute
    """

    def on_query_completions(self, view, prefix, locations):
        # Only trigger within HTML
        if not view.match_selector(locations[0], "text.html - source"): return []

        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))
        settings = context.get_settings()

        completion_list = []
        if ch == "<":
            # Visualforce Standard Components
            for tag in sorted(vf.tag_defs):
                completion_list.append((tag + "\tvf", tag))

            # Custom Component
            username = settings.get("username")
            component_completion_list = util.get_component_completion(username, "ApexComponent")
            completion_list.extend(component_completion_list)

            # Html Elements
            for tag in sorted(html.HTML_ELEMENTS_ATTRIBUTES):
                completion_list.append((tag + "\thtml", tag))

            completion_list.sort(key=lambda tup:tup[1])
                
        elif ch == ":":
            # Just Visualforce Component contains :
            matched_tag_prefix = view.substr(view.word(pt))

            # If tag prefix 'c', list all custom components
            if matched_tag_prefix == "c":
                username = settings.get("username")
                return util.get_component_completion(username, "ApexComponent")

            # Combine components
            tag_names = {}
            for tag_name in vf.tag_defs:
                tag_prefix, tag_suffix = tuple(tag_name.split(':'))

                if tag_prefix in tag_names:
                    tag_names[tag_prefix].append(tag_suffix)
                else:
                    tag_names[tag_prefix] = [tag_suffix]

            # If it's not valid tag prefix, just return
            if not matched_tag_prefix in tag_names: return []

            # Populate completion list  
            for tag_name in tag_names[matched_tag_prefix]:
                completion_list.append((tag_name + "\t" + matched_tag_prefix, tag_name))

        elif ch == " ":
            # Get the begin point of current line
            full_line_region = view.full_line(pt)
            full_line_begin = full_line_region.begin()

            ##########################################
            # Visualforce Attribute Completions
            ##########################################
            matched_region = view.find("<\\w+:\\w+", full_line_begin)
            if matched_region and full_line_region.contains(matched_region):
                matched_tag = view.substr(matched_region)[1:]

                # Combine the attr of matched visualforce tag
                if matched_tag in vf.tag_defs:
                    def_entry = vf.tag_defs[matched_tag]
                    for key, value in def_entry['attribs'].items():
                        if "values" in value:
                            completion_list.append((key + '\t' + value['type'], key))
                        else:
                            if value["type"] == "Object":
                                completion_list.append((key + '\t' + value['type'], key+'="{!$1}"$0'))
                            else:
                                completion_list.append((key + '\t' + value['type'], key+'="$1"$0'))

            ##########################################
            # Custom Component Attribute Completions
            ##########################################
            matched_region = view.find("<c:\\w+", full_line_begin)
            if matched_region and full_line_region.contains(matched_region):
                matched_tag = view.substr(matched_region)[1:]
                component_name = matched_tag.split(":")[1].strip()


            ##########################################
            # HTML Element Attribute Completions
            ##########################################
            matched_region = view.find("<\\w+\\s+", full_line_begin)

            # If matched region is found and matched block contains cursor point
            if matched_region and full_line_region.contains(matched_region):
                completion_list = []
                matched_tag = view.substr(matched_region)[1:].strip()
                if matched_tag in html.HTML_ELEMENTS_ATTRIBUTES:
                    def_entry = html.HTML_ELEMENTS_ATTRIBUTES[matched_tag]
                    for attr_name in sorted(def_entry):
                        if attr_name in html.HTML_ATTRIBUTES_VALUES and html.HTML_ATTRIBUTES_VALUES[attr_name]:
                            completion_list.append((attr_name + "\tattr", attr_name))
                        else:
                            completion_list.append((attr_name + "\tattr", attr_name+'="$1"$0'))

            # Sort the completion_list by first element
            completion_list.sort(key=lambda tup:tup[1])

        elif ch == "=":
            # Get the begin point of current line
            begin = view.full_line(pt).begin()

            ##########################################
            # Visualforce Attribute Values Completions
            ##########################################
            matched_region = view.find("<\\w+:\\w+", begin)
            if matched_region:
                # Get the Tag Name and Tag Attribute Name
                matched_tag = view.substr(matched_region)[1:]
                matched_attr_name = view.substr(view.word(pt-1))

                # Get the Attribute Values
                if matched_tag in vf.tag_defs and\
                        matched_attr_name in vf.tag_defs[matched_tag]["attribs"] and\
                        "values" in vf.tag_defs[matched_tag]["attribs"][matched_attr_name]:
                    for value in vf.tag_defs[matched_tag]["attribs"][matched_attr_name]["values"]:
                        completion_list.append((value + "\t" + matched_attr_name, '"%s"' % value))

            ##########################################
            # HTML Element Attribute Values Completions
            ##########################################
            matched_attr_name = view.substr(view.word(pt-1))
            if matched_attr_name in html.HTML_ATTRIBUTES_VALUES:
                for attr_value in html.HTML_ATTRIBUTES_VALUES[matched_attr_name]:
                    completion_list.append((attr_value + "\t" + matched_attr_name, '"%s"' % attr_value))

            # Sort the completion_list by first element
            completion_list.sort(key=lambda tup:tup[1])

        return (completion_list)