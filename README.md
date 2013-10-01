# Sublime IDE for salesforce
This plugin support Sublime Text 3 for windows. full docs refer to [SublimeApex User Guide](https://github.com/xjsender/SublimeApex/blob/master/docs/SublimeApex%20Guide.docx)

###New Project
+ This command is used to download or update your project
+ Once click this command, a new project will be downloaded and appeared in the sidebar
+ Project Folder Name Convention: the project name set in user settings append with date literal of today, for example,
if today is 2013/07/30 and user settings is 

```
{
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
your project folder name should be Exercise-Pro-20130730, you can close this time suffix feature by setting keep_project_name_time_suffix to false

##Completions:
You should add below setting to Perference > User - Setting, then you will have auto completions functionality.
+ 1. After input dot in apex code, show sobject field and apex class completions
+ 2. After List< and Set< in apex code, show sobject and apex class
+ 3. Input < in visualforce page, show all components.
+ 4. Input <apex:page and space to show all attributes of this component.
+ 5. Input <apex: or something standard library to show all component suffix.

```
    "auto_complete_triggers":
    [
        {
            "characters": ".",
            "selector": "source.java"
        },
        {
            "characters": "<",
            "selector": "source.java"
        },
        {
            "characters": "<",
            "selector": "text.html - source"
        },
        {
            "characters": ":",
            "selector": "text.html - source"
        },
        {
            "characters": " ",
            "selector": "text.html - source"
        },
        {
            "characters": ":",
            "selector": "text.html - source"
        }
    ]
```

###Execute Anonymous
+ After any snippet is chosen, the Execute Anonymous command is enabled.

###Execute Query
+ Just any snippet which start with SELECT is chosen, the Execute Query command is enabled

###Save component
+ This command is only enabled in ApexPage, ApexTrigger, ApexClass or ApexComponent file
+ After component is updated, click SublimeApex > Save to Server

###New Component #
Press Ctrl+Alt+N to invoke the input panel, and then input the new component info according to guide as below
```
1. Create new trigger: Trigger-Name.trigger, Sobject-Name
2. Create new class: Class-Name.cls
3. Create new component: Component-Name.component
4. Create new Page: Page-Name.page
```

# Installation #
Firstly, install sublime text and then extract the zip file into your sublime package path.
Package Name in sublime should be SublimeApex, for example, "D:\Sublime347\Data\Packages\SublimeApex" is my installation path.

Before start coding, you should initiate your project settings, you can keep your settings in Default Setting or User Setting, however, [User Settings] is prior to [Default Settings].

In order to prevent plugin update overriding your toolingapi settings, you should keep your custom settings into [Setting - User] by clicking [SublimeApex > Setting - User].

You can setup your projects follow below sample by clicking "Setting - User" in the main menu, projects must be included in {}.

When you initiate your settings, you can have more than one project in "projects", however, only one project default can be true.

If your project need security token, just put it follow "username".

Every time you want to switch the project, you can click [SublimeApex > Switch Project] in the main menu and choose that you want, and then the update projects settings will be saved to user settings.
``` 
{
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

# Supported Feature: #
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

7. When we want to run test, basically, your test result should be displayed as a new view.

8. If we want to refresh the folder, we just need to click the SublimeApex > Refresh Folder and then choose the folder we want to refresh.

9. Before we update plugin, we should move your customized settings from "Settings - Default" to "Settings - User"

10. Every time when you create a new view, it's default syntax is Apex.

11. If you don't want to keep the local history change, you can set keep_local_change_history to false in the settings.

12. If you want to output the session info, you can set output_session_info to true in the settings.