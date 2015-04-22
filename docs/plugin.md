# Plugin Operation

## Execute Query
After any snippet which start with SELECT is chosen, you can press <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Q</kbd> in windows or click ```HaoIDE``` > ```Execute Query```, the queried json result will be formated and shown in a new view.

## Keep Operation History
By default, the operation of ```Execute Query```, ```Describe sObject```, ```Gernate SOQL```, ```Execute Anonymous``` and ```Run Test``` will be kept into the ```.history``` path in current project, you can disable this feature by setting ```keep_operation_history``` to false

## Difference between Deploy to Server and Save to Server
* ```Deploy to Server``` use ```Metdata API``, which can be mainly used to deploy files to other different orgs.
* ```Save to Server``` use ```tooling API```, which can't be used in production org.

## Keep Apex Code Local History
When you save code, this plugin will keep the change after you saved it to server successfully.

You can close this feature by change ```keep_local_history_change``` settings to false and put it into your own ``user settings``

## Quick Goto Component
Put the focus in the Class Name, and then, press <kbd>shift</kbd>,  and click ```button1``` for twice, the class file will be open in background if this class file is exist, however, if you want to open this class in the foreground, you should press <kbd>shift</kbd> and click ```button1``` for triple.