# Sceenshot #
Funcationality Screenshots shown as below,

###Menus
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/main%20menu.png" />
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/sidebar%20menu.png" />
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/context%20menu.png" />

###Switch Project
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/switch%20project.png" />

###Sobject Field Completions
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/sobject%20field%20completions.png" />

###Apex Code Completions
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/Apex%20code%20completions.png" />
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/map%20completions.png" />
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/set%20completions.png" />
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/list%20completions.png" />

###Cross View Completions
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/cross%20view%20completions.png" />

###Visualforce Page Completions
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/visualforce%20page%20completions.png" />

###Run Test
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/choose%20test%20class.png" />
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/test%20result.png" />

###Refresh Folder
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/refresh%20folder.png" />

###Execute Anonymous
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/execute%20anonymous.png" />

###Execute Query
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/execute%20query.png" />

# Installation #
This plugin support ST2 and ST3, firstly, install sublime text and then extract the zip file into your sublime package path.

# Supported Feature: #
+ Muti-project management
+ Apex Code CRUD
+ Apex Code Folder Refresh
+ Run Test Class
+ Apex Code Local History
+ Execute Anonymous
+ Execute Query
+ Sobject Field Completions
+ Visualforce Page Completions
+ Buildin Method Completions
+ Cross View Variable Completions
+ Generate All or Specified Sobject Workbook
+ Generate Custom Field Workbook (Including Field Id)
+ Generate Global Describe Workbook
+ Generate Layout Avaiable PicklistValues
+ Export Validation Rule and Workflow
+ Quick Login to Home Page, Console, Debug Log...
+ Quick View chosen Id in SFDC Web
+ Quick View Apex Code in SFDC Web
+ Backup All or Specified Sobjects in Muti-thread (Very Fast)
+ Many common used snippets
+ Manually Update Plugin

# Dependency Lib #
+ [requests](https://github.com/kennethreitz/requests)
+ [xmltodict](https://github.com/martinblech/xmltodict)
+ [AllViewCompletions](https://github.com/alienhard/SublimeAllAutocomplete/blob/master/all_views_completions.py)

# Notes: #
1. Every time when we refresh all apex code from server, the sobject field completions will be initiated at the same time.

2. When we want to execute anonymous or query, we must choose any valid snippet in sublime and click the command.

3. Actually, retrieve all just retrieve sobject and workflow metadata, because this process is largely time-consuming.

4. Before we want to export validation rule or workflow, we must retrieve all, because we export the validation rule and workflow by parsing the metadata file.

5. Every time we save the apex code, your local copy will be put into project/history path every minute.

6. If we have two classes, the first one of which is the utility class for the second one, it would be best to open the first class so that we can see the variable completions when we edit the first one.

7. When we want to run test, basically, your test result should be displayed as a new view; however, if there is no active view, the new view will not show up, so we should check the result in the console log.

8. If we want to refresh all ApexTrigger, ApexClass, ApexPage or ApexComponent, we just need to click the SublimeApex > Refresh Folder and then choose the folder we want to refresh.

9. Before we update plugin, we should move your customized settings from "Settings - Default" to "Settings - User"

10. This plugin supports ST2 and ST3. ST2 is free generally but ST3 isn't. However, ST2 has many problems compared with ST3 as listed below:
    1. ST2 completions width is fixed; however, ST3 will adjust the completions width by content width.
    2. If there is no active view in the sublime window, we can't create a new view in ST2, but ST3 somethimes can.
    3. Every time, when the plugin is updated, we need to restart sublime in ST2, but there is no need to in ST3.
    4. ST3 console output is very fast, but not in ST2.
    5. UnicodeError may sometimes happen in ST2, but not in ST3.