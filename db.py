import threading
import time
import os
import json
import sublime
from . import requests, context, util
from .salesforce.api.tooling import ToolingApi

type_map = {
    "datetime": {
        "oracle": {
            "type": "{name} date",
            "field_attrs": ["name"]
        },
        "mysql": {
            "type": "{name} date",
            "field_attrs": ["name"]
        }
    },

    "date": {
        "oracle": {
            "type": "{name} date",
            "field_attrs": ["name"]
        },
        "mysql": {
            "type": "{name} date",
            "field_attrs": ["name"]
        }
    },

    "base64": {
        "oracle": {
            "type": "{name} CLOB",
            "field_attrs": ["name"]
        },
        "mysql": {
            "type": "{name} MEDIUMTEXT",
            "field_attrs": ["name"]
        }
    },

    "address": {
        "oracle": {
            "type": "{name} CLOB",
            "field_attrs": ["name"]
        },
        "mysql": {
            "type": "{name} MEDIUMTEXT",
            "field_attrs": ["name"]
        }
    },

    "text": {
        "oracle": {
            "type": "{name} CLOB",
            "field_attrs": ["name"]
        },
        "mysql": {
            "type": "{name} text",
            "field_attrs": ["name"]
        }
    },

    "textarea": {
        "oracle": {
            "type": "{name} CLOB",
            "field_attrs": ["name"]
        },
        "mysql": {
            "type": "{name} MEDIUMTEXT",
            "field_attrs": ["name"]
        }
    },

    "double": {
        "oracle": {
            "type": "{name} number({precision}, {scale})",
            "field_attrs": ["name", "precision", "scale"]
        },
        "mysql": {
            "type": "{name} numeric({precision}, {scale})",
            "field_attrs": ["name", "precision", "scale"]
        }
    },

    "int": {
        "oracle": {
            "type": "{name} number",
            "field_attrs": ["name"]
        },
        "mysql": {
            "type": "{name} numeric",
            "field_attrs": ["name"]
        }
    },

    "percent": {
        "oracle": {
            "type": "{name} number({precision}, {scale})",
            "field_attrs": ["name", "precision", "scale"]
        },
        "mysql": {
            "type": "{name} numeric({precision}, {scale})",
            "field_attrs": ["name", "precision", "scale"]
        }
    },

    "currency": {
        "oracle": {
            "type": "{name} number({precision}, {scale})",
            "field_attrs": ["name", "precision", "scale"]
        },
        "mysql": {
            "type": "{name} numeric({precision}, {scale})",
            "field_attrs": ["name", "precision", "scale"]
        }
    },

    "picklist": {
        "oracle": {
            "type": "{name} varchar2({length})",
            "field_attrs": ["name", "length"]
        },
        "mysql": {
            "type": "{name} varchar({length})",
            "field_attrs": ["name", "length"]
        }
    },

    "string": {
        "oracle": {
            "type": "{name} varchar2({length})",
            "field_attrs": ["name", "length"]
        },
        "mysql": {
            "type": "{name} varchar({length})",
            "field_attrs": ["name", "length"]
        }
    },

    "boolean": {
        "oracle": {
            "type": "{name} varchar2(20 char)",
            "field_attrs": ["name"]
        },
        "mysql": {
            "type": "{name} varchar(20)",
            "field_attrs": ["name"]
        }
    },

    "reference": {
        "oracle": {
            "type": "{name} varchar2(18 char)",
            "field_attrs": ["name"]
        },
        "mysql": {
            "type": "{name} varchar(18)",
            "field_attrs": ["name"]
        }
    },

    "email": {
        "oracle": {
            "type": "{name} varchar2({length} char)",
            "field_attrs": ["name", "length"]
        },
        "mysql": {
            "type": "{name} varchar({length})",
            "field_attrs": ["name", "length"]
        }
    },

    "id": {
        "oracle": {
            "type": "{name} varchar2(18 char) primary key",
            "field_attrs": ["name"]
        },
        "mysql": {
            "type": "{name} varchar(18) primary key",
            "field_attrs": ["name"]
        }
    },

    "multipicklist": {
        "oracle": {
            "type": "{name} varchar2({length} char)",
            "field_attrs": ["name", "length"]
        },
        "mysql": {
            "type": "{name} text",
            "field_attrs": ["name"]
        }
    },

    "phone": {
        "oracle": {
            "type": "{name} varchar2({length} char)",
            "field_attrs": ["name", "length"]
        },
        "mysql": {
            "type": "{name} varchar({length})",
            "field_attrs": ["name", "length"]
        }
    },

    "url": {
        "oracle": {
            "type": "{name} varchar2({length} char)",
            "field_attrs": ["name", "length"]
        },
        "mysql": {
            "type": "{name} varchar({length})",
            "field_attrs": ["name", "length"]
        }
    },

    "complexvalue": {
        "oracle": {
            "type": "{name} varchar2",
            "field_attrs": ["name"]
        },
        "mysql": {
            "type": "{name} varchar(200)",
            "field_attrs": ["name"]
        }
    },

    "anyType": {
        "oracle": {
            "type": "varchar2",
            "field_attrs": ["name"]
        },
        "mysql": {
            "type": "{name} varchar(200)",
            "field_attrs": ["name"]
        }
    },

    "combobox": {
        "oracle": {
            "type": "{name} varchar2({length} char)",
            "field_attrs": ["length"]
        },
        "mysql": {
            "type": "{name} varchar({length})",
            "field_attrs": ["length"]
        }
    }, 

    "time": {
        "oracle": {
            "type": "{name} varchar2",
            "field_attrs": ["name"]
        },
        "mysql": {
            "type": "{name} varchar(200)",
            "field_attrs": ["name"]
        }
    },

    "double": {
        "oracle": {
            "type": "{name} number({precision}, {scale})",
            "field_attrs": ["name", "precision", "scale"]
        },
        "mysql": {
            "type": "{name} numeric({precision}, {scale})",
            "field_attrs": ["name", "precision", "scale"]
        }
    }
}

def build_sql(sobject_desc, database="mysql", prefix=""):
    field_statments = []
    database_table = prefix + sobject_desc["name"]
    for field in sobject_desc["fields"]:
        sf_field_type = field["type"]

        # Exclude location compound field
        if sf_field_type == "location":
            continue

        # 如果string类型length超过4000，则使用BLOB或者CLOB
        if field["length"] >= 1300:
            sf_field_type = "text"

        db = type_map[sf_field_type].get(database, {})
        if not db:
            print (sf_field_type)
            continue

        field_attrs_val = {}
        for attr in db["field_attrs"]:
            field_attrs_val[attr] = field[attr]

        field_statement = db["type"].format(**field_attrs_val)

        # add Normal statement
        field_statments.append("\t" + field_statement)


    sql = ""
    if database == "mysql":
        sql = "drop table if exists %s;\n" % database_table
    sql += "create table %s (\n%s\n\t);\n" % (
        database_table,
        ",\n".join(field_statments)
    )

    return sql

exclude_reference_fields = [
    "OwnerId", "CreatedById",
    "LastModifiedById"
]

exclude_foreign_objects = [
    "ProcessDefinition", "ProcessInstance", 
    "ProcessNode", "UserLicense", 
    "BusinessProcess", "CallCenter", 
    "Organization", "Group", "Folder", 
    "BrandTemplate", "DandBCompany", "Individual",
    "OperatingHours"
]
def build_foreign_key(sobject_desc, database="mysql", prefix=""):
    database_table = prefix + sobject_desc["name"]

    foreign_keys = []
    for field in sobject_desc["fields"]:
        # Exclude non-reference field
        if field["type"] != "reference":
            continue

        # 排除部分标准的外键关联
        if field["name"] in exclude_reference_fields:
            continue

        # 排除部分对象的外键关联
        if field["referenceTo"][0] not in exclude_foreign_objects:
            referenceTo = prefix + field["referenceTo"][0]
            foreign_keys.append({
                "table": database_table,
                "constraint": "pk_%s_%s" % (database_table, field["relationshipName"]),
                "foreign_key": field["name"],
                "references": referenceTo,
                "drop_word": "FOREIGN KEY" if database == "mysql" else "CONSTRAINT"
            })

    statements = []
    for foreign_key in foreign_keys:
        foreign_key_statement = """
            alter table {table}
            drop {drop_word} {constraint};

            alter table {table}
            add CONSTRAINT {constraint} 
            FOREIGN KEY({foreign_key}) 
            REFERENCES {references}(id);
        """.format(
            **foreign_key
        )
        statements.append(foreign_key_statement)

    return "\n".join(statements)


def build_soql(sobject_desc):
    sobject_name = sobject_desc["name"]
    fields = [f["name"] for f in sobject_desc["fields"]]

    soql = "SELECT %s FROM %s" % (
        ", ".join(fields), sobject_name
    )

    return soql


def start_job(sobjects=[], prefix=""):
    settings = context.get_settings()
    api = ToolingApi(settings)

    # if no specified sobjects, describe all
    if not sobjects:
        sobjects = []
        result = api.describe_global()
        if not result["success"]:
            print (result)
            return

        for sobject_desc in result.get("sobjects"):
            sobjects.append(sobject_desc["name"])

    rows = ["label,name,soql,oracle,mysql,foreign key"]
    for sobject in sobjects:
        print (sobject)
        sobject_field_desc = api.describe_sobject(sobject)
        rows.append(
            '"%s","%s","%s","%s","%s","%s"' % (
                sobject_field_desc["label"], 
                sobject_field_desc["name"], 
                build_soql(sobject_field_desc),
                build_sql(sobject_field_desc, database="oracle", prefix=prefix),
                build_sql(sobject_field_desc, database="mysql", prefix=prefix),
                build_foreign_key(sobject_field_desc, prefix=prefix)
            )
        )
    
    outputdir = os.path.join(settings["workspace"], ".export")
    if not os.path.exists(outputdir): 
        os.makedirs(outputdir)
    outputfile = os.path.join(outputdir, "bcm.csv")
    with open(outputfile, "wb") as fp:
        fp.write("\n".join(rows).encode("utf-8"))

    view = sublime.active_window().open_file(outputfile)

sobjects = [
    "Account",
    "Opportunity",
    "Contact",
    "OpportunityLineItem",
    "User",
    "UserRole",
    "Profile",
    "Pricebook2",
    "PricebookEntry",
    "Product2"
]
thread = threading.Thread(target=start_job, args=(sobjects, "", ))
# thread.start()