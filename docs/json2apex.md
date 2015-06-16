# Convert JSON to Apex Step by Step
* Click ```Utilities``` > ```Convert JSON to Apex``` in the main menu
* Default class name of main class is ```JSON2Apex```, after you input the JSON to be converted, plugin will ask you to input the class name, you can change the default name there.
* In order to keep the accuracy of converted result, you should predefine the every value of every key in the input JSON

## Notes:
+ [x] If value is matched with ```\d{4}-\d{2}-\d{2}T[\d:Z.]+``` regress expression, data type will be thought as ```DateTime```
+ [x] If value is matched with ```\d{4}-\d{2}-\d{2}``` regress expression, data type will be thought as ```Date```
+ [x] If value is ```null```, data type will be thought as ```Object```

## Example:
If the json string is as below,
```javascript
{
    "name": "test",
    "birthday": "1982-01-19T09:58:13.190Z",
    "age": 32, 
    "money": 12321.5,
    "createdDate": "2015-01-20",
    "children": [
        {
            "name": "son",
            "age": 2,
            "birthday": "2013-01-19T09:58:13.190Z",
            "money": 0, 
            "toy": [{
                "name": "toy1"
            }]
        },
        {
            "name": "daughter",
            "age": 1,
            "birthday": "2014-01-19T09:58:13.190Z",
            "money": 0,
            "toy": [{
                "name": "toy2"
            }]
        }
    ],
    "father": {
        "name": "father",
        "age": 75,
        "birthday": "1940-01-19T09:58:13.190Z",
        "money": 0
    }
}
```

The converted apex will be as below:
```java
global class Toy {
    global String name;
}

global class Children {
    global String name;
    global List<Toy> toy;
    global Integer age;
    global Integer money;
    global DateTime birthday;
}

global class Father {
    global String name;
    global Integer age;
    global Integer money;
    global DateTime birthday;
}

global class JSON2Apex {
    global List<Children> children;
    global Date createdDate;
    global Integer age;
    global Decimal money;
    global String name;
    global Father father;
    global DateTime birthday;
}

global static JSON2Apex parse(String jsonStr) {
    return (JSON2Apex) JSON.deserialize(jsonStr, JSON2Apex.class);
}

static testMethod void testParse() {
    String json = '{"children": [{"name": "son", "toy": [{"name": "toy1"}], "age": 2, "money": 0, "birthday": "2013-01-19T09:58:13.190Z"}, {"name": "daughter", "toy": [{"name": "toy2"}], "age": 1, "money": 0, "birthday": "2014-01-19T09:58:13.190Z"}], "createdDate": "2015-01-20", "age": 32, "money": 12321.5, "name": "test", "father": {"name": "father", "age": 75, "money": 0, "birthday": "1940-01-19T09:58:13.190Z"}, "birthday": "1982-01-19T09:58:13.190Z"}';
    JSON2Apex obj = parse(json);
    System.assert(obj != null);
}
```