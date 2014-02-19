.. :changelog:

Release History
---------------

Release 0.0.9 (2014-02-19)
++++++++++++++++++

- Update the snippets for debug
- Add a new snippet "ReRender Form in JavaScript"
- Display the exception when delete MetadataContainerId, ie., unable to obtain exclusive access to this record


Patch for 0.0.8 (2014-02-12)
++++++++++++++++++

- Add two template for new component command: Controller and Utility Class
- Add two snippets


Patch for 0.0.7 (2014-02-12)
++++++++++++++++++

- Fix bug for [Issue #11](https://github.com/xjsender/SublimeApex/issues/11)


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
