# Salesforce Document Quick Reference
I get the idea idea from [Salesforce Referencee](https://github.com/Oblongmana/sublime-salesforce-reference) and added some feature based on it.

Click the ```HaoIDE``` > ```Document``` > ```Reload Salesforce Reference``` in the main menu, you need to confirm whether continue, after you confirmed it, then wait for a moment until the ```Open Document``` command is enabled, at this moment, you can press <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>O</kbd> or Click it to invoke the ```Open Document``` command, nearly all reference api will be shown in the list, you can try to choose any one and it will be opened in browser.

There is default ```docs``` settings, if you want to add some other document reference to here, you can customize it yourself.
```
"docs": {
    "apexcode": {
       "catalog": "Apex",
       "pattern": "*[@Title='Reference'].//TocEntry[@DescendantCount='0'].."
    },
    ...
},
```
+ **apexdoc**: the part in ```http://www.salesforce.com/us/developer/docs/apexdoc/Data/Toc.xml```, you can get the ```apexdoc``` from Salesforce documents link
+ **Apex**: the document prefix in the quick search panel
+ **pattern**: the XPath pattern for parse the content from the response

**You should be aware that every reloading is time-consuming, generally, you should reload it in every salesforce release**