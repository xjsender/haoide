.. :changelog:

Release History
-----------------


Build 3.6.1 (2021-01-13)
++++++++++++++++++++++++++++++++++++
* Removed component metadata cache after destructing
* Updated new Apex classes in Salesforce release v50.0
* Updated documentations, added Issue Report Guidance
* Miscellaneous bug fixings and refinements


Release 3.6.0 (2020-03-30)
++++++++++++++++++++++++++++++++++++
* Implemented Save lwc file to Server last one
    - Now you can save ``lwc`` HTML markup, JavaScript code, CSS file, SVG resource and **Additional JS files** to Salesforce directly by ``HaoIDE``
* Update component metadata after Creating Lightning Web Component or `lwc` resource like CSS, SVG, Additional JS files
* Updated related documentations.
* Miscellaneous bug fix and refinement.


Release 3.5.9 (2020-03-29)
++++++++++++++++++++++++++++++++++++

* Implemented Save lwc file to Server
    - Now you can save ``lwc`` HTML markup, JavaScript code, CSS file, SVG resource and additional JS files to Salesforce separately
* Update documents
    - updated documentations on auto completion, debug, lwc and etc.
* Miscellaneous bug fix and refinement


Release 3.5.8 (2020-03-28)
++++++++++++++++++++++++++++++++++++

* Refined Code coverage functionality:
   - View code coverage for certain Apex class/trigger file via context menu
   - View code coverage from (async) Test Result via context menu
* Miscellaneous bug fix and update


Release 3.5.7 (2020-03-26)
++++++++++++++++++++++++++++++++++++

* Refine Creating Lightning Web Component (``lwc``) process
* Add Retrieving, Destructing, Deploying lwc from both sidebar and context menu
* Add Creating CSS style, SVG file for lwc in context menu
* Fix auto completion for aura component bug
* Fix issue #198


Release 3.5.4 (2019-07-31)
++++++++++++++++++++++++++++++++++++
* Add component tag attr desc completion when hover on attr
* Add user interface api doc reference toc
* lwc supports label, staticresource, custom object and fields import
* Enhancement for lwc boolean attr completion
* Fix bug for meta file deployment


Release 3.5.4 (2018-02-12)
++++++++++++++++++++++++++++++++++++
* Fix issue #172
* Fix issue #173


Release 3.5.3 (2018-02-06)
++++++++++++++++++++++++++++++++++++
* Add missing base components from lightning developer guide by script: https://gist.github.com/xjsender/265d237fbeafebabff6c8669f9359fff#file-read-json-from-lightning-compnent-js
* Add $A.localizationService lib
* Fix some minor bugs


Release 3.5.2 (2018-02-03)
++++++++++++++++++++++++++++++++++++
* Support oAuth2 Login, check https://github.com/xjsender/haoide#project-configuration for guide
* Add Lightning event methods completion
* Add customlabel and staticresource completions for lightning component
* Add lightning component iconName support
* Add package.zip to file_exclude_patterns
* Add attributes completion after v.
* Update apex lib to v41
* Deliver enhancement for issue #145
* Fix custom label completion bug in Lightning mode
* Fix bug for open_aura_document_reference command
* Fix bug #147


Release 3.5.1 (2018-01-25)
++++++++++++++++++++++++++++++++++++
* Basic completion support for component controller or helper


Release 3.5.0 (2018-01-21)
++++++++++++++++++++++++++++++++++++
* Add aura component and attribute completion, contributed by @lushang
* Add some missed base component
* Add lightning component implements completion
* Add Queueable Apex Template
* Add SLDS classes completion
* Add some console snippets
* Add sObject completion when attribute support sObjects, such as type for aura:attribute
* Update export format for ``Export Profile`` command
* Fix some bugs, such as, aura app preview, custom label completion, etc.


Release 3.4.7 (2017-07-29)
++++++++++++++++++++++++++++++++++++
* Really and still busy on project delivery work in the past year, will continue in the next days.
* New Fetaure: Combine package.xml in selected folders
* New Feature: Custom Label completion support, which is fetched from ``project/.config/package.json`` by ``Reload Project Cache`` command
* Update Aura completion lib by ``lushang``
* Others


Release 3.4.6 (2016-09-26)
++++++++++++++++++++++++++++++++++++
* Deliver enhancement for issue #132
* Deliver enhancement for issue #134
* Deliver enhancement for issue #140
* Fix issue #138


Release 3.4.5 (2016-06-16)
++++++++++++++++++++++++++++++++++++
* Fix bug: sublime will be closed when view debug log by logId with pressing alt + dblclick left mouse
* Fix issue #126
* Deliver feature #119
* Add a new setting ``force_login_interval`` for controlling login cache refresh interval


Release 3.4.4 (2016-06-11)
++++++++++++++++++++++++++++++++++++
* Fix Urgent ``FileNotFoundError`` problem when create new code


Release 3.4.3 (2016-06-06)
++++++++++++++++++++++++++++++++++++
* Hide ``execute query`` command in the context menu, use ``REST TEST Query`` instead
* Rename Snippet ``HttpRequest - Authorization Basic Credentials.sublime-snippet`` to ``HttpRequest - Callout.sublime-snippet``
* Add new snippet named ``Page - loading action status.sublime-snippet``
* Add visibility control for ``Extract To Here`` in the sidebar menu
* Fix bug for custom components completion
* Fix bug for variable type fetching for code completion
* Fix issue #117


Release 3.4.2 (2016-05-23)
++++++++++++++++++++++++++++++++++++
* Change api version back to 35, fix issue #116


Release 3.4.1 (2016-05-23)
++++++++++++++++++++++++++++++++++++
* Fix issue #113
* Fix issue #115
* Fix Bug for conflict checking bug caused by solution for issue #108
* Fix Bug for ``fetch debug log``
* Execute ``fetch_debug_log`` operation after ``run sync test``


Release 3.4.0 (2016-05-20)
++++++++++++++++++++++++++++++++++++
- Deliver enhancement for issue #108
- Deliver enhancement for issue #111
- Fix bug when test class failed caused by dependency compilation
- Fix bug when view debug log detail
- Fix bug when read csv encoding
- Fix bug When create first new code that will clear the cache of others
- Fix bug When deploy files, default project is not switched back 
- Remove duplicate command ``Reload Sobject Cache`` from command palette
- Remove snippet ``Class Body - class comments``
- Add new snippet: ``Page - close window and refresh opener``
- Add keymap for ``Open All Documents``, check the keymap setting for detail
- Add new command ``copy_files_to_project`` for issue #113
- Update snippet: ``Debug - debug info``, ``Debug - debug error``, ``Class Header - class header``
- Update include_users_in_role_hierarchy to false on default
- Update ``folder_exclude_patterns`` pattern to exclude ``.templates`` folder in the sidebar


Release 3.3.9 (2016-04-18)
++++++++++++++++++++++++++++++++++++
* Force login every two hours
* Add retry operation for list package if session is expired
* Change display format for REST TEST Response, add a new setting ``remove_slash_for_rest_response``
* Fix bug for aura creation
* Add AuraEnabled template class
* Add a snippet for class comments header
* Add a snippet for LoggingLevel.ERROR debug
* Update a snippet for LoggingLevel.INFO debug


Release 3.3.8 (2016-04-12)
++++++++++++++++++++++++++++++++++++
* Enhancement for code template, welcome new template pull request
* Add runSpecifiedTest support for deploying files
* Change mousemap key mapping, see more detail at Q&A
* Update Q&A in the pulgin home page


Release 3.3.7 (2016-03-28)
++++++++++++++++++++++++++++++++++++
* Fix issue #88
* Fix issue #99, problem of ``reload document``
* Deliver enhancement for issue #96
* Open exported CSV file when execute ``Export CustomField`` command


Release 3.3.6 (2016-03-28)
++++++++++++++++++++++++++++++++++++
* Fix issue #98
* Add ``Return to First Step`` feature when open documentation by type
* Remove build-in reference settings which is replaced ``Reload Salesforce Document``
* Enhancement for ``Open Documentation`` feature
* Enhancement for ``Reload Project Cache`` feature


Release 3.3.5 (2016-03-26)
++++++++++++++++++++++++++++++++++++
* Greatly improve performance of code completion
* Fix invalid scope problem for custom class completion
* Enhancement for document reference
* Change panel message format


Release 3.3.4 (2016-03-23)
++++++++++++++++++++++++++++++++++++
* Fix issue #93
* Fix issue #97
* Optimize for methods in ``metadata.py``
* Update README.md


Release 3.3.3 (2016-03-14)
++++++++++++++++++++++++++++++++++++
* Fix issue #94
* Enhance ``refresh package`` command
* Add package.xml update support for command ``build_package_xml``


Release 3.3.2 (2016-03-12)
++++++++++++++++++++++++++++++++++++
* Fix issue #92


Release 3.3.1 (2016-03-11)
++++++++++++++++++++++++++++++++++++
* Rename ``deploy_package_to_server`` command to ``deploy_package``
* Add new command ``refresh_package``, see issue #91 for detail
* Add LastModifiedBy check for conflict check logic, see issue #89
* Remove setting ``ignore_project_package_xml`` and related logic


Release 3.3.0 (2016-03-11)
++++++++++++++++++++++++++++++++++++
* Deliver enhancement #91
* Fix bug issue #92
* Fix package.xml onload XML parse exception


Release 3.2.9 (2016-03-10)
++++++++++++++++++++++++++++++++++++
* Enhancement for ``role hierarchy exporting``
* Add new settings ``include_users_in_role_hierarchy`` to control whether including user in the CSV
* Deliver new feature, see issue #89
* upgrade build-in requests lib to 2.9.1
* change display message for list metadata in the output panel


Release 3.2.8 (2016-02-26)
++++++++++++++++++++++++++++++++++++
* Fix issue #88
* Fix bug for ``export workflow rules`` feature
* Add parameter ``vertical`` for ``export_data_template`` command for exporting Layout Workbook
* Add a command for copying login url, which can be used for login with different browser
* Update version and copyright information


Release 3.2.7 (2015-12-21)
++++++++++++++++++++++++++++++++++++
* Fix issue #86


Release 3.2.6 (2015-12-20)
++++++++++++++++++++++++++++++++++++
* Fix issue #84
* Fix issue #85
* New ``Export > Export Role Hierarchy`` command


Release 3.2.5 (2015-12-15)
++++++++++++++++++++++++++++++++++++
* Fix urgent bug issue #83
* Fix urgent bug for sobject cache reloading
* Remove ``allowed_sobjects`` setting


Release 3.2.4 (2015-12-09)
++++++++++++++++++++++++++++++++++++
* Enhancement for lightning development
* Add new command for creating ``SVG`` and ``design``
* Update lightning related library
* Change default ``api_version`` from ``34`` to ``35``


Release 3.2.3 (2015-12-01)
++++++++++++++++++++++++++++++++++++
* Bug Fix:
    Fix bug for lightning development when deploying cmp or app

* Enhancement:
    - Display the lightning type in the input panel when creating lightning components
    - Change ``No change`` to ``no difference`` in non-difference message when executing ``diff_with_server`` command

* Update:
    - Remove four commands ``create_lightning_application``, ``create_lightning_component``, ``create_lightning_interface``, ``create_lightning_event``, bind the four features to ``create_lightning_definition`` by difference ``_type``
    - Optimize completion for Boolean attribute in the html related page
    - Stop keeping useless ``settings.json`` to ``.config`` folder


Release 3.2.2 (2015-11-19)
++++++++++++++++++++++++++++++++++++
* Bug Fix:
    - Fix TypeError when export soql to csv
    - Fix aura app preview problem
    - Fix bug for missing standard Objects when retrieve all
    - Fix bug for `deploy selected open files` fetaure
    - Fix instance parse problem for lightning app preview
    - Fix bug of aura helperjs or controoler deploy

* New Feature:
    - Add new command to open aura document reference in the command palette

* Enhancement:
    - Improve output message of debug mode
    - Update README.MD


Release 3.2.1 (2015-11-10)
++++++++++++++++++++++++++++++++++++
* Fix issue #81


Release 3.2.0 (2015-10-07)
++++++++++++++++++++++++++++++++++++
* Deliver enhancement #73
* Deliver enhancement #77


Release 3.1.9 (2015-08-26)
++++++++++++++++++++++++++++++++++++
* Fix issue #71, export workbooks by user input
* Fix bug for visibility problem of ``Retrieve Package.xml``
* Add bootstrap3 support for styleClass attribute of salesforce standard components


Release 3.1.8 (2015-08-08)
++++++++++++++++++++++++++++++++++++
* Bug Fix:
    - Fix bug for bootstrap3 completion
    - Fix bug for ``toggle_metadata_objects`` command if project is not initiated
    - Fix bug for ``SOQL - SELECT FROM.sublime.snippet`` in windows

* Enhancement:
    - Add confirm request for ``retrieve files from server`` and ``retrieve files from this server``
    - Add confirm request for ``destruct package.xml from server`` and ``retrieve files from this server``
    - Identify ``this file`` or ``these files`` in confirm request message according to number of chosen files

* Update:
    - Add project name and remove [LOG] or [ERROR] notation in log or error panel
    - Rename ``destruct package.xml`` command to ``destruct package.xml from server``
    - Rename ``retrieve package.xml`` command to ``retrieve package.xml from server``
    - Update ``to`` or ``from`` in context menu item name to ``To`` or ``From``
    - Update confirm request message for ``destruct files from server``

* New:
    - Add a new command ``Enable Development Mode`` to quickly enable visualforce page development mode
    - Add bootstrap3 completion document


Release 3.1.7 (2015-08-05)
++++++++++++++++++++++++++++++++++++
* Enhancement:
    - Add `with sharing` for `Utility Class` in template
    - When you want to view code coverage, if you didn't download code, you can't view code coverage and you will get the reminder message in the status bar
    - Before v33.0, tooling API doesn't support relationship query just like ``ApexClass.LastModifiedBy.Name``, when you save code to server, plugin will check your code has conflict with server and tell you ``who change the code at when?``, because relationship query is not supported, plugin will need to issue a query request to fetch the LastModifiedBy Name by the LastModifiedById, from this version, it will not necessary.
    - Add comments for some settings
    - Move metadata.json from ``metadata.sublime-settings`` to ``.config/metadata.json``, when you create new project, if the ``metadata.json`` is exist in the ``.config`` path, plugin will skip the describe process, however, if you want to refresh the cache, you can execute ``Metadata > Describe Metadata`` to refresh the ``metadata.json`` cache file

* Bug Fix:
    - After you select all test class, you can't deselect all when you run tests
    - Problem when ``diff with other server``, see detail in issue #61

* New Feature:
    - Add a new command named ``destruct_package_xml`` in the context menu, which is used for destructing members defined in ``package.xml`` from current server, so if you want to remove some components from production, you can get the package.xml by ``Metadata > Build Package.xml``, and then execute ``destruct_package_xml`` to remove them from production

* Update:
    - Update keymap of ``retrieve from this server`` from ``super+shift+r`` to ``alt+shift+r``, fix issue #68
    - Update keymap of ``deploy to this server`` from ``super+shift+s`` to ``alt+shift+s``


Release 3.1.6 (2015-07-29)
++++++++++++++++++++++++++++++++++++
* Bug fix:
    - If controller name is same with page name, there will have problem when view code coverage
    - Fix bug when file is loaded
    - Fix issue #62
    - Fix issue #63

* Enhancement:
    - Deliver enhancement #64
    - Deliver enhancement #65
    - Deliver enhancement #66


Release 3.1.5 (2015-07-27)
++++++++++++++++++++++++++++++++++++
* New Feature:
    - Add bootstrap3 support for html class completion
    - Add a new setting ``disable_bootstrap_completion`` to control bootstrap completion

* Update:
    - Remove ``Metadata > Describe Metadata`` menu item in the main menu

* Fix Bug:
    - Fix bug for running sync test for class with namespace or not
    - Fix bug for ``get_file_attributes`` method


Release 3.1.4 (2015-07-25)
++++++++++++++++++++++++++++++++++++
* Bug Fix:
    - Fix issue #23?
    - Fix issue #58
    - Fix issue #59

* Enhancement:
    - Add filters support for ``Build Package.xml`` command, which is used to filter members which contains the input filters
    - Add update feature for ``Build Package.xml`` command, which is used to add or remove members from exist package.xml
    - Add keymap for some frequently-used commands
    - Add visibility control for some CURD command on code file
    - Aura related features
    - Merge ``Deploy Lightning To Server`` command with ``Deploy File to Server`` command
    - Merge ``Retrieve Lightning To Server`` command with ``Retrieve File to Server`` command
    - Use file full name as key in ``component_metadata.sublime-settings``, originally, we use name as key, for example, originally, ``AccountController`` is key, now is ``AccountController.cls``
    - Change ``Diff With Server`` command to just visible when code file is ``classes, triggers, components or pages``

* New Feature:
    - New ``Run Sync Test`` command for replacing ``Run Test`` feature
    - Read code coverage information from local cache kept by ``Run Sync Test`` command
    - New ``Retrieve from This Server`` command in the context menu
    - New ``Diff With This Server`` command in the context menu
    - New ``View File Attributes`` command in the context menu

* Update:
    -  ``Quick Goto`` is switched to standard sublime build-in, I changed the mousemap to bind with the standard feature , with this feature, you can quickly view the symbols in sublime, for example, when you see a statement like this ``AccountUtil.populateField()``, you can put focus in the method name, hold down ``shift`` and triple-click your left mouse, sublime will open the ``AccountUtil`` class and put focus in the selected method


Release 3.1.3 (2015-07-18)
++++++++++++++++++++++++++++++++++++
* Fix issue #54
* Fix issue #56


Release 3.1.2 (2015-07-17)
++++++++++++++++++++++++++++++++++++
* Fix issue #55


Release 3.1.1 (2015-07-16)
++++++++++++++++++++++++++++++++++++
* Bug fix:
    - Fix a issue for ``save_to_server`` command when ``api_version`` is less than 29
    - Fix problem in ``Class Body - test data util body-sublime-snippet.sublime-snippet``

* Enhancement:
    - Enhancement for issue #53
    - Enhancement for issue #54
    - Support deploy and retrieve for metadataObject which is in folder
    - Add support for visualforce email template development
    - Add select all feature for ``toggle_metadata_objects`` command
    - Add ``Territory2`` to ``allowed_sobjects`` list

* Update:
    - Remove ``disable_visualforce_completion`` setting
    - Add four settings to disable part of completion in visualforce page, see more in ``docs/completion.md``


Release 3.1.0 (2015-07-09)
++++++++++++++++++++++++++++++++++++
* Enhancement:
    - Sometimes, the inner class name is same with standard class or sObject, if this inner class is matched, ignore the standard completion
    - Add Notation [EU] for external or unique field in field completion, ``E`` means External, ``U`` means Unique
    - Add a new setting named ``disable_visualforce_completion`` to control visualforce completion

* Bug Fix:
    - Fix issue #49
    - Fix issue #50
    - Catch exception for ``check retrieve status`` request when retrieve

* New
    - Add a new snippet ``Bracket - sobject parenthesis.sublime-snippet``, see ``/docs/snippets.md`` for more detail

* Update
    - Change default ``api_version`` from 33 to 34
    - Move document for ``execute anonymous`` from ``project.md`` to ``debug.md``


Release 3.0.9 (2015-07-01)
++++++++++++++++++++++++++++++++++++
* Bug Fix:
    - Fix bug for snippet ``SOQL - SELECT * FROM.sublime-snippet``
    - Fix bug for ``extract_to_here`` command

* Enhancement:
    - Don't need confirmation to reload project cache after choose metadata objects
    - In order to avoid timeout exception, increase max_retries from 5 to 10 for retrieve zipFile request


Release 3.0.8 (2015-06-28)
++++++++++++++++++++++++++++++++++++
* Bug Fix:
    - Fix bug when build package.xml for whole org

* Enhancement:
    - Display chosen sObject Name when input trigger name
    - Enhancement for #39, open a new view, set status bar and close the new view
    - Add success message for ``extract_to_here`` command
    - Update all snippets

* New:
    - Add a quick link to view all snippets, see it in plugin home page
    - Add command to access all snippets in ``Utilities`` of main menu


Release 3.0.7 (2015-06-26)
++++++++++++++++++++++++++++++++++++
* Bug Fix:
    - Fix issue #46
    - Fix bugs caused by ``describe_global`` change in the ``tooling.py``

* Enhancement
    - Merge pull request #45 by @reyesml(https://github.com/reyesml)

* New
    - Add a snippets: ``Page Variable - get and set in one line.sublime-snippet``
    - Add a snippets: ``Page Variable - get and set in multiply line.sublime-snippet``
    - Add a new command for building package.xml for whole org


Release 3.0.6 (2015-06-23)
++++++++++++++++++++++++++++++++++++
* Bug Fix:
    - Merge pull request #42 by @pgAdmin(https://github.com/pgAdmin)
    - Merge pull request #43 by @reyesml(https://github.com/reyesml), fixed issue #6
    - Fix bug for ``export_workbook`` feature


Release 3.0.5 (2015-06-15)
++++++++++++++++++++++++++++++++++++
* Bug Fix:
    - Custom component attributes completion bug when component file is not exist in the target path

* Enhancement:
    - Improve regular expression for SOQL fields completion


Release 3.0.4 (2015-06-15)
++++++++++++++++++++++++++++++++++++
* Bug Fix:
    - Fix bug for issue #41
    - Fix bug for ``delete_file_from_server`` keybinding for windows
    - Fix bug for ``auto_update_on_save`` feature in windows
    - Fix ``KeyError: '\n\n'`` for converting complex JSON to Apex

* Enhancement:
    - Improve the regular expression for SOQL fields completion
    - Improve the regular expression for Apex class method completion
    - Improve the regular expression for visualforce component attribute completion
    - Improve the visualforce tag name completion, add ``>`` for tag name automatically
    - As the original design, you need to input your JSON when you execute JSON related commands, since this version, you just need to open any JSON file or select valid JSON content
    - Add ``JSON/XML Tool`` into context menu, which is same with ``Utilities`` in main menu
    - Update content for some docs

* New Feature:
    - Add attribute completion for custom component
    - Add document for all code completion, you can see the link in the plugin home page


Release 3.0.3 (2015-06-11)
++++++++++++++++++++++++++++++++++++
* Bug Fix:
    - Fix duplicate save check bug caused by release 3.0.2
    - Fix fields completion bug for cross sObjects between tooling and non-tooling, for example ``User``, ``RecordType``

* Enhancement:
    - Add session expired message for ``describe_metadata``
    - Enhancement for ``refresh_file_from_server``

* Update
    - Update pop-up compile message for ``save_to_server`` command


Release 3.0.2 (2015-06-07)
++++++++++++++++++++++++++++++++++++
* Bug fix:
    - Fix NoneType exception in the console when open context menu, this is caused by release 3.0.1
    - Fix bug for ``Debug > Track All Debug Logs`` in the main menu

* Enhancement
    - Duplicate save_to_server check logic change: use file name with extension but not only file name, as the original design, if the controller name is same with page name, if you are saving page, you can't save the related controller at the same time
    - Add timeout for query of conflict checking when ``save_to_server``
    - Prevent duplicate save conflict check when ``save_to_server``, as the original design, if you latest saving is interrupted, when you save it again, plugin will delete the metadata container Id for the saving file, at this time, save conflict checking will be executed again.

* New:
    - Add sObject completion for ``tooling sObjects``, for example, ``Validation Rule``, ``WorkflowRule``, ``ValidationRule``, ``WorkflowFieldUpdate``, ``WorkflowOutboundMessage``, ``WorkflowAlert`` or ``WorkflowTask``
    - Add * support for ``export query to CSV`` or ``export tooling query to CSV``, if you use * in the query statement, plugin will get all fields of this object and set them as the column headers
    - Add export command for tooling query into the ``Data Loader`` in the main menu, you can use this command to export records for tooling objects
    - Add a new markdown document related to debug
    - Add a menu item for quick accessing document related to debug

* Update:
    - Update the menu item names and location in command palette and the ``Debug`` of main menu
    - Change the default key binding for ``Debug > Run Test`` in the main menu


Release 3.0.1 (2015-06-04)
++++++++++++++++++++++++++++++++++++
* Bug fix:
    - Fix bug #39
    - Fix bug #40
    - Fix bug for SOQL completion

* Enhancement:
    - Enhancement for boolean attribute completion of standard visualforce component
    - Set ``word_wrap`` setting of new view to false when describe sObject
    - Keep attributes of all metadataObjects to local ``component_metadata.sublime-settings``
    - Prevent potential issue caused by change of ``component_metadata.sublime-settings``

* Update:
    - Add output panel message for ``describe_metadata`` command
    - Disable document reference reload feature
    - Add a ``salesforce_reference.sublime-settings`` for ``Document > Open Document`` in the main menu

* New API for metadata:
    - Add a new ``read_metadata`` method for ``metadata.py``, which will be used for ``diff_with_server`` feature in the future


Release 3.0.0 (2015-05-26)
++++++++++++++++++++++++++++++++++++
* Bug fix:
    - Fix bug #38
    - Fix bug for SOQL fields completion
    - Fix bug for attributes completion for value of ``apex:includeScript``

* New
    - Add a new snippet named ``Page - field label.sublime-snippet``


Release 2.9.9 (2015-05-25)
++++++++++++++++++++++++++++++++++++
* Enhancement
    - SOQL fields completion, see demo at plugin home page

* New
    - Add two demos at home page
    

Release 2.9.8 (2015-05-24)
++++++++++++++++++++++++++++++++++++
* Update:
    - Update the plugin install message for package control

* Enhancement:
    - Add the missed attributes for some standard components since v29.0
    - Add attribute values for standard components if attribute value is picklist attribute

* New:
    - Add a new setting ``auto_update_on_save``, default value is false
    - If ``auto_update_on_save`` is set to true, when you update the code file, ``save_to_server`` will be executed automatically

* Note:
    - From this version on, I will not keep frequently release on this plugin, I will move on to build Haoide plugin for brackets


Release 2.9.7 (2015-05-22)
++++++++++++++++++++++++++++++++++++
* Bug Fix:
    - Fix issue #36
    - Fix bug for ``childXmlNames`` parsing and ``childXmlNames`` completion for package.xml
    - Fix bug for timeout exception message for ``query`` method in ``tooling.py``
    - Fix NoneType exception for automatic extension or controller creation if current view is not local file
    - Tag plugin fix a bug for that tag name contains colon, `see tag issue https://github.com/titoBouzout/Tag/issues/79`_

* Enhancement:
    - Enhancement for attribute completion in visualforce page, if attribute value is already exist, it will not insert ``=""`` or ``="{!}"`` again
    - Enhancement for ``standardController`` sObject name completion in visualforce page, it will just work when attribute is ``standardController``
    - Add custom class completion for ``extension`` and ``controller`` attribute in visualforce page
    - Add values completion for some attributes of standard components which type should be picklist, for example, "apiVersion", "layout", "event" or "target" for link and so on, in this time I just updated to apex:composition, I will check the remaining standard component
    - Add two missed standard component into ``vf.py``, "apex:component" and "apex:componentBody"
    - Add custom page completion for these four attributes: "page", "template", "pageName", "finishLocation", for example, if you input <apex:include, pageName="", you can get custom page completion in the "" for pageName attribute

* New:
    - Add commands in command palette for ``reload_project_cache`` and ``build_package_xml``

* Update:
    - Update snippet ``Controller - add message in vf.sublime-snippet``


Release 2.9.6 (2015-05-20)
++++++++++++++++++++++++++++++++++++
* Bug Fix:
    - Fix issue #33
    - Fix issue #35

* Enhancement:
    - Add required check for XML utilities
    - Add required check for JSON utilities
    - Separate ``login`` feature from ``switch_project``
    - Add callback for ``switch_project`` for operations need switching, such as, ``deploy to server``, ``diff with server`` or ``retrieve from server``
    - Combine ``retrieve from server`` and ``retrieve from other server`` only one command, just like ``deploy to server``, you can switch project before retrieving
    - When ``reload_project_cache``, just if you selected at least one metadata object, reload will start, otherwise, do nothing

* New Feature
    - Add a new ``reload session cache`` command in ``Cache`` of the main menu for forced login

* Update
    - Because metadata.json of every project is stable, so save it into ``metadata.sublime-settings`` but not ``.config/metdata.json`` again
    - Remove ``check_workspace_available`` for export feature, because this check is useless


Release 2.9.5 (2015-05-16)
++++++++++++++++++++++++++++++++++++
* Enhancement:
    - Add callback for ``toggle_metadata_objects`` if ``.config/metadata.json`` is not exist
    - Move ``export_query_to_csv`` command from context menu to ``Data Loader`` in the main menu, add check logic for input soql and allow to try again.
    - Add snippets, ``Class Body - Trigger Template Bind.sublime-snippet``, ``Class Body - Trigger Template.sublime-snippet`` and ``Class Body - Trigger Template Implement.sublime-snippet``
    - Update content of snippet ``Class Body - Roll up summary utility.sublime-snippet`` to that written by me, see `more detail <https://gist.github.com/xjsender/1e40c274c07171531f0f>`_

* Update:
    - Rename ``View Release Notes`` command to ``Release Notes``
    - Rename ``json_pretty`` command to ``json_format``
    - Rename ``convert_xml_to_json`` command to ``xml_to_json``
    - Move ``xml_to_json`` from context menu to ``Utilites`` in the main menu
    - Add access to ``toggle_metadata_objects`` for both ``Settings`` and ``Metadata`` in the main menu
    - Upgrade build-in ``xmltodict`` module to ``0.9.2``
    - Update document for the change in this release

* New Feature:
    - New commands for ``HaoIDE > Utilities`` of the main menu:
        - Add a new command ``haoide_help`` to view related document
        - Add a new command ``json_to_xml`` to convert xml back to json, see issue #32
        - Add a new command ``xml_format`` to format selected xml content or whole file content, see issue #32


Release 2.9.4 (2015-05-13)
++++++++++++++++++++++++++++++++++++
* Bug Fix:
    - If there is only one member, just remove the type and the related member when ``build package xml``
    - When execute ``query_to_csv`` command and field value contains ``"`` or ``,``

* Enhancement:
    - Show the error message when list package for metadata objects if have
    - Support quick clear for symbol_table and sobject cache
    - Automatic ``{!}`` enhancement for vf tag just if type is "Object" or "ApexPages.Action"
    - Update type of some visualforce standard components from ``Object`` to ``String``
    - Change the item format in the quick panel when ``build package xml``
    - Add ``EmailTemplate`` to ``allowed_sobjects`` setting
    - Allow user to choose reloading specified ``metadata_object`` cache when execute reload_project_cache command
    - When operation is depends on login session, so login firstly and callback with this operation

* Update:
    - Rollback the delivered function for issue #15
    - Optimize on ``metadata.py``


Release 2.9.3 (2015-05-11)
++++++++++++++++++++++++++++++++++++
* Enhancement:
    - Package.xml completion read cache from ``.config/package.json``, no longer read cache from project file
    - Sort for items in quick panel of package.xml building
    - Add alert message for package.xml completion

* Bug Fix:
    - Add the folder into member when list_package for DocumentFolder, EmailFolder, ReportFolder and DashboardFolder
    - No four spaces in the quick panel of package.xml building for windows


Release 2.9.2 (2015-05-10)
++++++++++++++++++++++++++++++++++++
* Bug Fix:
    - Fix bug for ``combine_soql`` which is invoked by ``Generate SOQL`` and ``Bulk Query``
    - Fix bug for ``export_profile`` command
    - Fix bug for completion of building ``package.xml``
    - Fix bug for ``export_validation_rules`` command

* New Feature:
    - Deprecated ``metadataObjects`` since this release, which is replaced by ``<project>/.config/metadata.json``
    - Add ``describe_metadata`` command, ``<project>/.config/metadata.json`` will be generated by this command
    - Add ``reload_project_cache`` command, ``<project>/.config/package.json`` will be generated by this command
    - Add ``build_package_xml`` command, see `more <https://github.com/xjsender/SublimeApexScreenshot>`_
    - Add key bindings for ``build_package_xml`` command

* Enhancement:
    - Move package related logic from ``main.py`` to the new ``package.py``
    - Add thread progress for ``track_debug_log``, ``fetch_debug_log`` and ``track_all_debug_logs``
    - `create_new_project`` start supporting callback
    - Add metadata object for input description for ``create_new_component`` module
    - Add list_package support for ``CustomObject`` retrieve
    - Add availability check for ``.config/metadata.json`` for all related commands
    - Add ``api_version`` message into the sidebar message
    - Update ``api_version`` from ``32`` to ``33``
    - Update ``Metadata Migration`` to ``Metadata`` in the main menu
    - Update ``generate_soql`` logic to include ``Id`` field if no available matched fields
    - Update description for default settings
    - Update README.md


Release 2.9.1 (2015-05-05)
++++++++++++++++++++++++++++++++++++
* Fix bug for ``switch_project``, see issue #24
* Enhancement for speeding up ``Save To Server`` operation
* Rename ``save_component`` command to ``save_to_server``
* Rename ``delete_component`` command to ``delete_file_from_server``
* Simplify ``delete_file_from_server`` and ``refresh_file_from_server``
* Add two new value issue_url and history_url into package info
* Update ``report_issue`` and ``view_release_notes`` command to read url from package info


Release 2.9.0 (2015-05-03)
++++++++++++++++++++++++++++++++++++
* Fix bug for messy code in debug log detail
* Enhancement for not refreshing sidebar when ``retrieve_files_from_other_server``
* Enhancement for adding folder name to retrieve request when ``list_package`` for folders
* Enhancement for package.xml completion for folder name of Document, EmailTemplate, Dashboard and Report
* Enhancement for package.xml completion for AuraDefinitionBundle
* Enhancement for sobject completion, if there are two matched statements, ``insert prd`` and ``Product2 prd``, plugin will choose the second one as matched
* Enhancement for ``toggle_metadata_objects``, you can toggle metadata objects continually util you press ``ESC`` to exit
* Enhancement for ``generate_sobject_soql``, you can choose whether generate sobject SOQL of ``Custom``, ``Updateable`` or ``Createable``
* Update workspace of default build-in project from ``C:/ForcedotcomWorkspace`` to empty
* Update name of default build-in project from ``pro-test`` to ``pro-sublime``
* Update for ``toggle_metadata_objects``, after subscribe a new metadata object, don't refresh its folder again, just after you finish all toggle, you will need to confirm whether use refresh all subscribed metadata together
* Add ``toggle_metadata_objects`` document in ``docs/utilities.md``
* Remove four deprecated settings, ``keep_config_history``, ``output_session_info``, ``delay_seconds_for_hidden_output_panel_when_failed`` and ``get_static_resource_body``


Release 2.8.9 (2015-04-28)
++++++++++++++++++++++++++++++++++++
* Fix urgent bug for issue #22
* Enhancement for speeding up ``Save To Server`` operation
* Enhancement for supporting ``list_package`` when execute retrieve operation
* Enhancement for package.xml completion for Document, EmailTemplate, Dashboard and Report
* Enhancement for ``add_project_to_workspace`` just if login succeed
* Add a new ``link_project_with_sublime_project`` setting to control linking, default is false
* Update documents regarding to issue #18


Release 2.8.8 (2015-04-26)
++++++++++++++++++++++++++++++++++++
* Fix bug: If user don't have `Author Apex` privilege, plugin will give wrong information
* Fix bug: Show alert message if no available package.xml to combine
* Enhancement: Issue 15 about linking ``sublime-project`` with plugin project, deliver Windows solution but keep unchanged for OSX
* Enhancement: Add scope control for ``JSON to Apex``
* Enhancement: Set ``word_wrap`` of ``Test Run`` result to false
* Enhancement: Simplify retrieve status check for API version 31 and later, check more detail at `here <https://www.salesforce.com/us/developer/docs/api_meta/Content/meta_retrieve.htm>`_
* Update documents


Release 2.8.7 (2015-04-22)
++++++++++++++++++++++++++++++++++++
* Fix plugin loading NoneType issue
* Combine ``retrieve_package_file`` and ``retrieve_package_xml`` command to only ``retrieve_package_xml``
* Allow user to input extractTo path, enhancement for issue #19
* Add a new command ``combine_package_xml`` to combine all package.xml in many folders, see ``Salesforce Utilites`` quick link
* Update Documents


Release 2.8.6 (2015-04-20)
++++++++++++++++++++++++++++++++++++
* Optimization for parsing project name by path or file
* Change the default workspace of plugin level to empty
* Change the workspace to optional, if workspace of plugin level and project level are both empty, plugin will save the project to ``<packages_path>/User/HaoIDE``, 
* Change the name of ``execute_soql`` command to ``execute_query``
* If there has network connection issue, just display ``Network connection timeout`` but no more detail again
* Add a new command for export query to csv, you should be aware, query statement contains parent-to-child statement will not be enabled for this command
* Add a new ``auto_switch_project_on_file_activated`` setting to control project switching when file of non-default project is open, this feature is disabled by default
* Add a new ``reveal_file_in_sidebar_on_file_activated`` setting to control sidebar file revealing when the file is open, this feature is disabled by default


Release 2.8.5 (2015-04-10)
++++++++++++++++++++++++++++++++++++
* Biggest optimization for variable completion:
    - Exclude comment statement
    - Choose the nearest matched one
* Add a new ``remove_comments`` command in the ``Utilities``
* Allow ``extract_to_here`` command to support all zip resources


Release 2.8.4 (2015-04-09)
++++++++++++++++++++++++++++++++++++
* Add error popup display for latest version of sublime
* Add a new settings ``disable_html_completion`` to disable html completion
* Set default value of ``disable_html_completion`` as true because of conflict with sublime
* Optimize component attribute completion to support current line and next line
* Fix Bug: Wrong completion for Picklist2 when ``if (acc.Picklist1 == 'abc' && acc.Picklist2 == 'bcd')``
* Fix Bug: Plugin found the wrong variable type in the commented code for variable completion
* Ignore exception when keep package.xml for every deploy action
* Rename Heroku to Haoku in the ``Main Menu > Utilities``
* Remove useless ``.travis.yml``
* Remove ugly code for check whether statement is comment for code
* Update ``execute_soql`` command to execute query in heroku


Release 2.8.3 (2015-04-02)
++++++++++++++++++++++++++++++++++++
* If no CRUD privilege on profile object, just leave blank in the output csv
* Add field FLS export feature, it's a wonderful feature for document


Release 2.8.2 (2015-03-28)
++++++++++++++++++++++++++++++++++++
* Fix package.xml completion bug if file name contains multiple dot
* Fix package.xml completion bug if there have extracted zip resource
* Pull request for #14
* Spell problem of `Toggle Metadata Settings`
* Add entry point for ``Haoku`` in the ``Utilities`` of main menu
* Remove ``AuraDefinitionBundle`` from default subscribed Metadata settings


Release 2.8.1 (2015-03-05)
++++++++++++++++++++++++++++++++++++
* Fix issue #6
* Enhancement for issue #13


Release 2.8.0 (2015-02-11)
++++++++++++++++++++++++++++++++++++
* Fix issue #11, #12
* Add two commands ``Retrieve All`` and ``Retrieve sObject and Workflow`` in the command palette


Release 2.7.9 (2015-02-06)
++++++++++++++++++++++++++++++++++++
* Fix issue #4
* Fix issue #7
* Enhancement for ``diff_with_server``, allow diff compare with different project
* Upgrade ``requests`` to v2.5.1 and disable the InsecureRequestWarning
* Display line number before column number when ``save_component`` failed


Release 2.7.8 (2015-02-02)
++++++++++++++++++++++++++++++++++++
* Rename ``refresh_component`` command to ``refresh_file_from_server``
* Rename ``refresh_selected_components`` command to ``refresh_files_from_server``
* Rename ``delete_selected_components`` command to ``delete_files_from_server``
* Add a new command for ``retrieve file from other server`` for retrieve file from different project.
* Add a settings ``switch_back_after_migration`` to control whether switch back to original project after ``deploy to server``, ``deploy package to server``, ``deploy lightning to server`` or ``retrieve file from other server``, issue haoide:#3
* Fix issue #5
* Move ``pretty_json`` command from context menu to ``HaoIDE > Utilities > JSON Pretty`` in the main menu
* Update README.MD


Release 2.7.7 (2015-01-22)
++++++++++++++++++++++++++++++++++++
* Fix bug for ``Package.xml Completion``
* Enhancement: display error column in XML if deploy failed
* Enhancement for ``json_to_apex``
* Enhancement for ``describe_sobject``
* Add a new ``json_serialization`` command to serialize JSON to string
* Add a new ``panel`` menu item in Main Menu
* Rearrange Utilities menu item in Main Menu
* Update ``haoide`` to ``HaoIDE``


Release 2.7.6 (2015-01-20)
++++++++++++++++++++++++++++++++++++
* Enhancement for ``create_trace_flag`` command
* Add a enabled check logic for ``export profiles`` command
* Add a new ``haoide > Utilities > Convert JSON to Apex`` command for converting JSON to Apex
* Add commands for ``convert_json_to_apex`` in command palette
* Update README.MD about the `Convert JSON to Apex <https://github.com/xjsender/haoide#convert-json-to-apex>`_


Release 2.7.5 (2015-01-18)
++++++++++++++++++++++++++++++++++++
* Fix bug: messy code when view debug log detail in sublime
* Fix bug: timeout exception is not caught when save component
* Enhancement for completions
* Enhancement for ``export profile`` feature
* Add feature for export of ``userPermission`` and ``tabVisibility``
* Update README.MD


Release 2.7.4 (2015-01-16)
++++++++++++++++++++++++++++++++++++
* Fix bug for issue #75
* Update ``Chanel`` to ``Channel`` in the plugin copyright information
* Update license information
* Remove ``InstalledPackage`` from ``metadataObjects`` settings
* No longer check save conflict when compile code
* Add commands for ``export_profile`` in command palette
* Update default keymap for ``open log panel``, ``open error panel`` and ``open diff panel`` in the ``Utilities`` menu item
* Enhancement for login module, decrease the timeout seconds and repeat login until repeat times exceed 12 times


Release 2.7.3 (2015-01-14)
++++++++++++++++++++++++++++++++++++
* Fix bug for ``extract here`` command
* Fix bug for ``bulk api`` caused by release 2.7.2
* Fix long-term bug for inProgress message of deployment
* Enhancement for ``list debug log``, for example, sort logs order by StartTime ASC, remove the useless "\n"
* Add missed standard objects for ``CustomObject`` when retrieve metadata
* Add new command for exporting profile object security settings, it's a very useful feature
* Add ``Translations`` to metadataObjects settings
* Update snippet description for ``Debug - debug json.sublime-snippet``


Release 2.7.2 (2015-01-12)
++++++++++++++++++++++++++++++++++++
* Fix bug for issue #74
* Fix bug for ``cancel_deployment``
* Fix bug for ``reload symbol table`` when symbol_table is None
* Fix bug for ``execute anonymous`` when anonymous code contains non-english words since release 2.7.0
* Enhancement for message tracking in output panel
* Enhancement for settings check, if settings is valid, just display it in output panel
* Update snippet ``Debug - debug variable.sublime-snippet``
* Add snippet ``Debug - debug json.sublime-snippet``


Release 2.7.1 (2015-01-09)
++++++++++++++++++++++++++++++++++++
* Enhancement for ``standardController completion`` in ``<apex:page standardController=""``
* Enhancement for ``{!acc.} completion`` in visualforce page
* Enhancement for ``diff module``
* Fix some minor bugs


Release 2.7.0 (2015-01-03)
++++++++++++++++++++++++++++++++++++
* Rearrange the menu items of ``Login To`` in alphabetical order
* New format: ``LastName + FirstName => Email`` for ``Debug Log User List``
* Milestone change for soap body request
* Enhancement for quick extension and quick controller
* Fix Bug for Package Completion
* Fix Bug for ``opps`` completions in ``getAccountList(List<Opportunity> opps)``
* Fix Bug for ``allowed_sobjects``, change ``Assert`` to ``Asset``
* Fix Bug for ``reload_sobject_cache``
* Fix Bug for ``bulkapi``
* Change default value of ``last_n_logs`` from ``10`` to ``20``


Release 2.6.0 (2014-12-20)
++++++++++++++++++++++++++++++++++++
* Enhancement for ``refresh_folder``
* Enhancement for ``retrieve_all`` and ``retrieve_sobjects_and_workflows``
* Move export csv files to ``.export`` folder, for example, CustomFields, ValidationRules, Workflows and Workbooks, etc.


Release 2.5.9 (2014-12-17)
++++++++++++++++++++++++++++++++++++
* Completion enhancement for building package.xml
* Fix duplicate MetadataContainerId for issue #69
* `Build Package.xml Demo <https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/BuildPackageXML.gif>`_


Release 2.5.8 (2014-12-15)
++++++++++++++++++++++++++++++++++++
* Add all ``sharingRules`` metadata types to default components setting
* Rename ``.package`` to ``.deploy`` for ``deploy to server`` execution
* Remove ``subscribe_component`` and ``unsubscribe_component`` commands
* Add a new ``toggle_commands`` command to replace above two commands
* After a new component is subscribed, refresh the new folder from server
* Rename "ok" in confirm dialog to related message
* Add workspace check when create new project
* Update README.MD


Release 2.5.7 (2014-12-14)
++++++++++++++++++++++++++++++++++++
* Fix Bug for creating extension or controller after input # in visualforce page
* Adjust the location of ``Cache`` menu item
* Add a new command for ``retrieve package.xml`` in sidebar menu
* Add a new command for ``create package.xml`` in sidebar menu
* Add a new command for ``subscribe component`` in ``settings`` of main menu
* Add a new command for ``unsubscribe component`` in ``settings`` of main menu
* Add quick command for ``subscribe component`` in quick command palette
* Add quick command for ``unsubscribe component`` in quick command palette
* Remove ``retrieve_package_xml`` command from ``Metadata Migration`` of main menu
* Rename ``soap_bodies`` to ``soap``
* Update visibility for ``Update User Language``


Release 2.5.6 (2014-12-13)
++++++++++++++++++++++++++++++++++++
* Fix Bug for issue #65
* Fix Bug for issue #66
* Enhancement for issue #48, after deployed, the `package.xml` is saved to `.package` in workspace
* Before files are deployed to server, save them to local
* When you deploy any lightning element, just deploy the whole lightning component
* Convert StartTime of debug log to local time by timezone module


Release 2.5.5 (2014-12-09)
++++++++++++++++++++++++++++++++++++
* Fix Bug for creating Lightning Component Element
* When deploy failed due to lower code coverage, display the coverage warning message
* When new component is created, create the meta.xml file for it
* Hide ``Retrieve Lightning from Server`` command when chosen folder is not aura folder
* Hide ``Destruct Lightning from Server`` command when chosen folder is not aura folder
* Hide ``Extract to Here`` command if file extension is not `zip` or `resource`
* Update the Documentation


Release 2.5.4 (2014-12-07)
++++++++++++++++++++++++++++++++++++
* Add `dateutil` module for supporting timezone converting
* Fix Bug for `track debug log`
* Trim the space for `REST URI` automatically
* Remove `lib` from `Packages` in `.gitignore` file
* Support project level workspace for issue #63, see more detail at `workspace <https://github.com/xjsender/SublimeApex#workspace>`_


Release 2.5.3 (2014-12-05)
++++++++++++++++++++++++++++++++++++
* Adjust the context menu from most bottom to center
* Adjust the sidebar menu from most bottom to center
* Fix Bug for issue #62: 'module' object has no attribute 'populate_classes'
* Fix Bug for issue #61: KeyError: 'name' in `get_component_completion`
* Fix Bug for issue #60: Error with 'Update Project'
* Add lightning component description for `Lightning Component` development


Release 2.5.2 (2014-11-27)
++++++++++++++++++++++++++++++++++++
* After new lightning component is created, deploy it to server
* Add a new command for ``pretty json`` in the context menu
* hide the status message in progress bar when track self debug log after save succeed


Release 2.5.1 (2014-11-26)
++++++++++++++++++++++++++++++++++++
* Fix Bug: NoneType Exception when destruct files from server
* Fix Bug: when saving component, the active view is not file
* Add a new settings ``track_log_after_saved`` to control whether track log after save succeed


Release 2.5.0 (2014-11-26)
++++++++++++++++++++++++++++++++++++
* Fix Bug: when delete component, if there is a open view which is not bind to file, it will throw TypeError: argument of type 'NoneType' is not iterable, and then, file is deleted from server but local file is not removed
* Fix Bug: After folder is refreshed or project is updated, update the component cache
* Add `Lightning Component` document reference
* Add `Lightning Component` component tags to completions
* Add `Lightning Component` to `components` settings and set it as default subscribed component
* Add `Lightning Component` update feature
* Add `Lightning Component` components update feature
* Add `Lightning Component` component create feature
* Add `Lightning Component` component destruct feature
* Change default ``api_version`` from 31 to 32
* Remove ``Open Coverage Panel`` menu item in the main menu
* Add ``duration`` column for debug logs and rearrange it's columns order
* Add new document reference for ``Analytic Api``, ``Analytics Cloud Dashboard JSON``, ``Security Implementation`` 
  and ``Lightning Component``
* Add new command for viewing release notes
* Rename ``Extract Static Resource`` command to ``Extract To Here``, which command can be used to extract all zip source file but not only static resource for Salesforce
* Add ``settings`` to ``components`` settings
* If project is not created, all ``export`` feature and ``new component`` feature are not enabled


Release 2.4.0 (2014-11-18)
++++++++++++++++++++++++++++++++++++
* Fix issue #55
* Fix issue: non-english words are encoded to Unicode in result of ``Rest Test``
* Fix issue: when read local cache of record type, ``global name 'users' is not defined`` exception
* Rollback feature of ``view_code_coverage``, see issue #56
* Deprecate ``keep_config_history`` setting
* Update the description of ``keep_local_change_history`` setting
* When save operation has conflict and we cancel it, compare the local with server automatically


Release 2.3.0 (2014-11-14)
++++++++++++++++++++++++++++++++++++
* Use local ``<workspace>/.config/session.json`` to reuse session but not globals() again
* Use local ``<workspace>/.config/recordtype.json`` to ``record type`` but not globals() again
* Use local ``<workspace>/.config/users.json`` to ``users`` but not globals() again
* If ``execute_anonymous`` compiled succeed, use new view to display result, else, use output panel to display result
* Use frontdoor method to login to SFDC
* Add new document reference for ``Analytic Api``
* Display session expired message in the output panel


Release 2.2.0 (2014-11-12)
++++++++++++++++++++++++++++++++++++
Fix Issue:

* Fix issue: TypeError: string indices must be integers when refreshed folder is empty
* Fix issue: In windows, change of folder or file in sidebar is not reflect in real time
* Fix issue: Sometimes, file is not remove from local after ``destruct file from server``
* Fix issue: format problem of local ``.config`` info
* Fix issue: #52

Enhancement:

* Add time stamp for new view name of ``rest test``
* Show logs of ``fetch debug logs`` and ``execute_anonymous`` in the output panel but not new view
* Change default value of ``folder_exclude_patterns`` and ``file_exclude_patterns`` settings

New Feature:

* Add new command for ``fetch self debug log`` in the main menu and command palette


Release 2.1.0 (2014-11-10)
++++++++++++++++++++++++++++++++++++
+ Fix Bug: ``IndexError: list index out of range`` caused by release 2.0.0
+ Fix Bug for test class judgment: test class is that starts with `test` or ends with `test`
+ Add a new apex.py module, move execute_anonymous method from metadata.py to apex.py
+ Add a new command for ``diff with server`` in the context menu
+ Optimization on ``view_code_coverage`` feature
+ Add a new command ``Utilities > Open Coverage Panel`` in the main menu to open coverage panel
+ Rename ``Open Output Panel`` command to ``Open Log Panel`` and move it from ``Debug`` to ``Utilities`` in the main menu
+ Temporarily remove the ``Run All Test`` feature from ``Debug`` in the main menu


Release 2.0.0 (2014-11-08)
++++++++++++++++++++++++++++++++++++
+ Fix minor bug for ``Duplicate Save Execution of Same Component``
+ Remove useless message from ``message.py``
+ Add a space between parameters for completion of standard apex class 
+ Rename ``Describe`` menu item in the main menu to ``Utilities``
+ Add a new command for ``Convert 15 Id to 18 Id``
+ Add a new command for ``Track Self Debug Log``
+ Add new feature for updating ZIP Static Resource, see demo ``https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/UpdateStaticResource.gif``
+ Add commands for ``Convert 15 Id to 18 Id`` and ``track self debug log`` in the command palette
+ Add ``StaticResource`` to default subscribed components
+ Update README.MD


Release 1.9.0 (2014-11-04)
++++++++++++++++++++++++++++++++++++
+ Fix issue #50
+ Fix minor issue for ``delete_component``
+ Fix potential issue for retrieve and deploy
+ Add ``Destruct Files From Server`` command in the sidebar menu for deleting files from sandbox or production
+ Add ``Destruct From Server`` command in the context menu for deleting file from sandbox or production
+ Add new command ``cancel_deployment`` for quickly canceling deployment of specified
+ Add mousemap for canceling deployment: Put the focus in the task Id, and then press alt and click Left Mouse for triple will cancel deployment of specified task Id


Release 1.8.0 (2014-11-03)
++++++++++++++++++++++++++++++++++++
+ In order to prevent UI freeze, use thread to extract encoded zipFile to path
+ Solution for issue #49, add a new settings ``maximum_concurrent_connections`` to control concurrent connections
+ In order to prevent UI freeze, set default value of ``maximum_concurrent_connections`` to ``30``


Release 1.7.0 (2014-10-31)
++++++++++++++++++++++++++++++++++++
+ Fix Bug: If just compile component but not save, no need to keep history
+ Fix Bug: SOQL Field Completion problem if there is more than one character between from and sObject
+ Fix Bug: Replace all `LIST` to `List`
+ Remove ``Settings – Completions`` and ``Settings – Apex Template`` from main menu


Release 1.6.0 (2014-10-25)
++++++++++++++++++++++++++++++++++++
+ Fix Bug: issue #44 caused by release 1.5.0
+ Fix Bug: display ExpatError when retrieve package
+ Fix Bug: display json parse error message when execute rest test
+ Stop to hide output panel after retrieve is finished
+ show status message 'Not valid SFDC component' if current file is not valid SFDC component
+ Deprecate the delay_seconds_for_hidden_output_panel_when_failed settings
+ Stop to remove the error line highlight after ``save to server``, just remove it in the next save action
+ After save succeed, remove the highlight from view
+ Support error line highlight for visualforce page just if error line > 2
+ Add ``OpenCTI Api`` document to document reference


Release 1.5.0 (2014-10-21)
++++++++++++++++++++++++++++++++++++
+ Fix Bug for package import error in ``bulk api``
+ Add more detailed action summary for ``save component``, issue #45, issue #46
+ Add description for ``quick controller`` in README.MD


Release 1.4.0 (2014-10-18)
++++++++++++++++++++++++++++++++++++
+ Fix bug for completion: No completions for ``strMap`` if there has ``// Populate Map\nMap<String, String> strMap = new Map<String, String>();``
+ Fix Bug: ``deploy open files to server``
+ Add a new command for ``preview_page`` in the command palette
+ Input ``#`` after controller or extension name in the visualforce page, plugin will automatically create it for you
+ Remove ``static resource`` from default subscribed components


Release 1.3.0 (2014-10-14)
++++++++++++++++++++++++++++++++++++
+ Fix Minor bug for standard class completion: duplicate class in different namespace, for example, Communities, TimeZone, UnsupportedOperationException, Test, QueryException, Action
+ Fix Critical bug: non code file can't be retrieve from server, now, objects, reports and others can be retrieve from server
+ Fix Critical bug: Deploy exception after session cache is expired


Release 1.2.0 (2014-10-11)
++++++++++++++++++++++++++++++++++++
+ ``get_static_resource_body`` settings is deprecated
+ Change default ``api_version`` from ``30`` to ``31``
+ Add a new command ``deploy open files to server`` in the main menu, which is used to deploy open files in the sublime to target server
+ Add command for ``deploy open files to server`` in the Command Palette
+ Add ``static resource`` to default subscribed components
+ Fix Bug for Windows: After ``retrieve all`` is finished, invoke the ``refresh_folder_list`` standard function to display the new folders generated by ``retrieve all``
+ Fix Bug: ``Save to Server`` command (Use Tooling Api) can be only used on ``classes``, ``components``, ``pages`` and ``triggers`` but not other components, however, we can use ``Deploy to Server`` command (Use Metadata Api) to save all components


Release 1.1.0 (2014-10-09)
++++++++++++++++++++++++++++++++++++
+ Fix Bug for Windows: After ``export`` is finished, refresh the project folders to ensure the new folder is shown in the sidebar
+ Fix Bug: display deploy failed message if deploy is failed.
+ Fix Bug: symbol table is null when iterate symbol table
+ Update README.MD


Release 1.0.9 (2014-10-04)
++++++++++++++++++++++++++++++++++++
+ Fix Bug: After open a new view, open context menu, it will throw NoneType exception


Release 1.0.8 (2014-10-02)
++++++++++++++++++++++++++++++++++++
+ Fix issue at ``https://success.salesforce.com/answers?id=90630000000gxvwAAA``


Release 1.0.7 (2014-09-30)
++++++++++++++++++++++++++++++++++++
+ Fix Minor Bug for windows: After ``.config`` is generated, invoke the sublime command: ``refresh_folder_list``
+ Enhancement for checking whether current project is active project
+ Fix Critical Bug: If session is expired, we want to refresh the folder or update project, the console will always stop at  the step of ``[sf:retrieve] Start request for a retrieve...``
+ Fix issue #42, stop to remove folder when refresh folder or update project but just override, Notice: if you delete some file in the server, after ``update project`` and ``refresh folder``, these files will not deleted in the sublime, so, I suggest you should delete code in the sublime but not in the server


Release 1.0.6 (2014-09-28)
++++++++++++++++++++++++++++++++++++
+ Fix Minor Bug: After ``retrieve_package_file`` is succeed, hide the output panel
+ Fix Minor Bug: If current project is not ``active project``, disable the ``Retrieve Files From Server`` functionality
+ Fix Minor Bug: If current project is not ``active project``, disable the ``Retrieve File From Server`` functionality
+ Fix Minor Bug: If current project is not ``active project``, disable the ``Run Test Class`` functionality


Release 1.0.5 (2014-09-27)
++++++++++++++++++++++++++++++++++++
+ Fix bug: Exception when ``new project`` in a new org
+ Fix bug: If there is no any trigger, after ``new project``, the folder of ``trigger`` is not created.
+ Fix bug: ``subscribed_meta_folders`` and ``meta_folders`` in settings are not correct


Release 1.0.4 (2014-09-25)
++++++++++++++++++++++++++++++++++++
+ Fix urgent issue #40
+ Remove the useless soap related codes, for example, ``retrieve_apex_code_body``, ``retrieve_static_resource_body`` and so on
+ Fix minor bug: Don't allow to refresh or delete ``*-meta.xml`` file
+ Fix bug: ``allowed_packages`` is not working
+ Fix bug: mass refresh multiply folders
+ Fix minor bug: deploy failed message in the output panel
+ Add a new sidebar command ``Retrieve Files From Server``
+ Add a new context command ``Retrieve File From Server``
+ If ``allowed_packages`` is not empty, all packages are extracted to ``packages`` path,
    Project
        > .config
        > src
        > packages
            > package 1
            > package 2


Release 1.0.3 (2014-09-24)
++++++++++++++++++++++++++++++++++++
+ After ``Update Project`` is finished, remove the original ``src`` tree and then extract the zipFile to ``src``
+ After ``Refresh Folder`` is finished, remove the original folders and then extract the zipFile to specified folders
+ Fix urgent bug: if no project in sidebar and sidebar is hidden, after ``new project`` or ``update project``, the sidebar is not open automatically.


Release 1.0.2 (2014-09-23)
++++++++++++++++++++++++++++++++++++
+ Update the default value of ``checkOnly`` in ``deploy_options`` settings from ``true`` to ``false``
+ Fix Urgent bug: If one class is created in the server, after ``refresh folder``, cache of this folder will override all components
+ Remove some useless ``print`` statement
+ Fix minor bug: After code is saved, duplicate extension is displayed in the console
+ Add two settings ``folder_exclude_patterns`` and ``files_exclude_patterns`` to hide everything you want to hide in the sidebar
+ Update the ``add project to workspace`` logic to compatible with the above two settings
+ Add a new command ``Update Project Patterns`` in the main menu, see [Pattern Demo](https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/ProjectPattern.gif)


Release 1.0.1 (2014-09-22)
++++++++++++++++++++++++++++++++++++
+ Add ``LogLength`` column to result of ``fetch debug logs``
+ Update default value of ``display_field_name_and_label`` setting from ``false`` to ``true``
+ Remove the ``\n`` from success message in ``document.py``
+ Add description for ``save multiple components`` feature in the README.MD
+ Change output directory of ``retrieve package.xml`` from current directory to ``[ProjectName]-201409221812``
+ Add ``messages`` notes


Release 1.0.0 (2014-09-21)
++++++++++++++++++++++++++++++++++++
+ Add a new command ``Deploy To Server`` in the context menu
+ Fix bug for ``retrieve`` when session is expired
+ Fix bug for ``New ApexClass``, ``New ApexTrigger``, ``New ApexComponent`` and ``New ApexPage``
+ Fix bug ``TypeError: is_visible() missing 1 required positional argument: 'dirs'`` when open ``Command Palette``
+ Fix bug: If there is no any trigger or class, we want to create the first one, there has exception
+ Fix bug: ``Package.xml`` was overridden by ``refresh folder``


Release 0.9.9 (2014-09-20)
++++++++++++++++++++++++++++++++++++
+ Try to fix bug for ``new release messages display`` or who can tell me how to display ``release message``
+ Fix bug for ``quick go to component``


Release 0.9.8 (2014-09-20)
++++++++++++++++++++++++++++++++++++
+ Support multiply folder refresh
+ Add standard sObjects to CustomObject Package Members when create new project if CustomObject is subscribed
+ Update default subscribed components
+ Add a new command ``Deploy Files to Server``
+ Fix bug: Display debugLog info after deploy is finished
+ Upsert demo in README.MD
+ Display the new release message after new released upgrade is finished


Release 0.9.7 (2014-09-19)
++++++++++++++++++++++++++++++++++++
+ Milestone for Metadata Api Migration from ``Tooling Api`` for non-code meta
+ remove some time stamp for deploy
+ Functionality check for ``convert xml to json``
+ Optimize the zip utility for ``extract`` zip file or ``compress`` folder
+ Remove ``hidden_console_on_modify`` settings
+ Fix bug: the output console message for ``compile``
+ Use ``metadata api`` to new project
+ Use ``metadata api`` to refresh folder
+ Change the default settings content for ``components``, you can subscribe what you want to retrieve, default subscribe just include ``ApexPage``, ``ApexComponent``, ``ApexClass`` and ``ApexTrigger``


Release 0.9.6 (2014-09-16)
++++++++++++++++++++++++++++++++++++
+ Fix bug for issue #38, remove ``ownerRules``, ``criteriaBasedRules`` and ``installedPackages`` from default package.xml
+ Add a command to export CustomLables to csv
+ Update ``SOQL - SELECT FROM`` snippet


Release 0.9.5 (2014-09-15)
++++++++++++++++++++++++++++++++++++
+ Add confirm request for ``new project``
+ Add screenshot for ``Convert XML to JSON``
+ Fix KeyError Exception bug: cancel save operation if conflict.


Release 0.9.4 (2014-09-14)
++++++++++++++++++++++++++++++++++++
+ Move ``check_enabled`` from ``main.py`` to ``util.py``
+ If ``deploy status`` is in ``canceling``, continue to check deploy status until it's canceled.
+ Remove useless ``mkdir`` method from context.py
+ Move some methods from ``context.py`` to ``util.py``
+ Fix bug for ``deploy`` and change the syntax highlight from ``Java`` to ``JavaScript``


Release 0.9.3 (2014-09-13)
++++++++++++++++++++++++++++++++++++
+ Add a command to convert selection to JSON if selection is valid XML format
+ Add context menu item, commands for this command
+ Fix a bug for parsing ``apexrest`` url when executing rest test


Release 0.9.2 (2014-09-13)
++++++++++++++++++++++++++++++++++++
+ Fix bug when ``sosl_string`` contains ``-, ?, *``
+ Update ``query`` method in ``api.py``
+ Separate ``api.py`` to ``metadata.py`` and ``tooling.py`` and move them to new ``api`` folder
+ Rename ``bulkapi.py`` to ``bulk.py`` and move it to ``api`` folder
+ After ``New Project`` is finished, invoke the sublime command ``refresh_folder_list`` to reflect files change in the sidebar
+ After the code file is deleted, the related ``-meta.xml`` file is also deleted


Release 0.9.1 (2014-09-12)
++++++++++++++++++++++++++++++++++++
+ Fix bug when code has conflict and user cancel the save operation


Release 0.9.0 (2014-09-12)
++++++++++++++++++++++++++++++++++++
+ Fix bug for windows sidebar folder refresh
+ Not keep ``default_project`` settings in the settings of ``.config``
+ Add ``reload_symbol_tables_when_create_project`` setting
+ Set default value of ``reload_symbol_tables_when_create_project`` setting to ``false``
+ Fix bug for ``execute anonymous``


Release 0.8.9 (2014-09-11)
++++++++++++++++++++++++++++++++++++
+ If ``retrieve`` is in ``Queued``, thread sleep 2 seconds, else, thread sleep 1 seconds
+ If ``deploy`` is in ``Pending``, thread sleep 2 seconds, else, thread sleep 1 seconds
+ After project is switched, set status for all view of all window.
+ Fix the bug of ``remove temp zip``
+ When deploying, if component parse is finished, display the TestRun Progress


Release 0.8.8 (2014-09-11)
++++++++++++++++++++++++++++++++++++
+ Fix some bug for ``deploy``


Release 0.8.7 (2014-09-10)
++++++++++++++++++++++++++++++++++++
+ Update README
+ When ``New Project``, no need to select project
+ Fix bug ``c:`` completion


Release 0.8.6 (2014-09-09)
++++++++++++++++++++++++++++++++++++
+ Add ``c:`` prefix for custom component completion
+ Add space between timestamp and message in the panel


Release 0.8.5 (2014-09-08)
++++++++++++++++++++++++++++++++++++
+ Move some methods from processor.py to util.py
+ Optimize sObject Cache download
+ Add time stamp prefix for panel message
+ Fix bulkapi bug caused by release 0.8.3
+ Move ``allowed_packages`` to project of projects settings    
+ Add metadata retrieve support for ``allowed_packages``
+ Catch all ``requests`` exception
+ Use panel to display the progress information of ``document reloading``
+ From release 0.8.3 to this version, there have lots of big change, issue is welcomed
+ Add "Accept-Encoding": 'identity, deflate, compress, gzip' header for ``check_status``, ``check_deploy_status`` and ``check_retrieve_status`` in api.py


Release 0.8.4 (2014-09-08)
++++++++++++++++++++++++++++++++++++
+ If just checkOnly, output VALIDATE, otherwise, output DEPLOY
+ Update comments for ``mousemap``
+ Big Milestone, originally, we use ``tooling api`` to download apex code, now it is changed to retrieving by ``metadata api``
+ Happy to remove the ugly method ``refresh_components`` in api.py, this method is very very ugly


Release 0.8.3 (2014-09-07)
++++++++++++++++++++++++++++++++++++
+ Rearrange the attribute position in ``soap_bodies.py``
+ Update README.MD
+ When start ``deploy`` command, if clipboard content is not valid zip file path, set path with empty, otherwise, paste it to input panel
+ Rename ``Retrieve Metadata`` item in main menu to ``Retrieve All``
+ Rename ``Migration`` item in main menu to ``Metadata Migration``
+ Add confirmation request for ``Retrieve All`` and ``Retrieve sObjects and Workflow``
+ Rename ``Describe Sobject`` item in main menu to ``sObject``
+ Rename ``Generate SOQL`` item in main menu to ``sObject SOQL``
+ Rename ``SOQL History`` path from ``soql`` to ``SOQL``
+ Rename ``Workbook Export`` path from ``workbooks`` to ``Workbooks``
+ Rename ``CustomField`` path from ``customfield/customfield.csv`` to ``CustomField/CustomField.csv``
+ Rename ``Validation Rule`` path from ``validation/validation rules.csv`` to ``Validation/Validation Rules.csv``
+ Add ``Apex Code`` related sObject to ``allowed_sobjects`` settings
+ Remove ``proxies`` settings
+ Fix bug: Parse content from package.xml when there is only one types in package.xml
+ Add a new ``Retrieve Package.xml`` command in the context menu, just available when open file is ``package.xml``
+ Add a new ``Deploy to Server`` command in the sidebar menu, just available when the chosen folder is valid package path
+ Put the focus in the log id, press ``Alt`` and click left button, the debug log detail will be retrieved and displayed in the new view
+ Error message when export workflow or validation rule if not retrieve yet
+ Remove ``SnapshotAuditEvent``, ``SnapshotBin``, ``Question``, ``SnapshotConfig``, ``Reply`` and ``UserLicense`` from default ``retrieve_sobjects_workflow_task_body`` in ``soap_bodies.py``


Release 0.8.2 (2014-09-05)
++++++++++++++++++++++++++++++++++++
+ when ``retrieve package.xml``, if file in package.xml is not found in target org, display the message
+ Add ``deploy package.zip`` command to deploy zip file


Release 0.8.1 (2014-09-05)
++++++++++++++++++++++++++++++++++++
+ Change the UI of ``retrieve``
+ Add a command ``retrieve_package`` in the main menu to retrieve metadata by specified package.xml
+ Fix a bug for ``get_static_resource_body`` when creating a new project
+ Fix a bug for displaying the latest debug logs ``ORDER BY StartTime DESC`` when ``fetch logs``
+ Add a new demo link ``Retrieve Package.xml`` in README.MD


Release 0.8.0 (2014-09-04)
++++++++++++++++++++++++++++++++++++
- Change ``se`` Snippet from ``SELECT Id, $2 FROM $1$0`` to ``SELECT Id$2 FROM $1$0``
- Stop to open console when ``Refresh Selected Component``
- Originally, press ``shift+button1*3`` to open class in background and press ``shift+button1*2`` to open class in foreground, now it is changed to ``shift+button1*3`` for background and ``shift+button1*2`` for foreground
- Change screenshots to demo link
- Fix ``query_all`` bug in api.py


Patch for Release 0.7.9 (2014-09-01)
++++++++++++++++++++++++++++++++++++
+ ``output_session_info`` setting is deprecated and replaced by ``.config/session.json``
+ Do not keep ``projects`` settings in the ``.config/settings.json``, because it's private confidential


Release 0.7.9 (2014-09-01)
++++++++++++++++++++++++++++++++++++
+ Fix the display problem of ``Run Test`` and ``LoginTo ApexCode`` cause by History Item 1 of release 0.7.7
+ Rename the path name of ``Test Operation History`` from ``test`` to ``Test``
+ Fix bug for ``Create Component`` and ``Refresh Component Folder`` caused by History Item 1 of release 0.7.7


Release 0.7.8 (2014-08-31)
++++++++++++++++++++++++++++++++++++
+ Fix Operation History Format Problem
+ Inner class completion format ``Inner Class <Class Name>``
+ After Project is created, automatically keep the settings to ``.config`` path
+ Add ``keep_config_history`` to control whether keep config info when ``New Project``
+ Update README.MD


Release 0.7.7 (2014-08-30)
++++++++++++++++++++++++++++++++++++
+ In order to avoid component is not available to CRUD to server because of Sensitive Case, save the component name with lower case into local cache
+ Read custom class from ``Component Attribute Cache`` but not read them from ``Symbol Table Cache``
+ After input ``Page.``, list all custom visualforce page if have
+ After input ``<c:``, list all custom components if have
+ If field is formula, field completion format is ``CalculateField__c\tFormula(Decimal, 18, 0)``


Release 0.7.6 (2014-08-29)
++++++++++++++++++++++++++++++++++++
+ Deep process for result of ``Execute Rest`` if result is json string
+ Change Operation History Format
+ Add ``report_issue`` command


Release 0.7.5 (2014-08-24)
++++++++++++++++++++++++++++++++++++
- Add snippet ``Class Body - Get Child Roles By Role``
- ``Local Change History`` functionality is removed from events.py, just if ``save to server`` is succeed, the local change history will be kept
- Inner class completion format ``Inner Class <Class Name>``


Release 0.7.4 (2014-08-17)
++++++++++++++++++++++++++++++++++++
- Inner Class Completion format
- Add compress header for ``get`` method in api.py
- Fix ``Reload Sobject Cache`` bug caused by release 0.7.3
- Fix Symbol Table completions bug caused by Legacy Symbol Table Cache


Release 0.7.3 (2014-08-16)
++++++++++++++++++++++++++++++++++++
- Add MIT-LICENSE
- Remove ``quick visualforce`` functionality
- Rename method name ``get_toolingapi_settings`` in context.py to ``get_settings`` and update corresponding invoker
- Add two new commands: ``Reload SymbolTable Cache`` and ``Clear SymolTable Cache``
- When creating new project, not only download ``Apex Code`` and ``sObject Cache`` but also ``SymbolTable Cache``
- when class number is more than 400, original symbol table cache structure is stupid and highly reduce the user experience of symbol table completion, in order to speedup symbol table completion, when saving the symbol table cache, store them as the completion format in the cache.


Release 0.7.2 (2014-08-15)
++++++++++++++++++++++++++++++++++++
- Rename ``Toggle Log Panel`` menu item to ``Open Output Panel``
- Update README.MD 
- Add ``Preview Page`` command to preview visualforce page in server, just enabled when opening page
- Update About format


Release 0.7.1 (2014-08-12)
++++++++++++++++++++++++++++++++++++
- Add ``delay_seconds_for_hidden_output_panel_when_succeed`` for control delay seconds to hide output panel when saving succeed
- Rename setting ``delay_seconds_for_hidden_console`` to ``delay_seconds_for_hidden_output_panel_when_failed``


Release 0.7.0 (2014-08-11)
++++++++++++++++++++++++++++++++++++
- Even if component saving is succeed, show the output panel
- If component saving is succeed, hide the open output panel after 1.5 seconds
- When generating workbook or describe sobject, write the type column with Formula(<Field Type>) or <Field Type>


Release 0.6.9 (2014-08-09)
++++++++++++++++++++++++++++++++++++
- When export workbooks, check whether input are valid, if any one is not valid, allow user to input again
- ``Folder Refresh`` reminder message is changed
- Add ``Update Project`` command to just update the apex code but not include sobject metadata
- Add ``Update User Language`` command to update language for running user, which can be used in ``Generate Workbook``, ``Field Completion`` and all related
- Add keymap and commands for ``Update Project`` and ``Update User Language``
- Add a new setting ``user_language`` for ``Update User Language`` command
- Update the main menu, add ``Update`` main menu
- Add settings for package info, including ``name``, ``version``, ``homepage`` and so on
- Rename ``Help`` in main menu to ``About``, after click this item, not open browser and just display the plugin version info
- Add confirm request for ``update cache``


Release 0.6.8 (2014-08-08)
++++++++++++++++++++++++++++++++++++
- Add remind message to show output panel


Release 0.6.7 (2014-08-06)
++++++++++++++++++++++++++++++++++++
- Console Message --> OutputPanel Message
- Add a new command ``Open Log Panel`` for display log panel
- Click ``super+``` to open output panel
- Inner class completion


Release 0.6.6 (2014-08-05)
++++++++++++++++++++++++++++++++++++
- Set ``delay_seconds_for_hidden_console`` default value from ``15`` to ``9999``
- Update description for default settings
- Add property and method completion for inner class


Release 0.6.5 (2014-08-03)
++++++++++++++++++++++++++++++++++++
- Fix picklist completion bug
- Add keymap for ``Execute Rest Test`` command
- Remove catalog from README


Release 0.6.4 (2014-07-30)
++++++++++++++++++++++++++++++++++++
- fix TypeError: save_component() missing 1 required positional argument: 'is_check_only'
- Compatible to api 31 because `compile fail response change <https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/sforce_api_objects_deploydetails.htm>`_


Release 0.6.3 (2014-07-30)
++++++++++++++++++++++++++++++++++++
- Optimize Rest Test when response result is str
- Add ``proxies`` support, just beta


Release 0.6.2 (2014-07-29)
++++++++++++++++++++++++++++++++++++
- Fix issue for ``Delete`` command when list in returned json result is empty


Release 0.6.1 (2014-07-22)
++++++++++++++++++++++++++++++++++++
- **Picklist Value** completion from ``value`` to ``value(label)``
- **Save Conflict** functionality new format: **Modified by <LastName FirstName> at 2014-05-04 10:03:31, continue?**


Release 0.6.0 (2014-07-19)
++++++++++++++++++++++++++++++++++++
- Add search class and its methods for apex lib
- Fix bug for picklist value completion
- Change ``user`` to ``User`` for issue #31


Release 0.5.9 (2014-07-10)
++++++++++++++++++++++++++++++++++++
- Remove useless message from message.py
- Add some buld-in emmet supported snippets
- Add command ``quick_visualforce`` for emmet supported snippets
- Add TOC for README


Release 0.5.8 (2014-06-13)
++++++++++++++++++++++++++++++++++++
- Add a new class template ``Test Class``
- Add description for class template quick choose panel
- ``Clear Cache`` functionality change, display ``project name`` not ``username`` any more
- Add confirm request for ``Run All Test``


Release 0.5.7 (2014-06-05)
++++++++++++++++++++++++++++++++++++
- Optimize for opening url with browser
- Update OSX Keymap
- Fix bug for ``generate workbook`` in OSX
- Add ``Close Job`` command
- Update README.MD


Release 0.5.6 (2014-05-18)
++++++++++++++++++++++++++++++++++++
- Fix bug for ``SELECT * FROM Sobject``, issue #30
- Add time stamp for ``save conflict`` confirm message
- Optimize for ``Fetch Debug Log``
- TraceFlag Bug: Delete the old one and create a new one every time request to create trace flag, issue #29


Release 0.5.5 (2014-05-15)
++++++++++++++++++++++++++++++++++++
- Add ``*`` support for ``Rest Query``, if ``*`` query, just replace it with all fields of related sobject
- Add doc for Wild-card Character query
- Fix ``Run Test`` bug caused by previous release
- Add ``view_selected_code_coverage`` command to view code coverage by selected class name
- Add mousemap to quick view code coverage


Release 0.5.4 (2014-05-15)
++++++++++++++++++++++++++++++++++++
- Narrow down the code coverage column of test run result
- When run specified test class by main menu, if no test class, show the alert message
- Try to fix issue # 23


Release 0.5.3 (2014-05-12)
++++++++++++++++++++++++++++++++++++
- Add new snippet ``Sobject - sobject bracket``
- Update description of ``Update Sobjects``, ``Delete Sobjects``
- Add two commands for command ``Reload Cache`` and ``Clear Cache``
- Fix bug for ``Export Workflow``


Release 0.5.2 (2014-05-10)
++++++++++++++++++++++++++++++++++++
- Since from API 30, compound field (queryByDistance=true) can't be in soql field list
- Fix bug for bulk api caused by release 0.5.1


Release 0.5.1 (2014-05-10)
++++++++++++++++++++++++++++++++++++
- Fix Bug: ``Export CustomField``
- Update OSX keymap
- Add ``Export SOQL`` command to export sobject records by specified soql
- Add command for ``Export SOQL``
- Fix install message alert


Release 0.5.0 (2014-05-09)
++++++++++++++++++++++++++++++++++++
- Update ``README.MD``
- Fix bug UnicodeError for ``Export Workflows`` and ``Export Validation Rule`` in OSX
- Remove some useless code, for example, ``Export Field Dependency``


Release 0.4.9 (2014-05-04)
++++++++++++++++++++++++++++++++++++
- Change default setting ``delay_seconds_for_hidden_console`` from ``10`` to ``15``
- Change default ``api_version`` from ``29`` to ``30``
- Add command ``Retrieve Sobject And Workflow``


Release 0.4.8 (2014-04-27)
++++++++++++++++++++++++++++++++++++
- Optimize picklist value completion
- Remove ``.no-sublime-package``
- Replace ``excluded_sobjects`` settings with ``allowed_sobjects`` settings
- Optimize the sobject cache initiation for OSX
- Upgrade ``requests`` to latest version


Release 0.4.7 (2014-04-26)
++++++++++++++++++++++++++++++++++++
- Fix some flaw for trigger completion
- Optimize Apex Completion
- Update READMD.MD
- Add ``.no-sublime-package`` to tell sublime to unzip the package


Release 0.4.6 (2014-04-21)
++++++++++++++++++++++++++++++++++++
- Add ``last_n_logs`` setting to control the return number by fetching logs
- Add ``check_save_conflict`` setting to control saving conflict when LastModifiedBy is not running user


Release 0.4.5 (2014-04-20)
++++++++++++++++++++++++++++++++++++
- Update snippet: ``Exception - try catch finally`` and ``Exception - try catch``
- Add doc for api.py
- Originally, Keyword completion will exclude the existing-variable completion, now, bug mei le.
- Bug: ``Execute Anonymous`` apex string contains non-english character
- Combine ApexCompletion and SobjectCompletion
- If save error happened, the error line will be highlighted and the highlight line will be canceled after ``delay_seconds_for_hidden_console`` seconds


Release 0.4.4 (2014-04-17)
++++++++++++++++++++++++++++++++++++
- Optimize SOQL Field completion
- Update build-in apex lib
- Update ``query_all`` rest api from ``query`` to ``queryAll`` which is available since winter 14
- Add ``disable_soql_field_completion`` setting for controlling soql field completion
- In order to keep high efficient for code completion, add some not common used standard sobjects to ``Excluded_Sobjects`` setting for code completion


Release 0.4.3 (2014-04-16)
++++++++++++++++++++++++++++++++++++
- Add ``Search`` and ``Quick Search`` for ``Execute Rest Test``
- Update ``README.MD``
- When view is activated, display the default project in the sidebar


Release 0.4.2 (2014-04-16) (Millstone for fixing some flaw in completion)
++++++++++++++++++++++++++++++++++++
- Change ``display_field_name_and_label`` setting default value to false
- BUG: Find variable type by variable name in view (Ignore comment code)
- BUG: Find matched block in visualforce page (the matched region must contains current cursor point)
- Add SOQL field completion, it's very useful feature
- Add a new snippet for ``SELECT * FROM Account``, which is useful for corporation with SOQL field completion


Release 0.4.1 (2014-04-14)
++++++++++++++++++++++++++++++++++++
- Update ``Visualforce`` xPath and Document source code
- Change ``api_version`` back to 29
- Change the default test org password to updated one


Release 0.4.0 (2014-04-14)
++++++++++++++++++++++++++++++++++++
- ``Track Trace Flag`` expiration date verify logic change
- Return all sobjects when call ``Global Describe`` method in api.py, originally default return value is createable and queryable sobjects 


Release 0.3.9  (2014-04-12)
++++++++++++++++++++++++++++++++++++

- Update project folder structure, you can change it to original strcture by remove the ``src/`` from every component attribute
- If visualforce component attribute type is ``Object`` in visualforce completion, return ``<apex:inputField value="{!}"``
- Correct compile command thread status message
- Add local history for ``execute anonymous``, ``execute query``, ``describe sobject`` and ``Run Test``
- Add ``keep_operation_history`` setting to control whether add operation history
- If export something, check workspace availability, if not available, just make it
- Change password of default test org and set password policy to never expire
- Change the default ``api_version`` setting to ``30``
- Add confirmation request for every refresh operation, for example, ``Refresh Classes``, ``Refresh Selected Component``
- Add ``delay_seconds_for_hidden_console`` setting to hide console automatically if save error happen and console is opened, the default **default seconds** is ``10``
- Add a new class template ``Batch Class``
- Add a new command for generating SOQL for specified sobject


Release 0.3.8  (2014-04-03)
++++++++++++++++++++++++++++++++++++

- Add ``Metadata Api`` for document reference
- Display namespace name for standard class in completion
- when saving component, just goto error line if component is ``ApexClass`` or  ``ApexTrigger``
- Update README.MD


Release 0.3.7  (2014-04-02)
++++++++++++++++++++++++++++++++++++

- Remove default value for ``allowed_packages``
- Try to fix `issue #23 <https://github.com/xjsender/SublimeApex/issues/23>`_


Release 0.3.6  (2014-03-30)
++++++++++++++++++++++++++++++++++++

- Add thread progress for document reloading
- Add confirm request for document reloading
- Add default ``docs`` setting for `user customization <https://github.com/xjsender/SublimeApex#salesforce-document-quick-reference>`_


Release 0.3.5  (2014-03-29)
++++++++++++++++++++++++++++++++++++

- Clarify Usage of kinds of feature in README.MD


Release 0.3.4  (2014-03-26)
++++++++++++++++++++++++++++++++++++

- Fix urgent bug for `Issue #22 <https://github.com/xjsender/SublimeApex/issues/22>`_


Release 0.3.3  (2014-03-22)
++++++++++++++++++++++++++++++++++++

- Add confirmation request for ``Refresh Component``
- Add a new command for ``Compile Component``
- Update README


Release 0.3.2  (2014-03-22)
++++++++++++++++++++++++++++++++++++

- Upgrade ``xmltodict`` lib to latest
- Add ``namespace`` for standard class in the completion


**Release 0.3.1** (Milestone of Code Completion) (2014-03-22)
++++++++++++++++++++++++++++++++++++

- Fix bug: ``KeyError: 'symbol_table'`` when save component is not ``ApexClass``
- Add some new standard class to completion
- Keep the parameter info in the completion result
- Update README.MD


Release 0.3.0 (2014-03-20)
++++++++++++++++++++++++++++++++++++

- Remove the duplicate ``New Component`` command and add ``New ApexPage`` command in the quick command palette
- Update the apex standard class lib
- Add SymbolTable support for completions (Completion Parser is copy from Mavensmate)


Release 0.2.9 (2014-03-20)
++++++++++++++++++++++++++++++++++++

- Move the fields describe part from the bottom to top in the sobject describe result
- Change the default apex log level from ``Finest`` to ``Debug``
- Fix a completion regular expression bug for sobject and class which is start with ``j`` or ``J``
- When create new component, if there just have only one template, just choose the only one and no need to manually choose it.


Release 0.2.8 (2014-03-19)
++++++++++++++++++++++++++++++++++++

- Add ``Tooling Query`` for ``Rest Explorer``
- Add ``SOQL & SOSL`` for Salesforce Document Reference
- Change ``ListDebugLogs`` and ``CreateDebugLog`` commands to ``FetchDebugLog`` and ``TrackDebugLog``
- Remove shortcuts for four new commands


Release 0.2.7 (2014-03-17)
++++++++++++++++++++++++++++++++++++

- Update the tabTrigger from muti-bytes to less than 5-bytes for all snippets


Release 0.2.6 (2014-03-16)
++++++++++++++++++++++++++++++++++++

- Fix the bug of ``Rest Post``
- Remove ``Request``, ``Application``, ``LogLength``, ``DurationMilliseconds`` from ``List Debug Log`` columns
- Update description for ``display_field_name_and_label`` settings
- Fix bug: saving conflict on the same component


Release 0.2.5 (2014-03-15)
++++++++++++++++++++++++++++++++++++

- Remove the command ``New Component`` from the side bar
- Remove four shortcut keys for the four new component
- Add a new command for ``Update Project``
- Update the menu item and shortcuts for ``New Project``
- Optimize ``Quick Goto`` functionality, just choosing code name will work.


Release 0.2.4 (2014-03-11)
++++++++++++++++++++++++++++++++++++

- Update README.MD
- Remove shortcut key ``Ctrl+Alt+N`` for creating new component
- Add new shortcut keys for separated four new component commands


Release 0.2.3 (2014-03-10)
++++++++++++++++++++++++++++++++++++

- Add ``Console Toolkit``, ``Standard Objects``, ``Data Model`` and ``Tooling APi`` references to document list
- Update Main Menu Item
- Open ``View Debug Log Detail`` context menu item
- Add a new command ``Update Project``, you can invoke this command by press ``Alt+f7``
- Add sublime commands for new commands
- Add time stamp to succeed message for ``Create Code`` and ``Delete Code``
- Update README.MD for ``Update Project``


Release 0.2.2 (2014-03-07)
++++++++++++++++++++++++++++++++++++

- Remove some useless print statement in the document.py
- Update README.MD for latest release


Release 0.2.1 (2014-03-07)
++++++++++++++++++++++++++++++++++++

- Add ``Rest Api``, ``Visualforce``, ``Chatter Api``, ``Streaming Api`` and ``Bulk Api`` to document list
- Add methods redirect to document list


Release 0.2.0 (2014-03-07)
++++++++++++++++++++++++++++++++++++

- Change ``default_browser_path`` setting name to ``default_chrome_path``
- Add a new salesforce reference function from `Salesforce Reference <https://github.com/Oblongmana/sublime-salesforce-reference>`_
- Add a new snippet ``Custom Button - Disable Button``


Release 0.1.9 (2014-03-06)
++++++++++++++++++++++++++++++++++++
- Fix the static resource bug ``Can't convert 'dict' object to str implicitly``
- When creating trigger, just list the triggerable sobject
- If project is not created, ``New Component`` and ``Refresh Folder`` are disabled
- Update snippets(``Debug - schedule test`` and ``Debug - debug variable``)


Pre-release 0.1.8 (2014-03-05)
++++++++++++++++++++++++++++++++++++

- When save component and error happened, ``go to`` the error line
- Change the ``new component`` to separate ones
- When creating ``trigger``, we just need to choose sobject and input the trigger name
- When creating ``class``, ``component`` or ``page``, we need to choose template and input the name
- Change the ``Component Template``
- Change the ``Main Menu`` and ``Sidebar Menu``
- Move ``Refresh Folder`` function to ``Side Bar`` menu
- When ``New Project``, we need to choose the project, and then create project


Release 0.1.7 (2014-03-04)
++++++++++++++++++++++++++++++++++++

- If project is not created, ``New Component`` and ``Refresh Folder`` are disabled
- Allow empty json body for ``Post`` Action
- If rest response is list, return the list
- When switching project, stop checking login if login session is already in cache
- Fix a completion bug on ``__kav``


Release 0.1.6 (2014-03-01)
++++++++++++++++++++++++++++++++++++

- Update README.MD
- Refractoring api.py


Release 0.1.5 (2014-02-28)
++++++++++++++++++++++++++++++++++++

- Change new view event type from ``on_new_sync`` to ``on_new``
- Set the default format for rest test result to ``JavaScript``
- Add ``Query`` and ``Query All`` function for ``Rest Explorer``


Release 0.1.4 (2014-02-26)
++++++++++++++++++++++++++++++++++++

- Update comments for ``toolingapi.sublime-settings``
- Fix the bug for ``open console``


Release 0.1.3 (2014-02-24)
++++++++++++++++++++++++++++++++++++

- Add the support the static resource refresh functionality for the side bar menu
- Add the support the static resource refresh functionality for the context menu
- Add ``Patch`` method for ``Rest Explorer``

Release 0.1.2 (2014-02-22)
++++++++++++++++++++++++++++++++++++

- Add a new setting ``default_chrome_path``
- Optimize the ``Rest Explorer`` functionality
- When execute ``Rest Explorer``, if input json body is not valid, allow trying again.


Release 0.1.1 (2014-02-22)
++++++++++++++++++++++++++++++++++++

- Add snippets for console toolkit
- Add time stamp for success message of save component result
- Remove some useless message from message.py
- Enhancement for `Issue #12 <https://github.com/xjsender/SublimeApex/issues/12>`_


Release 0.1.0 (2014-02-20)
++++++++++++++++++++++++++++++++++++

- Add snippets for console toolkit
- Update README
- When menu item is not enabled, show the message in the status bar


Release 0.0.9 (2014-02-19)
++++++++++++++++++++++++++++++++++++

- Update the snippets for debug
- Add a new snippet "ReRender Form in JavaScript"
- Display the exception when delete MetadataContainerId, ie., unable to obtain exclusive access to this record
- When creating trigger by template, automatically remove the space input by user
- Change the create component input guide


Patch for 0.0.8 (2014-02-12)
++++++++++++++++++++++++++++++++++++

- Add two template for new component command: Controller and Utility Class
- Add two snippets


Patch for 0.0.7 (2014-02-12)
++++++++++++++++++++++++++++++++++++

- Fix bug for `Issue #11 <https://github.com/xjsender/SublimeApex/issues/11>`_


Release 0.0.7 (2014-02-08)
++++++++++++++++++++++++++++++++++++

- Fix problem when execute anonymous return error
- Change ``disable_keyword_completion`` from true to false


Release 0.0.6 (2014-02-08)
++++++++++++++++++++++++++++++++++++

- Fix retrieve metadata exception


Patch for 0.0.5 (2014-01-31)
++++++++++++++++++++++++++++++++++++

- Update README.MD


0.0.5 (2014-01-22)
++++++++++++++++++++++++++++++++++++

- Add Run All Test functionality
- Adjust the format of test run result of single test class
- Update README.MD


0.0.4 (2014-01-21)
++++++++++++++++++++++++++++++++++++

- Remove ``Widget.sublime-settings`` from plugin


0.0.3 (2014-01-20)
++++++++++++++++++++++++++++++++++++

- Add time stamp for all error message displayed in console
- Disable deploy metadata command
- When use bulk CUD, If clipboard content is file, just paste it into file path input panel
- Remove the ``(0)`` from ``Datetime(0)`` and ``Date(0)`` completion for Date and Datetime field


Patch 0.0.2 (2014-01-11)
++++++++++++++++++++++++++++++++++++

- Change the default test project


0.0.2 (2014-01-07)
++++++++++++++++++++++++++++++++++++

- Remove ``debug_log_headers`` and ``debug_log_headers_properties`` settings
- Unquote and unescape the error message returned by ``Save to Server``
- If ``testMethod`` or ``@IsTest`` is in class body, run test command should be enabled


Patch for 0.0.1 (2014-01-06)
++++++++++++++++++++++++++++++++++++

- When creating new component, if user input is not valid, user can try again if need
- Bug: if project is not created, just create the project for the new component
- Bug: 'BulkApi' object has no attribute 'monitor_batchs'
- Remove ``Widget`` settings and ``Setting - Console`` main menu
- Roll back save_component function to last version


0.0.1 (2014-01-05)
++++++++++++++++++++++++++++++++++++

- Remove ``Loop - for.sublime-snippet`` snippet
- Remove ``all_views_completions.py`` dependency lib
- Move ``commands``, ``keymap``, ``menus``, ``mousemap``, ``settings`` and ``snippet`` path to new config folder


Pre-release x.x.x (2013-12-06 -> 2013-12-31)
++++++++++++++++++++++++++++++++++++++++++++

- There is a long confusing term on github version control
- Add picklist value completions feature
- Export Sobject Data Template by Record Type
- Refactoring sobject completion for those complicated orgs
- Add four settings to permit user to close the code completion feature
- Disable keyword completion by default, need enable manually
- Change default workspace to ``C:/ForcedotcomWorkspace``
- Add support for log levels of anonymous code
- Add a new setting for disabling field name and label completion
- Fix bug for completion: variable in method parameter
- Add picklist value completion support for ``sObject.PicklistFrield =``
- Allow us to input file path when using Bulk Api to CRUD on data
- Automatically detect BOM header when CRUD on data
- After CRUD on csv data, put the log at the same path of this csv data
- Refactoring code completion for sobject field, relationship and picklist value
- Add command for reloading cache of sobjects
- Refactoring sobject field cache structure for speeding up field completion
- [Fix bulk api issue](https://github.com/kennethreitz/requests/issues/1833)
- Add command for clearing cache of sobjects
- Rearrange main menu items
- Automatically divide upload record by 10K every batch
- Add two settings for bulk load: ``maximum_batch_size`` and ``maximum_batch_bytes``
- Support data upload for ``ANSI`` and ``UTF-8`` with or without BOM


0.0.0 (2013-04-14)
++++++++++++++++++++++++++++++++++++

* Birth!

* Frustration
* Conception
