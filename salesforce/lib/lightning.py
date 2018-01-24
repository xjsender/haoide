# Metadata for Lightning component

component_interfaces = [
    "clients:availableForMailAppAppPage",
    "clients:hasEventContext",
    "clients:hasItemContext",
    "flexipage:availableForAllPageTypes",
    "flexipage:availableForRecordHome",
    "flexipage:availableForAllPageTypes",
    "forceCommunity:availableForAllPageTypes",
    "force:appHostable",
    "force:lightningQuickAction",
    "force:lightningQuickActionWithoutHeader",
    "force:lightningQuickAction",
    "ltng:allowGuestAccess",
    "force:hasRecordId",
    "force:hasSObjectName",
    "lightning:actionOverride",
    "lightning:appHomeTemplate",
    "lightning:availableForChatterExtensionComposer",
    "lightning:availableForChatterExtensionRenderer",
    "lightning:availableForFlowScreens",
    "lightning:homeTemplate",
    "lightning:recordHomeTemplate",
    "lightning:prechatUI"
]

# Since 2018, Spring18, v42
event_references = [
    "force:closeQuickAction",
    "force:createRecord",
    "force:editRecord",
    "force:navigateToComponent",
    "force:navigateToList",
    "force:navigateToObjectHome",
    "force:navigateToRelatedList",
    "force:navigateToSObject",
    "force:navigateToURL",
    "force:recordSave",
    "force:recordSaveSuccess",
    "force:refreshView",
    "force:showToast",
    "forceCommunity:analyticsInteraction",
    "forceCommunity:routeChange",
    "lightning:openFiles",
    "lightning:sendChatterExtensionPayload",
    "ltng:selectSObject",
    "ltng:sendMessage",
    "wave:discoverDashboard",
    "wave:discoverResponse",
    "wave:selectionChanged",
    "wave:update"
]

# Attributes which type is ApexPages.PageReference
page_reference_attrs = [
    "page",
    "template",
    "pageName",
    "finishLocation"
]

# ["analytics", "aura", "force", "forceChatter", "forceCommunity", "lightning", "ltng", "ui", "wave"]
tag_defs = {
    "analytics:reportChart": {
        "attribs": {
            "filter": {
                "type": "json",
                "values": [
                    "{\"column\": $1, \"operator\": $2, \"value\": $3}"
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "aura:application": {
        "attribs": {
            "access": {
                "type": "Picklist",
                "values": [
                    "public",
                    "global"
                ]
            },
            "controller": {
                "description": "The server-side controller class for the app. The format is namespace.myController.",
                "type": "String"
            },
            "description": {
                "type": "String"
            },
            "extends": {
                "type": "Component"
            },
            "implements": {
                "type": "String"
            },
            "useAppcache": {
                "type": "Boolean"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "aura:attribute": {
        "attribs": {
            "access": {
                "type": "Picklist",
                "values": [
                    "public",
                    "global",
                    "PRIVATE"
                ]
            },
            "default": {
                "type": "String"
            },
            "description": {
                "type": "String"
            },
            "name": {
                "type": "String"
            },
            "required": {
                "type": "Boolean"
            },
            "type": {
                "type": "Picklist",
                "supportSobjects": True,
                "values": [
                    "Boolean",
                    "Date",
                    "DateTime",
                    "Decimal",
                    "Double",
                    "Integer",
                    "Long",
                    "String",
                    "Object",
                    "List",
                    "Set",
                    "Map"
                ]
            }
        },
        "simple": False,
        "type": "aura"
    },
    "aura:component": {
        "attribs": {
            "access": {
                "type": "Picklist",
                "values": [
                    "public",
                    "global"
                ]
            },
            "body": {
                "type": "String"
            },
            "controller": {
                "type": "String"
            },
            "description": {
                "type": "String"
            },
            "extends": {
                "type": "Component"
            },
            "implements": {
                "type": "String"
            },
            "isTemplate": {
                "type": "Boolean"
            },
            "template": {
                "type": "Component"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "aura:dependency": {
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
                    "COMPONENT",
                    "APPLICATION",
                    "EVENT"
                ]
            }
        },
        "simple": False,
        "type": "aura"
    },
    "aura:event": {
        "attribs": {
            "access": {
                "type": "Picklist",
                "values": [
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
                    "COMPONENT",
                    "APPLICATION"
                ]
            }
        },
        "simple": False,
        "type": "aura"
    },
    "aura:expression": {
        "attribs": {
            "value": {
                "description": "The expression to evaluate and render.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "aura:handler": {
        "attribs": {
            "action": {
                "type": "Object"
            },
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
            "name": {
                "type": "text"
            },
            "value": {
                "type": "String"
            },
            "includeFacets": {
                "type": "Boolean"
            },
            "phase": {
                "type": "Picklist",
                "values": [
                    "bubble",
                    "capture"
                ]
            }
        },
        "simple": False,
        "type": "aura"
    },
    "aura:html": {
        "attribs": {
            "HTMLAttributes": {
                "description": "A Map of attributes to set on the html element.",
                "type": "HashMap"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "tag": {
                "description": "The name of the html element that should be rendered.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "aura:if": {
        "attribs": {
            "else": {
                "type": "ComponentDefRef[]"
            },
            "isTrue": {
                "type": "Boolean"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "aura:interface": {
        "attribs": {
            "access": {
                "type": "Picklist",
                "values": [
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
        },
        "simple": False,
        "type": "aura"
    },
    "aura:iteration": {
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
            }
        },
        "simple": False,
        "type": "aura"
    },
    "aura:method": {
        "attribs": {
            "access": {
                "type": "Picklist",
                "values": [
                    "public",
                    "global"
                ]
            },
            "action": {
                "type": "Expression",
                "values": [
                    "{!c.$0}",
                    "{!}"
                ]
            },
            "description": {
                "type": "String"
            },
            "name": {
                "description": "The method name. Use the method name to call the method in JavaScript code",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "aura:registerEvent": {
        "attribs": {
            "name": {
                "type": "text"
            },
            "type": {
                "type": "Picklist",
                "values": [
                    "ui:expand",
                    "ui:collapse",
                    "ui:menuFocusChange",
                    "ui:menuSelect",
                    "ui:menuTriggerPress",
                    "c:${1:MyEvent}"
                ]
            }
        },
        "simple": False,
        "type": "aura"
    },
    "aura:renderIf": {
        "attribs": {
            "else": {
                "type": "ComponentDefRef[]"
            },
            "isTrue": {
                "type": "Boolean"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "aura:set": {
        "attribs": {
            "attribute": {
                "type": "String"
            },
            "value": {
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "aura:template": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "bodyClass": {
                "description": "Extra body CSS styles",
                "type": "String"
            },
            "defaultBodyClass": {
                "description": "Default body CSS styles.",
                "type": "String"
            },
            "doctype": {
                "description": "The DOCTYPE declaration for the template",
                "type": "String"
            },
            "errorMessage": {
                "description": "Error loading text",
                "type": "String"
            },
            "errorTitle": {
                "description": "Error title when an error has occured.",
                "type": "String"
            },
            "loadingText": {
                "description": "Loading text",
                "type": "String"
            },
            "title": {
                "description": "The title of the template.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "aura:unescapedHtml": {
        "attribs": {
            "body": {
                "description": "The body of <aura:unescapedHtml> is ignored and won't be rendered.",
                "type": "Component[]"
            },
            "value": {
                "description": "The string that should be rendered as unescaped HTML.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "auraStorage:init": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "clearStorageOnInit": {
                "description": "Set to true to delete all previous data on initialization (relevant for persistent storage only). This value defaults to true.",
                "type": "Boolean"
            },
            "debugLoggingEnabled": {
                "description": "Set to true to enable debug logging with $A.log(). This value defaults to false.",
                "type": "Boolean"
            },
            "defaultAutoRefreshInterval": {
                "description": "The default duration (seconds) before an auto refresh request will be initiated. Actions may override this on a per-entry basis with Action.setStorable(). This value defaults to 30.",
                "type": "Integer"
            },
            "defaultExpiration": {
                "description": "The default duration (seconds) that an object will be retained in storage. Actions may override this on a per-entry basis with Action.setStorable(). This value defaults to 10.",
                "type": "Integer"
            },
            "maxSize": {
                "description": "Maximum size (KB) of the storage instance. Existing items will be evicted to make room for new items; algorithm is adapter-specific. This value defaults to 1000. ",
                "type": "Integer"
            },
            "name": {
                "description": "The programmatic name for the storage instance.",
                "type": "String"
            },
            "persistent": {
                "description": "Set to true if this storage desires persistence. This value defaults to false.",
                "type": "Boolean"
            },
            "secure": {
                "description": "Set to true if this storage requires secure storage support. This value defaults to false.",
                "type": "Boolean"
            },
            "version": {
                "description": "Version to associate with all stored items.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },

    "force:canvasApp": {
        "attribs": {
            "applicationName": {
                "description": "Name of the canvas app. Either applicationName or developerName is required.",
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "border": {
                "description": "Width of the canvas app border, in pixels. If not specified, defaults to 0 px.",
                "type": "String"
            },
            "canvasId": {
                "description": "An unique label within a page for the Canvas app window. This should be used when targeting events to this canvas app.",
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
            "displayLocation": {
                "description": "The location in the application where the canvas app is currently being called from.",
                "type": "String"
            },
            "height": {
                "description": "Canvas app window height, in pixels. If not specified, defaults to 900 px.",
                "type": "String"
            },
            "maxHeight": {
                "description": "The maximum height of the Canvas app window in pixels. Defaults to 2000 px; 'infinite' is also a valid value.",
                "type": "String"
            },
            "maxWidth": {
                "description": "The maximum width of the Canvas app window in pixels. Defaults to 1000 px; 'infinite' is also a valid value.",
                "type": "String"
            },
            "namespacePrefix": {
                "description": "Namespace value of the Developer Edition organization in which the canvas app was created. Optional if the canvas app wasn\u00a1\u00aft created in a Developer Edition organization. If not specified, defaults to null.",
                "type": "String"
            },
            "onCanvasAppError": {
                "description": "Name of the JavaScript function to be called if the canvas app fails to render.",
                "type": "String"
            },
            "onCanvasAppLoad": {
                "description": "Name of the JavaScript function to be called after the canvas app loads.",
                "type": "String"
            },
            "onCanvasSubscribed": {
                "description": "Name of the JavaScript function to be called after the canvas app registers with the parent.",
                "type": "String"
            },
            "parameters": {
                "description": "Object representation of parameters passed to the canvas app. This should be supplied in JSON format or as a JavaScript object literal. Here\u00a1\u00afs an example of parameters in a JavaScript object literal: {param1:'value1',param2:'value2'}. If not specified, defaults to null.",
                "type": "String"
            },
            "referenceId": {
                "description": "The reference id of the canvas app, if set this is used instead of developerName, applicationName and namespacePrefix",
                "type": "String"
            },
            "scrolling": {
                "description": "Canvas window scrolling",
                "type": "String"
            },
            "sublocation": {
                "description": "The sublocation is the location in the application where the canvas app is currently being called from, for ex, displayLocation can be PageLayout and sublocation can be S1MobileCardPreview or S1MobileCardFullview, etc",
                "type": "String"
            },
            "title": {
                "description": "Title for the link",
                "type": "String"
            },
            "watermark": {
                "description": "Renders a link if set to true",
                "type": "Boolean"
            },
            "width": {
                "description": "Canvas app window width, in pixels. If not specified, defaults to 800 px.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "force:inputField": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "The CSS style used to display the field.",
                "type": "String"
            },
            "errorComponent": {
                "description": "A component which is responsible for displaying the error message.",
                "type": "Component[]"
            },
            "required": {
                "description": "Specifies whether this field is required or not.",
                "type": "Boolean"
            },
            "value": {
                "description": "Data value of Salesforce field to which to bind.",
                "type": "Object"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "force:outputField": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "value": {
                "description": "Data value of Salesforce field to which to bind.",
                "type": "Object"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "force:recordData": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "fields": {
                "description": "Specifies which of the record's fields to query.",
                "type": "String[]"
            },
            "layoutType": {
                "description": "Name of the layout to query, which determines the fields included. Valid values are FULL or COMPACT. The layoutType and/or fields attribute must be specified.",
                "type": "String"
            },
            "mode": {
                "description": "The mode in which to load the record: VIEW (default) or EDIT.",
                "type": "Picklist",
                "values": [
                    "VIEW",
                    "EDIT"
                ]
            },
            "recordId": {
                "description": "The record Id",
                "type": "String"
            },
            "recordUpdated": {
                "description": "Event fired when the record has changed.",
                "type": "COMPONENT"
            },
            "targetError": {
                "description": "Will be set to the localized error message if the record can't be provided.",
                "type": "String"
            },
            "targetFields": {
                "description": "A simplified view of the fields in targetRecord, to reference record fields in component markup.",
                "type": "Object"
            },
            "targetRecord": {
                "description": "The provided record. This attribute will contain only the fields relevant to the requested layoutType and/or fields atributes.",
                "type": "Object"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "force:recordEdit": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "recordId": {
                "description": "The Id of the record to load, optional if record attribute is specified.",
                "type": "String"
            },
            "recordSave": {
                "description": "Record save request",
                "type": "COMPONENT"
            },
            "recordSaveSuccess": {
                "description": "Indicates that the record has been successfully saved.",
                "type": "COMPONENT"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "force:recordPreview": {
        "attribs": {
            "fields": {
                "description": "List of fields to query. This attribute or layoutType must be specified. If you specify both, the list of fields queried is the union of fields from fields and layoutType.",
                "type": "String[]"
            },
            "ignoreExistingAction": {
                "description": "Whether to skip the cache and force a server request. Defaults to false.Setting this attribute to true is useful for handling user-triggered actions such as pull-to-refresh.",
                "type": "Boolean"
            },
            "layoutType": {
                "description": "Name of the layout to query, which determines the fields included",
                "type": "String"
            },
            "mode": {
                "description": "The mode in which to access the record. Valid values are the following. -VIEW -EDIT. Defaults to VIEW.",
                "type": "Picklist",
                "values": [
                    "VIEW",
                    "EDIT"
                ]
            },
            "recordId": {
                "description": "The 15-character or 18-character ID of the record to load, modify, or delete. Defaults to null, to create a record.",
                "type": "String"
            },
            "recordUpdated": {
                "description": "The event fired when the record is loaded, changed, updated, or removed.",
                "type": "COMPONENT"
            },
            "targetError": {
                "description": "A reference to a component attribute to which a localized error message is assigned if necessary.",
                "type": "String"
            },
            "targetRecord": {
                "description": "A reference to a component attribute, to which the loaded record is assigned.Changes to the record are also assigned to this value, which triggers change handlers, re-renders, and so on.",
                "type": "Record"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "force:recordView": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "record": {
                "description": "The record (SObject) to load, optional if recordId attribute is specified.",
                "type": "SObjectRow"
            },
            "recordId": {
                "description": "The Id of the record to load, optional if record attribute is specified.",
                "type": "String"
            },
            "type": {
                "description": "The type of layout to use to display the record. Possible values: FULL, MINI. The default is FULL.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "forceChatter:feed": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "subjectId": {
                "description": "For most feeds tied to an entity, this is used specified the desired entity. Defaults to the current user if not specified",
                "type": "String"
            },
            "type": {
                "description": "The strategy used to find items associated with the subject. Valid values include: News, Home, Record, To.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "forceChatter:fullFeed": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "handleNavigationEvents": {
                "description": "Should this component handle navigation events for entities and urls. If true then navigation events will result in the entity or url being opened in a new window.",
                "type": "Boolean"
            },
            "subjectId": {
                "description": "For most feeds tied to an entity, this is used specified the desired entity. Defaults to the current user if not specified",
                "type": "String"
            },
            "type": {
                "description": "The strategy used to find items associated with the subject. Valid values include: News, Home, Record, To.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "forceChatter:publisher": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "context": {
                "description": "The context in which the component is being displayed (RECORD or GLOBAL). RECORD is for a record feed, and GLOBAL is for all other feed types. This attribute is case-sensitive.",
                "type": "String"
            },
            "recordId": {
                "description": "The record Id",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "forceCommunity:appLauncher": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "forceCommunity:navigationMenuBase": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "menuItems": {
                "description": "Automatically populated with data of menu item. This attribute is read-only.",
                "type": "Object"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "forceCommunity:notifications": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "forceCommunity:routeLink": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the anchor tag.",
                "type": "String"
            },
            "id": {
                "description": "The ID of the anchor tag.",
                "type": "String"
            },
            "label": {
                "description": "The text displayed in the link.",
                "type": "String"
            },
            "onClick": {
                "description": "Action to trigger when the anchor is clicked.",
                "type": "Action"
            },
            "routeInput": {
                "description": "The map of dynamic parameters that create the link. Only recordId-based routes are supported.",
                "type": "HashMap"
            },
            "title": {
                "description": "The text to display for the link tooltip.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "forceCommunity:waveDashboard": {
        "attribs": {
            "accessToken": {
                "description": "A valid access token obtained by logging into Salesforce. Useful when the component is used by Lightning Out in a non-Salesforce domain.",
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "dashboardId": {
                "description": "The unique ID of the dashboard",
                "type": "String"
            },
            "developerName": {
                "description": "The unique developer name of the dashboard",
                "type": "String"
            },
            "filter": {
                "description": "Adds selections or filters to the embedded dashboard at runtime",
                "type": "String"
            },
            "height": {
                "description": "Specifies the height of the dashboard, in pixels.",
                "type": "Integer"
            },
            "hideOnError": {
                "description": "Controls whether or not users see a dashboard that has an error",
                "type": "Boolean"
            },
            "openLinksInNewWindow": {
                "description": "If false, links to other dashboards will be opened in the same window.",
                "type": "Boolean"
            },
            "recordId": {
                "description": "Id of the current entity in the context of which the component is being displayed.",
                "type": "String"
            },
            "showHeader": {
                "description": "If true, the dashboard is displayed with a header bar that includes dashboard information and controls",
                "type": "Boolean"
            },
            "showSharing": {
                "description": "If true, and the dashboard is shareable, then the dashboard shows the Share icon",
                "type": "Boolean"
            },
            "showTitle": {
                "description": "If true, tile of the dashboard is included above the dashboard. If false, the dashboard appears without a title.",
                "type": "Boolean"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:accordion": {
        "attribs": {
            "activeSectionName": {
                "description": "The activeSectionName changes the default expanded section. The first section in the accordion is expanded by default.",
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:accordionSection": {
        "attribs": {
            "actions": {
                "description": "Enables a custom menu implementation. Actions are displayed to the right of the section title.",
                "type": "Component[]"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "label": {
                "description": "The text that displays as the title of the section.",
                "type": "String"
            },
            "name": {
                "description": "The unique section name to use with the activeSectionName attribute in the lightning:accordion component.",
                "type": "String"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:avatar": {
        "attribs": {
            "alternativeText": {
                "description": "The alternative text used to describe the avatar, which is displayed as hover text on the image. Required",
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "size": {
                "description": "The size of the avatar. Valid values are x-small, small, medium, and large. This value defaults to medium.",
                "type": "String"
            },
            "src": {
                "description": "The URL for the image. Required",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:badge": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "label": {
                "description": "The text to be displayed inside the badge.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:breadcrumb": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "href": {
                "description": "The URL of the page that the breadcrumb goes to.",
                "type": "String"
            },
            "label": {
                "description": "The text label for the breadcrumb.",
                "type": "String"
            },
            "name": {
                "description": "The name for the breadcrumb component. This value is optional and can be used to identify the breadcrumb in a callback.",
                "type": "String"
            },
            "onclick": {
                "description": "The action triggered when the breadcrumb is clicked.",
                "type": "Action"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:breadcrumbs": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "href": {
                "description": "The URL of the page that the breadcrumb goes to.",
                "type": "String"
            },
            "label": {
                "description": "The text label for the breadcrumb. Required.",
                "type": "String"
            },
            "name": {
                "description": "The name for the breadcrumb component. This value is optional and can be used to identify the breadcrumb in a callback.",
                "type": "String"
            },
            "onclick": {
                "description": "The action triggered when the breadcrumb is clicked.",
                "type": "Action"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:button": {
        "attribs": {
            "accesskey": {
                "description": "Specifies a shortcut key to activate or focus an element.",
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "disabled": {
                "description": "Specifies whether this button should be displayed in a disabled state. Disabled buttons can't be clicked. This value defaults to false.",
                "type": "Boolean"
            },
            "iconName": {
                "description": "The Lightning Design System name of the icon. ",
                "type": "String"
            },
            "iconPosition": {
                "description": "Describes the position of the icon with respect to body. Options include left and right. This value defaults to left.",
                "type": "String"
            },
            "label": {
                "description": "The text to be displayed inside the button.",
                "type": "String"
            },
            "name": {
                "description": "The name for the button element. This value is optional and can be used to identify the button in a callback.",
                "type": "String"
            },
            "onblur": {
                "description": "The action triggered when the element releases focus.",
                "type": "Action"
            },
            "onclick": {
                "description": "The action triggered when the button is clicked.",
                "type": "Action"
            },
            "onfocus": {
                "description": "The action triggered when the element receives focus.",
                "type": "Action"
            },
            "tabindex": {
                "description": "Specifies the tab order of an element (when the tab button is used for navigating).",
                "type": "Integer"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            },
            "type": {
                "description": "Specifies the type of button. Valid values are button, reset, and submit. This value defaults to button.",
                "type": "String"
            },
            "value": {
                "description": "The value for the button element. This value is optional and can be used when submitting a form.",
                "type": "String"
            },
            "variant": {
                "description": "The variant changes the appearance of the button. Accepted variants include base, neutral, brand, destructive, and inverse. This value defaults to neutral.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:buttonGroup": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:buttonIcon": {
        "attribs": {
            "accesskey": {
                "description": "Specifies a shortcut key to activate or focus an element.",
                "type": "String"
            },
            "alternativeText": {
                "description": "The alternative text used to describe the icon. This text should describe what happens when you click the button, for example 'Upload File', not what the icon looks like, 'Paperclip'. Required.",
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "disabled": {
                "description": "Specifies whether this button should be displayed in a disabled state. Disabled buttons can't be clicked. This value defaults to false.",
                "type": "Boolean"
            },
            "iconClass": {
                "description": "The class to be applied to the contained icon element.",
                "type": "String"
            },
            "iconName": {
                "description": "The Lightning Design System name of the icon. Names are written in the format '\\utility:down\\' where 'utility' is the category, and 'down' is the specific icon to be displayed. Required.",
                "type": "String"
            },
            "name": {
                "description": "The name for the button element. This value is optional and can be used to identify the button in a callback.",
                "type": "String"
            },
            "onblur": {
                "description": "The action triggered when the element releases focus.",
                "type": "Action"
            },
            "onclick": {
                "description": "The action triggered when the button is clicked.",
                "type": "Action"
            },
            "onfocus": {
                "description": "The action triggered when the element receives focus.",
                "type": "Action"
            },
            "size": {
                "description": "The size of the buttonIcon. For the bare variant, options include x-small, small, medium, and large. For non-bare variants, options include xx-small, x-small, small, and medium. This value defaults to medium.",
                "type": "String"
            },
            "tabindex": {
                "description": "Specifies the tab order of an element (when the tab button is used for navigating).",
                "type": "Integer"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            },
            "type": {
                "description": "Specifies the type of button. Valid values are button, reset, and submit. This value defaults to button.",
                "type": "String"
            },
            "value": {
                "description": "The value for the button element. This value is optional and can be used when submitting a form.",
                "type": "String"
            },
            "variant": {
                "description": "The variant changes the appearance of the button. Accepted variants include base, neutral, brand, destructive, and inverse. This value defaults to neutral.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:buttonIconStateful": {
        "attribs": {
            "accesskey": {
                "description": "Specifies a shortcut key to activate or focus an element.",
                "type": "String"
            },
            "alternativeText": {
                "description": "The alternative text used to describe the icon. This text should describe what happens when you click the button, for example 'Upload File', not what the icon looks like, 'Paperclip'.",
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "disabled": {
                "description": "Specifies whether this button should be displayed in a disabled state. Disabled buttons can't be clicked. This value defaults to false.",
                "type": "Boolean"
            },
            "iconName": {
                "description": "The Lightning Design System name of the icon",
                "type": "String"
            },
            "name": {
                "description": "The name for the button element. This value is optional and can be used to identify the button in a callback.",
                "type": "String"
            },
            "onblur": {
                "description": "The action triggered when the element releases focus.",
                "type": "Action"
            },
            "onclick": {
                "description": "The action that will be run when the button is clicked.",
                "type": "Action"
            },
            "onfocus": {
                "description": "The action triggered when the element receives focus.",
                "type": "Action"
            },
            "selected": {
                "description": "Specifies whether button is in selected state or not",
                "type": "Boolean"
            },
            "size": {
                "description": "The size of the buttonIcon. Options include xx-small, x-small, small, and medium. This value defaults to medium.",
                "type": "String"
            },
            "tabindex": {
                "description": "Specifies the tab order of an element (when the tab button is used for navigating).",
                "type": "Integer"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            },
            "value": {
                "description": "The value for the button element. This value is optional and can be used when submitting a form.",
                "type": "String"
            },
            "variant": {
                "description": "The variant changes the appearance of buttonIcon. Accepted variants border, and border-inverse. This value defaults to border.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:buttonMenu": {
        "attribs": {
            "accesskey": {
                "description": "Specifies a shortcut key to activate or focus an element.",
                "type": "String"
            },
            "alternativeText": {
                "description": "The alternative text used to describe the icon. This text should describe what happens when you click the button, for example 'Upload File', not what the icon looks like, 'Paperclip'. Required.",
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "ComponentDefRef[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "disabled": {
                "description": "Specifies whether this button should be displayed in a disabled state. Disabled buttons can't be clicked. This value defaults to false.",
                "type": "Boolean"
            },
            "iconName": {
                "description": "The Lightning Design System name of the icon. Names are written in the format '\\utility:down\\' where 'utility' is the category, and 'down' is the specific icon to be displayed.",
                "type": "String"
            },
            "iconSize": {
                "description": "The size of the icon. Options include xx-small, x-small, medium, or large. This value defaults to medium.",
                "type": "String",
                "values": [
                    "xx-small",
                    "x-small",
                    "medium",
                    "large"
                ]
            },
            "menuAlignment": {
                "description": "Determines the alignment of the menu relative to the button. Available options are: left, center, right. This value defaults to left.",
                "type": "String"
            },
            "name": {
                "description": "The name for the button element. This value is optional and can be used to identify the button in a callback.",
                "type": "String"
            },
            "onblur": {
                "description": "The action triggered when the element releases focus.",
                "type": "Action"
            },
            "onfocus": {
                "description": "The action triggered when the element receives focus.",
                "type": "Action"
            },
            "onselect": {
                "description": "Action fired when a menu item is selected. The 'detail.menuItem' property of the passed event is the selected menu item.",
                "type": "Action"
            },
            "tabindex": {
                "description": "Specifies the tab order of an element (when the tab button is used for navigating).",
                "type": "Integer"
            },
            "title": {
                "description": "Tooltip text on the button.",
                "type": "String"
            },
            "type": {
                "description": "If true, the menu items are displayed. This value defaults to false.",
                "type": "Boolean"
            },
            "value": {
                "description": "The value for the button element. This value is optional and can be used when submitting a form.",
                "type": "String"
            },
            "variant": {
                "description": "The variant changes the appearance of the button. Accepted variants include base, neutral, brand, destructive, and inverse. This value defaults to neutral.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:buttonStateful": {
        "attribs": {
            "accesskey": {
                "description": "Specifies a shortcut key to activate or focus an element.",
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "iconNameWhenHover": {
                "description": "The name of the icon to be used in the format \\'utility:close\\' when the state is true and the button receives focus.",
                "type": "String"
            },
            "iconNameWhenOff": {
                "description": "The name of the icon to be used in the format \\'utility:add\\' when the state is false.",
                "type": "String"
            },
            "iconNameWhenOn": {
                "description": "The name of the icon to be used in the format \\'utility:check\\' when the state is true.",
                "type": "String"
            },
            "labelWhenHover": {
                "description": "The text to be displayed inside the button when state is true and the button receives focus.",
                "type": "String"
            },
            "labelWhenOff": {
                "description": "The text to be displayed inside the button when state is false.",
                "type": "String"
            },
            "labelWhenOn": {
                "description": "The text to be displayed inside the button when state is true.",
                "type": "String"
            },
            "onblur": {
                "description": "The action triggered when the element releases focus.",
                "type": "Action"
            },
            "onclick": {
                "description": "The action triggered when the button is clicked.",
                "type": "Action"
            },
            "onfocus": {
                "description": "The action triggered when the element receives focus.",
                "type": "Action"
            },
            "state": {
                "description": "The state of the button, which shows whether the button has been selected or not. The default state is false.",
                "type": "Boolean"
            },
            "tabindex": {
                "description": "Specifies the tab order of an element (when the tab button is used for navigating).",
                "type": "Integer"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            },
            "variant": {
                "description": "The variant changes the appearance of the button. Accepted variants include brand, inverse, neutral and text. This value defaults to neutral.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:card": {
        "attribs": {
            "actions": {
                "description": "Actions are components such as button or buttonIcon. Actions are displayed in the header.",
                "type": "Component[]"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "footer": {
                "description": "The footer can include text or another component",
                "type": "Component[]"
            },
            "iconName": {
                "description": "The Lightning Design System name of the icon. Names are written in the format '\\utility:down\\' where 'utility' is the category, and 'down' is the specific icon to be displayed. The icon is displayed in the header to the left of the title.",
                "type": "String"
            },
            "title": {
                "description": "The title can include text or another component, and is displayed in the header.",
                "type": "Component[]"
            },
            "variant": {
                "description": "The variant changes the appearance of the card. Accepted variants include base or narrow. This value defaults to base.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:checkboxGroup": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "disabled": {
                "description": "Set to true if the checkbox group is disabled. Checkbox selections can't be changed for a disabled checkbox group. This value defaults to false.",
                "type": "Boolean"
            },
            "label": {
                "description": "Text label for the checkbox group.",
                "type": "String"
            },
            "messageWhenValueMissing": {
                "description": "Optional message displayed when no checkbox is selected and the required attribute is set to true.",
                "type": "String"
            },
            "name": {
                "description": "The name of the checkbox group.",
                "type": "String"
            },
            "onblur": {
                "description": "The action triggered when the checkbox group releases focus.",
                "type": "Action"
            },
            "onchange": {
                "description": "The action triggered when a checkbox value changes.",
                "type": "Action"
            },
            "onfocus": {
                "description": "The action triggered when the checkbox group receives focus.",
                "type": "Action"
            },
            "options": {
                "description": "Array of label-value pairs for each checkbox.",
                "type": "List"
            },
            "required": {
                "description": "Set to true if at least one checkbox must be selected. This value defaults to false.",
                "type": "Boolean"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            },
            "value": {
                "description": "The list of selected checkboxes. Each array entry contains the value of a selected checkbox. The value of each checkbox is set in the options attribute.",
                "type": "String[]"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:clickToDial": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "params": {
                "description": "Comma-separated list of parameters to pass to the third-party phone system.",
                "type": "String"
            },
            "recordId": {
                "description": "The Salesforce record Id that's associated with the phone number.",
                "type": "String"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            },
            "value": {
                "description": "The phone number.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:combobox": {
        "attribs": {
            "accesskey": {
                "description": "Specifies a shortcut key to activate or focus an element.",
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "disabled": {
                "description": "Specifies that an input element should be disabled. This value defaults to false.",
                "type": "Boolean"
            },
            "dropdownAlignment": {
                "description": "Determines the alignment of the drop-down relative to the input. Available values are left, center, right, bottom-left, bottom-center, bottom-right. The default is left.",
                "type": "String"
            },
            "label": {
                "description": "Text label for the combobox.",
                "type": "String"
            },
            "messageWhenValueMissing": {
                "description": "Error message to be displayed when the value is missing and input is required.",
                "type": "String"
            },
            "name": {
                "description": "Specifies the name of an input element.",
                "type": "String"
            },
            "onblur": {
                "description": "The action triggered when the element releases focus.",
                "type": "Action"
            },
            "onchange": {
                "description": "The action triggered when a value attribute changes.",
                "type": "Action"
            },
            "onfocus": {
                "description": "The action triggered when the element receives focus.",
                "type": "Action"
            },
            "options": {
                "description": "A list of options that are available for selection. Each option has the following attributes: class, selected, label, and value.",
                "type": "Object[]"
            },
            "placeholder": {
                "description": "Text that is displayed before an option is selected, to prompt the user to select an option. The default is &quot;Select an Option&quot;.",
                "type": "String"
            },
            "readonly": {
                "description": "Specifies that an input field is read-only. This value defaults to false.",
                "type": "Boolean"
            },
            "required": {
                "description": "Specifies that an input field must be filled out before submitting the form. This value defaults to false.",
                "type": "Boolean"
            },
            "tabindex": {
                "description": "Specifies the tab order of an element (when the tab button is used for navigating).",
                "type": "Integer"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            },
            "validity": {
                "description": "Represents the validity states that an element can be in, with respect to constraint validation.",
                "type": "Object"
            },
            "value": {
                "description": "Specifies the value of an input element.",
                "type": "Object"
            },
            "variant": {
                "description": "The variant changes the appearance of an input field. Accepted variants include standard and label-hidden. This value defaults to standard.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:container": {
        "attribs": {
            "alternativeText": {
                "description": "Used for alternative text in accessibility scenarios.",
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "The CSS class for the iframe element.",
                "type": "String"
            },
            "onerror": {
                "description": "The client-side controller action to run when an error occurs when sending a message to the contained app.",
                "type": "Action"
            },
            "onmessage": {
                "description": "The client-side controller action to run when a message is received from the contained content.",
                "type": "Action"
            },
            "src": {
                "description": "The resource name, landing page and query params in url format. Navigation is supported only for the single page identified.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:datatable": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "columns": {
                "description": "Array of the columns object that's used to define the data types. Required properties include 'label', 'fieldName', and 'type'. The default type is 'text'.",
                "type": "List"
            },
            "data": {
                "description": "The array of data to be displayed.",
                "type": "Object"
            },
            "defaultSortDirection": {
                "description": "Specifies the default sorting direction on an unsorted column. Valid options include 'asc' and 'desc'. The default is 'asc' for sorting in ascending order.",
                "type": "String"
            },
            "hideCheckboxColumn": {
                "description": "Hides or displays the checkbox column for row selection. To hide the checkbox column, set hideCheckboxColumn to true. The default is false.",
                "type": "Boolean"
            },
            "keyField": {
                "description": "Required for better performance. Associates each row with a unique ID.",
                "type": "String"
            },
            "maxColumnWidth": {
                "description": "The maximum width for all columns. The default is 1000px.",
                "type": "Integer"
            },
            "minColumnWidth": {
                "description": "The minimum width for all columns. The default is 50px.",
                "type": "Integer"
            },
            "onrowselection": {
                "description": "The action triggered when a row is selected.",
                "type": "Action"
            },
            "onsort": {
                "description": "The action triggered when a column is sorted.",
                "type": "Action"
            },
            "resizeColumnDisabled": {
                "description": "Specifies whether column resizing is disabled. The default is false.",
                "type": "Boolean"
            },
            "resizeStep": {
                "description": "The width to resize the column when user press left or right arrow. The default is 10px.",
                "type": "Integer"
            },
            "sortedBy": {
                "description": "The column fieldName that controls the sorting order. Sort the data using the onsort event handler.",
                "type": "String"
            },
            "sortedDirection": {
                "description": "Specifies the sorting direction. Sort the data using the onsort event handler. Valid options include 'asc' and 'desc'.",
                "type": "String"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:dualListbox": {
        "attribs": {
            "accesskey": {
                "description": "Specifies a shortcut key to activate or focus an element.",
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "disabled": {
                "description": "Specifies that an input element should be disabled. This value defaults to false.",
                "type": "Boolean"
            },
            "label": {
                "description": "Label for the dual list box.",
                "type": "String"
            },
            "max": {
                "description": "Maximum number of options required in the selected options list box.",
                "type": "Integer"
            },
            "min": {
                "description": "Minimum number of options required in the selected options list box.",
                "type": "Integer"
            },
            "name": {
                "description": "Specifies the name of an input element.",
                "type": "String"
            },
            "onblur": {
                "description": "The action triggered when the element releases focus.",
                "type": "Action"
            },
            "onchange": {
                "description": "The action triggered when a value attribute changes.",
                "type": "Action"
            },
            "onfocus": {
                "description": "The action triggered when the element receives focus.",
                "type": "Action"
            },
            "options": {
                "description": "A list of options that are available for selection. Each option has the following attributes: label and value.",
                "type": "Object[]"
            },
            "readonly": {
                "description": "Specifies that an input field is read-only. This value defaults to false.",
                "type": "Boolean"
            },
            "required": {
                "description": "Specifies that an input field must be filled out before submitting the form. This value defaults to false.",
                "type": "Boolean"
            },
            "requiredOptions": {
                "description": "A list of required options that cannot be removed from selected options list box. This list is populated with values from options attribute.",
                "type": "List"
            },
            "selectedLabel": {
                "description": "Label for selected options list box.",
                "type": "String"
            },
            "sourceLabel": {
                "description": "Label for source options list box.",
                "type": "String"
            },
            "tabindex": {
                "description": "Specifies the tab order of an element (when the tab button is used for navigating).",
                "type": "Integer"
            },
            "validity": {
                "description": "Represents the validity states that an element can be in, with respect to constraint validation.",
                "type": "Object"
            },
            "value": {
                "description": "Specifies the value of an input element.",
                "type": "Object"
            },
            "values": {
                "description": "A list of default options that are included in the selected options list box. This list is populated with values from the options attribute.",
                "type": "List"
            },
            "variant": {
                "description": "The variant changes the appearance of an input field. Accepted variants include standard and label-hidden. This value defaults to standard.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:dynamicIcon": {
        "attribs": {
            "alternativeText": {
                "description": "The alternative text used to describe the dynamicIcon. This text should describe what&#x2019;s happening. For example, 'Graph is refreshing', not what the icon looks like, 'Graph'.",
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "onclick": {
                "description": "The action triggered when the icon is clicked.",
                "type": "Action"
            },
            "option": {
                "description": "The option attribute changes the appearance of the dynamicIcon",
                "type": "String"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            },
            "type": {
                "description": "The Lightning Design System name of the dynamicIcon. Valid values are: ellie, eq, score, strength, trend, and waffle.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:fileCard": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "fileId": {
                "description": "The Salesforce File ID (ContentDocument).",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:fileUpload": {
        "attribs": {
            "accept": {
                "description": "Comma-separated list of file extensions that can be uploaded in the format .ext, such as .pdf, .jpg, or .png",
                "type": "List"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "disabled": {
                "description": "Specifies whether this component should be displayed in a disabled state. Disabled components can't be clicked. This value defaults to false.",
                "type": "Boolean"
            },
            "label": {
                "description": "The text label for the file uploader.",
                "type": "String"
            },
            "multiple": {
                "description": "Specifies whether a user can upload more than one file simultanesouly. This value defaults to false.",
                "type": "Boolean"
            },
            "onuploadfinished": {
                "description": "The action triggered when files have finished uploading.",
                "type": "Action"
            },
            "recordId": {
                "description": "The record Id of the record that the uploaded file is associated to.",
                "type": "String"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:flexipageRegionInfo": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "width": {
                "description": "The width of the region that the component resides in.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:flow": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "onstatuschange": {
                "description": "The current status of the flow interview.",
                "type": "Action"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:formattedDateTime": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "day": {
                "description": "Allowed values are numeric or 2-digit.",
                "type": "String"
            },
            "era": {
                "description": "Allowed values are narrow, short, or long.",
                "type": "String"
            },
            "hour": {
                "description": "Allowed values are numeric or 2-digit.",
                "type": "String"
            },
            "hour12": {
                "description": "Determines whether time is displayed as 12-hour. If false, time displays as 24-hour. The default setting is determined by the user's locale.",
                "type": "Boolean"
            },
            "minute": {
                "description": "Allowed values are numeric or 2-digit.",
                "type": "String"
            },
            "month": {
                "description": "Allowed values are 2-digit, narrow, short, or long.",
                "type": "String"
            },
            "second": {
                "description": "Allowed values are numeric or 2-digit.",
                "type": "String"
            },
            "timeZone": {
                "description": "The time zone to use. Implementations can include any time zone listed in the IANA time zone database. The default is the runtime's default time zone. Use this attribute only if you want to override the default time zone.",
                "type": "String"
            },
            "timeZoneName": {
                "description": "Allowed values are short or long. For example, the Pacific Time zone would display as 'PST' if you select 'short', or 'Pacific Standard Time' if you select 'long.'",
                "type": "String"
            },
            "value": {
                "description": "The value to be formatted, which can be a Date object or timestamp.",
                "type": "Object"
            },
            "weekday": {
                "description": "Allowed values are narrow, short, or long.",
                "type": "String"
            },
            "year": {
                "description": "Allowed values are numeric or 2-digit.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:formattedEmail": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "label": {
                "description": "The text label for the email.",
                "type": "String"
            },
            "onclick": {
                "description": "The action triggered when the email is clicked.",
                "type": "Action"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            },
            "value": {
                "description": "The email address that's displayed if a label is not provided.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:formattedLocation": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "latitude": {
                "description": "The latitude value of the geolocation. Latitude values must be within -90 and 90.",
                "type": "Decimal"
            },
            "longitude": {
                "description": "The longitude value of the geolocation. Longitude values must be within -180 and 180.",
                "type": "Decimal"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:formattedNumber": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "currencyCode": {
                "description": "Only used if style='currency', this attribute determines which currency is displayed. Possible values are the ISO 4217 currency codes, such as 'USD' for the US dollar.",
                "type": "String"
            },
            "currencyDisplayAs": {
                "description": "Determines how currency is displayed. Possible values are symbol, code, and name. This value defaults to symbol.",
                "type": "String"
            },
            "maximumFractionDigits": {
                "description": "The maximum number of fraction digits that are allowed.",
                "type": "Integer"
            },
            "maximumSignificantDigits": {
                "description": "The maximum number of significant digits that are allowed. Possible values are from 1 to 21.",
                "type": "Integer"
            },
            "minimumFractionDigits": {
                "description": "The minimum number of fraction digits that are required.",
                "type": "Integer"
            },
            "minimumIntegerDigits": {
                "description": "The minimum number of integer digits that are required. Possible values are from 1 to 21.",
                "type": "Integer"
            },
            "minimumSignificantDigits": {
                "description": "The minimum number of significant digits that are required. Possible values are from 1 to 21.",
                "type": "Integer"
            },
            "style": {
                "description": "The number formatting style to use. Possible values are decimal, currency, and percent. This value defaults to decimal.",
                "type": "String"
            },
            "value": {
                "description": "The value to be formatted.",
                "type": "Decimal"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:formattedPhone": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "onclick": {
                "description": "The action triggered when the phone number is clicked.",
                "type": "Action"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            },
            "value": {
                "description": "Sets the phone number to display.",
                "type": "Integer"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:formattedRichText": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            },
            "value": {
                "description": "Sets the rich text to display.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:formattedText": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "linkify": {
                "description": "Specifies whether the text should be converted to a link. If set to true, URLs and email addresses are displayed in anchor tags.",
                "type": "Boolean"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            },
            "value": {
                "description": "Text to output.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:formattedUrl": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "label": {
                "description": "The text to display in the link.",
                "type": "String"
            },
            "onclick": {
                "description": "The action triggered when the URL is clicked.",
                "type": "Action"
            },
            "target": {
                "description": "Specifies where to open the link. Options include _blank, _parent, _self, and _top.",
                "type": "String"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            },
            "tooltip": {
                "description": "The text to display when the mouse hovers over the link.",
                "type": "String"
            },
            "value": {
                "description": "The URL to be formatted.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:helptext": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "content": {
                "description": "Text to be shown in the popover.",
                "type": "String"
            },
            "iconName": {
                "description": "The Lightning Design System name of the icon used as the visible element",
                "type": "String"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:icon": {
        "attribs": {
            "alternativeText": {
                "description": "The alternative text used to describe the icon. This text should describe what happens when you click the button, for example 'Upload File', not what the icon looks like, 'Paperclip'.",
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "iconName": {
                "description": "The Lightning Design System name of the icon. Names are written in the format '\\utility:down\\' where 'utility' is the category, and 'down' is the specific icon to be displayed.",
                "type": "String"
            },
            "size": {
                "description": "The size of the icon. Options include xx-small, x-small, small, medium, or large. This value defaults to medium.",
                "type": "String"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            },
            "variant": {
                "description": "The variant changes the appearance of a utility icon. Accepted variants include inverse, warning and error. Use the inverse variant to implement a white fill in utility icons on dark backgrounds.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:input": {
        "attribs": {
            "accept": {
                "description": "Specifies the types of files that the server accepts. This attribute can be used only when type='file'.",
                "type": "String"
            },
            "accesskey": {
                "description": "Specifies a shortcut key to activate or focus an element.",
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "checked": {
                "description": "Specifies whether the checkbox is checked. This value defaults to false.",
                "type": "Boolean"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "disabled": {
                "description": "Specifies that an input element should be disabled. This value defaults to false.",
                "type": "Boolean"
            },
            "files": {
                "description": "A FileList that contains selected files. This attribute can be used only when type='file'.",
                "type": "Object"
            },
            "formatter": {
                "description": "String value with the formatter to be used.",
                "type": "String"
            },
            "isLoading": {
                "description": "Specifies whether the spinner is displayed to indicate that data is loading. This value defaults to false.",
                "type": "Boolean"
            },
            "label": {
                "description": "Text label for the input.",
                "type": "String"
            },
            "max": {
                "description": "Expected higher bound for the value in Floating-Point number",
                "type": "Decimal"
            },
            "maxlength": {
                "description": "The maximum number of characters allowed in the field.",
                "type": "Integer"
            },
            "messageToggleActive": {
                "description": "Text shown for the active state of a toggle. The default is \"Active\".",
                "type": "String"
            },
            "messageToggleInactive": {
                "description": "Text shown for then inactive state of a toggle. The default is \"Inactive\".",
                "type": "String"
            },
            "messageWhenBadInput": {
                "description": "Error message to be displayed when a bad input is detected.",
                "type": "String"
            },
            "messageWhenPatternMismatch": {
                "description": "Error message to be displayed when a pattern mismatch is detected.",
                "type": "String"
            },
            "messageWhenRangeOverflow": {
                "description": "Error message to be displayed when a range overflow is detected.",
                "type": "String"
            },
            "messageWhenRangeUnderflow": {
                "description": "Error message to be displayed when a range underflow is detected.",
                "type": "String"
            },
            "messageWhenStepMismatch": {
                "description": "Error message to be displayed when a step mismatch is detected.",
                "type": "String"
            },
            "messageWhenTooLong": {
                "description": "Error message to be displayed when the value is too long.",
                "type": "String"
            },
            "messageWhenTypeMismatch": {
                "description": "Error message to be displayed when a type mismatch is detected.",
                "type": "String"
            },
            "messageWhenValueMissing": {
                "description": "Error message to be displayed when the value is missing.",
                "type": "String"
            },
            "min": {
                "description": "Expected lower bound for the value in Floating-Point number",
                "type": "Decimal"
            },
            "minlength": {
                "description": "The minimum number of characters allowed in the field.",
                "type": "Integer"
            },
            "multiple": {
                "description": "Specifies that a user can enter more than one value. This attribute can be used only when type='file' or type='email'.",
                "type": "Boolean"
            },
            "name": {
                "description": "Specifies the name of an input element.",
                "type": "String"
            },
            "onblur": {
                "description": "The action triggered when the element releases focus.",
                "type": "Action"
            },
            "onchange": {
                "description": "The action triggered when a value attribute changes.",
                "type": "Action"
            },
            "onfocus": {
                "description": "The action triggered when the element receives focus.",
                "type": "Action"
            },
            "pattern": {
                "description": "Specifies the regular expression that the input's value is checked against. This attributed is supported for text, date, search, url, tel, email, and password types.",
                "type": "String"
            },
            "placeholder": {
                "description": "Text that is displayed when the field is empty, to prompt the user for a valid entry.",
                "type": "String"
            },
            "readonly": {
                "description": "Specifies that an input field is read-only. This value defaults to false.",
                "type": "Boolean"
            },
            "required": {
                "description": "Specifies that an input field must be filled out before submitting the form. This value defaults to false.",
                "type": "Boolean"
            },
            "step": {
                "description": "Granularity of the value in Positive Floating Point. Use 'any' when granularity is not a concern.",
                "type": "Object"
            },
            "tabindex": {
                "description": "Specifies the tab order of an element (when the tab button is used for navigating).",
                "type": "Integer"
            },
            "type": {
                "description": "The type of the input. This value defaults to text.",
                "type": "String"
            },
            "validity": {
                "description": "Represents the validity states that an element can be in, with respect to constraint validation.",
                "type": "Object"
            },
            "value": {
                "description": "Specifies the value of an input element.",
                "type": "Object"
            },
            "variant": {
                "description": "The variant changes the appearance of an input field. Accepted variants include standard and label-hidden. This value defaults to standard.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:inputLocation": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "disabled": {
                "description": "Specifies whether the compound field should be disabled. Disabled fields are grayed out and not clickable. This value defaults to false.",
                "type": "Boolean"
            },
            "label": {
                "description": "Text label for the compound field.",
                "type": "String"
            },
            "latitude": {
                "description": "The latitude value. Latitude values must be within -90 and 90.",
                "type": "String"
            },
            "longitude": {
                "description": "The longitude value. Longitude values must be within -180 and 180.",
                "type": "String"
            },
            "onblur": {
                "description": "The action triggered when the input releases focus.",
                "type": "Action"
            },
            "onchange": {
                "description": "The action triggered when the value changes.",
                "type": "Action"
            },
            "onfocus": {
                "description": "The action triggered when the input receives focus.",
                "type": "Action"
            },
            "readonly": {
                "description": "Specifies whether the compound field is read-only. This value defaults to false.",
                "type": "Boolean"
            },
            "required": {
                "description": "Specifies whether the compound field must be filled out. An error message is displayed if a user interacts with the field and does not provide a value. This value defaults to false.",
                "type": "Boolean"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            },
            "variant": {
                "description": "The variant changes the appearance of the compound field. Accepted variants include standard and label-hidden. This value defaults to standard.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:inputRichText": {
        "attribs": {
            "accesskey": {
                "description": "Specifies a shortcut key to activate or focus an element.",
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "disabled": {
                "description": "Specifies whether the editor is disabled. This value defaults to false.",
                "type": "Boolean"
            },
            "disabledCategories": {
                "description": "A comma-separated list of button categories to remove from the toolbar.",
                "type": "List"
            },
            "messageWhenBadInput": {
                "description": "Error message that's displayed when valid is false.",
                "type": "String"
            },
            "onblur": {
                "description": "The action triggered when the element releases focus.",
                "type": "Action"
            },
            "onfocus": {
                "description": "The action triggered when the element receives focus.",
                "type": "Action"
            },
            "placeholder": {
                "description": "Text that is displayed when the field is empty.",
                "type": "String"
            },
            "tabindex": {
                "description": "Specifies the tab order of an element (when the tab button is used for navigating).",
                "type": "Integer"
            },
            "valid": {
                "description": "Specifies whether the editor content is valid. If invalid, the slds-has-error class is added. This value defaults to true.",
                "type": "Boolean"
            },
            "value": {
                "description": "The HTML content in the rich text editor.",
                "type": "String"
            },
            "variant": {
                "description": "The variant changes the appearance of the toolbar. Accepted variants include bottom-toolbar.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:layout": {
        "attribs": {
            "body": {
                "description": "Body of the layout component.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class that is applied to the outer element. This style is in addition to base classes output by the component.",
                "type": "String"
            },
            "horizontalAlign": {
                "description": "Determines how to spread the layout items horizontally. The alignment options are center, space, spread, and end.",
                "type": "String"
            },
            "multipleRows": {
                "description": "Determines whether to wrap the child items when they exceed the layout width. If true, the items wrap to the following line. This value defaults to false.",
                "type": "Boolean"
            },
            "pullToBoundary": {
                "description": "Pulls layout items to the layout boundaries and corresponds to the padding size on the layout item. Possible values are small, medium, or large.",
                "type": "String"
            },
            "verticalAlign": {
                "description": "Determines how to spread the layout items vertically. The alignment options are start, center, end, and stretch.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:layoutItem": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class that will be applied to the outer element. This style is in addition to base classes output by the component.",
                "type": "String"
            },
            "flexibility": {
                "description": "Make the item fluid so that it absorbs any extra space in its container or shrinks when there is less space. Allowed values are auto, shrink, no-shrink, grow, no-grow, no-flex.",
                "type": "Object"
            },
            "largeDeviceSize": {
                "description": "If the viewport is divided into 12 parts, this attribute indicates the relative space the container occupies on device-types larger than desktop. It is expressed as an integer from 1 through 12.",
                "type": "Integer"
            },
            "mediumDeviceSize": {
                "description": "If the viewport is divided into 12 parts, this attribute indicates the relative space the container occupies on device-types larger than tablet. It is expressed as an integer from 1 through 12.",
                "type": "Integer"
            },
            "padding": {
                "description": "Sets padding to either the right and left sides of a container, or all sides of a container. Allowed values are horizontal-small, horizontal-medium, horizontal-large, around-small, around-medium, around-large.",
                "type": "String"
            },
            "size": {
                "description": "If the viewport is divided into 12 parts, size indicates the relative space the container occupies. Size is expressed as an integer from 1 through 12. This applies for all device-types.",
                "type": "Integer"
            },
            "smallDeviceSize": {
                "description": "If the viewport is divided into 12 parts, this attribute indicates the relative space the container occupies on device-types larger than mobile. It is expressed as an integer from 1 through 12.",
                "type": "Integer"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:menuItem": {
        "attribs": {
            "accesskey": {
                "description": "Specifies a shortcut key to activate or focus an element.",
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "checked": {
                "description": "If not specified, the menu item is not checkable. If true, the a check mark is shown to the left of the menu item. If false, a check mark is not shown but there is space to accommodate one.",
                "type": "Boolean"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "disabled": {
                "description": "If true the menu item is not actionable and is shown as disabled.",
                "type": "Boolean"
            },
            "iconName": {
                "description": "If provided an icon with the provided name is shown to the right of the menu item.",
                "type": "String"
            },
            "label": {
                "description": "Text of the menu item.",
                "type": "String"
            },
            "onactive": {
                "description": "DEPRECATED. The action triggered when this menu item becomes active.",
                "type": "Action"
            },
            "onblur": {
                "description": "The action triggered when the element releases focus.",
                "type": "Action"
            },
            "onfocus": {
                "description": "The action triggered when the element receives focus.",
                "type": "Action"
            },
            "tabindex": {
                "description": "Specifies the tab order of an element (when the tab button is used for navigating).",
                "type": "Integer"
            },
            "title": {
                "description": "Tooltip text.",
                "type": "String"
            },
            "value": {
                "description": "A value associated with the menu item.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:omniToolkitAPI": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:outputField": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "fieldName": {
                "description": "The API name of the field to be displayed.",
                "type": "String"
            },
            "variant": {
                "description": "Changes the appearance of the output. Accepted variants include standard and label-hidden. This value defaults to standard.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:path": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "hideUpdateButton": {
                "description": "Specified whether the Mark Complete button is displayed next to the path. If true, the button is not displayed. The Mark Complete button is displayed by default.",
                "type": "Boolean"
            },
            "onselect": {
                "description": "The action triggered when a step on the path is clicked.",
                "type": "Action"
            },
            "recordId": {
                "description": "The record's ID",
                "type": "String"
            },
            "variant": {
                "description": "Changes the appearance of the path",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:picklistPath": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "onselect": {
                "description": "The action triggered when a step on the path is clicked.",
                "type": "Action"
            },
            "picklistFieldApiName": {
                "description": "The API name of the field from which the path is derived. For example, StageName for Opportunity.",
                "type": "String"
            },
            "recordId": {
                "description": "The record's ID",
                "type": "String"
            },
            "variant": {
                "description": "Changes the appearance of the path",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:pill": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "hasError": {
                "description": "Specifies whether the pill has errors. The default is false.",
                "type": "Boolean"
            },
            "href": {
                "description": "The URL of the page that the link goes to.",
                "type": "String"
            },
            "label": {
                "description": "The text label that displays in the pill.",
                "type": "String"
            },
            "media": {
                "description": "The icon or figure that's displayed next to the textual information.",
                "type": "Component[]"
            },
            "name": {
                "description": "The name for the pill. This value is optional and can be used to identify the pill in a callback.",
                "type": "String"
            },
            "onclick": {
                "description": "The action triggered when the button is clicked.",
                "type": "Action"
            },
            "onremove": {
                "description": "The action triggered when the pill is removed.",
                "type": "Action"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:progressBar": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "size": {
                "description": "The size of the progress bar. Valid values are x-small, small, medium, and large. The default value is medium.",
                "type": "String"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            },
            "value": {
                "description": "The percentage value of the progress bar.",
                "type": "Integer"
            },
            "variant": {
                "description": "The variant of the progress bar. Valid values are base and circular.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:progressIndicator": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "currentStep": {
                "description": "The current step, which must match the value attribute of one of progressStep components. If a step is not provided, the value of the first progressStep component is used.",
                "type": "String"
            },
            "hasError": {
                "description": "Indicates whether the current step is in error state and displays a warning icon on the step indicator. Applies to the base type only. This value defaults to false.",
                "type": "Boolean"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            },
            "type": {
                "description": "Changes the visual pattern of the indicator. Valid values are base and path. This value defaults to base.",
                "type": "String"
            },
            "variant": {
                "description": "Changes the appearance of the progress indicator for the base type only",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:radioGroup": {
        "attribs": {
            "accesskey": {
                "description": "Specifies a shortcut key to activate or focus an element.",
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "disabled": {
                "description": "Specifies that an input element should be disabled. This value defaults to false.",
                "type": "Boolean"
            },
            "label": {
                "description": "Text label for the radio group.",
                "type": "String"
            },
            "messageWhenValueMissing": {
                "description": "Optional message displayed when no radio button is selected and the required attribute is set to true.",
                "type": "String"
            },
            "name": {
                "description": "Specifies the name of an input element.",
                "type": "String"
            },
            "onblur": {
                "description": "The action triggered when the element releases focus.",
                "type": "Action"
            },
            "onchange": {
                "description": "The action triggered when a value attribute changes.",
                "type": "Action"
            },
            "onfocus": {
                "description": "The action triggered when the element receives focus.",
                "type": "Action"
            },
            "options": {
                "description": "Array of label-value pairs for each radio button.",
                "type": "List"
            },
            "readonly": {
                "description": "Specifies that an input field is read-only. This value defaults to false.",
                "type": "Boolean"
            },
            "required": {
                "description": "Specifies that an input field must be filled out before submitting the form. This value defaults to false.",
                "type": "Boolean"
            },
            "tabindex": {
                "description": "Specifies the tab order of an element (when the tab button is used for navigating).",
                "type": "Integer"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            },
            "type": {
                "description": "The style of the radio group. Options are radio or button. The default is radio.",
                "type": "String"
            },
            "validity": {
                "description": "Represents the validity states that an element can be in, with respect to constraint validation.",
                "type": "Object"
            },
            "value": {
                "description": "Specifies the value of an input element.",
                "type": "Object"
            },
            "variant": {
                "description": "The variant changes the appearance of an input field. Accepted variants include standard and label-hidden. This value defaults to standard.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:recordViewForm": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "objectApiName": {
                "description": "The API name of the object.",
                "type": "String"
            },
            "recordId": {
                "description": "The ID of the record to be displayed.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:relativeDateTime": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "value": {
                "description": "The timestamp or JavaScript Date object to be formatted.",
                "type": "Object"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:select": {
        "attribs": {
            "accesskey": {
                "description": "Specifies a shortcut key to activate or focus an element.",
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class that will be applied to the outer element. This style is in addition to base classes associated with the component.",
                "type": "String"
            },
            "disabled": {
                "description": "Specifies that an input element should be disabled. This value defaults to false.",
                "type": "Boolean"
            },
            "label": {
                "description": "Text that describes the desired select input.",
                "type": "String"
            },
            "messageWhenValueMissing": {
                "description": "Error message to be displayed when the value is missing.",
                "type": "String"
            },
            "name": {
                "description": "Specifies the name of an input element.",
                "type": "String"
            },
            "onblur": {
                "description": "The action triggered when the element releases focus.",
                "type": "Action"
            },
            "onchange": {
                "description": "The action triggered when a value attribute changes.",
                "type": "Action"
            },
            "onfocus": {
                "description": "The action triggered when the element receives focus.",
                "type": "Action"
            },
            "readonly": {
                "description": "Specifies that an input field is read-only. This value defaults to false.",
                "type": "Boolean"
            },
            "required": {
                "description": "Specifies that an input field must be filled out before submitting the form. This value defaults to false.",
                "type": "Boolean"
            },
            "tabindex": {
                "description": "Specifies the tab order of an element (when the tab button is used for navigating).",
                "type": "Integer"
            },
            "validity": {
                "description": "Represents the validity states that an element can be in, with respect to constraint validation.",
                "type": "Object"
            },
            "value": {
                "description": "The value of the select, also used as the default value to select the right option during init. If no value is provided, the first option will be selected.",
                "type": "String"
            },
            "variant": {
                "description": "The variant changes the appearance of an input field. Accepted variants include standard and label-hidden. This value defaults to standard.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:slider": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "disabled": {
                "description": "The disabled value of the input range. This value default to false.",
                "type": "Boolean"
            },
            "label": {
                "description": "The text label for the input range. Provide your own label to describe the slider. Otherwise, no label is displayed.",
                "type": "String"
            },
            "max": {
                "description": "The max value of the input range. This value defaults to 100.",
                "type": "Integer"
            },
            "messageWhenBadInput": {
                "description": "Error message to be displayed when a bad input is detected. Use with setCustomValidity.",
                "type": "String"
            },
            "messageWhenPatternMismatch": {
                "description": "Error message to be displayed when a pattern mismatch is detected. Use with setCustomValidity.",
                "type": "String"
            },
            "messageWhenRangeOverflow": {
                "description": "Error message to be displayed when a range overflow is detected. Use with setCustomValidity.",
                "type": "String"
            },
            "messageWhenRangeUnderflow": {
                "description": "Error message to be displayed when a range underflow is detected. Use with setCustomValidity.",
                "type": "String"
            },
            "messageWhenStepMismatch": {
                "description": "Error message to be displayed when a step mismatch is detected. Use with setCustomValidity.",
                "type": "String"
            },
            "messageWhenTooLong": {
                "description": "Error message to be displayed when the value is too long. Use with setCustomValidity.",
                "type": "String"
            },
            "messageWhenTypeMismatch": {
                "description": "Error message to be displayed when a type mismatch is detected. Use with setCustomValidity.",
                "type": "String"
            },
            "messageWhenValueMissing": {
                "description": "Error message to be displayed when the value is missing. Use with setCustomValidity.",
                "type": "String"
            },
            "min": {
                "description": "The min value of the input range. This value defaults to 0.",
                "type": "Integer"
            },
            "onblur": {
                "description": "The action triggered when the slider releases focus.",
                "type": "Action"
            },
            "onchange": {
                "description": "The action triggered when the slider value changes. You must pass any newly selected value back to the slider component to bind the new value to the slider.",
                "type": "String"
            },
            "onfocus": {
                "description": "The action triggered when the slider receives focus.",
                "type": "Action"
            },
            "size": {
                "description": "The size value of the input range. This value default to empty, which is the base. Supports x-small, small, medium, and large.",
                "type": "String"
            },
            "step": {
                "description": "The step increment value of the input range. Example steps include 0.1, 1, or 10. This value defaults to 1.",
                "type": "String"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            },
            "type": {
                "description": "The type of the input range position. This value defaults to horizontal.",
                "type": "String"
            },
            "value": {
                "description": "The numerical value of the input range. This value defaults to 0.",
                "type": "Integer"
            },
            "variant": {
                "description": "The variant changes the appearance of the slider. Accepted variants include standard and label-hidden. This value defaults to standard.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:spinner": {
        "attribs": {
            "alternativeText": {
                "description": "The alternative text used to describe the reason for the wait and need for a spinner.",
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "size": {
                "description": "The size of the spinner. Accepted sizes are small, medium, and large. This value defaults to medium.",
                "type": "String"
            },
            "variant": {
                "description": "The variant changes the appearance of the spinner. Accepted variants are brand and inverse.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:tab": {
        "attribs": {
            "accesskey": {
                "description": "Specifies a shortcut key to activate or focus an element.",
                "type": "String"
            },
            "body": {
                "description": "The body of the tab.",
                "type": "ComponentDefRef[]"
            },
            "id": {
                "description": "The optional ID is used during tabset's onSelect event to determine which tab was clicked.",
                "type": "String"
            },
            "label": {
                "description": "The text that appears in the tab.",
                "type": "Component[]"
            },
            "onactive": {
                "description": "The action triggered when this tab becomes active.",
                "type": "Action"
            },
            "onblur": {
                "description": "The action triggered when the element releases focus.",
                "type": "Action"
            },
            "onfocus": {
                "description": "The action triggered when the element receives focus.",
                "type": "Action"
            },
            "tabindex": {
                "description": "Specifies the tab order of an element (when the tab button is used for navigating).",
                "type": "Integer"
            },
            "title": {
                "description": "The title displays when you hover over the tab. The title should describe the content of the tab for screen readers.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:tabSet": {
        "attribs": {
            "body": {
                "description": "The body of the component. This could be one or more lightning:tab components.",
                "type": "ComponentDefRef[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "onselect": {
                "description": "The action that will run when the tab is clicked.",
                "type": "Action"
            },
            "selectedTabId": {
                "description": "Allows you to set a specific tab to open by default. If this attribute is not used, the first tab opens by default.",
                "type": "String"
            },
            "variant": {
                "description": "The variant changes the appearance of the tabset. Accepted variants are default and scoped.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:textarea": {
        "attribs": {
            "accesskey": {
                "description": "Specifies a shortcut key to activate or focus an element.",
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class that will be applied to the outer element. This style is in addition to base classes associated with the component.",
                "type": "String"
            },
            "disabled": {
                "description": "Specifies that an input element should be disabled. This value defaults to false.",
                "type": "Boolean"
            },
            "label": {
                "description": "Text that describes the desired textarea input.",
                "type": "String"
            },
            "maxlength": {
                "description": "The maximum number of characters allowed in the textarea.",
                "type": "Integer"
            },
            "messageWhenBadInput": {
                "description": "Error message to be displayed when a bad input is detected.",
                "type": "String"
            },
            "messageWhenTooLong": {
                "description": "Error message to be displayed when the value is too long.",
                "type": "String"
            },
            "messageWhenValueMissing": {
                "description": "Error message to be displayed when the value is missing.",
                "type": "String"
            },
            "minlength": {
                "description": "The minimum number of characters allowed in the textarea.",
                "type": "Integer"
            },
            "name": {
                "description": "Specifies the name of an input element.",
                "type": "String"
            },
            "onblur": {
                "description": "The action triggered when the element releases focus.",
                "type": "Action"
            },
            "onchange": {
                "description": "The action triggered when a value attribute changes.",
                "type": "Action"
            },
            "onfocus": {
                "description": "The action triggered when the element receives focus.",
                "type": "Action"
            },
            "placeholder": {
                "description": "Text that is displayed when the field is empty, to prompt the user for a valid entry.",
                "type": "String"
            },
            "readonly": {
                "description": "Specifies that an input field is read-only. This value defaults to false.",
                "type": "Boolean"
            },
            "required": {
                "description": "Specifies that an input field must be filled out before submitting the form. This value defaults to false.",
                "type": "Boolean"
            },
            "tabindex": {
                "description": "Specifies the tab order of an element (when the tab button is used for navigating).",
                "type": "Integer"
            },
            "validity": {
                "description": "Represents the validity states that an element can be in, with respect to constraint validation.",
                "type": "Object"
            },
            "value": {
                "description": "The value of the textarea, also used as the default value during init.",
                "type": "String"
            },
            "variant": {
                "description": "The variant changes the appearance of an input field. Accepted variants include standard and label-hidden. This value defaults to standard.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:tile": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class that will be applied to the outer element. This style is in addition to base classes associated with the component.",
                "type": "String"
            },
            "href": {
                "description": "The URL of the page that the link goes to.",
                "type": "String"
            },
            "label": {
                "description": "The text label that displays in the tile and hover text.",
                "type": "String"
            },
            "media": {
                "description": "The icon or figure that's displayed next to the textual information.",
                "type": "Component[]"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:tree": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "header": {
                "description": "The text that's displayed as the tree heading.",
                "type": "String"
            },
            "items": {
                "description": "An array of key-value pairs that describe the tree. Keys include label, name, disabled, expanded, and items.",
                "type": "Object"
            },
            "onselect": {
                "description": "The action triggered when a tree item is selected.",
                "type": "Action"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:utilityBarAPI": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:verticalNavigation": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "compact": {
                "description": "Specify true to reduce spacing between navigation items. This value defaults to false.",
                "type": "Boolean"
            },
            "onbeforeselect": {
                "description": "Action fired before an item is selected",
                "type": "Action"
            },
            "onselect": {
                "description": "Action fired when an item is selected. The event params include the `name` of the selected item.",
                "type": "Action"
            },
            "selectedItem": {
                "description": "Name of the nagivation item to make active.",
                "type": "String"
            },
            "shaded": {
                "description": "Specify true when the vertical navigation is sitting on top of a shaded background. This value defaults to false.",
                "type": "Boolean"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:verticalNavigationItem": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "href": {
                "description": "The URL of the page that the navigation item goes to.",
                "type": "String"
            },
            "label": {
                "description": "The text displayed for the navigation item.",
                "type": "String"
            },
            "name": {
                "description": "A unique identifier for the navigation item.",
                "type": "String"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:verticalNavigationItemBadge": {
        "attribs": {
            "assistiveText": {
                "description": "Assistive text describing the number in the badge. This is used to enhance accessibility and is not displayed to the user.",
                "type": "String"
            },
            "badgeCount": {
                "description": "The number to show inside the badge. If this value is zero the badge will be hidden.",
                "type": "Integer"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "href": {
                "description": "The URL of the page that the navigation item goes to.",
                "type": "String"
            },
            "label": {
                "description": "The text displayed for this navigation item.",
                "type": "String"
            },
            "name": {
                "description": "A unique identifier for this navigation item.",
                "type": "String"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:verticalNavigationItemIcon": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "type": "String"
            },
            "href": {
                "description": "The URL of the page that the navigation item goes to.",
                "type": "String"
            },
            "iconName": {
                "description": "The Lightning Design System name of the icon. Names are written in the format '\\utility:down\\' where 'utility' is the category, and 'down' is the specific icon to be displayed.",
                "type": "String"
            },
            "label": {
                "description": "The text displayed for this navigation item.",
                "type": "String"
            },
            "name": {
                "description": "A unique identifier for this navigation item.",
                "type": "String"
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:verticalNavigationOverflow": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:verticalNavigationSection": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "label": {
                "description": "The heading text for this section.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:workspaceAPI": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ltng:require": {
        "attribs": {
            "afterScriptsLoaded": {
                "description": "Fired when ltng:require has loaded all scripts listed in ltng:require.scripts",
                "type": "COMPONENT"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "scripts": {
                "description": "The set of scripts in dependency order that will be loaded.",
                "type": "String[]"
            },
            "styles": {
                "description": "The set of style sheets in dependency order that will be loaded.",
                "type": "String[]"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:actionMenuItem": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "blur": {
                "description": "Indicates that a component has been put out of focus.",
                "type": "COMPONENT"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "disabled": {
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is 'false'.",
                "type": "Boolean"
            },
            "focus": {
                "description": "Indicates that a component has been put on focus.",
                "type": "COMPONENT"
            },
            "hideMenuAfterSelected": {
                "description": "Set to true to hide menu after the menu item is selected.",
                "type": "Boolean"
            },
            "keydown": {
                "description": "Indicates that the user has pressed and released a keyboard key.",
                "type": "COMPONENT"
            },
            "keypress": {
                "description": "Indicates that the user has pressed and held down a keyboard key.",
                "type": "COMPONENT"
            },
            "keyup": {
                "description": "Indicates that the user has released a keyboard key.",
                "type": "COMPONENT"
            },
            "label": {
                "description": "The text displayed on the component.",
                "type": "String"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "select": {
                "description": "Indicates that the user has made a selection.",
                "type": "COMPONENT"
            },
            "selected": {
                "description": "The status of the menu item. True means this menu item is selected; False is not selected.",
                "type": "Boolean"
            },
            "type": {
                "description": "The concrete type of the menu item. Accepted values are 'action', 'checkbox', 'radio', 'separator' or any namespaced,component descriptor, e.g. ns:xxxxmenuItem.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:button": {
        "attribs": {
            "accesskey": {
                "description": "The keyboard access key that puts the button in focus. When the button is in focus, pressing Enter clicks the button.",
                "type": "String"
            },
            "aura:id": {
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "buttonTitle": {
                "description": "The text displayed in a tooltip when the mouse pointer hovers over the button.",
                "type": "String"
            },
            "buttonType": {
                "description": "Specifies the type attribute in the HTML input element. Default value is button.",
                "type": "String"
            },
            "class": {
                "description": "A CSS style to be attached to the button. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "disabled": {
                "description": "Specifies whether this button should be displayed in a disabled state. Disabled buttons can't be clicked. Default value is 'false'.",
                "type": "Boolean"
            },
            "label": {
                "description": "The text displayed on the button. Corresponds to the value attribute of the rendered HTML input element.",
                "type": "String"
            },
            "labelClass": {
                "description": "A CSS style to be attached to the label. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "press": {
                "description": "Indicates that the component has been pressed.",
                "type": "COMPONENT"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:checkboxMenuItem": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "blur": {
                "description": "Indicates that a component has been put out of focus.",
                "type": "COMPONENT"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "disabled": {
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is 'false'.",
                "type": "Boolean"
            },
            "focus": {
                "description": "Indicates that a component has been put on focus.",
                "type": "COMPONENT"
            },
            "hideMenuAfterSelected": {
                "description": "Set to true to hide menu after the menu item is selected.",
                "type": "Boolean"
            },
            "keydown": {
                "description": "Indicates that the user has pressed and released a keyboard key.",
                "type": "COMPONENT"
            },
            "keypress": {
                "description": "Indicates that the user has pressed and held down a keyboard key.",
                "type": "COMPONENT"
            },
            "keyup": {
                "description": "Indicates that the user has released a keyboard key.",
                "type": "COMPONENT"
            },
            "label": {
                "description": "The text displayed on the component.",
                "type": "String"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "select": {
                "description": "Indicates that the user has made a selection.",
                "type": "COMPONENT"
            },
            "selected": {
                "description": "The status of the menu item. True means this menu item is selected; False is not selected.",
                "type": "Boolean"
            },
            "type": {
                "description": "The concrete type of the menu item. Accepted values are 'action', 'checkbox', 'radio', 'separator' or any namespaced component descriptor, e.g. ns:xxxxmenuItem.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:inputCheckbox": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "blur": {
                "description": "Indicates that a component has been put out of focus.",
                "type": "COMPONENT"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "change": {
                "description": "Indicates that the content of a component or the state has changed.",
                "type": "COMPONENT"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "clearErrors": {
                "description": "Indicates that any validation error should be cleared.",
                "type": "COMPONENT"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "copy": {
                "description": "Indicates that the user has copied content to the clipboard.",
                "type": "COMPONENT"
            },
            "cut": {
                "description": "Indicates that the user has cut content to the clipboard.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "disabled": {
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is 'false'.",
                "type": "Boolean"
            },
            "focus": {
                "description": "Indicates that a component has been put on focus.",
                "type": "COMPONENT"
            },
            "keydown": {
                "description": "Indicates that the user has pressed and released a keyboard key.",
                "type": "COMPONENT"
            },
            "keypress": {
                "description": "Indicates that the user has pressed and held down a keyboard key.",
                "type": "COMPONENT"
            },
            "keyup": {
                "description": "Indicates that the user has released a keyboard key.",
                "type": "COMPONENT"
            },
            "label": {
                "description": "The text displayed on the component.",
                "type": "String"
            },
            "labelClass": {
                "description": "The CSS class of the label component",
                "type": "String"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "name": {
                "description": "The name of the component.",
                "type": "String"
            },
            "paste": {
                "description": "Indicates that the user has pasted content from the clipboard.",
                "type": "COMPONENT"
            },
            "required": {
                "description": "Specifies whether the input is required. Default value is 'false'.",
                "type": "Boolean"
            },
            "requiredIndicatorClass": {
                "description": "The CSS class of the required indicator component",
                "type": "String"
            },
            "select": {
                "description": "Indicates that the user has made a selection.",
                "type": "COMPONENT"
            },
            "text": {
                "description": "The input value attribute.",
                "type": "String"
            },
            "updateOn": {
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is 'change,click'.",
                "type": "String"
            },
            "validationError": {
                "description": "Indicates that the component has validation error(s).",
                "type": "COMPONENT"
            },
            "value": {
                "description": "Indicates whether the status of the option is selected. Default value is 'false'.",
                "type": "Boolean"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:inputCurrency": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "blur": {
                "description": "Indicates that a component has been put out of focus.",
                "type": "COMPONENT"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "change": {
                "description": "Indicates that the content of a component or the state has changed.",
                "type": "COMPONENT"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "clearErrors": {
                "description": "Indicates that any validation error should be cleared.",
                "type": "COMPONENT"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "copy": {
                "description": "Indicates that the user has copied content to the clipboard.",
                "type": "COMPONENT"
            },
            "cut": {
                "description": "Indicates that the user has cut content to the clipboard.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "disabled": {
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false.",
                "type": "Boolean"
            },
            "focus": {
                "description": "Indicates that a component has been put on focus.",
                "type": "COMPONENT"
            },
            "format": {
                "description": "The format of the number. For example, format='.00' displays the number followed by two decimal places. If not specified, the Locale default format will be used.",
                "type": "String"
            },
            "keydown": {
                "description": "Indicates that the user has pressed and released a keyboard key.",
                "type": "COMPONENT"
            },
            "keypress": {
                "description": "Indicates that the user has pressed and held down a keyboard key.",
                "type": "COMPONENT"
            },
            "keyup": {
                "description": "Indicates that the user has released a keyboard key.",
                "type": "COMPONENT"
            },
            "label": {
                "description": "The text of the label component",
                "type": "String"
            },
            "labelClass": {
                "description": "The CSS class of the label component",
                "type": "String"
            },
            "maxlength": {
                "description": "The maximum number of characters that can be typed into the input field. Corresponds to the maxlength attribute of the rendered HTML input element.",
                "type": "Integer"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "paste": {
                "description": "Indicates that the user has pasted content from the clipboard.",
                "type": "COMPONENT"
            },
            "placeholder": {
                "description": "Text that is displayed when the field is empty, to prompt the user for a valid entry.",
                "type": "String"
            },
            "required": {
                "description": "Specifies whether the input is required. Default value is false.",
                "type": "Boolean"
            },
            "requiredIndicatorClass": {
                "description": "The CSS class of the required indicator component",
                "type": "String"
            },
            "select": {
                "description": "Indicates that the user has made a selection.",
                "type": "COMPONENT"
            },
            "size": {
                "description": "The width of the input field, in characters. Corresponds to the size attribute of the rendered HTML input element.",
                "type": "Integer"
            },
            "updateOn": {
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is change.",
                "type": "String"
            },
            "validationError": {
                "description": "Indicates that the component has validation error(s).",
                "type": "COMPONENT"
            },
            "value": {
                "description": "The input value of the number.",
                "type": "BigDecimal"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:inputDate": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "blur": {
                "description": "Indicates that a component has been put out of focus.",
                "type": "COMPONENT"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "change": {
                "description": "Indicates that the content of a component or the state has changed.",
                "type": "COMPONENT"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "clearErrors": {
                "description": "Indicates that any validation error should be cleared.",
                "type": "COMPONENT"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "copy": {
                "description": "Indicates that the user has copied content to the clipboard.",
                "type": "COMPONENT"
            },
            "cut": {
                "description": "Indicates that the user has cut content to the clipboard.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "disabled": {
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false.",
                "type": "Boolean"
            },
            "displayDatePicker": {
                "description": "Indicate if ui:datePicker is displayed.",
                "type": "Boolean"
            },
            "focus": {
                "description": "Indicates that a component has been put on focus.",
                "type": "COMPONENT"
            },
            "format": {
                "description": "The java.text.SimpleDateFormat style format string.",
                "type": "String"
            },
            "keydown": {
                "description": "Indicates that the user has pressed and released a keyboard key.",
                "type": "COMPONENT"
            },
            "keypress": {
                "description": "Indicates that the user has pressed and held down a keyboard key.",
                "type": "COMPONENT"
            },
            "keyup": {
                "description": "Indicates that the user has released a keyboard key.",
                "type": "COMPONENT"
            },
            "label": {
                "description": "The text of the label component",
                "type": "String"
            },
            "labelClass": {
                "description": "The CSS class of the label component",
                "type": "String"
            },
            "langLocale": {
                "description": "The language locale used to format date time.",
                "type": "String"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "paste": {
                "description": "Indicates that the user has pasted content from the clipboard.",
                "type": "COMPONENT"
            },
            "required": {
                "description": "Specifies whether the input is required. Default value is false.",
                "type": "Boolean"
            },
            "requiredIndicatorClass": {
                "description": "The CSS class of the required indicator component",
                "type": "String"
            },
            "select": {
                "description": "Indicates that the user has made a selection.",
                "type": "COMPONENT"
            },
            "updateOn": {
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is 'change'.",
                "type": "String"
            },
            "validationError": {
                "description": "Indicates that the component has validation error(s).",
                "type": "COMPONENT"
            },
            "value": {
                "description": "The input value of the date/time.",
                "type": "Date"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:inputDateTime": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "blur": {
                "description": "Indicates that a component has been put out of focus.",
                "type": "COMPONENT"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "change": {
                "description": "Indicates that the content of a component or the state has changed.",
                "type": "COMPONENT"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "clearErrors": {
                "description": "Indicates that any validation error should be cleared.",
                "type": "COMPONENT"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "copy": {
                "description": "Indicates that the user has copied content to the clipboard.",
                "type": "COMPONENT"
            },
            "cut": {
                "description": "Indicates that the user has cut content to the clipboard.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "disabled": {
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is 'false'.",
                "type": "Boolean"
            },
            "displayDatePicker": {
                "description": "Indicate if ui:datePicker is displayed.",
                "type": "Boolean"
            },
            "focus": {
                "description": "Indicates that a component has been put on focus.",
                "type": "COMPONENT"
            },
            "format": {
                "description": "The java.text.SimpleDateFormat style format string.",
                "type": "String"
            },
            "keydown": {
                "description": "Indicates that the user has pressed and released a keyboard key.",
                "type": "COMPONENT"
            },
            "keypress": {
                "description": "Indicates that the user has pressed and held down a keyboard key.",
                "type": "COMPONENT"
            },
            "keyup": {
                "description": "Indicates that the user has released a keyboard key.",
                "type": "COMPONENT"
            },
            "label": {
                "description": "The text of the label component",
                "type": "String"
            },
            "labelClass": {
                "description": "The CSS class of the label component",
                "type": "String"
            },
            "langLocale": {
                "description": "The language locale used to format date time.",
                "type": "String"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "paste": {
                "description": "Indicates that the user has pasted content from the clipboard.",
                "type": "COMPONENT"
            },
            "required": {
                "description": "Specifies whether the input is required. Default value is 'false'.",
                "type": "Boolean"
            },
            "requiredIndicatorClass": {
                "description": "The CSS class of the required indicator component",
                "type": "String"
            },
            "select": {
                "description": "Indicates that the user has made a selection.",
                "type": "COMPONENT"
            },
            "updateOn": {
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is 'change'.",
                "type": "String"
            },
            "validationError": {
                "description": "Indicates that the component has validation error(s).",
                "type": "COMPONENT"
            },
            "value": {
                "description": "The input value of the date/time.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:inputDefaultError": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "value": {
                "description": "The list of errors strings to be displayed.",
                "type": "ArrayList"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:inputEmail": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "blur": {
                "description": "Indicates that a component has been put out of focus.",
                "type": "COMPONENT"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "change": {
                "description": "Indicates that the content of a component or the state has changed.",
                "type": "COMPONENT"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "clearErrors": {
                "description": "Indicates that any validation error should be cleared.",
                "type": "COMPONENT"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "copy": {
                "description": "Indicates that the user has copied content to the clipboard.",
                "type": "COMPONENT"
            },
            "cut": {
                "description": "Indicates that the user has cut content to the clipboard.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "disabled": {
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is 'false'.",
                "type": "Boolean"
            },
            "focus": {
                "description": "Indicates that a component has been put on focus.",
                "type": "COMPONENT"
            },
            "keydown": {
                "description": "Indicates that the user has pressed and released a keyboard key.",
                "type": "COMPONENT"
            },
            "keypress": {
                "description": "Indicates that the user has pressed and held down a keyboard key.",
                "type": "COMPONENT"
            },
            "keyup": {
                "description": "Indicates that the user has released a keyboard key.",
                "type": "COMPONENT"
            },
            "label": {
                "description": "The text of the label component",
                "type": "String"
            },
            "labelClass": {
                "description": "The CSS class of the label component",
                "type": "String"
            },
            "maxlength": {
                "description": "The maximum number of characters that can be typed into the input field. Corresponds to the maxlength attribute of the rendered HTML input element.",
                "type": "Integer"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "paste": {
                "description": "Indicates that the user has pasted content from the clipboard.",
                "type": "COMPONENT"
            },
            "placeholder": {
                "description": "Text that is displayed when the field is empty, to prompt the user for a valid entry.",
                "type": "String"
            },
            "required": {
                "description": "Specifies whether the input is required. Default value is 'false'.",
                "type": "Boolean"
            },
            "requiredIndicatorClass": {
                "description": "The CSS class of the required indicator component",
                "type": "String"
            },
            "select": {
                "description": "Indicates that the user has made a selection.",
                "type": "COMPONENT"
            },
            "size": {
                "description": "The width of the input field, in characters. Corresponds to the size attribute of the rendered HTML input element.",
                "type": "Integer"
            },
            "updateOn": {
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is 'change'.",
                "type": "String"
            },
            "validationError": {
                "description": "Indicates that the component has validation error(s).",
                "type": "COMPONENT"
            },
            "value": {
                "description": "The value currently in the input field.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:inputNumber": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "blur": {
                "description": "Indicates that a component has been put out of focus.",
                "type": "COMPONENT"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "change": {
                "description": "Indicates that the content of a component or the state has changed.",
                "type": "COMPONENT"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "clearErrors": {
                "description": "Indicates that any validation error should be cleared.",
                "type": "COMPONENT"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "copy": {
                "description": "Indicates that the user has copied content to the clipboard.",
                "type": "COMPONENT"
            },
            "cut": {
                "description": "Indicates that the user has cut content to the clipboard.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "disabled": {
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is 'false'.",
                "type": "Boolean"
            },
            "focus": {
                "description": "Indicates that a component has been put on focus.",
                "type": "COMPONENT"
            },
            "format": {
                "description": "The format of the number. For example, format=\u00a1\u00b0.00\u00a1\u00b1 displays the number followed by two decimal places. If not specified, the Locale default format will be used.",
                "type": "String"
            },
            "keydown": {
                "description": "Indicates that the user has pressed and released a keyboard key.",
                "type": "COMPONENT"
            },
            "keypress": {
                "description": "Indicates that the user has pressed and held down a keyboard key.",
                "type": "COMPONENT"
            },
            "keyup": {
                "description": "Indicates that the user has released a keyboard key.",
                "type": "COMPONENT"
            },
            "label": {
                "description": "The text of the label component",
                "type": "String"
            },
            "labelClass": {
                "description": "The CSS class of the label component",
                "type": "String"
            },
            "maxlength": {
                "description": "The maximum number of characters that can be typed into the input field. Corresponds to the maxlength attribute of the rendered HTML input element.",
                "type": "Integer"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "paste": {
                "description": "Indicates that the user has pasted content from the clipboard.",
                "type": "COMPONENT"
            },
            "placeholder": {
                "description": "Text that is displayed when the field is empty, to prompt the user for a valid entry.",
                "type": "String"
            },
            "required": {
                "description": "Specifies whether the input is required. Default value is 'false'.",
                "type": "Boolean"
            },
            "requiredIndicatorClass": {
                "description": "The CSS class of the required indicator component",
                "type": "String"
            },
            "select": {
                "description": "Indicates that the user has made a selection.",
                "type": "COMPONENT"
            },
            "size": {
                "description": "The width of the input field, in characters. Corresponds to the size attribute of the rendered HTML input element.",
                "type": "Integer"
            },
            "updateOn": {
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is 'change'.",
                "type": "String"
            },
            "validationError": {
                "description": "Indicates that the component has validation error(s).",
                "type": "COMPONENT"
            },
            "value": {
                "description": "The input value of the number.",
                "type": "BigDecimal"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:inputPhone": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "blur": {
                "description": "Indicates that a component has been put out of focus.",
                "type": "COMPONENT"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "change": {
                "description": "Indicates that the content of a component or the state has changed.",
                "type": "COMPONENT"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "clearErrors": {
                "description": "Indicates that any validation error should be cleared.",
                "type": "COMPONENT"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "copy": {
                "description": "Indicates that the user has copied content to the clipboard.",
                "type": "COMPONENT"
            },
            "cut": {
                "description": "Indicates that the user has cut content to the clipboard.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "disabled": {
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is 'false'.",
                "type": "Boolean"
            },
            "focus": {
                "description": "Indicates that a component has been put on focus.",
                "type": "COMPONENT"
            },
            "keydown": {
                "description": "Indicates that the user has pressed and released a keyboard key.",
                "type": "COMPONENT"
            },
            "keypress": {
                "description": "Indicates that the user has pressed and held down a keyboard key.",
                "type": "COMPONENT"
            },
            "keyup": {
                "description": "Indicates that the user has released a keyboard key.",
                "type": "COMPONENT"
            },
            "label": {
                "description": "The text of the label component",
                "type": "String"
            },
            "labelClass": {
                "description": "The CSS class of the label component",
                "type": "String"
            },
            "maxlength": {
                "description": "The maximum number of characters that can be typed into the input field. Corresponds to the maxlength attribute of the rendered HTML input element.",
                "type": "Integer"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "paste": {
                "description": "Indicates that the user has pasted content from the clipboard.",
                "type": "COMPONENT"
            },
            "placeholder": {
                "description": "Text that is displayed when the field is empty, to prompt the user for a valid entry.",
                "type": "String"
            },
            "required": {
                "description": "Specifies whether the input is required. Default value is 'false'.",
                "type": "Boolean"
            },
            "requiredIndicatorClass": {
                "description": "The CSS class of the required indicator component",
                "type": "String"
            },
            "select": {
                "description": "Indicates that the user has made a selection.",
                "type": "COMPONENT"
            },
            "size": {
                "description": "The width of the input field, in characters. Corresponds to the size attribute of the rendered HTML input element.",
                "type": "Integer"
            },
            "updateOn": {
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is 'change'.",
                "type": "String"
            },
            "validationError": {
                "description": "Indicates that the component has validation error(s).",
                "type": "COMPONENT"
            },
            "value": {
                "description": "The value currently in the input field.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:inputRadio": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "blur": {
                "description": "Indicates that a component has been put out of focus.",
                "type": "COMPONENT"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "change": {
                "description": "Indicates that the content of a component or the state has changed.",
                "type": "COMPONENT"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "clearErrors": {
                "description": "Indicates that any validation error should be cleared.",
                "type": "COMPONENT"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "copy": {
                "description": "Indicates that the user has copied content to the clipboard.",
                "type": "COMPONENT"
            },
            "cut": {
                "description": "Indicates that the user has cut content to the clipboard.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "disabled": {
                "description": "Specifies whether this radio button should be displayed in a disabled state. Disabled radio buttons can't be clicked. Default value is false.",
                "type": "Boolean"
            },
            "focus": {
                "description": "Indicates that a component has been put on focus.",
                "type": "COMPONENT"
            },
            "keydown": {
                "description": "Indicates that the user has pressed and released a keyboard key.",
                "type": "COMPONENT"
            },
            "keypress": {
                "description": "Indicates that the user has pressed and held down a keyboard key.",
                "type": "COMPONENT"
            },
            "keyup": {
                "description": "Indicates that the user has released a keyboard key.",
                "type": "COMPONENT"
            },
            "label": {
                "description": "The text displayed on the component.",
                "type": "String"
            },
            "labelClass": {
                "description": "The CSS class of the label component",
                "type": "String"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "name": {
                "description": "The name of the component.",
                "type": "String"
            },
            "paste": {
                "description": "Indicates that the user has pasted content from the clipboard.",
                "type": "COMPONENT"
            },
            "required": {
                "description": "Specifies whether the input is required. Default value is false.",
                "type": "Boolean"
            },
            "requiredIndicatorClass": {
                "description": "The CSS class of the required indicator component",
                "type": "String"
            },
            "select": {
                "description": "Indicates that the user has made a selection.",
                "type": "COMPONENT"
            },
            "text": {
                "description": "The input value attribute.",
                "type": "String"
            },
            "updateOn": {
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is change.",
                "type": "String"
            },
            "validationError": {
                "description": "Indicates that the component has validation error(s).",
                "type": "COMPONENT"
            },
            "value": {
                "description": "Indicates whether the status of the option is selected. Default value is false.",
                "type": "Boolean"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:inputRichText": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "blur": {
                "description": "Indicates that a component has been put out of focus.",
                "type": "COMPONENT"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "change": {
                "description": "Indicates that the content of a component or the state has changed.",
                "type": "COMPONENT"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "clearErrors": {
                "description": "Indicates that any validation error should be cleared.",
                "type": "COMPONENT"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "cols": {
                "description": "The width of the text area, which is defined by the number of characters to display in a single row at a time. Default value is \u00a1\u00b020\u00a1\u00b1.",
                "type": "Integer"
            },
            "copy": {
                "description": "Indicates that the user has copied content to the clipboard.",
                "type": "COMPONENT"
            },
            "cut": {
                "description": "Indicates that the user has cut content to the clipboard.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "disabled": {
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false.",
                "type": "Boolean"
            },
            "focus": {
                "description": "Indicates that a component has been put on focus.",
                "type": "COMPONENT"
            },
            "height": {
                "description": "The height of the editing area (that includes the editor content). This can be an integer, for pixel sizes, or any CSS-defined length unit.",
                "type": "String"
            },
            "keydown": {
                "description": "Indicates that the user has pressed and released a keyboard key.",
                "type": "COMPONENT"
            },
            "keypress": {
                "description": "Indicates that the user has pressed and held down a keyboard key.",
                "type": "COMPONENT"
            },
            "keyup": {
                "description": "Indicates that the user has released a keyboard key.",
                "type": "COMPONENT"
            },
            "label": {
                "description": "The text of the label component",
                "type": "String"
            },
            "labelClass": {
                "description": "The CSS class of the label component",
                "type": "String"
            },
            "maxlength": {
                "description": "The maximum number of characters that can be typed into the input field. Corresponds to the maxlength attribute of the rendered HTML textarea element.",
                "type": "Integer"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "paste": {
                "description": "Indicates that the user has pasted content from the clipboard.",
                "type": "COMPONENT"
            },
            "placeholder": {
                "description": "The text that is displayed by default.",
                "type": "String"
            },
            "readonly": {
                "description": "Specifies whether the text area should be rendered as read-only. Default value is \u00a1\u00b0false\u00a1\u00b1.",
                "type": "Boolean"
            },
            "required": {
                "description": "Specifies whether the input is required. Default value is false.",
                "type": "Boolean"
            },
            "requiredIndicatorClass": {
                "description": "The CSS class of the required indicator component",
                "type": "String"
            },
            "resizable": {
                "description": "Specifies whether or not the textarea should be resizable. Defaults to true.",
                "type": "Boolean"
            },
            "rows": {
                "description": "The height of the text area, which is defined by the number of rows to display at a time. Default value is '2'.",
                "type": "Integer"
            },
            "select": {
                "description": "Indicates that the user has made a selection.",
                "type": "COMPONENT"
            },
            "updateOn": {
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is change.",
                "type": "String"
            },
            "validationError": {
                "description": "Indicates that the component has validation error(s).",
                "type": "COMPONENT"
            },
            "value": {
                "description": "The value currently in the input field.",
                "type": "String"
            },
            "width": {
                "description": "The editor UI outer width. This can be an integer, for pixel sizes, or any CSS-defined unit. If isRichText is set to false, use the cols attribute instead.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:inputSecret": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "blur": {
                "description": "Indicates that a component has been put out of focus.",
                "type": "COMPONENT"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "change": {
                "description": "Indicates that the content of a component or the state has changed.",
                "type": "COMPONENT"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "clearErrors": {
                "description": "Indicates that any validation error should be cleared.",
                "type": "COMPONENT"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "copy": {
                "description": "Indicates that the user has copied content to the clipboard.",
                "type": "COMPONENT"
            },
            "cut": {
                "description": "Indicates that the user has cut content to the clipboard.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "disabled": {
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false.",
                "type": "Boolean"
            },
            "focus": {
                "description": "Indicates that a component has been put on focus.",
                "type": "COMPONENT"
            },
            "keydown": {
                "description": "Indicates that the user has pressed and released a keyboard key.",
                "type": "COMPONENT"
            },
            "keypress": {
                "description": "Indicates that the user has pressed and held down a keyboard key.",
                "type": "COMPONENT"
            },
            "keyup": {
                "description": "Indicates that the user has released a keyboard key.",
                "type": "COMPONENT"
            },
            "label": {
                "description": "The text of the label component",
                "type": "String"
            },
            "labelClass": {
                "description": "The CSS class of the label component",
                "type": "String"
            },
            "maxlength": {
                "description": "The maximum number of characters that can be typed into the input field. Corresponds to the maxlength attribute of the rendered HTML input element.",
                "type": "Integer"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "paste": {
                "description": "Indicates that the user has pasted content from the clipboard.",
                "type": "COMPONENT"
            },
            "placeholder": {
                "description": "Text that is displayed when the field is empty, to prompt the user for a valid entry.",
                "type": "String"
            },
            "required": {
                "description": "Specifies whether the input is required. Default value is false.",
                "type": "Boolean"
            },
            "requiredIndicatorClass": {
                "description": "The CSS class of the required indicator component",
                "type": "String"
            },
            "select": {
                "description": "Indicates that the user has made a selection.",
                "type": "COMPONENT"
            },
            "size": {
                "description": "The width of the input field, in characters. Corresponds to the size attribute of the rendered HTML input element.",
                "type": "Integer"
            },
            "updateOn": {
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is 'change'.",
                "type": "String"
            },
            "validationError": {
                "description": "Indicates that the component has validation error(s).",
                "type": "COMPONENT"
            },
            "value": {
                "description": "The value currently in the input field.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:inputSelect": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "blur": {
                "description": "Indicates that a component has been put out of focus.",
                "type": "COMPONENT"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "change": {
                "description": "Indicates that the content of a component or the state has changed.",
                "type": "COMPONENT"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "clearErrors": {
                "description": "Indicates that any validation error should be cleared.",
                "type": "COMPONENT"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "copy": {
                "description": "Indicates that the user has copied content to the clipboard.",
                "type": "COMPONENT"
            },
            "cut": {
                "description": "Indicates that the user has cut content to the clipboard.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "disabled": {
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false.",
                "type": "Boolean"
            },
            "focus": {
                "description": "Indicates that a component has been put on focus.",
                "type": "COMPONENT"
            },
            "keydown": {
                "description": "Indicates that the user has pressed and released a keyboard key.",
                "type": "COMPONENT"
            },
            "keypress": {
                "description": "Indicates that the user has pressed and held down a keyboard key.",
                "type": "COMPONENT"
            },
            "keyup": {
                "description": "Indicates that the user has released a keyboard key.",
                "type": "COMPONENT"
            },
            "label": {
                "description": "The text of the label component",
                "type": "String"
            },
            "labelClass": {
                "description": "The CSS class of the label component",
                "type": "String"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "multiple": {
                "description": "Specifies whether the input is a multiple select. Default value is \u00a1\u00b0false\u00a1\u00b1.",
                "type": "Boolean"
            },
            "options": {
                "description": "A list of aura.components.ui.InputOption.",
                "type": "List"
            },
            "paste": {
                "description": "Indicates that the user has pasted content from the clipboard.",
                "type": "COMPONENT"
            },
            "required": {
                "description": "Specifies whether the input is required. Default value is false.",
                "type": "Boolean"
            },
            "requiredIndicatorClass": {
                "description": "The CSS class of the required indicator component",
                "type": "String"
            },
            "select": {
                "description": "Indicates that the user has made a selection.",
                "type": "COMPONENT"
            },
            "updateOn": {
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is change.",
                "type": "String"
            },
            "validationError": {
                "description": "Indicates that the component has validation error(s).",
                "type": "COMPONENT"
            },
            "value": {
                "description": "The value currently in the input field.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:inputSelectOption": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "blur": {
                "description": "Indicates that a component has been put out of focus.",
                "type": "COMPONENT"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "disabled": {
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false.",
                "type": "Boolean"
            },
            "focus": {
                "description": "Indicates that a component has been put on focus.",
                "type": "COMPONENT"
            },
            "keydown": {
                "description": "Indicates that the user has pressed and released a keyboard key.",
                "type": "COMPONENT"
            },
            "keypress": {
                "description": "Indicates that the user has pressed and held down a keyboard key.",
                "type": "COMPONENT"
            },
            "keyup": {
                "description": "Indicates that the user has released a keyboard key.",
                "type": "COMPONENT"
            },
            "label": {
                "description": "The text displayed on the component.",
                "type": "String"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "name": {
                "description": "The name of the component.",
                "type": "String"
            },
            "select": {
                "description": "Indicates that the user has made a selection.",
                "type": "COMPONENT"
            },
            "text": {
                "description": "The input value attribute.",
                "type": "String"
            },
            "value": {
                "description": "Indicates whether the status of the option is selected. Default value is \u00a1\u00b0false\u00a1\u00b1.",
                "type": "Boolean"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:inputText": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "blur": {
                "description": "Indicates that a component has been put out of focus.",
                "type": "COMPONENT"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "change": {
                "description": "Indicates that the content of a component or the state has changed.",
                "type": "COMPONENT"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "clearErrors": {
                "description": "Indicates that any validation error should be cleared.",
                "type": "COMPONENT"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "copy": {
                "description": "Indicates that the user has copied content to the clipboard.",
                "type": "COMPONENT"
            },
            "cut": {
                "description": "Indicates that the user has cut content to the clipboard.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "disabled": {
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false.",
                "type": "Boolean"
            },
            "focus": {
                "description": "Indicates that a component has been put on focus.",
                "type": "COMPONENT"
            },
            "keydown": {
                "description": "Indicates that the user has pressed and released a keyboard key.",
                "type": "COMPONENT"
            },
            "keypress": {
                "description": "Indicates that the user has pressed and held down a keyboard key.",
                "type": "COMPONENT"
            },
            "keyup": {
                "description": "Indicates that the user has released a keyboard key.",
                "type": "COMPONENT"
            },
            "label": {
                "description": "The text of the label component",
                "type": "String"
            },
            "labelClass": {
                "description": "The CSS class of the label component",
                "type": "String"
            },
            "maxlength": {
                "description": "The maximum number of characters that can be typed into the input field. Corresponds to the maxlength attribute of the rendered HTML input element.",
                "type": "Integer"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "paste": {
                "description": "Indicates that the user has pasted content from the clipboard.",
                "type": "COMPONENT"
            },
            "placeholder": {
                "description": "Text that is displayed when the field is empty, to prompt the user for a valid entry.",
                "type": "String"
            },
            "required": {
                "description": "Specifies whether the input is required. Default value is false.",
                "type": "Boolean"
            },
            "requiredIndicatorClass": {
                "description": "The CSS class of the required indicator component",
                "type": "String"
            },
            "select": {
                "description": "Indicates that the user has made a selection.",
                "type": "COMPONENT"
            },
            "size": {
                "description": "The width of the input field, in characters. Corresponds to the size attribute of the rendered HTML input element.",
                "type": "Integer"
            },
            "updateOn": {
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is change.",
                "type": "String"
            },
            "validationError": {
                "description": "Indicates that the component has validation error(s).",
                "type": "COMPONENT"
            },
            "value": {
                "description": "The value currently in the input field.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:inputTextArea": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "blur": {
                "description": "Indicates that a component has been put out of focus.",
                "type": "COMPONENT"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "change": {
                "description": "Indicates that the content of a component or the state has changed.",
                "type": "COMPONENT"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "clearErrors": {
                "description": "Indicates that any validation error should be cleared.",
                "type": "COMPONENT"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "cols": {
                "description": "The width of the text area, which is defined by the number of characters to display in a single row at a time. Default value is '20'.",
                "type": "Integer"
            },
            "copy": {
                "description": "Indicates that the user has copied content to the clipboard.",
                "type": "COMPONENT"
            },
            "cut": {
                "description": "Indicates that the user has cut content to the clipboard.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "disabled": {
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is 'false'.",
                "type": "Boolean"
            },
            "focus": {
                "description": "Indicates that a component has been put on focus.",
                "type": "COMPONENT"
            },
            "keydown": {
                "description": "Indicates that the user has pressed and released a keyboard key.",
                "type": "COMPONENT"
            },
            "keypress": {
                "description": "Indicates that the user has pressed and held down a keyboard key.",
                "type": "COMPONENT"
            },
            "keyup": {
                "description": "Indicates that the user has released a keyboard key.",
                "type": "COMPONENT"
            },
            "label": {
                "description": "The text of the label component",
                "type": "String"
            },
            "labelClass": {
                "description": "The CSS class of the label component",
                "type": "String"
            },
            "maxlength": {
                "description": "The maximum number of characters that can be typed into the input field. Corresponds to the maxlength attribute of the rendered HTML textarea element.",
                "type": "Integer"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "paste": {
                "description": "Indicates that the user has pasted content from the clipboard.",
                "type": "COMPONENT"
            },
            "placeholder": {
                "description": "The text that is displayed by default.",
                "type": "String"
            },
            "readonly": {
                "description": "Specifies whether the text area should be rendered as read-only. Default value is 'false'.",
                "type": "Boolean"
            },
            "required": {
                "description": "Specifies whether the input is required. Default value is 'false'.",
                "type": "Boolean"
            },
            "requiredIndicatorClass": {
                "description": "The CSS class of the required indicator component",
                "type": "String"
            },
            "resizable": {
                "description": "Specifies whether or not the textarea should be resizable. Defaults to true.",
                "type": "Boolean"
            },
            "rows": {
                "description": "The height of the text area, which is defined by the number of rows to display at a time. Default value is '2'.",
                "type": "Integer"
            },
            "select": {
                "description": "Indicates that the user has made a selection.",
                "type": "COMPONENT"
            },
            "updateOn": {
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is 'change'.",
                "type": "String"
            },
            "validationError": {
                "description": "Indicates that the component has validation error(s).",
                "type": "COMPONENT"
            },
            "value": {
                "description": "The value currently in the input field.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:inputURL": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "blur": {
                "description": "Indicates that a component has been put out of focus.",
                "type": "COMPONENT"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "change": {
                "description": "Indicates that the content of a component or the state has changed.",
                "type": "COMPONENT"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "clearErrors": {
                "description": "Indicates that any validation error should be cleared.",
                "type": "COMPONENT"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "copy": {
                "description": "Indicates that the user has copied content to the clipboard.",
                "type": "COMPONENT"
            },
            "cut": {
                "description": "Indicates that the user has cut content to the clipboard.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "disabled": {
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false.",
                "type": "Boolean"
            },
            "focus": {
                "description": "Indicates that a component has been put on focus.",
                "type": "COMPONENT"
            },
            "keydown": {
                "description": "Indicates that the user has pressed and released a keyboard key.",
                "type": "COMPONENT"
            },
            "keypress": {
                "description": "Indicates that the user has pressed and held down a keyboard key.",
                "type": "COMPONENT"
            },
            "keyup": {
                "description": "Indicates that the user has released a keyboard key.",
                "type": "COMPONENT"
            },
            "label": {
                "description": "The text of the label component",
                "type": "String"
            },
            "labelClass": {
                "description": "The CSS class of the label component",
                "type": "String"
            },
            "maxlength": {
                "description": "The maximum number of characters that can be typed into the input field. Corresponds to the maxlength attribute of the rendered HTML input element.",
                "type": "Integer"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "paste": {
                "description": "Indicates that the user has pasted content from the clipboard.",
                "type": "COMPONENT"
            },
            "placeholder": {
                "description": "Text that is displayed when the field is empty, to prompt the user for a valid entry.",
                "type": "String"
            },
            "required": {
                "description": "Specifies whether the input is required. Default value is false.",
                "type": "Boolean"
            },
            "requiredIndicatorClass": {
                "description": "The CSS class of the required indicator component",
                "type": "String"
            },
            "select": {
                "description": "Indicates that the user has made a selection.",
                "type": "COMPONENT"
            },
            "size": {
                "description": "The width of the input field, in characters. Corresponds to the size attribute of the rendered HTML input element.",
                "type": "Integer"
            },
            "updateOn": {
                "description": "Updates the component's value binding if the updateOn attribute is set to the handled event. Default value is change.",
                "type": "String"
            },
            "validationError": {
                "description": "Indicates that the component has validation error(s).",
                "type": "COMPONENT"
            },
            "value": {
                "description": "The value currently in the input field.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:menu": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:menuItem": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "blur": {
                "description": "Indicates that a component has been put out of focus.",
                "type": "COMPONENT"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "disabled": {
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false.",
                "type": "Boolean"
            },
            "focus": {
                "description": "Indicates that a component has been put on focus.",
                "type": "COMPONENT"
            },
            "hideMenuAfterSelected": {
                "description": "Set to true to hide menu after the menu item is selected.",
                "type": "Boolean"
            },
            "keydown": {
                "description": "Indicates that the user has pressed and released a keyboard key.",
                "type": "COMPONENT"
            },
            "keypress": {
                "description": "Indicates that the user has pressed and held down a keyboard key.",
                "type": "COMPONENT"
            },
            "keyup": {
                "description": "Indicates that the user has released a keyboard key.",
                "type": "COMPONENT"
            },
            "label": {
                "description": "The text displayed on the component.",
                "type": "String"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "select": {
                "description": "Indicates that the user has made a selection.",
                "type": "COMPONENT"
            },
            "selected": {
                "description": "The status of the menu item. True means this menu item is selected; False is not selected.",
                "type": "Boolean"
            },
            "type": {
                "description": "The concrete type of the menu item. Accepted values are 'action', 'checkbox', 'radio', 'separator' or any namespaced component descriptor, e.g. ns:xxxxmenuItem.",
                "type": "String",
                "values": [
                    "action",
                    "checkbox",
                    "radio",
                    "separator",
                    "${1:ns:xxxxmenuItem}"
                ]
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:menuItemSeparator": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:menuList": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "autoPosition": {
                "description": "Move the popup target up when there is not enough space at the bottom to display. Note: even if autoPosition is set to false, popup will still position the menu relative to the trigger. To override default positioning, use manualPosition attribute.",
                "type": "Boolean"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "closeOnClickOutside": {
                "description": "Close target when user clicks or taps outside of the target",
                "type": "Boolean"
            },
            "closeOnTabKey": {
                "description": "Indicates whether to close the target list on tab key or not.",
                "type": "Boolean"
            },
            "collapse": {
                "description": "Indicates that a component collapses.",
                "type": "COMPONENT"
            },
            "curtain": {
                "description": "Whether or not to apply an overlay under the target.",
                "type": "Boolean"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "expand": {
                "description": "Indicates that a component expands.",
                "type": "COMPONENT"
            },
            "menuFocusChange": {
                "description": "Indicates that the user changes menu item focus inside a menu component.",
                "type": "COMPONENT"
            },
            "menuItems": {
                "description": "A list of menu items set explicitly using instances of the Java class: aura.components.ui.MenuItem.",
                "type": "List"
            },
            "menuSelect": {
                "description": "Indicates that the user selects a menu item inside a menu component.",
                "type": "COMPONENT"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "visible": {
                "description": "Controls the visibility of the menu. The default is false, which hides the menu.",
                "type": "Boolean"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:menuTrigger": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "blur": {
                "description": "Indicates that a component has been put out of focus.",
                "type": "COMPONENT"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "disabled": {
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false.",
                "type": "Boolean"
            },
            "focus": {
                "description": "Indicates that a component has been put on focus.",
                "type": "COMPONENT"
            },
            "keydown": {
                "description": "Indicates that the user has pressed and released a keyboard key.",
                "type": "COMPONENT"
            },
            "keypress": {
                "description": "Indicates that the user has pressed and held down a keyboard key.",
                "type": "COMPONENT"
            },
            "keyup": {
                "description": "Indicates that the user has released a keyboard key.",
                "type": "COMPONENT"
            },
            "menuTriggerPress": {
                "description": "Indicates that the menu trigger is clicked.",
                "type": "COMPONENT"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "select": {
                "description": "Indicates that the user has made a selection.",
                "type": "COMPONENT"
            },
            "title": {
                "description": "The text to display as a tooltip when the mouse pointer hovers over this component.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:menuTriggerLink": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "blur": {
                "description": "Indicates that a component has been put out of focus.",
                "type": "COMPONENT"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "disabled": {
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false.",
                "type": "Boolean"
            },
            "focus": {
                "description": "Indicates that a component has been put on focus.",
                "type": "COMPONENT"
            },
            "keydown": {
                "description": "Indicates that the user has pressed and released a keyboard key.",
                "type": "COMPONENT"
            },
            "keypress": {
                "description": "Indicates that the user has pressed and held down a keyboard key.",
                "type": "COMPONENT"
            },
            "keyup": {
                "description": "Indicates that the user has released a keyboard key.",
                "type": "COMPONENT"
            },
            "label": {
                "description": "The text displayed on the component.",
                "type": "String"
            },
            "menuTriggerPress": {
                "description": "Indicates that the menu trigger is clicked.",
                "type": "COMPONENT"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "select": {
                "description": "Indicates that the user has made a selection.",
                "type": "COMPONENT"
            },
            "title": {
                "description": "The text to display as a tooltip when the mouse pointer hovers over this component.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:message": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "closable": {
                "description": "Specifies whether to display an 'x' that will close the alert when clicked. Default value is 'false'.",
                "type": "Boolean"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "severity": {
                "description": "The severity of the message. Possible values: message (default), confirm, info, warning, error",
                "type": "String"
            },
            "title": {
                "description": "The title text for the message.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:outputCheckbox": {
        "attribs": {
            "altChecked": {
                "description": "The alternate text description when the checkbox is checked. Default value is 'True'.",
                "type": "String"
            },
            "altUnchecked": {
                "description": "The alternate text description when the checkbox is unchecked. Default value is 'False'.",
                "type": "String"
            },
            "aura:id": {
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "value": {
                "description": "Specifies whether the checkbox is checked.",
                "type": "Boolean"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:outputCurrency": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "currencyCode": {
                "description": "The ISO 4217 currency code specified as a String, e.g. USD.",
                "type": "String"
            },
            "currencySymbol": {
                "description": "The currency symbol specified as a String.",
                "type": "String"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "format": {
                "description": "The format of the number. For example, format=\u00a1\u00b0.00\u00a1\u00b1 displays the number followed by two decimal places. If not specified, the default format based on the browser's locale will be used.",
                "type": "String"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "value": {
                "description": "The output value of the currency, which is defined as type Decimal.",
                "type": "BigDecimal"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:outputDataTime": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "format": {
                "description": "A string (pattern letters are defined in java.text.SimpleDateFormat) used to format the date and time of the value attribute.",
                "type": "String"
            },
            "langLocale": {
                "description": "The language locale used to format date value.",
                "type": "String"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "timezone": {
                "description": "The timezone ID, for example, America/Los_Angeles.",
                "type": "Picklist",
                "values": [
                    "Pacific/Chatham",
                    "Pacific/Auckland",
                    "Pacific/Enderbury",
                    "Pacific/Fiji",
                    "Pacific/Tongatapu",
                    "Asia/Kamchatka",
                    "Australia/Lord_Howe",
                    "Australia/Sydney",
                    "Pacific/Guadalcanal",
                    "Pacific/Norfolk",
                    "Australia/Adelaide",
                    "Australia/Brisbane",
                    "Australia/Darwin",
                    "Asia/Seoul",
                    "Asia/Tokyo",
                    "Asia/Hong_Kong",
                    "Asia/Kuala_Lumpur",
                    "Asia/Manila",
                    "Asia/Shanghai",
                    "Asia/Singapore",
                    "Asia/Taipei",
                    "Australia/Perth",
                    "Asia/Bangkok",
                    "Asia/Ho_Chi_Minh",
                    "Asia/Jakarta",
                    "Asia/Rangoon",
                    "Asia/Dhaka",
                    "Asia/Kathmandu",
                    "Asia/Colombo",
                    "Asia/Kolkata",
                    "Asia/Karachi",
                    "Asia/Tashkent",
                    "Asia/Yekaterinburg",
                    "Asia/Kabul",
                    "Asia/Baku",
                    "Asia/Dubai",
                    "Asia/Tbilisi",
                    "Asia/Yerevan",
                    "Asia/Tehran",
                    "Africa/Nairobi",
                    "Asia/Baghdad",
                    "Asia/Kuwait",
                    "Asia/Riyadh",
                    "Europe/Minsk",
                    "Europe/Moscow",
                    "Africa/Cairo",
                    "Africa/Johannesburg",
                    "Asia/Beirut",
                    "Asia/Jerusalem",
                    "Europe/Athens",
                    "Europe/Bucharest",
                    "Europe/Helsinki",
                    "Europe/Istanbul",
                    "Africa/Algiers",
                    "Europe/Amsterdam",
                    "Europe/Berlin",
                    "Europe/Brussels",
                    "Europe/Paris",
                    "Europe/Prague",
                    "Europe/Rome",
                    "Africa/Casablanca",
                    "Europe/Dublin",
                    "Europe/Lisbon",
                    "Europe/London",
                    "America/Scoresbysund",
                    "Atlantic/Azores",
                    "Atlantic/Cape_Verde",
                    "America/Sao_Paulo",
                    "Atlantic/South_Georgia",
                    "America/Argentina/Buenos_Aires",
                    "America/Santiago",
                    "America/St_Johns",
                    "America/Halifax",
                    "America/Puerto_Rico",
                    "Atlantic/Bermuda",
                    "America/Caracas",
                    "America/Bogota",
                    "America/Indiana/Indianapolis",
                    "America/Lima",
                    "America/New_York",
                    "America/Panama",
                    "America/Chicago",
                    "America/El_Salvador",
                    "America/Mexico_City",
                    "America/Denver",
                    "America/Mazatlan",
                    "America/Phoenix",
                    "America/Los_Angeles",
                    "America/Tijuana",
                    "Pacific/Pitcairn",
                    "America/Anchorage",
                    "Pacific/Gambier",
                    "Pacific/Marquesas",
                    "America/Adak",
                    "Pacific/Honolulu",
                    "Pacific/Niue",
                    "Pacific/Pago_Pago"
                ]
            },
            "value": {
                "description": "An ISO8601-formatted string representing a date time.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:outputDate": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "format": {
                "description": "A string (pattern letters are defined in java.text.SimpleDateFormat) used to format the date and time of the value attribute.",
                "type": "String"
            },
            "langLocale": {
                "description": "The language locale used to format date value.",
                "type": "String"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "value": {
                "description": "The output value of the date. It should be a date string in ISO-8601 format (YYYY-MM-DD).",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:outputEmail": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "value": {
                "description": "The output value of the email",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:outputNumber": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "format": {
                "description": "The format of the number. For example, format=\u00a1\u00b0.00\u00a1\u00b1 displays the number followed by two decimal places. If not specified, the Locale default format will be used.",
                "type": "String"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "value": {
                "description": "The number displayed when this component is rendered.",
                "type": "BigDecimal"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:outputPhone": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "value": {
                "description": "The phone number displayed when this component is rendered.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:outputRichText": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "value": {
                "description": "The richly-formatted text used for output.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:outputText": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "value": {
                "description": "The text displayed when this component is rendered.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:outputTextArea": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "value": {
                "description": "The text to display.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:outputURL": {
        "attribs": {
            "alt": {
                "description": "The alternate text description for image (used when there is no label)",
                "type": "String"
            },
            "aura:id": {
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "disabled": {
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false.",
                "type": "Boolean"
            },
            "iconClass": {
                "description": "The CSS style used to display the icon or image.",
                "type": "String"
            },
            "label": {
                "description": "The text displayed on the component.",
                "type": "String"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "target": {
                "description": "The target destination where this rendered component is displayed. Possible values: _blank, _parent, _self, _top",
                "type": "Picklist",
                "values": [
                    "_blank",
                    "_parent",
                    "_self",
                    "_top"
                ]
            },
            "title": {
                "description": "The text to display as a tooltip when the mouse pointer hovers over this component.",
                "type": "String"
            },
            "value": {
                "description": "The text displayed when this component is rendered.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:radioMenuItem": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "blur": {
                "description": "Indicates that a component has been put out of focus.",
                "type": "COMPONENT"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "class": {
                "description": "A CSS style to be attached to the component. This style is added in addition to base styles output by the component.",
                "type": "String"
            },
            "click": {
                "description": "Indicates that a component has been clicked.",
                "type": "COMPONENT"
            },
            "dblclick": {
                "description": "Indicates that a component has been double-clicked.",
                "type": "COMPONENT"
            },
            "disabled": {
                "description": "Specifies whether the component should be displayed in a disabled state. Default value is false.",
                "type": "Boolean"
            },
            "focus": {
                "description": "Indicates that a component has been put on focus.",
                "type": "COMPONENT"
            },
            "hideMenuAfterSelected": {
                "description": "Set to true to hide menu after the menu item is selected.",
                "type": "Boolean"
            },
            "keydown": {
                "description": "Indicates that the user has pressed and released a keyboard key.",
                "type": "COMPONENT"
            },
            "keypress": {
                "description": "Indicates that the user has pressed and held down a keyboard key.",
                "type": "COMPONENT"
            },
            "keyup": {
                "description": "Indicates that the user has released a keyboard key.",
                "type": "COMPONENT"
            },
            "label": {
                "description": "The text displayed on the component.",
                "type": "String"
            },
            "mousedown": {
                "description": "Indicates that the user has pressed a mouse key.",
                "type": "COMPONENT"
            },
            "mousemove": {
                "description": "Indicates that the user has moved the mouse pointer.",
                "type": "COMPONENT"
            },
            "mouseout": {
                "description": "Indicates that the user has moved the mouse pointer away from the component.",
                "type": "COMPONENT"
            },
            "mouseover": {
                "description": "Indicates that the user has moved the mouse pointer over the component.",
                "type": "COMPONENT"
            },
            "mouseup": {
                "description": "Indicates that the user has released the mouse button.",
                "type": "COMPONENT"
            },
            "select": {
                "description": "Indicates that the user has made a selection.",
                "type": "COMPONENT"
            },
            "selected": {
                "description": "The status of the menu item. True means this menu item is selected; False is not selected.",
                "type": "Boolean"
            },
            "type": {
                "description": "The concrete type of the menu item. Accepted values are 'action', 'checkbox', 'radio', 'separator' or any namespaced component descriptor, e.g. ns:xxxxmenuItem.",
                "type": "Picklist",
                "values": [
                    "action",
                    "checkbox",
                    "radio",
                    "separator",
                    "${1:ns:xxxxmenuItem}"
                ]
            }
        },
        "simple": False,
        "type": "aura"
    },
    "ui:spinner": {
        "attribs": {
            "aura:id": {
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "isVisible": {
                "description": "Specifies whether or not this spinner should be visible. Defaults to true.",
                "type": "Boolean"
            },
            "toggleLoadingIndicator": {
                "description": "Change the visibility of a ui:spinner component.",
                "type": "COMPONENT"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "wave:waveDashboard": {
        "attribs": {
            "accessToken": {
                "description": "A valid access token obtained by logging into Salesforce. Useful when the component is used by Lightning Out in a non salesforce domain.",
                "type": "String"
            },
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "dashboardId": {
                "description": "The unique ID of the dashboard",
                "type": "String"
            },
            "developerName": {
                "description": "The unique developer name of the dashboard",
                "type": "String"
            },
            "filter": {
                "description": "Adds selections or filters to the embedded dashboard at runtime",
                "type": "String"
            },
            "height": {
                "description": "Specifies the height of the dashboard, in pixels.",
                "type": "Integer"
            },
            "hideOnError": {
                "description": "Controls whether or not users see a dashboard that has an error",
                "type": "Boolean"
            },
            "openLinksInNewWindow": {
                "description": "If false, links to other dashboards will be opened in the same window.",
                "type": "Boolean"
            },
            "recordId": {
                "description": "Id of the current entity in the context of which the component is being displayed.",
                "type": "String"
            },
            "showHeader": {
                "description": "If true, the dashboard is displayed with a header bar that includes dashboard information and controls",
                "type": "Boolean"
            },
            "showSharing": {
                "description": "If true, and the dashboard is shareable, then the dashboard shows the Share icon",
                "type": "Boolean"
            },
            "showTitle": {
                "description": "If true, title of the dashboard is included above the dashboard. If false, the dashboard appears without a title.",
                "type": "Boolean"
            }
        },
        "simple": False,
        "type": "aura"
    }
}
