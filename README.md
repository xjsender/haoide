# Sceenshot #
This plugin support ST2 and ST3, firstly, install sublime text and then extract the zip file into your sublime package path.
###1. Sobject Field Completions
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/Apex%20code%20completions.png" />

###2. Apex Code Completions
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/sobject%20field%20completions.png" />

# Installation #
This plugin support ST2 and ST3, firstly, install sublime text and then extract the zip file into your sublime package path.

# Supported Feature: #
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
1. Every time when you refresh all apex code from server, you sobject field completions will be initiated at the same time.

2. When you want to execute anonymous or query, you must choose any valid snippet in sublime and click the command.

3. Actually, retrieve all just retrieve sobject and workflow metadata, because this process is largely consuming time.

4. Before you want to export validation rule or workflow, you must retrieve all, because we export the validation rule and workflow by parsing the metadata file.

5. Every time when you save the apex code, your local copy will be put into project/history path every minute.

6. If you have two classes, the first one is the utility class of the second one, you'd better open the first class, and then you can see the variable completions when you edit the first one.

7. When you run test, basically, you test result should be displayed as a new view, however, if there is no active view, the new view will not show up, so you should check the result in the console log.

8. If you want to refresh all ApexTrigger, ApexClass, ApexPage or ApexComponent, you just need to click the SublimeApex > Refresh Folder and then choose the folder you want to refresh.

9. Before you update plugin, you should move your customized settings in "Settings - Default" to "Settings - User"

10. This plugin supports ST2 and ST3, ST2 is free generally but ST3 not, however, ST2 has much problem compared with ST3, list as below,
    1. ST2 completions width is fixed, however, ST3 will adjust the completions width by content width.
    2. If no active view in the sublime window, we can't create new view in ST2 but ST3 somethimes can.
    3. Everytime, when plugin is updated, we need to restart sublime in ST2 but no need in ST3
    4. ST3 console output is very fast but not in ST2.
    5. UnicodeError may happen in ST2 sometimes but not in ST3.