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
        "type": "aura",
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
                "type": "Boolean"
            }
        }
    },

    "aura:attribute": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "access": {
                "type": "Picklist",
                "values":[
                    "public", "global", "PRIVATE"
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
                "type": "String"
            },
            "required": {
                "type": "Boolean"
            },
            "description": {
                "type": "String"
            }
        }
    },

    "aura:component": {
        "simple": False,
        "type": "aura",
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

    "aura:method": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "name": {
                "type": "String",
                "description": "The method name. Use the method name to call the method in JavaScript code"
            },
            "action": {
                "type": "Expression",
                "values":[
                    "{!c.$0}",
                    "{!}"
                ]
            },
            "access": {
                "type": "Picklist",
                "values":[
                    "public",
                    "global"
                ]
            },
            "description": {
                "type": "String"
            }
        }
    },

    "aura:dependency": {
        "simple": False,
        "type": "aura",
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
        "type": "aura",
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

    "aura:handler": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "event": {
                "type": "Picklist",
                "values": [
                    "${1:Customize}",
                    "aura:doneRendering",
                    "aura:doneWaiting",
                    "aura:locationChange",
                    "aura:systemError",
                    "aura:valueChange",
                    "aura:valueDestroy",
                    "aura:valueInit",
                    "aura:waiting"
                ]
            },

            "action": {
                "type": "Object"
            }
        }
    },

    "aura:if": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "else": {
                "type": "ComponentDefRef[]"
            },
            "isTrue": {
                "type": "Boolean"
            }
        }
    },

    "aura:html": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },
            "HTMLAttributes": {
                "type": "HashMap",
                "description": "A Map of attributes to set on the html element."
            },
            "tag": {
                "type": "String",
                "description": "The name of the html element that should be rendered."
            }
        }
    },

    "aura:expression": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "value": {
                "type": "String",
                "description": "The expression to evaluate and render."
            }
        }
    },

    "aura:interface": {
        "simple": False,
        "type": "aura",
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
        "type": "aura",
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
        "type": "aura",
        "attribs": {
            "else": {
                "type": "ComponentDefRef[]"
            },
            "isTrue": {
                "type": "Boolean"
            }
        }
    },

    "aura:set": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "attribute": {
                "type": "String"
            },
            "value": {
                "type": "String"
            }
        }
    },

    "aura:set": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "value": {
                "type": "String",
                "description": "The String to be rendered."
            }
        }
    },

    "aura:unescapedHtml": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of <aura:unescapedHtml> is ignored and won't be rendered."
            },
            "value": {
                "type": "String",
                "description": "The string that should be rendered as unescaped HTML."
            }
        }
    },

    "aura:template": {
        "simple": False,
        "type": "aura",
        "attribs": {
           "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },
            "bodyClass": {
                "type": "String",
                "description": "Extra body CSS styles"
            },
            "defaultBodyClass": {
                "type": "String",
                "description": "Default body CSS styles."
            },
            "doctype": {
                "type": "String",
                "description": "The DOCTYPE declaration for the template"
            },
            "errorMessage": {
                "type": "String",
                "description": "Error loading text"
            },
            "errorTitle": {
                "type": "String",
                "description": "Error title when an error has occured."
            },
            "loadingText": {
                "type": "String",
                "description": "Loading text"
            },
            "title": {
                "type": "String",
                "description": "The title of the template."
            }
        }
    },

    "force:canvasApp": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "displayLocation": {
                "description": "The location in the application where the canvas app is currently being called from.", 
                "type": "String"
            }, 
            "containerId": {
                "description": "An html element id in which canvas app is rendered. The container needs to be defined before canvasApp cmp usage.", 
                "type": "String"
            }, 
            "developerName": {
                "description": "Developer name of the canvas app. This name is defined when the canvas app is created and can be viewed in the Canvas App Previewer. Either developerName or applicationName is required.", 
                "type": "String"
            }, 
            "maxWidth": {
                "description": "The maximum width of the Canvas app window in pixels. Defaults to 1000 px; 'infinite' is also a valid value.", 
                "type": "String"
            }, 
            "maxHeight": {
                "description": "The maximum height of the Canvas app window in pixels. Defaults to 2000 px; 'infinite' is also a valid value.", 
                "type": "String"
            }, 
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.", 
                "type": "Component[]"
            }, 
            "onCanvasAppError": {
                "description": "Name of the JavaScript function to be called if the canvas app fails to render.", 
                "type": "String"
            }, 
            "width": {
                "description": "Canvas app window width, in pixels. If not specified, defaults to 800 px.", 
                "type": "String"
            }, 
            "watermark": {
                "description": "Renders a link if set to true", 
                "type": "Boolean"
            }, 
            "applicationName": {
                "description": "Name of the canvas app. Either applicationName or developerName is required.", 
                "type": "String"
            }, 
            "title": {
                "description": "Title for the link", 
                "type": "String"
            }, 
            "referenceId": {
                "description": "The reference id of the canvas app, if set this is used instead of developerName, applicationName and namespacePrefix", 
                "type": "String"
            }, 
            "namespacePrefix": {
                "description": "Namespace value of the Developer Edition organization in which the canvas app was created. Optional if the canvas app wasn¡¯t created in a Developer Edition organization. If not specified, defaults to null.", 
                "type": "String"
            }, 
            "border": {
                "description": "Width of the canvas app border, in pixels. If not specified, defaults to 0 px.", 
                "type": "String"
            }, 
            "onCanvasAppLoad": {
                "description": "Name of the JavaScript function to be called after the canvas app loads.", 
                "type": "String"
            }, 
            "scrolling": {
                "description": "Canvas window scrolling", 
                "type": "String"
            }, 
            "canvasId": {
                "description": "An unique label within a page for the Canvas app window. This should be used when targeting events to this canvas app.", 
                "type": "String"
            }, 
            "parameters": {
                "description": "Object representation of parameters passed to the canvas app. This should be supplied in JSON format or as a JavaScript object literal. Here¡¯s an example of parameters in a JavaScript object literal: {param1:'value1',param2:'value2'}. If not specified, defaults to null.", 
                "type": "String"
            }, 
            "sublocation": {
                "description": "The sublocation is the location in the application where the canvas app is currently being called from, for ex, displayLocation can be PageLayout and sublocation can be S1MobileCardPreview or S1MobileCardFullview, etc", 
                "type": "String"
            }, 
            "height": {
                "description": "Canvas app window height, in pixels. If not specified, defaults to 900 px.", 
                "type": "String"
            }, 
            "onCanvasSubscribed": {
                "description": "Name of the JavaScript function to be called after the canvas app registers with the parent.", 
                "type": "String"
            }
        }
    },

    "force:inputField": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },
            "class": {
                "type": "String",
                "description": "The CSS style used to display the field."
            },
            "errorComponent": {
                "type": "Component[]",
                "description": "A component which is responsible for displaying the error message."
            },
            "required": {
                "type": "Boolean",
                "description": "Specifies whether this field is required or not."
            },
            "value": {
                "type": "Object",
                "description": "Data value of Salesforce field to which to bind."
            }
        }
    },

    "force:outputField": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },
            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },   
            "value": {
                "type": "Object",
                "description": "Data value of Salesforce field to which to bind."
            }
        }
    },

    "force:recordEdit": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },
            "recordId": {
                "type": "String",
                "description": "The Id of the record to load, optional if record attribute is specified."
            },
            "recordSave": {
                "type": "COMPONENT",
                "description": "Record save request"
            },
            "recordSaveSuccess": {
                "type": "COMPONENT",
                "description": "Indicates that the record has been successfully saved."
            }
        }
    },

    "force:recordView": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },
            "recordId": {
                "type": "SObjectRow",
                "description": "The record (SObject) to load, optional if recordId attribute is specified."
            },
            "recordId": {
                "type": "String",
                "description": "The Id of the record to load, optional if record attribute is specified."
            },
            "type": {
                "type": "String",
                "description": "The type of layout to use to display the record. Possible values: FULL, MINI. The default is FULL."
            },
        }
    },

    "forceChatter:feed": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },
            "subjectId": {
                "type": "String",
                "description": "For most feeds tied to an entity, this is used specified the desired entity. Defaults to the current user if not specified"
            },
            "type": {
                "type": "String",
                "description": "The strategy used to find items associated with the subject. Valid values include: News, Home, Record, To."
            }
        }
    },

    "ltng:require": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },
            "scripts": {
                "type": "String[]",
                "description": "The set of scripts in dependency order that will be loaded."
            },
            "styles": {
                "type": "String[]",
                "description": "The set of style sheets in dependency order that will be loaded."
            },
            "afterScriptsLoaded": {
                "type": "COMPONENT",
                "description": "Fired when ltng:require has loaded all scripts listed in ltng:require.scripts"
            }
        }
    },

    "ui:actionMenuItem": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.", 
                "type": "COMPONENT"
            }, 
            "label": {
                "description": "The text displayed on the component.", 
                "type": "String"
            }, 
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.", 
                "type": "String"
            }, 
            "keydown": {
                "description": "Indicates that the user has pressed and released a keyboard key.", 
                "type": "COMPONENT"
            }, 
            "blur": {
                "description": "Indicates that a component has been put out of focus.", 
                "type": "COMPONENT"
            }, 
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.", 
                "type": "COMPONENT"
            }, 
            "selected": {
                "description": "The status of the menu item. True means this menu item is selected; False is not selected.", 
                "type": "Boolean"
            }, 
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.", 
                "type": "COMPONENT"
            }, 
            "keyup": {
                "description": "Indicates that the user has released a keyboard key.", 
                "type": "COMPONENT"
            }, 
            "type": {
                "description": "The concrete type of the menu item. Accepted values are 'action', 'checkbox', 'radio', 'separator' or any namespaced,component descriptor, e.g. ns:xxxxmenuItem.", 
                "type": "String"
            }, 
            "hideMenuAfterSelected": {
                "description": "Set to true to hide menu after the menu item is selected.", 
                "type": "Boolean"
            }, 
            "select": {
                "description": "Indicates that the user has made a selection.", 
                "type": "COMPONENT"
            }, 
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.", 
                "type": "Component[]"
            }, 
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.", 
                "type": "COMPONENT"
            }, 
            "focus": {
                "description": "Indicates that a component has been put on focus.", 
                "type": "COMPONENT"
            }, 
            "disabled": {
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is 'false'.", 
                "type": "Boolean"
            }, 
            "keypress": {
                "description": "Indicates that the user has pressed and held down a keyboard key.", 
                "type": "COMPONENT"
            }, 
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.", 
                "type": "COMPONENT"
            }, 
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.", 
                "type": "COMPONENT"
            }, 
            "click": {
                "description": "Indicates that a component has been clicked.", 
                "type": "COMPONENT"
            }
        }
    },

    "ui:button": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "label": {
                "type": "String", 
                "description": "The text displayed on the button. Corresponds to the value attribute of the rendered HTML input element."
            }, 
            "buttonType": {
                "type": "String", 
                "description": "Specifies the type attribute in the HTML input element. Default value is button."
            }, 
            "disabled": {
                "type": "Boolean", 
                "description": "Specifies whether this button should be displayed in a disabled state. Disabled buttons can't be clicked. Default value is 'false'."
            }, 
            "body": {
                "type": "Component[]", 
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            }, 
            "labelClass": {
                "type": "String", 
                "description": "A CSS style to be attached to the label. This style is added in addition to base styles output by the component."
            }, 
            "class": {
                "type": "String", 
                "description": "A CSS style to be attached to the button. This style is added in addition to base styles output by the component."
            }, 
            "accesskey": {
                "type": "String", 
                "description": "The keyboard access key that puts the button in focus. When the button is in focus, pressing Enter clicks the button."
            }, 
            "buttonTitle": {
                "type": "String", 
                "description": "The text displayed in a tooltip when the mouse pointer hovers over the button."
            },
            "press": {
                "type": "COMPONENT", 
                "description": "Indicates that the component has been pressed."
            }, 
        }
    },

    "ui:checkboxMenuItem": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "label": {
                "type": "String", 
                "description": "The text displayed on the component."
            }, 
            "mousedown": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has pressed a mouse key."
            }, 
            "click": {
                "type": "COMPONENT", 
                "description": "Indicates that a component has been clicked."
            }, 
            "keyup": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has released a keyboard key."
            }, 
            "dblclick": {
                "type": "COMPONENT", 
                "description": "Indicates that a component has been double-clicked."
            }, 
            "mouseup": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has released the mouse button."
            }, 
            "body": {
                "type": "Component[]", 
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            }, 
            "mousemove": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has moved the mouse pointer."
            }, 
            "keypress": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has pressed and held down a keyboard key."
            }, 
            "class": {
                "type": "String", 
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            }, 
            "keydown": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has pressed and released a keyboard key."
            }, 
            "select": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has made a selection."
            }, 
            "selected": {
                "type": "Boolean", 
                "description": "The status of the menu item. True means this menu item is selected; False is not selected."
            }, 
            "type": {
                "type": "String", 
                "description": "The concrete type of the menu item. Accepted values are 'action', 'checkbox', 'radio', 'separator' or any namespaced component descriptor, e.g. ns:xxxxmenuItem."
            }, 
            "disabled": {
                "type": "Boolean", 
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is 'false'."
            }, 
            "blur": {
                "type": "COMPONENT", 
                "description": "Indicates that a component has been put out of focus."
            }, 
            "focus": {
                "type": "COMPONENT", 
                "description": "Indicates that a component has been put on focus."
            }, 
            "mouseover": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has moved the mouse pointer over the component."
            }, 
            "mouseout": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            }, 
            "hideMenuAfterSelected": {
                "type": "Boolean", 
                "description": "Set to true to hide menu after the menu item is selected."
            }
        }
    },

    "ui:inputCheckbox": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "name": {
                "description": "The name of the component.", 
                "type": "String"
            }, 
            "clearErrors": {
                "description": "Indicates that any validation error should be cleared.", 
                "type": "COMPONENT"
            }, 
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.", 
                "type": "Component[]"
            }, 
            "updateOn": {
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is 'change,click'.", 
                "type": "String"
            }, 
            "value": {
                "description": "Indicates whether the status of the option is selected. Default value is 'false'.", 
                "type": "Boolean"
            }, 
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.", 
                "type": "COMPONENT"
            }, 
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.", 
                "type": "COMPONENT"
            }, 
            "change": {
                "description": "Indicates that the content of a component or the state has changed.", 
                "type": "COMPONENT"
            }, 
            "labelClass": {
                "description": "The CSS class of the label component", 
                "type": "String"
            }, 
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.", 
                "type": "COMPONENT"
            }, 
            "validationError": {
                "description": "Indicates that the component has validation error(s).", 
                "type": "COMPONENT"
            }, 
            "blur": {
                "description": "Indicates that a component has been put out of focus.", 
                "type": "COMPONENT"
            }, 
            "paste": {
                "description": "Indicates that the user has pasted content from the clipboard.", 
                "type": "COMPONENT"
            }, 
            "copy": {
                "description": "Indicates that the user has copied content to the clipboard.", 
                "type": "COMPONENT"
            }, 
            "select": {
                "description": "Indicates that the user has made a selection.", 
                "type": "COMPONENT"
            }, 
            "text": {
                "description": "The input value attribute.", 
                "type": "String"
            }, 
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.", 
                "type": "COMPONENT"
            }, 
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.", 
                "type": "String"
            }, 
            "requiredIndicatorClass": {
                "description": "The CSS class of the required indicator component", 
                "type": "String"
            }, 
            "keydown": {
                "description": "Indicates that the user has pressed and released a keyboard key.", 
                "type": "COMPONENT"
            }, 
            "disabled": {
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is 'false'.", 
                "type": "Boolean"
            }, 
            "label": {
                "description": "The text displayed on the component.", 
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.", 
                "type": "COMPONENT"
            }, 
            "keyup": {
                "description": "Indicates that the user has released a keyboard key.", 
                "type": "COMPONENT"
            }, 
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.", 
                "type": "COMPONENT"
            }, 
            "focus": {
                "description": "Indicates that a component has been put on focus.", 
                "type": "COMPONENT"
            }, 
            "keypress": {
                "description": "Indicates that the user has pressed and held down a keyboard key.", 
                "type": "COMPONENT"
            }, 
            "cut": {
                "description": "Indicates that the user has cut content to the clipboard.", 
                "type": "COMPONENT"
            }, 
            "required": {
                "description": "Specifies whether the input is required. Default value is 'false'.", 
                "type": "Boolean"
            }, 
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.", 
                "type": "COMPONENT"
            }
        }
    },

    "ui:inputCurrency": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "disabled": {
                "type": "Boolean",
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false."
            },

            "format": {
                "type": "String",
                "description": "The format of the number. For example, format='.00' displays the number followed by two decimal places. If not specified, the Locale default format will be used."
            },

            "label": {
                "type": "String",
                "description": "The text of the label component"
            },

            "labelClass": {
                "type": "String",
                "description": "The CSS class of the label component"
            },

            "maxlength": {
                "type": "Integer",
                "description": "The maximum number of characters that can be typed into the input field. Corresponds to the maxlength attribute of the rendered HTML input element."
            },

            "placeholder": {
                "type": "String",
                "description": "Text that is displayed when the field is empty, to prompt the user for a valid entry."
            },

            "required": {
                "type": "Boolean",
                "description": "Specifies whether the input is required. Default value is false."
            },

            "requiredIndicatorClass": {
                "type": "String",
                "description": "The CSS class of the required indicator component"
            },

            "size": {
                "type": "Integer",
                "description": "The width of the input field, in characters. Corresponds to the size attribute of the rendered HTML input element."
            },

            "updateOn": {
                "type": "String",
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is change."
            },

            "value": {
                "type": "BigDecimal",
                "description": "The input value of the number."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            },

            "select": {
                "type": "COMPONENT",
                "description": "Indicates that the user has made a selection."
            },

            "blur": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put out of focus."
            },

            "focus": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put on focus."
            },

            "keypress": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and held down a keyboard key."
            },

            "keyup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released a keyboard key."
            },

            "keydown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and released a keyboard key."
            },

            "cut": {
                "type": "COMPONENT",
                "description": "Indicates that the user has cut content to the clipboard."
            },

            "validationError": {
                "type": "COMPONENT",
                "description": "Indicates that the component has validation error(s)."
            },

            "clearErrors": {
                "type": "COMPONENT",
                "description": "Indicates that any validation error should be cleared."
            },

            "change": {
                "type": "COMPONENT",
                "description": "Indicates that the content of a component or the state has changed."
            },

            "copy": {
                "type": "COMPONENT",
                "description": "Indicates that the user has copied content to the clipboard."
            },
            "paste": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pasted content from the clipboard."
            }
        }
    },

    "ui:inputDate": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "disabled": {
                "type": "Boolean",
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false."
            },

            "displayDatePicker": {
                "type": "Boolean",
                "description": "Indicate if ui:datePicker is displayed."
            },

            "format": {
                "type": "String",
                "description": "The java.text.SimpleDateFormat style format string."
            },

            "label": {
                "type": "String",
                "description": "The text of the label component"
            },

            "labelClass": {
                "type": "String",
                "description": "The CSS class of the label component"
            },

            "langLocale": {
                "type": "String",
                "description": "The language locale used to format date time."
            },

            "required": {
                "type": "Boolean",
                "description": "Specifies whether the input is required. Default value is false."
            },

            "requiredIndicatorClass": {
                "type": "String",
                "description": "The CSS class of the required indicator component"
            },

            "updateOn": {
                "type": "String",
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is 'change'."
            },

            "value": {
                "type": "Date",
                "description": "The input value of the date/time."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            },

            "select": {
                "type": "COMPONENT",
                "description": "Indicates that the user has made a selection."
            },

            "blur": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put out of focus."
            },

            "focus": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put on focus."
            },

            "keypress": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and held down a keyboard key."
            },

            "keyup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released a keyboard key."
            },

            "keydown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and released a keyboard key."
            },

            "cut": {
                "type": "COMPONENT",
                "description": "Indicates that the user has cut content to the clipboard."
            },

            "validationError": {
                "type": "COMPONENT",
                "description": "Indicates that the component has validation error(s)."
            },

            "clearErrors": {
                "type": "COMPONENT",
                "description": "Indicates that any validation error should be cleared."
            },

            "change": {
                "type": "COMPONENT",
                "description": "Indicates that the content of a component or the state has changed."
            },

            "copy": {
                "type": "COMPONENT",
                "description": "Indicates that the user has copied content to the clipboard."
            },

            "paste": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pasted content from the clipboard."
            }
        }
    },

    "ui:inputDateTime": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "disabled": {
                "type": "Boolean",
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is 'false'."
            },

            "displayDatePicker": {
                "type": "Boolean",
                "description": "Indicate if ui:datePicker is displayed."
            },

            "format": {
                "type": "String",
                "description": "The java.text.SimpleDateFormat style format string."
            },

            "label": {
                "type": "String",
                "description": "The text of the label component"
            },

            "labelClass": {
                "type": "String",
                "description": "The CSS class of the label component"
            },

            "langLocale": {
                "type": "String",
                "description": "The language locale used to format date time."
            },

            "required": {
                "type": "Boolean",
                "description": "Specifies whether the input is required. Default value is 'false'."
            },

            "requiredIndicatorClass": {
                "type": "String",
                "description": "The CSS class of the required indicator component"
            },

            "updateOn": {
                "type": "String",
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is 'change'."
            },

            "value": {
                "type": "String",
                "description": "The input value of the date/time."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            },

            "select": {
                "type": "COMPONENT",
                "description": "Indicates that the user has made a selection."
            },

            "blur": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put out of focus."
            },

            "focus": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put on focus."
            },

            "keypress": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and held down a keyboard key."
            },

            "keyup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released a keyboard key."
            },

            "keydown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and released a keyboard key."
            },

            "cut": {
                "type": "COMPONENT",
                "description": "Indicates that the user has cut content to the clipboard."
            },

            "validationError": {
                "type": "COMPONENT",
                "description": "Indicates that the component has validation error(s)."
            },

            "clearErrors": {
                "type": "COMPONENT",
                "description": "Indicates that any validation error should be cleared."
            },

            "change": {
                "type": "COMPONENT",
                "description": "Indicates that the content of a component or the state has changed."
            },

            "copy": {
                "type": "COMPONENT",
                "description": "Indicates that the user has copied content to the clipboard."
            },

            "paste": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pasted content from the clipboard."
            }
        }
    },

    "ui:inputDefaultError": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]", 
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String", 
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "value": {
                "type": "ArrayList", 
                "description": "The list of errors strings to be displayed."
            },

            "dblclick": {
                "type": "COMPONENT", 
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT", 
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has pressed a mouse key."
            }
        }
    },

    "ui:inputEmail": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "disabled": {
                "type": "Boolean",
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is 'false'."
            },

            "label": {
                "type": "String",
                "description": "The text of the label component"
            },

            "labelClass": {
                "type": "String",
                "description": "The CSS class of the label component"
            },

            "maxlength": {
                "type": "Integer",
                "description": "The maximum number of characters that can be typed into the input field. Corresponds to the maxlength attribute of the rendered HTML input element."
            },

            "placeholder": {
                "type": "String",
                "description": "Text that is displayed when the field is empty, to prompt the user for a valid entry."
            },

            "required": {
                "type": "Boolean",
                "description": "Specifies whether the input is required. Default value is 'false'."
            },

            "requiredIndicatorClass": {
                "type": "String",
                "description": "The CSS class of the required indicator component"
            },

            "size": {
                "type": "Integer",
                "description": "The width of the input field, in characters. Corresponds to the size attribute of the rendered HTML input element."
            },

            "updateOn": {
                "type": "String",
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is 'change'."
            },

            "value": {
                "type": "String",
                "description": "The value currently in the input field."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            },

            "select": {
                "type": "COMPONENT",
                "description": "Indicates that the user has made a selection."
            },

            "blur": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put out of focus."
            },

            "focus": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put on focus."
            },

            "keypress": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and held down a keyboard key."
            },

            "keyup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released a keyboard key."
            },

            "keydown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and released a keyboard key."
            },

            "cut": {
                "type": "COMPONENT",
                "description": "Indicates that the user has cut content to the clipboard."
            },

            "validationError": {
                "type": "COMPONENT",
                "description": "Indicates that the component has validation error(s)."
            },

            "clearErrors": {
                "type": "COMPONENT",
                "description": "Indicates that any validation error should be cleared."
            },

            "change": {
                "type": "COMPONENT",
                "description": "Indicates that the content of a component or the state has changed."
            },

            "copy": {
                "type": "COMPONENT",
                "description": "Indicates that the user has copied content to the clipboard."
            },

            "paste": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pasted content from the clipboard."
            }
        }
    },

    "ui:inputNumber": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "disabled": {
                "type": "Boolean",
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is 'false'."
            },

            "format": {
                "type": "String",
                "description": "The format of the number. For example, format=¡°.00¡± displays the number followed by two decimal places. If not specified, the Locale default format will be used."
            },

            "label": {
                "type": "String",
                "description": "The text of the label component"
            },

            "labelClass": {
                "type": "String",
                "description": "The CSS class of the label component"
            },

            "maxlength": {
                "type": "Integer",
                "description": "The maximum number of characters that can be typed into the input field. Corresponds to the maxlength attribute of the rendered HTML input element."
            },

            "placeholder": {
                "type": "String",
                "description": "Text that is displayed when the field is empty, to prompt the user for a valid entry."
            },

            "required": {
                "type": "Boolean",
                "description": "Specifies whether the input is required. Default value is 'false'."
            },

            "requiredIndicatorClass": {
                "type": "String",
                "description": "The CSS class of the required indicator component"
            },

            "size": {
                "type": "Integer",
                "description": "The width of the input field, in characters. Corresponds to the size attribute of the rendered HTML input element."
            },

            "updateOn": {
                "type": "String",
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is 'change'."
            },

            "value": {
                "type": "BigDecimal",
                "description": "The input value of the number."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            },

            "select": {
                "type": "COMPONENT",
                "description": "Indicates that the user has made a selection."
            },

            "blur": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put out of focus."
            },

            "focus": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put on focus."
            },

            "keypress": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and held down a keyboard key."
            },

            "keyup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released a keyboard key."
            },

            "keydown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and released a keyboard key."
            },

            "cut": {
                "type": "COMPONENT",
                "description": "Indicates that the user has cut content to the clipboard."
            },

            "validationError": {
                "type": "COMPONENT",
                "description": "Indicates that the component has validation error(s)."
            },

            "clearErrors": {
                "type": "COMPONENT",
                "description": "Indicates that any validation error should be cleared."
            },

            "change": {
                "type": "COMPONENT",
                "description": "Indicates that the content of a component or the state has changed."
            },

            "copy": {
                "type": "COMPONENT",
                "description": "Indicates that the user has copied content to the clipboard."
            },

            "paste": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pasted content from the clipboard."
            }
        }
    },

    "ui:inputPhone": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "disabled": {
                "type": "Boolean",
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is 'false'."
            },

            "label": {
                "type": "String",
                "description": "The text of the label component"
            },

            "labelClass": {
                "type": "String",
                "description": "The CSS class of the label component"
            },

            "maxlength": {
                "type": "Integer",
                "description": "The maximum number of characters that can be typed into the input field. Corresponds to the maxlength attribute of the rendered HTML input element."
            },

            "placeholder": {
                "type": "String",
                "description": "Text that is displayed when the field is empty, to prompt the user for a valid entry."
            },

            "required": {
                "type": "Boolean",
                "description": "Specifies whether the input is required. Default value is 'false'."
            },

            "requiredIndicatorClass": {
                "type": "String",
                "description": "The CSS class of the required indicator component"
            },

            "size": {
                "type": "Integer",
                "description": "The width of the input field, in characters. Corresponds to the size attribute of the rendered HTML input element."
            },

            "updateOn": {
                "type": "String",
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is 'change'."
            },

            "value": {
                "type": "String",
                "description": "The value currently in the input field."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            },

            "select": {
                "type": "COMPONENT",
                "description": "Indicates that the user has made a selection."
            },

            "blur": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put out of focus."
            },

            "focus": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put on focus."
            },

            "keypress": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and held down a keyboard key."
            },

            "keyup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released a keyboard key."
            },

            "keydown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and released a keyboard key."
            },

            "cut": {
                "type": "COMPONENT",
                "description": "Indicates that the user has cut content to the clipboard."
            },

            "validationError": {
                "type": "COMPONENT",
                "description": "Indicates that the component has validation error(s)."
            },

            "clearErrors": {
                "type": "COMPONENT",
                "description": "Indicates that any validation error should be cleared."
            },

            "change": {
                "type": "COMPONENT",
                "description": "Indicates that the content of a component or the state has changed."
            },

            "copy": {
                "type": "COMPONENT",
                "description": "Indicates that the user has copied content to the clipboard."
            },

            "paste": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pasted content from the clipboard."
            }
        }
    },

    "ui:inputRadio": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "disabled": {
                "type": "Boolean",
                "description": "Specifies whether this radio button should be displayed in a disabled state. Disabled radio buttons can't be clicked. Default value is false."
            },

            "label": {
                "type": "String",
                "description": "The text displayed on the component."
            },

            "labelClass": {
                "type": "String",
                "description": "The CSS class of the label component"
            },

            "name": {
                "type": "String",
                "description": "The name of the component."
            },

            "required": {
                "type": "Boolean",
                "description": "Specifies whether the input is required. Default value is false."
            },

            "requiredIndicatorClass": {
                "type": "String",
                "description": "The CSS class of the required indicator component"
            },

            "text": {
                "type": "String",
                "description": "The input value attribute."
            },

            "updateOn": {
                "type": "String",
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is change."
            },

            "value": {
                "type": "Boolean",
                "description": "Indicates whether the status of the option is selected. Default value is false."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            },

            "select": {
                "type": "COMPONENT",
                "description": "Indicates that the user has made a selection."
            },

            "blur": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put out of focus."
            },

            "focus": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put on focus."
            },

            "keypress": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and held down a keyboard key."
            },

            "keyup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released a keyboard key."
            },

            "keydown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and released a keyboard key."
            },

            "cut": {
                "type": "COMPONENT",
                "description": "Indicates that the user has cut content to the clipboard."
            },

            "validationError": {
                "type": "COMPONENT",
                "description": "Indicates that the component has validation error(s)."
            },

            "clearErrors": {
                "type": "COMPONENT",
                "description": "Indicates that any validation error should be cleared."
            },

            "change": {
                "type": "COMPONENT",
                "description": "Indicates that the content of a component or the state has changed."
            },

            "copy": {
                "type": "COMPONENT",
                "description": "Indicates that the user has copied content to the clipboard."
            },

            "paste": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pasted content from the clipboard."
            }
        }
    },

    "ui:inputRichText": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "cols": {
                "type": "Integer",
                "description": "The width of the text area, which is defined by the number of characters to display in a single row at a time. Default value is ¡°20¡±."
            },

            "disabled": {
                "type": "Boolean",
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false."
            },

            "height": {
                "type": "String",
                "description": "The height of the editing area (that includes the editor content). This can be an integer, for pixel sizes, or any CSS-defined length unit."
            },

            "label": {
                "type": "String",
                "description": "The text of the label component"
            },

            "labelClass": {
                "type": "String",
                "description": "The CSS class of the label component"
            },

            "maxlength": {
                "type": "Integer",
                "description": "The maximum number of characters that can be typed into the input field. Corresponds to the maxlength attribute of the rendered HTML textarea element."
            },

            "placeholder": {
                "type": "String",
                "description": "The text that is displayed by default."
            },

            "readonly": {
                "type": "Boolean",
                "description": "Specifies whether the text area should be rendered as read-only. Default value is ¡°false¡±."
            },

            "required": {
                "type": "Boolean",
                "description": "Specifies whether the input is required. Default value is false."
            },

            "requiredIndicatorClass": {
                "type": "String",
                "description": "The CSS class of the required indicator component"
            },

            "resizable": {
                "type": "Boolean",
                "description": "Specifies whether or not the textarea should be resizable. Defaults to true."
            },

            "rows": {
                "type": "Integer",
                "description": "The height of the text area, which is defined by the number of rows to display at a time. Default value is '2'."
            },

            "updateOn": {
                "type": "String",
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is change."
            },

            "value": {
                "type": "String",
                "description": "The value currently in the input field."
            },

            "width": {
                "type": "String",
                "description": "The editor UI outer width. This can be an integer, for pixel sizes, or any CSS-defined unit. If isRichText is set to false, use the cols attribute instead."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            },

            "select": {
                "type": "COMPONENT",
                "description": "Indicates that the user has made a selection."
            },

            "blur": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put out of focus."
            },

            "focus": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put on focus."
            },

            "keypress": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and held down a keyboard key."
            },

            "keyup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released a keyboard key."
            },

            "keydown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and released a keyboard key."
            },

            "cut": {
                "type": "COMPONENT",
                "description": "Indicates that the user has cut content to the clipboard."
            },

            "validationError": {
                "type": "COMPONENT",
                "description": "Indicates that the component has validation error(s)."
            },

            "clearErrors": {
                "type": "COMPONENT",
                "description": "Indicates that any validation error should be cleared."
            },

            "change": {
                "type": "COMPONENT",
                "description": "Indicates that the content of a component or the state has changed."
            },

            "copy": {
                "type": "COMPONENT",
                "description": "Indicates that the user has copied content to the clipboard."
            },

            "paste": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pasted content from the clipboard."
            }
        }
    },

    "ui:inputSecret": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "disabled": {
                "type": "Boolean",
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false."
            },

            "label": {
                "type": "String",
                "description": "The text of the label component"
            },

            "labelClass": {
                "type": "String",
                "description": "The CSS class of the label component"
            },

            "maxlength": {
                "type": "Integer",
                "description": "The maximum number of characters that can be typed into the input field. Corresponds to the maxlength attribute of the rendered HTML input element."
            },

            "placeholder": {
                "type": "String",
                "description": "Text that is displayed when the field is empty, to prompt the user for a valid entry."
            },

            "required": {
                "type": "Boolean",
                "description": "Specifies whether the input is required. Default value is false."
            },

            "requiredIndicatorClass": {
                "type": "String",
                "description": "The CSS class of the required indicator component"
            },

            "size": {
                "type": "Integer",
                "description": "The width of the input field, in characters. Corresponds to the size attribute of the rendered HTML input element."
            },

            "updateOn": {
                "type": "String",
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is 'change'."
            },

            "value": {
                "type": "String",
                "description": "The value currently in the input field."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            },

            "select": {
                "type": "COMPONENT",
                "description": "Indicates that the user has made a selection."
            },

            "blur": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put out of focus."
            },

            "focus": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put on focus."
            },

            "keypress": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and held down a keyboard key."
            },

            "keyup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released a keyboard key."
            },

            "keydown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and released a keyboard key."
            },

            "cut": {
                "type": "COMPONENT",
                "description": "Indicates that the user has cut content to the clipboard."
            },

            "validationError": {
                "type": "COMPONENT",
                "description": "Indicates that the component has validation error(s)."
            },

            "clearErrors": {
                "type": "COMPONENT",
                "description": "Indicates that any validation error should be cleared."
            },

            "change": {
                "type": "COMPONENT",
                "description": "Indicates that the content of a component or the state has changed."
            },

            "copy": {
                "type": "COMPONENT",
                "description": "Indicates that the user has copied content to the clipboard."
            },

            "paste": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pasted content from the clipboard."
            }
        }
    },

    "ui:inputSelect": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "disabled": {
                "type": "Boolean",
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false."
            },

            "label": {
                "type": "String",
                "description": "The text of the label component"
            },

            "labelClass": {
                "type": "String",
                "description": "The CSS class of the label component"
            },

            "multiple": {
                "type": "Boolean",
                "description": "Specifies whether the input is a multiple select. Default value is ¡°false¡±."
            },

            "options": {
                "type": "List",
                "description": "A list of aura.components.ui.InputOption."
            },

            "required": {
                "type": "Boolean",
                "description": "Specifies whether the input is required. Default value is false."
            },

            "requiredIndicatorClass": {
                "type": "String",
                "description": "The CSS class of the required indicator component"
            },

            "updateOn": {
                "type": "String",
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is change."
            },

            "value": {
                "type": "String",
                "description": "The value currently in the input field."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            },

            "select": {
                "type": "COMPONENT",
                "description": "Indicates that the user has made a selection."
            },

            "blur": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put out of focus."
            },

            "focus": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put on focus."
            },

            "keypress": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and held down a keyboard key."
            },

            "keyup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released a keyboard key."
            },

            "keydown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and released a keyboard key."
            },

            "cut": {
                "type": "COMPONENT",
                "description": "Indicates that the user has cut content to the clipboard."
            },

            "validationError": {
                "type": "COMPONENT",
                "description": "Indicates that the component has validation error(s)."
            },

            "clearErrors": {
                "type": "COMPONENT",
                "description": "Indicates that any validation error should be cleared."
            },

            "change": {
                "type": "COMPONENT",
                "description": "Indicates that the content of a component or the state has changed."
            },

            "copy": {
                "type": "COMPONENT",
                "description": "Indicates that the user has copied content to the clipboard."
            },

            "paste": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pasted content from the clipboard."
            }
        }
    },

    "ui:inputSelectOption": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "disabled": {
                "type": "Boolean",
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false."
            },

            "label": {
                "type": "String",
                "description": "The text displayed on the component."
            },

            "name": {
                "type": "String",
                "description": "The name of the component."
            },

            "text": {
                "type": "String",
                "description": "The input value attribute."
            },

            "value": {
                "type": "Boolean",
                "description": "Indicates whether the status of the option is selected. Default value is ¡°false¡±."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            },

            "select": {
                "type": "COMPONENT",
                "description": "Indicates that the user has made a selection."
            },

            "blur": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put out of focus."
            },

            "focus": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put on focus."
            },

            "keypress": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and held down a keyboard key."
            },

            "keyup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released a keyboard key."
            },

            "keydown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and released a keyboard key."
            }
        }
    },

    "ui:inputText": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "disabled": {
                "type": "Boolean",
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false."
            },

            "label": {
                "type": "String",
                "description": "The text of the label component"
            },

            "labelClass": {
                "type": "String",
                "description": "The CSS class of the label component"
            },

            "maxlength": {
                "type": "Integer",
                "description": "The maximum number of characters that can be typed into the input field. Corresponds to the maxlength attribute of the rendered HTML input element."
            },

            "placeholder": {
                "type": "String",
                "description": "Text that is displayed when the field is empty, to prompt the user for a valid entry."
            },

            "required": {
                "type": "Boolean",
                "description": "Specifies whether the input is required. Default value is false."
            },

            "requiredIndicatorClass": {
                "type": "String",
                "description": "The CSS class of the required indicator component"
            },

            "size": {
                "type": "Integer",
                "description": "The width of the input field, in characters. Corresponds to the size attribute of the rendered HTML input element."
            },

            "updateOn": {
                "type": "String",
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is change."
            },

            "value": {
                "type": "String",
                "description": "The value currently in the input field."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            },

            "select": {
                "type": "COMPONENT",
                "description": "Indicates that the user has made a selection."
            },

            "blur": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put out of focus."
            },

            "focus": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put on focus."
            },

            "keypress": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and held down a keyboard key."
            },

            "keyup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released a keyboard key."
            },

            "keydown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and released a keyboard key."
            },

            "cut": {
                "type": "COMPONENT",
                "description": "Indicates that the user has cut content to the clipboard."
            },

            "validationError": {
                "type": "COMPONENT",
                "description": "Indicates that the component has validation error(s)."
            },

            "clearErrors": {
                "type": "COMPONENT",
                "description": "Indicates that any validation error should be cleared."
            },

            "change": {
                "type": "COMPONENT",
                "description": "Indicates that the content of a component or the state has changed."
            },

            "copy": {
                "type": "COMPONENT",
                "description": "Indicates that the user has copied content to the clipboard."
            },

            "paste": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pasted content from the clipboard."
            }
        }
    },

    "ui:inputTextArea": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "cols": {
                "type": "Integer",
                "description": "The width of the text area, which is defined by the number of characters to display in a single row at a time. Default value is '20'."
            },

            "disabled": {
                "type": "Boolean",
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is 'false'."
            },

            "label": {
                "type": "String",
                "description": "The text of the label component"
            },

            "labelClass": {
                "type": "String",
                "description": "The CSS class of the label component"
            },

            "maxlength": {
                "type": "Integer",
                "description": "The maximum number of characters that can be typed into the input field. Corresponds to the maxlength attribute of the rendered HTML textarea element."
            },

            "placeholder": {
                "type": "String",
                "description": "The text that is displayed by default."
            },

            "readonly": {
                "type": "Boolean",
                "description": "Specifies whether the text area should be rendered as read-only. Default value is 'false'."
            },

            "required": {
                "type": "Boolean",
                "description": "Specifies whether the input is required. Default value is 'false'."
            },

            "requiredIndicatorClass": {
                "type": "String",
                "description": "The CSS class of the required indicator component"
            },

            "resizable": {
                "type": "Boolean",
                "description": "Specifies whether or not the textarea should be resizable. Defaults to true."
            },

            "rows": {
                "type": "Integer",
                "description": "The height of the text area, which is defined by the number of rows to display at a time. Default value is '2'."
            },

            "updateOn": {
                "type": "String",
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is 'change'."
            },

            "value": {
                "type": "String",
                "description": "The value currently in the input field."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            },

            "select": {
                "type": "COMPONENT",
                "description": "Indicates that the user has made a selection."
            },

            "blur": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put out of focus."
            },

            "focus": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put on focus."
            },

            "keypress": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and held down a keyboard key."
            },

            "keyup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released a keyboard key."
            },

            "keydown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and released a keyboard key."
            },

            "cut": {
                "type": "COMPONENT",
                "description": "Indicates that the user has cut content to the clipboard."
            },

            "validationError": {
                "type": "COMPONENT",
                "description": "Indicates that the component has validation error(s)."
            },

            "clearErrors": {
                "type": "COMPONENT",
                "description": "Indicates that any validation error should be cleared."
            },

            "change": {
                "type": "COMPONENT",
                "description": "Indicates that the content of a component or the state has changed."
            },

            "copy": {
                "type": "COMPONENT",
                "description": "Indicates that the user has copied content to the clipboard."
            },

            "paste": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pasted content from the clipboard."
            }
        }
    },

    "ui:inputURL": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "disabled": {
                "type": "Boolean",
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false."
            },

            "label": {
                "type": "String",
                "description": "The text of the label component"
            },

            "labelClass": {
                "type": "String",
                "description": "The CSS class of the label component"
            },

            "maxlength": {
                "type": "Integer",
                "description": "The maximum number of characters that can be typed into the input field. Corresponds to the maxlength attribute of the rendered HTML input element."
            },

            "placeholder": {
                "type": "String",
                "description": "Text that is displayed when the field is empty, to prompt the user for a valid entry."
            },

            "required": {
                "type": "Boolean",
                "description": "Specifies whether the input is required. Default value is false."
            },

            "requiredIndicatorClass": {
                "type": "String",
                "description": "The CSS class of the required indicator component"
            },

            "size": {
                "type": "Integer",
                "description": "The width of the input field, in characters. Corresponds to the size attribute of the rendered HTML input element."
            },

            "updateOn": {
                "type": "String",
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is change."
            },

            "value": {
                "type": "String",
                "description": "The value currently in the input field."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            },

            "select": {
                "type": "COMPONENT",
                "description": "Indicates that the user has made a selection."
            },

            "blur": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put out of focus."
            },

            "focus": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put on focus."
            },

            "keypress": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and held down a keyboard key."
            },

            "keyup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released a keyboard key."
            },

            "keydown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and released a keyboard key."
            },

            "cut": {
                "type": "COMPONENT",
                "description": "Indicates that the user has cut content to the clipboard."
            },

            "validationError": {
                "type": "COMPONENT",
                "description": "Indicates that the component has validation error(s)."
            },

            "clearErrors": {
                "type": "COMPONENT",
                "description": "Indicates that any validation error should be cleared."
            },

            "change": {
                "type": "COMPONENT",
                "description": "Indicates that the content of a component or the state has changed."
            },

            "copy": {
                "type": "COMPONENT",
                "description": "Indicates that the user has copied content to the clipboard."
            },

            "paste": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pasted content from the clipboard."
            }
        }
    },

    "ui:menu": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            }
        }
    },

    "ui:menuItem": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "disabled": {
                "type": "Boolean",
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false."
            },

            "hideMenuAfterSelected": {
                "type": "Boolean",
                "description": "Set to true to hide menu after the menu item is selected."
            },

            "label": {
                "type": "String",
                "description": "The text displayed on the component."
            },

            "selected": {
                "type": "Boolean",
                "description": "The status of the menu item. True means this menu item is selected; False is not selected."
            },

            "type": {
                "type": "String",
                "values": [
                    "action", "checkbox", "radio", "separator", "${1:ns:xxxxmenuItem}"
                ],
                "description": "The concrete type of the menu item. Accepted values are 'action', 'checkbox', 'radio', 'separator' or any namespaced component descriptor, e.g. ns:xxxxmenuItem."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            },

            "select": {
                "type": "COMPONENT",
                "description": "Indicates that the user has made a selection."
            },

            "blur": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put out of focus."
            },

            "focus": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put on focus."
            },

            "keypress": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and held down a keyboard key."
            },

            "keyup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released a keyboard key."
            },

            "keydown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and released a keyboard key."
            }
        }
    },

    "ui:menuItemSeparator": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            }
        }
    },

    "ui:menuList": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "autoPosition": {
                "type": "Boolean",
                "description": "Move the popup target up when there is not enough space at the bottom to display. Note: even if autoPosition is set to false, popup will still position the menu relative to the trigger. To override default positioning, use manualPosition attribute."
            },

            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "closeOnClickOutside": {
                "type": "Boolean",
                "description": "Close target when user clicks or taps outside of the target"
            },

            "closeOnTabKey": {
                "type": "Boolean",
                "description": "Indicates whether to close the target list on tab key or not."
            },

            "curtain": {
                "type": "Boolean",
                "description": "Whether or not to apply an overlay under the target."
            },

            "menuItems": {
                "type": "List",
                "description": "A list of menu items set explicitly using instances of the Java class: aura.components.ui.MenuItem."
            },

            "visible": {
                "type": "Boolean",
                "description": "Controls the visibility of the menu. The default is false, which hides the menu."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            },

            "expand": {
                "type": "COMPONENT",
                "description": "Indicates that a component expands."
            },

            "menuSelect": {
                "type": "COMPONENT",
                "description": "Indicates that the user selects a menu item inside a menu component."
            },

            "collapse": {
                "type": "COMPONENT",
                "description": "Indicates that a component collapses."
            },

            "menuFocusChange": {
                "type": "COMPONENT",
                "description": "Indicates that the user changes menu item focus inside a menu component."
            }
        }
    },

    "ui:menuTrigger": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "disabled": {
                "type": "Boolean",
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false."
            },

            "title": {
                "type": "String",
                "description": "The text to display as a tooltip when the mouse pointer hovers over this component."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            },

            "select": {
                "type": "COMPONENT",
                "description": "Indicates that the user has made a selection."
            },

            "blur": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put out of focus."
            },

            "focus": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put on focus."
            },

            "keypress": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and held down a keyboard key."
            },

            "keyup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released a keyboard key."
            },

            "keydown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and released a keyboard key."
            },

            "menuTriggerPress": {
                "type": "COMPONENT",
                "description": "Indicates that the menu trigger is clicked."
            }
        }
    },

    "ui:menuTriggerLink": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]", 
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String", 
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "disabled": {
                "type": "Boolean", 
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false."
            },

            "label": {
                "type": "String", 
                "description": "The text displayed on the component."
            },

            "title": {
                "type": "String", 
                "description": "The text to display as a tooltip when the mouse pointer hovers over this component."
            },

            "dblclick": {
                "type": "COMPONENT", 
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT", 
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has pressed a mouse key."
            },

            "select": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has made a selection."
            },

            "blur": {
                "type": "COMPONENT", 
                "description": "Indicates that a component has been put out of focus."
            },

            "focus": {
                "type": "COMPONENT", 
                "description": "Indicates that a component has been put on focus."
            },

            "keypress": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has pressed and held down a keyboard key."
            },

            "keyup": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has released a keyboard key."
            },

            "keydown": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has pressed and released a keyboard key."
            },

            "menuTriggerPress": {
                "type": "COMPONENT", 
                "description": "Indicates that the menu trigger is clicked."
            }
        }
    },

    "ui:message": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "closable": {
                "type": "Boolean",
                "description": "Specifies whether to display an 'x' that will close the alert when clicked. Default value is 'false'."
            },

            "severity": {
                "type": "String",
                "description": "The severity of the message. Possible values: message (default), confirm, info, warning, error"
            },

            "title": {
                "type": "String",
                "description": "The title text for the message."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            }
        }
    },

    "ui:outputCheckbox": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "altChecked": {
                "type": "String",
                "description": "The alternate text description when the checkbox is checked. Default value is 'True'."
            },

            "altUnchecked": {
                "type": "String",
                "description": "The alternate text description when the checkbox is unchecked. Default value is 'False'."
            },

            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "value": {
                "type": "Boolean",
                "description": "Specifies whether the checkbox is checked."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            }
        }
    },

    "ui:outputCurrency": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "type": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "type": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "currencyCode": {
                "type": "String",
                "type": "The ISO 4217 currency code specified as a String, e.g. USD."
            },

            "currencySymbol": {
                "type": "String",
                "type": "The currency symbol specified as a String."
            },

            "format": {
                "type": "String",
                "type": "The format of the number. For example, format=¡°.00¡± displays the number followed by two decimal places. If not specified, the default format based on the browser's locale will be used."
            },

            "value": {
                "type": "BigDecimal",
                "type": "The output value of the currency, which is defined as type Decimal."
            },

            "dblclick": {
                "type": "COMPONENT",
                "type": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "type": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "type": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "type": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "type": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "type": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "type": "Indicates that the user has pressed a mouse key."
            }
        }
    },

    "ui:outputData": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]", 
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String", 
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "format": {
                "type": "String", 
                "description": "A string (pattern letters are defined in java.text.SimpleDateFormat) used to format the date and time of the value attribute."
            },

            "langLocale": {
                "type": "String", 
                "description": "The language locale used to format date value."
            },

            "value": {
                "type": "String", 
                "description": "The output value of the date. It should be a date string in ISO-8601 format (YYYY-MM-DD)."
            },

            "dblclick": {
                "type": "COMPONENT", 
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT", 
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has pressed a mouse key."
            }
        }
    },

    "ui:outputDataTime": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]", 
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String", 
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "format": {
                "type": "String", 
                "description": "A string (pattern letters are defined in java.text.SimpleDateFormat) used to format the date and time of the value attribute."
            },

            "langLocale": {
                "type": "String", 
                "description": "The language locale used to format date value."
            },

            "timezone": {
                "type": "String", 
                "description": "The timezone ID, for example, America/Los_Angeles."
            },

            "value": {
                "type": "String", 
                "description": "An ISO8601-formatted string representing a date time."
            },

            "dblclick": {
                "type": "COMPONENT", 
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT", 
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT", 
                "description": "Indicates that the user has pressed a mouse key."
            }
        }
    },

    "ui:outputEmail": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "value": {
                "type": "String",
                "description": "The output value of the email"
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            }
        }
    },

    "ui:outputNumber": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "format": {
                "type": "String",
                "description": "The format of the number. For example, format=¡°.00¡± displays the number followed by two decimal places. If not specified, the Locale default format will be used."
            },

            "value": {
                "type": "BigDecimal",
                "description": "The number displayed when this component is rendered."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            }
        }
    },

    "ui:outputPhone": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "value": {
                "type": "String",
                "description": "The phone number displayed when this component is rendered."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            }
        }
    },

    "ui:outputRichText": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "value": {
                "type": "String",
                "description": "The richly-formatted text used for output."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            }
        }
    },

    "ui:outputText": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "value": {
                "type": "String",
                "description": "The text displayed when this component is rendered."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            }
        }
    },

    "ui:outputTextArea": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "value": {
                "type": "String",
                "description": "The text to display."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            }
        }
    },

    "ui:outputURL": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "alt": {
                "type": "String",
                "description": "The alternate text description for image (used when there is no label)"
            },

            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "disabled": {
                "type": "Boolean",
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false."
            },

            "iconClass": {
                "type": "String",
                "description": "The CSS style used to display the icon or image."
            },

            "label": {
                "type": "String",
                "description": "The text displayed on the component."
            },

            "target": {
                "type": "Picklist",
                "values": [
                    "_blank", "_parent", "_self", "_top"
                ],
                "description": "The target destination where this rendered component is displayed. Possible values: _blank, _parent, _self, _top"
            },

            "title": {
                "type": "String",
                "description": "The text to display as a tooltip when the mouse pointer hovers over this component."
            },

            "value": {
                "type": "String",
                "description": "The text displayed when this component is rendered."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            }
        }
    },

    "ui:radioMenuItem": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "class": {
                "type": "String",
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component."
            },

            "disabled": {
                "type": "Boolean",
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false."
            },

            "hideMenuAfterSelected": {
                "type": "Boolean",
                "description": "Set to true to hide menu after the menu item is selected."
            },

            "label": {
                "type": "String",
                "description": "The text displayed on the component."
            },

            "selected": {
                "type": "Boolean",
                "description": "The status of the menu item. True means this menu item is selected; False is not selected."
            },

            "type": {
                "type": "Picklist",
                "values": [
                    "action", "checkbox", "radio", "separator", "${1:ns:xxxxmenuItem}"
                ],
                "description": "The concrete type of the menu item. Accepted values are 'action', 'checkbox', 'radio', 'separator' or any namespaced component descriptor, e.g. ns:xxxxmenuItem."
            },

            "dblclick": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been double-clicked."
            },

            "mouseover": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer over the component."
            },

            "mouseout": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer away from the component."
            },

            "mouseup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released the mouse button."
            },

            "mousemove": {
                "type": "COMPONENT",
                "description": "Indicates that the user has moved the mouse pointer."
            },

            "click": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been clicked."
            },

            "mousedown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed a mouse key."
            },

            "select": {
                "type": "COMPONENT",
                "description": "Indicates that the user has made a selection."
            },

            "blur": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put out of focus."
            },

            "focus": {
                "type": "COMPONENT",
                "description": "Indicates that a component has been put on focus."
            },

            "keypress": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and held down a keyboard key."
            },

            "keyup": {
                "type": "COMPONENT",
                "description": "Indicates that the user has released a keyboard key."
            },

            "keydown": {
                "type": "COMPONENT",
                "description": "Indicates that the user has pressed and released a keyboard key."
            }

        }
    },

    "ui:spinner": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag."
            },

            "isVisible": {
                "type": "Boolean",
                "description": "Specifies whether or not this spinner should be visible. Defaults to true."
            },

            "toggleLoadingIndicator": {
                "type": "COMPONENT",
                "description": "Change the visibility of a ui:spinner component."
            }
        }
    },

    "apex:attribute": {
        "simple": False,
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "required": {
                "type": "Boolean"
            },
            "description": {
                "type": "String"
            }
        }
    },

    # ChatterAnswer
    "chatteranswers:aboutme": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "communityId": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "noSignIn": {
                "type": "Boolean"
            },
            "rendered": {
                "type": "Boolean"
            }
        }
    },

    "chatteranswers:allfeeds": {
        "simple": False,
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "id": {
                "type": "String"
            },
            "jsApiVersion": {
                "type": "Double"
            },
            "noSignIn": {
                "type": "Boolean"
            },
            "rendered": {
                "type": "Boolean"
            },
            "useUrlRewriter": {
                "type": "Boolean"
            }
        }
    },

    "chatteranswers:changepassword": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        }
    },

    "chatteranswers:datacategoryfilter": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "communityId": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        }
    },

    "chatteranswers:feedfilter": {
        "simple": False,
        "type": "visualforce",
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
                "type": "Boolean"
            }
        }
    },

    "chatteranswers:feeds": {
        "simple": False,
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "rendered": {
                "type": "Boolean"
            },
            "useUrlRewriter": {
                "type": "Boolean"
            }
        }
    },

    "chatteranswers:forgotpassword": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            },
            "useUrlRewriter": {
                "type": "Boolean"
            }
        }
    },

    "chatteranswers:forgotpasswordconfirm": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            },
            "useUrlRewriter": {
                "type": "Boolean"
            }
        }
    },

    "chatteranswers:guestsignin": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            },
            "useUrlRewriter": {
                "type": "Boolean"
            }
        }
    },

    "chatteranswers:help": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        }
    },

    "chatteranswers:login": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            },
            "useUrlRewriter": {
                "type": "Boolean"
            }
        }
    },

    "chatteranswers:registration": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "hideTerms": {
                "type": "Boolean"
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
                "type": "Boolean"
            },
            "useUrlRewriter": {
                "type": "Boolean"
            }
        }
    },

    "chatteranswers:searchask": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "communityId": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "noSignIn": {
                "type": "Boolean"
            },
            "rendered": {
                "type": "Boolean"
            },
            "searchLanguage": {
                "type": "String"
            },
            "useUrlRewriter": {
                "type": "Boolean"
            }
        }
    },

    "chatteranswers:singleitemfeed": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "entityId": {
                "type": "id"
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        }
    },

    # Messaging part
    "messaging:attachment": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "filename": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "inline": {
                "type": "Boolean"
            },
            "renderAs": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        }
    },
    "apex:emailPublisher": {
        "type": "visualforce",
        "attribs": {
            "autoCollapseBody": {
                "type": "Boolean"
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
                "type": "Boolean"
            },
            "entityId": {
                "type": "id"
            },
            "expandableHeader": {
                "type": "Boolean"
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
                "type": "Boolean"
            },
            "reRender": {
                "type": "Object"
            },
            "sendButtonName": {
                "type": "String"
            },
            "showAdditionalFields": {
                "type": "Boolean"
            },
            "showAttachments": {
                "type": "Boolean"
            },
            "showSendButton": {
                "type": "Boolean"
            },
            "showTemplates": {
                "type": "Boolean"
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
                "type": "Boolean"
            },
            "width": {
                "type": "String"
            }
        }
    },
    "messaging:emailHeader": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "name": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        }
    },
    "messaging:emailTemplate": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        }
    },
    "messaging:plainTextEmailBody": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        }
    },

    # analytics part
    "analytics:reportChart": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "filter": {
                "type": "json",
                "values":[
                    '{"column": $1, "operator": $2, "value": $3}'
                ]
            },
            "hideOnError": {
                "type": "Boolean"
            },
            "rendered": {
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "action": {
                "type": "ApexPages.Action"
            },
            "enabled": {
                "type": "Boolean"
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
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "immediate": {
                "type": "Boolean"
            },
            "rendered": {
                "type": "Boolean"
            },
            "renderRegionOnly": {
                "type": "Boolean"
            }
        }
    },
    "apex:actionStatus": {
        "simple": False,
        "type": "visualforce",
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
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "action": {
                "type": "ApexPages.Action"
            },
            "disabled": {
                "type": "Boolean"
            },
            "disableDefault": {
                "type": "Boolean"
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
                "type": "Boolean"
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
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
                "type": "Boolean"
            },
            "rendererFn": {
                "type": "String"
            },
            "showInLegend": {
                "type": "Boolean"
            },
            "tips": {
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "dashSize": {
                "type": "Integer"
            },
            "fields": {
                "type": "String"
            },
            "grid": {
                "type": "Boolean"
            },
            "gridFill": {
                "type": "Boolean"
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
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "groupGutter": {
                "type": "Integer"
            },
            "gutter": {
                "type": "Integer"
            },
            "highlight": {
                "type": "Boolean"
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
                "type": "Boolean"
            },
            "rendererFn": {
                "type": "String"
            },
            "showInLegend": {
                "type": "Boolean"
            },
            "stacked": {
                "type": "Boolean"
            },
            "tips": {
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "animate": {
                "type": "Boolean"
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
                "type": "Boolean"
            },
            "height": {
                "type": "String"
            },
            "hidden": {
                "type": "Boolean"
            },
            "id": {
                "type": "String"
            },
            "legend": {
                "type": "Boolean"
            },
            "name": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            },
            "renderTo": {
                "type": "String"
            },
            "resizable": {
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "rendererFn": {
                "type": "String"
            },
            "trackMouse": {
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "breakBefore": {
                "type": "Boolean"
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
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "access": {
                "type": "Picklist",
                "values": [
                    "public",
                    "global"
                ]
            },
            "allowDML": {
                "type": "Boolean"
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
                "type": "Boolean"
            },
            "selfClosing": {
                "type": "Boolean"
            }
        }
    },
    "apex:componentBody": {
        "simple": True,
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        }
    },
    "apex:commandButton": {
        "simple": True,
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "id": {
                "type": "String"
            },
            "image": {
                "type": "String"
            },
            "immediate": {
                "type": "Boolean"
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
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
                "type": "Boolean"
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
        "type": "visualforce",
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
        "type": "visualforce",
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
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "name": {
                "type": "String"
            }
        }
    },
    "apex:detail": {
        "simple": True,
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "inlineEdit": {
                "type": "Boolean"
            },
            "oncomplete": {
                "type": "String"
            },
            "relatedList": {
                "type": "Boolean"
            },
            "relatedListHover": {
                "type": "Boolean"
            },
            "rendered": {
                "type": "Boolean"
            },
            "rerender": {
                "type": "String"
            },
            "showChatter": {
                "type": "Boolean"
            },
            "subject": {
                "type": "String"
            },
            "title": {
                "type": "Boolean"
            }
        }
    },
    "apex:dynamicComponent": {
        "simple": True,
        "type": "visualforce",
        "attribs": {
            "componentValue": {
                "type": "UIComponent"
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        }
    },
    "apex:enhancedList": {
        "simple": True,
        "type": "visualforce",
        "attribs": {
            "customizable": {
                "type": "Boolean"
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
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "name": {
                "type": "String"
            }
        }
    },
    "apex:flash": {
        "simple": False,
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "play": {
                "type": "Boolean"
            },
            "rendered": {
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
                "type": "Boolean"
            },
            "rendered": {
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "id": {
                "type": "String"
            },
            "labelField": {
                "type": "String"
            },
            "needle": {
                "type": "Boolean"
            },
            "rendered": {
                "type": "Boolean"
            },
            "rendererFn": {
                "type": "String"
            },
            "tips": {
                "type": "Boolean"
            }
        }
    },
    "apex:iframe": {
        "simple": True,
        "type": "visualforce",
        "attribs": {
            "frameborder": {
                "type": "Boolean"
            },
            "height": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            },
            "scrolling": {
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "pageName": {
                "type": "ApexPages.PageReference"
            },
            "rendered": {
                "type": "Boolean"
            }
        }
    },
    "apex:includeScript": {
        "simple": True,
        "type": "visualforce",
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
        "type": "visualforce",
        "attribs": {
            "changedStyleClass": {
                "type": "String"
            },
            "disabled": {
                "type": "Boolean"
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
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
                "type": "Boolean"
            },
            "required": {
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "id": {
                "type": "String"
            },
            "immediate": {
                "type": "Boolean"
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
                "type": "Boolean"
            },
            "required": {
                "type": "Boolean"
            },
            "selected": {
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "required": {
                "type": "Boolean"
            },
            "list": {
                "type": "Object"
            },
            "showDatePicker": {
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "immediate": {
                "type": "Boolean"
            },
            "rendered": {
                "type": "Boolean"
            },
            "required": {
                "type": "Boolean"
            },
            "value": {
                "type": "Object"
            }
        }
    },
    "apex:inputSecret": {
        "simple": True,
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "id": {
                "type": "String"
            },
            "immediate": {
                "type": "Boolean"
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
                "type": "Boolean"
            },
            "redisplay": {
                "type": "Boolean"
            },
            "rendered": {
                "type": "Boolean"
            },
            "required": {
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
                "type": "Boolean"
            },
            "required": {
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
                "type": "Boolean"
            },
            "rendered": {
                "type": "Boolean"
            },
            "required": {
                "type": "Boolean"
            },
            "richText": {
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "name": {
                "type": "String"
            }
        }
    },
    "apex:legend": {
        "simple": False,
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "spacing": {
                "type": "Integer"
            }
        }
    },
    "apex:lineSeries": {
        "simple": False,
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "fillColor": {
                "type": "String"
            },
            "highlight": {
                "type": "Boolean"
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
                "type": "Boolean"
            },
            "rendererFn": {
                "type": "String"
            },
            "showInLegend": {
                "type": "Boolean"
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
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            },
            "type": {
                "type": "String"
            }
        }
    },
    "apex:logCallPublisher": {
        "type": "visualforce",
        "attribs": {
            "autoCollapseBody": {
                "type": "Boolean"
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
                "type": "Boolean"
            },
            "reRender": {
                "type": "Object"
            },
            "showAdditionalFields": {
                "type": "Boolean"
            },
            "showSubmitButton": {
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "showOnlyActiveInfoWindow": {
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "maxWidth": {
                "type": "Integer"
            },
            "rendered": {
                "type": "Boolean"
            }
        }
    },
    "apex:mapMarker": {
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "title": {
                "type": "String"
            }
        }
    },
    "apex:message": {
        "simple": True,
        "type": "visualforce",
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
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "dir": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "globalOnly": {
                "type": "Boolean"
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
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "entityId": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        }
    },
    "apex:outputField": {
        "simple": True,
        "type": "visualforce",
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
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "dir": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "escape": {
                "type": "Boolean"
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
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "applyHtmlTag": {
                "type": "Boolean"
            },
            "cache": {
                "type": "Boolean"
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
                "type": "Boolean"
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
                "type": "Boolean"
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
                "type": "Boolean"
            },
            "setup": {
                "type": "Boolean"
            },
            "showChat": {
                "type": "Boolean"
            },
            "showHeader": {
                "type": "Boolean"
            },
            "sidebar": {
                "type": "Boolean"
            },
            "standardController": {
                "type": "String"
            },
            "standardStylesheets": {
                "type": "Boolean"
            },
            "tabStyle": {
                "type": "String"
            },
            "title": {
                "type": "String"
            },
            "wizard": {
                "type": "Boolean"
            }
        }
    },
    "apex:pageBlock": {
        "simple": False,
        "type": "visualforce",
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
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "collapsible": {
                "type": "Boolean"
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
                "type": "Boolean"
            },
            "showHeader": {
                "type": "Boolean"
            },
            "title": {
                "type": "String"
            }
        }
    },
    "apex:pageBlockSectionItem": {
        "simple": False,
        "type": "visualforce",
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
                "type": "Boolean"
            }
        }
    },
    "apex:pageBlockTable": {
        "simple": False,
        "type": "visualforce",
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
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "detail": {
                "type": "String"
            },
            "escape": {
                "type": "Boolean"
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "escape": {
                "type": "Boolean"
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            },
            "showDetail": {
                "type": "Boolean"
            }
        }
    },
    "apex:panelBar": {
        "simple": False,
        "type": "visualforce",
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
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
            }
        }
    },
    "apex:panelGrid": {
        "simple": False,
        "type": "visualforce",
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
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
        "type": "visualforce",
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
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "id": {
                "type": "String"
            },
            "labelField": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            },
            "rendererFn": {
                "type": "String"
            },
            "showInLegend": {
                "type": "Boolean"
            },
            "tips": {
                "type": "Boolean"
            }
        }
    },
    "apex:radarSeries": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "fill": {
                "type": "String"
            },
            "highlight": {
                "type": "Boolean"
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
                "type": "Boolean"
            },
            "showInLegend": {
                "type": "Boolean"
            },
            "strokeColor": {
                "type": "String"
            },
            "strokeWidth": {
                "type": "Integer"
            },
            "tips": {
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
            }
        }
    },
    "apex:remoteObjectModel": {
        "type": "visualforce",
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
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "first": {
                "type": "Integer"
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
                "type": "Boolean"
            },
            "rendererFn": {
                "type": "String"
            },
            "showInLegend": {
                "type": "Boolean"
            },
            "tips": {
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "scrollbars": {
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "accesskey": {
                "type": "String"
            },
            "border": {
                "type": "Integer"
            },
            "borderVisible": {
                "type": "Boolean"
            },
            "dirs": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "disabled": {
                "type": "Boolean"
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
                "type": "Boolean"
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
                "type": "Boolean"
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
                "type": "Boolean"
            },
            "rendered": {
                "type": "Boolean"
            },
            "required": {
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
                "type": "Boolean"
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
                "type": "Boolean"
            },
            "rendered": {
                "type": "Boolean"
            },
            "required": {
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "itemEscaped": {
                "type": "Boolean"
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
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            },
            "value": {
                "type": "Object"
            }
        }
    },
    "apex:selectRadio": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "accesskey": {
                "type": "String"
            },
            "border": {
                "type": "Integer"
            },
            "borderVisible": {
                "type": "Boolean"
            },
            "dirs": {
                "type": "Picklist",
                "values": [
                    "RTL",
                    "LTR"
                ]
            },
            "disabled": {
                "type": "Boolean"
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
                "type": "Boolean"
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
                "type": "Boolean"
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
                "type": "Boolean"
            },
            "rendered": {
                "type": "Boolean"
            },
            "required": {
                "type": "Boolean"
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
        "type": "visualforce",
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
    "apex:tab": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "disabled": {
                "type": "Boolean"
            },
            "focus": {
                "type": "String"
            },
            "id": {
                "type": "String"
            },
            "immediate": {
                "type": "Boolean"
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
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "objectId": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            },
            "reRender": {
                "type": "String"
            }
        }
    },
    "c:sitefooter": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        }
    },
    "c:siteheader": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        }
    },
    "c:sitelogin": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        }
    },
    "c:sitepoweredby": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        }
    },
    "chatter:feed": {
        "simple": True,
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "reRender": {
                "type": "String"
            },
            "showPublisher": {
                "type": "Boolean"
            }
        }
    },
    "chatter:feedWithFollowers": {
        "simple": True,
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "reRender": {
                "type": "String"
            },
            "showHeader": {
                "type": "Boolean"
            }
        }
    },
    "chatter:follow": {
        "simple": True,
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "reRender": {
                "type": "String"
            }
        }
    },
    "chatter:followers": {
        "simple": True,
        "type": "visualforce",
        "attribs": {
            "entityId": {
                "type": "id"
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        }
    },
    "chatter:newsfeed": {
        "simple": True,
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "onComplete": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            },
            "reRender": {
                "type": "String"
            }
        }
    },
    "chatter:userPhotoUpload": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            },
            "showOriginalPhoto": {
                "type": "Boolean"
            }
        }
    },
    "flow:interview": {
        "simple": False,
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "rerender": {
                "type": "String"
            },
            "showHelp": {
                "type": "Boolean"
            }
        }
    },
    "ideas:detailOutputLink": {
        "simple": False,
        "type": "visualforce",
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
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "sort": {
                "type": "String"
            },
            "status": {
                "type": "String"
            },
            "stickyAttributes": {
                "type": "Boolean"
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
        "type": "visualforce",
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
                "type": "Boolean"
            },
            "sort": {
                "type": "String"
            },
            "stickyAttributes": {
                "type": "Boolean"
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
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        }
    },
    "site:previewAsAdmin": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        }
    },
    "social:profileViewer": {
        "simple": False,
        "type": "visualforce",
        "attribs": {
            "entityId": {
                "type": "id"
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        }
    },
    "support:clickToDial": {
        "simple": False,
        "type": "visualforce",
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
                "type": "Boolean"
            }
        }
    }
}