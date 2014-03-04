import sublime, sublime_plugin

from . import context
from . import util
from .salesforce.support import apex
from .salesforce.support import vf
from .salesforce.support import html

class symbol_table_completions(sublime_plugin.EventListener):
    """
    Just when utility class is open, completions list will show up
    """

    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0], "source.java"): return []

        location = locations[0]
        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))
        if ch != ".": return

        # Get the variable name
        variable_name = view.substr(view.word(pt))

        # Get the symbols in open view
        window = sublime.active_window()
        symbol_locations = window.lookup_symbol_in_index(variable_name)
        if len(symbol_locations) == 0: return
        view = window.find_open_file(symbol_locations[0][0])
        if view == None: return
        
        completion_list = []
        for region, func in view.symbols():
            func = func.strip()
            func_name = func.split("(")[0]

            # Exclude private method and not static method
            full_line = view.full_line(region)
            full_line_text = view.substr(full_line)
            if "private" in full_line_text: continue
            if "static" not in full_line_text: continue

            # Exclude if and class notation
            if func.startswith('if') or func.startswith('class'): continue
            matched_func_type_region = view.find("\\w+\\s+" + func_name, full_line.begin())
            matched_region_text = view.substr(matched_func_type_region)
            func_type = matched_region_text.split(' ')[0]

            # If no parameter, put the foucs at the end
            completion_list.append((func + "\t" + func_type, 
                func_name +  ("()$0" if "()" in func else "($1)$0")))

        completion_list.sort(key=lambda tup:tup[1])
        return completion_list

class SobjectCompletions(sublime_plugin.EventListener):
    """
    When you refresh all, your sobject completions will updated at the same time

    when you input a variable, this part will get the variable type by the variable
    and then get the field information according to the variable type
    """

    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0], "source.java"): return []

        location = locations[0]
        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))
        if ch not in [".", "="]: return []

        settings = context.get_toolingapi_settings()
        metadata = util.get_sobject_completions(settings["username"])
        if not metadata or "sobjects" not in metadata: return []

        # Get all related settings
        disable_fields_completion = settings["disable_fields_completion"]
        disable_relationship_completion = settings["disable_relationship_completion"]
        display_field_name_and_label = settings["display_field_name_and_label"]
        disable_picklist_value_completion = settings["disable_picklist_value_completion"]

        completion_list = []
        if ch == ".":
            # Get the variable name
            variable_name = view.substr(view.word(pt-1))

            completion_list = []
            if not disable_fields_completion:
                # Get the matched region by variable name
                matched_regions = view.find_all("[a-zA-Z_1-9]+\\s+" + variable_name + "\\s*[,:;=)\\s]")
                variable_type = ""
                if len(matched_regions) > 0:
                    matched_block = view.substr(matched_regions[0])
                    variable_type = matched_block.split(" ")[0]

                sobjects_describe = metadata["sobjects"]
                if variable_type.lower() in sobjects_describe:
                    sobject_name = variable_type.lower()
                elif variable_name.lower() in sobjects_describe:
                    sobject_name = variable_name.lower()
                else:
                    sobject_name = ""

                if sobject_name in sobjects_describe:
                    sobject_describe = sobjects_describe.get(sobject_name)
                    completion_list = util.get_sobject_completion_list(sobject_describe, 
                        display_field_name_and_label=display_field_name_and_label)
                    
                    # If variable_name is not empty, show the methods extended from sobject
                    if variable_type: 
                        methods = apex.apex_completions["sobject"]["methods"]
                        for key in sorted(methods.keys()):
                            completion_list.append(("Sobject." + key, methods[key]))

            if not disable_relationship_completion and not completion_list:
                sobjects_describe = metadata.get("sobjects")
                parentRelationships = metadata.get("parentRelationships")
                
                # Parent sobject Field completions
                if variable_name not in parentRelationships: return []

                # Because relationship name is not unique, so we need to display sobject name prefix
                matched_sobjects = parentRelationships[variable_name]
                if len(matched_sobjects) == 1:
                    sobject_name = matched_sobjects[0].lower()
                    if sobject_name not in sobjects_describe: return []
                    completion_list = util.get_sobject_completion_list(sobjects_describe[sobject_name], 
                        display_field_name_and_label=settings["display_field_name_and_label"],
                        display_child_relationships=False)
                else:
                    for sobject in matched_sobjects:
                        if sobject.lower() not in sobjects_describe: continue
                        completion_list.extend(util.get_sobject_completion_list(sobjects_describe[sobject.lower()], 
                            prefix=sobject+".", 
                            display_field_name_and_label=settings["display_field_name_and_label"],
                            display_child_relationships=False))

        elif ch == "=":
            if disable_picklist_value_completion: return []

            # Get the begin point of current line
            begin = view.full_line(pt).begin()

            # Get Sobject Variable Name and Field Name
            matched_region = view.find("[a-zA-Z_1-9]+\\.[a-zA-Z_1-9]+", begin)
            if not matched_region: return []
            variable_name, field_name = view.substr(matched_region).split(".")

            # Get Sobject Name
            matched_regions = view.find_all("[a-zA-Z_1-9]+\\s+" + variable_name + "\\s*[:;=)\\s]")
            sobject_name = ""
            if len(matched_regions): 
                matched_block = view.substr(matched_regions[0])
                sobject_name = matched_block.split(" ")[0]

            # Get sobject describe
            sobjects_describe = metadata["sobjects"]
            if sobject_name.lower() in sobjects_describe:
                sobject_name = sobject_name.lower()
            elif variable_name.lower() in sobjects_describe:
                sobject_name = variable_name.lower()
            else:
                return []
            sobject_describe = sobjects_describe.get(sobject_name)

            # Get sobject picklist field describe
            if field_name not in sobject_describe["picklist_fields"]: return []
            picklist_field_describe = sobject_describe["picklist_fields"][field_name]

            completion_list = []
            for picklist_field in sorted(picklist_field_describe.keys()):
                completion_list.append((picklist_field, picklist_field_describe[picklist_field]))

        return (completion_list, sublime.INHIBIT_WORD_COMPLETIONS or sublime.INHIBIT_EXPLICIT_COMPLETIONS)

class ApexCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0], "source.java"):
            return []

        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))

        completion_list = []
        if ch == ".":
            # Get the variable name
            variable_name = view.substr(view.word(pt - 1))
            
            # If variable_name is namespace, just display classes of this namespace
            # Strange Class: System, ApexPages, Database, Schema, Site, Messaging
            # these class has the same name with namespace, so just put these namespace classes
            # to class property
            if variable_name in apex.apex_namespaces:
                completion_list = [(c, c) for c in apex.apex_namespaces[variable_name]]
                return completion_list

            # Get the matched variable type
            pattern = "([a-zA-Z_1-9]+[\\[\\]]*|(map|list|set)[<,.\\s>a-zA-Z_1-9]*)\\s+" + variable_name + "[,;\\s:=){]"
            matched_regions = view.find_all(pattern, sublime.IGNORECASE)
            variable_type = ""

            if len(matched_regions) > 0:
                matched_block = view.substr(matched_regions[0]).strip()
                # If list, map, set
                if "<" in matched_block and ">" in matched_block:
                    variable_type = matched_block.split("<")[0].strip()
                # String[] strs;
                elif "[]" in matched_block:
                    variable_type = 'list'
                # String str;
                else:
                    variable_type = matched_block.split(" ")[0]

            class_name = ""
            if variable_name.lower() in apex.apex_completions:
                class_name = variable_name.lower()
            elif variable_type.lower() in apex.apex_completions:
                class_name = variable_type.lower()
            else:
                return

            # If class_name is "", it means not found in this view
            if class_name == "": return []

            # Get the methods by class_name
            methods = apex.apex_completions[class_name]["methods"]
            for key in sorted(methods.keys()):
                completion_list.append((key, methods[key]))

            # Get the properties by class_name
            properties = apex.apex_completions[class_name]["properties"]
            if isinstance(properties, list):
                for p in sorted(properties): 
                    completion_list.append((p + "\tNameSpace Class", p))
            elif isinstance(properties, dict):
                for key in sorted(properties.keys()): 
                    if "\t" in key:
                        completion_list.append((key, properties[key]))
                    else:
                        completion_list.append((key + "\tProperty", properties[key]))
        elif ch != "=" and prefix in "abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ":
            settings = context.get_toolingapi_settings()
            if not settings["disable_keyword_completion"]:
                sobjects_describe = util.get_sobject_completions(settings["username"]).get("sobjects")
                if sobjects_describe:
                    for key in sorted(sobjects_describe.keys()):
                        sobject_name = sobjects_describe[key]["name"]
                        completion_list.append((sobject_name + "\tSobject", sobject_name))

            # Add all apex class to <> completions
            for key in sorted(apex.apex_completions):
                class_name = apex.apex_completions[key]["name"]
                completion_list.append((class_name + "\tClass", class_name))

        # Sort tuple list by the first element of tuple
        # completion_list.sort(key=lambda tup:tup[1])
        return (completion_list, sublime.INHIBIT_WORD_COMPLETIONS or sublime.INHIBIT_EXPLICIT_COMPLETIONS)

class PageCompletions(sublime_plugin.EventListener):
    """
    vf.py is stolen from https://github.com/joeferraro/MavensMate-SublimeText/blob/master/lib/vf.py
    html.py is stolen from https://github.com/sergeche/emmet-sublime/blob/master/emmet_completions/meta.py
    
    1. input <, list all tag
    2. input : list all suffix of all visualforce Components
    3. input space, list all attributes of tags, if tag attribute has predefined values, 
       output attr, otherwise, output attr="$1"
    4. input =, list all values of this corresponding attribute
    """

    def on_query_completions(self, view, prefix, locations):
        # Only trigger within HTML
        if not view.match_selector(locations[0], "text.html - source"): return []

        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))

        completion_list = []
        if ch == "<":
            # Visualforce Standard Components
            for tag in sorted(vf.tag_defs):
                completion_list.append((tag + "\tvf", tag))

            # Html Elements
            for tag in sorted(html.HTML_ELEMENTS_ATTRIBUTES):
                completion_list.append((tag + "\thtml", tag))
                
        elif ch == ":":
            # Just Visualforce Component contains :
            matched_tag_prefix = view.substr(view.word(pt))

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
            begin = view.full_line(pt).begin()

            ##########################################
            # Visualforce Attribute Completions
            ##########################################
            matched_region = view.find("<\\w+:\\w+", begin)
            if matched_region:
                matched_tag = view.substr(matched_region)[1:]

                # Combine the attr of matched visualforce tag
                if matched_tag in vf.tag_defs:
                    def_entry = vf.tag_defs[matched_tag]
                    for key, value in def_entry['attribs'].items():
                        if "values" in value:
                            completion_list.append((key + '\t' + value['type'], key))
                        else:
                            completion_list.append((key + '\t' + value['type'], key+'="$1"$0'))

            ##########################################
            # HTML Element Attribute Completions
            ##########################################
            matched_region = view.find("<\\w+\\s+", begin)
            if matched_region:
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
                matched_attr_name = view.substr(view.word(pt - 1))

                # Get the Attribute Values
                if matched_tag in vf.tag_defs and\
                        matched_attr_name in vf.tag_defs[matched_tag]["attribs"] and\
                        "values" in vf.tag_defs[matched_tag]["attribs"][matched_attr_name]:
                    for value in vf.tag_defs[matched_tag]["attribs"][matched_attr_name]["values"]:
                        completion_list.append((value + "\t" + matched_attr_name, '"%s"' % value))

            ##########################################
            # HTML Element Attribute Values Completions
            ##########################################
            matched_attr_name = view.substr(view.word(pt - 1))
            if matched_attr_name in html.HTML_ATTRIBUTES_VALUES:
                for attr_value in html.HTML_ATTRIBUTES_VALUES[matched_attr_name]:
                    completion_list.append((attr_value + "\t" + matched_attr_name, '"%s"' % attr_value))

            # Sort the completion_list by first element
            completion_list.sort(key=lambda tup:tup[1])

        return (completion_list)