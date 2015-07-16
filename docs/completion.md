## Completions
* Visualforce Components Completion
* HTML Standard Tag Completion
* Apex Code Completion
* Package.xml Completion

### Visualforce Page Completion
  * Standard Visualforce Component
    - Component Name Completion
      + After input ``<`` in visualforce page, plugin will list all standard components
      + After input tag prefix, for example, ``<apex:`` or ``<chatter:``, plugin will list all related suffixes
    <hr />
    - Component Attribute Completion
      + Input ``space`` after tage name, for example, ``<apex:page``, you will see all the related attributes of this component
    <hr />
    - Component Attribute Value Completion
      + Input ``=`` after attribute name, if this attribute has fixed values, plugin will list all available values for it, for example, if you input ``<apex:pageBlock mode=``, plugin will list four available values, ``detail, maindetail, edit, inlineEdit``
    <hr />
    - Sobject names and custom classes completion
      * If you input ``<apex:page standardController=""``, you will see plugin list all available sObjects
      * If you input ``<apex:page extension=""`` or ``<apex:page controller=""``, you will see plugin list all available custom classes
    <hr />
    - Quick creation for controller or extension
      * Input ``#`` after controller or extension name, if it is already exist, plugin will show you the error message, otherwise, plugin will create the controller or extension for you
    <hr />
    - Custom Field Completion in visualforce Page
      + After input ``acc.``, if acc is defined as ``Account`` Type in the corresponding controller or extension, plugin will list the available fields and relationship names
    <hr />
  * Custom Component
    - After input ``<c:``, plugin will list all custom component names in the components directory if exists
    - After input ``space`` after ``<c:compnentName>, plugin will read attributes from the corresponding component file if exists

### HTML Standard Tag Completion
  * Sublime has the build-in html completion, in order to avoid conflict, this feature is disabled by default, you can open it by setting ``disable_html_completion`` to ``false``
  * It have three types of completion, just similar with visualforce completion,
    - After input ``<`` in visualforce page, plugin will list all standard HTML tag names
    - Input ``space`` after HTML tag name, for example, ``<a``, you will see all the attributes of this tags
    - Input ``=`` after the HTML tag attribute, if this attributes has fixed values, plugin will list all available values for this tag attribute

### Settings for Visualforce and HTML completion
```json
    // Indicate whether disable attribute completion
    "disable_component_attribute_completion": false,

    // Flag to disable attribute value completion
    "disable_component_attribute_value_completion": false,

    // Flag to disable custom component attributes completion in visualforce page
    "disable_custom_component_completion": false,

    // Flag to disable apex variable completion in visualforce page
    "disable_apex_completion_in_visualforce": false,

    // Indicate whether disable html completion, 
    // Because sublime text has the default html completion code,
    // so this feature is disabled by default
    "disable_html_completion": true
```

### Apex Code Completion
* Keyword completion
* Stand Class Completion
* Custom Class Completion
* Sobject fields completion
    - [EU] notation for field, ``E`` means External, ``U`` means Unique
* Sobject relationship name completion
* Sobject relationship fields completion
* Picklist value completion after input ``Account.Type =``
* Visualforce page completion after input ``page.``
* [SOQL Fields completion](https://github.com/xjsender/SublimeApexScreenshot/raw/master/BuildSOQL.gif)
* [All demos](https://github.com/xjsender/SublimeApexScreenshot/raw/master/Completions.gif)

### Package.xml Completion
* Before building ``package.xml``, you must ``reload project cache`` to ensure package.xml completion is working,
* You can choose the folder in the sidebar and click right mouse to open sidebar menu, and then, you can execute ``HaoIDE > Create Package.xml`` command to create a basic package file
* It have two types of completion
  - Input ``types`` in the package.xml, and then hit <kbd>tab</kbd>, you will see below text is inserted to cursor point, at this time, when you can input the metadata object name in the current cursor point, plugin will list all available metadata objects, you can choose that you want to insert to current context
  ```xml
  <types>
    <members></members>
    <name>Cursor Here</name>
  </types>
  ```
  - After metadata object is input, press <kbd>tab</kbd>, current cursor point will be moved to point between ``<members>`` and ``</members>``, when you input any character, plugin will list the matched available component names
  - If you want to add more members, you can hit <kbd>tab</kbd> and then <kbd>Enter</kbd> after input your component name, you will current cursor is changed to next new line, you can type ``mem`` and hit <kbd>tab</kbd>, ``<members></members>`` will be inserted to context, you can continue the second step as above
