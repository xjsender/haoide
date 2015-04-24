# Retrieve
## Retrieve All Step by Step
* Click ```Metadata Migration``` > ```Retrieve All``` in the main menu
* After retrieve is finished, retrieved metadata will be extracted to ``Project/src``

**This feature is not good enough, because there is no listPackage feature supported, for example, report and dashboard can't be retrieve if no detail folder/report is specified in package.xml**

## Retrieve sObject And Workflow
* Used for retrieving metadata of all sObjects and Workflows

## Retrieve Files From Server Step by Step
You can retrieve files from server by below two ways,

* By Sidebar Menu
    - Choose a file of salesforce supported in the sidebar
    - Execute ```HaoIDE > Refresh Files From Server``` command in the sidebar menu, retrieve will start
    - After retrieve is finished, you will see the retrieved result

* By Context Menu
    - Choose a file of salesforce supported in the sidebar
    - Execute ```HaoIDE > Refresh From Server``` command in the context menu, retrieve will start
    - After retrieve is finished, you will see the retrieved result

## Retrieve Package.xml Step by Step
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