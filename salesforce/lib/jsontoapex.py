import re

mappings = {
    "bool": "Boolean",
    "date": "Date",
    "datetime": "DateTime",
    "str": "String",
    "float": "Decimal",
    "int": "Integer",
    "list": "List",
    "dict": "JSON",
    "NoneType": "Object"
}

class JSONConverter():
    """ Example: 
        import sublime
        from .salesforce.lib.jsontoapex import JSONConverter
        converter = JSONConverter()
        converter.convert2apex("Student", jsonstr)
        view = sublime.active_window().new_file()
        view.run_command("new_view", {
            "name": "JSON2APEX",
            "input": "\n".join(converter.classes)
        })
    """
    def __init__(self):
        self.classes = []

    def upcase_first_letter(self, s):
        return s[0].upper() + s[1:]

    def convert2apex(self, name, jsonstr):
        if isinstance(jsonstr, list):
            if len(jsonstr) == 0:
                self.classes.append("public class %s {\n\n}\n" % name)
                return
            else:
                jsonstr = jsonstr[0]

        if isinstance(jsonstr, dict):
            statements = []
            for key, value in jsonstr.items():
                data_type = type(value).__name__
                if data_type == "str":
                    if re.match("\d{4}-\d{2}-\d{2}T[\d:Z.]+", value):
                        data_type = "datetime"
                    elif  re.match("\d{4}-\d{2}-\d{2}", value):
                        data_type = "date"

                if data_type == "dict":
                    statements.append("\tpublic {type} {name};".format(
                        type=self.upcase_first_letter(key), name=key
                    ))

                    self.convert2apex(self.upcase_first_letter(key), jsonstr[key])

                elif data_type == "list":
                    statements.append("\tpublic List<{type}> {name};".format(
                        type=self.upcase_first_letter(key), name=key
                    ))

                    if not jsonstr[key]:
                        self.classes.append("public class %s {\n\n}\n" % self.upcase_first_letter(key))
                    else:
                        self.convert2apex(self.upcase_first_letter(key), jsonstr[key][0])

                else:
                    statements.append("\tpublic {type} {name};".format(
                        type=mappings[data_type], name=key
                    ))

            _class = "public class {name} {{\n{class_variable}\n}}\n".format(
                name=name, class_variable="\n".join(statements)
            )

            if _class not in self.classes:
                self.classes.append(_class)