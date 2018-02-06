import sublime
import sublime_plugin
import os
import re
import json

from . import context
from . import util
from .salesforce import xmltodict
from .salesforce.lib import apex
from .salesforce.lib import vf
from .salesforce.lib import lightning
from .salesforce.lib import html
from .salesforce.lib import bootstrap
from .salesforce.lib import slds

from .salesforce.lib.panel import Printer


def load_sobject_cache(reload_cache=False, username=None):
    """ Reload component cache in globals()
    """
    if reload_cache or "metadata" not in globals():
        if not username:
            username = context.get_setting("username")
        metadata = util.get_sobject_metadata(username)
        globals()["metadata"] = metadata

    return globals()["metadata"]


class PackageCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0], "text.xml"):
            return []

        # Check whether current file is package file
        pattern = "<types>[\s.*<>\-\w/\%1-9]+</types>"
        if not view.find_all(pattern): return

        location = locations[0]
        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))
        variable_name = view.substr(view.word(pt-1))

        # Get plugin settings
        settings = context.get_settings()
        completion_list = []  

        describe_metadata = util.get_described_metadata(settings)
        if not describe_metadata:
            if settings["debug_mode"]:
                print("You must execute describe_metadata command before have completion")
            return completion_list
        metadata_objects = describe_metadata["metadataObjects"]

        # <name></name> completion
        full_line = view.full_line(pt)
        if "<name>" in view.substr(full_line):
            for mo in metadata_objects:
                display = "%s\t%s" % (mo["xmlName"], "Metadata Type")
                completion_list.append((display, mo["xmlName"]))

                # Get all Children
                childXmlNames = mo.get("childXmlNames", [])
                if isinstance(childXmlNames, str):
                    childXmlNames = [childXmlNames]
                    
                for child in childXmlNames:
                    display = "%s\t%s" % (child, mo["xmlName"])
                    completion_list.append((display, child))

            return completion_list

        # <members></members> completion
        elif "<members>" in view.substr(full_line):
            # Check whether package cache is exist in `.config/package.json`
            package_cache = util.get_package_info(settings)
            if not package_cache:
                message = "No completion before reload_project_cache"
                Printer.get("error").write(message)
                return completion_list

            matched_region = view.find("<name>\\w+</name>", full_line.begin())
            if not matched_region: return []
            matched_content = view.substr(matched_region)
            meta_type = matched_content[6:-7].strip()

            # List all members in `.config/package.json`
            if meta_type in package_cache:
                for member in package_cache[meta_type]:
                    completion_list.append(("%s\t%s" % (member, meta_type), member))

        return completion_list, sublime.INHIBIT_WORD_COMPLETIONS or sublime.INHIBIT_EXPLICIT_COMPLETIONS


class ApexCompletions(sublime_plugin.EventListener):
    """ There are two type of completions:
    1. Keyword Completion, including Standard Class Names, Custom Class Names and All Sobject Names
    2. Method and Properties Completion of Apex Standard Class and Custom Class
    3. Sobject Completion, e.g. 
        3.1 Field Completion, including fields, parentRelationships and childRelationships
        3.2 Picklist Value Completion
        3.3 Fields of parentRelationships
        3.4 SOQL Field List Completion
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
        username = settings["username"]
        
        # In order to speed up code completion,
        # store the "metadata" into globals()
        metadata = load_sobject_cache(username=username)

        # Get sobjects describe and symbol tables
        sobjects_describe = metadata.get("sobjects", {})
        parentRelationships = metadata.get("parentRelationships", {})
        symbol_tables = util.get_symbol_tables(username)

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
                        completion_list.append((sobject_name + "\tsObject", sobject_name))

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
                    apex_class_completion = util.get_component_completion(username, "ApexClass")
                    if apex_class_completion: 
                        completion_list.extend(apex_class_completion)

                    return completion_list

        # SOQL Field List Completion
        if ch == " ":
            if not settings["disable_soql_field_completion"]:
                matched_region, is_between_start_and_from, sobject_name = util.get_soql_match_region(view, pt)
                if not is_between_start_and_from or not sobject_name: return []
                matched_soql = view.substr(matched_region)

                # Check whether there has fields completions
                if sobject_name.lower() in sobjects_describe:
                    sobject_describe = sobjects_describe.get(sobject_name.lower())

                    # Find all matched parent-to-child query in this view
                    matches = view.find_all("\(\s*SELECT([\s\S]+?)\)", sublime.IGNORECASE)

                    child_relationship_name = None
                    is_cursor_in_child_query = False
                    for m in matches:
                        # This child query is not in the whole soql region
                        if not matched_region.contains(m):
                            continue

                        # Cursor point is not located in this child soql region
                        if not m.contains(pt):
                            continue

                        # Cursor point is in child query
                        is_cursor_in_child_query = True

                        # Cursor point is not located between select and from
                        if variable_name.lower() == "from":
                            continue
                        
                        ms = view.substr(m)
                        from_pos = ms.lower().find("from")
                        pos_of_space_after_from = ms.find(" ", from_pos+6)
                        child_relationship_name = ms[from_pos+5:pos_of_space_after_from].strip()

                    # There have three criteria when cursor point is different:
                    #   1. SELECT (SELECT  FROM <CursorPoint> ORDER BY Name ASC) FROM Account
                    #       - Just display parent to child relationship names
                    #       
                    #   2. SELECT (SELECT Id, <CursorPoint> FROM Opportunities) FROM Account
                    #       - Display fields and parent relationship names for child sObject
                    #       
                    #   3. SELECT Id, <CursorPoint>, (SELECT Id FROM Opportunities), <CursorPoint> FROM Account
                    #       - Display fields and parent relationship names for parent sObject
                    if not child_relationship_name:
                        if is_cursor_in_child_query:
                            # Just display child relationship names
                            completion_list = util.get_sobject_completion_list(
                                sobject_describe,
                                display_fields=False,
                                display_parent_relationships=False
                            )
                        else:
                            # Display all
                            completion_list = util.get_sobject_completion_list(
                                sobject_describe,
                                display_child_relationships=False
                            )
                    else:
                        childRelationships = sobject_describe.get("childRelationships")
                        if child_relationship_name in childRelationships:
                            child_sobject_name = childRelationships[child_relationship_name]
                            if child_sobject_name.lower() in sobjects_describe:
                                completion_list = util.get_sobject_completion_list(
                                    sobjects_describe.get(child_sobject_name.lower()), 
                                    prefix=child_sobject_name+".",
                                    display_child_relationships=False
                                )

                    return completion_list, sublime.INHIBIT_WORD_COMPLETIONS or sublime.INHIBIT_EXPLICIT_COMPLETIONS

        elif ch == ".":
            # Input Page., list all custom ApexPages
            if variable_name.lower() == 'page': 
                return util.get_component_completion(username, "ApexPage")

            # Get the variable type by variable name
            pattern = "([a-zA-Z_1-9]+[\\[\\]]*|(map+|list|set)[^\\n^(][<,.\\s>a-zA-Z_1-9]+)\\s+%s[,;\\s:=){]" % variable_name
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

            if not completion_list and not settings["disable_relationship_completion"]:
                # Because relationship name is not unique, so we need to display sobject name prefix
                matched_sobjects = parentRelationships.get(variable_name, [])
                if len(matched_sobjects) == 1:
                    sobject_name = matched_sobjects[0].lower()
                    if sobject_name in sobjects_describe:
                        completion_list = util.get_sobject_completion_list(
                            sobjects_describe[sobject_name],
                            display_child_relationships=False
                        )
                else:
                    for sobject in matched_sobjects:
                        if sobject.lower() not in sobjects_describe: 
                            continue
                        completion_list.extend(util.get_sobject_completion_list(
                            sobjects_describe[sobject.lower()],
                            prefix=sobject+".", 
                            display_child_relationships=False)
                        )

            # Add standard class in specified namespace to completions
            if variable_name in apex.apex_namespaces:
                for standard_class in apex.apex_namespaces[variable_name]:
                    completion_list.append(("%s\t%s" % (standard_class, variable_name), standard_class))

            # Check whether variable is standard class
            if variable_type.lower() in apex.apex_completions:
                class_name = variable_type.lower()
            elif variable_name.lower() in apex.apex_completions:
                class_name = variable_name.lower()
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

                            # Sometimes, the inner class name is same with standard class or sObject
                            # if this inner class is matched, ignore the standard completion
                            if innerclass.lower() in inners:
                                completion_list = []
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
                            attributes = util.get_file_attributes(view.file_name())
                            namespace = attributes["name"]
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
                # Get the row and col of current point
                cursor_row, cursor_col = view.rowcol(pt)

                # Get all matched regions
                matched_regions = view.find_all("([a-zA-Z_1-9]+\\.[a-zA-Z_1-9]+)")

                # Get the nearest matched region from start to end
                # for example, matched regions by above pattern are : 
                #       [(4, 24), (28, 57), (76, 96), (100, 129)]
                # If the second one has the same row with cursor point, so it
                # will be chosen as the right matched region
                matched_region = None
                for mr in matched_regions:
                    row, col = view.rowcol(mr.begin())
                    if cursor_row == row:
                        matched_region = mr

                if not matched_region: 
                    return []
                variable_name, field_name = view.substr(matched_region).split(".")

                # Get Sobject Name
                pattern = "([a-zA-Z_1-9]+[\\[\\]]*|(map+|list|set)[^\\n^(][<,.\\s>a-zA-Z_1-9]+)\\s+%s[,;\\s:=){]" % variable_name
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
                if not sobject_describe: 
                    return []
                if field_name not in sobject_describe["picklist_fields"]: 
                    return []
                picklist_values = sobject_describe["picklist_fields"][field_name]

                completion_list = []
                for pv in picklist_values:
                    completion_list.append(("%s(%s)\t%s" % (
                            pv["value"], pv["label"], field_name
                        ), " '%s'" % pv["value"]
                    ))

        return completion_list

class LightningCompletions(sublime_plugin.EventListener):
    """ Lightning Javascript completion

    1. Standard Event Completion
    2. Customized Event Completion
    3. ...
    """

    def on_query_completions(self, view, prefix, locations):
        # Only trigger within HTML
        if not view.match_selector(locations[0], "source.js"): 
            return []

        settings = context.get_settings()
        workspace = settings["workspace"]

        # Only work for lightning controller.js and helper.js
        file_name = view.file_name()
        if not file_name:
            return []
        if not file_name.endswith('Controller.js') and\
                not file_name.endswith('Helper.js'):
            return []

        # Get component name by cut off suffix
        component_name = ""
        for suffix in ["Controller.js", "Helper.js"]:
            if file_name.endswith(suffix):
                base, fullName = os.path.split(file_name)
                component_name = fullName[:-len(suffix)]
                break

        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))
        var_name = view.substr(view.word(pt-1))
        if var_name.startswith("$"):
            var_name = var_name[1:]
            
        completion_list = []
        if ch == ".":
            if var_name in lightning.standard_lib:
                _lib = lightning.standard_lib[var_name]

                if "sub_classes" in _lib:
                    for v in _lib["sub_classes"]:
                        completion_list.append((
                            "%s\tSub Class" % v, v
                        ))

                if "properties" in _lib:
                    for v in _lib["properties"]:
                        completion_list.append((
                            "%s\tProperty" % v, v
                        ))

                if "methods" in _lib:
                    for k, v in _lib["methods"].items():
                        completion_list.append((
                            "%s" % k, v
                        ))

                # Component completion, support CustomLabel, StaticResource now
                metaObject = lightning.standard_lib[var_name].get("metaObject")
                if metaObject:
                    completion_list = util.get_completion_from_cache(
                        settings, metaObject, True
                    )

            # Custom events completion
            if var_name == 'e':
                events = util.get_metadata_elements(
                    os.path.join(workspace, "src", "aura"),
                    ".evt"
                )
                for eve in events:
                    completion_list.append((
                        "c:%s\tCustom Event" % eve,
                        "c:%s" % eve
                    ))

            # Component attribute completion
            if var_name == 'v':
                attributes = util.get_component_attributes(
                    settings, component_name, is_lightning=True
                )

                for attribute in attributes:
                    display = "%s\t%s(%s)" % (
                        attribute["name"], 
                        attribute["description"],
                        attribute["type"].capitalize()
                    )
                    value = attribute["name"]
                    completion_list.append((display, value))

        # Keyword completion for standard lib
        if ch not in [".", "="]:
            if not settings["disable_keyword_completion"]:
                for k, v in lightning.standard_lib.items():
                    if v.get("sub_class"):
                        continue
                    prefix = v.get('prefix', '')
                    completion_list.append((
                        "%s%s\t%s" % (prefix, k, v.get("type", "")), 
                        "%s%s%s" % (
                            '\\' if prefix == "$" else "",
                            prefix, k
                        ),
                    ))


        return completion_list

class PageCompletions(sublime_plugin.EventListener):
    """ There are three kinds of completion, Visualforce, Html and Custom Lightning component
    Visualforce Lib is based on Mavensmate
    Html Lib is based on EMMET
    
    1. input <, list all Tags of Visualforce, Html and Lightning components
    2. input :, list suffix of all Visualforce and Lightning Components
    3. input space, list all attributes of tags, if tag attribute has predefined values, 
       output attr, otherwise, output attr="$1"
    4. input =, list all values of this corresponding attribute
    """

    def on_query_completions(self, view, prefix, locations):
        # Only trigger within HTML
        if not view.match_selector(locations[0], "text.html - source"): 
            return []

        # Get plugin settings
        settings = context.get_settings()
        username = settings["username"]

        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))
        next_char = view.substr(sublime.Region(pt + 2, pt + 3))
        variable_name = view.substr(view.word(pt-1))
        begin = view.full_line(pt).begin()

        # Determine if current file is Lightning
        file_name = view.file_name()
        if not file_name :
            is_lightning = False
        else:
            is_lightning = True if file_name.split(".")[-1] in ["app", "cmp", "evt"] else False

        # Get tag definition of Visualforce page or Lightning component
        tag_defs = lightning.tag_defs if is_lightning else vf.tag_defs

        # In order to speed up code completion,
        # store the "metadata" into globals()
        metadata = load_sobject_cache(username=username)
        sobjects_describe = metadata.get("sobjects", {})
            
        completion_list = []
        if ch in ["<", ":"]:
            # Check whether tag has ending, for example,
            # `<apex:page />` has ending, `<apex:page` doesn't have
            tag_has_ending = False

            for mr in view.find_all("<\w[\s\S]+?>"):
                if mr.contains(pt):
                    tag_has_ending = True

            if ch == "<":
                # Standard Lightning/Visualforce Components
                for tag in sorted(tag_defs):
                    attr = tag_defs[tag]
                    completion_list.append((tag + "\t%s" % attr["type"], tag if tag_has_ending else (tag + "$1>")))

                if is_lightning:
                    # Custom Lightning Component
                    completion_list.extend(util.get_component_completion(username, "AuraDefinitionBundle"))
                else:
                    # Custom Apex Component
                    completion_list.extend(util.get_component_completion(username, "ApexComponent"))

                # HTML Elements
                for tag in sorted(html.HTML_ELEMENTS_ATTRIBUTES):
                    completion_list.append((tag + "\thtml",
                                            tag if tag_has_ending else (tag + "$1>")))

                completion_list.sort(key=lambda tup: tup[1])

            elif ch == ":":
                # Just Visualforce and Lightning Component contain prefix/namespace :
                matched_tag_prefix = view.substr(view.word(pt))

                # If tag prefix 'c', list all custom Apex components or  Lightning components
                if matched_tag_prefix == "c":
                    if is_lightning:
                        return util.get_component_completion(username, "AuraDefinitionBundle")
                    else:
                        return util.get_component_completion(username, "ApexComponent")

                # Combine components
                tag_names = {}
                for tag_name in tag_defs:
                    tag_prefix, tag_suffix = tuple(tag_name.split(':'))

                    if tag_prefix in tag_names:
                        tag_names[tag_prefix].append(tag_suffix)
                    else:
                        tag_names[tag_prefix] = [tag_suffix]

                # If it's not valid tag prefix, just return
                if matched_tag_prefix not in tag_names:
                    return []

                # Populate completion list
                for tag_name in tag_names[matched_tag_prefix]:
                    completion_list.append((tag_name + "\t" + matched_tag_prefix,
                                            tag_name if tag_has_ending else (tag_name + "$1>")))

        elif ch == " ":
            # Get the begin point of current line
            cursor_row, cursor_col = view.rowcol(pt)

            ############################################################
            # Standard Visualforce/Lightning Attribute Completions
            ############################################################
            if not settings["disable_component_attribute_completion"]:
                # Get the two chars after course point
                # If these two chars is '="', it means attribute value is already exist
                # we will not add ="{!}" or ="" for this attribute
                forward_two_chars = view.substr(sublime.Region(pt + 2, pt + 4))

                # Get all matched regions
                matched_regions = view.find_all("<\w+:\w+[\s\S]*?>")

                # Choose the matched one that contains cursor point
                matched_region = None
                for mr in matched_regions:
                    if mr.contains(pt):
                        matched_region = mr
                        break

                if matched_region:
                    matched_tag = view.substr(matched_region).split(" ")[0][1:].strip()

                    # Combine the attr of matched Visualforce tag
                    if matched_tag in tag_defs:
                        def_entry = tag_defs[matched_tag]
                        for key, value in def_entry['attribs'].items():
                            display = "%s\t%s" % (key, value['type'])

                            # Has value completion
                            if "values" in value or value["type"] == "Boolean" or forward_two_chars == '="':
                                completion_list.append((display, key))
                                continue
                            
                            if value["type"] in ["Object", "ApexPages.Action"]:
                                completion_list.append((display, key+'="{!$1}"$0'))
                            else:
                                completion_list.append((display, key+'="$1"$0'))

            ######################################################
            # Custom Apex/Lightning Component Attribute Completions
            ######################################################
            # Get all matched regions
            if not settings["disable_custom_component_completion"]:
                matched_regions = view.find_all("<c:\\w+")

                # Get the nearest matched region from start to end
                # for example, matched regions by above pattern are :
                #       [(4, 24), (28, 57), (76, 96), (100, 129)]
                # the cursor point is int the next or same row
                # with the second one, so that one is the exact one
                matched_region = None
                for mr in matched_regions:
                    row, col = view.rowcol(mr.begin())
                    if cursor_row == row or cursor_row == row + 1:
                        matched_region = mr
                
                if matched_region:
                    matched_tag = view.substr(matched_region)[1:]
                    tag_name = matched_tag.split(":")[1].strip()
                    completion_list.extend(util.get_attribute_completion(settings, tag_name, is_lightning))

            ##########################################
            # HTML Element Attribute Completions
            ##########################################
            if not settings["disable_html_completion"]:
                # Get all matched regions
                matched_regions = view.find_all("<\w+\s+[\s\S]*?>")

                # Get the nearest matched region from start to end
                # for example, matched regions by above pattern are : 
                #       [(4, 24), (28, 57), (76, 96), (100, 129)]
                # the cursor point is int the next or same row 
                # with the second one, so that one is the exact one
                matched_region = None
                for mr in matched_regions:
                    if mr.contains(pt):
                        matched_region = mr

                # If matched region is found and matched block contains cursor point
                if matched_region:
                    matched_tag = view.substr(matched_region)[1:].split(" ")[0].strip()
                    if matched_tag in html.HTML_ELEMENTS_ATTRIBUTES:
                        def_entry = html.HTML_ELEMENTS_ATTRIBUTES[matched_tag]
                        for attr_name in sorted(def_entry):
                            if attr_name in html.HTML_ATTRIBUTES_VALUES and html.HTML_ATTRIBUTES_VALUES[attr_name]:
                                completion_list.append((attr_name + "\tattr", attr_name))
                            else:
                                completion_list.append((attr_name + "\tattr", attr_name+'="$1"$0'))

            ############################################
            # Bootstrap3 class name completions
            ############################################
            if not settings["disable_bootstrap_completion"]:
                matched_attribute_regions = view.find_all('\w+="[\w\s\-]*"')
                for mr in matched_attribute_regions:
                    if not mr.contains(pt):
                        continue
                    class_name = view.substr(mr).split("=")[0]
                    if class_name.lower() in ["styleclass", "class"]:
                        for class_name in bootstrap.classes:
                            completion_list.append(("%s\tBootstrap3" % class_name, class_name))
                        break

            # SLDS class name completions
            if not settings["disable_slds_completion"]:
                matched_attribute_regions = view.find_all('\w+="[\w\s\-]*"')
                for mr in matched_attribute_regions:
                    if not mr.contains(pt):
                        continue
                    class_name = view.substr(mr).split("=")[0]
                    if class_name.lower() == "class":
                        for class_name in slds.classes:
                            completion_list.append(("%s\tSLDS" % class_name, class_name))
                        break

            # Sort the completion_list by first element
            completion_list.sort(key=lambda tup: tup[1])

        elif ch == "=":
            ############################################################
            # Visualforce/Lightning Attribute Values Completions
            ############################################################
            if not settings["disable_component_attribute_value_completion"]:
                matched_regions = view.find_all("<\w+:\w+[\s\S]*?>")

                matched_region = None
                for mr in matched_regions:
                    if mr.contains(pt):
                        matched_region = mr

                if matched_region:
                    # Get the Tag Name and Tag Attribute Name
                    matched_tag = view.substr(matched_region)[1:]
                    matched_tag = matched_tag.split(" ")[0].strip()
                    matched_attr_name = view.substr(view.word(pt-1))

                    # Get the Attribute Values
                    if matched_tag in tag_defs and matched_attr_name in tag_defs[matched_tag]["attribs"]:
                        tag_attribute = tag_defs[matched_tag]["attribs"][matched_attr_name]

                        # If attr type boolean, add {!} to it
                        if tag_attribute["type"] == "Boolean":
                            completion_list.append(("{!}" + "\t" + matched_attr_name, '"{!$1}"$0'))
                            completion_list.append(("true" + "\t" + matched_attr_name, '"true"$0'))
                            completion_list.append(("false" + "\t" + matched_attr_name, '"false"$0'))

                        if "values" in tag_attribute:
                            for value in tag_attribute["values"]:
                                completion_list.append((value + "\t" + matched_attr_name, '"%s"' % value))

                            # If attribute support sobjects
                            if tag_attribute.get("supportSobjects"):
                                for key in sorted(sobjects_describe.keys()):
                                    sobject_name = sobjects_describe[key]["name"]
                                    completion_list.append((sobject_name + "\tsObject", '"%s"' % sobject_name))

                        return completion_list

            ##########################################
            # HTML Element Attribute Values Completions
            ##########################################
            if not settings["disable_html_completion"]:
                matched_attr_name = view.substr(view.word(pt-1))
                if matched_attr_name in html.HTML_ATTRIBUTES_VALUES:
                    for attr_value in html.HTML_ATTRIBUTES_VALUES[matched_attr_name]:
                        completion_list.append((attr_value + "\t" + matched_attr_name, '"%s"' % attr_value))

            # Sort the completion_list by first element
            completion_list.sort(key=lambda tup:tup[1])

        if ch in ['"']:
            # 1. sObject completion for standardController
            pattern = "<\\w+:\\w+\\s+standardController=\"\\w+\""
            matched_region = view.find(pattern, begin, sublime.IGNORECASE)
            if matched_region and matched_region.contains(pt): 
                for key in sorted(sobjects_describe.keys()):
                    sobject_name = sobjects_describe[key]["name"]
                    completion_list.append((sobject_name + "\tsObject", sobject_name))

            # 2. Custom class completion for extension or controller
            matched_region = view.find('(controller="\\w+"|extensions="\\w+")', begin)
            if matched_region and matched_region.contains(pt): 
                apex_class_completion = util.get_component_completion(username, "ApexClass")
                completion_list.extend(apex_class_completion)

            # 3. Add page completion for Visualforce page
            attr_name = variable_name
            if attr_name in vf.page_reference_attrs and not is_lightning:
                apex_class_completion = util.get_component_completion(username, "ApexPage")
                completion_list.extend(apex_class_completion)

            # 4. Bootstrap3 class name completions
            if not settings["disable_bootstrap_completion"]:
                matched_attribute_regions = view.find_all('\w+="[\w\s\-]*"')
                for mr in matched_attribute_regions:
                    if not mr.contains(pt):
                        continue
                    class_name = view.substr(mr).split("=")[0]
                    if class_name.lower() == "class":
                        for class_name in bootstrap.classes:
                            completion_list.append(("%s\tBootstrap3" % class_name, class_name))
                        break

            # 5. SLDS class name completions
            if not settings["disable_slds_completion"]:
                matched_attribute_regions = view.find_all('\w+="[\w\s\-]*"')
                for mr in matched_attribute_regions:
                    if not mr.contains(pt):
                        continue
                    class_name = view.substr(mr).split("=")[0]
                    print (class_name)
                    if class_name.lower() == "class":
                        for class_name in slds.classes:
                            completion_list.append(("%s\tSLDS" % class_name, class_name))
                        break
        
        # Completions for Lightning component interface, for example,
        #   e.g. force:appHostable, force:lightningQuickAction
        if ch in ['"', ',', ' ']:
            matched_region = view.find('(implements="[\\w\\s:\\,]+")', begin)
            if matched_region and matched_region.contains(pt):
                completion_list = []
                for _interface in lightning.component_interfaces:
                    completion_list.append(('%s\tInterface' % _interface, _interface))

        if ch == ".":
            ################################################################
            #  Custom label completion, fetched form .config/package.json
            ################################################################
            if variable_name.lower() == "label":
                return util.get_completion_from_cache(settings, "CustomLabel", is_lightning)

            ################################################################
            # Extension or Controller creation after # with specified pattern
            ################################################################
            if not view.file_name(): 
                return completion_list

            # Get the name of controller or extension
            pattern = '\\s+(controller="\\w+"|extensions="\\w+")'
            matched_regions = view.find_all(pattern)
            if not matched_regions: 
                return completion_list
            controller_name = view.substr(matched_regions[0]).split('"')[1]

            # Get the classes path
            base, filename = os.path.split(view.file_name())
            src, path = os.path.split(base)
            controller_path = os.path.join(src, "classes", controller_name+".cls")
            if not os.path.isfile(controller_path):
                return completion_list

            # Get the variable type in the respective controller
            # and then show the field list of variable type
            with open(controller_path, "rb") as fp:
                content = fp.read()

            # Page Variable Completion
            pattern = "[a-zA-Z_1-9]+\\s+%s[,;\\s:=){]" % variable_name
            match = re.compile(pattern.encode("utf-8"), re.IGNORECASE).search(content)
            if match and match.group():
                variable_type = match.group().decode("utf-8").split(" ")[0]
                if variable_type.lower() in sobjects_describe:
                    sobject_describe = sobjects_describe.get(variable_type.lower())
                    completion_list = util.get_sobject_completion_list(sobject_describe)

        return completion_list
