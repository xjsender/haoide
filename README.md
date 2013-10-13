# Sublime IDE for salesforce
This plugin support ```Sublime Text 3``` for windows. full docs refer to [SublimeApex User Guide](https://github.com/xjsender/SublimeApex/blob/master/docs/SublimeApex%20Guide.docx)

## New Project
+ This command is used to download or update your project
+ Once click this command, a new project will be downloaded and appeared in the sidebar
+ Project Folder Name Convention: the project name set in user settings append with date literal of today, for example,
if today is ```2013/07/30``` and user settings is 

```javascript
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
your project folder name should be ```Exercise-Pro-20130730```, you can close this time suffix feature by setting ```keep_project_name_time_suffix``` to false

## Completions:
+ 1. ```Input .```, show all methods of class
+ 2. ```Input .```, show all fields, parent relationship name and child relationship names
+ 3. ```Input .``` after sobject relationship name, show all fields of this relationship name
+ 4. ```Input .```, show all public methods of custom class if corresponding class view is open
+ 5. ```Input <``` after list or set, list all sobjects and apex classes
+ 6. ```input <```, list all tag, including Visualforce Components and HTML Elements
+ 7. ```input :```, list all suffix of all visualforce Components
+ 8. ```input space```, list all attributes of tags, if tag attribute has predefined values, output attr, otherwise, output attr="$1"
+ 9. ```input =```, list all values of this corresponding attributes

## Execute Anonymous
After any snippet is chosen, the Execute Anonymous command is enabled.

## Execute Query
Just any snippet which start with SELECT is chosen, the Execute Query command is enabled

## Save component
+ This command is only enabled in ApexPage, ApexTrigger, ApexClass or ApexComponent file
+ After component is updated, click ```SublimeApex > Save to Server```

## Refresh component
+ This command is only enabled in ApexPage, ApexTrigger, ApexClass or ApexComponent file
+ After component is updated in UI or other IDE, click ```SublimeApex > Refresh From Server```

## Delete component
+ This command is only enabled in ApexPage, ApexTrigger, ApexClass or ApexComponent file
+ If component is useless and you want to delete it from server, click ```SublimeApex > Delete From Server```

## New Component #
Press ```Ctrl+Alt+N``` or click ```SublimeApex > New Component``` to invoke the input panel, and then input the new component info according to guide as below
```
1. Create new trigger: Trigger-Name.trigger, Sobject-Name
2. Create new class: Class-Name.cls
3. Create new component: Component-Name.component
4. Create new Page: Page-Name.page
```

## Create Debug Log
If you want to track the log of any user, click ```SublimeApex > Apex Test > Create Debug Log```, wait for a moment, you will see the user list, choose one and press enter, check the progress in the status bar until succeed message appeared, and then your debug log user is recorded.

## List Debug Log
If you want to see the log list of any user, click ```SublimeApex > Apex Test > List Debug Logs```, wait for a moment, you will see the user list, choose one and press enter, check the progress in the status bar until succeed message appeared, and then a new view with the log list will be open.

## Run Test
There are two methods to run test, one is by Main Menu, other is in the context menu
+ 1. By Main Menu: click ```SublimeApex > Apex Test > Run Test```, choose the test class and press enter, check the progress in the status bar until succeed message appeared, and then a new view with the test result will be open.
+ 2. By Context Menu: in the context of opened class, click ```SublimeApex > Run Test Class```, check the progress in the status bar until succeed message appeared, and then a new view with the test result will be open.

## View Code Coverage
This feature just works when api version is >= 29.0
In the context menu of open class or trigger, click ```button1 > SublimeApex > View Code Coverage```, after the thread is over, you will see the code coverage percentage in the console and a new view with not covered highlight lines.

## Refresh Folder
Click SublimeApex > Refresh Folder to refresh folder

## Refresh Multiply Components
Choose the components you want to refresh, and then Click ```SublimeApex > Refresh Selected Components``` in the Sidebar Menu

## Delete Multiply Components
Choose the components you want to delete, and then Click ```SublimeApex > Delete Selected Components``` in the Sidebar Menu

## Quick Goto Component
Put the focus in the Class Name, and then, press ```shift``` and ```button1```, the class file will be open if this class file is exist

## Retrieve All Metadata
Click ```SublimeApex > Retrieve Metadata``` in the main menu, you will see a new open view with message, this view will be refreshed every five seconds, after the retrieve status is completed, plug-in will download the base64 zipfile, after that, base64 zipfile will be decoded to zip file, at the last, this zip file will be extracted.

## Deploy Metadata
This functionality is not perfect now, but it can work now.

## Proxy
Refer to [Request Proxies](http://docs.python-requests.org/en/latest/user/advanced/#proxies)

...

# Configuration #
## Preference - Settings
```javascript
{
    // Auto completion after these characters
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
        },
        {
            "characters": "=",
            "selector": "text.html - source"
        }
    ]
}
```
## Settings - Default
```javascript
{
    // Indicate whether add project name time suffix
    // When this setting value is true, you create a new project at yestoday and you refresh 
    // it's code today, a new project folder will be created to keep the refreshed code
    // Two methods to fix this bug:
    //     1. Set this setting value to false, 
    //     2. Create new project every day.
    // It depends on your choice.
    "keep_project_name_time_suffix": true,

    // Indicate whether print session id, maybe you need this session id
    // for other purpose
    "output_session_info": false,

    // Indicate whether keep local history history
    "keep_local_change_history": true,

    // Every time when you save component and error happened, the console will be open.
    // When you edit the code according to the error message, this flag is used to indicate
    // whether the console will be hidden automatically
    "hidden_console_on_modify": true,

    // Sometimes, you may want to develop package, so you need to just download the code 
    // in the allowed packages, because package name is unique in the whole salesforce org, 
    // so I put it here but not in project property
    "allowed_packages": ["sinaweibo", "twitter", "facebook"],

    // API version
    "api_version": 28,

    ...
}
```

## Settings - User
because default setting is the plugin default setting, In order to prevent that plugin update override your projects configurations and any other customization setting, you'd better put them at here.
```javascript
{
    "projects": {
        "sandbox-org-dev1": {
            "default": true,
            "login_url": "https://test.salesforce.com",
            "password": "password",
            "username": "username@org.com.dev1"
        },
        "pro-org": {
            "default": false,
            "login_url": "https://login.salesforce.com",
            "password": "password",
            "username": "username@org.com",
            "security_token": "*****"
        }
    },
    "workspace": "C:/Users/Administrator/Dropbox/workspace",
    "keep_local_change_history": false,
    "keep_project_name_time_suffix": false,
    "hidden_console_on_modify": false
}
````
- **default**: there should be only one default active project
- **login_url**: sandbox is ```https://test.salesforce```, production is ```https://login.salesforce```
- **username**: login confidential
- **password**: login confidential
- **security_token**: If have, just put it here, if not, you can remove this attr or left it empty

## Key Bindings - Default
Here are the all key bindings to corresponding command, you can customize them according to your habit.
```javascript
[
    // Switch Project
    {"keys": ["alt+s"], "command": "switch_project"},

    // Download all code and save them to new project
    {"keys": ["alt+f5"], "command": "new_project"},

    // Refresh Folder
    {"keys": ["alt+r","alt+f"], "command": "refresh_folder"},

    ...
]
```

## Key Bindings - User
If you have your own shortcut key convention, you should put it here
```javascript
[
    // Switch Project
    {"keys": ["alt+s"], "command": "switch_project"},

    // Download all code and save them to new project
    {"keys": ["alt+f5"], "command": "new_project"},

    // Refresh Folder
    {"keys": ["alt+r","alt+f"], "command": "refresh_folder"},

    ...
]
```

## Key Bindings - mousemap
```javascript
[
    // Press Shift and Click Left Mouse for twice will open class file in the background
    {
        "button": "button1", "count": 2, "modifiers": ["shift"],
        "press_command": "goto_component", 
        "press_args": {"is_background": true}
    },

    // Press Shift and Click Left Mouse for triple will open class file
    {
        "button": "button1", "count": 3, "modifiers": ["shift"],
        "press_command": "goto_component", 
        "press_args": {"is_background": false}
    }
]
```
- **button1**: it means left mouse button
- **button2**: it means right mouse button
- **count**: count = 2 means double click, count = 3 means triple click
- **modifiers**: it means the assist key
- **press_command**: the bind command
- **press_args**: the bind command arguments

# Installation #
Firstly, install sublime text and then extract the zip file into your sublime package path.
Package Name in sublime should be SublimeApex, for example, ```D:\Sublime347\Data\Packages\SublimeApex``` is my installation path.

Before start coding, you should initiate your project settings, you can keep your settings in Default Setting or User Setting, however, ```User Settings``` is prior to ```Default Settings```.

In order to prevent plugin update overriding your toolingapi settings, you should keep your custom settings into ```Setting - User``` by clicking ```SublimeApex > Setting - User```.

You can setup your projects follow below sample by clicking "Setting - User" in the main menu, projects must be included in {}.

When you initiate your settings, you can have more than one project in "projects", however, only one project default can be true.

If your project need security token, just put it follow "username".

Every time you want to switch the project, you can click ```SublimeApex > Switch Project``` in the main menu and choose that you want, and then the update projects settings will be saved to user settings.
```javascript
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