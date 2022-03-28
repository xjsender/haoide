# Since 2019, Winter19, v44
std_events = {
    "lightning:conversationAgentSend": {
        "attrs": [
            {
                "type": "string", 
                "required": True, 
                "access": "global", 
                "name": "recordId", 
                "description": "Record ID of the conversation"
            }, 
            {
                "type": "string", 
                "required": True, 
                "access": "global", 
                "name": "content", 
                "description": "The text of a message in the chat log."
            }, 
            {
                "type": "string", 
                "required": True, 
                "access": "global", 
                "name": "name", 
                "description": "The name of the agent who is attempting to send the message as it appears in the chat log."
            }, 
            {
                "type": "string", 
                "required": True, 
                "access": "global", 
                "name": "type", 
                "description": "The type of message that was received—for example, agent."
            }, 
            {
                "type": "date", 
                "required": True, 
                "access": "global", 
                "name": "timestamp", 
                "description": "The date and time the agent attempted to send the chat message."
            }
        ]
    },

    "lightning:conversationChatEnded": {
        "attrs": [
            {
                "name": "recordId",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "Record ID of the conversation"
            }
        ]
    },

    "lightning:conversationCustomEvent": {
        "attrs": [
            {
                "name": "recordId",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "Record ID of the conversation"
            },
            {
                "name": "type",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "Name of the custom event"
            },
            {
                "name": "data",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "Data attached to the custom event"
            }
        ]
    },

    "lightning:conversationNewMessage": {
        "attrs": [
            {
                "name": "recordId",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "Record ID of the conversation"
            },
            {
                "name": "content",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "The text of a message in the chat log."
            },
            {
                "name": "name",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "The name of the agent who is attempting to send the message as it appears in the chat log."
            },
            {
                "name": "type",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "The type of message that was received—for example, agent."
            },
            {
                "name": "timestamp",
                "type": "date",
                "access": "global",
                "required": True,
                "description": "The date and time the agent attempted to send the chat message."
            }
        ]
    },

    "lightning:openFiles": {
        "attrs": [
            {
                "name": "recordIds",
                "type": "string[]",
                "access": "global",
                "required": True,
                "description": "IDs of the records to open. This must not be empty."
            },
            {
                "name": "selectedRecordId",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "ID of the record to open first among the one specified in the recordIds attribute. If this value is not provided or if the value provided is not in the list, the first element from the list will be used."
            }
        ]
    },

    "lightning:sendChatterExtensionPayload": {
        "attrs": [
            {
                "name": "payload",
                "type": "object",
                "access": "global",
                "required": True,
                "description": "Payload data to be saved with the feed item."
            },
            {
                "name": "extensionTitle",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "Title for the extension to be saved with the feed item."
            },
            {
                "name": "extensionDescription",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "Description for the extension to be saved with the feed item"
            },
            {
                "name": "extensionThumbnailUrl",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "thumbnailUrl for the extension to be saved with the feedItem"
            }
        ]
    },

    "lightning:tabClosed": {
        "attrs": [
            {
                "name": "tabId",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "The closed tab ID."
            }
        ]
    },

    "lightning:tabCreated": {
        "attrs": [
            {
                "name": "tabId",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "The newly created tab ID."
            }
        ]
    },

    "lightning:tabFocused": {
        "attrs": [
            {
                "name": "previousTabId",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "The previously focused tab ID."
            },
            {
                "name": "currentTabId",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "The currently focused tab ID."
            }
        ]
    },

    "lightning:tabRefreshed": {
        "attrs": [
            {
                "name": "tabId",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "The currently refreshed tab ID."
            }
        ]
    },

    "lightning:tabReplaced": {
        "attrs": [
            {
                "name": "tabId",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "The ID of the refreshed tab."
            }
        ]
    },

    "lightning:tabUpdated": {
        "attrs": [
            {
                "name": "tabId",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "The ID of the tab that was updated."
            }
        ]
    },

    "aura:applicationEvent": {
        "attrs": []
    },

    "aura:componentEvent": {
        "attrs": []
    },

    "aura:doneRendering": {
        "attrs": []
    },

    "aura:doneWaiting": {
        "attrs": []
    },

    "aura:locationChange": {
        "attrs": [
            {
                "name": "token",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "The new hash part of the url"
            },
            {
                "name": "querystring",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "The query string portion of the hash that is stripped off and applied to the event as parameters."
            }
        ]
    },

    "aura:methodCall": {
        "attrs": [
            {
                "name": "name",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "The name of the method called."
            },
            {
                "name": "arguments",
                "type": "list",
                "access": "global",
                "required": False,
                "description": "The list of arguments passed into the public method."
            }
        ]
    },

    "aura:noAccess": {
        "attrs": [
            {
                "name": "redirectURL",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "A url that the server says the application should redirect the browser to when this event fires."
            }
        ]
    },

    "aura:systemError": {
        "attrs": [
            {
                "name": "message",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "The message to be displayed during an error."
            },
            {
                "name": "error",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "The system error that's returned."
            }
        ]
    },

    "aura:valueChange": {
        "attrs": [
            {
                "name": "expression",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "The expression that triggered the value change."
            },
            {
                "name": "oldValue",
                "type": "object",
                "access": "global",
                "required": False,
                "description": "The previous value that was changed."
            },
            {
                "name": "value",
                "type": "object",
                "access": "global",
                "required": False,
                "description": "The new value."
            },
            {
                "name": "index",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "If the handler was registered through an ArrayValue or MapValue, the name/index of the changed Value in that ArrayValue or MapValue"
            }
        ]
    },

    "aura:valueDestroy": {
        "attrs": [
            {
                "name": "value",
                "type": "object",
                "access": "global",
                "required": False,
                "description": "The component that is being destroyed."
            }
        ]
    },

    "aura:valueEvent": {
        "attrs": []
    },

    "aura:valueInit": {
        "attrs": [
            {
                "name": "value",
                "type": "object",
                "access": "global",
                "required": False,
                "description": "The component that initialized."
            }
        ]
    },

    "aura:valueRender": {
        "attrs": [
            {
                "name": "value",
                "type": "object",
                "access": "global",
                "required": False,
                "description": "The component that rendered."
            }
        ]
    },

    "aura:waiting": {
        "attrs": []
    },
    
    "force:closeQuickAction": {
        "attrs": []
    },

    "force:createRecord": {
        "attrs": [
            {
                "name": "entityApiName",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "Required. The API name of the custom or standard object, such as \"Account\", \"Case\", \"Contact\", \"Lead\", \"Opportunity\", or \"namespace__objectName__c\"."
            },
            {
                "name": "recordTypeId",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "Non-null if recordTypes are enabled. Null means Master RecordType."
            },
            {
                "name": "defaultFieldValues",
                "type": "map",
                "access": "global",
                "required": False,
                "description": "Prepopulates fields on a record create panel, including fields not displayed on the panel. ID fields and rich text fields can't be prepopulated. Users must have create access to prepopulated fields. Errors during saving that are caused by field access limitations do not display error messages."
            }
        ]
    },

    "force:editRecord": {
        "attrs": [
            {
                "name": "recordId",
                "type": "string",
                "access": "global",
                "required": True,
                "description": ""
            }
        ]
    },

    "force:navigateHome": {
        "attrs": []
    },

    "force:navigateToComponent" : {
        "attrs": [
            {
                "name": "componentDef",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "The component to navigate to, for example, c:myComponent."
            },
            {
                "name": "componentAttributes",
                "type": "object",
                "access": "global",
                "required": False,
                "description": "The attributes for the component."
            },
            {
                "name": "isredirect",
                "type": "boolean",
                "access": "global",
                "required": False,
                "description": "Specifies whether the navigation is a redirect. If true, the browser replaces the current URL with the new one in the navigation history. This value defaults to false."
            }
        ]
    },

    "force:navigateToList": {
        "attrs": [
            {
                "name": "listViewId",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "The ID of the list view to be displayed"
            },
            {
                "name": "listViewName",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "Specifies the name for the list view and doesn't need to match the actual name. To use the actual name that's saved for the list view, set listViewName to null."
            },
            {
                "name": "scope",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "The name of the sObject in the view, for example, 'Account' or 'MyObject__c'"
            }
        ]
    },
    "force:navigateToObjectHome": {
        "attrs": [
            {
                "name": "scope",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "Tname or key prefix of entity to display object home for."
            },
            {
                "name": "resetHistory",
                "type": "boolean",
                "access": "global",
                "required": False,
                "description": "Set to true to reset history"
            }
        ]
    },

    # "force:navigateToReactNativeApp": {
    #     "attrs": [
    #         {
    #             "name": "appName",
    #             "type": "string",
    #             "access": "global",
    #             "required": False,
    #             "description": "The name of the react native app to navigate to, for example, Insights."
    #         },
    #         {
    #             "name": "params",
    #             "type": "object",
    #             "access": "global",
    #             "required": False,
    #             "description": "The parameters required for the react native app."
    #         }
    #     ]
    # },

    "force:navigateToRelatedList": {
        "attrs": [
            {
                "name": "relatedListId",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "The API name of the related list to display. For standard objects it is typically the related list's entity api name in plural form, such as 'Contacts' or '​Opportunitie​s'. For custom objects it takes the form of '{​YourCustom​Relationship​Label}__r'"
            },
            {
                "name": "parentRecordId",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "The ID of the parent record"
            },
            {
                "name": "entityApiName",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "The entity API name of the related list"
            }
        ]
    },

    "force:navigateToSObject": {
        "attrs": [
            {
                "name": "networkId",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "InheritedNetwork that the event is associated with."
            },
            {
                "name": "recordId",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "The record ID"
            },
            {
                "name": "slideDevName",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "The slideDevName of the slide to navigate to. By default, options are 'chatter', 'related', 'detail'."
            },
            {
                "name": "isredirect",
                "type": "boolean",
                "access": "global",
                "required": False,
                "description": "If we are redirecting in place, we don't want to create 2 history entries for hybrid. Instead hybrid ignores redirects as a history entry."
            }
        ]
    },

    "force:navigateToURL": {
        "attrs": [
            {
                "name": "networkId",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "InheritedNetwork that the event is associated with."
            },
            {
                "name": "isredirect",
                "type": "boolean",
                "access": "global",
                "required": False,
                "description": "If we are redirecting in place, we don't want to create 2 history entries for hybrid. Instead hybrid ignores redirects as a history entry."
            },
            {
                "name": "url",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "The URL of the target"
            }
        ]
    },

    "force:recordSave": {
        "attrs": []
    },

    "force:recordSaveSuccess": {
        "attrs": []
    },

    "force:refreshView": {
        "attrs": []
    },

    "force:showToast": {
        "attrs": [
            {
                "name": "title",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "Specifies the title for a message to display. The title is shown above the message in a slightly larger font."
            },
            {
                "name": "duration",
                "type": "integer",
                "access": "global",
                "required": False,
                "description": "Length of time the toast is visible for, in milliseconds. Applies to 'dismissible' or 'pester' toast modes. The default is 5000ms if the provided value is less than 5000ms."
            },
            {
                "name": "message",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "The message to display in the toast."
            },
            {
                "name": "key",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "Icon to use when toast type is 'other'. Icon keys are available at the Lightning Design System Icons page."
            },
            {
                "name": "mode",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "The toast mode, which controls how users can dismiss the toast. Valid values are 'pester' and 'sticky'. The default is 'dismissible', which displays the close button."
            },
            {
                "name": "type",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "The toast type, which can be 'error', 'warning', 'success', or 'info'. The default is 'other', which is styled like an 'info' toast and doesn’t display an icon, unless specified by the key attribute."
            },
            {
                "name": "messageTemplate",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "Overwrites message string with the specified message. Requires messageTemplateData."
            },
            {
                "name": "messageTemplateData",
                "type": "object[]",
                "access": "global",
                "required": False,
                "description": "An array of text and actions to be used in messageTemplate."
            }
        ]
    },

    "forceChatter:customOpenFile": {
        "attrs":  [
            {
                "name": "recordId",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "ID of the file record. This must not be empty."
            }
        ]
    },

    "forceChatter:postCreated": {
        "attrs": [
            {
                "name": "feedItemId",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "The id of the feed item that has been created"
            }
        ]
    },

    "forceCommunity:analyticsInteraction": {
        "attrs": [
            {
                "name": "hitType",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "The type of hit. Supported types: 'event', 'social', 'exception', 'timing'."
            },
            {
                "name": "eventCategory",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "The type or category of item that was interacted with. Required for 'event' hitType."
            },
            {
                "name": "eventAction",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "The type of action. Required for 'event' hitType."
            },
            {
                "name": "eventLabel",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "A label for providing additional event information."
            },
            {
                "name": "eventValue",
                "type": "integer",
                "access": "global",
                "required": False,
                "description": "A positive numeric value associated with the event."
            },
            {
                "name": "socialNetwork",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "The network on which the action occurs. Required for 'social' hitType."
            },
            {
                "name": "socialAction",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "The type of action that happens. Required for 'social' hitType."
            },
            {
                "name": "socialTarget",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "Specifies the target of a social interaction. Required for 'social' hitType."
            },
            {
                "name": "exDescription",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "A description of the exception."
            },
            {
                "name": "exFatal",
                "type": "boolean",
                "access": "global",
                "required": False,
                "description": "True if the exception was fatal."
            },
            {
                "name": "timingCategory",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "A string for categorizing all user timing variables into logical groups. Required for 'timing' hitType."
            },
            {
                "name": "timingVar",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "A string to identify the variable being recorded. Required for 'timing' hitType."
            },
            {
                "name": "timingValue",
                "type": "integer",
                "access": "global",
                "required": False,
                "description": "The number of milliseconds in elapsed time to report to Google Analytics. Required for 'timing' hitType."
            },
            {
                "name": "timingLabel",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "A string that can be used to add flexibility in visualizing user timings in the reports."
            }
        ]
    },

    "forceCommunity:routeChange": {
        "attrs": []
    },

    "lightningcommunity:deflectionSignal": {
        "attrs": [
            {
                "name": "sourceType",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "Descriptor of where deflection occured. Only signals with supported types will get processed. sourceType is synonymous with signalAgent."
            },
            {
                "name": "source",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "The unique identifier of how the user arrived at the deflection item."
            },
            {
                "name": "destinationType",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "Entity type of the deflection item."
            },
            {
                "name": "destination",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "The id of the deflection item."
            },
            {
                "name": "payload",
                "type": "object",
                "access": "global",
                "required": False,
                "description": "Additional information about the deflection signal. The content of the payload depends on the sourceType."
            },
            {
                "name": "shouldSubmitSourceTypeSignals",
                "type": "boolean",
                "access": "global",
                "required": False,
                "description": "Once an event is fired with shouldSubmitSourceTypeSignals=true,all signals of that sourceType are submitted to the server in a single batch to be processed. This should always be true unless signals are logically dependent on each other and must be processed together."
            },
            {
                "name": "callback",
                "type": "object",
                "access": "global",
                "required": False,
                "description": "Callback function invoked after signal is received and processed. Only called if shouldSubmitSourceTypeSignals=true."
            }
        ]
    },

    "ltng:afterScriptsLoaded": {
        "attrs": []
    },

    "ltng:beforeLoadingResources": {
        "attrs": []
    },

    "ltng:selectSObject": {
        "attrs": [
            {
                "name": "recordId",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "The record ID associated with the record to select."
            },
            {
                "name": "channel",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "Represents the channel name. Specify this attribute if you want particular components to process some event messages while ignoring others."
            }
        ]
    },

    "ltng:sendMessage": {
        "attrs": [
            {
                "name": "message",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "A message in the form of a String or JSON."
            },
            {
                "name": "channel",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "Represents the channel name. Use a channel to enable a component to filter down to specific events."
            }
        ]
    },

    "ui:clearErrors": {
        "attrs": []
    },

    "ui:collapse": {
        "attrs": []
    },

    "ui:expand": {
        "attrs": []
    },

    "ui:menuFocusChange": {
        "attrs": [
            {
                "name": "previousItem",
                "type": "component[]",
                "access": "global",
                "required": False,
                "description": "The menu item that's previously focused."
            },
            {
                "name": "currentItem",
                "type": "component[]",
                "access": "global",
                "required": False,
                "description": "The menu item that's currently focused."
            }
        ]
    },

    "ui:menuSelect": {
        "attrs": [
            {
                "name": "selectedItem",
                "type": "component[]",
                "access": "global",
                "required": False,
                "description": "The menu item that's selected."
            },
            {
                "name": "hideMenu",
                "type": "boolean",
                "access": "global",
                "required": False,
                "description": "Hides menu if set to true."
            },
            {
                "name": "deselectSiblings",
                "type": "boolean",
                "access": "global",
                "required": False,
                "description": "Deselects the siblings of the currently selected menu item."
            },
            {
                "name": "focusTrigger",
                "type": "boolean",
                "access": "global",
                "required": False,
                "description": "Sets focus to menuTrigger."
            }
        ]
    },

    "ui:menuTriggerPress": {
        "attrs": []
    },

    "ui:validationError": {
        "attrs": []
    },

    "wave:discover": {
        "attrs": [
            {
                "name": "UID",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "Optional identifier that will be included in the response data."
            }
        ]
    },

    "wave:discoverResponse": {
        "attrs": [
            {
                "name": "id",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "Dashboard Id."
            },
            {
                "name": "type",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "Type of component, usually dashboard."
            },
            {
                "name": "title",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "Title of the dashboard."
            },
            {
                "name": "isLoaded",
                "type": "boolean",
                "access": "global",
                "required": True,
                "description": "Whether dashboard is loaded or still loading."
            },
            {
                "name": "UID",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "Optional parameter sent with the request."
            }
        ]
    },

    "wave:pageChange": {
        "attrs": [
            {
                "name": "pageid",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "The dashboard page that should be displayed if value is supplied."
            },
            {
                "name": "devName",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "The dev name for the Wave Asset."
            }
        ]
    },

    "wave:selectionChanged": {
        "attrs": [
            {
                "name": "noun",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "The type of the Wave asset for which a selection change event occurred."
            },
            {
                "name": "verb",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "The action that occurred on the Wave asset."
            },
            {
                "name": "id",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "The identifier of the Wave asset for which a selection change event occurred."
            },
            {
                "name": "payload",
                "type": "string",
                "access": "global",
                "required": False,
                "description": "Contains the selection information from the asset that fired the event."
            }
        ]
    },

    "wave:update": {
        "attrs": [
            {
                "name": "id",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "The identifier for the Wave asset, in the form of a standard 18-character ID."
            },
            {
                "name": "value",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "The JSON representing the filter or selection to be applied to the asset."
            },
            {
                "name": "type",
                "type": "string",
                "access": "global",
                "required": True,
                "description": "The type of the Wave asset. Currently, only dashboard is supported."
            }
        ]
    }
}

standard_lib = {
    'e': {
        "type": "Standard Class",
        "properties": sorted(std_events.keys())
    },

    "A": {
        "type": "Standard Class",
        "prefix": "$",
        "sub_classes": [
            "util", "localizationService"
        ],
        "methods": {
            "createComponent(String type, Object attributes, function callback)\tvoid": "createComponent(${1:String type}, ${2:Object attributes}, ${3:function callback})$0",
            "createComponents(Array components, function callback)\tvoid": "createComponents(${1:Array components}, ${2:function callback})$0",
            "enqueueAction(Action action, Boolean background)\tvoid": "enqueueAction(${1:Action action}, ${2:Boolean background})$0",
            "enqueueAction(Action action)\tvoid": "enqueueAction(${1:Action action})$0",
            "get(String key, function callback)\tvoid": "get(${1:String key}, ${2:function callback})$0",
            "get(String key)\tvoid": "get(${1:String key})$0",
            "getCallback(function callback)\tvoid": "getCallback(${!:function callback})$0",
            "getComponent(Object identifier)\tvoid": "getComponent(${1:Object identifier})$0",
            "getReference(String key)\tvoid": "getReference(${1:String key})$0",
            "getRoot()\tvoid": "getRoot()$0",
            "getToken(String token)\tvoid": "getToken(${1:String token})$0",
            "log(Object value, Object error)\tvoid": "log(${1:Object value}, ${2:Object error})$0",
            "reportError(String message, Error error)\tvoid": "reportError(${1:String message}, ${2:Error error})$0",
            "set(String key, Object value)\tvoid": "set(${1:String key}, ${2:Object value})$0",
            "warning(String w, Error e)\tvoid": "warning(${1:String w}, ${2:Error e})$0",
        }
    },

    "util": {
        "sub_class": True,
        "type": "Standard Class",
        "methods": {
            "addClass(Object element, String newClass)\tvoid": "addClass(${1:Object element}, ${2:String newClass})$0",
            "getBooleanValue(Object val)\tBoolean": "getBooleanValue(${1:Object val})$0",
            "hasClass(Object element, String className)\tBoolean": "hasClass(${1:Object element}, ${2:String className})$0",
            "isArray(Object obj)\tBoolean": "isArray(${1:Object obj})$0",
            "isEmpty(Object obj)\tBoolean": "isEmpty(${1:Object obj})$0",
            "isObject(Object obj)\tBoolean": "isObject(${1:Object obj})$0",
            "isUndefined(Object obj)\tBoolean": "isUndefined(${1:Object obj})$0",
            "isUndefinedOrNull(Object obj)\tBoolean": "isUndefinedOrNull(${1:Object obj})$0",
            "removeClass(Object element, String newClass)\tvoid": "removeClass(${1:Object element}, ${2:String newClass})$0",
            "toggleClass(Object element, String className)\tvoid": "toggleClass(${1:Object element}, ${2:String className})$0"
        }
    },

    "localizationService": {
        "sub_class": True,
        "type": "Sub Class",
        "methods": {
            "UTCToWallTime(Date date, String timezone, function callback)\tvoid": "UTCToWallTime(${1:Date date}, ${2:String timezone}, ${3:function callback})$0",
            "WallTimeToUTC(Date date, String timezone, function callback)\tvoid": "WallTimeToUTC(${1:Date date}, ${2:String timezone}, ${3:function callback})$0",
            "displayDuration(Duration d, Boolean noSuffix)\tString": "displayDuration(${1:Duration d}, ${2:Boolean noSuffix})$0",
            "displayDurationInDays(Duration d)\tNumber": "displayDurationInDays(${1:Duration d})$0",
            "displayDurationInHours(Duration d)\tNumber": "displayDurationInHours(${1:Duration d})$0",
            "displayDurationInMilliseconds(Duration d)\tNumber": "displayDurationInMilliseconds(${1:Duration d})$0",
            "displayDurationInMinutes(Duration d)\tNumber": "displayDurationInMinutes(${1:Duration d})$0",
            "displayDurationInMonths(Duration d)\tNumber": "displayDurationInMonths(${1:Duration d})$0",
            "displayDurationInSeconds(Duration d)\tNumber": "displayDurationInSeconds(${1:Duration d})$0",
            "duration(Number | Object num, String unit)\tObject": "duration(${1:Number | Object num}, ${2:String unit})$0",
            "endOf(String | Number | Date date, String unit)\tDate": "endOf(${1:String | Number | Date date}, ${2:String unit})$0",
            "formatCurrency(Number number)\tNumber": "formatCurrency(${1:Number number})$0",
            "formatDate(String | Number | Date date, String formatString, String locale)\tString": "formatDate(${1:String | Number | Date date}, ${2:String formatString}, ${3:String locale})$0",
            "formatDateTime(String | Number | Date date, String formatString, String locale)\tString": "formatDateTime(${1:String | Number | Date date}, ${2:String formatString}, ${3:String locale})$0",
            "formatDateTimeUTC(String | Number | Date date, String formatString, String locale)\tString": "formatDateTimeUTC(${1:String | Number | Date date}, ${2:String formatString}, ${3:String locale})$0",
            "formatDateUTC(String | Number | Date date, String formatString, String locale)\tString": "formatDateUTC(${1:String | Number | Date date}, ${2:String formatString}, ${3:String locale})$0",
            "formatNumber(Number number)\tNumber": "formatNumber(${1:Number number})$0",
            "formatPercent(Number number)\tNumber": "formatPercent(${1:Number number})$0",
            "formatTime(String | Number | Date date, String formatString, String locale)\tString": "formatTime(${1:String | Number | Date date}, ${2:String formatString}, ${3:String locale})$0",
            "formatTimeUTC(String | Number | Date date, String formatString, String locale)\tString": "formatTimeUTC(${1:String | Number | Date date}, ${2:String formatString}, ${3:String locale})$0",
            "getDateStringBasedOnTimezone(String timezone, Date dateObj, function callback)\tvoid": "getDateStringBasedOnTimezone(${1:String timezone}, ${2:Date dateObjfunction callback})$0",
            "getDaysInDuration(Duration d)\tNumber": "getDaysInDuration(${1:Duration d})$0",
            "getDefaultCurrencyFormat()\tNumber": "getDefaultCurrencyFormat()$0",
            "getDefaultNumberFormat()\tNumber": "getDefaultNumberFormat()$0",
            "getDefaultPercentFormat()\tNumber": "getDefaultPercentFormat()$0",
            "getHoursInDuration(Duration d)\tNumber": "getHoursInDuration(${1:Duration d})$0",
            "getLocalizedDateTimeLabels()\tObject": "getLocalizedDateTimeLabels()$0",
            "getMillisecondsInDuration(Duration d)\tNumber": "getMillisecondsInDuration(${1:Duration d})$0",
            "getMinutesInDuration(Duration d)\tNumber": "getMinutesInDuration(${1:Duration d})$0",
            "getMonthsInDuration(Duration d)\tNumber": "getMonthsInDuration(${1:Duration d})$0",
            "getNumberFormat(String formatString symbols)\tNumber": "getNumberFormat(${1:String formatString symbols})$0",
            "getSecondsInDuration(Duration d)\tNumber": "getSecondsInDuration(${1:Duration d})$0",
            "getToday(String timezone, function callback)\tString": "getToday(${1:String timezone}, ${2:function callback})$0",
            "getYearsInDuration(Duration d)\tNumber": "getYearsInDuration(${1:Duration d})$0",
            "isAfter(String | Number | Date date1, String | Number | Date date2, String unit)\tBoolean": "isAfter(${1:String | Number | Date date1}, ${2:String | Number | Date date2}, ${3:String unit})$0",
            "isBefore(String | Number | Date date1, String | Number | Date date2, String unit)\tBoolean": "isBefore(${1:String | Number | Date date1}, ${2:String | Number | Date date2}, ${3:String unit})$0",
            "isBetween(String | Number | Date date, String | Number | Date fromDate, String | Number | Date toDate, String unit)\tBoolean: unit})$0": "isBetween(${1:String | Number | Date date}, ${2:String | Number | Date fromDate}, ${3:String | Number | Date toDate}, ${4:String unit})\tBoolean: unit})$0",
            "isPeriodTimeView(String pattern)\tBoolean": "isPeriodTimeView(${1:String pattern})$0",
            "isSame(String | Number | Date date1, String | Number | Date date2, String unit)\tBoolean": "isSame(${1:String | Number | Date date1}, ${2:String | Number | Date date2}, ${3:String unit})$0",
            "parseDateTime(String dateTimeString, String parseFormat, String locale, Boolean strictParsing)\tDate": "parseDateTime(${1:String dateTimeString}, ${2:String parseFormat}, ${3:String locale}, ${4:Boolean strictParsing})$0",
            "parseDateTimeISO8601(String dateTimeString)\tDate": "parseDateTimeISO8601(${1:String dateTimeString})$0",
            "parseDateTimeUTC(String dateTimeString, String parseFormat, String locale, Boolean strictParsing)\tDate": "parseDateTimeUTC(${1:String dateTimeString}, ${2:String parseFormat}, ${3:String locale}, ${4:Boolean strictParsing})$0",
            "startOf(String | Number | Date date, String unit)\tDate": "startOf(${1:String | Number | Date date}, ${2:String unit})$0",
            "toISOString(Date date)\tString": "toISOString(${1:Date date})$0",
            "translateFromLocalizedDigits(String input)\tString": "translateFromLocalizedDigits(${1:String input})$0",
            "translateFromOtherCalendar(Date date)\tDate": "translateFromOtherCalendar(${1:Date date})$0",
            "translateToLocalizedDigits(String input)\tString": "translateToLocalizedDigits(${1:String input})$0",
            "translateToOtherCalendar(Date date)\tDate": "translateToOtherCalendar(${1:Date date})$0"
        }
    },

    "action": {
        "type": "Customized Lib",
        "methods": {
            "getError()\tObject[]": "getError()$0",
            "getName()\tString": "getName()$0",
            "getParam(String name)\tObject": "getParam(${1:String name})$0",
            "getParams()\tObject": "getParams()$0",
            "getReturnValue()\tvoid": "getReturnValue()$0",
            "getState()\tString": "getState()$0",
            "isBackground()\tvoid": "isBackground()$0",
            "setAbortable()\tvoid": "setAbortable()$0",
            "setBackground()\tvoid": "setBackground()$0",
            "setCallback(Object scope, function callback, String name)\tvoid": "setCallback(${1:Object scope}, ${2:function callback}, ${3:String name})$0",
            "setParam(String key, Object value)\tvoid": "setParam(${1:String key}, ${2:Object value})$0",
            "setParams(Object config)\tvoid": "setParams(${1:Object config})$0",
            "setStorable(Object config)\tvoid": "setStorable(${1:Object config})$0"
        }
    },

    "response": {
        "type": "Customized Lib",
        "methods": {
            "getState()\tString": "getState()",
            "getReturnValue()\tObject": "getReturnValue()",
            "getError()\tArray": "getError()"
        }
    },


    "component": {
        "type": "Customized Lib",
        "methods": {
            "addEventHandler(String event, function handler, String phase, Boolean includeFacets)\tvoid": "addEventHandler(${1:String event}, ${2:function handler}, ${3:String phase}, ${4:Boolean includeFacetse})$0",
            "addValueHandler(Object config)\tvoid": "addValueHandler(${1:Object config})$0",
            "addValueProvider(String key, Object valueProvider)\tvoid": "addValueProvider(${1:String key}, ${2:Object valueProvider})$0",
            "autoDestroy(Boolean destroy)\tvoid": "autoDestroy(Boolean destroy)$0",
            "clearReference(String key)\tvoid": "clearReference(${1:String key})$0",
            "destroy()\tvoid": "destroy()$0",
            "find(String | Object name)\tvoid": "find(${1:String | Object} ${2:name})$0",
            "get(String key)\tvoid": "get(${1:String key})$0",
            "getConcreteComponent()\tvoid": "getConcreteComponent()$0",
            "getElement()\tvoid": "getElement()$0",
            "getElements()\tvoid": "getElements()$0",
            "getEvent(String name)\tvoid": "getEvent(${1:String name})$0",
            "getGlobalId()\tvoid": "getGlobalId()$0",
            "getLocalId()\tvoid": "getLocalId()$0",
            "getName()\tvoid": "getName()$0",
            "getReference(String key)\tPropertyReferenceValue": "getReference(${1:String key})$0",
            "getSuper()\tvoid": "getSuper()$0",
            "getType()\tvoid": "getType()$0",
            "getVersion()\tvoid": "getVersion()$0",
            "isConcrete()\tvoid": "isConcrete()$0",
            "isInstanceOf(String name)\tBoolean": "isInstanceOf(${1:String name})$0",
            "isValid()\tvoid": "isValid()$0",
            "removeEventHandler(String event, function handler, String phase)\tvoid": "removeEventHandler(${1:String event}, ${2:function handler}, ${3:String phase})$0",
            "set(String key, Object value)\tvoid": "set(${1:String key}, ${2:Object value})$0"
        }
    },

    "cmp": {
        "type": "Customized Lib",
        "methods": {
            "addEventHandler(String event, function handler, String phase, Boolean includeFacets)\tvoid": "addEventHandler(${1:String event}, ${2:function handler}, ${3:String phase}, ${4:Boolean includeFacetse})$0",
            "addValueHandler(Object config)\tvoid": "addValueHandler(${1:Object config})$0",
            "addValueProvider(String key, Object valueProvider)\tvoid": "addValueProvider(${1:String key}, ${2:Object valueProvider})$0",
            "autoDestroy(Boolean destroy)\tvoid": "autoDestroy(Boolean destroy)$0",
            "clearReference(String key)\tvoid": "clearReference(${1:String key})$0",
            "destroy()\tvoid": "destroy()$0",
            "find(String | Object name)\tvoid": "find(${1:String | Object} ${2:name})$0",
            "get(String key)\tvoid": "get(${1:String key})$0",
            "getConcreteComponent()\tvoid": "getConcreteComponent()$0",
            "getElement()\tvoid": "getElement()$0",
            "getElements()\tvoid": "getElements()$0",
            "getEvent(String name)\tvoid": "getEvent(${1:String name})$0",
            "getGlobalId()\tvoid": "getGlobalId()$0",
            "getLocalId()\tvoid": "getLocalId()$0",
            "getName()\tvoid": "getName()$0",
            "getReference(String key)\tPropertyReferenceValue": "getReference(${1:String key})$0",
            "getSuper()\tvoid": "getSuper()$0",
            "getType()\tvoid": "getType()$0",
            "getVersion()\tvoid": "getVersion()$0",
            "isConcrete()\tvoid": "isConcrete()$0",
            "isInstanceOf(String name)\tBoolean": "isInstanceOf(${1:String name})$0",
            "isValid()\tvoid": "isValid()$0",
            "removeEventHandler(String event, function handler, String phase)\tvoid": "removeEventHandler(${1:String event}, ${2:function handler}, ${3:String phase})$0",
            "set(String key, Object value)\tvoid": "set(${1:String key}, ${2:Object value})$0"
        }
    },

    "Browser": {
        "type": "Standard Class",
        "prefix": "$",
        "methods": {
            "formFactor()\tBoolean": "formFactor()$0",
            "isAndroid()\tBoolean": "isAndroid()$0",
            "isIOS()\tBoolean": "isIOS()$0",
            "isIPad()\tBoolean": "isIPad()$0",
            "isIPhone()\tBoolean": "isIPhone()$0",
            "isPhone()\tBoolean": "isPhone()$0",
            "isTablet()\tBoolean": "isTablet()$0",
            "isWindowsPhone()\tBoolean": "isWindowsPhone()$0"
        }
    },

    "console": {
        "type": "Standard Class",
        "methods": {
            "log()\tvoid": "log($1)$0",
            "error()\tvoid": "error($1)$0",
            "info()\tvoid": "info($1)$0",
            "warn()\tvoid": "warn($1)$0"
        }
    },

    "event": {
        "type": "Standard Class",
        "methods": {
            "fire(Object params)\tvoid": "fire(${1:Object params})$0",
            "getEventType()\tString": "getEventType()$0",
            "getName()\tString": "getName()$0",
            "getParam(String name)\tObject": "getParam(${1:String name})$0",
            "getParams()\tObject": "getParams()$0",
            "getPhase()\tvoid": "getPhase()$0",
            "getSource()\tObject": "getSource()$0",
            "getType()\tString": "getType()$0",
            "pause()\tvoid": "pause()$0",
            "preventDefault()\tvoid": "preventDefault()$0",
            "preventDefault()\tvoid": "preventDefault()$0",
            "setParam(String key, Object value)\tvoid": "setParam(${1:String key}, ${2:Object value})$0",
            "setParams(Object config)\tvoid": "setParams(${1:Object config})$0",
            "stopPropagation()\tvoid": "stopPropagation()$0"
        }
    },

    "Locale": {
        "type": "Standard Class",
        "prefix": "$",
        "properties": [
            "country",
            "currency",
            "currencyCode",
            "decimal",
            "firstDayOfWeek",
            "grouping",
            "isEasternNameStyle",
            "labelForToday",
            "language",
            "langLocale",
            "nameOfMonths",
            "nameOfWeekdays",
            "timezone",
            "userLocaleCountry",
            "userLocaleLang",
            "variant"
        ]
    },

    "Label": {
        "metaObject": "CustomLabel",
        "type": "Standard Class",
        "prefix": "$"
    },

    "Resource": {
        "metaObject": "StaticResource",
        "type": "Standard Class",
        "prefix": "$"
    },

    "v": {
        "type": "Component View"
    }
}

# Attributes which type is ApexPages.PageReference
page_reference_attrs = [
    "page",
    "template",
    "pageName",
    "finishLocation"
]

component_interfaces = [
    "aura:rootComponent",
    "clients:availableForMailAppAppPage",
    "clients:hasEventContext",
    "clients:hasItemContext",
    "flexipage:availableForAllPageTypes",
    "flexipage:availableForRecordHome",
    "forceCommunity:availableForAllPageTypes",
    "forceCommunity:layout",
    "forceCommunity:profileMenuInterface",
    "forceCommunity:searchInterface",
    "forceCommunity:themeLayout",
    "force:appHostable",
    "force:hasRecordId",
    "force:hasSObjectName",
    "force:lightningQuickActionWithoutHeader",
    "force:lightningQuickAction",
    "lightning:actionOverride",
    "lightning:appHomeTemplate",
    "lightning:availableForChatterExtensionComposer",
    "lightning:availableForChatterExtensionRenderer",
    "lightning:availableForFlowActions",
    "lightning:availableForFlowScreens",
    "lightning:backgroundUtilityItem",
    "lightning:hasPageReference",
    "lightning:homeTemplate",
    "lightning:isUrlAddressable",   
    "lightning:recordHomeTemplate",
    "lightning:utilityItem",
    # "lightning:prechatUI"
    "lightningcommunity:allowInRelaxedCSP",
    "lightningsnapin:minimizedUI",
    "lightningsnapin:prechatUI",
    "ltng:allowGuestAccess"
]

icon_names = [
    "action:add_contact",
    "action:add_file",
    "action:add_photo_video",
    "action:add_relationship",
    "action:announcement",
    "action:apex",
    "action:approval",
    "action:back",
    "action:call",
    "action:canvas",
    "action:change_owner",
    "action:change_record_type",
    "action:check",
    "action:clone",
    "action:close",
    "action:defer",
    "action:delete",
    "action:description",
    "action:dial_in",
    "action:download",
    "action:edit_groups",
    "action:edit_relationship",
    "action:edit",
    "action:email",
    "action:fallback",
    "action:filter",
    "action:flow",
    "action:follow",
    "action:following",
    "action:freeze_user",
    "action:goal",
    "action:google_news",
    "action:info",
    "action:join_group",
    "action:lead_convert",
    "action:leave_group",
    "action:log_a_call",
    "action:log_event",
    "action:manage_perm_sets",
    "action:map",
    "action:more",
    "action:new_account",
    "action:new_campaign",
    "action:new_case",
    "action:new_child_case",
    "action:new_contact",
    "action:new_event",
    "action:new_group",
    "action:new_lead",
    "action:new_note",
    "action:new_notebook",
    "action:new_opportunity",
    "action:new_person_account",
    "action:new_task",
    "action:new",
    "action:password_unlock",
    "action:preview",
    "action:priority",
    "action:question_post_action",
    "action:quote",
    "action:recall",
    "action:record",
    "action:refresh",
    "action:reject",
    "action:remove_relationship",
    "action:remove",
    "action:reset_password",
    "action:share_file",
    "action:share_link",
    "action:share_poll",
    "action:share_post",
    "action:share_thanks",
    "action:share",
    "action:sort",
    "action:submit_for_approval",
    "action:update_status",
    "action:update",
    "action:upload",
    "action:user_activation",
    "action:user",
    "action:view_relationship",
    "action:web_link",
    "custom:custom1",
    "custom:custom2",
    "custom:custom3",
    "custom:custom4",
    "custom:custom5",
    "custom:custom6",
    "custom:custom7",
    "custom:custom8",
    "custom:custom9",
    "custom:custom10",
    "custom:custom11",
    "custom:custom12",
    "custom:custom13",
    "custom:custom14",
    "custom:custom15",
    "custom:custom16",
    "custom:custom17",
    "custom:custom18",
    "custom:custom19",
    "custom:custom20",
    "custom:custom21",
    "custom:custom22",
    "custom:custom23",
    "custom:custom24",
    "custom:custom25",
    "custom:custom26",
    "custom:custom27",
    "custom:custom28",
    "custom:custom29",
    "custom:custom30",
    "custom:custom31",
    "custom:custom32",
    "custom:custom33",
    "custom:custom34",
    "custom:custom35",
    "custom:custom36",
    "custom:custom37",
    "custom:custom38",
    "custom:custom39",
    "custom:custom40",
    "custom:custom41",
    "custom:custom42",
    "custom:custom43",
    "custom:custom44",
    "custom:custom45",
    "custom:custom46",
    "custom:custom47",
    "custom:custom48",
    "custom:custom49",
    "custom:custom50",
    "custom:custom51",
    "custom:custom52",
    "custom:custom53",
    "custom:custom54",
    "custom:custom55",
    "custom:custom56",
    "custom:custom57",
    "custom:custom58",
    "custom:custom59",
    "custom:custom60",
    "custom:custom61",
    "custom:custom62",
    "custom:custom63",
    "custom:custom64",
    "custom:custom65",
    "custom:custom66",
    "custom:custom67",
    "custom:custom68",
    "custom:custom69",
    "custom:custom70",
    "custom:custom71",
    "custom:custom72",
    "custom:custom73",
    "custom:custom74",
    "custom:custom75",
    "custom:custom76",
    "custom:custom77",
    "custom:custom78",
    "custom:custom79",
    "custom:custom80",
    "custom:custom81",
    "custom:custom82",
    "custom:custom83",
    "custom:custom84",
    "custom:custom85",
    "custom:custom86",
    "custom:custom87",
    "custom:custom88",
    "custom:custom89",
    "custom:custom90",
    "custom:custom91",
    "custom:custom92",
    "custom:custom93",
    "custom:custom94",
    "custom:custom95",
    "custom:custom96",
    "custom:custom97",
    "custom:custom98",
    "custom:custom99",
    "custom:custom100",
    "custom:custom101",
    "custom:custom102",
    "custom:custom103",
    "custom:custom104",
    "custom:custom105",
    "custom:custom106",
    "custom:custom107",
    "custom:custom108",
    "custom:custom109",
    "custom:custom110",
    "custom:custom111",
    "custom:custom112",
    "custom:custom113",
    "doctype:ai",
    "doctype:attachment",
    "doctype:audio",
    "doctype:box_notes",
    "doctype:csv",
    "doctype:eps",
    "doctype:excel",
    "doctype:exe",
    "doctype:flash",
    "doctype:folder",
    "doctype:gdoc",
    "doctype:gdocs",
    "doctype:gform",
    "doctype:gpres",
    "doctype:gsheet",
    "doctype:html",
    "doctype:image",
    "doctype:keynote",
    "doctype:library_folder",
    "doctype:link",
    "doctype:mp4",
    "doctype:overlay",
    "doctype:pack",
    "doctype:pages",
    "doctype:pdf",
    "doctype:ppt",
    "doctype:psd",
    "doctype:quip_doc",
    "doctype:quip_sheet",
    "doctype:rtf",
    "doctype:slide",
    "doctype:stypi",
    "doctype:txt",
    "doctype:unknown",
    "doctype:video",
    "doctype:visio",
    "doctype:webex",
    "doctype:word",
    "doctype:xml",
    "doctype:zip",
    "standard:account",
    "standard:address",
    "standard:announcement",
    "standard:answer_best",
    "standard:answer_private",
    "standard:answer_public",
    "standard:approval",
    "standard:apps_admin",
    "standard:apps",
    "standard:article",
    "standard:asset_relationship",
    "standard:assigned_resource",
    "standard:avatar_loading",
    "standard:avatar",
    "standard:bot",
    "standard:business_hours",
    "standard:calibration",
    "standard:call_history",
    "standard:call",
    "standard:campaign_members",
    "standard:campaign",
    "standard:canvas",
    "standard:carousel",
    "standard:case_change_status",
    "standard:case_comment",
    "standard:case_email",
    "standard:case_log_a_call",
    "standard:case_milestone",
    "standard:case_transcript",
    "standard:case",
    "standard:channel_program_history",
    "standard:channel_program_levels",
    "standard:channel_program_members",
    "standard:channel_programs",
    "standard:client",
    "standard:cms",
    "standard:coaching",
    "standard:connected_apps",
    "standard:contact_list",
    "standard:contact",
    "standard:contract_line_item",
    "standard:contract",
    "standard:custom_notification",
    "standard:custom",
    "standard:customers",
    "standard:dashboard",
    "standard:datadotcom",
    "standard:default",
    "standard:document",
    "standard:drafts",
    "standard:email_chatter",
    "standard:email",
    "standard:empty",
    "standard:endorsement",
    "standard:entitlement_process",
    "standard:entitlement_template",
    "standard:entitlement",
    "standard:entity_milestone",
    "standard:entity",
    "standard:environment_hub",
    "standard:event",
    "standard:feed",
    "standard:feedback",
    "standard:file",
    "standard:flow",
    "standard:folder",
    "standard:forecasts",
    "standard:generic_loading",
    "standard:goals",
    "standard:group_loading",
    "standard:groups",
    "standard:hierarchy",
    "standard:home",
    "standard:household",
    "standard:insights",
    "standard:investment_account",
    "standard:iot_orchestrations",
    "standard:lead_insights",
    "standard:lead_list",
    "standard:lead",
    "standard:link",
    "standard:list_email",
    "standard:live_chat",
    "standard:location",
    "standard:log_a_call",
    "standard:macros",
    "standard:maintenance_asset",
    "standard:maintenance_plan",
    "standard:marketing_actions",
    "standard:merge",
    "standard:messaging_conversation",
    "standard:messaging_session",
    "standard:messaging_user",
    "standard:metrics",
    "standard:news",
    "standard:note",
    "standard:omni_supervisor",
    "standard:operating_hours",
    "standard:opportunity_splits",
    "standard:opportunity",
    "standard:orders",
    "standard:partner_fund_allocation",
    "standard:partner_fund_claim",
    "standard:partner_fund_request",
    "standard:partner_marketing_budget",
    "standard:partners",
    "standard:past_chat",
    "standard:people",
    "standard:performance",
    "standard:person_account",
    "standard:photo",
    "standard:poll",
    "standard:portal",
    "standard:post",
    "standard:pricebook",
    "standard:process",
    "standard:product_consumed",
    "standard:product_item_transaction",
    "standard:product_item",
    "standard:product_request_line_item",
    "standard:product_request",
    "standard:product_required",
    "standard:product_transfer",
    "standard:product",
    "standard:question_best",
    "standard:question_feed",
    "standard:quick_text",
    "standard:quip_sheet",
    "standard:quip",
    "standard:quotes",
    "standard:recent",
    "standard:record",
    "standard:related_list",
    "standard:relationship",
    "standard:report",
    "standard:resource_absence",
    "standard:resource_capacity",
    "standard:resource_preference",
    "standard:resource_skill",
    "standard:return_order_line_item",
    "standard:return_order",
    "standard:reward",
    "standard:rtc_presence",
    "standard:sales_path",
    "standard:scan_card",
    "standard:search",
    "standard:service_appointment",
    "standard:service_contract",
    "standard:service_crew_member",
    "standard:service_crew",
    "standard:service_report",
    "standard:service_resource",
    "standard:service_territory_location",
    "standard:service_territory_member",
    "standard:service_territory",
    "standard:shipment",
    "standard:skill_entity",
    "standard:skill_requirement",
    "standard:skill",
    "standard:social",
    "standard:solution",
    "standard:sossession",
    "standard:survey",
    "standard:task",
    "standard:task2",
    "standard:team_member",
    "standard:template",
    "standard:thanks_loading",
    "standard:thanks",
    "standard:timesheet_entry",
    "standard:timesheet",
    "standard:timeslot",
    "standard:today",
    "standard:topic",
    "standard:topic2",
    "standard:unmatched",
    "standard:user",
    "standard:work_order_item",
    "standard:work_order",
    "standard:work_type",
    "utility:activity",
    "utility:ad_set",
    "utility:add",
    "utility:adduser",
    "utility:anchor",
    "utility:animal_and_nature",
    "utility:announcement",
    "utility:answer",
    "utility:answered_twice",
    "utility:apex",
    "utility:approval",
    "utility:apps",
    "utility:arrowdown",
    "utility:arrowup",
    "utility:attach",
    "utility:automate",
    "utility:back",
    "utility:ban",
    "utility:block_visitor",
    "utility:bold",
    "utility:bookmark",
    "utility:breadcrumbs",
    "utility:broadcast",
    "utility:brush",
    "utility:bucket",
    "utility:builder",
    "utility:call",
    "utility:campaign",
    "utility:cancel_file_request",
    "utility:cancel_transfer",
    "utility:capslock",
    "utility:case",
    "utility:cases",
    "utility:center_align_text",
    "utility:change_owner",
    "utility:change_record_type",
    "utility:chart",
    "utility:chat",
    "utility:check",
    "utility:checkin",
    "utility:chevrondown",
    "utility:chevronleft",
    "utility:chevronright",
    "utility:chevronup",
    "utility:classic_interface",
    "utility:clear",
    "utility:clock",
    "utility:close",
    "utility:collapse_all",
    "utility:color_swatch",
    "utility:comments",
    "utility:company",
    "utility:connected_apps",
    "utility:contract_alt",
    "utility:contract",
    "utility:copy_to_clipboard",
    "utility:copy",
    "utility:crossfilter",
    "utility:custom_apps",
    "utility:cut",
    "utility:dash",
    "utility:database",
    "utility:datadotcom",
    "utility:dayview",
    "utility:delete",
    "utility:deprecate",
    "utility:description",
    "utility:desktop_console",
    "utility:desktop",
    "utility:dislike",
    "utility:dock_panel",
    "utility:down",
    "utility:download",
    "utility:edit_form",
    "utility:edit",
    "utility:email",
    "utility:emoji",
    "utility:end_call",
    "utility:end_chat",
    "utility:erect_window",
    "utility:error",
    "utility:event",
    "utility:expand_all",
    "utility:expand_alt",
    "utility:expand",
    "utility:fallback",
    "utility:favorite",
    "utility:feed",
    "utility:file",
    "utility:filter",
    "utility:filterList",
    "utility:flow",
    "utility:food_and_drink",
    "utility:forward",
    "utility:frozen",
    "utility:full_width_view",
    "utility:graph",
    "utility:groups",
    "utility:help",
    "utility:hide",
    "utility:hierarchy",
    "utility:home",
    "utility:identity",
    "utility:image",
    "utility:inbox",
    "utility:info_alt",
    "utility:info",
    "utility:insert_tag_field",
    "utility:insert_template",
    "utility:internal_share",
    "utility:italic",
    "utility:jump_to_bottom",
    "utility:jump_to_top",
    "utility:justify_text",
    "utility:kanban",
    "utility:keyboard_dismiss",
    "utility:knowledge_base",
    "utility:layers",
    "utility:layout",
    "utility:left_align_text",
    "utility:left",
    "utility:level_up",
    "utility:light_bulb",
    "utility:like",
    "utility:link",
    "utility:list",
    "utility:listen",
    "utility:location",
    "utility:lock",
    "utility:log_a_call",
    "utility:logout",
    "utility:lower_flag",
    "utility:macros",
    "utility:magicwand",
    "utility:mark_all_as_read",
    "utility:matrix",
    "utility:merge_field",
    "utility:merge",
    "utility:metrics",
    "utility:minimize_window",
    "utility:missed_call",
    "utility:moneybag",
    "utility:monthlyview",
    "utility:move",
    "utility:muted",
    "utility:new_direct_message",
    "utility:new_window",
    "utility:new",
    "utility:news",
    "utility:note",
    "utility:notebook",
    "utility:notification",
    "utility:office365",
    "utility:offline_cached",
    "utility:offline",
    "utility:omni_channel",
    "utility:open_folder",
    "utility:open",
    "utility:opened_folder",
    "utility:outbound_call",
    "utility:overflow",
    "utility:package_org_beta",
    "utility:package_org",
    "utility:package",
    "utility:page",
    "utility:palette",
    "utility:paste",
    "utility:pause",
    "utility:people",
    "utility:phone_landscape",
    "utility:phone_portrait",
    "utility:photo",
    "utility:picklist",
    "utility:pin",
    "utility:pinned",
    "utility:power",
    "utility:preview",
    "utility:priority",
    "utility:privately_shared",
    "utility:process",
    "utility:push",
    "utility:puzzle",
    "utility:question_mark",
    "utility:question",
    "utility:questions_and_answers",
    "utility:quick_text",
    "utility:quotation_marks",
    "utility:rating",
    "utility:record_create",
    "utility:record",
    "utility:redo",
    "utility:refresh",
    "utility:relate",
    "utility:reminder",
    "utility:remove_formatting",
    "utility:remove_link",
    "utility:replace",
    "utility:reply_all",
    "utility:reply",
    "utility:reset_password",
    "utility:resource_absence",
    "utility:resource_capacity",
    "utility:resource_territory",
    "utility:retweet",
    "utility:richtextbulletedlist",
    "utility:richtextindent",
    "utility:richtextnumberedlist",
    "utility:richtextoutdent",
    "utility:right_align_text",
    "utility:right",
    "utility:rotate",
    "utility:rows",
    "utility:rules",
    "utility:salesforce1",
    "utility:save",
    "utility:search",
    "utility:sentiment_negative",
    "utility:sentiment_neutral",
    "utility:settings",
    "utility:setup_assistant_guide",
    "utility:setup",
    "utility:share_file",
    "utility:share_mobile",
    "utility:share_post",
    "utility:share",
    "utility:shield",
    "utility:shopping_bag",
    "utility:side_list",
    "utility:signpost",
    "utility:smiley_and_people",
    "utility:sms",
    "utility:snippet",
    "utility:socialshare",
    "utility:sort",
    "utility:spinner",
    "utility:standard_objects",
    "utility:stop",
    "utility:strikethrough",
    "utility:success",
    "utility:summary",
    "utility:summarydetail",
    "utility:survey",
    "utility:switch",
    "utility:symbols",
    "utility:sync",
    "utility:table",
    "utility:tablet_landscape",
    "utility:tablet_portrait",
    "utility:tabset",
    "utility:task",
    "utility:text_background_color",
    "utility:text_color",
    "utility:threedots_vertical",
    "utility:threedots",
    "utility:thunder",
    "utility:tile_card_list",
    "utility:topic",
    "utility:touch_action",
    "utility:trail",
    "utility:travel_and_places",
    "utility:trending",
    "utility:turn_off_notifications",
    "utility:type_tool",
    "utility:undelete",
    "utility:undeprecate",
    "utility:underline",
    "utility:undo",
    "utility:unlock",
    "utility:unmuted",
    "utility:up",
    "utility:upload",
    "utility:user_role",
    "utility:user",
    "utility:video",
    "utility:voicemail_drop",
    "utility:volume_high",
    "utility:volume_low",
    "utility:volume_off",
    "utility:warning",
    "utility:weeklyview",
    "utility:wifi",
    "utility:work_order_type",
    "utility:world",
    "utility:yubi_key",
    "utility:zoomin",
    "utility:zoomout"
]

timezones = [
    "Pacific/Kiritimati",
    "Pacific/Enderbury",
    "Pacific/Tongatapu",
    "Pacific/Chatham",
    "Asia/Kamchatka",
    "Pacific/Auckland",
    "Pacific/Fiji",
    "Pacific/Guadalcanal",
    "Pacific/Norfolk",
    "Australia/Lord_Howe",
    "Australia/Brisbane",
    "Australia/Sydney",
    "Australia/Adelaide",
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
    "Asia/Tehran",
    "Asia/Baku",
    "Asia/Dubai",
    "Asia/Tbilisi",
    "Asia/Yerevan",
    "Africa/Nairobi",
    "Asia/Baghdad",
    "Asia/Beirut",
    "Asia/Jerusalem",
    "Asia/Kuwait",
    "Asia/Riyadh",
    "Europe/Athens",
    "Europe/Bucharest",
    "Europe/Helsinki",
    "Europe/Istanbul",
    "Europe/Minsk",
    "Europe/Moscow",
    "Africa/Cairo",
    "Africa/Johannesburg",
    "Europe/Amsterdam",
    "Europe/Berlin",
    "Europe/Brussels",
    "Europe/Paris",
    "Europe/Prague",
    "Europe/Rome",
    "Africa/Algiers",
    "Europe/Dublin",
    "Europe/Lisbon",
    "Europe/London",
    "Africa/Casablanca",
    "America/Scoresbysund",
    "Atlantic/Azores",
    "GMT",
    "Atlantic/Cape_Verde",
    "Atlantic/South_Georgia",
    "America/St_Johns",
    "America/Argentina/Buenos_Aires",
    "America/Halifax",
    "America/Sao_Paulo",
    "Atlantic/Bermuda",
    "America/Caracas",
    "America/Indiana/Indianapolis",
    "America/New_York",
    "America/Puerto_Rico",
    "America/Santiago",
    "America/Bogota",
    "America/Chicago",
    "America/Lima",
    "America/Mexico_City",
    "America/Panama",
    "America/Denver",
    "America/El_Salvador",
    "America/Mazatlan",
    "America/Los_Angeles",
    "America/Phoenix",
    "America/Tijuana",
    "America/Anchorage",
    "Pacific/Pitcairn",
    "America/Adak",
    "Pacific/Gambier",
    "Pacific/Marquesas",
    "Pacific/Honolulu",
    "Pacific/Niue",
    "Pacific/Pago_Pago"
]

html_global_methods = [
    "onabort", "onautocomplete", "onautocompleteerror", "onauxclick", "onblur",
    "oncancel", "oncanplay", "oncanplaythrough", "onchange", "onclick",
    "onclose", "oncontextmenu", "oncuechange", "ondblclick", "ondrag",
    "ondragend", "ondragenter", "ondragexit", "ondragleave", "ondragover",
    "ondragstart", "ondrop", "ondurationchange", "onemptied", "onended",
    "onerror", "onfocus", "oninput", "oninvalid", "onkeydown",
    "onkeypress", "onkeyup", "onload", "onloadeddata", "onloadedmetadata",
    "onloadstart", "onmousedown", "onmouseenter", "onmouseleave",
    "onmousemove", "onmouseout", "onmouseover", "onmouseup",
    "onmousewheel", "onpause", "onplay", "onplaying", "onprogress",
    "onratechange", "onreset", "onresize", "onscroll", "onseeked",
    "onseeking", "onselect", "onshow", "onsort", "onstalled", "onsubmit",
    "onsuspend", "ontimeupdate", "ontoggle", "onvolumechange", "onwaiting"
]

# ["analytics", "aura", "force", "forceChatter", "forceCommunity", "lightning", "ltng", "ui", "wave"]
tag_defs = {
    "sfdc:sobjects": {
        "attribs": {},
        "simple": False,
        "type": "aura"
    },
    "sfdc:sobject": {
        "attribs": {},
        "simple": False,
        "type": "aura"
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
                "type": "Picklist",
                "values": [
                    "${1:Customize}",
                    "force:slds",
                    "ltng:outApp"
                ]
            },
            "extensible": {
                "type": "Boolean",
                "description": "Indicates whether the app is extensible by another app. Defaults to false."
            },
            "template": {
                "type": "Component"
            },
            "tokens": {
                "type": "String"
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
                    "private"
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
                    "Method",
                    "Object",
                    "String[]",
                    "Integer[]",
                    "Map",
                    "List",
                    "Set",
                    "Aura.Action",
                    "Aura.Component",
                    "Aura.Component[]"
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
                "type": "Picklist",
                "values": [
                    "aura:template"
                ]
            },
            "implements": {
                "type": "Picklist",
                "values": component_interfaces
            },
            "isTemplate": {
                "type": "Boolean"
            },
            "template": {
                "type": "Component"
            },
            "extensible": {
                "type": "Boolean",
                "description": "Set to true if the component can be extended. The default is false."
            },
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
                    "EVENT",
                    "INTERFACE"
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
                    "aura:valueRender",
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

    "design:attribute": {
        "attribs": {
            "datasource": {
                "description": "Renders a field as a picklist, with static values. Only supported for String attributes.",
                "type": "String"
            },
            "default": {
                "description": "Sets a default value on an attribute in a design resource.",
                "type": "String"
            },
            "description": {
                "description": "Displays as an i-bubble for the attribute in the tool.",
                "type": "String"
            },
            "label": {
                "description": "Attribute label that displays in the tool.",
                "type": "String"
            },
            "max": {
                "description": "If the attribute is an Integer, this sets its maximum allowed value. If the attribute is a String, this is the maximum length allowed.",
                "type": "Integer"
            },
            "min": {
                "description": "If the attribute is an Integer, this sets its minimum allowed value. If the attribute is a String, this is the minimum length allowed.",
                "type": "Integer"
            },
            "": {
                "description": "",
                "type": "String"
            },
            "name": {
                "description": "Required attribute. Its value must match the aura:attribute name value in the .cmp resource.",
                "type": "String"
            },
            "placeholder": {
                "description": "Input placeholder text for the attribute when it displays in the tool.",
                "type": "String"
            },
            "required": {
                "description": "Denotes whether the attribute is required. If omitted, defaults to false.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "design:component": {
        "attribs": {
            "label": {
                "description": "Sets the label of the component when it displays in tools such as App Builder.",
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
                "type": "Picklist",
                "values": [
                    "FULL", "MINI"
                ]
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

    "aura:text": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "value": {
                "type": "String",
                "description": "The String to be rendered.",
                "required": False
            }
        }
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
                "type": "Picklist",
                "values": ["x-small", "small", "medium", "large"],
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
                "type": "Picklist",
                "values": icon_names
            },
            "iconPosition": {
                "description": "Describes the position of the icon with respect to body. Options include left and right. This value defaults to left.",
                "type": "Picklist",
                "values": ["left", "right"]
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
                "type": "Picklist",
                "values": ["button", "rest", "submit"]
            },
            "value": {
                "description": "The value for the button element. This value is optional and can be used when submitting a form.",
                "type": "String"
            },
            "variant": {
                "description": "The variant changes the appearance of the button. Accepted variants include base, neutral, brand, destructive, and inverse. This value defaults to neutral.",
                "type": "Picklist",
                "values": [
                    "base",
                    "neutral",
                    "brand",
                    "destructive",
                    "inverse",
                    "success"
                ]
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
                "type": "Picklist",
                "values": icon_names
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
                "type": "Picklist",
                "values": ["xx-small", "x-small", "small", "medium", "large"],
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
                "type": "Picklist",
                "values": ["button", "reset", "submit"]
            },
            "value": {
                "description": "The value for the button element. This value is optional and can be used when submitting a form.",
                "type": "String"
            },
            "variant": {
                "description": "The variant changes the appearance of the button. Accepted variants include base, neutral, brand, destructive, and inverse. This value defaults to neutral.",
                "type": "Picklist",
                "values": [
                    "base",
                    "container",
                    "brand",
                    "border",
                    "border-filled",
                    "bare-inverse",
                    "border-inverse"
                ]
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
                "type": "Picklist",
                "values": icon_names
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
                "type": "Picklist",
                "values": ["xx-small", "x-small", "small", "medium"]
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
                "type": "Picklist",
                "values": [
                    "border",
                    "border-filled",
                    "border-inverse"
                ]
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
                "type": "Picklist",
                "values": icon_names
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
                "type": "Picklist",
                "values": ["auto", "left", "center", "right", "bottom-left", "bottom-center", "bottom-right"]
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
                "type": "Picklist",
                "values": [
                    "base",
                    "container",
                    "border",
                    "border-filled",
                    "bare-inverse",
                    "border-inverse"
                ]
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
                "type": "Picklist",
                "values": icon_names
            },
            "iconNameWhenOff": {
                "description": "The name of the icon to be used in the format \\'utility:add\\' when the state is false.",
                "type": "Picklist",
                "values": icon_names
            },
            "iconNameWhenOn": {
                "description": "The name of the icon to be used in the format \\'utility:check\\' when the state is true.",
                "type": "Picklist",
                "values": icon_names
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
                "type": "Picklist",
                "values": [
                    "neutral",
                    "brand",
                    "destructive",
                    "inverse",
                    "success",
                    "text"
                ]
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
                "type": "Picklist",
                "values": icon_names
            },
            "title": {
                "description": "The title can include text or another component, and is displayed in the header.",
                "type": "Component[]"
            },
            "variant": {
                "description": "The variant changes the appearance of the card. Accepted variants include base or narrow. This value defaults to base.",
                "type": "Picklist",
                "values": [
                    "base",
                    "narrow"
                ]
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:carousel": {
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
            "scrollDuration": {
                "description": "The auto scroll duration. The default is 5 seconds, after that the next image is displayed.",
                "type": "Integer",
                "default": 5
            },
            "disableAutoScroll": {
                "description": "Specifies whether auto scroll is disabled. The default value is false.",
                "type": "Boolean"
            },
            "disableAutoRefresh": {
                "description": "Specifies whether the carousel should stop looping from the beginning after the last item is displayed. The default value is false.",
                "type": "Boolean"
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
                "type": "Picklist",
                "values": ["auto", "left", "center", "right", "bottom-left", "bottom-center", "bottom-right"]
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
                "type": "Picklist",
                "values": [
                    "standard",
                    "label-hidden"
                ]
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
    "lightning:conversationToolkitAPI": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            }
        },
        "methods": {},
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
                "type": "Picklist",
                "values": ["asc", "desc"]
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
                "type": "Picklist",
                "values": ["asc", "desc"]
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
                "type": "Picklist",
                "values": [
                    "standard",
                    "label-hidden"
                ]
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
                "type": "Picklist",
                "values": ["ellie", "eq", "score", "strength", "trend", "waffle"]
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:empApi": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            }
        },
        "methods": {},
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
    "lightning:formattedAddress": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "required": False
            },
            "city": {
                "type": "String",
                "description": "The city detail for the address.",
                "required": False
            },
            "class": {
                "type": "String",
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "required": False
            },
            "country": {
                "type": "String",
                "description": "The country detail for the address.",
                "required": False
            },
            "disabled": {
                "type": "Boolean",
                "description": "Specifies whether the address is clickable. This value defaults to False.",
                "required": False
            },
            "latitude": {
                "type": "Decimal",
                "description": "The latitude of the location if known. Latitude values must be within -90 and 90.",
                "required": False
            },
            "longitude": {
                "type": "Decimal",
                "description": "The longitude of the location if known. Longitude values must be within -180 and 180.",
                "required": False
            },
            "postalCode": {
                "type": "String",
                "description": "The postal code detail for the address.",
                "required": False
            },
            "province": {
                "type": "String",
                "description": "The province detail for the address.",
                "required": False
            },
            "street": {
                "type": "String",
                "description": "The street detail for the address.",
                "required": False
            },
            "title": {
                "type": "String",
                "description": "Displays tooltip text when the mouse moves over the element.",
                "required": False
            }
        }
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
                "type": "Picklist",
                "values": ["narrow", "short", "long"]
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
                "type": "Picklist",
                "values": timezones
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
    "lightning:formattedName": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "required": False
            },
            "class": {
                "type": "String",
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "required": False
            },
            "firstName": {
                "type": "String",
                "description": "The value for the first name.",
                "required": False
            },
            "format": {
                "type": "String",
                "description": "The format for which to display the name. Valid values include short, medium, and long. This value defaults to long.",
                "required": False
            },
            "informalName": {
                "type": "String",
                "description": "The value for the informal name.",
                "required": False
            },
            "lastName": {
                "type": "String",
                "description": "The value for the last name.",
                "required": False
            },
            "middleName": {
                "type": "String",
                "description": "The value for the middle name.",
                "required": False
            },
            "salutation": {
                "type": "String",
                "description": "The value for the salutation, such as Dr. or Mrs.",
                "required": False
            },
            "suffix": {
                "type": "String",
                "description": "The value for the suffix.",
                "required": False
            },
            "title": {
                "type": "String",
                "description": "Displays tooltip text when the mouse moves over the element.",
                "required": False
            }
        }
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
                "type": "Picklist",
                "values": ["symbol", "code", "name"]
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
                "type": "Picklist",
                "values": ["decimal", "currency", "percent"]
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
    "lightning:formattedTime": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "required": False
            },
            "class": {
                "type": "String",
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "required": False
            },
            "title": {
                "type": "String",
                "description": "Displays tooltip text when the mouse moves over the element.",
                "required": False
            },
            "value": {
                "type": "String",
                "description": "The time value to format.",
                "required": False
            }
        }
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
                "type": "Picklist",
                "values": ["_blank", "_parent", "_self", "_top"]
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
                "type": "Picklist",
                "values": icon_names
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
                "type": "Picklist",
                "values": icon_names
            },
            "size": {
                "description": "The size of the icon. Options include xx-small, x-small, small, medium, or large. This value defaults to medium.",
                "type": "Picklist",
                "values": ["xx-small", "x-small", "small", "medium", "large"]
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            },
            "variant": {
                "description": "The variant changes the appearance of a utility icon. Accepted variants include inverse, warning and error. Use the inverse variant to implement a white fill in utility icons on dark backgrounds.",
                "type": "Picklist",
                "values": [
                    "error",
                    "warning",
                    "inverse"
                ]
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
                "type": "Picklis",
                "values": [
                    "Checkbox",
                    "Checkbox-button",
                    "Color",
                    "Date",
                    "Datetime",
                    "Email",
                    "File",
                    "Month",
                    "Number",
                    "Password",
                    "Radio",
                    "Range",
                    "Search",
                    "Tel",
                    "Text",
                    "Time",
                    "Toggle",
                    "URL",
                    "Week"
                ]
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
                "type": "Picklist",
                "values": [
                    "standard",
                    "label-hidden"
                ]
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:inputAddress": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "addressLabel": {
                "type": "String",
                "description": "The label of the address compound field.",
                "required": False
            },
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "required": False
            },
            "city": {
                "type": "String",
                "description": "The city field of the address.",
                "required": False
            },
            "cityLabel": {
                "type": "String",
                "description": "The label of the city field of the address.",
                "required": False
            },
            "class": {
                "type": "String",
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "required": False
            },
            "country": {
                "type": "String",
                "description": "The country field of the address. If countryOptions is provided, this country value is selected by default.",
                "required": False
            },
            "countryLabel": {
                "type": "String",
                "description": "The label of the country field of the address.",
                "required": False
            },
            "countryOptions": {
                "type": "List",
                "description": "The array of label-value pairs for the country. Displays a dropdown menu of options.",
                "required": False
            },
            "disabled": {
                "type": "Boolean",
                "description": "Specifies whether the address fields are disabled. This value defaults to false.",
                "required": False
            },
            "onblur": {
                "type": "Action",
                "description": "The action triggered when the input releases focus.",
                "required": False
            },
            "onchange": {
                "type": "Action",
                "description": "The action triggered when the value changes.",
                "required": False
            },
            "onfocus": {
                "type": "Action",
                "description": "The action triggered when the input receives focus.",
                "required": False
            },
            "postalCode": {
                "type": "String",
                "description": "The postal code field of the address.",
                "required": False
            },
            "postalCodeLabel": {
                "type": "String",
                "description": "The label of the postal code field of the address.",
                "required": False
            },
            "province": {
                "type": "String",
                "description": "The province field of the address. If provinceOptions is provided, this province value is selected by default.",
                "required": False
            },
            "provinceLabel": {
                "type": "String",
                "description": "The label of the province field of the address.",
                "required": False
            },
            "provinceOptions": {
                "type": "List",
                "description": "The array of label-value pairs for the province. Displays a dropdown menu of options.",
                "required": False
            },
            "readonly": {
                "type": "Boolean",
                "description": "Specifies whether the address fields are read-only. This value defaults to false.",
                "required": False
            },
            "required": {
                "type": "Boolean",
                "description": "Specifies whether the address fields are required. This value defaults to false.",
                "required": False
            },
            "street": {
                "type": "String",
                "description": "The street field of the address.",
                "required": False
            },
            "streetLabel": {
                "type": "String",
                "description": "The label of the street field of the address.",
                "required": False
            },
            "title": {
                "type": "String",
                "description": "Displays tooltip text when the mouse moves over the element.",
                "required": False
            },
            "variant": {
                "type": "Picklist",
                "values": [
                    "standard",
                    "label-hidden"
                ],
                "description": "The variant changes the appearance of the compound field. Accepted variants include standard and label-hidden. This value defaults to standard.",
                "required": False
            }
        }
    },
    "lightning:inputField": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the\n                                body of the tag.",
                "required": False
            },
            "class": {
                "type": "String",
                "description": "A CSS class for the outer element, in addition to the component's\n                                base classes.",
                "required": False
            },
            "fieldName": {
                "type": "String",
                "description": "The API name of the field to be displayed.",
                "required": False
            }
        }
    },
    "lightning:inputLocation": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "required": False
            },
            "class": {
                "type": "String",
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "required": False
            },
            "title": {
                "type": "String",
                "description": "Displays tooltip text when the mouse moves over the element.",
                "required": False
            },
            "latitude": {
                "type": "String",
                "description": "The latitude value. Latitude values must be within -90 and 90.",
                "required": False
            },
            "longitude": {
                "type": "String",
                "description": "The longitude value. Longitude values must be within -180 and 180.",
                "required": False
            },
            "required": {
                "type": "Boolean",
                "description": "Specifies whether the compound field must be filled out. An error message is displayed if a user interacts with the field and does not provide a value. This value defaults to false.",
                "required": False
            },
            "disabled": {
                "type": "Boolean",
                "description": "Specifies whether the compound field should be disabled. Disabled fields are grayed out and not clickable. This value defaults to false.",
                "required": False
            },
            "readonly": {
                "type": "Boolean",
                "description": "Specifies whether the compound field is read-only. This value defaults to false.",
                "required": False
            },
            "variant": {
                "type": "Picklist",
                "values": [
                    "standard",
                    "label-hidden"
                ],
                "description": "The variant changes the appearance of the compound field. Accepted variants include standard and label-hidden. This value defaults to standard.",
                "required": False
            },
            "label": {
                "type": "String",
                "description": "Text label for the compound field.",
                "required": False
            },
            "onblur": {
                "type": "Action",
                "description": "The action triggered when the input releases focus.",
                "required": False
            },
            "onchange": {
                "type": "Action",
                "description": "The action triggered when the value changes.",
                "required": False
            },
            "onfocus": {
                "type": "Action",
                "description": "The action triggered when the input receives focus.",
                "required": False
            }
        }
    },
    "lightning:inputName": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "required": False
            },
            "class": {
                "type": "String",
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "required": False
            },
            "disabled": {
                "type": "Boolean",
                "description": "Specifies whether the compound field should be disabled. Disabled fields are grayed out and not clickable. This value defaults to false.",
                "required": False
            },
            "fieldsToDisplay": {
                "type": "List",
                "description": "List of fields to be displayed on the component. This value defaults to ['firstName', 'salutation', 'lastName']. Other field values include middleName, informalName, suffix.",
                "required": False
            },
            "firstName": {
                "type": "String",
                "description": "Displays the First Name field.",
                "required": False
            },
            "informalName": {
                "type": "String",
                "description": "Displays the Informal Name field.",
                "required": False
            },
            "label": {
                "type": "String",
                "description": "Text label for the compound field.",
                "required": False
            },
            "lastName": {
                "type": "String",
                "description": "Displays the Last Name field. This field is always displayed if you set required to true.",
                "required": False
            },
            "middleName": {
                "type": "String",
                "description": "Displays the Middle Name field.",
                "required": False
            },
            "onblur": {
                "type": "Action",
                "description": "The action triggered when the input releases focus.",
                "required": False
            },
            "onchange": {
                "type": "Action",
                "description": "The action triggered when the value changes.",
                "required": False
            },
            "onfocus": {
                "type": "Action",
                "description": "The action triggered when the input receives focus.",
                "required": False
            },
            "options": {
                "type": "List",
                "description": "Displays a list of salutation options, such as Dr. or Mrs., provided as label-value pairs.",
                "required": False
            },
            "readonly": {
                "type": "Boolean",
                "description": "Specifies whether the compound field is read-only. This value defaults to false.",
                "required": False
            },
            "required": {
                "type": "Boolean",
                "description": "Specifies whether the compound field must be filled out. A red asterisk is displayed on the Last Name field. An error message is displayed if a user interacts with the Last Name field and does not provide a value. This value defaults to false.",
                "required": False
            },
            "salutation": {
                "type": "String",
                "description": "Displays the Salutation field as a dropdown menu. An array of label-value pairs must be provided using the options attribute.",
                "required": False
            },
            "suffix": {
                "type": "String",
                "description": "Displays the Suffix field.",
                "required": False
            },
            "title": {
                "type": "String",
                "description": "Displays tooltip text when the mouse moves over the element.",
                "required": False
            },
            "variant": {
                "type": "Picklist",
                "values": [
                    "standard",
                    "label-hidden"
                ],
                "description": "The variant changes the appearance of the compound field. Accepted variants include standard and label-hidden. This value defaults to standard.",
                "required": False
            }
        }
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
                "type": "Picklist",
                "values": [
                    "bottom-toolbar"
                ]
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:insertImageButton": {
        "attribs": {
            "body": {
                "description": "Body of the layout component.",
                "type": "Component[]"
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
                "type": "Picklist",
                "values": ["center", "space", "spread", "end"]
            },
            "multipleRows": {
                "description": "Determines whether to wrap the child items when they exceed the layout width. If true, the items wrap to the following line. This value defaults to false.",
                "type": "Boolean"
            },
            "pullToBoundary": {
                "description": "Pulls layout items to the layout boundaries and corresponds to the padding size on the layout item. Possible values are small, medium, or large.",
                "type": "Picklist",
                "values": ["small", "medium", "large"]
            },
            "verticalAlign": {
                "description": "Determines how to spread the layout items vertically. The alignment options are start, center, end, and stretch.",
                "type": "Picklist",
                "values": ["start", "center", "end", "stretch"]
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
                "type": "Picklist",
                "values": [
                    "horizontal-small",
                    "horizontal-medium",
                    "horizontal-large",
                    "around-small",
                    "around-medium",
                    "around-large"
                ]
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
    "lightning:listView": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "required": False
            },
            "enableInlineEdit": {
                "type": "Boolean",
                "description": "Specifies whether the inline edit of cells is enabled. This value defaults to false.",
                "required": False
            },
            "listName": {
                "type": "String",
                "description": "The developer name of the List View",
                "required": False
            },
            "objectApiName": {
                "type": "String",
                "description": "The API name of the object to be displayed in this List View",
                "required": False
            },
            "rows": {
                "type": "Integer",
                "description": "Specifies the number of rows to initially load and additional rows after each subsequent 'Load More' click. The default and maximum number of rows value is 50.",
                "required": False
            },
            "showActionBar": {
                "type": "Boolean",
                "description": "Specifies whether the action bar displays. This value defaults to false.",
                "required": False
            },
            "showRowLevelActions": {
                "type": "Boolean",
                "description": "Specifies whether row level actions are displayed (as a dropdown menu in the last column of the row). This value defaults to false.",
                "required": False
            }
        }
    },
    "lightning:map": {
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
            "zoomLevel": {
                "description": "Corresponds to zoom levels defined in Google Maps API. If not specified, the map component automatically chooses an appropriate zoom level to show all markers with comfortable margins.",
                "type": "Integer"
            },
            "mapMarkers": {
                "description": "Array containing one or more objects with the address or coordinates to be displayed.",
                "type": "Object"
            },
            "markersTitle": {
                "description": "Provides the heading title for the markers. Required if specifying multiple markers. The title is displayed below the map as a header for the list of clickable addresses.",
                "type": "String"
            },
            "center": {
                "description": "If provided an icon with the provided name is shown to the right of the menu item.",
                "type": "Object",
                "values": "Centers the map according to an specific 'mapMarker' object. If a map marker is not specified, the map centers automatically."
            },
            "showFooter": {
                "description": "Shows footer with 'Open in Google Maps' link. Default value: 'false'.",
                "type": "Boolean"
            }
        },
        "simple": False,
        "type": "aura",
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
                "type": "Picklist",
                "values": icon_names
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
    "lightning:navigation": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            }
        },
        "simple": False,
        "type": "aura",
        "description": "Generates URL for a given pageReference. This component requires API version 43.0 and later."
    },
    "lightning:navigationItemAPI": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:notificationsLibrary": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
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
                "type": "Picklist",
                "values": [
                    "standard",
                    "label-hidden"
                ]
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:overlayLibrary": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
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
    "lightning:pillContainer": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "required": False
            },
            "class": {
                "type": "String",
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "required": False
            },
            "items": {
                "type": "List",
                "description": "An array of items to be rendered as pills in a container.",
                "required": False
            },
            "label": {
                "type": "String",
                "description": "Aria label for the pill container.",
                "required": False
            },
            "onitemremove": {
                "type": "Action",
                "description": "The action triggered when a pill is removed.",
                "required": False
            },
            "singleLine": {
                "type": "Boolean",
                "description": "Whether keep pills in single line.",
                "required": False
            },
            "title": {
                "type": "String",
                "description": "Displays tooltip text when the mouse moves over the element.",
                "required": False
            }
        }
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
                "type": "Picklist",
                "values": ["x-small", "small", "medium", "large"]
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
                "type": "Picklist",
                "values": [
                    "base",
                    "circular"
                ]
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
                "type": "Picklist",
                "values": ["base", "path"]
            },
            "variant": {
                "description": "Changes the appearance of the progress indicator for the base type only",
                "type": "picklist",
                "values": [
                    "base",
                    "shaded"
                ]
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:quickActionAPI": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:quipCard": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "parentRecordId": {
                "description": "ID of the Salesforce record to display the card for.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    # "lightning:progressStep": {
    #     "attribs": {
    #         "label": {
    #             "type": "String"
    #         },
    #         "value": {
    #             "type": "String"
    #         }
    #     },
    #     "simple": False,
    #     "type": "aura"
    # },
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
                "type": "Picklist",
                "values": [
                    "radio",
                    "button"
                ]
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
                "type": "Picklist",
                "values": [
                    "standard",
                    "label-hidden"
                ]
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightning:recordEditForm": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "required": False
            },
            "class": {
                "type": "String",
                "description": "A CSS class for the outer element, in addition to the component's base classes.",
                "required": False
            },
            "objectApiName": {
                "type": "String",
                "description": "The API name of the object.",
                "required": False
            },
            "onerror": {
                "type": "Action",
                "description": "The action triggered when there is an error on form submission.",
                "required": False
            },
            "onload": {
                "type": "Action",
                "description": "The action triggered when the form data is loaded.",
                "required": False
            },
            "onsubmit": {
                "type": "Action",
                "description": "The action triggered when the form is submitted.",
                "required": False
            },
            "onsuccess": {
                "type": "Action",
                "description": "The action triggered when the form is saved.",
                "required": False
            },
            "recordId": {
                "type": "String",
                "description": "The ID of the record to be displayed.",
                "required": False
            },
            "recordTypeId": {
                "type": "String",
                "description": "The ID of the record type, which is required if you created multiple record types but don't have a default.",
                "required": False
            }
        }
    },
    "lightning:recordForm": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "fields": {
                "description": "List of fields to be displayed.",
                "type": "String[]"
            },
            "class": {
                "description": "A CSS class that will be applied to the outer element. This style is in addition to base classes associated with the component.",
                "type": "String"
            },
            "recordId": {
                "description": "The ID of the record to be displayed.",
                "type": "String"
            },
            "objectApiName": {
                "description": "The API name of the object.",
                "type": "String",
                "required": True
            },
            "layoutType": {
                "description": "The type of layout to use to display the form fields. Possible values: Compact, Full.",
                "type": "Picklist",
                "values": ["Compact", "Full"]
            },
            "columns": {
                "description": "Specifies the number of columns for the form.",
                "type": "Integer"
            },
            "mode": {
                "description": "Specifies the interaction and display style for the form. Possible values: view, edit, readonly",
                "type": "Picklist",
                "values": ["view", "edit", "readonly"]
            },
            "recordTypeId": {
                "description": "The ID of the record type, which is required if you created multiple record types but don't have a default.",
                "type": "String"
            },
            "onload": {
                "description": "The action triggered when the form data is loaded.",
                "type": "Action"
            },
            "onsubmit": {
                "description": "The action triggered when the form is submitted.",
                "type": "Action"
            },
            "onsuccess": {
                "description": "The action triggered when the form is saved.",
                "type": "Action"
            },
            "onerror": {
                "description": "The action triggered when there is an error on form submission.",
                "type": "Action"
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
                "type": "Picklist",
                "values": [
                    "standard",
                    "label-hidden"
                ]
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
                "type": "Picklist",
                "values": ["x-small", "small", "medium", "large"]
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
                "type": "Picklist",
                "values": [
                    "standard",
                    "label-hidden"
                ]
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
                "type": "Picklist",
                "values": ["small", "medium", "large"]
            },
            "title": {
                "description": "Displays tooltip text when the mouse moves over the element.",
                "type": "String"
            },
            "variant": {
                "description": "The variant changes the appearance of the spinner. Accepted variants are brand and inverse.",
                "type": "Picklist",
                "values": [
                    "base",
                    "brand",
                    "inverse"
                ]
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
                "type": "Picklist",
                "values": [
                    "default",
                    "scoped"
                ]
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
                "type": "Picklist",
                "values": [
                    "standard",
                    "label-hidden"
                ]
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
    "lightning:treeGrid": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "": {
                "type": "Object",
                "description": "The toggled row data.",
                "required": False
            },
            "columns": {
                "type": "List",
                "description": "Array of the columns object that's used to define the data types.\n                                Required properties include 'label', 'dataKey', and 'type'. The\n                                default type is 'text'.",
                "required": False
            },
            "minColumnWidthmaxColumnWidth": {
                "type": "integer",
                "description": "The width of the column when it's initialized, which must be\n                                within the minColumnWidth and\n                                    maxColumnWidth values, or\n                                within 50px and 1000px if they are not provided.",
                "required": False
            },
            "currencyCodecurrency": {
                "type": "object",
                "description": "Provides custom formatting with component attributes for the data\n                                type. For example, currencyCode\n                                for the currency type. For more\n                                information, see Formatting with Data Types.",
                "required": False
            },
            "standard:opportunity": {
                "type": "string",
                "description": "The Lightning Design System name of the icon. Names are written\n                                in the format standard:opportunity. The icon is appended to the left\n                                of the header label.",
                "required": False
            },
            "lightning:formattedNumber": {
                "type": "Displays a percentage using lightning:formattedNumber",
                "description": "Same as number type",
                "required": False
            },
            "lightning:formattedDateTime": {
                "type": "Displays a date and time based on the locale using lightning:formattedDateTime",
                "description": "N/A",
                "required": False
            },
            "lightning:formattedText": {
                "type": "Displays text using lightning:formattedText",
                "description": "N/A",
                "required": False
            },
            "lightning:formattedUrl": {
                "type": "Displays a URL using lightning:formattedUrl",
                "description": "label, target",
                "required": False
            },
            "lightning:buttonMenuright": {
                "type": "Displays a dropdown menu using lightning:buttonMenu with actions as menu\n                                items",
                "description": "rowActions (required), menuAlignment (defaults to right)",
                "required": False
            },
            "lightning:button": {
                "type": "Displays a button using lightning:button",
                "description": "disabled, iconName, iconPosition, label, name, title,\n                                variant",
                "required": False
            },
            "lightning:formattedEmail": {
                "type": "Displays an email address using lightning:formattedEmail",
                "description": "N/A",
                "required": False
            },
            "lightning:formattedLocation": {
                "type": "Displays a latitude and longitude of a location using lightning:formattedLocation",
                "description": "latitude, longitude",
                "required": False
            },
            "lightning:formattedPhone": {
                "type": "Displays a phone number using lightning:formattedPhone",
                "description": "N/A",
                "required": False
            },
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the\n                                body of the tag.",
                "required": False
            },
            "class": {
                "type": "String",
                "description": "A CSS class for the outer element, in addition to the component's\n                                base classes.",
                "required": False
            },
            "data": {
                "type": "Object",
                "description": "The array of data to be displayed.",
                "required": False
            },
            "expandedRows": {
                "type": "List",
                "description": "The array of unique row IDs that are expanded.",
                "required": False
            },
            "hideCheckboxColumn": {
                "type": "Boolean",
                "description": "Hides or displays the checkbox column for row selection. To hide\n                                the checkbox column, set hideCheckboxColumn to true. The default is\n                                false.",
                "required": False
            },
            "isLoading": {
                "type": "Boolean",
                "description": "Specifies whether more data is being loaded and displays a\n                                spinner if so. The default is false.",
                "required": False
            },
            "keyField": {
                "type": "String",
                "description": "Required for better performance. Associates each row with a\n                                unique ID.",
                "required": False
            },
            "maxColumnWidth": {
                "type": "Integer",
                "description": "The maximum width for all columns. The default is 1000px.",
                "required": False
            },
            "minColumnWidth": {
                "type": "Integer",
                "description": "The minimum width for all columns. The default is 50px.",
                "required": False
            },
            "onresize": {
                "type": "Action",
                "description": "The action triggered when the table renders columns the first\n                                time and every time its resized an specific column.",
                "required": False
            },
            "onrowaction": {
                "type": "Action",
                "description": "The action triggered when an operation its clicked. By default\n                                its to closes the actions menu.",
                "required": False
            },
            "onrowselection": {
                "type": "Action",
                "description": "The action triggered when a row is selected.",
                "required": False
            },
            "ontoggle": {
                "type": "Action",
                "description": "The action triggered when a row is toggled (expanded or\n                                collapsed).",
                "required": False
            },
            "ontoggleall": {
                "type": "Action",
                "description": "The action triggered when all rows are toggled (expanded or\n                                collapsed).",
                "required": False
            },
            "resizeColumnDisabled": {
                "type": "Boolean",
                "description": "Specifies whether column resizing is disabled. The default is\n                                false.",
                "required": False
            },
            "rowNumberOffset": {
                "type": "Integer",
                "description": "Determines where to start counting the row number. The default is\n                                0.",
                "required": False
            },
            "selectedRows": {
                "type": "List",
                "description": "The array of unique row IDs that are selected.",
                "required": False
            },
            "showRowNumberColumn": {
                "type": "Boolean",
                "description": "Hides or displays the row number column. To show the row number\n                                column, set showRowNumberColumn to true. The default is\n                                false.",
                "required": False
            },
            "title": {
                "type": "String",
                "description": "Displays tooltip text when the mouse moves over the\n                                element.",
                "required": False
            }
        }
    },
    "lightning:unsavedChanges": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "label": {
                "description": "Label for the unsaved content which appears in prompt for save or discard.",
                "type": "String"
            },
            "onsave": {
                "description": "Action to handle saving unsaved content.",
                "type": "Action"
            },
            "ondiscard": {
                "description": "Action to handle discarding unsaved content.",
                "type": "Action"
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
                "type": "Picklist",
                "values": icon_names
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
    "lightningcommunity:backButton": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            },
            "iconName": {
                "description": "The Lightning Design System name of the icon. Only utility icons can be used in this component.",
                "type": "Picklist",
                "values": icon_names
            },
            "onnavigationcomplete": {
                "description": "Event handler action fired after every page navigation is complete. 'navigationcomplete' event provides 'canGoBack' boolean parameter value.",
                "type": "Action"
            },
            "class": {
                "description": "Styling class for back button.",
                "type": "String"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightningsnapin:minimizedAPI": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightningsnapin:prechatAPI": {
        "attribs": {
            "body": {
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "type": "Component[]"
            }
        },
        "simple": False,
        "type": "aura"
    },
    "lightningsnapin:settingsAPI": {
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
    "ui:outputDateTime": {
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
                "values": timezones
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
    "ui:scrollerWrapper": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "required": False
            },
            "class": {
                "type": "String",
                "description": "A CSS class applied to the outer element. This style is in addition to base classes output by the component.",
                "required": False
            }
        }
    },
    # "ui:spinner": {
    #     "attribs": {
    #         "aura:id": {
    #             "type": "String"
    #         },
    #         "body": {
    #             "description": "The body of the component. In markup, this is everything in the body of the tag.",
    #             "type": "Component[]"
    #         },
    #         "isVisible": {
    #             "description": "Specifies whether or not this spinner should be visible. Defaults to true.",
    #             "type": "Boolean"
    #         },
    #         "toggleLoadingIndicator": {
    #             "description": "Change the visibility of a ui:spinner component.",
    #             "type": "COMPONENT"
    #         }
    #     },
    #     "simple": False,
    #     "type": "aura"
    # },
    "wave:sdk": {
        "simple": False,
        "type": "aura",
        "attribs": {
            "body": {
                "type": "Component[]",
                "description": "The body of the component. In markup, this is everything in the body of the tag.",
                "required": False
            }
        }
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