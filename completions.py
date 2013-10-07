import sublime, sublime_plugin
import re
import time

from . import context
from .salesforce import metadata as apex
from .salesforce import vf
from .salesforce import html

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
                func_name +  ("()$0" if "()" in func else "($0)")))

        completion_list.sort(key=lambda tup:tup[1])
        return completion_list

def get_sobject_completions():
    # Load sobjects compoletions
    setting = sublime.load_settings("sobjects_completion.sublime-settings")

    # Load sobjects field meatadata
    toolingapi_settings = context.get_toolingapi_settings()
    username = toolingapi_settings["username"]

    # If current username is in settings, it means project is initiated
    if not setting.has(username):
        return {}

    return setting.get(username)

class SobjectCompletions(sublime_plugin.EventListener):
    """
    When you refresh all, your sobject completions will updated at the same time

    when you input a variable, this part will get the variable type by the variable
    and then get the field information according to the variable type
    """

    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0], "source.java"):
            return []

        location = locations[0]
        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))

        if ch != ".": return[]

        # Get the variable name
        variable_name = view.substr(view.word(pt))

        # Get the matched region by variable name
        # 1. Account.
        # 2. Account acc;
        # 3. Account acc = new Account()
        # 4. for (Account acc : accs)
        # 5. public static void updateAccount(Account acc)
        # 6. public Account acc {get; set;}
        matched_regions = view.find_all("\\w+\\s+" + variable_name + "\\s*[:;=)\s]")
        sobject = ""
        if len(matched_regions) > 0:
            matched_block = view.substr(matched_regions[0])
            sobject = matched_block.split(" ")[0]

        # If username is in settings, get the sobject fields describe dict
        metadata = get_sobject_completions()
        if not metadata: return

        completion_list = []
        if sobject in metadata:
            sobject = sobject
        elif sobject.capitalize() in metadata:
            sobject = sobject.capitalize()
        elif variable_name in metadata:
            sobject = variable_name
        elif variable_name.capitalize() in metadata:
            sobject = variable_name.capitalize()
        else: 
            return []

        sobject_describe = metadata.get(sobject)

        # Fields Describe
        for key in sorted(sobject_describe["fields"]):
            completion_list.append((key, sobject_describe["fields"][key]))

        # Child Relationship Describe
        for key in sorted(sobject_describe["childRelationships"]):
            completion_list.append((key, sobject_describe["childRelationships"][key]))           

        return (completion_list, 
            sublime.INHIBIT_WORD_COMPLETIONS or sublime.INHIBIT_EXPLICIT_COMPLETIONS)

class ApexCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0], "source.java"):
            return []

        location = locations[0]
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
            # String str; 
            # String str = 'abc';
            # for (String str : strs) {}
            # List<String> strs;
            # Set<String> strs;
            # Map<String> strs;
            pattern = "(\\w+|(map|list|set)[<,\\s>\w]*)\\s+" + variable_name + "[;\\s:=){]"
            matched_regions = view.find_all(pattern, sublime.IGNORECASE)
            variable_type = ""

            if len(matched_regions) > 0:
                matched_block = view.substr(matched_regions[0]).strip()
                # If list, map, set
                if "<" in matched_block and ">" in matched_block:
                    variable_type = matched_block.split("<")[0].strip()
                # String str
                # for (String str :)
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
                    completion_list.append((p + "\t NameSpace Class", p))
            elif isinstance(properties, dict):
                for key in sorted(properties.keys()): 
                    completion_list.append((key + "\tProperty", properties[key]))

        # After input <, list all sobjects and class
        elif ch == "<":
            # If list<, map< or set<, continue
            full_line = view.full_line(pt)
            matched_region = view.find("(list|map|set)<", full_line.begin(), sublime.IGNORECASE)
            if not matched_region: return []
            if not full_line.contains(matched_region): return []

            # Add all sobjects to <> completions
            metadata = get_sobject_completions()
            for key in sorted(metadata.keys()):
                completion_list.append((key + "\t" + "Sobject", key))

            # Add all apex class to <> completions
            for key in sorted(apex.apex_completions):
                class_name = apex.apex_completions[key]["name"]
                completion_list.append((class_name + "\t" + "Class", class_name))

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
        if not view.match_selector(locations[0],
                "text.html - source"):
            return []

        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))

        completion_list = []
        if ch == "<":
            # Visualforce Standard Components
            for tag in sorted(vf.tag_defs):
                completion_list.append((tag, tag))

            # Html Elements
            for tag in sorted(html.HTML_ELEMENTS_ATTRIBUTES):
                completion_list.append((tag, tag))
                
        elif ch == ":":
            # Just Visualforce Component contains :
            tag_prefix = view.substr(view.word(pt))
            if tag_prefix not in vf.tag_names: return []
            for tag_name in vf.tag_names[tag_prefix]:
                completion_list.append((tag_name + "\t" + tag_prefix, tag_name))

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
                            completion_list.append((attr_name, attr_name))
                        else:
                            completion_list.append((attr_name, attr_name+'="$1"$0'))

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
                matched_attr_region = view.find("\\s\\w+=", begin)
                matched_attr_name = view.substr(view.word(pt - 1))

                # Get the Attribute Values
                if matched_tag in vf.tag_defs and\
                        matched_attr_name in vf.tag_defs[matched_tag]["attribs"] and\
                        "values" in vf.tag_defs[matched_tag]["attribs"][matched_attr_name]:
                    for value in vf.tag_defs[matched_tag]["attribs"][matched_attr_name]["values"]:
                        completion_list.append((value + "\t" + matched_attr_name, '"%s"' % value))

            # Process Attribute Value of HTML Element
            matched_attr_name = view.substr(view.word(pt - 1))
            if matched_attr_name in html.HTML_ATTRIBUTES_VALUES:
                for attr_value in html.HTML_ATTRIBUTES_VALUES[matched_attr_name]:
                    completion_list.append((attr_value + "\t" + matched_attr_name, '"%s"' % attr_value))

        return (completion_list)