import sublime, sublime_plugin
import re
import time

from . import context
from .salesforce.metadata import apex_completions
from .salesforce import vf

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
            return

        fields = metadata.get(sobject)
        for key in sorted(fields.keys()):
            completion_list.append((key, fields[key]))

        return (completion_list, sublime.INHIBIT_WORD_COMPLETIONS or sublime.INHIBIT_EXPLICIT_COMPLETIONS)

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
            # Get the variable name
            pt = pt - 1
            variable_name = view.substr(view.word(pt))

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
            if variable_name.lower() in apex_completions:
                class_name = variable_name.lower()
            elif variable_type.lower() in apex_completions:
                class_name = variable_type.lower()
            else:
                return

            # If class_name is "", it means not found in this view
            if class_name == "": return []

            # Get the methods by class_name
            methods = apex_completions[class_name]["methods"]
            for key in sorted(methods.keys()):
                completion_list.append((key, methods[key]))

            # Get the properties by class_name
            properties = apex_completions[class_name]["properties"]
            for key in (properties.keys()):
                completion_list.append((key, properties[key]))

        # After input <, list all sobjects and class
        elif ch == "<":
            # If list<, map< or set<, continue
            begin = view.full_line(pt).begin()
            matched_region = view.find("(list|map|set)<", begin, sublime.IGNORECASE)
            if not matched_region: return []
            if matched_region.begin() > begin: return

            # Add all sobjects to <> completions
            metadata = get_sobject_completions()
            for key in metadata:
                completion_list.append((key + "\t" + "Sobject", key))

            # Add all apex class to <> completions
            for key in apex_completions:
                class_name = apex_completions[key]["name"]
                completion_list.append((class_name + "\t" + "Class", class_name))

        # Sort tuple list by the first element of tuple
        completion_list.sort(key=lambda tup:tup[1])
        return (completion_list, sublime.INHIBIT_WORD_COMPLETIONS or sublime.INHIBIT_EXPLICIT_COMPLETIONS)

class PageCompletions(sublime_plugin.EventListener):
    """
    vf.py is stolen from https://github.com/joeferraro/MavensMate-SublimeText/blob/master/lib/vf.py
    Provide completions that match just after typing an opening angle bracket
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
            for tag in vf.tag_defs:
                completion_list.append((tag, tag))
        elif ch == " ":
            # Find the match tag
            begin = view.full_line(pt).begin()
            matched_region = view.find("<\\w+:\\w+", begin)
            if not matched_region: return []
            matched_tag = view.substr(matched_region)[1:]
            print (matched_tag)

            # Combine the attr of matched tag
            def_entry = vf.tag_defs[matched_tag]
            for key, value in def_entry['attribs'].items():
                completion_list.append((key + '\t' + value['type'], key+'="$1"$0'))

        return (completion_list)