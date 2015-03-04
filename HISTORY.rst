.. :changelog:

Release History

---------------


Release 2.8.1 (2015-03-05)
++++++++++++++++++
* Fix issue #6
* Enhancement for issue #13


Release 2.8.0 (2015-02-11)
++++++++++++++++++
* Fix issue #11, #12
* Add two commands ``Retrieve All`` and ``Retrieve sObject and Workflow`` in the command palette


Release 2.7.9 (2015-02-06)
++++++++++++++++++
* Fix issue #4
* Fix issue #7
* Enhancement for ``diff_with_server``, allow diff compare with different project
* Upgrade ``requests`` to v2.5.1 and disable the InsecureRequestWarning
* Display line number before column number when ``save_component`` failed


Release 2.7.8 (2015-02-02)
++++++++++++++++++
* Rename ``refresh_component`` command to ``refresh_file_from_server``
* Rename ``refresh_selected_components`` command to ``refresh_files_from_server``
* Rename ``delete_selected_components`` command to ``delete_files_from_server``
* Add a new command for ``retrieve file from other server`` for retrieve file from different project.
* Add a settings ``switch_back_after_migration`` to control whether switch back to original project after ``deploy to server``, ``deploy package to server``, ``deploy lighting to server`` or ``retrieve file from other server``, issue haoide:#3
* Fix issue #5
* Move ``pretty_json`` command from context menu to ``HaoIDE > Utilities > JSON Pretty`` in the main menu
* Update README.MD


Release 2.7.7 (2015-01-22)
++++++++++++++++++
* Fix bug for ``Package.xml Completion``
* Enhancement: display error column in XML if deploy failed
* Enhancement for ``json_to_apex``
* Enhancement for ``describe_sobject``
* Add a new ``json_serialization`` command to serialize JSON to string
* Add a new ``panel`` menu item in Main Menu
* Rearrange Utilities menu item in Main Menu
* Update ``haoide`` to ``HaoIDE``


Release 2.7.6 (2015-01-20)
++++++++++++++++++
* Enhancement for ``create_trace_flag`` command
* Add a enabled check logic for ``export profiles`` command
* Add a new ``haoide > Utilities > Convert JSON to Apex`` command for converting JSON to Apex
* Add commands for ``convert_json_to_apex`` in command palette
* Update README.MD about the `Convert JSON to Apex <https://github.com/xjsender/haoide#convert-json-to-apex>`_


Release 2.7.5 (2015-01-18)
++++++++++++++++++
* Fix bug: messy code when view debug log detail in sublime
* Fix bug: timeout exception is not caught when save component
* Enhancement for completions
* Enhancement for ``export profile`` feature
* Add feature for export of ``userPermission`` and ``tabVisibility``
* Update README.MD


Release 2.7.4 (2015-01-16)
++++++++++++++++++
* Fix bug for issue #75
* Update ``Chanel`` to ``Channel`` in the plugin copyright information
* Update license information
* Remove ``InstalledPackage`` from ``metadataObjects`` settings
* No longer check save conflict when compile code
* Add commands for ``export_profile`` in command palette
* Update default keymap for ``open log panel``, ``open error panel`` and ``open diff panel`` in the ``Utilities`` menu item
* Enhancement for login module, decrease the timeout seconds and repeat login until repeat times exceed 12 times


Release 2.7.3 (2015-01-14)
++++++++++++++++++
* Fix bug for ``extract here`` command
* Fix bug for ``bulk api`` caused by release 2.7.2
* Fix long-term bug for inProgress message of deployment
* Enhancement for ``list debug log``, for example, sort logs order by StartTime ASC, remove the useless "\n"
* Add missed standard objects for ``CustomObject`` when retrieve metadata
* Add new command for exporting profile object security settings, it's a very useful feature
* Add ``Translations`` to metadataObjects settings
* Update snippet description for ``Debug - debug json.sublime-snippet``


Release 2.7.2 (2015-01-12)
++++++++++++++++++
* Fix bug for issue #74
* Fix bug for ``cancel_deployment``
* Fix bug for ``reload symbol table`` when symbol_table is None
* Fix bug for ``execute anonymous`` when anonymous code contains non-english words since release 2.7.0
* Enhancement for message tracking in output panel
* Enhancement for settings check, if settings is valid, just display it in output panel
* Update snippet ``Debug - debug variable.sublime-snippet``
* Add snippet ``Debug - debug json.sublime-snippet``


Release 2.7.1 (2015-01-09)
++++++++++++++++++
* Enhancement for ``standardController completion`` in ``<apex:page standardController=""``
* Enhancement for ``{!acc.} completion`` in visualforce page
* Enhancement for ``diff module``
* Fix some minor bugs


Release 2.7.0 (2015-01-03)
++++++++++++++++++
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
++++++++++++++++++
* Enhancement for ``refresh_folder``
* Enhancement for ``retrieve_all`` and ``retrieve_sobjects_and_workflows``
* Move export csv files to ``.export`` folder, for example, CustomFields, ValidationRules, Workflows and Workbooks, etc.


Release 2.5.9 (2014-12-17)
++++++++++++++++++
* Completion enhancement for building package.xml
* Fix duplicate MetadataContainerId for issue #69
* `Build Package.xml Demo <https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/BuildPackageXML.gif>`_


Release 2.5.8 (2014-12-15)
++++++++++++++++++
* Add all ``sharingRules`` metadata types to default components setting
* Rename ``.package`` to ``.deploy`` for ``deploy to server`` execution
* Remove ``subscribe_component`` and ``unsubscribe_component`` commands
* Add a new ``toggle_commands`` command to replace above two commands
* After a new component is subscribed, refresh the new folder from server
* Rename "ok" in confirm dialog to related message
* Add workspace check when create new project
* Update README.MD


Release 2.5.7 (2014-12-14)
++++++++++++++++++
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
++++++++++++++++++
* Fix Bug for issue #65
* Fix Bug for issue #66
* Enhancement for issue #48, after deployed, the `package.xml` is saved to `.package` in workspace
* Before files are deployed to server, save them to local
* When you deploy any lighting element, just deploy the whole lighting component
* Convert StartTime of debug log to local time by timezone module


Release 2.5.5 (2014-12-09)
++++++++++++++++++
* Fix Bug for creating Lighting Component Element
* When deploy failed due to lower code coverage, display the coverage warning message
* When new component is created, create the meta.xml file for it
* Hide ``Retrieve Lighting from Server`` command when chosen folder is not aura folder
* Hide ``Destruct Lighting from Server`` command when chosen folder is not aura folder
* Hide ``Extract to Here`` command if file extension is not `zip` or `resource`
* Update the Documentation


Release 2.5.4 (2014-12-07)
++++++++++++++++++
* Add `dateutil` module for supporting timezone converting
* Fix Bug for `track debug log`
* Trim the space for `REST URI` automatically
* Remove `lib` from `Packages` in `.gitignore` file
* Support project level workspace for issue #63, see more detail at `workspace <https://github.com/xjsender/SublimeApex#workspace>`_


Release 2.5.3 (2014-12-05)
++++++++++++++++++
* Adjust the context menu from most bottom to center
* Adjust the sidebar menu from most bottom to center
* Fix Bug for issue #62: 'module' object has no attribute 'populate_classes'
* Fix Bug for issue #61: KeyError: 'name' in `get_component_completion`
* Fix Bug for issue #60: Error with 'Update Project'
* Add lighting component description for `Lighting Component` development


Release 2.5.2 (2014-11-27)
++++++++++++++++++
* After new lighting component is created, deploy it to server
* Add a new command for ``pretty json`` in the context menu
* hide the status message in progress bar when track self debug log after save succeed


Release 2.5.1 (2014-11-26)
++++++++++++++++++
* Fix Bug: NoneType Exception when destruct files from server
* Fix Bug: when saving component, the active view is not file
* Add a new settings ``track_log_after_saved`` to control whether track log after save succeed


Release 2.5.0 (2014-11-26)
++++++++++++++++++
* Fix Bug: when delete component, if there is a open view which is not bind to file, it will throw TypeError: argument of type 'NoneType' is not iterable, and then, file is deleted from server but local file is not removed
* Fix Bug: After folder is refreshed or project is updated, update the component cache
* Add `Lighting Component` document reference
* Add `Lighting Component` component tags to completions
* Add `Lighting Component` to `components` settings and set it as default subscribed component
* Add `Lighting Component` update feature
* Add `Lighting Component` components update feature
* Add `Lighting Component` component create feature
* Add `Lighting Component` component destruct feature
* Change default ``api_version`` from 31 to 32
* Remove ``Open Coverage Panel`` menu item in the main menu
* Add ``duration`` column for debug logs and rearrange it's columns order
* Add new document reference for ``Analytic Api``, ``Analytics Cloud Dashboard JSON``, ``Security Implementation`` 
  and ``Lighting Component``
* Add new command for viewing release notes
* Rename ``Extract Static Resource`` command to ``Extract To Here``, which command can be used to extract all zip source file but not only static resource for Salesforce
* Add ``settings`` to ``components`` settings
* If project is not created, all ``export`` feature and ``new component`` feature are not enabled


Release 2.4.0 (2014-11-18)
++++++++++++++++++
* Fix issue #55
* Fix issue: non-english words are encoded to Unicode in result of ``Rest Test``
* Fix issue: when read local cache of record type, ``global name 'users' is not defined`` exception
* Rollback feature of ``view_code_coverage``, see issue #56
* Deprecate ``keep_config_history`` setting
* Update the description of ``keep_local_change_history`` setting
* When save operation has conflict and we cancel it, compare the local with server automatically


Release 2.3.0 (2014-11-14)
++++++++++++++++++
* Use local ``<workspace>/.config/session.json`` to reuse session but not globals() again
* Use local ``<workspace>/.config/recordtype.json`` to ``record type`` but not globals() again
* Use local ``<workspace>/.config/users.json`` to ``users`` but not globals() again
* If ``execute_anonymous`` compiled succeed, use new view to display result, else, use output panel to display result
* Use frontdoor method to login to SFDC
* Add new document reference for ``Analytic Api``
* Display session expired message in the output panel


Release 2.2.0 (2014-11-12)
++++++++++++++++++
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
++++++++++++++++++
+ Fix Bug: ``IndexError: list index out of range`` caused by release 2.0.0
+ Fix Bug for test class judgment: test class is that starts with `test` or ends with `test`
+ Add a new apex.py module, move execute_anonymous method from metadata.py to apex.py
+ Add a new command for ``diff with server`` in the context menu
+ Optimization on ``view_code_coverage`` feature
+ Add a new command ``Utilities > Open Coverage Panel`` in the main menu to open coverage panel
+ Rename ``Open Output Panel`` command to ``Open Log Panel`` and move it from ``Debug`` to ``Utilities`` in the main menu
+ Temporarily remove the ``Run All Test`` feature from ``Debug`` in the main menu


Release 2.0.0 (2014-11-08)
++++++++++++++++++
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
++++++++++++++++++
+ Fix issue #50
+ Fix minor issue for ``delete_component``
+ Fix potential issue for retrieve and deploy
+ Add ``Destruct Files From Server`` command in the sidebar menu for deleting files from sandbox or production
+ Add ``Destruct From Server`` command in the context menu for deleting file from sandbox or production
+ Add new command ``cancel_deployment`` for quickly canceling deployment of specified
+ Add mousemap for canceling deployment: Put the focus in the task Id, and then press alt and click Left Mouse for triple will cancel deployment of specified task Id


Release 1.8.0 (2014-11-03)
++++++++++++++++++
+ In order to prevent UI freeze, use thread to extract encoded zipFile to path
+ Solution for issue #49, add a new settings ``maximum_concurrent_connections`` to control concurrent connections
+ In order to prevent UI freeze, set default value of ``maximum_concurrent_connections`` to ``30``


Release 1.7.0 (2014-10-31)
++++++++++++++++++
+ Fix Bug: If just compile component but not save, no need to keep history
+ Fix Bug: SOQL Field Completion problem if there is more than one character between from and sObject
+ Fix Bug: Replace all `LIST` to `List`
+ Remove ``Settings – Completions`` and ``Settings – Apex Template`` from main menu


Release 1.6.0 (2014-10-25)
++++++++++++++++++
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
++++++++++++++++++
+ Fix Bug for package import error in ``bulk api``
+ Add more detailed action summary for ``save component``, issue #45, issue #46
+ Add description for ``quick controller`` in README.MD


Release 1.4.0 (2014-10-18)
++++++++++++++++++
+ Fix bug for completion: No completions for ``strMap`` if there has ``// Populate Map\nMap<String, String> strMap = new Map<String, String>();``
+ Fix Bug: ``deploy open files to server``
+ Add a new command for ``preview_page`` in the command palette
+ Input ``#`` after controller or extension name in the visualforce page, plugin will automatically create it for you
+ Remove ``static resource`` from default subscribed components


Release 1.3.0 (2014-10-14)
++++++++++++++++++
+ Fix Minor bug for standard class completion: duplicate class in different namespace, for example, Communities, TimeZone, UnsupportedOperationException, Test, QueryException, Action
+ Fix Critical bug: non code file can't be retrieve from server, now, objects, reports and others can be retrieve from server
+ Fix Critical bug: Deploy exception after session cache is expired


Release 1.2.0 (2014-10-11)
++++++++++++++++++
+ ``get_static_resource_body`` settings is deprecated
+ Change default ``api_version`` from ``30`` to ``31``
+ Add a new command ``deploy open files to server`` in the main menu, which is used to deploy open files in the sublime to target server
+ Add command for ``deploy open files to server`` in the Command Palette
+ Add ``static resource`` to default subscribed components
+ Fix Bug for Windows: After ``retrieve all`` is finished, invoke the ``refresh_folder_list`` standard function to display the new folders generated by ``retrieve all``
+ Fix Bug: ``Save to Server`` command (Use Tooling Api) can be only used on ``classes``, ``components``, ``pages`` and ``triggers`` but not other components, however, we can use ``Deploy to Server`` command (Use Metadata Api) to save all components


Release 1.1.0 (2014-10-09)
++++++++++++++++++
+ Fix Bug for Windows: After ``export`` is finished, refresh the project folders to ensure the new folder is shown in the sidebar
+ Fix Bug: display deploy failed message if deploy is failed.
+ Fix Bug: symbol table is null when iterate symbol table
+ Update README.MD


Release 1.0.9 (2014-10-04)
++++++++++++++++++
+ Fix Bug: After open a new view, open context menu, it will throw NoneType exception


Release 1.0.8 (2014-10-02)
++++++++++++++++++
+ Fix issue at ``https://success.salesforce.com/answers?id=90630000000gxvwAAA``


Release 1.0.7 (2014-09-30)
++++++++++++++++++
+ Fix Minor Bug for windows: After ``.config`` is generated, invoke the sublime command: ``refresh_folder_list``
+ Enhancement for checking whether current project is active project
+ Fix Critical Bug: If session is expired, we want to refresh the folder or update project, the console will always stop at  the step of ``[sf:retrieve] Start request for a retrieve...``
+ Fix issue #42, stop to remove folder when refresh folder or update project but just override, Notice: if you delete some file in the server, after ``update project`` and ``refresh folder``, these files will not deleted in the sublime, so, I suggest you should delete code in the sublime but not in the server


Release 1.0.6 (2014-09-28)
++++++++++++++++++
+ Fix Minor Bug: After ``retrieve_package_file`` is succeed, hide the output panel
+ Fix Minor Bug: If current project is not ``active project``, disable the ``Retrieve Files From Server`` functionality
+ Fix Minor Bug: If current project is not ``active project``, disable the ``Retrieve File From Server`` functionality
+ Fix Minor Bug: If current project is not ``active project``, disable the ``Run Test Class`` functionality


Release 1.0.5 (2014-09-27)
++++++++++++++++++
+ Fix bug: Exception when ``new project`` in a new org
+ Fix bug: If there is no any trigger, after ``new project``, the folder of ``trigger`` is not created.
+ Fix bug: ``subscribed_meta_folders`` and ``meta_folders`` in settings are not correct


Release 1.0.4 (2014-09-25)
++++++++++++++++++
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
++++++++++++++++++
+ After ``Update Project`` is finished, remove the original ``src`` tree and then extract the zipFile to ``src``
+ After ``Refresh Folder`` is finished, remove the original folders and then extract the zipFile to specified folders
+ Fix urgent bug: if no project in sidebar and sidebar is hidden, after ``new project`` or ``update project``, the sidebar is not open automatically.


Release 1.0.2 (2014-09-23)
++++++++++++++++++
+ Update the default value of ``checkOnly`` in ``deploy_options`` settings from ``true`` to ``false``
+ Fix Urgent bug: If one class is created in the server, after ``refresh folder``, cache of this folder will override all components
+ Remove some useless ``print`` statement
+ Fix minor bug: After code is saved, duplicate extension is displayed in the console
+ Add two settings ``folder_exclude_patterns`` and ``files_exclude_patterns`` to hide everything you want to hide in the sidebar
+ Update the ``add project to workspace`` logic to compatible with the above two settings
+ Add a new command ``Update Project Patterns`` in the main menu, see [Pattern Demo](https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/ProjectPattern.gif)


Release 1.0.1 (2014-09-22)
++++++++++++++++++
+ Add ``LogLength`` column to result of ``fetch debug logs``
+ Update default value of ``display_field_name_and_label`` setting from ``false`` to ``true``
+ Remove the ``\n`` from success message in ``document.py``
+ Add description for ``save multiple components`` feature in the README.MD
+ Change output directory of ``retrieve package.xml`` from current directory to ``[ProjectName]-201409221812``
+ Add ``messages`` notes


Release 1.0.0 (2014-09-21)
++++++++++++++++++
+ Add a new command ``Deploy To Server`` in the context menu
+ Fix bug for ``retrieve`` when session is expired
+ Fix bug for ``New ApexClass``, ``New ApexTrigger``, ``New ApexComponent`` and ``New ApexPage``
+ Fix bug ``TypeError: is_visible() missing 1 required positional argument: 'dirs'`` when open ``Command Palette``
+ Fix bug: If there is no any trigger or class, we want to create the first one, there has exception
+ Fix bug: ``Package.xml`` was overridden by ``refresh folder``


Release 0.9.9 (2014-09-20)
++++++++++++++++++
+ Try to fix bug for ``new release messages display`` or who can tell me how to display ``release message``
+ Fix bug for ``quick go to component``


Release 0.9.8 (2014-09-20)
++++++++++++++++++
+ Support multiply folder refresh
+ Add standard sObjects to CustomObject Package Members when create new project if CustomObject is subscribed
+ Update default subscribed components
+ Add a new command ``Deploy Files to Server``
+ Fix bug: Display debugLog info after deploy is finished
+ Upsert demo in README.MD
+ Display the new release message after new released upgrade is finished


Release 0.9.7 (2014-09-19)
++++++++++++++++++
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
++++++++++++++++++
+ Fix bug for issue #38, remove ``ownerRules``, ``criteriaBasedRules`` and ``installedPackages`` from default package.xml
+ Add a command to export CustomLables to csv
+ Update ``SOQL - SELECT FROM`` snippet


Release 0.9.5 (2014-09-15)
++++++++++++++++++
+ Add confirm request for ``new project``
+ Add screenshot for ``Convert XML to JSON``
+ Fix KeyError Exception bug: cancel save operation if conflict.


Release 0.9.4 (2014-09-14)
++++++++++++++++++
+ Move ``check_enabled`` from ``main.py`` to ``util.py``
+ If ``deploy status`` is in ``canceling``, continue to check deploy status until it's canceled.
+ Remove useless ``mkdir`` method from context.py
+ Move some methods from ``context.py`` to ``util.py``
+ Fix bug for ``deploy`` and change the syntax highlight from ``Java`` to ``JavaScript``


Release 0.9.3 (2014-09-13)
++++++++++++++++++
+ Add a command to convert selection to JSON if selection is valid XML format
+ Add context menu item, commands for this command
+ Fix a bug for parsing ``apexrest`` url when executing rest test


Release 0.9.2 (2014-09-13)
++++++++++++++++++
+ Fix bug when ``sosl_string`` contains ``-, ?, *``
+ Update ``query`` method in ``api.py``
+ Separate ``api.py`` to ``metadata.py`` and ``tooling.py`` and move them to new ``api`` folder
+ Rename ``bulkapi.py`` to ``bulk.py`` and move it to ``api`` folder
+ After ``New Project`` is finished, invoke the sublime command ``refresh_folder_list`` to reflect files change in the sidebar
+ After the code file is deleted, the related ``-meta.xml`` file is also deleted


Release 0.9.1 (2014-09-12)
++++++++++++++++++
+ Fix bug when code has conflict and user cancel the save operation


Release 0.9.0 (2014-09-12)
++++++++++++++++++
+ Fix bug for windows sidebar folder refresh
+ Not keep ``default_project`` settings in the settings of ``.config``
+ Add ``reload_symbol_tables_when_create_project`` setting
+ Set default value of ``reload_symbol_tables_when_create_project`` setting to ``false``
+ Fix bug for ``execute anonymous``


Release 0.8.9 (2014-09-11)
++++++++++++++++++
+ If ``retrieve`` is in ``Queued``, thread sleep 2 seconds, else, thread sleep 1 seconds
+ If ``deploy`` is in ``Pending``, thread sleep 2 seconds, else, thread sleep 1 seconds
+ After project is switched, set status for all view of all window.
+ Fix the bug of ``remove temp zip``
+ When deploying, if component parse is finished, display the TestRun Progress


Release 0.8.8 (2014-09-11)
++++++++++++++++++
+ Fix some bug for ``deploy``


Release 0.8.7 (2014-09-10)
++++++++++++++++++
+ Update README
+ When ``New Project``, no need to select project
+ Fix bug ``c:`` completion


Release 0.8.6 (2014-09-09)
++++++++++++++++++
+ Add ``c:`` prefix for custom component completion
+ Add space between timestamp and message in the panel


Release 0.8.5 (2014-09-08)
++++++++++++++++++
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
++++++++++++++++++
+ If just checkOnly, output VALIDATE, otherwise, output DEPLOY
+ Update comments for ``mousemap``
+ Big Milestone, originally, we use ``tooling api`` to download apex code, now it is changed to retrieving by ``metadata api``
+ Happy to remove the ugly method ``refresh_components`` in api.py, this method is very very ugly


Release 0.8.3 (2014-09-07)
++++++++++++++++++
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
++++++++++++++++++
+ when ``retrieve package.xml``, if file in package.xml is not found in target org, display the message
+ Add ``deploy package.zip`` command to deploy zip file


Release 0.8.1 (2014-09-05)
++++++++++++++++++
+ Change the UI of ``retrieve``
+ Add a command ``retrieve_package`` in the main menu to retrieve metadata by specified package.xml
+ Fix a bug for ``get_static_resource_body`` when creating a new project
+ Fix a bug for displaying the latest debug logs ``ORDER BY StartTime DESC`` when ``fetch logs``
+ Add a new demo link ``Retrieve Package.xml`` in README.MD


Release 0.8.0 (2014-09-04)
++++++++++++++++++
- Change ``se`` Snippet from ``SELECT Id, $2 FROM $1$0`` to ``SELECT Id$2 FROM $1$0``
- Stop to open console when ``Refresh Selected Component``
- Originally, press ``shift+button1*3`` to open class in background and press ``shift+button1*2`` to open class in foreground, now it is changed to ``shift+button1*3`` for background and ``shift+button1*2`` for foreground
- Change screenshots to demo link
- Fix ``query_all`` bug in api.py


Patch for Release 0.7.9 (2014-09-01)
++++++++++++++++++
+ ``output_session_info`` setting is deprecated and replaced by ``.config/session.json``
+ Do not keep ``projects`` settings in the ``.config/settings.json``, because it's private confidential


Release 0.7.9 (2014-09-01)
++++++++++++++++++
+ Fix the display problem of ``Run Test`` and ``LoginTo ApexCode`` cause by History Item 1 of release 0.7.7
+ Rename the path name of ``Test Operation History`` from ``test`` to ``Test``
+ Fix bug for ``Create Component`` and ``Refresh Component Folder`` caused by History Item 1 of release 0.7.7


Release 0.7.8 (2014-08-31)
++++++++++++++++++
+ Fix Operation History Format Problem
+ Inner class completion format ``Inner Class <Class Name>``
+ After Project is created, automatically keep the settings to ``.config`` path
+ Add ``keep_config_history`` to control whether keep config info when ``New Project``
+ Update README.MD


Release 0.7.7 (2014-08-30)
++++++++++++++++++
+ In order to avoid component is not available to CRUD to server because of Sensitive Case, save the component name with lower case into local cache
+ Read custom class from ``Component Attribute Cache`` but not read them from ``Symbol Table Cache``
+ After input ``Page.``, list all custom visualforce page if have
+ After input ``<c:``, list all custom components if have
+ If field is formula, field completion format is ``CalculateField__c\tFormula(Decimal, 18, 0)``


Release 0.7.6 (2014-08-29)
++++++++++++++++++
+ Deep process for result of ``Execute Rest`` if result is json string
+ Change Operation History Format
+ Add ``report_issue`` command


Release 0.7.5 (2014-08-24)
++++++++++++++++++
- Add snippet ``Class Body - Get Child Roles By Role``
- ``Local Change History`` functionality is removed from events.py, just if ``save to server`` is succeed, the local change history will be kept
- Inner class completion format ``Inner Class <Class Name>``


Release 0.7.4 (2014-08-17)
++++++++++++++++++
- Inner Class Completion format
- Add compress header for ``get`` method in api.py
- Fix ``Reload Sobject Cache`` bug caused by release 0.7.3
- Fix Symbol Table completions bug caused by Legacy Symbol Table Cache


Release 0.7.3 (2014-08-16)
++++++++++++++++++
- Add MIT-LICENSE
- Remove ``quick visualforce`` functionality
- Rename method name ``get_toolingapi_settings`` in context.py to ``get_settings`` and update corresponding invoker
- Add two new commands: ``Reload SymbolTable Cache`` and ``Clear SymolTable Cache``
- When creating new project, not only download ``Apex Code`` and ``sObject Cache`` but also ``SymbolTable Cache``
- when class number is more than 400, original symbol table cache structure is stupid and highly reduce the user experience of symbol table completion, in order to speedup symbol table completion, when saving the symbol table cache, store them as the completion format in the cache.


Release 0.7.2 (2014-08-15)
++++++++++++++++++
- Rename ``Toggle Log Panel`` menu item to ``Open Output Panel``
- Update README.MD 
- Add ``Preview Page`` command to preview visualforce page in server, just enabled when opening page
- Update About format


Release 0.7.1 (2014-08-12)
++++++++++++++++++
- Add ``delay_seconds_for_hidden_output_panel_when_succeed`` for control delay seconds to hide output panel when saving succeed
- Rename setting ``delay_seconds_for_hidden_console`` to ``delay_seconds_for_hidden_output_panel_when_failed``


Release 0.7.0 (2014-08-11)
++++++++++++++++++
- Even if component saving is succeed, show the output panel
- If component saving is succeed, hide the open output panel after 1.5 seconds
- When generating workbook or describe sobject, write the type column with Formula(<Field Type>) or <Field Type>


Release 0.6.9 (2014-08-09)
++++++++++++++++++
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
++++++++++++++++++
- Add remind message to show output panel


Release 0.6.7 (2014-08-06)
++++++++++++++++++
- Console Message --> OutputPanel Message
- Add a new command ``Open Log Panel`` for display log panel
- Click ``super+``` to open output panel
- Inner class completion


Release 0.6.6 (2014-08-05)
++++++++++++++++++
- Set ``delay_seconds_for_hidden_console`` default value from ``15`` to ``9999``
- Update description for default settings
- Add property and method completion for inner class


Release 0.6.5 (2014-08-03)
++++++++++++++++++
- Fix picklist completion bug
- Add keymap for ``Execute Rest Test`` command
- Remove catalog from README


Release 0.6.4 (2014-07-30)
++++++++++++++++++
- fix TypeError: save_component() missing 1 required positional argument: 'is_check_only'
- Compatible to api 31 because `compile fail response change <https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/sforce_api_objects_deploydetails.htm>`_


Release 0.6.3 (2014-07-30)
++++++++++++++++++
- Optimize Rest Test when response result is str
- Add ``proxies`` support, just beta


Release 0.6.2 (2014-07-29)
++++++++++++++++++
- Fix issue for ``Delete`` command when list in returned json result is empty


Release 0.6.1 (2014-07-22)
++++++++++++++++++
- **Picklist Value** completion from ``value`` to ``value(label)``
- **Save Conflict** functionality new format: **Modified by <LastName FirstName> at 2014-05-04 10:03:31, continue?**


Release 0.6.0 (2014-07-19)
++++++++++++++++++
- Add search class and its methods for apex lib
- Fix bug for picklist value completion
- Change ``user`` to ``User`` for issue #31


Release 0.5.9 (2014-07-10)
++++++++++++++++++
- Remove useless message from message.py
- Add some buld-in emmet supported snippets
- Add command ``quick_visualforce`` for emmet supported snippets
- Add TOC for README


Release 0.5.8 (2014-06-13)
++++++++++++++++++
- Add a new class template ``Test Class``
- Add description for class template quick choose panel
- ``Clear Cache`` functionality change, display ``project name`` not ``username`` any more
- Add confirm request for ``Run All Test``


Release 0.5.7 (2014-06-05)
++++++++++++++++++
- Optimize for opening url with browser
- Update OSX Keymap
- Fix bug for ``generate workbook`` in OSX
- Add ``Close Job`` command
- Update README.MD


Release 0.5.6 (2014-05-18)
++++++++++++++++++
- Fix bug for ``SELECT * FROM Sobject``, issue #30
- Add time stamp for ``save conflict`` confirm message
- Optimize for ``Fetch Debug Log``
- TraceFlag Bug: Delete the old one and create a new one every time request to create trace flag, issue #29


Release 0.5.5 (2014-05-15)
++++++++++++++++++
- Add ``*`` support for ``Rest Query``, if ``*`` query, just replace it with all fields of related sobject
- Add doc for Wild-card Character query
- Fix ``Run Test`` bug caused by previous release
- Add ``view_selected_code_coverage`` command to view code coverage by selected class name
- Add mousemap to quick view code coverage


Release 0.5.4 (2014-05-15)
++++++++++++++++++
- Narrow down the code coverage column of test run result
- When run specified test class by main menu, if no test class, show the alert message
- Try to fix issue # 23


Release 0.5.3 (2014-05-12)
++++++++++++++++++
- Add new snippet ``Sobject - sobject bracket``
- Update description of ``Update Sobjects``, ``Delete Sobjects``
- Add two commands for command ``Reload Cache`` and ``Clear Cache``
- Fix bug for ``Export Workflow``


Release 0.5.2 (2014-05-10)
++++++++++++++++++
- Since from API 30, compound field (queryByDistance=true) can't be in soql field list
- Fix bug for bulk api caused by release 0.5.1


Release 0.5.1 (2014-05-10)
++++++++++++++++++
- Fix Bug: ``Export CustomField``
- Update OSX keymap
- Add ``Export SOQL`` command to export sobject records by specified soql
- Add command for ``Export SOQL``
- Fix install message alert


Release 0.5.0 (2014-05-09)
++++++++++++++++++
- Update ``README.MD``
- Fix bug UnicodeError for ``Export Workflows`` and ``Export Validation Rule`` in OSX
- Remove some useless code, for example, ``Export Field Dependency``


Release 0.4.9 (2014-05-04)
++++++++++++++++++
- Change default setting ``delay_seconds_for_hidden_console`` from ``10`` to ``15``
- Change default ``api_version`` from ``29`` to ``30``
- Add command ``Retrieve Sobject And Workflow``


Release 0.4.8 (2014-04-27)
++++++++++++++++++
- Optimize picklist value completion
- Remove ``.no-sublime-package``
- Replace ``excluded_sobjects`` settings with ``allowed_sobjects`` settings
- Optimize the sobject cache initiation for OSX
- Upgrade ``requests`` to latest version


Release 0.4.7 (2014-04-26)
++++++++++++++++++
- Fix some flaw for trigger completion
- Optimize Apex Completion
- Update READMD.MD
- Add ``.no-sublime-package`` to tell sublime to unzip the package


Release 0.4.6 (2014-04-21)
++++++++++++++++++
- Add ``last_n_logs`` setting to control the return number by fetching logs
- Add ``check_save_conflict`` setting to control saving conflict when LastModifiedBy is not running user


Release 0.4.5 (2014-04-20)
++++++++++++++++++
- Update snippet: ``Exception - try catch finally`` and ``Exception - try catch``
- Add doc for api.py
- Originally, Keyword completion will exclude the existing-variable completion, now, bug mei le.
- Bug: ``Execute Anonymous`` apex string contains non-english character
- Combine ApexCompletion and SobjectCompletion
- If save error happened, the error line will be highlighted and the highlight line will be canceled after ``delay_seconds_for_hidden_console`` seconds


Release 0.4.4 (2014-04-17)
++++++++++++++++++
- Optimize SOQL Field completion
- Update build-in apex lib
- Update ``query_all`` rest api from ``query`` to ``queryAll`` which is available since winter 14
- Add ``disable_soql_field_completion`` setting for controlling soql field completion
- In order to keep high efficient for code completion, add some not common used standard sobjects to ``Excluded_Sobjects`` setting for code completion


Release 0.4.3 (2014-04-16)
++++++++++++++++++
- Add ``Search`` and ``Quick Search`` for ``Execute Rest Test``
- Update ``README.MD``
- When view is activated, display the default project in the sidebar


Release 0.4.2 (2014-04-16) (Millstone for fixing some flaw in completion)
++++++++++++++++++
- Change ``display_field_name_and_label`` setting default value to false
- BUG: Find variable type by variable name in view (Ignore comment code)
- BUG: Find matched block in visualforce page (the matched region must contains current cursor point)
- Add SOQL field completion, it's very useful feature
- Add a new snippet for ``SELECT * FROM Account``, which is useful for corporation with SOQL field completion


Release 0.4.1 (2014-04-14)
++++++++++++++++++
- Update ``Visualforce`` xPath and Document source code
- Change ``api_version`` back to 29
- Change the default test org password to updated one


Release 0.4.0 (2014-04-14)
++++++++++++++++++
- ``Track Trace Flag`` expiration date verify logic change
- Return all sobjects when call ``Global Describe`` method in api.py, originally default return value is createable and queryable sobjects 


Release 0.3.9  (2014-04-12)
++++++++++++++++++

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
++++++++++++++++++

- Add ``Metadata Api`` for document reference
- Display namespace name for standard class in completion
- when saving component, just goto error line if component is ``ApexClass`` or  ``ApexTrigger``
- Update README.MD


Release 0.3.7  (2014-04-02)
++++++++++++++++++

- Remove default value for ``allowed_packages``
- Try to fix `issue #23 <https://github.com/xjsender/SublimeApex/issues/23>`_


Release 0.3.6  (2014-03-30)
++++++++++++++++++

- Add thread progress for document reloading
- Add confirm request for document reloading
- Add default ``docs`` setting for `user customization <https://github.com/xjsender/SublimeApex#salesforce-document-quick-reference>`_


Release 0.3.5  (2014-03-29)
++++++++++++++++++

- Clarify Usage of kinds of feature in README.MD


Release 0.3.4  (2014-03-26)
++++++++++++++++++

- Fix urgent bug for `Issue #22 <https://github.com/xjsender/SublimeApex/issues/22>`_


Release 0.3.3  (2014-03-22)
++++++++++++++++++

- Add confirmation request for ``Refresh Component``
- Add a new command for ``Compile Component``
- Update README


Release 0.3.2  (2014-03-22)
++++++++++++++++++

- Upgrade ``xmltodict`` lib to latest
- Add ``namespace`` for standard class in the completion


**Release 0.3.1** (Milestone of Code Completion) (2014-03-22)
++++++++++++++++++

- Fix bug: ``KeyError: 'symbol_table'`` when save component is not ``ApexClass``
- Add some new standard class to completion
- Keep the parameter info in the completion result
- Update README.MD


Release 0.3.0 (2014-03-20)
++++++++++++++++++

- Remove the duplicate ``New Component`` command and add ``New ApexPage`` command in the quick command palette
- Update the apex standard class lib
- Add SymbolTable support for completions (Completion Parser is copy from Mavensmate)


Release 0.2.9 (2014-03-20)
++++++++++++++++++

- Move the fields describe part from the bottom to top in the sobject describe result
- Change the default apex log level from ``Finest`` to ``Debug``
- Fix a completion regular expression bug for sobject and class which is start with ``j`` or ``J``
- When create new component, if there just have only one template, just choose the only one and no need to manually choose it.


Release 0.2.8 (2014-03-19)
++++++++++++++++++

- Add ``Tooling Query`` for ``Rest Explorer``
- Add ``SOQL & SOSL`` for Salesforce Document Reference
- Change ``ListDebugLogs`` and ``CreateDebugLog`` commands to ``FetchDebugLog`` and ``TrackDebugLog``
- Remove shortcuts for four new commands


Release 0.2.7 (2014-03-17)
++++++++++++++++++

- Update the tabTrigger from muti-bytes to less than 5-bytes for all snippets


Release 0.2.6 (2014-03-16)
++++++++++++++++++

- Fix the bug of ``Rest Post``
- Remove ``Request``, ``Application``, ``LogLength``, ``DurationMilliseconds`` from ``List Debug Log`` columns
- Update description for ``display_field_name_and_label`` settings
- Fix bug: saving conflict on the same component


Release 0.2.5 (2014-03-15)
++++++++++++++++++

- Remove the command ``New Component`` from the side bar
- Remove four shortcut keys for the four new component
- Add a new command for ``Update Project``
- Update the menu item and shortcuts for ``New Project``
- Optimize ``Quick Goto`` functionality, just choosing code name will work.


Release 0.2.4 (2014-03-11)
++++++++++++++++++

- Update README.MD
- Remove shortcut key ``Ctrl+Alt+N`` for creating new component
- Add new shortcut keys for separated four new component commands


Release 0.2.3 (2014-03-10)
++++++++++++++++++

- Add ``Console Toolkit``, ``Standard Objects``, ``Data Model`` and ``Tooling APi`` references to document list
- Update Main Menu Item
- Open ``View Debug Log Detail`` context menu item
- Add a new command ``Update Project``, you can invoke this command by press ``Alt+f7``
- Add sublime commands for new commands
- Add time stamp to succeed message for ``Create Code`` and ``Delete Code``
- Update README.MD for ``Update Project``


Release 0.2.2 (2014-03-07)
++++++++++++++++++

- Remove some useless print statement in the document.py
- Update README.MD for latest release


Release 0.2.1 (2014-03-07)
++++++++++++++++++

- Add ``Rest Api``, ``Visualforce``, ``Chatter Api``, ``Streaming Api`` and ``Bulk Api`` to document list
- Add methods redirect to document list


Release 0.2.0 (2014-03-07)
++++++++++++++++++

- Change ``default_browser_path`` setting name to ``default_chrome_path``
- Add a new salesforce reference function from `Salesforce Reference <https://github.com/Oblongmana/sublime-salesforce-reference>`_
- Add a new snippet ``Custom Button - Disable Button``


Release 0.1.9 (2014-03-06)
++++++++++++++++++
- Fix the static resource bug ``Can't convert 'dict' object to str implicitly``
- When creating trigger, just list the triggerable sobject
- If project is not created, ``New Component`` and ``Refresh Folder`` are disabled
- Update snippets(``Debug - schedule test`` and ``Debug - debug variable``)


Pre-release 0.1.8 (2014-03-05)
++++++++++++++++++

- When save component and error happened, ``go to`` the error line
- Change the ``new component`` to separate ones
- When creating ``trigger``, we just need to choose sobject and input the trigger name
- When creating ``class``, ``component`` or ``page``, we need to choose template and input the name
- Change the ``Component Template``
- Change the ``Main Menu`` and ``Sidebar Menu``
- Move ``Refresh Folder`` function to ``Side Bar`` menu
- When ``New Project``, we need to choose the project, and then create project


Release 0.1.7 (2014-03-04)
++++++++++++++++++

- If project is not created, ``New Component`` and ``Refresh Folder`` are disabled
- Allow empty json body for ``Post`` Action
- If rest response is list, return the list
- When switching project, stop checking login if login session is already in cache
- Fix a completion bug on ``__kav``


Release 0.1.6 (2014-03-01)
++++++++++++++++++

- Update README.MD
- Refractoring api.py


Release 0.1.5 (2014-02-28)
++++++++++++++++++

- Change new view event type from ``on_new_sync`` to ``on_new``
- Set the default format for rest test result to ``JavaScript``
- Add ``Query`` and ``Query All`` function for ``Rest Explorer``


Release 0.1.4 (2014-02-26)
++++++++++++++++++

- Update comments for ``toolingapi.sublime-settings``
- Fix the bug for ``open console``


Release 0.1.3 (2014-02-24)
++++++++++++++++++

- Add the support the static resource refresh functionality for the side bar menu
- Add the support the static resource refresh functionality for the context menu
- Add ``Patch`` method for ``Rest Explorer``

Release 0.1.2 (2014-02-22)
++++++++++++++++++

- Add a new setting ``default_chrome_path``
- Optimize the ``Rest Explorer`` functionality
- When execute ``Rest Explorer``, if input json body is not valid, allow trying again.


Release 0.1.1 (2014-02-22)
++++++++++++++++++

- Add snippets for console toolkit
- Add time stamp for success message of save component result
- Remove some useless message from message.py
- Enhancement for `Issue #12 <https://github.com/xjsender/SublimeApex/issues/12>`_


Release 0.1.0 (2014-02-20)
++++++++++++++++++

- Add snippets for console toolkit
- Update README
- When menu item is not enabled, show the message in the status bar


Release 0.0.9 (2014-02-19)
++++++++++++++++++

- Update the snippets for debug
- Add a new snippet "ReRender Form in JavaScript"
- Display the exception when delete MetadataContainerId, ie., unable to obtain exclusive access to this record
- When creating trigger by template, automatically remove the space input by user
- Change the create component input guide


Patch for 0.0.8 (2014-02-12)
++++++++++++++++++

- Add two template for new component command: Controller and Utility Class
- Add two snippets


Patch for 0.0.7 (2014-02-12)
++++++++++++++++++

- Fix bug for `Issue #11 <https://github.com/xjsender/SublimeApex/issues/11>`_


Release 0.0.7 (2014-02-08)
++++++++++++++++++

- Fix problem when execute anonymous return error
- Change ``disable_keyword_completion`` from true to false


Release 0.0.6 (2014-02-08)
++++++++++++++++++

- Fix retrieve metadata exception


Patch for 0.0.5 (2014-01-31)
++++++++++++++++++

- Update README.MD


0.0.5 (2014-01-22)
++++++++++++++++++

- Add Run All Test functionality
- Adjust the format of test run result of single test class
- Update README.MD


0.0.4 (2014-01-21)
++++++++++++++++++

- Remove ``Widget.sublime-settings`` from plugin


0.0.3 (2014-01-20)
++++++++++++++++++

- Add time stamp for all error message displayed in console
- Disable deploy metadata command
- When use bulk CUD, If clipboard content is file, just paste it into file path input panel
- Remove the ``(0)`` from ``Datetime(0)`` and ``Date(0)`` completion for Date and Datetime field


Patch 0.0.2 (2014-01-11)
++++++++++++++++++

- Change the default test project


0.0.2 (2014-01-07)
++++++++++++++++++

- Remove ``debug_log_headers`` and ``debug_log_headers_properties`` settings
- Unquote and unescape the error message returned by ``Save to Server``
- If ``testMethod`` or ``@IsTest`` is in class body, run test command should be enabled


Patch for 0.0.1 (2014-01-06)
++++++++++++++++++

- When creating new component, if user input is not valid, user can try again if need
- Bug: if project is not created, just create the project for the new component
- Bug: 'BulkApi' object has no attribute 'monitor_batchs'
- Remove ``Widget`` settings and ``Setting - Console`` main menu
- Roll back save_component function to last version


0.0.1 (2014-01-05)
++++++++++++++++++

- Remove ``Loop - for.sublime-snippet`` snippet
- Remove ``all_views_completions.py`` dependency lib
- Move ``commands``, ``keymap``, ``menus``, ``mousemap``, ``settings`` and ``snippet`` path to new config folder


Pre-release x.x.x (2013-12-06 -> 2013-12-31)
++++++++++++++++++

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
++++++++++++++++++

* Birth!

* Frustration
* Conception
