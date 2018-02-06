# Salesforce Document Quick Reference
I get the idea idea from [Salesforce Referencee](https://github.com/Oblongmana/sublime-salesforce-reference) and added some feature based on it.

Click the ```HaoIDE``` > ```Document``` > ```Reload Salesforce Reference``` in the main menu, you need to confirm whether continue, after you confirmed it, then wait for a moment until the ```Open Document``` command is enabled, at this moment, you can press <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>O</kbd> or Click it to invoke the ```Open Document``` command, nearly all reference api will be shown in the list, you can try to choose any one and it will be opened in browser.

This is default ```docs``` settings, if you want to add some other document references to here, you can customize it by yourself, for example, 
+ In the below sample, you can see "Apex Developer Guide": "apexcode" key-value,
+ The key can be any meaningful words, which is used in quick panel
+ The value can be found in https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_dev_guide.htm
```
"docs" : {
    "Apex Developer Guide": "apexcode",
    "AJAX Toolkit Developer Guide": "ajax",
    "Salesforce Reports and Dashboards REST API Developer Guide": "api_analytics",
    "Analytics Cloud Dashboard JSON": "bi_dev_guide_json",
    "Visualforce Developer Guide": "pages",
    "Streaming API Developer Guide": "api_streaming",
    "Salesforce Security Guide": "securityImplGuide",
    "Bulk API Developer Guide": "api_asynch",
    "REST API Developer Guide": "api_rest",
    "Open CTI Developer Guide": "api_cti",
    "Tooling API Developer Guide": "api_tooling",
    "SOAP API Developer Guide": "api",
    "Industries REST API Developer Guide": "api_rest_industries",
    "Chatter REST API Developer Guide": "chatterapi",
    "Metadata API Developer Guide": "api_meta",
    "Console Integration Toolkit Developer Guide": "api_console",
    "Object Reference": "object_reference",
    "SOQL and SOSL Reference": "soql_sosl",
    "Lightning Components Developer Guide": "lightning",
    "Development Lifecycle Guide": "dev_lifecycle",
    "Migration Tool Guide": "daas",
    "Force.com Workbook": "workbook",
    "Integration Workbook": "integration_workbook",
    "Identity Implementation Guide": "identityImplGuide",
    "Formulas Quick Reference": "salesforce_formulas_cheatsheet"
}
```

**You should be aware that every reloading is time-consuming, generally, you should reload it in every salesforce release**