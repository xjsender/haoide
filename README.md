# Sublime IDE for salesforce
This plugin supports ```Sublime Text 3``` for windows and OSX, not tested for Linux. **If you think this plugin is helpful, please star this plugin.**

# Change Logs:
See [History](https://github.com/xjsender/SublimeApex/blob/master/HISTORY.rst)

# Supported Feature:
+ Muti-project management
+ Configurable API Version
+ View Code Coverage
+ Create Debug Log
+ Retrieve Debug Logs of Specified User
+ Apex Code CRUD
+ Apex Code Folder Refresh
+ Run Test Class
+ Apex Code Local History
+ Execute Anonymous
+ Execute Query
+ Quick Documents Reference Search for kinds of Salesforce APIs
+ Kinds of code completions, see sector "Completions"
+ Generate All or Specified Sobject Workbook
+ Generate Custom Field Workbook (Including Field Id)
+ Generate Global Describe Workbook
+ Generate Layout Avaiable PicklistValues
+ Export Data Template for Specified Recod Types
+ Export Validation Rule and Workflow
+ Quick Login to Home Page, Console, Debug Log...
+ Quick View chosen Id in SFDC Web
+ Quick View Apex Code in SFDC Web
+ Backup All or Specified Sobjects in Muti-thread (Very Fast)
+ Many common used snippets
+ Manually Update Plugin

# Installation #
This plugin is hosted on [package control](https://sublime.wbond.net/packages/Salesforce%20IDE), you can install this plugin by searching ```Salesforce IDE``` in package control

# Project Configuration #
If your operation system is **OSX**, you must set the workspace in ```SublimeApex > Setting > Setting - User```.

There is a default test org in this plugin, you can see it by clicking ```SublimeApex > Switch Project``` in the main menu, however, if you want to use this plugin in your own org, you need to configure your org user confidential before new project

In order to prevent plugin update overriding your settings, you should keep your customize settings into ```Setting - User``` by clicking ```SublimeApex > Settings > Setting - User```.
re
You can setup your projects follow below sample by clicking ```SublimeApex > Settings > Setting - User``` in the main menu, projects must be included in {}.

When you initiate your settings, you can have more than one project in "projects", however, only one project default should be true.

If your own org login need security token, just set it as sample.

Every time you want to switch the project, you can click ```SublimeApex > Switch Project``` in the main menu and choose that you want, and then the updated projects settings will be saved to user settings.

If you want to check the current active project, you can check the most left of side bar or press ```alt+s```

After your project configuration is finished, you can click ```SublimeApex > new project``` in the main menu to download your code.
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

## New Project
+ You need to choose which pre-defined org to start new project
+ This command is used to download or update your project
+ Once you click this command and choose a project setting,  a new project will be downloaded and appeared in the sidebar
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

### Update Project
You can press ```Alt+f7``` to update your active project

## Completions:
+ 1. ```Input .```, show all methods of class
+ 2. ```Input .```, show all fields, parent relationship name and child relationship names
+ 3. ```Input .``` after sobject relationship name, show all fields of this relationship name
+ 4. ```Input .```, show all public methods of custom class if corresponding class view is open
+ 5. ```Input English Character```, show all sobject name and standard class name
+ 6. ```input <```, list all tag, including Visualforce Components and HTML Elements
+ 7. ```input :```, list all suffix of all visualforce Components
+ 8. ```input space```, list all attributes of tags
+ 9. ```input =```, list all values of this corresponding attributes in Visualforce page
+ 10. If sobject field type is picklist, after you input ```opp.StageName =``` or ```Opportunity.StageName =```, all available picklist values will be shown

### Completions Screenshots
<img src="https://raw.github.com/xjsender/SublimeApexScreenshot/master/apex.jpg" /><br/>
<img src="https://raw.github.com/xjsender/SublimeApexScreenshot/master/page.png" /><br/>

## Execute Anonymous
Choose any apex code snippet, press ```Ctrl+Alt+E``` or click ```SublimeApex > Execute Anonymous```, the executed result will be shown in a new view.

There has a ```log_levels``` setting in the default setting, If you want to change anonymous log levels, you can put your log levels settings into your user setting.

**If your chosen code snippet contains non-english word, there will have problem.**

## Execute Query
After any snippet which start with SELECT is chosen, you can press ```Ctrl+Alt+Q``` or click ```SublimeApex > Execute Query```, the queried json result will be formated and shown in a new view.

## Save component
+ This command is only enabled in salesforce code file
+ After code is updated, click ```SublimeApex > Save to Server``` or press ```Ctrl+Alt+S```

## Refresh component
+ This command is only enabled in salesforce code file
+ After code is updated in UI or other IDE, press ```Ctrl+Alt+R``` or click ```SublimeApex > Refresh From Server``` to refresh it server.

## Delete component
+ This command is only enabled in salesforce code file
+ If component is useless and you want to delete it from server, click ```SublimeApex > Delete From Server```

## New ApexClass #
Click ```SublimeApex > New > New ApexClass```, choose the predefined template, and then input the class name in the input panel at the bottom, after that, your class will be created.

## New ApexPage #
Click ```SublimeApex > New > New ApexPage```, choose the predefined template (Just have only one template now), and then input the page name in the input panel at the bottom, after that, your page will be created.

## New ApexComponent #
Click ```SublimeApex > New > New ApexComponent```, choose the predefined template (Just have only one template now), and then input the component name in the input panel at the bottom, after that, your component will be created.

## New ApexTrigger #
Click ```SublimeApex > New > New ApexTrigger```, choose the sobject on which you will create trigger, and then input the trigger name in the input panel at the bottom, after that, your trigger will be created.

## Create Debug Log
If you want to track the log of any user, click ```SublimeApex > Apex Test > Create Debug Log```, wait for a moment, you will see the user list, choose one and press enter, check the progress in the status bar until succeed message appeared, and then your debug log user is recorded.

## List Debug Log
If you want to see the log list of any user, click ```SublimeApex > Apex Test > List Debug Logs```, wait for a moment, you will see the user list, choose one and press enter, check the progress in the status bar until succeed message appeared, and then a new view with the log list will be open.

You can choose the ```Log Id``` and click ```SublimeApex > View Debug Log In Sublime``` command in the context menu, wait for the end of the progress on the status bar, after it is finished, a new view with the log detail will be opened.

Or, you can choose any Log Id and click ```SublimeApex > View Id In Salesforce Web```, wait for a moment, browser will be open and redirect to the log detail page.

## Run Test
There are two methods to run test, one is by Main Menu, other is in the context menu
+ 1. By Main Menu: click ```SublimeApex > Apex Test > Run Test```, choose the test class and press enter, check the progress in the status bar until succeed message appeared, and then a new view with the test result will be open.
+ 2. By Context Menu: in the context of opened class, click ```SublimeApex > Run Test Class```, check the progress in the status bar until succeed message appeared, and then a new view with the test result will be open.

## View Code Coverage
This feature just works when api version is >= 29.0
In the context menu of open class or trigger, click ```SublimeApex > View Code Coverage``` in the context menu, ait for the end of the progress on the status bar, you will see the code coverage percentage in the console and a new view with not covered highlight lines.

## Refresh Folder
Click the folder in the side bar, refresh that you want to refresh, if you choose the classes folder, the ```Refresh ApexClass``` command will be visible, ```ApexTrigger```, ```ApexComponent```, ```ApexPage``` and ```StaticResource``` is same.

## Salesforce Document Quick Reference
I forked this idea from [Salesforce Referencee](https://github.com/Oblongmana/sublime-salesforce-reference) and added some feature based on it.

Click the ```SublimeApex > Reference > Reload Salesforce Reference``` in the main menu, wait for a moment until the ```Open Document``` command is enabled, at this moment, you can press ```Ctrl+Shift+O``` or Click it to invoke the ```Open Document``` command, nearly all reference api will be shown in the list, you can try to choose any one and it will be opened in browser.

## Refresh Multiply Components
Choose the components you want to refresh, and then Click ```SublimeApex > Refresh Selected Components``` in the Sidebar Menu

## Delete Multiply Components
Choose the components you want to delete, and then Click ```SublimeApex > Delete Selected Components``` in the Sidebar Menu

## Quick Goto Component
Put the focus in the Class Name, and then, press ```shift```,  and click ```button1``` for twice, the class file will be open in background if this class file is exist, however, if you want to open this class in the foreground, you should press ```shift``` and click ```button1``` for triple.

## Retrieve All Metadata
Click ```SublimeApex > Retrieve Metadata``` in the main menu, you will see a new open view with message, this view will be refreshed every five seconds, after the retrieve status is completed, plug-in will download the base64 zipfile, after that, base64 zipfile will be decoded to zip file, at the last, this zip file will be extracted.

## Deploy Metadata
This functionality is not perfect now, but it can work now.

## Export Workflow Rules
After you downloaded all metadata by clicking ```SublimeApex > Migration > Retrieve Metadata```, you can click ```SublimeApex > Export > Export Workflow``` to backup all workflows in your org to csv.

## Export Validation Rules
After you downloaded all metadata by clicking ```SublimeApex > Migration > Retrieve Metadata```, you can click ```SublimeApex > Export > Export Validation Rule``` to backup all validation rules in your org to csv.

## Export CustomFields
You can click ```SublimeApex > Export > Export CustomFields``` to export all custom fields in your org to csv.

## Export Workbook of sobjects
You can click ```SublimeApex > Export > Export Workbook``` to export all sobject workbooks in your org to csv.
If you just want to export some attributes of sobject workbook, you can do it by setting workbook_field_describe_columns in ```SublimeApex > Settings > Setting - User.

## Exceute Rest Test
Up to now, support Head, Get, Post, Delete and Retrieve Body Methods, for example, Input ```/sobjects/Account/Describe``` and click ```SublimeApex> Execute Rest Test``` in the context menu or press ```F9```, context dynamic menu will show up, you can choose GET to retrieve Account Describe Result in the new view.

## Export Data Template
Click ```SublimeApex > Export > Export Data Template```, wait for a moment, choose the record type of sobject, the sobject data template by record type will be exported

## Bulk Api
+ Up to now, support export, insert, update and delete.
+ You can set the batch size and batch bytes for every batch by put ```maximum_batch_size``` and ```maximum_batch_bytes``` in your user settings, you should be aware, maximum records of single batch is **10K** and maximum bytes of single batch is **1000K**
+ This tool will get your CSV file encoding type by detecting the first **1000** bytes of the CSV file, as a best practice, you should prepare CSV file which encoding type is ```ANSI``` or ```UTF-8```.
+ If you want to insert a CSV file, you'd better open the CSV file in sublime and copy the file path, after you choose the sobject that you want to insert records, this tool will automatically get the file path from the clipboard

## Proxy
Refer to [Request Proxies](http://docs.python-requests.org/en/latest/user/advanced/#proxies)

# Dependency Lib #
+ [requests](https://github.com/kennethreitz/requests)
+ [xmltodict](https://github.com/martinblech/xmltodict)