# Sublime IDE for Salesforce
This plugin supports ```Sublime Text 3``` for windows and OSX, not tested for Linux.

# Installation
You can install this plugin by searching ```haoide``` in package control

# Quick Link
+ <a href="https://github.com/xjsender/haoide/blob/master/HISTORY.rst" target="_blank">Change Logs</a>
+ <a href="https://github.com/xjsender/SublimeApexScreenshot" target="_blank">All Demos</a>
+ <a href="/docs/project.md" target="_blank">Project Configuration</a>
+ <a href="/docs/retrieve.md" target="_blank">Retrieve</a>
+ <a href="/docs/deploy.md" target="_blank">Deploy</a>
+ <a href="/docs/staticresource.md" target="_blank">Static Resource Bundle</a>
+ <a href="/docs/export.md" target="_blank">Export CSV</a>
+ <a href="/docs/utilites.md" target="_blank">Salesforce Utilities</a>
+ <a href="/docs/json2apex.md" target="_blank">Convert JSON to Apex</a>
+ <a href="/docs/rest.md" target="_blank">REST Test</a>
+ <a href="/docs/bulk.md" target="_blank">Bulk API</a>
+ <a href="/docs/document.md" target="_blank">Document Quick Reference</a>
+ <a href="https://github.com/xjsender/SublimeApexScreenshot/raw/master/LightingDevelopment.gif" target="_blank">Lighting Development</a>
+ <a href="https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/Completions.gif" target="_blank">Completions Demo</a>
+ <a href="http://docs.python-requests.org/en/latest/user/advanced/#proxies" target="_blank">Request Proxies</a>

## Execute Query
After any snippet which start with SELECT is chosen, you can press <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Q</kbd> in windows or click ```HaoIDE``` > ```Execute Query```, the queried json result will be formated and shown in a new view.

## Keep Operation History
By default, the operation of ```Execute Query```, ```Describe sObject```, ```Gernate SOQL```, ```Execute Anonymous``` and ```Run Test``` will be kept into the ```.history``` path in current project, you can disable this feature by setting ```keep_operation_history``` to false

## Difference between Deploy to Server and Save to Server
* ```Deploy to Server``` use ```Metdata API``, which can be mainly used to deploy files to other different orgs.
* ```Save to Server``` use ```tooling API```, which can't be used in production org.

## Save component
+ This command is only enabled in salesforce code file of active project
+ After code is updated, click ```HaoIDE``` > ```Save to Server``` in the context menu or press <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>S</kbd>
+ If the saving process failed, the console will be open and automatically hidden in **10** seconds, if you think **10** seconds is not enough to check the error message, you add it up to more by setting ```delay_seconds_for_hidden_output_panel_when_failed```

This command just supports ```ApexClass```, ```ApexPage```, ```ApexComponent``` and ```ApexTrigger```, not support ```StaticResource```, if you want to use it to update static resource, you should use ```Deploy to Server``` to see ```[Update StaticResource](#update-static-resource)``` Part in this page

## Save multiple components
Select the files in the sidebar, click ``haoide`` > ``Deploy Files to Server`` in the sidebar menu.

## Save file to other org
- Select the files in the sidebar, click ``haoide`` > ``Deploy Files to Server`` in the sidebar menu
- Open the file to save, click ``haoide`` > ``Deploy to Server`` in the context menu

## Refresh component
+ This command is only enabled in salesforce code file of active project
+ After code is updated in UI or other IDE, press <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>R</kbd> or click ```HaoIDE``` > ```Refresh From Server``` to refresh it from server.

## Delete component
+ This command is only enabled in salesforce code file
+ If you want to delete it from server, click ```HaoIDE``` > ```Delete From Server```

## New ApexClass
Click ```HaoIDE``` > ```New``` > ```New ApexClass```, choose the predefined template, and then input the class name in the input panel at the bottom, after that, your class will be created.

## New ApexPage
Click ```HaoIDE``` > ```New``` > ```New ApexPage```, and then input the page name in the input panel at the bottom, after that, your page will be created.

After you input # after extension or controller name in visualforce page, plugin will create it for you automatically, see [demo](https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/QuickController.gif)

## New ApexComponent
Click ```HaoIDE``` > ```New``` > ```New ApexComponent```, and then input the component name in the input panel at the bottom, after that, your component will be created.

## New ApexTrigger
Click ```HaoIDE``` > ```New``` > ```New ApexTrigger```, choose the sobject on which you will create trigger, and then input the trigger name in the input panel at the bottom, after that, your trigger will be created.

## Create Debug Log
If you want to track the log of any user, click ```HaoIDE``` > ```Debug``` > ```Track Debug Log```, wait for a moment, you will see the user list, choose one and press enter, check the progress in the status bar until succeed message appeared, and then your debug log user is recorded.

If you just want to track debug log of yourself, you can click click ```HaoIDE``` > ```Debug``` > ```Track Self Debug Log```.

There is a default ```trace_flag``` settings that is used to define the debug log level in the default settings, you can put your own change into your user settings.

## Fetch Debug Log
If you want to see the log list of any user, click ```HaoIDE``` > ```Apex Test``` > ```Fetch Debug Logs```, wait for a moment, you will see the user list, choose one and press <kbd>enter</kbd>, check the progress in the status bar until succeed message appeared, and then a new view with the log list will be open.

You can choose the ```Log Id``` and click ```HaoIDE``` > ```View Debug Log In Sublime``` command in the context menu, wait for the end of the progress on the status bar, after it is finished, a new view with the log detail will be opened.

Or, you can choose any Log Id and click ```HaoIDE``` > ```View Id In Salesforce Web```, wait for a moment, browser will be open and redirect to the log detail page.

## View Debug Log Detail
Put the focus in the ```Log Id```, press <kbd>alt</kbd> and click left button, the debug log detail will be retrieved and displayed in the new view.

## Run Test
There are two methods to run test, one is by Main Menu, other is in the context menu
By Main Menu: click ```HaoIDE``` > ```Debug``` > ```Run Test```, choose the test class and press <kbd>enter</kbd>, check the progress in the status bar until succeed message appeared, and then a new view with the test result will be open.
By Context Menu: in the context of opened class, click ```HaoIDE``` > ```Run Test Class```, check the progress in the status bar until succeed message appeared, and then a new view with the test result will be open.

## View Code Coverage
This feature just works when api version is >= 29.0
In the context menu of open class or trigger, click ```HaoIDE``` > ```View Code Coverage``` in the context menu, ait for the end of the progress on the status bar, you will see the code coverage percentage in the console and a new view with not covered highlight lines.

Put the focus in the ApexClass Name, press ```alt``` and click left button for twice, the code coverage of specified class will be retrieved and displayed in the new view.

## Keep Apex Code Local History
When you save code, this plugin will keep the change after you saved it to server successfully.

You can close this feature by change ```keep_local_history_change``` settings to false and put it into your own ``user settings``

## Refresh Folder
Choose the folders in the side bar and refresh them by click ```haoide > Refresh Folder`` in the sidebar menu

## Refresh Multiply Components
Choose the components you want to refresh, and then Click ```HaoIDE``` > ```Refresh Selected Components``` in the Sidebar Menu

## Delete Multiply Components
Choose the components you want to delete, and then Click ```HaoIDE``` > ```Delete Selected Components``` in the Sidebar Menu

## Quick Goto Component
Put the focus in the Class Name, and then, press <kbd>shift</kbd>,  and click ```button1``` for twice, the class file will be open in background if this class file is exist, however, if you want to open this class in the foreground, you should press <kbd>shift</kbd> and click ```button1``` for triple.

# Build-in Dependency Lib
+ [requests](https://github.com/kennethreitz/requests)
+ [xmltodict](https://github.com/martinblech/xmltodict)
+ [dateutil](http://labix.org/python-dateutil/)
+ [xmlformatter](https://pypi.python.org/pypi/xmlformatter/)
