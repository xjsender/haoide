.. :changelog:

Release History

---------------

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
