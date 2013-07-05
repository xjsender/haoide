# Installation #
This plugin support ST2 and ST3, firstly, install sublime text and then extract the zip file into your sublime package path.

# Supported Feature: #
+ Apex Code CRUD
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