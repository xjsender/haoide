# Sublime IDE for Salesforce
This plugin supports ```Sublime Text 3``` for windows and OSX, not tested for Linux.

# Change Logs
    - See [History](https://github.com/xjsender/haoide/blob/master/HISTORY.rst)

# Demo
    - [Demo is here](https://github.com/xjsender/SublimeApexScreenshot)

# Installation
You can install this plugin by searching ```haoide``` in package control

# Project Configuration
## Worspace
If your operation system is **OSX**, you should change the workspace in ```HaoIDE``` > ```Setting``` > ```Setting - User``` to your own, if you didn't do that, plugin will save the project to ```<packages_path>/User/HaoIDE```, 

There are two tiers of workspace concept in this plugin, including plugin level workspace and project level workspace, the privilege level of project level is higher than the plugin level workspace, if you didn't define the workspace in the project property of ```projects``` setting, plugin will set your plugin level workspace to the default workspace, for example, if the settings is set as below:

```javascript
{
    // Workspace in OSX is different with windows, 
    // workspace can be "/Users/<Your User>/salesforce/workspace"
    "workspace": "c:/salesforce/workspace1",
    "projects": {
        "pro-exercise": {
            "default": true,
            "login_url": "https://login.salesforce.com",
            "password": "******",
            "username": "mouse@exercise.com",
            "workspace": "c:/salesforce/workspace2",
        }
    }
}
```

Your plugin level workspace is ```c:/salesforce/workspace1```, your project level workspace is ```c:/salesforce/workspace2```, because you have defined your project level workspace, so the default workspace of ```pro-exercise``` project is ```c:/salesforce/workspace2```, however, if the settings is set as below,

```javascript
{
    // Workspace in OSX is different with windows, 
    // workspace can be "/Users/<Your User>/salesforce/workspace"
    "workspace": "c:/salesforce/workspace1",
    "projects": {
        "pro-exercise": {
            "default": true,
            "login_url": "https://login.salesforce.com",
            "password": "******",
            "username": "mouse@exercise.com",
            "workspace": "c:/salesforce/workspace2",
        },

        "sandbox-exercise": {
            "default": true,
            "login_url": "https://login.salesforce.com",
            "password": "******",
            "username": "mouse@exercise.com"
        }
    }
}
```

Your plugin level workspace is ```c:/salesforce/workspace1```, because ```pro-exercise``` has its own workspace and ```sandbox-exercise``` doesn't have, so, the workspace of ```pro-exercise``` is ```c:/salesforce/workspace2```, the workspace of ```sandbox-exercise``` is ```c:/salesforce/workspace1```


## Projects
There is a default test org in this plugin, you can see it by clicking ```HaoIDE``` > ```Switch Project``` in the main menu, however, if you want to use this plugin in your own org, you need to configure your org user confidential before new project.

In order to prevent plugin update overriding your settings, you should keep your customize settings into ```Setting - User``` by clicking ```HaoIDE``` > ```Settings``` > ```Setting - User```.

You can setup your projects follow below sample by clicking ```HaoIDE``` > ```Settings``` > ```Setting - User``` in the main menu, projects must be included in {}.

When you initiate your settings, you can have more than one project in "projects", however, only one project default should be true.

If your own org login need security token, just set it as sample.

Every time you want to switch the project, you can click ```HaoIDE``` > ```Switch Project``` in the main menu and choose that you want, and then the updated projects settings will be saved to user settings.

If you want to check the current active project, you can check the most left of side bar or press <kbd>ALT</kbd>+<kbd>S</kbd>

After your project configuration is finished, you can click ```HaoIDE``` > ```New``` > ```new project``` in the main menu to download your code.
```javascript
{
    // In OSX, the worspace path is different with windows,
    // for example, workspace in OSX could be "/Users/<Your User>/salesforce/workspace"
    "workspace": "d:/ForcedotcomWorkspace",
    "projects": {
        "Project1 Name": {
            "default": true,
            "login_url": "https://test.salesforce.com",
            "password": "a",
            "username": "a@a.com",

            // If you have security token, just put it here
            "security_token": "12sad3223adfas",

            // Allowed Package Names, for example, twitter, weibo etc.
            "allowed_packages": []
        },
        "Project2 Name": {
            "default": false,
            "login_url": "https://test.salesforce.com",
            "password": "b",
            "username": "b@b.com"
        }
        ......
    }
}
```


## New Project
+ This command is used to create new project
+ Once you click this command, a new project will be downloaded and appeared in the sidebar
+ Just after new project is finished, sobject completions will work
+ Project Folder Name Convention: the project name set in user settings append with date literal of today, for example,
if today is ```2013/07/30``` and user settings is 

```javascript
{
    // Workspace in OSX is different with windows, 
    // workspace can be "/Users/<Your User>/salesforce/workspace"
    "workspace": "c:/ForcedotcomWorkspace",
    "projects": {
        "Exercise-Pro": {
            "default": true,
            "login_url": "https://login.salesforce.com",
            "password": "******",
            "username": "mouse@exercise.com"
        }
    }
}
```
your project folder name should be ```Exercise-Pro-20130730```, you can close this time suffix feature by setting ```keep_project_name_time_suffix``` to false

**If you are developing a package, you need to add your package namespace to settings ``allowed_packages``, more detail to check the ``allowed_packages`` in the default settings**

## Update Project
You can click ```haoide > Update > Update Project``` in the main menu or press <kbd>Alt</kbd>+<kbd>R</kbd> to update your active project.

## Completions:
    - [Completions Demo](https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/Completions.gif)

## Execute Anonymous
Choose any apex code snippet, press <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>E</kbd> or click ```HaoIDE``` > ```Execute Anonymous```, you will see the result, you should be aware, if anonymous code compile is failed, message will be shown in output panel, just after compile succeed, the executed result will be shown in the new view.

There has a ```log_levels``` setting in the default setting, If you want to change anonymous log levels, you can put your log levels settings into your user setting.

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

## Salesforce Document Quick Reference
    - See <a href="/documentreference.md" target="_blank">Document Quick Reference</a>

## Refresh Multiply Components
Choose the components you want to refresh, and then Click ```HaoIDE``` > ```Refresh Selected Components``` in the Sidebar Menu

## Delete Multiply Components
Choose the components you want to delete, and then Click ```HaoIDE``` > ```Delete Selected Components``` in the Sidebar Menu

## Quick Goto Component
Put the focus in the Class Name, and then, press <kbd>shift</kbd>,  and click ```button1``` for twice, the class file will be open in background if this class file is exist, however, if you want to open this class in the foreground, you should press <kbd>shift</kbd> and click ```button1``` for triple.

## Retrieve All Metadata
Click ```HaoIDE``` > ```Metadata Migration``` > ```Retrieve All``` in the main menu, you will see a new open view with message, this view will be refreshed every five seconds, after the retrieve status is completed, plug-in will download the base64 zipfile, after that, base64 zipfile will be decoded to zip file, at the last, this zip file will be extracted.

**This feature is not good enough, because there is no listPackage feature supported, for example, report and dashboard can't be retrieve if no detail folder/report is specified in package.xml**

## Retrieve Package.xml
With this feature, plugin can retrieve the metadata by package.xml from the default project, if package.xml parse failed, error will be shown in the output panel.

You can retrieve package.xml by below two ways,

* By Sidebar Menu
    - Choose a package file, which name should be end with ```.xml```
    - Execute ```HaoIDE > Retrieve Package.xml``` command in the sidebar menu
    - You will need to input the output path for retrieved result, which has a default value same with the path of current package.xml, after input the output path and click <kbd>Enter</kbd>, retrieve will start
    - After retrieve is finished, you will see the retrieved package in your input path

* By Context Menu
    - Open a package file, which name should be end with ```.xml```
    - Execute ```HaoIDE > Retrieve Package.xml``` command in the context menu
    - You will need to input the output path for retrieved result, which has a default value same with the path of current package.xml, after input the output path and click <kbd>Enter</kbd>, retrieve will start
    - After retrieve is finished, you will see the retrieved package in your input path

## Update Static Resource
With this feature, you can directly edit static zip resource, there are several steps to do it,

* Choose the static zip resource that you need to update in the ```staticresources``` folder

* Click ``HaoIDE`` > ``Extract To Here`` to extract it to ``sub folder`` of ``staticresources``, which name is same with the static resource.
    - ``Extract To Here`` command can extract all kinds of zip resource, no matter what extension of the file.
    - If file is not zip resource, error message will be shown in the output panel

* After you made change on the file in the sub folder, choose the name of ``sub folder`` and click ``HaoIDE`` > ``Update StaticResource`` in the sidebar menu to save it to server.

* [UpdateStaticResource Demo](https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/UpdateStaticResource.gif)

## Deploy
There has a setting ``switch_back_after_migration`` to control whether switch back to original project after deploy is finished, default value is ``true``

* Deploy Package Zip, [demo](https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/DeployZip.gif) is here
    - Click ```HaoIDE``` > ```Metadata Migration``` > ```Deploy Package.zip``` in the main menu
    - Input your zip file path and click <kbd>Enter</kbd>
    - Waiting and checking the progress message in the output panel
    - After operation is finished, you will see the deploy result

* Deploy Files to Server
    - Choose the file to deploy
    - Click ```HaoIDE``` > ```Deploy File to Server``` in the context menu
    - Waiting and checking the progress message in the output panel
    - After operation is finished, you will see the deploy result

* Deploy Open Files
    - Sometimes, when you want to deploy class, page or somethings else, however, you didn't want to choose them in the sidebar when there are huge number of code files, you can open the files that you want to deploy to server and Click ```HaoIDE``` > ```Metadata Migration``` > ```Deploy Open Files``` in the main menu to deploy multiply files to target server. 

    - Actually, you can even open code files in different orgs and deploy them to the same org, for example, there have three classes to be deployed, A and B are in UAT environment and they are newly developed feature, C in UAT environment is completely different with production environment and there is urgent bug needed to be fixed in production, so at this moment, you can open A and B classes in UAT and the fixed version of C class in production and click ```Deploy Open Files``` to deploy the three class from different orgs to production environment.

    - This command is just enabled when any one of open files is salesforce code files.

* Deploy Package Folder, [demo](https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/DeployPackageFolder.gif) is here
    - Choose a valid package folder, for example, ``src`` folder or ``Project/src``, plugin will check whether ``src`` folder contains ``package.xml`` file, if yes, you will ``Deploy To Server`` command in the sidebar menu, otherwise, ``Deploy To Server`` will be hidden
    - Click the ```Deploy To Server`` command
    - Waiting and checking the progress message in the output panel
    - After operation is finished, you will see the deploy result

## Export
You can export somethings in your org to CSV by these features

* Export CustomFields
    - Click ```HaoIDE``` > ```Export``` > ```Export CustomField```
    - ``CustomFields`` will be exported to ``Project/.export/CustomFields.csv``

* Export Workflow Rules
    - Download metadata of ``sObjects and Workflow`` by clicking ```Migration``` > ```Retrieve Sobject And Workflow``` in the main menu
    - Click ```Export``` > ```Export Workflow``` in the main menu to backup all workflows in your org to csv
    - ```workflow_rule_columns```, ``workflow_field_update_columns``, ``workflow_email_alert_columns``, ``workflow_outbound_message_columns`` and ``workflow_task_columns`` defines the columns of export CSV, you can adjust the sequence and columns by customizing your own value of this five settings

* Export Validation Rules
    - Download metadata of ``sObjects and Workflow`` by clicking ```Migration``` > ```Retrieve Sobject And Workflow``` in the main menu
    - Click ```Export``` > ```Export Validation Rule``` in the main menu
    - All ValidationRules in your org will be exported to ``Project/.export/ValidationRules.csv``
    - ```validation_rule_columns``` setting defines the columns of export CSV, you can adjust the sequence and columns by customizing your own value of this setting

* Export Profile Workbook
    - Retrieve all metadata by clicking ``Metadata Migration`` > ``Retrieve All`` in the main menu to download all related components.
    - Click ``HaoIDE`` > ``Export`` > ``Export Profile`` in the main menu to export ``ObjectPermission``, ``TabVisibilities``, ``FieldLevelSecurity`` and ``UserPermissions`` of all profiles to four different CSV files, you can check below sample CSVs.
    - Exported profile csv from sample org
        + [FieldLevelSecurity.csv](https://github.com/xjsender/SublimeApexScreenshot/blob/master/CSV/Profile/FieldLevelSecurity.csv)
        + [ObjectPermissions.csv](https://github.com/xjsender/SublimeApexScreenshot/blob/master/CSV/Profile/ObjectPermissions.csv)
        + [TabVisibilities.csv](https://github.com/xjsender/SublimeApexScreenshot/blob/master/CSV/Profile/TabVisibilities.csv)
        + [UserPermissions.csv](https://github.com/xjsender/SublimeApexScreenshot/blob/master/CSV/Profile/UserPermissions.csv)

* Export Workbook of sobjects
    - Click ``Export`` > ``Export Workbook`` in the main menu
    - Input * to export all sObject workbooks
    - Input sObject Names separated with semi-colon to export some
    - ``workbook_field_describe_columns`` setting define the columns

* Export Data Template
    - Click ``Export`` > ``Export Data Template`` in the main menu
    - Waiting until ``sObject => RecordType`` quick panel is open
    - Choose one and press <kbd>Enter</kbd> and template will be exported
    - From the row 1 to row 6, they are,
        + [Field Label]...
        + [Field API]...
        + [Field Type]...
        + [Layout Required]...
        + [Picklist Label if has]...
        + [Picklist Value if has]


## Utilities
There are some utilities to keep your work efficient as below

* Convert 15Id to 18Id
    - Click ```Utilities``` > ```Convert 15Id to 18Id``` in the main menu
    - to convert your input 15Id to 18Id, if your input is not valid 15Id, it will be returned as original value

* Describe sObject
    - Click ```Utilities``` > ```Describe sObect``` in the main menu
    - Choose a sObject in the quick panel and press <kbd>Enter</kbd>
    - The describe result will appear in the new view

* Generate sObject SOQL
    - Click ```Utilities``` > ```Generate sObject SOQL``` in the main menu
    - Choose a sObject in the quick panel and press <kbd>Enter</kbd>
    - The sObject SOQL will appear in the new view

* Pretty JSON
    - Click ```Utilities``` > ```JSON Pretty``` in the main menu
    - Input your JSON Body in the input panel and press <kbd>Enter</kbd>
    - The Prettied JSON will appear in the new view

* Serialize JSON
    - Click ```Utilities``` > ```JSON Serialization``` in the main menu
    - Input your JSON Body in the input panel and press <kbd>Enter</kbd>
    - The Serialized JSON will appear in the new view

* Convert JSON to Apex
    - See <a href="/json2apex.md" target="_blank">Convert JSON to Apex</a>

## Lighting Component Development
    - [lighting component demo](https://github.com/xjsender/SublimeApexScreenshot/raw/master/LightingDevelopment.gif)

## Exceute REST Test
    - See <a href="/rest.md" target="_blank">REST Test</a>

## Bulk Api
    - See <a href="/bulk.md" target="_blank">Bulk API</a>

## Proxy
    - [Request Proxies](http://docs.python-requests.org/en/latest/user/advanced/#proxies)

# Build-in Dependency Lib
+ [requests](https://github.com/kennethreitz/requests)
+ [xmltodict](https://github.com/martinblech/xmltodict)
+ [dateutil](http://labix.org/python-dateutil/)
+ [xmlformatter](https://pypi.python.org/pypi/xmlformatter/)
