import re
import json

mappings = {
    "bool": "Boolean",
    "date": "Date",
    "datetime": "DateTime",
    "str": "String",
    "float": "Decimal",
    "int": "Integer",
    "NoneType": "Object"
}

class JSONConverter():
    """ Example: 
        from .salesforce.lib.jsontoapex import JSONConverter
        snippet = JSONConverter().convert2apex(name, jsonstr).snippet
    """
    def __init__(self, **args):
        self.classes = []
        self.snippet = None

        if "scope" in args:
            self.scope = args["scope"]

    def upcase_first_letter(self, s):
        return s[0].upper() + s[1:]

    def add_parser(self, name):
        parser = "{scope} static {name} parse(String jsonStr) {{\n" + \
            "\treturn ({name}) JSON.deserialize(jsonStr, {name}.class);\n" + \
        "}}\n"

        self.classes.append(parser.format(scope=self.scope, name=name))

    def add_testmethod(self, jsonStr):
        testmethod = "static testMethod void testParse() {{\n" + \
            "\tString json = '{jsonStr}';\n" + \
            "\tJSON2Apex obj = parse(json);\n" + \
            "\tSystem.assert(obj != null);\n" + \
            "}}\n"

        self.classes.append(testmethod.format(jsonStr=jsonStr))

    def convert2apex(self, name, dict_obj, level=0):
        if isinstance(dict_obj, list):
            if len(dict_obj) == 0:
                self.classes.append("%s class %s {{\n\n}}\n" % (
                    self.scope, name
                ))
                self.snippet = "\n".join(self.classes)[:-1]
                return self
            else:
                dict_obj = dict_obj[0]

        if isinstance(dict_obj, dict):
            statements = []
            for key, value in dict_obj.items():
                data_type = type(value).__name__
                if data_type == "str":
                    if re.match("\d{4}-\d{2}-\d{2}T[\d:Z.]+", value):
                        data_type = "datetime"
                    elif  re.match("\d{4}-\d{2}-\d{2}", value):
                        data_type = "date"

                if data_type == "dict":
                    statements.append("\t{scope} {type} {name};".format(
                        scope=self.scope, 
                        type=self.upcase_first_letter(key), 
                        name=key
                    ))

                    self.convert2apex(self.upcase_first_letter(key), dict_obj[key], 1)

                elif data_type == "list":
                    statements.append("\t{scope} List<{type}> {name};".format(
                        scope=self.scope, 
                        type=self.upcase_first_letter(key), 
                        name=key
                    ))

                    if not dict_obj[key]:
                        self.classes.append("{scope} class {name} {{\n\n}}\n".format(
                            scope=self.scope, 
                            name=self.upcase_first_letter(key)
                        ))
                    else:
                        self.convert2apex(self.upcase_first_letter(key), dict_obj[key][0], 1)

                else:
                    statements.append("\t{scope} {type} {name};".format(
                        scope=self.scope, 
                        type=mappings[data_type], 
                        name=key
                    ))

            _class = "{scope} class {name} {{\n{class_variable}\n}}\n".format(
                scope=self.scope, 
                name=name, 
                class_variable="\n".join(statements)
            )

            if _class not in self.classes:
                self.classes.append(_class)

            if level == 0:
                self.add_parser(name)
                self.add_testmethod(json.dumps(dict_obj))
                self.snippet = "\n".join(self.classes)[:-1]

        return self