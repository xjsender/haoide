# Sublime IDE for salesforce
This plugin supports ```Sublime Text 3``` for windows and OSX (**MUST Change the default Workspace for OSX**, otherwise, the downloaded code will not appeared in the sidebar), not tested for Linux.
**If you think this plugin is helpful, please star this plugin.**

# Change Logs
See [History](https://github.com/xjsender/SublimeApex/blob/master/HISTORY.rst)

# Demo
+ [Install Plugin](https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/InstallPackage.gif) 
+ [Completions](https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/Completions.gif)
+ [Trigger](https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/Trigger.gif)
+ [Visualforce Page](https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/html.gif)
+ [Execute Rest Test](https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/Execute%20Rest%20Test.gif)
+ [Document Reference](https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/DocumentReference.gif)
+ [Export Workbooks](https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/ExportWorkbooks.gif)
+ [Export Workflow](https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/ExportWorkflow.gif)
+ [Retrieve Package.xml](https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/RetrievePackage.gif)
+ [Deploy Package.zip](https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/DeployZip.gif)
+ [Deploy Package Folder](https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/DeployPackageFolder.gif)

# Installation
This plugin is hosted on [package control](https://sublime.wbond.net/packages/Salesforce%20IDE), after you [installed the package control](https://sublime.wbond.net/installation#st3), you can install this plugin by searching ```Salesforce IDE``` in package control

# Project Configuration
If your operation system is **OSX**, you must set the workspace in ```SublimeApex``` > ```Setting``` > ```Setting - User```.

There is a default test org in this plugin, you can see it by clicking ```SublimeApex``` > ```Switch Project``` in the main menu, however, if you want to use this plugin in your own org, you need to configure your org user confidential before new project.

In order to prevent plugin update overriding your settings, you should keep your customize settings into ```Setting - User``` by clicking ```SublimeApex``` > ```Settings``` > ```Setting - User```.

You can setup your projects follow below sample by clicking ```SublimeApex``` > ```Settings``` > ```Setting - User``` in the main menu, projects must be included in {}.

When you initiate your settings, you can have more than one project in "projects", however, only one project default should be true.

If your own org login need security token, just set it as sample.

Every time you want to switch the project, you can click ```SublimeApex``` > ```Switch Project``` in the main menu and choose that you want, and then the updated projects settings will be saved to user settings.

If you want to check the current active project, you can check the most left of side bar or press <kbd>ALT</kbd>+<kbd>S</kbd>

After your project configuration is finished, you can click ```SublimeApex``` > ```New``` > ```new project``` in the main menu to download your code.
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
            "security_token": "12sad3223adfas"
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

# Usage
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
    "workspace": "d:/ForcedotcomWorkspace",
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
You can click ```SublimeApex > Update > Update Project``` in the main menu or press <kbd>Alt</kbd>+<kbd>R</kbd> to update your active project.

## Completions:
+ Standard Class Completion
+ sObject Fields Completion and sObject Relationship Completion
+ Relationship Fields Completion
+ Custom Class Completion
+ Input any Character, Show All Standard sObject, Custom sObject, Standard Class and Custom Class
+ After input ``Page.``, list all custom visualforce page
+ Picklist Value Completion
+ SOQL Fields Completion
+ Standard Visualforce Component and Custom Visualforce Component Completion
+ HTML Elements Completion
+ HTML and Visualforce Component Attribute Completion
+ HTML and Visualforce Component Attribute Value Completion

## Execute Anonymous
Choose any apex code snippet, press <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>E</kbd> or click ```SublimeApex``` > ```Execute Anonymous```, the executed result will be shown in a new view.

There has a ```log_levels``` setting in the default setting, If you want to change anonymous log levels, you can put your log levels settings into your user setting.

**If your chosen code snippet contains non-english word, there will have problem.**

## Execute Query
After any snippet which start with SELECT is chosen, you can press <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Q</kbd> in windows or click ```SublimeApex``` > ```Execute Query```, the queried json result will be formated and shown in a new view.

## Describe Sobject
Click ```SublimeApex``` > ```Describe``` > ```sObect``` and then choose a sObject in the selection panel, the describe result will appear in the new view

## Generate SOQL
Click ```SublimeApex``` > ```Describe``` > ```sObject SOQL``` and then choose a sObject in the selection panel, the sObject SOQL will appear in the new view

## Keep Operation History
By default, the operation of ```Execute Query```, ```Describe sObject```, ```Gernate SOQL```, ```Execute Anonymous``` and ```Run Test``` will be kept into the ```.history``` path in current project, you can disable this feature by setting ```keep_operation_history``` to false

## Save component
+ This command is only enabled in salesforce code file of active project
+ After code is updated, click ```SublimeApex``` > ```Save to Server``` in the context menu or press <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>S</kbd>
+ If the saving process failed, the console will be open and automatically hidden in **10** seconds, if you think **10** seconds is not enough to check the error message, you add it up to more by setting ```delay_seconds_for_hidden_output_panel_when_failed```

## Refresh component
+ This command is only enabled in salesforce code file of active project
+ After code is updated in UI or other IDE, press <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>R</kbd> or click ```SublimeApex``` > ```Refresh From Server``` to refresh it from server.

## Delete component
+ This command is only enabled in salesforce code file
+ If you want to delete it from server, click ```SublimeApex``` > ```Delete From Server```

## New ApexClass
Click ```SublimeApex``` > ```New``` > ```New ApexClass```, choose the predefined template, and then input the class name in the input panel at the bottom, after that, your class will be created.

## New ApexPage
Click ```SublimeApex``` > ```New``` > ```New ApexPage```, and then input the page name in the input panel at the bottom, after that, your page will be created.

## New ApexComponent
Click ```SublimeApex``` > ```New``` > ```New ApexComponent```, and then input the component name in the input panel at the bottom, after that, your component will be created.

## New ApexTrigger
Click ```SublimeApex``` > ```New``` > ```New ApexTrigger```, choose the sobject on which you will create trigger, and then input the trigger name in the input panel at the bottom, after that, your trigger will be created.

## Create Debug Log
If you want to track the log of any user, click ```SublimeApex``` > ```Debug``` > ```Create Debug Log```, wait for a moment, you will see the user list, choose one and press enter, check the progress in the status bar until succeed message appeared, and then your debug log user is recorded.

There is a default ```trace_flag``` settings that is used to define the debug log level in the default settings, you can put your own change into your user settings

## List Debug Log
If you want to see the log list of any user, click ```SublimeApex``` > ```Apex Test``` > ```List Debug Logs```, wait for a moment, you will see the user list, choose one and press <kbd>enter</kbd>, check the progress in the status bar until succeed message appeared, and then a new view with the log list will be open.

You can choose the ```Log Id``` and click ```SublimeApex``` > ```View Debug Log In Sublime``` command in the context menu, wait for the end of the progress on the status bar, after it is finished, a new view with the log detail will be opened.

Or, you can choose any Log Id and click ```SublimeApex``` > ```View Id In Salesforce Web```, wait for a moment, browser will be open and redirect to the log detail page.

## View Debug Log Detail
Put the focus in the ```Log Id```, press ```alt``` and click left button, the debug log detail will be retrieved and displayed in the new view.

## Run Test
There are two methods to run test, one is by Main Menu, other is in the context menu
By Main Menu: click ```SublimeApex``` > ```Debug``` > ```Run Test```, choose the test class and press <kbd>enter</kbd>, check the progress in the status bar until succeed message appeared, and then a new view with the test result will be open.
By Context Menu: in the context of opened class, click ```SublimeApex``` > ```Run Test Class```, check the progress in the status bar until succeed message appeared, and then a new view with the test result will be open.

## View Code Coverage
This feature just works when api version is >= 29.0
In the context menu of open class or trigger, click ```SublimeApex``` > ```View Code Coverage``` in the context menu, ait for the end of the progress on the status bar, you will see the code coverage percentage in the console and a new view with not covered highlight lines.

Put the focus in the ApexClass Name, press ```alt``` and click left button for twice, the code coverage of specified class will be retrieved and displayed in the new view.

## Keep Apex Code Local History
When you save code, this plugin will keep the change after you saved it to server successfully.

You can close this feature by change ```keep_local_history_change``` settings to false and put it into your own ``user settings``

## Refresh Folder
Click the folder in the side bar, refresh that you want to refresh, if you choose the classes folder, the ```Refresh ApexClass``` command will be visible, ```ApexTrigger```, ```ApexComponent```, ```ApexPage``` and ```StaticResource``` is same.

## Salesforce Document Quick Reference
I get the idea idea from [Salesforce Referencee](https://github.com/Oblongmana/sublime-salesforce-reference) and added some feature based on it.

Click the ```SublimeApex``` > ```Document``` > ```Reload Salesforce Reference``` in the main menu, you need to confirm whether continue, after you confirmed it, then wait for a moment until the ```Open Document``` command is enabled, at this moment, you can press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>O</kbd> or Click it to invoke the ```Open Document``` command, nearly all reference api will be shown in the list, you can try to choose any one and it will be opened in browser.

There is default ```docs``` settings, if you want to add some other document reference to here, you can customize it yourself.
```
"docs": {
    "apexcode": {
       "catalog": "Apex",
       "pattern": "*[@Title='Reference'].//TocEntry[@DescendantCount='0'].."
    },
    ...
},
```
+ **apexdoc**: the part in ```http://www.salesforce.com/us/developer/docs/apexdoc/Data/Toc.xml```, you can get the ```apexdoc``` from Salesforce documents link
+ **Apex**: the document prefix in the quick search panel
+ **pattern**: the XPath pattern for parse the content from the response

**You should be aware that every reloading is time-consuming, generally, you should reload it in every salesforce release**

## Refresh Multiply Components
Choose the components you want to refresh, and then Click ```SublimeApex``` > ```Refresh Selected Components``` in the Sidebar Menu

## Delete Multiply Components
Choose the components you want to delete, and then Click ```SublimeApex``` > ```Delete Selected Components``` in the Sidebar Menu

## Quick Goto Component
Put the focus in the Class Name, and then, press <kbd>shift</kbd>,  and click ```button1``` for twice, the class file will be open in background if this class file is exist, however, if you want to open this class in the foreground, you should press <kbd>shift</kbd> and click ```button1``` for triple.

## Retrieve All Metadata
Click ```SublimeApex``` > ```Migration``` > ```Retrieve Metadata``` in the main menu, you will see a new open view with message, this view will be refreshed every five seconds, after the retrieve status is completed, plug-in will download the base64 zipfile, after that, base64 zipfile will be decoded to zip file, at the last, this zip file will be extracted.

## Retrieve Package.xml
Click ```SublimeApex``` > ```Migration``` > ```Retrieve Package.xml``` in the main menu, input your package file path, after that, you will see the effect.

see [Retrieve Package.xml Demo](https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/RetrievePackage.gif)

## Deploy Package Zip
Click ```SublimeApex``` > ```Migration``` > ```Retrieve Metadata``` in the main menu, input your zip file path, after that, you will see the effect.

see [Deploy Package Demo](https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/DeployZip.gif)

## Deploy Package Folder
Choose a valid package folder, click right button, check if the ```Deploy to Server``` command is enabled, if yes, it means the package folder is valid, and then click the ```Deploy To Server`` command, you will see the effect.

**This feature is in beta now, Default Deploy checkOnly is true, need more detail? please check the deploy_options settings in default settings**

see [Deploy Package Folder](https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/DeployPackageFolder.gif)

## Export Workflow Rules
After you downloaded all metadata by clicking ```SublimeApex``` > ```Migration``` > ```Retrieve Metadata```, you can click ```SublimeApex``` > ```Export``` > ```Export Workflow``` to backup all workflows in your org to csv.

If you just want to export some attributes of workflows, you can remove some columns in the ```workflow_rule_columns```, ``workflow_field_update_columns``, ``workflow_email_alert_columns``, ``workflow_outbound_message_columns`` and ``workflow_task_columns`` settings and put it into your own user settings.

## Export Validation Rules
After you downloaded all metadata by clicking ```SublimeApex``` > ```Migration``` > ```Retrieve Metadata```, you can click ```SublimeApex``` > ```Export``` > ```Export Validation Rule``` to backup all validation rules in your org to csv.

If you just want to export some attributes of validation rules, you can remove some columns in the ```validation_rule_columns``` setting and put it into your own user settings

## Export CustomFields
You can click ```SublimeApex``` > ```Export``` > ```Export CustomFields``` to export all custom fields in your org to csv.

## Export Workbook of sobjects
You can click ```SublimeApex``` > ```Export``` > ```Export Workbook``` to export all sobject workbooks in your org to csv.

If you just want to export some attributes of sobject workbook, you can remove some columns in the ```workbook_field_describe_columns``` setting and put it into your own user settings

## Exceute Rest Test
Up to now, support ```Get```, ```Post```, ```Put```, ```Patch```, ```Delete```, ```Tooling Query```, ```Query```, ```Query All```, ```Head```, ```Retrieve Body```, ```Search``` and ```Quick Search``` methods.

for example, 

+ **Query Sample**, you can input ```SELECT Id, Name FROM Account LIMIT 1``` and choose it, choose the intput SOQL, and then click ```Execute Rest Test``` in the context menu, choose the ```Query``` in the popup menu, wait for a moment, the queried json result will be shown in the new view.
```
{
    'done': True,
    'records': [{
        'Id': '001O000000M1mPwIAJ',
        'Name': '周星驰',
        'attributes': {
            'type': 'Account',
            'url': '/services/data/v30.0/sobjects/Account/001O000000M1mPwIAJ'
        }
    }],
    'totalSize': 1
}
```

+ **Query With Wildcard Character***, you can input ```SELECT * FROM Account LIMIT 1``` and choose it, choose the intput SOQL, and then click ```Execute Rest Test``` in the context menu, choose the ```Query``` in the popup menu, wait for a moment, the queried json result will be shown in the new view.
```
{
    'done': True,
    'records': [{
        'Id': '001O000000M1mPwIAJ',
        'Name': '周星驰',
        ....
        'attributes': {
            'type': 'Account',
            'url': '/services/data/v30.0/sobjects/Account/001O000000M1mPwIAJ'
        }
    }],
    'totalSize': 1
}
```

+ **Tooling Query Sample**, you can input ```SELECT Id, Name FROM ApexClass``` and choose it, choose the intput SOQL, and then click ```Execute Rest Test``` in the context menu, choose the ```Tooling Query``` in the popup menu, wait for a moment, the queried json result will be shown in the new view.

+ **Post Sample**: you can input ```/sobjects/Account``` and choose it, click ```Execute Rest Test``` in the context menu, choose the ```Post``` in the popup menu and input the json ```{"Name": "Test Rest Test"}``` in the input panel, wait for a moment, the inserted new account will be shown in the new view.
```
{
    'errors': [],
    'id': '001O000000MIiSXIA1'
}
```

+ **Get Sample**: input ```/sobjects/Account/001O000000MIiSXIA1``` and choose it, click ```Execute Rest Test``` in the context menu, choose the ```Get``` in the popup menu, wait for a moment, the detail information of the specified Id will be shown in the new view:
```
{
    'BillingAddress': {
        'city': None,
        'country': 'United States',
        ...
    },
    'BillingCity': None,
    'BillingCountry': 'United States',
    'BillingCountryCode': 'US',
    ...
}
```

+ **Delete Sample**: input ```/sobjects/Account/001O000000MIiSXIA1``` and choose it, click ```Execute Rest Test``` in the context menu, choose the ```Delete``` in the popup menu, wait for a moment, the delete result will be shown in the new view:
```
{

}
```

+ **Patch Sample**: Sometimes, you want to update some fields of record, you can input ```/sobjects/Account/001O000000MIiSXIA1``` and choose it, click ```Execute Rest Test``` in the context menu, choose the ```Patch``` in the popup menu and input ```{"Name": "Test Path"}``` in the input panel, wait for a moment, the patch result will be shown in the new view:
```
{

}
```

+ **Search Sample**: Sometimes, want to test search action, you can input ```FIND {test}``` and choose it, click ```Execute Rest Test``` in the context menu, choose the ```Search``` in the popup menu, wait for a moment, the patch result will be shown in the new view:
```
[{
    'Id': '001O0000001OWv5IAG',
    'attributes': {
        'type': 'Account',
        'url': '/services/data/v29.0/sobjects/Account/001O0000001OWv5IAG'
    }
}]
```

+ **Quick Search Sample**: Sometimes, want to search something, you can input ```test``` and choose it, click ```Execute Rest Test``` in the context menu, choose the ```Quick Search``` in the popup menu, wait for a moment, the patch result will be shown in the new view:
```
[{
    'Id': '001O0000001OWv5IAG',
    'attributes': {
        'type': 'Account',
        'url': '/services/data/v29.0/sobjects/Account/001O0000001OWv5IAG'
    }
}]
```


## Export Data Template
Click ```SublimeApex``` > ```Export``` > ```Export Data Template```, wait for a moment, choose the record type of sobject, the sobject data template by record type will be exported. From the row 1 to row 6, meaning is show as below,
```
[Field Label]...
[Field API]...
[Field Type]...
[Layout Required]...
[Picklist Label if has]...
[Picklist Value if has]
```

## Bulk Api
+ Up to now, support close jobs, export, insert, update and delete.
+ You can set the batch size and batch bytes for every batch by put ```maximum_batch_size``` and ```maximum_batch_bytes``` in your user settings, you should be aware, maximum records of single batch is **10K** and maximum bytes of single batch is **1000K**
+ This tool will get your CSV file encoding type by detecting the first **1000** bytes of the CSV file, as a best practice, you should prepare CSV file which encoding type is ```ANSI``` or ```UTF-8```.
+ If you want to insert a CSV file, you'd better open the CSV file in sublime and copy the file path, after you choose the sobject that you want to insert records, this tool will automatically get the file path from the clipboard

## Proxy
Refer to [Request Proxies](http://docs.python-requests.org/en/latest/user/advanced/#proxies)

# Build-in Dependency Lib
+ [requests](https://github.com/kennethreitz/requests)
+ [xmltodict](https://github.com/martinblech/xmltodict)
