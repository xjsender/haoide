# Export
You can export somethings in your org to CSV by these features

* Export CustomFields
    - Click ```HaoIDE``` > ```Export``` > ```Export CustomField```
    - ``CustomFields`` will be exported to ``Project/.export/CustomFields.csv``

* Export Workflow Rules
    - Download metadata of ``sObjects and Workflow`` by clicking ```Migration``` > ```Retrieve Sobject And Workflow``` in the main menu
    - Click ```Export``` > ```Export Workflow``` in the main menu to backup all workflows in your org to csv
    - ```workflow_rule_columns```, ``workflow_field_update_columns``, ``workflow_email_alert_columns``, ``workflow_outbound_message_columns`` and ``workflow_task_columns`` defines the columns of export CSV, you can adjust the sequence and columns by customizing your own value of this five settings

* Export Validation Rules
    - Download metadata of ``sObjects and Workflow`` by clicking ```Migration``` > ```Retrieve Sobject And Workflow``` in the main menu
    - Click ```Export``` > ```Export Validation Rule``` in the main menu
    - All ValidationRules in your org will be exported to ``Project/.export/ValidationRules.csv``
    - ```validation_rule_columns``` setting defines the columns of export CSV, you can adjust the sequence and columns by customizing your own value of this setting

* Export Profile Workbook
    - Retrieve all metadata by clicking ``Metadata Migration`` > ``Retrieve All`` in the main menu to download all related components.
    - Click ``HaoIDE`` > ``Export`` > ``Export Profile`` in the main menu to export ``ObjectPermission``, ``TabVisibilities``, ``FieldLevelSecurity`` and ``UserPermissions`` of all profiles to four different CSV files, you can check below sample CSVs.
    - Exported profile csv from sample org
        + [FieldLevelSecurity.csv](https://github.com/xjsender/SublimeApexScreenshot/blob/master/CSV/Profile/FieldLevelSecurity.csv)
        + [ObjectPermissions.csv](https://github.com/xjsender/SublimeApexScreenshot/blob/master/CSV/Profile/ObjectPermissions.csv)
        + [TabVisibilities.csv](https://github.com/xjsender/SublimeApexScreenshot/blob/master/CSV/Profile/TabVisibilities.csv)
        + [UserPermissions.csv](https://github.com/xjsender/SublimeApexScreenshot/blob/master/CSV/Profile/UserPermissions.csv)

* Export Workbook of sobjects
    - Click ``Export`` > ``Export Workbook`` in the main menu
    - Input * to export all sObject workbooks
    - Input sObject Names separated with semi-colon to export some
    - ``workbook_field_describe_columns`` setting define the columns

* Export Data Template
    - Click ``Export`` > ``Export Data Template`` in the main menu
    - Waiting until ``sObject => RecordType`` quick panel is open
    - Choose one and press <kbd>Enter</kbd> and template will be exported
    - From the row 1 to row 6, they are,
        + [Field Label]...
        + [Field API]...
        + [Field Type]...
        + [Layout Required]...
        + [Picklist Label if has]...
        + [Picklist Value if has]