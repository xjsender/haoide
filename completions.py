import sublime, sublime_plugin
import re
import time

from . import context
from .salesforce.metadata import apex_completions

class SobjectCompletions(sublime_plugin.EventListener):
    """
    When you refresh all, your sobject completions will updated at the same time

    when you input a variable, this part will get the variable type by the variable
    and then get the field information according to the variable type
    """

    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0], "source.java"):
            return []

        # Load sobjects compoletions
        setting = sublime.load_settings("sobjects_completion.sublime-settings")

        # Load sobjects field meatadata
        toolingapi_settings = context.get_toolingapi_settings()
        username = toolingapi_settings["username"]

        # If current username is in settings, it means project is initiated
        if not setting.has(username):
            return

        location = locations[0]
        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))

        if ch != ".":
            return

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
        metadata = setting.get(username)
        completion_list = []
        if sobject in metadata:
            sobject = sobject
        elif sobject.capitalize() in metadata:
            sobject = sobject.capitalize()
        elif variable_name in metadata:
            sobject = variable_name
        elif variable_name.capitalize() in metadata:
            sobject = variable_name
        else: 
            return

        fields = metadata.get(sobject)
        for key in fields.keys():
            completion_list.append((sobject + "." + key, fields[key]))

        return (completion_list, sublime.INHIBIT_WORD_COMPLETIONS or sublime.INHIBIT_EXPLICIT_COMPLETIONS)

class ApexCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0], "source.java"):
            return []

        location = locations[0]
        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))

        if ch != ".":
            return

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
        pattern = "(\\w+\\s+|map<\\w+[\\D\\d]*>|list<\\w+[\\D\\d]*>|set<\\w+[\\D\\d]*>)\\s" +\
            variable_name + "\\s*[:;=)\\s]"
        matched_regions = view.find_all(pattern, sublime.IGNORECASE)
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

        completion_list = []
        class_name = ""
        if variable_name in apex_completions:
            class_name = variable_name
        elif variable_name.capitalize() in apex_completions:
            class_name = variable_name.capitalize()
        elif variable_type in apex_completions:
            class_name = variable_type
        elif variable_type.capitalize() in apex_completions:
            class_name = variable_type.capitalize()
        else:
            return

        # If class_name is "", it means not found in this view
        if class_name == "": return []

        # Get the methods by class_name
        methods = apex_completions.get(class_name)
        for key in methods.keys():
            completion_list.append((key, methods[key]))

        return (completion_list, sublime.INHIBIT_WORD_COMPLETIONS or sublime.INHIBIT_EXPLICIT_COMPLETIONS)

# Extends Sublime Text autocompletion to find matches in all open
# files. By default, Sublime only considers words from the current file.

# limits to prevent bogging down the system
MIN_WORD_SIZE = 3
MAX_WORD_SIZE = 30

MAX_VIEWS = 20
MAX_WORDS_PER_VIEW = 100
MAX_FIX_TIME_SECS_PER_VIEW = 0.01

class CrossViewCompletions(sublime_plugin.EventListener):
    """
    https://github.com/alienhard/SublimeAllAutocomplete/blob/master/all_views_completions.py
    """

    def on_query_completions(self, view, prefix, locations):
        words = []

        # Limit number of views but always include the active view. This
        # view goes first to prioritize matches close to cursor position.
        other_views = [v for v in sublime.active_window().views() if v.id != view.id]
        views = [view] + other_views
        views = views[0:MAX_VIEWS]

        for v in views:
            if len(locations) > 0 and v.id == view.id:
                view_words = v.extract_completions(prefix, locations[0])
            else:
                view_words = v.extract_completions(prefix)

            view_words = [w for w in view_words]
            view_words = self.filter_words(view_words)
            view_words = self.fix_truncation(v, view_words)
            words += view_words

        words = self.without_duplicates(words)
        matches = [(w, w) for w in words]
        return matches

    def filter_words(self, words):
        words = words[0:MAX_WORDS_PER_VIEW]
        return [w for w in words if MIN_WORD_SIZE <= len(w) <= MAX_WORD_SIZE]

    # keeps first instance of every word and retains the original order
    # (n^2 but should not be a problem as len(words) <= MAX_VIEWS*MAX_WORDS_PER_VIEW)
    def without_duplicates(self, words):
        result = []
        for w in words:
            if w not in result:
                result.append(w)
        return result


    # Ugly workaround for truncation bug in Sublime when using view.extract_completions()
    # in some types of files.
    def fix_truncation(self, view, words):
        fixed_words = []
        start_time = time.time()

        for i, w in enumerate(words):
            #The word is truncated if and only if it cannot be found with a word boundary before and after

            # this fails to match strings with trailing non-alpha chars, like
            # 'foo?' or 'bar!', which are common for instance in Ruby.
            truncated = view.find(r'\b' + re.escape(w) + r'\b', 0) is None
            if truncated:
                #Truncation is always by a single character, so we extend the word by one word character before a word boundary
                extended_words = []
                view.find_all(r'\b' + re.escape(w) + r'\w\b', 0, "$0", extended_words)
                if len(extended_words) > 0:
                    fixed_words += extended_words
                else:
                    # to compensate for the missing match problem mentioned above, just
                    # use the old word if we didn't find any extended matches
                    fixed_words.append(w)
            else:
                #Pass through non-truncated words
                fixed_words.append(w)

            # if too much time is spent in here, bail out,
            # and don't bother fixing the remaining words
            if time.time() - start_time > MAX_FIX_TIME_SECS_PER_VIEW:
                return fixed_words + words[i+1:]

        return fixed_words

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
        if ch != '<':
            return []

        # Not include chart component
        return ([
            ('apex:actionFunction\tVisualforce Page', 'apex:actionFunction name="$1" action="$2" rerender="$3" status="$4"/>'),
            ('apex:actionPoller\tVisualforce Page', 'apex:actionPoller action="$1" rerender="$2" interval="$3"/>'),
            ('apex:actionRegion\tVisualforce Page', 'apex:actionRegion>\n\t$1\n</apex:actionRegion>'),
            ('apex:actionStatus\tVisualforce Page', 'apex:actionStatus id="$1"/>'),
            ('apex:actionSupport\tVisualforce Page', 'apex:actionSupport event="$1" action="$2" rerender="$3" status="$4"/>'),
            ('apex:attribute\tVisualforce Page', 'apex:attribute name="$1" description="$2" type="$3" required=\"${4:true}\"/>'),
            ('apex:column\tVisualforce Page', 'apex:column value="$1"/>'),
            ('apex:commandButton\tVisualforce Page', 'apex:commandButton action="$1" value="$2" id="$3"/>'),
            ('apex:commandLink\tVisualforce Page', 'apex:commandLink action="$1" value="$2" id="$3"/>'),
            ('apex:component\tVisualforce Page', 'apex:component>\n\t$1\n</apex:component>'),
            ('apex:componentBody\tVisualforce Page', 'apex:componentBody />'),
            ('apex:composition\tVisualforce Page', 'apex:composition template="$1">\n\t$2\n</apex:composition>'),
            ('apex:dataList\tVisualforce Page', 'apex:dataList value="$1" var="$2" id="$3">\n\t$4\n</apex:dataList>'),
            ('apex:dataTable\tVisualforce Page', 'apex:dataTable value="$1" var="$2" id="$3">\n\t$4\n</apex:dataTable>'),
            ('apex:define\tVisualforce Page', 'apex:define name="$1"/>'),
            ('apex:detail\tVisualforce Page', 'apex:detail subject="$1" relatedList=\"${2:false}\" title=\"${3:false}\"/>'),
            ('apex:dynamicComponent\tVisualforce Page', 'apex:dynamicComponent componentValue="$1"/>'),
            ('apex:emailPublisher\tVisualforce Page', 'apex:emailPublisher />'),
            ('apex:enhancedList\tVisualforce Page', 'apex:enhancedList type="$1" height="$2" rowsPerPage="$3" id="$4"/>'),
            ('apex:facet\tVisualforce Page', 'apex:facet name="$1">$2<apex:facet/>'),
            ('apex:flash\tVisualforce Page', 'apex:flash src="$1" height="$2" width="$3"/>'),
            ('apex:form\tVisualforce Page', 'apex:form id="$1">\n\t$2\n</apex:form>'),
            ('apex:iframe\tVisualforce Page', 'apex:iframe src="$1" scrolling="$2" id="$3"/>'),
            ('apex:image\tVisualforce Page', 'apex:image id="$1" value="$2" width="$3" height="$4"/>'),
            ('apex:include\tVisualforce Page', 'apex:include pageName="$1"/>'),
            ('apex:includeScript\tVisualforce Page', 'apex:includeScript value="$1"/>'),
            ('apex:inlineEditSupport\tVisualforce Page', 'apex:inlineEditSupport showOnEdit="$1" cancelButton="$2" hideOnEdit="$3" event="$4"/>'),
            ('apex:inputCheckbox\tVisualforce Page', 'apex:inputCheckbox value="$1"/>'),
            ('apex:inputField\tVisualforce Page', 'apex:inputField value="$1"/>'),
            ('apex:inputHidden\tVisualforce Page', 'apex:inputHidden value="$1"/>'),
            ('apex:inputSecret\tVisualforce Page', 'apex:inputSecret value="$1"/>'),
            ('apex:inputText\tVisualforce Page', 'apex:inputText value="$1"/>'),
            ('apex:inputTextarea\tVisualforce Page', 'apex:inputTextarea value="$1"/>'),
            ('apex:insert\tVisualforce Page', 'apex:insert name="$1"/>'),
            ('apex:listViews\tVisualforce Page', 'apex:listViews name="$1"/>'),
            ('apex:message\tVisualforce Page', 'apex:message for="$1"/>'),
            ('apex:messages\tVisualforce Page', 'apex:messages />'),
            ('apex:outputField\tVisualforce Page', 'apex:outputField value="$1"/>'),
            ('apex:outputLabel\tVisualforce Page', 'apex:outputLabel value="$1" for="$2"/>'),
            ('apex:outputLink\tVisualforce Page', 'apex:outputLink value="$1"/>'),
            ('apex:outputPanel\tVisualforce Page', 'apex:outputPanel id="$1">\n\t$2\n</apex:outputPanel>'),
            ('apex:outputText\tVisualforce Page', 'apex:outputText value="$1"/>'),
            ('apex:page\tVisualforce Page', 'apex:page id="$1">\n\t$2\n</apex:page>'),
            ('apex:pageBlock\tVisualforce Page', 'apex:pageBlock mode=\"${1:detail}\">\n\t$2\n</apex:pageBlock>'),
            ('apex:pageBlockButtons\tVisualforce Page', 'apex:pageBlockButtons>\n\t$1\n</apex:pageBlockButtons>'),
            ('apex:pageBlockSection\tVisualforce Page', 'apex:pageBlockSection title="$1" columns="$2">\n\t$3\n</apex:pageBlockSection>'),
            ('apex:pageBlockSectionItem\tVisualforce Page', 'apex:pageBlockSectionItem>\n\t$1\n</apex:pageBlockSectionItem>'),
            ('apex:pageBlockTable\tVisualforce Page', 'apex:pageBlockTable value="$1" var="$2">\n\t$3\n</apex:pageBlockTable>'),
            ('apex:pageMessage\tVisualforce Page', 'apex:pageMessage summary="$1" srverity="$2" strength=\"${3:3}\"/>'),
            ('apex:pageMessages\tVisualforce Page', 'apex:pageMessages />'),
            ('apex:panelBar\tVisualforce Page', 'apex:panelBar>\n\t$1\n</apex:panelBar>'),
            ('apex:panelBarItem\tVisualforce Page', 'apex:panelBarItem label="$1">$2<apex:panelBarItem/>'),
            ('apex:panelGrid\tVisualforce Page', 'apex:panelGrid columns="$1">\n\t$2\n</apex:panelGrid>'),
            ('apex:panelGroup\tVisualforce Page', 'apex:panelGroup id="$1">\n\t$2\n</apex:panelGroup>'),
            ('apex:param\tVisualforce Page', 'apex:param value="$1"/>'),
            ('apex:relatedList\tVisualforce Page', 'apex:relatedList list="$1"/>'),
            ('apex:repeat\tVisualforce Page', 'apex:repeat value="$1" var="$2">\n\t$3\n</apex:repeat>'),
            ('apex:selectCheckboxes\tVisualforce Page', 'apex:selectCheckboxes value="$1">\n\t$2\n</apex:selectCheckboxes>'),
            ('apex:selectList\tVisualforce Page', 'apex:selectList value="$1" size="$2">\n\t$3\n</apex:selectList>'),
            ('apex:selectOption\tVisualforce Page', 'apex:selectOption itemValue="$1" itemLabel="$2"/>'),
            ('apex:selectOptions\tVisualforce Page', 'apex:selectOptions value="$1"/>'),
            ('apex:selectRadio\tVisualforce Page', 'apex:selectRadio value="$1">\n\t$2\n</apex:selectRadio>'),
            ('apex:stylesheet\tVisualforce Page', 'apex:stylesheet value="$1"/>'),
            ('apex:tab\tVisualforce Page', 'apex:tab label="$1" name="$2"/>'),
            ('apex:tabPanel\tVisualforce Page', 'apex:tabPanel>\n\t$2\n</apex:tabPanel>'),
            ('apex:toolbarGroup\tVisualforce Page', 'apex:toolbarGroup itemSeparator="$1" id="$2">\n\t$3\n</apex:toolbarGroup>'),
            ('apex:variable\tVisualforce Page', 'apex:variable var="$1" value="$2"/>'),
            ('apex:vote\tVisualforce Page', 'apex:vote objectId="$1"/>')

        ], sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)