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
            pattern = "(\\w+\\s+|map<\\w+,[\\s<]*\\w+[>]*>|list<\\w+[<>\\w]*>|set<\\w+[<>\\w]*>)\\s+" +\
                variable_name + "\\s*[:;=)\\s]"
            print (pattern)
            matched_regions = view.find_all(pattern, sublime.IGNORECASE)
            print (variable_name)
            print (matched_regions)

            variable_type = ""

            if len(matched_regions) > 0:
                matched_block = view.substr(matched_regions[0])
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
            # Add all sobjects to <> completions
            metadata = get_sobject_completions()
            for key in metadata:
                completion_list.append((key + "\t", key))

            # Add all apex class to <> completions
            for key in apex_completions:
                class_name = apex_completions[key]["name"]
                completion_list.append((class_name + "\t", class_name))

        # Sort tuple list by the first element of tuple
        completion_list.sort(key=lambda tup:tup[1])
        return (completion_list, sublime.INHIBIT_WORD_COMPLETIONS or sublime.INHIBIT_EXPLICIT_COMPLETIONS)

class PageCompletions(sublime_plugin.EventListener):
    """
    Provide completions that match just after typing an opening angle bracket
    https://github.com/jairzh/sublime-sfdc-assist/blob/master/visualforce_completions.py
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
                completion_list.append((key + '\t' + value['type'], key+'="$1" $0'))

        return (completion_list)

        # # Not include chart component
        # return ([
        #     ('apex:actionFunction\tVisualforce Page', 'apex:actionFunction name="$1" action="$2" rerender="$3" status="$4"/>'),
        #     ('apex:actionPoller\tVisualforce Page', 'apex:actionPoller action="$1" rerender="$2" interval="$3"/>'),
        #     ('apex:actionRegion\tVisualforce Page', 'apex:actionRegion>\n\t$1\n</apex:actionRegion>'),
        #     ('apex:actionStatus\tVisualforce Page', 'apex:actionStatus id="$1"/>'),
        #     ('apex:actionSupport\tVisualforce Page', 'apex:actionSupport event="$1" action="$2" rerender="$3" status="$4"/>'),
        #     ('apex:attribute\tVisualforce Page', 'apex:attribute name="$1" description="$2" type="$3" required=\"${4:true}\"/>'),
        #     ('apex:column\tVisualforce Page', 'apex:column value="$1"/>'),
        #     ('apex:commandButton\tVisualforce Page', 'apex:commandButton action="$1" value="$2" id="$3"/>'),
        #     ('apex:commandLink\tVisualforce Page', 'apex:commandLink action="$1" value="$2" id="$3"/>'),
        #     ('apex:component\tVisualforce Page', 'apex:component>\n\t$1\n</apex:component>'),
        #     ('apex:componentBody\tVisualforce Page', 'apex:componentBody />'),
        #     ('apex:composition\tVisualforce Page', 'apex:composition template="$1">\n\t$2\n</apex:composition>'),
        #     ('apex:dataList\tVisualforce Page', 'apex:dataList value="$1" var="$2" id="$3">\n\t$4\n</apex:dataList>'),
        #     ('apex:dataTable\tVisualforce Page', 'apex:dataTable value="$1" var="$2" id="$3">\n\t$4\n</apex:dataTable>'),
        #     ('apex:define\tVisualforce Page', 'apex:define name="$1"/>'),
        #     ('apex:detail\tVisualforce Page', 'apex:detail subject="$1" relatedList=\"${2:false}\" title=\"${3:false}\"/>'),
        #     ('apex:dynamicComponent\tVisualforce Page', 'apex:dynamicComponent componentValue="$1"/>'),
        #     ('apex:emailPublisher\tVisualforce Page', 'apex:emailPublisher />'),
        #     ('apex:enhancedList\tVisualforce Page', 'apex:enhancedList type="$1" height="$2" rowsPerPage="$3" id="$4"/>'),
        #     ('apex:facet\tVisualforce Page', 'apex:facet name="$1">$2<apex:facet/>'),
        #     ('apex:flash\tVisualforce Page', 'apex:flash src="$1" height="$2" width="$3"/>'),
        #     ('apex:form\tVisualforce Page', 'apex:form id="$1">\n\t$2\n</apex:form>'),
        #     ('apex:iframe\tVisualforce Page', 'apex:iframe src="$1" scrolling="$2" id="$3"/>'),
        #     ('apex:image\tVisualforce Page', 'apex:image id="$1" value="$2" width="$3" height="$4"/>'),
        #     ('apex:include\tVisualforce Page', 'apex:include pageName="$1"/>'),
        #     ('apex:includeScript\tVisualforce Page', 'apex:includeScript value="$1"/>'),
        #     ('apex:inlineEditSupport\tVisualforce Page', 'apex:inlineEditSupport showOnEdit="$1" cancelButton="$2" hideOnEdit="$3" event="$4"/>'),
        #     ('apex:inputCheckbox\tVisualforce Page', 'apex:inputCheckbox value="$1"/>'),
        #     ('apex:inputField\tVisualforce Page', 'apex:inputField value="$1"/>'),
        #     ('apex:inputHidden\tVisualforce Page', 'apex:inputHidden value="$1"/>'),
        #     ('apex:inputSecret\tVisualforce Page', 'apex:inputSecret value="$1"/>'),
        #     ('apex:inputText\tVisualforce Page', 'apex:inputText value="$1"/>'),
        #     ('apex:inputTextarea\tVisualforce Page', 'apex:inputTextarea value="$1"/>'),
        #     ('apex:insert\tVisualforce Page', 'apex:insert name="$1"/>'),
        #     ('apex:listViews\tVisualforce Page', 'apex:listViews name="$1"/>'),
        #     ('apex:message\tVisualforce Page', 'apex:message for="$1"/>'),
        #     ('apex:messages\tVisualforce Page', 'apex:messages />'),
        #     ('apex:outputField\tVisualforce Page', 'apex:outputField value="$1"/>'),
        #     ('apex:outputLabel\tVisualforce Page', 'apex:outputLabel value="$1" for="$2"/>'),
        #     ('apex:outputLink\tVisualforce Page', 'apex:outputLink value="$1"/>'),
        #     ('apex:outputPanel\tVisualforce Page', 'apex:outputPanel id="$1">\n\t$2\n</apex:outputPanel>'),
        #     ('apex:outputText\tVisualforce Page', 'apex:outputText value="$1"/>'),
        #     ('apex:page\tVisualforce Page', 'apex:page id="$1">\n\t$2\n</apex:page>'),
        #     ('apex:pageBlock\tVisualforce Page', 'apex:pageBlock mode=\"${1:detail}\">\n\t$2\n</apex:pageBlock>'),
        #     ('apex:pageBlockButtons\tVisualforce Page', 'apex:pageBlockButtons>\n\t$1\n</apex:pageBlockButtons>'),
        #     ('apex:pageBlockSection\tVisualforce Page', 'apex:pageBlockSection title="$1" columns="$2">\n\t$3\n</apex:pageBlockSection>'),
        #     ('apex:pageBlockSectionItem\tVisualforce Page', 'apex:pageBlockSectionItem>\n\t$1\n</apex:pageBlockSectionItem>'),
        #     ('apex:pageBlockTable\tVisualforce Page', 'apex:pageBlockTable value="$1" var="$2">\n\t$3\n</apex:pageBlockTable>'),
        #     ('apex:pageMessage\tVisualforce Page', 'apex:pageMessage summary="$1" srverity="$2" strength=\"${3:3}\"/>'),
        #     ('apex:pageMessages\tVisualforce Page', 'apex:pageMessages />'),
        #     ('apex:panelBar\tVisualforce Page', 'apex:panelBar>\n\t$1\n</apex:panelBar>'),
        #     ('apex:panelBarItem\tVisualforce Page', 'apex:panelBarItem label="$1">$2<apex:panelBarItem/>'),
        #     ('apex:panelGrid\tVisualforce Page', 'apex:panelGrid columns="$1">\n\t$2\n</apex:panelGrid>'),
        #     ('apex:panelGroup\tVisualforce Page', 'apex:panelGroup id="$1">\n\t$2\n</apex:panelGroup>'),
        #     ('apex:param\tVisualforce Page', 'apex:param value="$1"/>'),
        #     ('apex:relatedList\tVisualforce Page', 'apex:relatedList list="$1"/>'),
        #     ('apex:repeat\tVisualforce Page', 'apex:repeat value="$1" var="$2">\n\t$3\n</apex:repeat>'),
        #     ('apex:selectCheckboxes\tVisualforce Page', 'apex:selectCheckboxes value="$1">\n\t$2\n</apex:selectCheckboxes>'),
        #     ('apex:selectList\tVisualforce Page', 'apex:selectList value="$1" size="$2">\n\t$3\n</apex:selectList>'),
        #     ('apex:selectOption\tVisualforce Page', 'apex:selectOption itemValue="$1" itemLabel="$2"/>'),
        #     ('apex:selectOptions\tVisualforce Page', 'apex:selectOptions value="$1"/>'),
        #     ('apex:selectRadio\tVisualforce Page', 'apex:selectRadio value="$1">\n\t$2\n</apex:selectRadio>'),
        #     ('apex:stylesheet\tVisualforce Page', 'apex:stylesheet value="$1"/>'),
        #     ('apex:tab\tVisualforce Page', 'apex:tab label="$1" name="$2"/>'),
        #     ('apex:tabPanel\tVisualforce Page', 'apex:tabPanel>\n\t$2\n</apex:tabPanel>'),
        #     ('apex:toolbarGroup\tVisualforce Page', 'apex:toolbarGroup itemSeparator="$1" id="$2">\n\t$3\n</apex:toolbarGroup>'),
        #     ('apex:variable\tVisualforce Page', 'apex:variable var="$1" value="$2"/>'),
        #     ('apex:vote\tVisualforce Page', 'apex:vote objectId="$1"/>')

        # ], sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)