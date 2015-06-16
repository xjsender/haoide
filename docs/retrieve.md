# Retrieve
## Toggle Metadata Objects
* Open your command palette and input HaoIDE: ``Toggle Metadata Objects``
* Subscribe the metadata object util all you want are finished, press ``ESC``
* After that, you will be asked to confirm whether execute ``update_project`` command to download all subscribed metadata, once you confirmed to execute update operation, plugin will start to update whole project for you, otherwise, nothing will happen.

## Retrieve All Step by Step
* Click ```Metadata Migration``` > ```Retrieve All``` in the main menu
* After retrieve is finished, retrieved metadata will be extracted to ``Project/src``

## Retrieve sObject And Workflow Step by Step
* Click ```Metadata Migration``` > ```Retrieve sObject And Workflow``` in the main menu
* After retrieve is finished, ``objects`` and ``workflows`` will be extracted to ``Project/src``

## Retrieve Files From Server Step by Step
You can retrieve files from server by below two ways,

* By Sidebar Menu
    - Choose one or more files in the sidebar
    - Execute ```HaoIDE > Refresh Files From Server``` command in the sidebar menu, retrieve will start
    - After retrieve is finished, selected files will be refreshed with the latest source

* By Context Menu
    - Choose a file or more files in the sidebar
    - Execute ```HaoIDE > Refresh From Server``` command in the context menu, retrieve will start
    - After retrieve is finished, selected files will be refreshed with the latest source

## Retrieve Package.xml Step by Step
With this feature, plugin can retrieve the metadata by package.xml from the default project, if package.xml parse failed, error will be shown in the output panel.

You can retrieve package.xml by below two ways,

* By Sidebar Menu 
    - Choose a package file, which name should be end with ```.xml```
    - Execute ```HaoIDE > Retrieve Package.xml``` command in the sidebar menu
    - You will need to input the output path for retrieved result, which has a default value same with the path of current package.xml, after input the output path and hit <kbd>Enter</kbd>, retrieve will start
    - After retrieve is finished, you will see the retrieved package in your input path

* By Context Menu
    - Open a package file, which name should be end with ```.xml```
    - Execute ```HaoIDE > Retrieve Package.xml``` command in the context menu
    - You will need to input the output path for retrieved result, which has a default value same with the path of current package.xml, after input the output path and hit <kbd>Enter</kbd>, retrieve will start
    - After retrieve is finished, you will see the retrieved package in your input path