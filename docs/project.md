
# Project Configuration
## Worspace
If your operation system is **OSX**, you should change the workspace in ```HaoIDE``` > ```Setting``` > ```Setting - User``` to your own, if you didn't do that, plugin will save the project to ```<packages_path>/User/HaoIDE```, 

There are two tiers of workspace concept in this plugin, including plugin level workspace and project level workspace, the privilege of project level is higher than the plugin level workspace, if you didn't define the workspace in the project property of ```projects``` setting, plugin will set your plugin level workspace to the default workspace, for example, if the settings is set as below:

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
+ This command is located in the ``New > New Project`` of the main menu
+ Once you click this command, a new project will be downloaded and appeared in the sidebar
+ Just after new project is finished, sObject completions will work
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
your project folder name should be ```Exercise-Pro-20130730```, you can close this time suffix feature by setting ```keep_project_name_time_suffix``` to ``false``

**If you are developing a package, you need to add your package namespace to settings ``allowed_packages``, more detail to check the ``allowed_packages`` in the default settings**

## Update Project
You can click ```haoide > Update > Update Project``` in the main menu or press <kbd>Alt</kbd>+<kbd>R</kbd> to update your active project.

## Execute Anonymous
Choose any apex code snippet, press <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>E</kbd> or click ```HaoIDE``` > ```Execute Anonymous``` in the context menu, you will see the result, you should be aware, if anonymous code compile is failed, message will be shown in output panel, just after compile succeed, the executed result will be shown in the new view.

There has a ```log_levels``` setting in the default settings to control the anonymous log level , If you want to change anonymous log levels, you can override it in your user settings.