# Sceenshot #
Funcationality Screenshots shown as below,

###Menus
+ Main Menu:<br/>
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/main%20menu.png" /><br/>
+ Siderbar Menu:<br/>
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/siderbar%20menu.png" /><br/>
+ Context Menu:<br/>
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/context%20menu.png" />

###Switch Project
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/switch%20project.png" />

###New Project
+ This command is used to download or update your project
+ Once click this command, a new project will be downloaded and appeared in the sidebar
+ Project Folder Name Convention: the project name set in user settings append with date literal of today, for example,
if user settings is 
```
{
    "workspace": "d:/ForcedotcomWorkspace",
    "projects": {
        "Exercise-Pro": {
            "default": true,
            "login_url": "https://login.salesforce.com",
            "password": "bp333333",
            "username": "mouse@exercise.com"
        }
    }
}
```
today is 2013/07/30, your project folder name should be Exercise-Pro-20130730
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/new%20project.png" />

###Sobject Field Completions
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/sobject%20field%20completions.png" />

###Apex Code Completions
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/Apex%20code%20completions.png" /><br/>
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/map%20completions.png" /><br/>
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/set%20completions.png" /><br/>
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/list%20completions.png" />

###Cross View Completions
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/cross%20view%20completions.png" />

###Visualforce Page Completions
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/visualforce%20page%20completions.png" />

###Run Test
+ Choose Test Class <br/>
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/choose%20test%20class.png" />

+ View Test Result<br/>
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/test%20result.png" />

+ Choose the LogId and view detail in SFDC<br/>
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/view%20debug%20log.png" />

###Refresh Folder
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/refresh%20folder.png" />

###Execute Anonymous
+ After any snippet is chosen, the Execute Anonymous command is enabled.
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/execute%20anonymous.png" />

###Execute Query
+ Just any snippet which start with SELECT is chosen, the Execute Query command is enabled
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/execute%20query.png" />

###Deploy component
+ This command is only enabled in ApexPage, ApexTrigger, ApexClass or ApexComponent file
+ After component is updated, click SublimeApex > Deploy to Server
<img src="https://raw.github.com/xjsender/SublimeApex/master/screenshot/deploy%20component.png" />

# Installation #
This plugin support ST2 and ST3, firstly, install sublime text and then extract the zip file into your sublime package path.
Package Name in sublime should be SublimeApex, for example, "D:\Sublime347\Data\Packages\SublimeApex" is my installation path.

Before start coding, you should initiate your project settings, you can keep your settings in Default Setting or User Setting, however, [User Settings] is prior to [Default Settings].

In order to prevent plugin update overriding your toolingapi settings, you should keep your custom settings into [Setting - User] by clicking [SublimeApex > Setting - User].

You can setup your projects follow below sample by clicking "Setting - User" in the main menu, projects must be included in {}.

When you initiate your settings, you can have more than one project in "projects", however, only one project default can be true.

Every time you want to switch the project, you can click [SublimeApex > Switch Project] in the main menu and choose that you want, and then the update projects settings will be saved to user settings.
``` 
{
    "workspace": "d:/ForcedotcomWorkspace",
    "projects": {
        "Project1 Name": {
            "default": true,
            "login_url": "https://test.salesforce.com",
            "password": "a",
            "username": "a@a.com"
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