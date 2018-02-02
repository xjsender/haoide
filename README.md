# Sublime IDE for Salesforce
This plugin supports [Sublime Text 3](http://www.sublimetext.com/3) for windows and OSX, not tested for Linux.

All of my motivation on this plugin come from your star, if you think this plugin is helpful in your daily work, please **star** this plugin.

# Installation

> Before install this plugin, you must install [Sublime Text 3](http://www.sublimetext.com/3) and then [Package Control](https://packagecontrol.io/installation).

After you have installed ``package control`` in your sublime, you can install this plugin by searching ``haoide`` in package control, if you don't know how to use ``package control``, you can refer to [usage of package control](https://packagecontrol.io/docs/usage).

Or, You can follow the step-by-step [instruction](https://meighanrockssf.wordpress.com/portfolio/install-haoide/) by [Meighan Brodkey](https://twitter.com/meighansf)

# Project Configuration
After you have installed this plugin successfully, you can follow <a href="/docs/project.md" target="_blank">Project Configuration</a> to configure your own project.

If you don't want to keep your user credential information in the plugin , you just need to do it as below format, plugin will lanuch the browser to start OAuth2 Login process,
```javascript
"projects": {
  "pro-sublime": {
      "default": true,
      "login_url": "https://login.salesforce.com",
      "login_type": "REST",
      "subscribed_metadata_objects": [
          "ApexClass",
          "ApexComponent",
          "ApexTrigger",
          "AuraDefinitionBundle"
      ],
      "username": "apex.sublime@dev.com"
    },
}
```

# Change Logs
+ <a href="https://github.com/xjsender/haoide/blob/master/HISTORY.rst" target="_blank">Change Logs</a>

# Quick Link
* <a href="/docs/debug.md" target="_blank">Execute Anonymous</a>
* <a href="/docs/completion.md" target="_blank">Code AutoComplete</a>
* <a href="/docs/snippets.md" target="_blank">Snippets</a>
* <a href="/docs/tooling.md" target="_blank">Tooling Operation</a>
* <a href="/docs/debug.md" target="_blank">Debug and Test</a>
* <a href="/docs/retrieve.md" target="_blank">Retrieve</a>
* <a href="/docs/deploy.md" target="_blank">Deploy</a>
* <a href="/docs/staticresource.md" target="_blank">Static Resource Bundle</a>
* <a href="/docs/export.md" target="_blank">Export CSV</a>
* <a href="/docs/utilities.md" target="_blank">Salesforce Utilities</a>
* <a href="/docs/json2apex.md" target="_blank">Convert JSON to Apex</a>
* <a href="/docs/rest.md" target="_blank">REST Test</a>
* <a href="/docs/dataloader.md" target="_blank">Data Loader</a>
* <a href="/docs/document.md" target="_blank">Document Quick Reference</a>
* <a href="/docs/plugin.md" target="_blank">Plugin Operation</a>
* <a href="https://github.com/xjsender/SublimeApexScreenshot/raw/master/LightingDevelopment.gif" target="_blank">Lighting Development</a>
* <a href="https://raw.githubusercontent.com/xjsender/SublimeApexScreenshot/master/Completions.gif" target="_blank">Completions Demo</a>
* <a href="http://docs.python-requests.org/en/latest/user/advanced/#proxies" target="_blank">Request Proxies</a>

# Build-in Dependency Lib
  > - [requests](https://github.com/kennethreitz/requests)
  > - [xmltodict](https://github.com/martinblech/xmltodict)
  > - [dateutil](http://labix.org/python-dateutil/)
  > - [xmlformatter](https://pypi.python.org/pypi/xmlformatter/)
  > - [Salesforce oAuth2](https://github.com/neworganizing/salesforce-oauth2)
  > - [SalesforceXyTools](https://github.com/exiahuang/SalesforceXyTools)

# Q&A
+ ``Refresh Package`` vs ``Update Project``
    * ``Refresh Package`` can update the project by the ``package.xml`` in the project folder or ``project/src`` folder
    * ``Update Project`` will update the project according to ``subscribed metadata``

+ ``Refresh Folder`` vs ``Update Project``
    * Generally, ``Refresh Folder`` can be used to update the components in the chosen folders
    * However, ``Update Project`` is always used to refresh all folders or newly subscribed metadata

+ ``Save to Server`` vs ``Deploy to Server``
    * ``Save to Server`` is achieved by ``Tooling API`` tech, which is usually used to develop apex code in sandbox
    * ``Deploy to Server`` is achieved by ``Metadata API`` tech, which is usually used to develop none-apex in sandbox, deploy any components into different org or production

+ What's the usage of ``Update Project Pattern`` command?
    * Everytime when you udpate the ``file_exclude_patterns`` or ``folder_exclude_patterns``, you must execute ``Update Project Pattern`` command to ensure it is working.
    * Everytime when the default project doesn't appeared in the sidebar panel, you an use this command to show the default project.

+ If you failed to deploy package after release 3.3.7
  * you should remove ``deploy_options`` from your user settings, see more detail at [issue #101](https://github.com/xjsender/haoide/issues/101)

+ If all menu items are all gray and disabled after you installed haoide
  * You should check whether [issue #112](https://github.com/xjsender/haoide/issues/112) can resolve your problem

+ Don't want to create new project with time stamp every day?
  * You can set ``keep_project_name_time_suffix`` to ``false``

+ What is the usage of mouesmap key bindings?
  * Press ``shift`` + Dblclick ``left mouse button``: Quick open component by name
  * Press ``alt`` + Click ``left mouse button``: Retrieve debug log detail by id
  * Press ``alt`` + DblClick ``left mouse button``: View code coverage by name
  * Press ``alt`` + Triple Click ``left mouse button``: Cancel deployment by Id
