# Attributes which type is ApexPages.PageReference
page_reference_attrs = [
    "page",
    "template",
    "pageName",
    "finishLocation"
]

tag_defs = {
    "aura:application": {
        "simple": False,
        "attribs": {
            "access": {
                "type": "Picklist",
                "values":[
                    "public",
                    "global"
                ]
            },
            "controller": {
                "type": "String"
            },
            "description": {
                "type": "String"
            },
            "implements": {
                "type": "String"
            },
            "useAppcache": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },

    "aura:component": {
        "simple": False,
        "attribs": {
            "access": {
                "type": "Picklist",
                "values":[
                    "public",
                    "global"
                ]
            },
            "controller": {
                "type": "String"
            },
            "description": {
                "type": "String"
            },
            "implements": {
                "type": "String"
            }
        }
    },

    "aura:dependency": {
        "simple": False,
        "attribs": {
            "resource": {
                "type": "String",
                "values": [
                    "markup://sampleNamespace:sampleComponent",
                    "markup://sampleNamespace:*",
                    "markup://sampleNamespace:input*"
                ]
            },
            "type": {
                "type": "Picklist",
                "values": [
                    "COMPONENT", "APPLICATION", "EVENT"
                ]
            }
        }
    },

    "aura:event": {
        "simple": False,
        "attribs": {
            "access": {
                "type": "Picklist",
                "values":[
                    "public",
                    "global"
                ]
            },
            "description": {
                "type": "String"
            },
            "extends": {
                "type": "String",
                "values": [
                    "namespace:myEvent"
                ]
            },
            "type": {
                "type": "Picklist",
                "values": [
                    "COMPONENT", "APPLICATION"
                ]
            }
        }
    },

    "aura:if": {
        "simple": False,
        "attribs": {
            "else": {
                "type": "ComponentDefRef[]"
            },
            "isTrue": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            }
        }
    },

    "aura:interface": {
        "simple": False,
        "attribs": {
            "access": {
                "type": "Picklist",
                "values":[
                    "public",
                    "global"
                ]
            },
            "description": {
                "type": "String"
            },
            "extends": {
                "type": "String",
                "values": [
                    "namespace:myEvent"
                ]
            }
        }
    },

    "aura:iteration": {
        "simple": False,
        "attribs": {
            "body": {
                "type": "ComponentDefRef[]"
            },
            "indexVar": {
                "type": "String"
            },
            "items": {
                "type": "List"
            },
            "var": {
                "type": "String"
            },
        }
    },

    "aura:renderIf": {
        "simple": False,
        "attribs": {
            "else": {
                "type": "ComponentDefRef[]"
            },
            "isTrue": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            }
        }
    },

    "aura:set": {
        "simple": False,
        "attribs": {
            "attribute": {
                "type": "String"
            },
            "value": {
                "type": "String"
            },
        }
    },

    "aura:attribute": {
        "simple": False,
        "attribs": {
            "access": {
                "type": "Picklist",
                "values":[
                    "public",
                    "global", "PRIVATE"
                ]
            },
            "name": {
                "type": "String"
            },
            "type": {
                "type": "Picklist",
                "values": [
                    "Boolean", "Date", "DateTime", "Decimal", 
                    "Double", "Integer", "Long", "String",
                    "Object", "List", "Set", "Map"
                ]
            },
            "default": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            },
            "required": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            },
            "description": {
                "type": "String"
            }
        }
    },

    "apex:attribute": {
        "simple": False,
        "attribs": {
            "access": {
                "type": "Picklist",
                "values":[
                    "public",
                    "global"
                ]
            },
            "assignTo": {
                "type": "Object"
            },
            "name": {
                "type": "String"
            },
            "type": {
                "type": "Picklist",
                "values": [
                    "Boolean", "Date", "DateTime", "Decimal", 
                    "Double", "Integer", "Long", "String", 
                    "Object"
                ]
            },
            "id": {
                "type": "String"
            },
            "encode": {
                "type": "String"
            },
            "default": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            },
            "required": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            },
            "description": {
                "type": "String"
            }
        }
    },

    # ChatterAnswer
    "chatteranswers:aboutme": {
        "simple": False,
        "attribs": {
            "communityId": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "noSignIn": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            }
        }
    },

    "chatteranswers:allfeeds": {
        "simple": False,
        "attribs": {
            "articleLanguage": {
                "type": "String"
            },
            "communityId": {
                "type": "id"
            },
            "filterOptions": {
                "type": "Picklist",
                "values":[
                    'AllQuestions', 'UnansweredQuestions', 
                    'UnsolvedQuestions', 'SolvedQuestions', 
                    'MyQuestions', 'MostPopular', 
                    'DatePosted', 'RecentActivity'
                ]
            },
            "forceSecureCustomWebAddress": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            },
            "id": {
                "type": "String"
            },
            "jsApiVersion": {
                "type": "Double"
            },
            "noSignIn": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            },
            "useUrlRewriter": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            }
        }
    },

    "chatteranswers:changepassword": {
        "simple": False,
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            }
        }
    },

    "chatteranswers:datacategoryfilter": {
        "simple": False,
        "attribs": {
            "communityId": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            }
        }
    },

    "chatteranswers:feedfilter": {
        "simple": False,
        "attribs": {
            "filterOptions": {
                "type": "Picklist",
                "values":[
                    'AllQuestions', 'UnansweredQuestions', 
                    'UnsolvedQuestions', 'SolvedQuestions', 
                    'MyQuestions', 'MostPopular', 
                    'DatePosted', 'RecentActivity'
                ]
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            }
        }
    },

    "chatteranswers:feeds": {
        "simple": False,
        "attribs": {
            "articleLanguage": {
                "type": "String"
            },
            "communityId": {
                "type": "id"
            },
            "id": {
                "type": "String"
            },
            "jsApiVersion": {
                "type": "Double"
            },
            "noSignIn": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            },
            "useUrlRewriter": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            }
        }
    },

    "chatteranswers:forgotpassword": {
        "simple": False,
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            },
            "useUrlRewriter": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            }
        }
    },

    "chatteranswers:forgotpasswordconfirm": {
        "simple": False,
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            },
            "useUrlRewriter": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            }
        }
    },

    "chatteranswers:guestsignin": {
        "simple": False,
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            },
            "useUrlRewriter": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            }
        }
    },

    "chatteranswers:help": {
        "simple": False,
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            }
        }
    },

    "chatteranswers:login": {
        "simple": False,
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            },
            "useUrlRewriter": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            }
        }
    },

    "chatteranswers:registration": {
        "simple": False,
        "attribs": {
            "hideTerms": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            },
            "id": {
                "type": "String"
            },
            "profileId": {
                "type": "id"
            },
            "registrationClassName": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            },
            "useUrlRewriter": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            }
        }
    },

    "chatteranswers:searchask": {
        "simple": False,
        "attribs": {
            "communityId": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "noSignIn": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            },
            "searchLanguage": {
                "type": "String"
            },
            "useUrlRewriter": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            }
        }
    },

    "chatteranswers:singleitemfeed": {
        "simple": False,
        "attribs": {
            "entityId": {
                "type": "id"
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            }
        }
    },

    # Messaging part
    "messaging:attachment": {
        "simple": False,
        "attribs": {
            "filename": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "inline": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            },
            "renderAs": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            }
        }
    },
    "apex:emailPublisher": {
        "attribs": {
            "autoCollapseBody": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "bccVisibility": {
                "type": "Picklist",
                "values": [
                    "editable",
                    "editableWithLookup",
                    "readOnly",
                    "hidden"
                ]
            },
            "ccVisibility": {
                "type": "Picklist",
                "values": [
                    "editable",
                    "editableWithLookup",
                    "readOnly",
                    "hidden"
                ]
            },
            "emailBody": {
                "type": "String"
            },
            "emailBodyFormat": {
                "type": "Picklist",
                "values": [
                    "text",
                    "HTML",
                    "textAndHTML"
                ]
            },
            "emailBodyHeight": {
                "type": "String"
            },
            "enableQuickText": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "entityId": {
                "type": "id"
            },
            "expandableHeader": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "fromAddresses": {
                "type": "String"
            },
            "fromVisibility": {
                "type": "Picklist",
                "values": [
                    "selectable",
                    "hidden"
                ]
            },
            "id": {
                "type": "String"
            },
            "onSubmitFailure": {
                "type": "String"
            },
            "onSubmitSuccess": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "reRender": {
                "type": "Object"
            },
            "sendButtonName": {
                "type": "String"
            },
            "showAdditionalFields": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "showAttachments": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "showSendButton": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "showTemplates": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "subject": {
                "type": "String"
            },
            "subjectVisibility": {
                "type": "Picklist",
                "values": [
                    "editable",
                    "readOnly",
                    "hidden"
                ]
            },
            "submitFunctionName": {
                "type": "String"
            },
            "title": {
                "type": "String"
            },
            "toAddresses": {
                "type": "String"
            },
            "toVisibility": {
                "type": "Picklist",
                "values": [
                    "editable",
                    "editableWithLookup",
                    "readOnly",
                    "hidden"
                ]
            },
            "verticalResize": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "width": {
                "type": "String"
            }
        }
    },
    "messaging:emailHeader": {
        "simple": False,
        "attribs": {
            "name": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            }
        }
    },
    "messaging:emailTemplate": {
        "simple": False,
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            },
            "language": {
                "type": "String"
            },
            "recipientType": {
                "type": "String"
            },
            "relatedToType": {
                "type": "String"
            },
            "replyTo": {
                "type": "String"
            },
            "subject": {
                "type": "String"
            }
        }
    },
    "messaging:htmlEmailBody": {
        "simple": False,
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            }
        }
    },
    "messaging:plainTextEmailBody": {
        "simple": False,
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            }
        }
    },

    # analytics part
    "analytics:reportChart": {
        "simple": False,
        "attribs": {
            "filter": {
                "type": "json",
                "values":[
                    '{"column": $1, "operator": $2, "value": $3}'
                ]
            },
            "hideOnError": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values":[
                    "true", "false"
                ]
            },
            "reportId": {
                "type": "String"
            },
            "size": {
                "type": "String"
            }
        }
    },

    "apex:actionFunction": {
        "simple": True,
        "attribs": {
            "action": {
                "type": "ApexPages.Action"
            },
            "focus": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "immediate": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "name": {
                "type": "String"
            },
            "onbeforedomupdate": {
                "type": "String"
            },
            "oncomplete": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "reRender": {
                "type": "String"
            },
            "status": {
                "type": "String"
            },
            "timeout": {
                "type": "Integer"
            }
        }
    },
    "apex:actionPoller": {
        "simple": True,
        "attribs": {
            "action": {
                "type": "ApexPages.Action"
            },
            "enabled": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "id": {
                "type": "String"
            },
            "interval": {
                "type": "Integer"
            },
            "oncomplete": {
                "type": "String"
            },
            "onsubmit": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "reRender": {
                "type": "String"
            },
            "status": {
                "type": "String"
            },
            "timeout": {
                "type": "Integer"
            }
        }
    },
    "apex:actionRegion": {
        "simple": False,
        "attribs": {
            "id": {
                "type": "String"
            },
            "immediate": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "renderRegionOnly": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "apex:actionStatus": {
        "simple": False,
        "attribs": {
            "dirs": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "for": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "layout": {
                "type": "Picklist",
                "values": [
                    "lineDirection",
                    "pageDirection"
                ]
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "onstart": {
                "type": "String"
            },
            "onstop": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "startStyle": {
                "type": "String"
            },
            "startStyleClass": {
                "type": "String"
            },
            "startText": {
                "type": "String"
            },
            "stopStyle": {
                "type": "String"
            },
            "stopStyleClass": {
                "type": "String"
            },
            "stopText": {
                "type": "String"
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "title": {
                "type": "String"
            }
        }
    },
    "apex:actionSupport": {
        "simple": True,
        "attribs": {
            "action": {
                "type": "ApexPages.Action"
            },
            "disabled": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "disableDefault": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "event": {
                "type": "Picklist",
                "values": [
                    "onblur",
                    "onchange",
                    "onclick",
                    "ondblclick",
                    "onfocus",
                    "onkeydown",
                    "onkeypress",
                    "onkeyup",
                    "onmousedown",
                    "onmousemove",
                    "onmouseout",
                    "onmouseover",
                    "onmouseup",
                    "onselect"
                ]
            },
            "focus": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "immediate": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "onbeforedomupdate": {
                "type": "String"
            },
            "oncomplete": {
                "type": "String"
            },
            "onsubmit": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "reRender": {
                "type": "String"
            },
            "status": {
                "type": "String"
            },
            "timeout": {
                "type": "Integer"
            }
        }
    },
    "apex:areaSeries": {
        "simple": False,
        "attribs": {
            "axis": {
                "type": "Picklist",
                "values": [
                    "bottom",
                    "left",
                    "right",
                    "top"
                ]
            },
            "colorSet": {
                "type": "String"
            },
            "highlight": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "highlightLineWidth": {
                "type": "Integer"
            },
            "highlightOpacity": {
                "type": "String"
            },
            "highlightStrokeColor": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "opacity": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rendererFn": {
                "type": "String"
            },
            "showInLegend": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "tips": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "title": {
                "type": "String"
            },
            "xField": {
                "type": "String"
            },
            "yField": {
                "type": "String"
            }
        }
    },
    "apex:axis": {
        "simple": False,
        "attribs": {
            "dashSize": {
                "type": "Integer"
            },
            "fields": {
                "type": "String"
            },
            "grid": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "gridFill": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "id": {
                "type": "String"
            },
            "margin": {
                "type": "Integer"
            },
            "maximum": {
                "type": "Integer"
            },
            "minimum": {
                "type": "Integer"
            },
            "position": {
                "type": "Picklist",
                "values": [
                    "bottom",
                    "gauge",
                    "left",
                    "radial",
                    "right",
                    "top"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "steps": {
                "type": "Integer"
            },
            "title": {
                "type": "String"
            },
            "type": {
                "type": "String",
                "values": [
                    "Category",
                    "Gauge",
                    "Numeric",
                    "Radial"
                ]
            }
        }
    },
    "apex:barSeries": {
        "simple": False,
        "attribs": {
            "axis": {
                "type": "Picklist",
                "values": [
                    "left",
                    "right",
                    "top",
                    "bottom"
                ]
            },
            "colorSet": {
                "type": "String"
            },
            "colorsProgressWithinSeries": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "groupGutter": {
                "type": "Integer"
            },
            "gutter": {
                "type": "Integer"
            },
            "highlight": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "highlightColor": {
                "type": "String"
            },
            "highlightLineWidth": {
                "type": "Integer"
            },
            "highlightOpacity": {
                "type": "String"
            },
            "highlightStroke": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "orientation": {
                "type": "Picklist",
                "values": [
                    "horizontal",
                    "vertical"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rendererFn": {
                "type": "String"
            },
            "showInLegend": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "stacked": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "tips": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "title": {
                "type": "String"
            },
            "xField": {
                "type": "String"
            },
            "xPadding": {
                "type": "Integer"
            },
            "yField": {
                "type": "String"
            },
            "yPadding": {
                "type": "Integer"
            }
        }
    },
    "apex:canvasApp": {
        "simple": True,
        "attribs": {
            "applicationName": {
                "type": "String"
            },
            "border": {
                "type": "String"
            },
            "canvasId": {
                "type": "String"
            },
            "containerId": {
                "type": "String"
            },
            "developerName": {
                "type": "String"
            },
            "height": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "maxHeight": {
                "type": "String"
            },
            "maxWidth": {
                "type": "String"
            },
            "namespacePrefix": {
                "type": "String"
            },
            "onCanvasAppError": {
                "type": "String"
            },
            "onCanvasAppLoad": {
                "type": "String"
            },
            "parameters": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "scrolling": {
                "type": "String"
            },
            "width": {
                "type": "String"
            }
        }
    },
    "apex:chart": {
        "simple": False,
        "attribs": {
            "animate": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "background": {
                "type": "String"
            },
            "colorSet": {
                "type": "String"
            },
            "data": {
                "type": "Object"
            },
            "floating": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "height": {
                "type": "String"
            },
            "hidden": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "id": {
                "type": "String"
            },
            "legend": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "name": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "renderTo": {
                "type": "String"
            },
            "resizable": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "theme": {
                "type": "String"
            },
            "width": {
                "type": "String"
            }
        }
    },
    "apex:chartLabel": {
        "simple": True,
        "attribs": {
            "color": {
                "type": "String"
            },
            "display": {
                "type": "Picklist",
                "values": [
                    "insideEnd",
                    "insideStart",
                    "middle",
                    "none",
                    "outside",
                    "over",
                    "rotate",
                    "under"
                ]
            },
            "field": {
                "type": "String"
            },
            "font": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "minMargin": {
                "type": "Integer"
            },
            "orientation": {
                "type": "Picklist",
                "values": [
                    "horizontal",
                    "vertical"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rendererFn": {
                "type": "String"
            },
            "rotate": {
                "type": "Integer"
            }
        }
    },
    "apex:chartTips": {
        "simple": True,
        "attribs": {
            "height": {
                "type": "Integer"
            },
            "id": {
                "type": "String"
            },
            "labelField": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rendererFn": {
                "type": "String"
            },
            "trackMouse": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "valueField": {
                "type": "String"
            },
            "width": {
                "type": "Integer"
            }
        }
    },
    "apex:column": {
        "simple": True,
        "attribs": {
            "breakBefore": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "colspan": {
                "type": "Integer"
            },
            "dirs": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "footerClass": {
                "type": "String"
            },
            "footerValue": {
                "type": "String"
            },
            "headerClass": {
                "type": "String"
            },
            "headerValue": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rowspan": {
                "type": "Integer"
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "title": {
                "type": "String"
            },
            "value": {
                "type": "Object"
            },
            "width": {
                "type": "String"
            }
        }
    },
    "apex:component": {
        "simple": True,
        "attribs": {
            "access": {
                "type": "Picklist",
                "values": [
                    "public",
                    "global"
                ]
            },
            "allowDML": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "controller": {
                "type": "String"
            },
            "extensions": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "language": {
                "type": "String"
            },
            "layout": {
                "type": "Picklist",
                "values": [
                    "block",
                    "inline",
                    "none"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "selfClosing": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "apex:componentBody": {
        "simple": True,
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "apex:commandButton": {
        "simple": True,
        "attribs": {
            "accesskey": {
                "type": "String"
            },
            "action": {
                "type": "ApexPages.Action"
            },
            "alt": {
                "type": "String"
            },
            "dirs": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "disabled": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "id": {
                "type": "String"
            },
            "image": {
                "type": "String"
            },
            "immediate": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "lang": {
                "type": "String"
            },
            "onblur": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "oncomplete": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onfocus": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "reRender": {
                "type": "String"
            },
            "status": {
                "type": "String"
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "tabindex": {
                "type": "String"
            },
            "timeout": {
                "type": "Integer"
            },
            "title": {
                "type": "String"
            },
            "value": {
                "type": "String"
            }
        }
    },
    "apex:commandLink": {
        "simple": True,
        "attribs": {
            "accesskey": {
                "type": "String"
            },
            "action": {
                "type": "ApexPages.Action"
            },
            "charset": {
                "type": "String"
            },
            "coords": {
                "type": "String"
            },
            "dirs": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "hreflang": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "immediate": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "lang": {
                "type": "String"
            },
            "onblur": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "oncomplete": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onfocus": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "rel": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "reRender": {
                "type": "String"
            },
            "rev": {
                "type": "String"
            },
            "shape": {
                "type": "Picklist",
                "values": [
                    "default", 
                    "circle", 
                    "rect", 
                    "poly"
                ]
            },
            "status": {
                "type": "String"
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "tabindex": {
                "type": "String"
            },
            "target": {
                "type": "Picklist",
                "values": [
                    "_blank",
                    "_parent",
                    "_self",
                    "_top"
                ]
            },
            "timeout": {
                "type": "Integer"
            },
            "title": {
                "type": "String"
            },
            "type": {
                "type": "String"
            },
            "value": {
                "type": "String"
            }
        }
    },
    "apex:composition": {
        "simple": False,
        "attribs": {
            "rendered": {
                "type": "String"
            },
            "template": {
                "type": "ApexPages.PageReference"
            }
        }
    },
    "apex:dataList": {
        "simple": False,
        "attribs": {
            "dirs": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "first": {
                "type": "Integer"
            },
            "id": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rows": {
                "type": "Integer"
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "title": {
                "type": "String"
            },
            "type": {
                "type": "String"
            },
            "value": {
                "type": "Object"
            },
            "var": {
                "type": "String"
            }
        }
    },
    "apex:dataTable": {
        "simple": False,
        "attribs": {
            "align": {
                "type": "Picklist",
                "values": [
                    "left", 
                    "center", 
                    "right"
                ]
            },
            "bgcolor": {
                "type": "String"
            },
            "border": {
                "type": "String"
            },
            "captionClass": {
                "type": "String"
            },
            "captionStyle": {
                "type": "String"
            },
            "cellpadding": {
                "type": "String"
            },
            "cellspacing": {
                "type": "String"
            },
            "columnClasses": {
                "type": "String"
            },
            "columns": {
                "type": "Integer"
            },
            "columnsWidth": {
                "type": "String"
            },
            "dirs": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "first": {
                "type": "Integer"
            },
            "footerClass": {
                "type": "String"
            },
            "frame": {
                "type": "Picklist",
                "values": [
                    "none", 
                    "above", 
                    "below", 
                    "hsides", 
                    "vsides", 
                    "lhs", 
                    "rhs", 
                    "box", 
                    "border"
                ]
            },
            "headerClass": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "onRowClick": {
                "type": "String"
            },
            "onRowDblClick": {
                "type": "String"
            },
            "onRowMouseDown": {
                "type": "String"
            },
            "onRowMouseMove": {
                "type": "String"
            },
            "onRowMouseOut": {
                "type": "String"
            },
            "onRowMouseOver": {
                "type": "String"
            },
            "onRowMouseUp": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rowClasses": {
                "type": "String"
            },
            "rows": {
                "type": "Integer"
            },
            "rules": {
                "type": "String",
                "values": [
                    "none", 
                    "groups", 
                    "rows", 
                    "cols", 
                    "all"
                ]
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "summary": {
                "type": "String"
            },
            "title": {
                "type": "String"
            },
            "value": {
                "type": "Object"
            },
            "var": {
                "type": "String"
            },
            "width": {
                "type": "String"
            }
        }
    },
    "apex:define": {
        "simple": False,
        "attribs": {
            "name": {
                "type": "String"
            }
        }
    },
    "apex:detail": {
        "simple": True,
        "attribs": {
            "id": {
                "type": "String"
            },
            "inlineEdit": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "oncomplete": {
                "type": "String"
            },
            "relatedList": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "relatedListHover": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rerender": {
                "type": "String"
            },
            "showChatter": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "subject": {
                "type": "String"
            },
            "title": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "apex:dynamicComponent": {
        "simple": True,
        "attribs": {
            "componentValue": {
                "type": "UIComponent"
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "apex:enhancedList": {
        "simple": True,
        "attribs": {
            "customizable": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "height": {
                "type": "Integer"
            },
            "id": {
                "type": "String"
            },
            "listId": {
                "type": "String"
            },
            "oncomplete": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "reRender": {
                "type": "String"
            },
            "rowsPerPage": {
                "type": "Picklist",
                "values": [
                    "10",
                    "25",
                    "50",
                    "100",
                    "200"
                ]
            },
            "type": {
                "type": "SObject"
            },
            "width": {
                "type": "Integer"
            }
        }
    },
    "apex:facet": {
        "simple": False,
        "attribs": {
            "name": {
                "type": "String"
            }
        }
    },
    "apex:flash": {
        "simple": False,
        "attribs": {
            "flashvars": {
                "type": "String"
            },
            "height": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "loop": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "play": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "src": {
                "type": "String"
            },
            "width": {
                "type": "String"
            }
        }
    },
    "apex:form": {
        "simple": False,
        "attribs": {
            "accept": {
                "type": "String"
            },
            "acceptcharset": {
                "type": "String"
            },
            "dir": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "enctype": {
                "type": "Picklist",
                "values": [
                    "application/x-www-form-urlencoded",
                    "application/xml",
                    "application/json"
                ]
            },
            "forceSSL": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "id": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "onreset": {
                "type": "String"
            },
            "onsubmit": {
                "type": "String"
            },
            "prependId": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "target": {
                "type": "Picklist",
                "values": [
                    "_blank",
                    "_parent",
                    "_self",
                    "_top"
                ]
            },
            "title": {
                "type": "String"
            }
        }
    },
    "apex:gaugeSeries": {
        "simple": False,
        "attribs": {
            "colorSet": {
                "type": "String"
            },
            "dataField": {
                "type": "String"
            },
            "donut": {
                "type": "Integer"
            },
            "highlight": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "id": {
                "type": "String"
            },
            "labelField": {
                "type": "String"
            },
            "needle": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rendererFn": {
                "type": "String"
            },
            "tips": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "apex:iframe": {
        "simple": True,
        "attribs": {
            "frameborder": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "height": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "scrolling": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "src": {
                "type": "String"
            },
            "title": {
                "type": "String"
            },
            "width": {
                "type": "String"
            }
        }
    },
    "apex:image": {
        "simple": True,
        "attribs": {
            "alt": {
                "type": "String"
            },
            "dir": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "height": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "ismap": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "lang": {
                "type": "String"
            },
            "longdesc": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "title": {
                "type": "String"
            },
            "url": {
                "type": "String"
            },
            "usemap": {
                "type": "String"
            },
            "value": {
                "type": "Object"
            },
            "width": {
                "type": "String"
            }
        }
    },
    "apex:include": {
        "simple": True,
        "attribs": {
            "id": {
                "type": "String"
            },
            "pageName": {
                "type": "ApexPages.PageReference"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "apex:includeScript": {
        "simple": True,
        "attribs": {
            "id": {
                "type": "String"
            },
            "value": {
                "type": "Object",
                "values": [
                    "{!URLFOR(\$Resource.$1, '$2')}",
                    "{!\$Resource.$1}"
                ]
            }
        }
    },
    "apex:inlineEditSupport": {
        "simple": True,
        "attribs": {
            "changedStyleClass": {
                "type": "String"
            },
            "disabled": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "event": {
                "type": "String"
            },
            "hideOnEdit": {
                "type": "Object"
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "resetFunction": {
                "type": "String"
            },
            "showOnEdit": {
                "type": "Object"
            }
        }
    },
    "apex:input": {
        "attribs": {
            "accesskey": {
                "type": "String"
            },
            "alt": {
                "type": "String"
            },
            "dir": {
                "type": "String"
            },
            "disabled": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "id": {
                "type": "String"
            },
            "label": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "list": {
                "type": "Object"
            },
            "onblur": {
                "type": "String"
            },
            "onchange": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onfocus": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "required": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "size": {
                "type": "Integer"
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "tabindex": {
                "type": "String"
            },
            "title": {
                "type": "String"
            },
            "type": {
                "type": "Picklist",
                "values": [
                    "auto",
                    "date",
                    "datetime",
                    "datetime-local",
                    "month",
                    "week",
                    "time",
                    "email",
                    "number",
                    "range",
                    "search",
                    "tel",
                    "text"
                ]
            },
            "value": {
                "type": "Object"
            }
        }
    },
    "apex:inputCheckbox": {
        "simple": True,
        "attribs": {
            "accesskey": {
                "type": "String"
            },
            "dir": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "disabled": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "id": {
                "type": "String"
            },
            "immediate": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "label": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "onblur": {
                "type": "String"
            },
            "onchange": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onfocus": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "onselect": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "required": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "selected": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "tabindex": {
                "type": "String"
            },
            "title": {
                "type": "String"
            },
            "value": {
                "type": "Object"
            }
        }
    },
    "apex:inputField": {
        "simple": True,
        "attribs": {
            "id": {
                "type": "String"
            },
            "label": {
                "type": "String"
            },
            "onblur": {
                "type": "String"
            },
            "onchange": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onfocus": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "onselect": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "required": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "list": {
                "type": "Object"
            },
            "showDatePicker": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "type": {
                "type": "Picklist",
                "values": [
                    "auto",
                    "date",
                    "datetime",
                    "datetime-local",
                    "month",
                    "week",
                    "time",
                    "email",
                    "number",
                    "range",
                    "search",
                    "tel",
                    "text"
                ]
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "taborderhint": {
                "type": "Integer"
            },
            "value": {
                "type": "Object"
            }
        }
    },
    "apex:inputFile": {
        "simple": False,
        "attribs": {
            "accept": {
                "type": "String"
            },
            "accessKey": {
                "type": "String"
            },
            "alt": {
                "type": "String"
            },
            "contentType": {
                "type": "String"
            },
            "dir": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "disabled": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "fileName": {
                "type": "String"
            },
            "fileSize": {
                "type": "Integer"
            },
            "id": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "onblur": {
                "type": "String"
            },
            "onchange": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onfocus": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "required": {
                "type": "java:\/\/java.lang.Boolean"
            },
            "size": {
                "type": "Integer"
            },
            "style": {
                "type": "String"
            },
            "styleclass": {
                "type": "String"
            },
            "tabindex": {
                "type": "Integer"
            },
            "title": {
                "type": "String"
            },
            "value": {
                "type": "Blob"
            }
        }
    },
    "apex:inputHidden": {
        "simple": True,
        "attribs": {
            "id": {
                "type": "String"
            },
            "immediate": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "required": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "value": {
                "type": "Object"
            }
        }
    },
    "apex:inputSecret": {
        "simple": True,
        "attribs": {
            "accesskey": {
                "type": "String"
            },
            "alt": {
                "type": "String"
            },
            "dir": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "disabled": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "id": {
                "type": "String"
            },
            "immediate": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "label": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "maxlength": {
                "type": "Integer"
            },
            "onblur": {
                "type": "String"
            },
            "onchange": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onfocus": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "onselect": {
                "type": "String"
            },
            "readonly": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "redisplay": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "required": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "size": {
                "type": "Integer"
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "tabindex": {
                "type": "String"
            },
            "title": {
                "type": "String"
            },
            "value": {
                "type": "Object"
            }
        }
    },
    "apex:inputText": {
        "simple": True,
        "attribs": {
            "accesskey": {
                "type": "String"
            },
            "alt": {
                "type": "String"
            },
            "dirs": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "disabled": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "id": {
                "type": "String"
            },
            "label": {
                "type": "String"
            },
            "list": {
                "type": "Object"
            },
            "lang": {
                "type": "String"
            },
            "maxlength": {
                "type": "Integer"
            },
            "onblur": {
                "type": "String"
            },
            "onchange": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onfocus": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "required": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "size": {
                "type": "Integer"
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "tabindex": {
                "type": "String"
            },
            "title": {
                "type": "String"
            },
            "value": {
                "type": "Object"
            }
        }
    },
    "apex:inputTextarea": {
        "simple": True,
        "attribs": {
            "accesskey": {
                "type": "String"
            },
            "cols": {
                "type": "Integer"
            },
            "dir": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "disabled": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "id": {
                "type": "String"
            },
            "label": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "onblur": {
                "type": "String"
            },
            "onchange": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onfocus": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "onselect": {
                "type": "String"
            },
            "readonly": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "required": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "richText": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rows": {
                "type": "Integer"
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "tabindex": {
                "type": "String"
            },
            "title": {
                "type": "String"
            },
            "value": {
                "type": "Object"
            }
        }
    },
    "apex:insert": {
        "simple": False,
        "attribs": {
            "name": {
                "type": "String"
            }
        }
    },
    "apex:legend": {
        "simple": False,
        "attribs": {
            "font": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "padding": {
                "type": "Integer"
            },
            "position": {
                "type": "Picklist",
                "values": [
                    "bottom",
                    "left",
                    "right",
                    "top"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "spacing": {
                "type": "Integer"
            }
        }
    },
    "apex:lineSeries": {
        "simple": False,
        "attribs": {
            "axis": {
                "type": "Picklist",
                "values": [
                    "bottom",
                    "left",
                    "right",
                    "top"
                ]
            },
            "fill": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "fillColor": {
                "type": "String"
            },
            "highlight": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "highlightStrokeWidth": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "markerFill": {
                "type": "String"
            },
            "markerSize": {
                "type": "Integer"
            },
            "markerType": {
                "type": "Picklist",
                "values": [
                    "circle",
                    "cross"
                ]
            },
            "opacity": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rendererFn": {
                "type": "String"
            },
            "showInLegend": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "smooth": {
                "type": "Integer"
            },
            "strokeColor": {
                "type": "String"
            },
            "strokeWidth": {
                "type": "String"
            },
            "tips": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "title": {
                "type": "String"
            },
            "xField": {
                "type": "String"
            },
            "yField": {
                "type": "String"
            }
        }
    },
    "apex:listViews": {
        "simple": True,
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "type": {
                "type": "String"
            }
        }
    },
    "apex:logCallPublisher": {
        "attribs": {
            "autoCollapseBody": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "entityId": {
                "type": "id"
            },
            "id": {
                "type": "String"
            },
            "logCallBody": {
                "type": "String"
            },
            "logCallBodyHeight": {
                "type": "String"
            },
            "onSubmitFailure": {
                "type": "String"
            },
            "onSubmitSuccess": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "reRender": {
                "type": "Object"
            },
            "showAdditionalFields": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "showSubmitButton": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "submitButtonName": {
                "type": "String"
            },
            "submitFunctionName": {
                "type": "String"
            },
            "title": {
                "type": "String"
            },
            "width": {
                "type": "String"
            }
        }
    },
    "apex:map": {
        "attribs": {
            "center": {
                "type": "Object",
                "values": [
                    "${1:1 Market Street, San Francisco, CA}",
                    "${1:{latitude: 37.794, longitude: -122.395\}}",
                    "${1:Map<String, Double>}"
                ]
            },
            "height": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "mapType": {
                "type": "Picklist",
                "values": [
                    "hybrid",
                    "roadmap",
                    "satellite"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "showOnlyActiveInfoWindow": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "width": {
                "type": "String"
            },
            "zoomLevel": {
                "type": "Integer"
            }
        }
    },
    "apex:mapInfoWindow": {
        "attribs": {
            "id": {
                "type": "String"
            },
            "maxWidth": {
                "type": "Integer"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "apex:mapMarker": {
        "attribs": {
            "icon": {
                "type": "String",
                "values": [
                    "{!URLFOR($Resource.$1, '$2')}"
                ]
            },
            "id": {
                "type": "String"
            },
            "position": {
                "type": "Object",
                "values": [
                    "${1:1 Market Street, San Francisco, CA}",
                    "${1:{latitude: 37.794, longitude: -122.395\}}",
                    "${1:Map<String, Double>}"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "title": {
                "type": "String"
            }
        }
    },
    "apex:message": {
        "simple": True,
        "attribs": {
            "dir": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "for": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "title": {
                "type": "String"
            }
        }
    },
    "apex:messages": {
        "simple": True,
        "attribs": {
            "dir": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "globalOnly": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "id": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "layout": {
                "type": "Picklist",
                "values": [
                    "lineDirection",
                    "pageDirection"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "title": {
                "type": "String"
            }
        }
    },
    "apex:milestoneTracker": {
        "entityId": {
            "type": "String"
        },
        "id": {
            "type": "String"
        },
        "rendered": {
            "type": "Boolean",
            "values": [
                "true",
                "false"
            ]
        }
    },
    "apex:outputField": {
        "simple": True,
        "attribs": {
            "dir": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "id": {
                "type": "String"
            },
            "label": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "title": {
                "type": "String"
            },
            "value": {
                "type": "Object"
            }
        }
    },
    "apex:outputLabel": {
        "simple": False,
        "attribs": {
            "accesskey": {
                "type": "String"
            },
            "dir": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "escape": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "for": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "onblur": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onfocus": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "tabindex": {
                "type": "String"
            },
            "title": {
                "type": "String"
            },
            "value": {
                "type": "Object"
            }
        }
    },
    "apex:outputLink": {
        "simple": False,
        "attribs": {
            "accesskey": {
                "type": "String"
            },
            "charset": {
                "type": "String"
            },
            "coords": {
                "type": "String"
            },
            "dir": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "disabled": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "hreflang": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "onblur": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onfocus": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "rel": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rev": {
                "type": "String"
            },
            "shape": {
                "type": "String"
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "tabindex": {
                "type": "String"
            },
            "target": {
                "type": "Picklist",
                "values": [
                    "_blank",
                    "_parent",
                    "_self",
                    "_top"
                ]
            },
            "title": {
                "type": "String"
            },
            "type": {
                "type": "String"
            },
            "value": {
                "type": "Object"
            }
        }
    },
    "apex:outputPanel": {
        "simple": False,
        "attribs": {
            "dir": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "id": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "layout": {
                "type": "Picklist",
                "values": [
                    "lineDirection",
                    "pageDirection"
                ]
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "title": {
                "type": "String"
            }
        }
    },
    "apex:outputText": {
        "simple": False,
        "attribs": {
            "dir": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "escape": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "id": {
                "type": "String"
            },
            "label": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "title": {
                "type": "String"
            },
            "value": {
                "type": "Object"
            }
        }
    },
    "apex:page": {
        "simple": False,
        "attribs": {
            "action": {
                "type": "ApexPages.Action"
            },
            "apiVersion": {
                "type": "Picklist",
                "values": [
                    "28.0",
                    "29.0",
                    "30.0",
                    "31.0",
                    "32.0",
                    "33.0",
                    "34.0",
                    "100.0, really up to 100?"
                ]
            },
            "applyBodyTag": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "applyHtmlTag": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "cache": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "contentType": {
                "type": "Picklist",
                "values": [
                    "application/pdf#${1:fileName}",
                    "application/xml#${1:fileName}",
                    "application/vnd.ms-excel#${1:fileName}",
                    "application/json#${1:fileName}"
                ]
            },
            "controller": {
                "type": "String"
            },
            "deferLastCommandUntilReady": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "docType": {
                "type": "String"
            },
            "expires": {
                "type": "Integer"
            },
            "extensions": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "label": {
                "type": "String"
            },
            "language": {
                "type": "String"
            },
            "manifest": {
                "type": "String"
            },
            "name": {
                "type": "String"
            },
            "pageStyle": {
                "type": "String"
            },
            "readOnly": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "recordSetVar": {
                "type": "String"
            },
            "renderAs": {
                "type": "Picklist",
                "values": [
                    "pdf"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "setup": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "showChat": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "showHeader": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "sidebar": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "standardController": {
                "type": "String"
            },
            "standardStylesheets": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "tabStyle": {
                "type": "String"
            },
            "title": {
                "type": "String"
            },
            "wizard": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "apex:pageBlock": {
        "simple": False,
        "attribs": {
            "dir": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "helpTitle": {
                "type": "String"
            },
            "helpUrl": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "mode": {
                "type": "Picklist",
                "values": [
                    "detail",
                    "maindetail",
                    "edit",
                    "inlineEdit"
                ]
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "tabStyle": {
                "type": "String"
            },
            "title": {
                "type": "String"
            }
        }
    },
    "apex:pageBlockButtons": {
        "simple": False,
        "attribs": {
            "dir": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "id": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "location": {
                "type": "Picklist",
                "values": [
                    "both",
                    "bottom",
                    "top"
                ]
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "title": {
                "type": "String"
            }
        }
    },
    "apex:pageBlockSection": {
        "simple": False,
        "attribs": {
            "collapsible": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "columns": {
                "type": "Integer"
            },
            "dir": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "id": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "showHeader": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "title": {
                "type": "String"
            }
        }
    },
    "apex:pageBlockSectionItem": {
        "simple": False,
        "attribs": {
            "dataStyle": {
                "type": "String"
            },
            "dataStyleClass": {
                "type": "String"
            },
            "dataTitle": {
                "type": "String"
            },
            "dir": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "helpText": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "labelStyle": {
                "type": "String"
            },
            "labelStyleClass": {
                "type": "String"
            },
            "labelTitle": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "onDataclick": {
                "type": "String"
            },
            "onDatadblclick": {
                "type": "String"
            },
            "onDatakeydown": {
                "type": "String"
            },
            "onDatakeypress": {
                "type": "String"
            },
            "onDatakeyup": {
                "type": "String"
            },
            "onDatamousedown": {
                "type": "String"
            },
            "onDatamousemove": {
                "type": "String"
            },
            "onDatamouseout": {
                "type": "String"
            },
            "onDatamouseover": {
                "type": "String"
            },
            "onDatamouseup": {
                "type": "String"
            },
            "onLabelclick": {
                "type": "String"
            },
            "onLabeldblclick": {
                "type": "String"
            },
            "onLabelkeydown": {
                "type": "String"
            },
            "onLabelkeypress": {
                "type": "String"
            },
            "onLabelkeyup": {
                "type": "String"
            },
            "onLabelmousedown": {
                "type": "String"
            },
            "onLabelmousemove": {
                "type": "String"
            },
            "onLabelmouseout": {
                "type": "String"
            },
            "onLabelmouseover": {
                "type": "String"
            },
            "onLabelmouseup": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "apex:pageBlockTable": {
        "simple": False,
        "attribs": {
            "align": {
                "type": "Picklist",
                "values": [
                    "left",
                    "center",
                    "right"
                ]
            },
            "border": {
                "type": "String"
            },
            "captionClass": {
                "type": "String"
            },
            "captionStyle": {
                "type": "String"
            },
            "cellpadding": {
                "type": "String"
            },
            "cellspacing": {
                "type": "String"
            },
            "columnClasses": {
                "type": "String"
            },
            "columns": {
                "type": "Integer"
            },
            "columnsWidth": {
                "type": "String"
            },
            "dir": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "first": {
                "type": "Integer"
            },
            "footerClass": {
                "type": "String"
            },
            "frame": {
                "type": "Picklist",
                "values": [
                    "none", 
                    "above", 
                    "below", 
                    "hsides", 
                    "vsides", 
                    "lhs", 
                    "rhs", 
                    "box", 
                    "border"
                ]
            },
            "headerClass": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "onRowClick": {
                "type": "String"
            },
            "onRowDblClick": {
                "type": "String"
            },
            "onRowMouseDown": {
                "type": "String"
            },
            "onRowMouseMove": {
                "type": "String"
            },
            "onRowMouseOut": {
                "type": "String"
            },
            "onRowMouseOver": {
                "type": "String"
            },
            "onRowMouseUp": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rowClasses": {
                "type": "String"
            },
            "rows": {
                "type": "Integer"
            },
            "rules": {
                "type": "String"
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "summary": {
                "type": "String"
            },
            "title": {
                "type": "String"
            },
            "value": {
                "type": "Object"
            },
            "var": {
                "type": "String"
            },
            "width": {
                "type": "String"
            }
        }
    },
    "apex:pageMessage": {
        "simple": False,
        "attribs": {
            "detail": {
                "type": "String"
            },
            "escape": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "severity": {
                "type": "String",
                "values": [
                    "CONFIRM", 
                    "INFO", 
                    "WARNING", 
                    "ERROR"
                ]
            },
            "strength": {
                "type": "Picklist",
                "values": [
                    "0", 
                    "1", 
                    "2", 
                    "3"
                ]
            },
            "summary": {
                "type": "String"
            },
            "title": {
                "type": "String"
            }
        }
    },
    "apex:pageMessages": {
        "simple": False,
        "attribs": {
            "escape": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "showDetail": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "apex:panelBar": {
        "simple": False,
        "attribs": {
            "contentClass": {
                "type": "String"
            },
            "contentStyle": {
                "type": "String"
            },
            "headerClass": {
                "type": "String"
            },
            "headerClassActive": {
                "type": "String"
            },
            "headerStyle": {
                "type": "String"
            },
            "headerStyleActive": {
                "type": "String"
            },
            "height": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "items": {
                "type": "Object"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "switchType": {
                "type": "Picklist",
                "values": [
                    "client",
                    "server",
                    "ajax"
                ]
            },
            "value": {
                "type": "Object"
            },
            "var": {
                "type": "String"
            },
            "width": {
                "type": "String"
            }
        }
    },
    "apex:panelBarItem": {
        "simple": False,
        "attribs": {
            "contentClass": {
                "type": "String"
            },
            "contentStyle": {
                "type": "String"
            },
            "expanded": {
                "type": "String"
            },
            "headerClass": {
                "type": "String"
            },
            "headerClassActive": {
                "type": "String"
            },
            "headerStyle": {
                "type": "String"
            },
            "headerStyleActive": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "label": {
                "type": "String"
            },
            "name": {
                "type": "Object"
            },
            "onenter": {
                "type": "String"
            },
            "onleave": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "apex:panelGrid": {
        "simple": False,
        "attribs": {
            "bgcolor": {
                "type": "String"
            },
            "border": {
                "type": "Integer"
            },
            "captionClass": {
                "type": "String"
            },
            "captionStyle": {
                "type": "String"
            },
            "cellpadding": {
                "type": "String"
            },
            "cellspacing": {
                "type": "String"
            },
            "columnClasses": {
                "type": "String"
            },
            "columns": {
                "type": "Integer"
            },
            "dir": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "footerClass": {
                "type": "String"
            },
            "frame": {
                "type": "Picklist",
                "values": [
                    "none", 
                    "above", 
                    "below", 
                    "hsides", 
                    "vsides", 
                    "lhs", 
                    "rhs", 
                    "box", 
                    "border"
                ]
            },
            "headerClass": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rowClasses": {
                "type": "String"
            },
            "rules": {
                "type": "String"
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "summary": {
                "type": "String"
            },
            "title": {
                "type": "String"
            },
            "width": {
                "type": "String"
            }
        }
    },
    "apex:panelGroup": {
        "simple": False,
        "attribs": {
            "id": {
                "type": "String"
            },
            "layout": {
                "type": "Picklist",
                "values": [
                    "lineDirection",
                    "pageDirection"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            }
        }
    },
    "apex:param": {
        "simple": True,
        "attribs": {
            "assignTo": {
                "type": "Object"
            },
            "id": {
                "type": "String"
            },
            "name": {
                "type": "String"
            },
            "value": {
                "type": "Object"
            }
        }
    },
    "apex:pieSeries": {
        "simple": False,
        "attribs": {
            "colorSet": {
                "type": "String"
            },
            "dataField": {
                "type": "String"
            },
            "donut": {
                "type": "Integer"
            },
            "highlight": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "id": {
                "type": "String"
            },
            "labelField": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rendererFn": {
                "type": "String"
            },
            "showInLegend": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "tips": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "apex:radarSeries": {
        "simple": False,
        "attribs": {
            "fill": {
                "type": "String"
            },
            "highlight": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "id": {
                "type": "String"
            },
            "markerFill": {
                "type": "String"
            },
            "markerSize": {
                "type": "Integer"
            },
            "markerType": {
                "type": "Picklist",
                "values": [
                    "circle",
                    "cross"
                ]
            },
            "opacity": {
                "type": "Integer"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "showInLegend": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "strokeColor": {
                "type": "String"
            },
            "strokeWidth": {
                "type": "Integer"
            },
            "tips": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "title": {
                "type": "String"
            },
            "xField": {
                "type": "String"
            },
            "yField": {
                "type": "String"
            }
        }
    },
    "apex:relatedList": {
        "simple": True,
        "attribs": {
            "id": {
                "type": "String"
            },
            "list": {
                "type": "Object"
            },
            "pageSize": {
                "type": "Integer"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "subject": {
                "type": "String"
            },
            "title": {
                "type": "String"
            }
        }
    },
    "apex:remoteObjectField": {
        "simple": False,
        "attribs": {
            "id": {
                "type": "String"
            },
            "jsShorthand": {
                "type": "String"
            },
            "name": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "apex:remoteObjectModel": {
        "attribs": {
            "create": {
                "type": "String"
            },
            "delete": {
                "type": "String"
            },
            "fields": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "jsShorthand": {
                "type": "String"
            },
            "name": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "retrieve": {
                "type": "String"
            },
            "update": {
                "type": "String"
            }
        }
    },
    "apex:remoteObjects": {
        "attribs": {
            "create": {
                "type": "String"
            },
            "delete": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "jsNamespace": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "retrieve": {
                "type": "String"
            },
            "update": {
                "type": "String"
            }
        }
    },
    "apex:repeat": {
        "simple": False,
        "attribs": {
            "first": {
                "type": "Integer"
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rows": {
                "type": "Integer"
            },
            "value": {
                "type": "Object"
            },
            "var": {
                "type": "String"
            }
        }
    },
    "apex:scatterSeries": {
        "simple": False,
        "attribs": {
            "axis": {
                "type": "Picklist",
                "values": [
                    "bottom",
                    "left",
                    "right",
                    "top"
                ]
            },
            "highlight": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "id": {
                "type": "String"
            },
            "markerFill": {
                "type": "String"
            },
            "markerSize": {
                "type": "Integer"
            },
            "markerType": {
                "type": "Picklist",
                "values": [
                    "circle",
                    "cross"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rendererFn": {
                "type": "String"
            },
            "showInLegend": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "tips": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "title": {
                "type": "String"
            },
            "xField": {
                "type": "String"
            },
            "yField": {
                "type": "String"
            }
        }
    },
    "apex:scontrol": {
        "simple": True,
        "attribs": {
            "controlName": {
                "type": "String"
            },
            "height": {
                "type": "Integer"
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "scrollbars": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "subject": {
                "type": "Object"
            },
            "width": {
                "type": "Integer"
            }
        }
    },
    "apex:sectionHeader": {
        "simple": True,
        "attribs": {
            "description": {
                "type": "String"
            },
            "help": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "printUrl": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "subtitle": {
                "type": "String"
            },
            "title": {
                "type": "String"
            }
        }
    },
    "apex:selectCheckboxes": {
        "simple": False,
        "attribs": {
            "accesskey": {
                "type": "String"
            },
            "border": {
                "type": "Integer"
            },
            "borderVisible": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "dirs": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "disabled": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "disabledClass": {
                "type": "String"
            },
            "enabledClass": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "immediate": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "label": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "layout": {
                "type": "Picklist",
                "values": [
                    "lineDirection",
                    "pageDirection"
                ]
            },
            "legendInvisible": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "legendText": {
                "type": "String"
            },
            "onblur": {
                "type": "String"
            },
            "onchange": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onfocus": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "onselect": {
                "type": "String"
            },
            "readonly": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "required": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "tabindex": {
                "type": "String"
            },
            "title": {
                "type": "String"
            },
            "value": {
                "type": "Object"
            }
        }
    },
    "apex:selectList": {
        "simple": False,
        "attribs": {
            "accesskey": {
                "type": "String"
            },
            "dirs": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "disabled": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "disabledClass": {
                "type": "String"
            },
            "enabledClass": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "label": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "multiselect": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "onblur": {
                "type": "String"
            },
            "onchange": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onfocus": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "onselect": {
                "type": "String"
            },
            "readonly": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "required": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "size": {
                "type": "Integer"
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "tabindex": {
                "type": "String"
            },
            "title": {
                "type": "String"
            },
            "value": {
                "type": "Object"
            }
        }
    },
    "apex:selectOption": {
        "simple": False,
        "attribs": {
            "dirs": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "id": {
                "type": "String"
            },
            "itemDescription": {
                "type": "String"
            },
            "itemDisabled": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "itemEscaped": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "itemLabel": {
                "type": "String"
            },
            "itemValue": {
                "type": "Object"
            },
            "lang": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "title": {
                "type": "String"
            },
            "value": {
                "type": "Object"
            }
        }
    },
    "apex:selectOptions": {
        "simple": False,
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "value": {
                "type": "Object"
            }
        }
    },
    "apex:selectRadio": {
        "simple": False,
        "attribs": {
            "accesskey": {
                "type": "String"
            },
            "border": {
                "type": "Integer"
            },
            "borderVisible": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "dirs": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "disabled": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "disabledClass": {
                "type": "String"
            },
            "enabledClass": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "immediate": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "label": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "layout": {
                "type": "Picklist",
                "values": [
                    "lineDirection",
                    "pageDirection"
                ]
            },
            "legendInvisible": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "legendText": {
                "type": "String"
            },
            "onblur": {
                "type": "String"
            },
            "onchange": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onfocus": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "onselect": {
                "type": "String"
            },
            "readonly": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "required": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "tabindex": {
                "type": "String"
            },
            "title": {
                "type": "String"
            },
            "value": {
                "type": "Object"
            }
        }
    },
    "apex:stylesheet": {
        "simple": True,
        "attribs": {
            "id": {
                "type": "String"
            },
            "value": {
                "type": "Object"
            }
        }
    },
    "apex:tab": {
        "simple": False,
        "attribs": {
            "disabled": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "focus": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "immediate": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "label": {
                "type": "String"
            },
            "labelWidth": {
                "type": "String"
            },
            "name": {
                "type": "Object"
            },
            "onclick": {
                "type": "String"
            },
            "oncomplete": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "ontabenter": {
                "type": "String"
            },
            "ontableave": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "reRender": {
                "type": "String"
            },
            "status": {
                "type": "String"
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "switchType": {
                "type": "Picklist",
                "values": [
                    "client",
                    "server",
                    "ajax"
                ]
            },
            "timeout": {
                "type": "Integer"
            },
            "title": {
                "type": "String"
            }
        }
    },
    "apex:tabPanel": {
        "simple": False,
        "attribs": {
            "activeTabClass": {
                "type": "String"
            },
            "contentClass": {
                "type": "String"
            },
            "contentStyle": {
                "type": "String"
            },
            "dirs": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "disabledTabClass": {
                "type": "String"
            },
            "headerAlignment": {
                "type": "String"
            },
            "headerClass": {
                "type": "String"
            },
            "headerSpacing": {
                "type": "String"
            },
            "height": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "immediate": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "inactiveTabClass": {
                "type": "String"
            },
            "lang": {
                "type": "String"
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "reRender": {
                "type": "String"
            },
            "selectedTab": {
                "type": "Object"
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "switchType": {
                "type": "Picklist",
                "values": [
                    "client",
                    "server",
                    "ajax"
                ]
            },
            "tabClass": {
                "type": "String"
            },
            "title": {
                "type": "String"
            },
            "value": {
                "type": "Object"
            },
            "width": {
                "type": "String"
            }
        }
    },
    "apex:toolbar": {
        "simple": False,
        "attribs": {
            "contentClass": {
                "type": "String"
            },
            "contentStyle": {
                "type": "String"
            },
            "height": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "itemSeparator": {
                "type": "String",
                "values": [
                    "none",
                    "line",
                    "square",
                    "disc",
                    "grid"
                ]
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onitemclick": {
                "type": "String"
            },
            "onitemdblclick": {
                "type": "String"
            },
            "onitemkeydown": {
                "type": "String"
            },
            "onitemkeypress": {
                "type": "String"
            },
            "onitemkeyup": {
                "type": "String"
            },
            "onitemmousedown": {
                "type": "String"
            },
            "onitemmousemove": {
                "type": "String"
            },
            "onitemmouseout": {
                "type": "String"
            },
            "onitemmouseover": {
                "type": "String"
            },
            "onitemmouseup": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "separatorClass": {
                "type": "String"
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "width": {
                "type": "String"
            }
        }
    },
    "apex:toolbarGroup": {
        "simple": False,
        "attribs": {
            "id": {
                "type": "String"
            },
            "itemSeparator": {
                "type": "String",
                "values": [
                    "none",
                    "line",
                    "square",
                    "disc",
                    "grid"
                ]
            },
            "location": {
                "type": "Picklist",
                "values": [
                    "left",
                    "right"
                ]
            },
            "onclick": {
                "type": "String"
            },
            "ondblclick": {
                "type": "String"
            },
            "onkeydown": {
                "type": "String"
            },
            "onkeypress": {
                "type": "String"
            },
            "onkeyup": {
                "type": "String"
            },
            "onmousedown": {
                "type": "String"
            },
            "onmousemove": {
                "type": "String"
            },
            "onmouseout": {
                "type": "String"
            },
            "onmouseover": {
                "type": "String"
            },
            "onmouseup": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "separatorClass": {
                "type": "String"
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            }
        }
    },
    "apex:variable": {
        "simple": True,
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "value": {
                "type": "Object"
            },
            "var": {
                "type": "String"
            }
        }
    },
    "apex:vote": {
        "simple": False,
        "attribs": {
            "id": {
                "type": "String"
            },
            "objectId": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "reRender": {
                "type": "String"
            }
        }
    },
    "c:sitefooter": {
        "simple": False,
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "c:siteheader": {
        "simple": False,
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "c:sitelogin": {
        "simple": False,
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "c:sitepoweredby": {
        "simple": False,
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "chatter:feed": {
        "simple": True,
        "attribs": {
            "entityId": {
                "type": "id"
            },
            "feedItemType": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "onComplete": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "reRender": {
                "type": "String"
            },
            "showPublisher": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "chatter:feedWithFollowers": {
        "simple": True,
        "attribs": {
            "entityId": {
                "type": "id"
            },
            "id": {
                "type": "String"
            },
            "onComplete": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "reRender": {
                "type": "String"
            },
            "showHeader": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "chatter:follow": {
        "simple": True,
        "attribs": {
            "entityId": {
                "type": "id"
            },
            "id": {
                "type": "String"
            },
            "onComplete": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "reRender": {
                "type": "String"
            }
        }
    },
    "chatter:followers": {
        "simple": True,
        "attribs": {
            "entityId": {
                "type": "id"
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "chatter:newsfeed": {
        "simple": True,
        "attribs": {
            "id": {
                "type": "String"
            },
            "onComplete": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "reRender": {
                "type": "String"
            }
        }
    },
    "chatter:userPhotoUpload": {
        "simple": False,
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "showOriginalPhoto": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "flow:interview": {
        "simple": False,
        "attribs": {
            "buttonLocation": {
                "type": "String",
                "values": [
                    "both",
                    "bottom",
                    "top"
                ]
            },
            "buttonStyle": {
                "type": "String"
            },
            "finishLocation": {
                "type": "ApexPages.PageReference"
            },
            "id": {
                "type": "String"
            },
            "interview": {
                "type": "Flow.Interview"
            },
            "name": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "rerender": {
                "type": "String"
            },
            "showHelp": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "ideas:detailOutputLink": {
        "simple": False,
        "attribs": {
            "id": {
                "type": "String"
            },
            "ideaId": {
                "type": "String"
            },
            "page": {
                "type": "ApexPages.PageReference"
            },
            "pageNumber": {
                "type": "Integer"
            },
            "pageOffset": {
                "type": "Integer"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            }
        }
    },
    "ideas:listOutputLink": {
        "simple": False,
        "attribs": {
            "category": {
                "type": "String"
            },
            "communityId": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "page": {
                "type": "ApexPages.PageReference"
            },
            "pageNumber": {
                "type": "Integer"
            },
            "pageOffset": {
                "type": "Integer"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "sort": {
                "type": "String"
            },
            "status": {
                "type": "String"
            },
            "stickyAttributes": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            }
        }
    },
    "ideas:profileListOutputLink": {
        "simple": False,
        "attribs": {
            "communityId": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "page": {
                "type": "ApexPages.PageReference"
            },
            "pageNumber": {
                "type": "Integer"
            },
            "pageOffset": {
                "type": "Integer"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "sort": {
                "type": "String"
            },
            "stickyAttributes": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            },
            "style": {
                "type": "String"
            },
            "styleClass": {
                "type": "String"
            },
            "userId": {
                "type": "String"
            }
        }
    },
    "site:googleAnalyticsTracking": {
        "simple": False,
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "site:previewAsAdmin": {
        "simple": False,
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "social:profileViewer": {
        "simple": False,
        "attribs": {
            "entityId": {
                "type": "id"
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    },
    "support:clickToDial": {
        "simple": False,
        "attribs": {
            "entityId": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "number": {
                "type": "String"
            },
            "params": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean",
                "values": [
                    "true", "false"
                ]
            }
        }
    }
}