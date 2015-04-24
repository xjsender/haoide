# Utilities
There are some utilities to keep your work efficient as below

## Convert 15Id to 18Id Step by Step
* Click ```Utilities``` > ```Convert 15Id to 18Id``` in the main menu
* to convert your input 15Id to 18Id, if your input is not valid 15Id, it will be returned as original value

## Describe sObject Step by Step
* Click ```Utilities``` > ```Describe sObect``` in the main menu
* Choose a sObject in the quick panel and press <kbd>Enter</kbd>
* The describe result will appear in the new view

## Generate sObject SOQL Step by Step
* Click ```Utilities``` > ```Generate sObject SOQL``` in the main menu
* Choose a sObject in the quick panel and press <kbd>Enter</kbd>
* The sObject SOQL will appear in the new view

## Pretty JSON Step by Step
* Click ```Utilities``` > ```JSON Pretty``` in the main menu
* Input your JSON Body in the input panel and press <kbd>Enter</kbd>
* The Prettied JSON will appear in the new view

## Serialize JSON Step by Step
* Click ```Utilities``` > ```JSON Serialization``` in the main menu
* Input your JSON Body in the input panel and press <kbd>Enter</kbd>
* The Serialized JSON will appear in the new view

## Convert JSON to Apex
* See <a href="json2apex.md" target="_blank">Convert JSON to Apex</a>

## Create Package.xml Step by Step
* Choose the folder in which posit the package.xml
* Click ``HaoIDE > Create Package.xml`` in the sidebar menu
* You will see the created package.xml in it

## Combine Package.xml in folders to only one Step by Step
If we have many ``package.xml`` files, for example, every developer will have his/her own ``package.xml`` to deploy, or every requirement will have one ``package.xml`` file, at the last stage of project implementation, only one deployment is required, so, how can we combine these package.xml files to only one.

You may concern about the accuracy, don't worry, plugin will automatically help you remove the duplicated ones, sort them and generate the new package.xml for you.

You can do this combine like this,

* Drag all your folder which contains package.xml to sublime, then, 
* Choose all of them and click ``Combine Package.xml`` in the sidebar menu, then, 
* Input the output path to contain the combined package.xml and press <kbd>Enter</kbd>, then,
* You will see the combined package.xml in the input path

