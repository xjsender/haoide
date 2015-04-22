# Exceute Rest Test
Up to now, support ```Get```, ```Post```, ```Put```, ```Patch```, ```Delete```, ```Tooling Query```, ```Query```, ```Query All```, ```Head```, ```Retrieve Body```, ```Search``` and ```Quick Search``` methods.

for example, 

+ **Query Sample**, you can input ```SELECT Id, Name FROM Account LIMIT 1``` and choose it, choose the intput SOQL, and then click ```Execute Rest Test``` in the context menu, choose the ```Query``` in the popup menu, wait for a moment, the queried json result will be shown in the new view.
```
{
    'done': True,
    'records': [{
        'Id': '001O000000M1mPwIAJ',
        'Name': '周星驰',
        'attributes': {
            'type': 'Account',
            'url': '/services/data/v30.0/sobjects/Account/001O000000M1mPwIAJ'
        }
    }],
    'totalSize': 1
}
```

+ **Query With Wildcard Character***, you can input ```SELECT * FROM Account LIMIT 1``` and choose it, choose the intput SOQL, and then click ```Execute Rest Test``` in the context menu, choose the ```Query``` in the popup menu, wait for a moment, the queried json result will be shown in the new view.
```
{
    'done': True,
    'records': [{
        'Id': '001O000000M1mPwIAJ',
        'Name': '周星驰',
        ....
        'attributes': {
            'type': 'Account',
            'url': '/services/data/v30.0/sobjects/Account/001O000000M1mPwIAJ'
        }
    }],
    'totalSize': 1
}
```

+ **Tooling Query Sample**, you can input ```SELECT Id, Name FROM ApexClass``` and choose it, choose the intput SOQL, and then click ```Execute Rest Test``` in the context menu, choose the ```Tooling Query``` in the popup menu, wait for a moment, the queried json result will be shown in the new view.

+ **Post Sample**: you can input ```/sobjects/Account``` and choose it, click ```Execute Rest Test``` in the context menu, choose the ```Post``` in the popup menu and input the json ```{"Name": "Test Rest Test"}``` in the input panel, wait for a moment, the inserted new account will be shown in the new view.
```
{
    'errors': [],
    'id': '001O000000MIiSXIA1'
}
```

+ **Get Sample**: input ```/sobjects/Account/001O000000MIiSXIA1``` and choose it, click ```Execute Rest Test``` in the context menu, choose the ```Get``` in the popup menu, wait for a moment, the detail information of the specified Id will be shown in the new view:
```
{
    'BillingAddress': {
        'city': None,
        'country': 'United States',
        ...
    },
    'BillingCity': None,
    'BillingCountry': 'United States',
    'BillingCountryCode': 'US',
    ...
}
```

+ **Delete Sample**: input ```/sobjects/Account/001O000000MIiSXIA1``` and choose it, click ```Execute Rest Test``` in the context menu, choose the ```Delete``` in the popup menu, wait for a moment, the delete result will be shown in the new view:
```
{}
```

+ **Patch Sample**: Sometimes, you want to update some fields of record, you can input ```/sobjects/Account/001O000000MIiSXIA1``` and choose it, click ```Execute Rest Test``` in the context menu, choose the ```Patch``` in the popup menu and input ```{"Name": "Test Path"}``` in the input panel, wait for a moment, the patch result will be shown in the new view:
```
{}
```

+ **Search Sample**: Sometimes, want to test search action, you can input ```FIND {test}``` and choose it, click ```Execute Rest Test``` in the context menu, choose the ```Search``` in the popup menu, wait for a moment, the patch result will be shown in the new view:
```
[{
    'Id': '001O0000001OWv5IAG',
    'attributes': {
        'type': 'Account',
        'url': '/services/data/v29.0/sobjects/Account/001O0000001OWv5IAG'
    }
}]
```

+ **Quick Search Sample**: Sometimes, want to search something, you can input ```test``` and choose it, click ```Execute Rest Test``` in the context menu, choose the ```Quick Search``` in the popup menu, wait for a moment, the patch result will be shown in the new view:
```
[{
    'Id': '001O0000001OWv5IAG',
    'attributes': {
        'type': 'Account',
        'url': '/services/data/v29.0/sobjects/Account/001O0000001OWv5IAG'
    }
}]
```