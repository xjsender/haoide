# Lightning Web Component  
 Lightning web components (`lwc`) are custom HTML elements built using HTML and modern JavaScript.

**This feature works when api version is >= 45.0**

 ## Create Lightning Web Component

Create `lwc` by clicking `HaoIDE -> New -> New Lightning Web Component` from the menu, 
and inputting the valid `lwc` name.

For better convenience, will create the `lwc` as `LightningComponentBundle` with three `LwcResources` 
-- HTML file, JavaScript file and configuration file under the component's folder.

 ```
 myComponent
   ├──myComponent.html
   ├──myComponent.js
   └──myComponent.js-meta.xml
```

## Add CSS File
From the component folder or file's sidebar context menu, 
click `HaoIDE -> Create Lwc Style`.

## Add SVG Icon
From the component folder or file's sidebar context menu, 
click `HaoIDE -> Create Lwc SVG`.

## Add Additional JavaScript File(s)

You can create Additional JavaScript files under the component's folder by yourself.

Notice:  
>These additional JavaScript files must be ES6 modules and must have names that are unique within the component’s folder.

## Component Tests

You can create Jest tests files following the official guide by yourself:

>To create Jest tests for a component, create a folder called `__tests__` at the top level of the component’s folder. 
Save the tests inside the `__tests__` folder.  
Test files must have names that end in “.js”, and we recommend that tests end in “.test.js. 
>You can have a single test file with all of your component tests, or you can have multiple files to organize related tests. Test files can be placed in sub folders.
## Retrieve Bundle/File
Two Approaches:

1. From the component folder or file's sidebar context menu, 
click `HaoIDE -> Retrieve Lightning From Server`.
2. From the opened component file's context menu, click `HaoIDE -> Retrieve From Server` or
`HaoIDE -> Retrieve From This Server`.

## Deploy Bundle/File
Two Approaches:

1. From the component folder or file's sidebar context menu, 
click `HaoIDE -> Deploy Lightning From Server`.
2. From the opened component file's context menu, click `HaoIDE -> Deploy To Server` or
`HaoIDE -> Deploy To This Server`.

## Save Component File to Server
`lwc`'s HTML markup, JavaScript code, CSS file, SVG resource, additional JS files
can save to Salesforce as `LightningComponentResource` separately.

From the opened component file's context menu, click `HaoIDE -> Deploy From Server` or
`HaoIDE -> Save To Server`. or simply press `ctrl+alt+s`(Windows).

If you cannot save certain file to server, try retrieving it from server first.

**Notice:**
XML configuration file (`js-meta.xml`) cannot save to server since the Metadata API does not support it.

## Destruct Component
Two Approaches:

1. From the component folder or file's sidebar context menu, 
click `HaoIDE -> Destruct Lightning From Server`.
2. From the opened component file's context menu, click `HaoIDE -> Destruct From Server`.

## Reference
[Lightning Web Components Developer Guide][1]

[1]: https://developer.salesforce.com/docs/atlas.en-us.lwc.meta/lwc/lwc_intro.htm