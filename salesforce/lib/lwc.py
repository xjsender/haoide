# Since 2019, Winter19, v44
from .lightning import icon_names, timezones

std_templates = {

}
# tag definitions for lwc
tag_defs = {
    "template": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "for:each": {
                "type": "TrackObject",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Use this directive to iterate over an array and render a list."
            },
            "for:item": {
                "type": "TrackObject",
                "access": "global",
                "required": False,
                "default": "",
                "description": ""
            },
            "if:true": {
                "type": "TrackObject",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Use this directive to conditionally render DOM elements in a template."
            },
            "if:false": {
                "type": "TrackObject",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Use this directive to conditionally render DOM elements in a template."
            },
            "key": {
                "type": "TrackObject",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Use this directive to improve rendering performance by assigning a unique identifier to each item in a list. The key must be a string or a number, it can’t be an object. The engine uses the keys to determine which items have changed."
            },
            "lwc:dom": {
                "type": "TrackObject",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Add this directive to a native HTML element to call appendChild() on the element from the owner’s JavaScript class and preserve styling."
            }
        }
    },

    "lightning-accordion": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "title": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Displays tooltip text when the mouse moves over the element."
            },
            "active-section-name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Changes the default expanded section.\nThe first section in the accordion is expanded by default."
            },
            "allow-multiple-sections-open": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the accordion allows multiple open sections.\nOtherwise, opening a section closes another that's currently open."
            }
        },
        "events": {
            "onsectiontoggle": {
                "type": "COMPONENT",
                "description": "The event fired when an accordion section is toggled"
            }
        }
    },

    "lightning-accordion-section": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The unique section name to use with the active-section-name attribute in the accordion component."
            },
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The text that displays as the title of the section."
            },
            "title": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Displays a tooltip text when the mouse moves over the element."
            }
        }
    },

    "lightning-avatar": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "alternative-text": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The alternative text used to describe the avatar, which is displayed as\nhover text on the image."
            },
            "fallback-icon-name": {
                "type": "Picklist",
                "values": icon_names,
                "access": "global",
                "required": False,
                "default": "",
                "description": "The Lightning Design System name of the icon used as a fallback when the\nimage fails to load. The initials fallback relies on this for its\nbackground color. Names are written in the format 'standard:account'\nwhere 'standard' is the category, and 'account' is the specific icon to\nbe displayed. Only icons from the standard and custom categories are\nallowed."
            },
            "initials": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If the record name contains two words, like first and last name, use the\nfirst capitalized letter of each. For records that only have a single\nword name, use the first two letters of that word using one capital and\none lower case letter."
            },
            "size": {
                "type": "Picklist",
                "values": ["xx-small", "x-small", "small", "medium", "large"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "The size of the avatar. Valid values are x-small, small, medium, and large. This value defaults to medium."
            },
            "src": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The URL for the image."
            },
            "variant": {
                "type": "Picklist",
                "values": ["square", "circle", ""],
                "access": "global",
                "required": False,
                "default": "",
                "description": "The variant changes the shape of the avatar. Valid values are empty,\ncircle, and square. This value defaults to square."
            }
        }
    },

    "lightning-badge": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The text to be displayed inside the badge."
            }
        }
    },

    "lightning-breadcrumb": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "href": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The URL of the page that the breadcrumb goes to."
            },
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The text label for the breadcrumb."
            },
            "name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The name for the breadcrumb component. This value is optional and can be\nused to identify the breadcrumb in a callback."
            }
        }
    },

    "lightning-breadcrumbs": {
        "simple": False,
        "type": "lwc",
        "attribs": {}
    },

    "lightning-button": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": ""
            },
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": ""
            },
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": ""
            },
            "variant": {
                "type": "Picklist",
                "values": [
                    "base",
                    "neutral",
                    "brand",
                    "destructive",
                    "inverse",
                    "success"
                ],
                "access": "global",
                "required": False,
                "default": "neutral",
                "description": ""
            },
            "icon-name": {
                "type": "Picklist",
                "values": icon_names,
                "access": "global",
                "required": False,
                "default": "",
                "description": ""
            },
            "icon-position": {
                "type": "Picklist",
                "values": ["left", "right"],
                "access": "global",
                "required": False,
                "default": "left",
                "description": ""
            },
            "type": {
                "type": "Picklist",
                "values": ["reset", "submit", "button"],
                "access": "global",
                "required": False,
                "default": "button",
                "description": ""
            }
        }
    },

    "lightning-button-group": {
        "simple": False,
        "type": "lwc",
        "attribs": {}
    },

    "lightning-button-icon": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": ""
            },
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": ""
            },
            "variant": {
                "type": "Picklist",
                "values": [
                    "base",
                    "neutral",
                    "brand",
                    "destructive",
                    "inverse",
                    "success"
                ],
                "access": "global",
                "required": False,
                "default": "",
                "description": ""
            },
            "icon-name": {
                "type": "Picklist",
                "values": icon_names,
                "access": "global",
                "required": False,
                "default": "",
                "description": ""
            },
            "icon-class": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": ""
            },
            "size": {
                "type": "Picklist",
                "values": ["xx-small", "x-small", "small", "medium", "large"],
                "access": "global",
                "required": False,
                "default": "",
                "description": ""
            },
            "type": {
                "type": "Picklis",
                "values": ["button", "rest", "submit"],
                "access": "global",
                "required": False,
                "default": "",
                "description": ""
            },
            "alternative-text": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": ""
            },
            "tooltip": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": ""
            }
        }
    },

    "lightning-button-icon-stateful": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": ""
            },
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": ""
            },
            "variant": {
                "type": "Picklist",
                "values": [
                    "base",
                    "neutral",
                    "brand",
                    "destructive",
                    "inverse",
                    "success"
                ],
                "access": "global",
                "required": False,
                "default": "",
                "description": ""
            },
            "icon-name": {
                "type": "Picklist",
                "values": icon_names,
                "access": "global",
                "required": False,
                "default": "",
                "description": ""
            },
            "size": {
                "type": "Picklist",
                "values": ["xx-small", "x-small", "small", "medium", "large"],
                "access": "global",
                "required": False,
                "default": "",
                "description": ""
            },
            "alternative-text": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": ""
            },
            "selected": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": ""
            }
        }
    },

    "lightning-button-menu": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "variant": {
                "type": "Picklist",
                "values": [
                    "bare",
                    "container",
                    "border",
                    "border-filled",
                    "bare-inverse",
                    "border-inverse"
                ],
                "access": "global",
                "required": False,
                "default": "border",
                "description": "The variant changes the look of the button.\nAccepted variants include bare, container, border, border-filled, bare-inverse, and border-inverse.\nThis value defaults to border."
            },
            "icon-size": {
                "type": "Picklist",
                "values": ["xx-small", "x-small", "small", "medium", "large"],
                "access": "global",
                "required": False,
                "default": "medium",
                "description": "The size of the icon.\nOptions include xx-small, x-small, medium, or large.\nThis value defaults to medium."
            },
            "icon-name": {
                "type": "Picklist",
                "values": icon_names,
                "access": "global",
                "required": False,
                "default": "utility:down",
                "description": "The name of the icon to be used in the format 'utility:down'.\nIf an icon other than 'utility:down' or 'utility:chevrondown' is used,\na utility:down icon is appended to the right of that icon.\nThis value defaults to utility:down."
            },
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The value for the button element.\nThis value is optional and can be used when submitting a form."
            },
            "alternative-text": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The assistive text for the button."
            },
            "loading-state-alternative-text": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Message displayed while the menu is in the loading state."
            },
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Optional text to be shown on the button."
            },
            "draft-alternative-text": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Describes the reason for showing the draft indicator.\nThis is required when is-draft is true."
            },
            "menu-alignment": {
                "type": "String",
                "values": ["auto", "left", "center", "right", "bottom-left", "bottom-center", "bottom-right"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "Determines the alignment of the menu relative to the button.\nAvailable options are: auto, left, center, right, bottom-left, bottom-center, bottom-right.\nThe auto option aligns the dropdown menu based on available space.\nThis value defaults to left."
            },
            "disabled": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the menu can be opened by users."
            },
            "nubbin": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, a nubbin is present on the menu.\nA nubbin is a stub that protrudes from the menu item towards the button menu.\nThe nubbin position is based on the menu-alignment."
            },
            "title": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Displays tooltip text when the mouse moves over the button menu."
            },
            "is-draft": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the menu trigger shows a draft indicator."
            },
            "is-loading": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the menu is in a loading state and shows a spinner."
            },
            "access-key": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The keyboard shortcut for the button menu."
            },
            "tab-index": {
                "type": "Integer",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Reserved for internal use. Use tabindex instead to indicate if an element should be focusable.\ntabindex can be set to 0 or -1.\nThe default tabindex value is 0, which means that the button is focusable and participates in sequential keyboard navigation.\n-1 means that the button is focusable but does not participate in keyboard navigation."
            },
            "tooltip": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Text to display when the user mouses over or focuses on the button.\nThe tooltip is auto-positioned relative to the button and screen space."
            }
        }
    },

    "lightning-button-stateful": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "icon-name-when-on": {
                "type": "Picklist",
                "values": icon_names,
                "access": "global",
                "required": False,
                "default": "",
                "description": "The name of the icon to be used in the format 'utility:check' when the state is true."
            },
            "icon-name-when-off": {
                "type": "Picklist",
                "values": icon_names,
                "access": "global",
                "required": False,
                "default": "",
                "description": "The name of the icon to be used in the format 'utility:add' when the state is false."
            },
            "icon-name-when-hover": {
                "type": "Picklist",
                "values": icon_names,
                "access": "global",
                "required": False,
                "default": "",
                "description": "The name of the icon to be used in the format 'utility:close' when the state is true and the button receives focus."
            },
            "label-when-off": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The text to be displayed inside the button when state is false."
            },
            "label-when-on": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The text to be displayed inside the button when state is true."
            },
            "label-when-hover": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The text to be displayed inside the button when state is true and the button receives focus."
            },
            "variant": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The variant changes the appearance of the button.\nAccepted variants include brand, destructive, inverse, neutral, success, and text."
            },
            "selected": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the button is in the selected state."
            }
        }
    },

    "lightning-card": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "title": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The title can include text, and is displayed in the header.\nTo include additional markup or another component, use the title slot."
            },
            "icon-name": {
                "type": "Picklist",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The Lightning Design System name of the icon.\nNames are written in the format 'utility:down' where 'utility' is the category,\nand 'down' is the specific icon to be displayed.\nThe icon is displayed in the header to the left of the title.",
                "values": icon_names
            },
            "variant": {
                "type": "Picklist",
                "values": [
                    "base", "narrow"
                ],
                "access": "global",
                "required": False,
                "default": "",
                "description": "The variant changes the appearance of the card.\nAccepted variants include base or narrow.\nThis value defaults to base."
            }
        }
    },

    "lightning-carousel": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "disable-auto-scroll": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, images do not automatically scroll and users must click the indicators to scroll."
            },
            "disable-auto-refresh": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the carousel stops looping\nafter the last item is displayed."
            },
            "scroll-duration": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "5",
                "description": "The auto scroll duration. The default is 5 seconds, after that the next\nimage is displayed."
            }
        }
    },

    "lightning-carousel-image": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "src": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The path to the image."
            },
            "header": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Text for the label that's displayed under the image."
            },
            "description": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "5",
                "description": "Text displayed under the header."
            },
            "alternative-text": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "5",
                "description": "Assistive text for the image."
            },
            "href": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "5",
                "description": "A URL to create a link for the image. Clicking the image opens the link in the same frame."
            }
        }
    },

    "lightning-checkbox-group": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Text label for the checkbox group."
            },
            "options": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Array of label-value pairs for each checkbox."
            },
            "message-when-value-missing": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Optional message to be displayed when no checkbox is selected\nand the required attribute is set."
            },
            "name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The name of the checkbox group."
            },
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The list of selected checkboxes.\nEach array entry contains the value of a selected checkbox.\nThe value of each checkbox is set in the options attribute."
            },
            "disabled": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the checkbox group is disabled.\nCheckbox selections can't be changed for a disabled checkbox group."
            },
            "required": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, at least one checkbox must be selected."
            },
            "variant": {
                "type": "Picklist",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The variant changes the appearance of the checkbox group.\nAccepted variants include standard, label-hidden, label-inline, and label-stacked.\nThis value defaults to standard.\nUse label-hidden to hide the label but make it available to assistive technology.\nUse label-inline to horizontally align the label and checkbox group.\nUse label-stacked to place the label above the checkbox group."
            },
            "validity": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Represents the validity states that an element can be in, with respect to constraint validation."
            }
        }
    },

    "lightning-click-to-dial": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "body": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Inherited from aura:componentThe body of the component. In markup, this is everything in the body of the tag."
            },
            "class": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "InheritedA CSS class for the outer element, in addition to the component's base classes."
            },
            "title": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "InheritedDisplays tooltip text when the mouse moves over the element."
            },
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The phone number."
            },
            "recordId": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The Salesforce record Id that's associated with the phone number."
            },
            "params": {
                "type": "List",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Comma-separated list of parameters to pass to the third-party phone system."
            }
        }
    },

    "lightning-combobox": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "body": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Inherited from aura:componentThe body of the component. In markup, this is everything in the body of the tag."
            },
            "name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "InheritedSpecifies the name of an input element."
            },
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "InheritedSpecifies the value of an input element."
            },
            "variant": {
                "type": "Picklist",
                "values": ["standard", "label-inline", "label-hidden", "label-stacked"],
                "access": "global",
                "required": False,
                "default": "standard",
                "description": "InheritedThe variant changes the appearance of an input field. Accepted variants include standard, label-inline, label-hidden, and label-stacked. This value defaults to standard, which displays the label above the field. Use label-hidden to hide the label but make it available to assistive technology. Use label-inline to horizontally align the label and input field. Use label-stacked to place the label above the input field."
            },
            "disabled": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "false",
                "description": "InheritedSpecifies that an input element should be disabled. This value defaults to false."
            },
            "readonly": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "false",
                "description": "InheritedSpecifies that an input field is read-only. This value defaults to false."
            },
            "required": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "false",
                "description": "InheritedSpecifies that an input field must be filled out before submitting the form. This value defaults to false."
            },
            "validity": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "InheritedRepresents the validity states that an element can be in, with respect to constraint validation."
            },
            "onchange": {
                "type": "Method",
                "access": "global",
                "required": False,
                "default": "",
                "description": "InheritedThe action triggered when a value attribute changes."
            },
            "accesskey": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "InheritedSpecifies a shortcut key to activate or focus an element."
            },
            "tabindex": {
                "type": "Integer",
                "access": "global",
                "required": False,
                "default": "",
                "description": "InheritedSpecifies the tab order of an element when the Tab key is used for navigating. The tabindex value can be set to 0 or -1. The default is 0, which means that the component is focusable and participates in sequential keyboard navigation. -1 means that the component is focusable but does not participate in keyboard navigation."
            },
            "onfocus": {
                "type": "Method",
                "access": "global",
                "required": False,
                "default": "",
                "description": "InheritedThe action triggered when the element receives focus."
            },
            "onblur": {
                "type": "Method",
                "access": "global",
                "required": False,
                "default": "",
                "description": "InheritedThe action triggered when the element releases focus."
            },
            "class": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "InheritedA CSS class for the outer element, in addition to the component's base classes."
            },
            "title": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "InheritedDisplays tooltip text when the mouse moves over the element."
            },
            "options": {
                "type": "List",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A list of options that are available for selection. Each option has the following attributes: label and value."
            },
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Text label for the combobox."
            },
            "placeholder": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "Select an Option",
                "description": "Text that is displayed before an option is selected, to prompt the user to select an option. The default is \"Select an Option\"."
            },
            "dropdownAlignment": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "left",
                "description": "Specifies where the drop-down list is aligned with or anchored to the selection field. By default the list is aligned with the selection field at the top so the list opens down.  Use bottom-left to make the selection field display at the bottom so the list opens above it.  Use auto to let the component determine where to open the list based on space available."
            },
            "messageWhenValueMissing": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when the value is missing and input is required."
            },
            "fieldLevelHelp": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Help text detailing the purpose and function of the combobox."
            },
            "spinnerActive": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "false",
                "description": "Displays a spinner to indicate activity in the dropdown list. This value defaults to false."
            }
        }
    },

    "lightning-datatable": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "columns": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Array of the columns object that's used to define the data types.\nRequired properties include 'label', 'fieldName', and 'type'. The default type is 'text'.\nSee the Documentation tab for more information."
            },
            "data": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The array of data to be displayed."
            },
            "key-field": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Required for better performance.\nAssociates each row with a unique ID."
            },
            "hide-checkbox-column": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the checkbox column for row selection is hidden."
            },
            "show-row-number-column": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the row numbers are shown in the first column."
            },
            "row-number-offset": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Determines where to start counting the row number.\nThe default is 0."
            },
            "resize-column-disabled": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, column resizing is disabled."
            },
            "min-column-width": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The minimum width for all columns.\nThe default is 50px."
            },
            "max-column-width": {
                "type": "Integer",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The maximum width for all columns.\nThe default is 1000px."
            },
            "resize-step": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "10px",
                "description": "The width to resize the column when a user presses left or right arrow.\nThe default is 10px."
            },
            "sorted-by": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The column fieldName that controls the sorting order.\nSort the data using the onsort event handler."
            },
            "sorted-direction": {
                "type": "Picklist",
                "values": ["asc", "desc"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies the sorting direction.\nSort the data using the onsort event handler.\nValid options include 'asc' and 'desc'."
            },
            "default-sort-direction": {
                "type": "Picklist",
                "values": ["asc", "desc"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies the default sorting direction on an unsorted column.\nValid options include 'asc' and 'desc'.\nThe default is 'asc' for sorting in ascending order."
            },
            "enable-infinite-loading": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, you can load a subset of data and then display more\nwhen users scroll to the end of the table.\nUse with the onloadmore event handler to retrieve more data."
            },
            "load-more-offset": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Determines when to trigger infinite loading based on\nhow many pixels the table's scroll position is from the bottom of the table.\nThe default is 20."
            },
            "is-loading": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, a spinner is shown to indicate that more data is loading."
            },
            "max-row-selection": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The maximum number of rows that can be selected.\nCheckboxes are used for selection by default,\nand radio buttons are used when maxRowSelection is 1."
            },
            "selected-rows": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Enables programmatic row selection with a list of key-field values."
            },
            "errors": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies an object containing information about cell level, row level, and table level errors.\nWhen it's set, error messages are displayed on the table accordingly."
            },
            "draft-values": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The current values per row that are provided during inline edit."
            },
            "hide-table-header": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the table header is hidden."
            },
            "suppress-bottom-bar": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the footer that displays the Save and Cancel buttons is hidden during inline editing."
            }
        }
    },

    "lightning-dual-listbox": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "source-label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Label for the source options listbox."
            },
            "selected-label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Label for the selected options listbox."
            },
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Label for the dual listbox."
            },
            "options": {
                "type": "List",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A list of options that are available for selection. Each option has the following attributes: label and value."
            },
            "min": {
                "type": "Integer",
                "access": "global",
                "required": False,
                "default": "0",
                "description": "Minimum number of options required in the selected options listbox."
            },
            "max": {
                "type": "Integer",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Maximum number of options allowed in the selected options listbox."
            },
            "name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies the name of an input element."
            },
            "message-when-value-missing": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when the value is missing and input is required."
            },
            "message-when-range-overflow": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when a range overflow is detected."
            },
            "message-when-range-underflow": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when a range underflow is detected."
            },
            "disabled": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the listbox is disabled and users cannot interact with it."
            },
            "required": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the user must add an item to the selected listbox before submitting the form."
            },
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A list of default options that are included in the selected options listbox. This list is populated with values from the options attribute."
            },
            "required-options": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A list of required options that cannot be removed from selected options listbox. This list is populated with values from the options attribute."
            },
            "variant": {
                "type": "Picklist",
                "values": ["standard", "label-hidden", "label-inline", "label-stacked"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "The variant changes the appearance of the dual listbox.\nAccepted variants include standard, label-hidden, label-inline, and label-stacked.\nThis value defaults to standard.\nUse label-hidden to hide the label but make it available to assistive technology.\nUse label-inline to horizontally align the label and dual listbox.\nUse label-stacked to place the label above the dual listbox."
            },
            "size": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Number of items that display in the listboxes before vertical scrollbars are displayed. Determines the vertical size of the listbox."
            },
            "field-level-help": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Help text detailing the purpose and function of the dual listbox."
            },
            "disable-reordering": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the Up and Down buttons used for reordering the selected list items are hidden."
            },
            "show-activity-indicator": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, a spinner is displayed in the first listbox to indicate loading activity."
            },
            "validity": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Represents the validity states that an element can be in, with respect to constraint validation."
            },
            "add-button-label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Label for add button."
            },
            "remove-button-label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Label for remove button."
            },
            "up-button-label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Label for up button."
            },
            "down-button-label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Label for down button."
            }
        }
    },

    "lightning-dynamic-icon": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "alternative-text": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The alternative text used to describe the dynamic icon.\nThis text should describe what's happening.\nFor example, 'Graph is refreshing', not what the icon looks like, 'Graph'."
            },
            "type": {
                "type": "Picklist",
                "values": ["ellie", "eq", "score", "strength", "trend", "waffle"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "The Lightning Design System name of the dynamic icon.\nValid values are: ellie, eq, score, strength, trend, and waffle."
            },
            "option": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The option attribute changes the appearance of the dynamic icon.\nThe options available depend on the type.\neq: play (default) or stop\nscore: positive (default) or negative\nstrength: -3, -2, -1, 0 (default), 1, 2, 3\ntrend: neutral (default), up, or down"
            }
        }
    },

    "lightning-emp-api": {
        "simple": False,
        "type": "lwc",
        "attribs": {}
    },

    "lightning-file-upload": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies the name of the input element."
            },
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The text label for the file uploader."
            },
            "accept": {
                "type": "Picklist",
                "values": [
                    ".avi", ".doc", ".dot", ".docx", ".exe",
                    ".msg", ".wrf", ".html", ".acgi", ".htm",
                    ".htx", ".shtm", ".shtml", ".htt", ".mht",
                    ".mhtm", ".mhtml", ".mov", ".mp3", ".mp4",
                    ".mpeg", ".mpg", ".pdf", ".ppt", ".pot",
                    ".pps", ".pptx", ".svg", ".svgz", ".swf",
                    ".txml", ".unknown", ".wav", ".wma", ".wmv",
                    ".xhtml", ".xls", ".xlt", ".xlsx", ".xm"
                ],
                "access": "global",
                "required": False,
                "default": "",
                "description": "Comma-separated list of file extensions that can be uploaded\nin the format .ext, such as .pdf, .jpg, or .png."
            },
            "record-id": {
                "type": "TrackObject",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The record Id of the record that the uploaded file is associated to."
            },
            "disabled": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "false",
                "description": "Specifies whether this component should be displayed in a disabled state.\nDisabled components can't be clicked. The default is false."
            },
            "multiple": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "false",
                "description": "Specifies whether a user can upload more than one file simultanesouly.\nThe default is false."
            }
        }
    },

    "lightning-formatted-address": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "street": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The street detail for the address."
            },
            "city": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The city detail for the address."
            },
            "province": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The province detail for the address."
            },
            "country": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The country detail for the address."
            },
            "postal-code": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The postal code detail for the address."
            },
            "latitude": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The latitude of the location if known. Latitude values must be within -90 and 90."
            },
            "longitude": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The longitude of the location if known. Longitude values must be within -180 and 180."
            },
            "disabled": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the address is displayed as plain text and is not clickable."
            },
            "show-static-map": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "false",
                "description": "Displays a static map of the location using Google Maps. This value defaults to false."
            }
        }
    },

    "lightning-formatted-date-time": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The value to be formatted, which can be a Date object, timestamp, or an ISO8601 formatted string."
            },
            "weekday": {
                "type": "Picklist",
                "values": ["narrow", "short", "long"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies how to display the day of the week. Allowed values are narrow, short, or long."
            },
            "era": {
                "type": "Picklist",
                "values": ["narrow", "short", "long"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "Allowed values are narrow, short, or long."
            },
            "year": {
                "type": "Integer",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Allowed values are numeric or 2-digit."
            },
            "month": {
                "type": "Integer",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Allowed values are 2-digit, narrow, short, or long."
            },
            "day": {
                "type": "Integer",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Allowed values are numeric or 2-digit."
            },
            "hour": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Allowed values are numeric or 2-digit."
            },
            "minute": {
                "type": "Integer",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Allowed values are numeric or 2-digit."
            },
            "second": {
                "type": "Integer",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Allowed values are numeric or 2-digit."
            },
            "time-zone-name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Allowed values are short or long. For example, the Pacific time zone would display as 'PST'\nif you specify 'short', or 'Pacific Standard Time' if you specify 'long.'"
            },
            "time-zone": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The time zone to display. Use this attribute only if you want to override the default, which is the runtime's\ntime zone. Specify a time zone listed in the IANA time zone database (https://www.iana.org/time-zones). For example, set\nthe value to 'Pacific/Honolulu' to display Hawaii time. The short code UTC is also accepted."
            },
            "hour12": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Determines whether time is displayed as 12-hour. If False, time displays as 24-hour. The default setting is determined by the user's locale."
            }
        }
    },

    "lightning-formatted-email": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The email address that's displayed if a label is not provided."
            },
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The text label for the email address."
            },
            "tab-index": {
                "type": "Integer",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Reserved for internal use. Use tabindex instead to indicate if an element should be focusable.\nA value of 0 means that the element is focusable and\nparticipates in sequential keyboard navigation. A value of -1 means\nthat the element is focusable but does not participate in keyboard navigation."
            },
            "hide-icon": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "false",
                "description": "If present, the email icon is hidden and only the email address is displayed."
            }
        }
    },

    "lightning-formatted-location": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "latitude": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The latitude of the geolocation. Latitude values must be within -90 and 90."
            },
            "longitude": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The longitude of the geolocation. Longitude values must be within -180 and 180."
            }
        }
    },

    "lightning-formatted-name": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "format": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The format to use to display the name. Valid values include short, medium, and long. This value defaults to long."
            },
            "salutation": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The value for the salutation, such as Dr. or Mrs."
            },
            "first-name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The value for the first name."
            },
            "last-name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The value for the last name."
            },
            "middle-name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The value for the middle name."
            },
            "suffix": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The value for the suffix, such as Jr. or Esq."
            },
            "informal-name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The value for the informal name."
            }
        }
    },

    "lightning-formatted-number": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The value to be formatted."
            },
            "format-style": {
                "type": "Picklist",
                "values": ["decimal", "currency", "percent"],
                "access": "global",
                "required": False,
                "default": "decimal",
                "description": "The number formatting style to use. Possible values are decimal, currency,\nand percent. This value defaults to decimal."
            },
            "currency-code": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Only used if format-style='currency', this attribute determines which currency is\ndisplayed. Possible values are the ISO 4217 currency codes, such as 'USD' for the US dollar."
            },
            "currency-display-as": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "symbol",
                "description": "Determines how currency is displayed. Possible values are symbol, code, and name. This value defaults to symbol."
            },
            "minimum-integer-digits": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The minimum number of integer digits that are required. Possible values are from 1 to 21."
            },
            "minimum-fraction-digits": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The minimum number of fraction digits that are required."
            },
            "maximum-fraction-digits": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The maximum number of fraction digits that are allowed."
            },
            "minimum-significant-digits": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The minimum number of significant digits that are required. Possible values are from 1 to 21."
            },
            "maximum-significant-digits": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The maximum number of significant digits that are allowed. Possible values are from 1 to 21."
            }
        }
    },

    "lightning-formatted-phone": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Sets the phone number to display."
            },
            "tab-index": {
                "type": "Integer",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Reserved for internal use. Use tabindex instead to indicate if an element should be focusable.\nA value of 0 means that the element is focusable and\nparticipates in sequential keyboard navigation. A value of -1 means\nthat the element is focusable but does not participate in keyboard navigation."
            }
        }
    },

    "lightning-formatted-rich-text": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "disable-linkify": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the component does not create links in the rich text."
            },
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Sets the rich text to display."
            }
        }
    },

    "lightning-formatted-text": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Sets the text to display."
            },
            "linkify": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, URLs and email addresses are displayed in anchor tags.\nThey are displayed in plain text by default."
            }
        }
    },

    "lightning-formatted-time": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Time value to format."
            }
        }
    },

    "lightning-formatted-url": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "target": {
                "type": "Picklist",
                "values": ["_blank", "_parent", "_self", "_top"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies where to open the link. Options include _blank, _parent, _self, and _top."
            },
            "tooltip": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The text to display when the mouse hovers over the link."
            },
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The text to display in the link."
            },
            "tab-index": {
                "type": "Integer",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Reserved for internal use. Use tabindex instead to indicate if an element should be focusable.\nA value of 0 means that the element is focusable and\nparticipates in sequential keyboard navigation. A value of -1 means\nthat the element is focusable but does not participate in keyboard navigation."
            },
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The URL to format."
            }
        }
    },

    "lightning-helptext": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "content": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Text to be shown in the popover."
            },
            "icon-name": {
                "type": "Picklist",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The Lightning Design System name of the icon used as the visible element.\nNames are written in the format 'utility:info' where 'utility' is the category,\nand 'info' is the specific icon to be displayed.\nThe default is 'utility:info'.",
                "values": icon_names
            },
            "icon-variant": {
                "type": "Picklist",
                "values": ["inverse", "warning", "error"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "Changes the appearance of the icon.\nAccepted variants include inverse, warning, error."
            }
        }
    },

    "lightning-icon": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "alternative-text": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The alternative text used to describe the icon.\nThis text should describe what happens when you click the button,\nfor example 'Upload File', not what the icon looks like, 'Paperclip'."
            },
            "src": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A uri path to a custom svg sprite, including the name of the resouce,\nfor example: /assets/icons/standard-sprite/svg/test.svg#icon-heart"
            },
            "icon-name": {
                "type": "Picklist",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The Lightning Design System name of the icon.\nNames are written in the format 'utility:down' where 'utility' is the category,\nand 'down' is the specific icon to be displayed.",
                "values": icon_names
            },
            "size": {
                "type": "Picklist",
                "values": ["xx-small", "x-small", "small", "medium", "large"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "The size of the icon. Options include xx-small, x-small, small, medium, or large.\nThe default is medium."
            },
            "variant": {
                "type": "Picklist",
                "values": ["inverse", "success", "warning", "error"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "The variant changes the appearance of a utility icon.\nAccepted variants include inverse, success, warning, and error.\nUse the inverse variant to implement a white fill in utility icons on dark backgrounds."
            }
        }
    },

    "lightning-input": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "placeholder": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Text that is displayed when the field is empty, to prompt the user for a valid entry."
            },
            "name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies the name of an input element."
            },
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Text label for the input."
            },
            "message-when-bad-input": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when a bad input is detected."
            },
            "message-when-pattern-mismatch": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when a pattern mismatch is detected."
            },
            "message-when-range-overflow": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when a range overflow is detected."
            },
            "message-when-range-underflow": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when a range underflow is detected."
            },
            "message-when-step-mismatch": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when a step mismatch is detected."
            },
            "message-when-too-short": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when the value is too short."
            },
            "message-when-too-long": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when the value is too long."
            },
            "message-when-type-mismatch": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when a type mismatch is detected."
            },
            "message-when-value-missing": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when the value is missing."
            },
            "message-toggle-active": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Text shown for the active state of a toggle. The default is \"Active\"."
            },
            "message-toggle-inactive": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Text shown for the inactive state of a toggle. The default is \"Inactive\"."
            },
            "aria-label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Describes the input to assistive technologies."
            },
            "autocomplete": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Controls auto-filling of the field. Input types that support autocomplete are\nemail, search, tel, text, and url. Set the attribute to pass\nthrough autocomplete values to be interpreted by the browser."
            },
            "format-fraction-digits": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Reserved for internal use."
            },
            "time-aria-controls": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A space-separated list of element IDs whose presence or content is controlled by the\ntime input when type='datetime'. On mobile devices, this is merged with aria-controls\nand date-aria-controls to describe the native date time input."
            },
            "date-style": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The display style of the date when type='date' or type='datetime'. Valid values are\nshort, medium (default), and long. The format of each style is specific to the locale.\nOn mobile devices this attribute has no effect."
            },
            "time-style": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The display style of the time when type='time' or type='datetime'. Valid values are\nshort (default), medium, and long. Currently, medium and long styles look the same.\nOn mobile devices this attribute has no effect."
            },
            "date-aria-label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Describes the date input to assistive technologies when type='datetime'. On mobile devices,\nthis label is merged with aria-label and time-aria-label to describe the native date time input."
            },
            "date-aria-labelled-by": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A space-separated list of element IDs that provide labels for the date input when type='datetime'.\nOn mobile devices, this is merged with aria-labelled-by and time-aria-labelled-by to describe\nthe native date time input."
            },
            "time-aria-labelled-by": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A space-separated list of element IDs that provide labels for the time input when type='datetime'.\nOn mobile devices, this is merged with aria-labelled-by and date-aria-labelled-by to describe\nthe native date time input."
            },
            "time-aria-described-by": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A space-separated list of element IDs that provide descriptive labels for the time input when\ntype='datetime'. On mobile devices, this is merged with aria-described-by and date-aria-described-by\nto describe the native date time input."
            },
            "date-aria-controls": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A space-separated list of element IDs whose presence or content is controlled by the\ndate input when type='datetime'. On mobile devices, this is merged with aria-controls\nand time-aria-controls to describe the native date time input."
            },
            "date-aria-described-by": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A space-separated list of element IDs that provide descriptive labels for the date input when\ntype='datetime'. On mobile devices, this is merged with aria-described-by and time-aria-described-by\nto describe the native date time input."
            },
            "aria-controls": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A space-separated list of element IDs whose presence or content is controlled by the input."
            },
            "aria-labelled-by": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A space-separated list of element IDs that provide labels for the input."
            },
            "aria-described-by": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A space-separated list of element IDs that provide descriptive labels for the input."
            },
            "formatter": {
                "type": "Picklist",
                "values": ["decimal", "percent", "percent-fixed", "currency"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "String value with the formatter to be used for number input. Valid values include\ndecimal, percent, percent-fixed, and currency."
            },
            "type": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The type of the input. This value defaults to text."
            },
            "is-loading": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "For the search type only. If present, a spinner is displayed to indicate that data is loading."
            },
            "pattern": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies the regular expression that the input's value is checked against.\nThis attribute is supported for text, search, url, tel, email, and password types."
            },
            "max-length": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The maximum number of characters allowed in the field."
            },
            "accept": {
                "type": "Picklist",
                "values": [
                    ".avi", ".doc", ".dot", ".docx", ".exe",
                    ".msg", ".wrf", ".html", ".acgi", ".htm",
                    ".htx", ".shtm", ".shtml", ".htt", ".mht",
                    ".mhtm", ".mhtml", ".mov", ".mp3", ".mp4",
                    ".mpeg", ".mpg", ".pdf", ".ppt", ".pot",
                    ".pps", ".pptx", ".svg", ".svgz", ".swf",
                    ".txml", ".unknown", ".wav", ".wma", ".wmv",
                    ".xhtml", ".xls", ".xlt", ".xlsx", ".xm"
                ],
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies the types of files that the server accepts. This attribute can be used only when type='file'."
            },
            "min-length": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The minimum number of characters allowed in the field."
            },
            "max": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The maximum acceptable value for the input.  This attribute can be used only with number,\nrange, date, time, and datetime input types. For number and range type, the max value is a\ndecimal number. For the date, time, and datetime types, the max value must use a valid string for the type."
            },
            "min": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The minimum acceptable value for the input. This attribute can be used only with number,\nrange, date, time, and datetime input types. For number and range types, the min value\nis a decimal number. For the date, time, and datetime types, the min value must use a valid string for the type."
            },
            "step": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Granularity of the value, specified as a positive floating point number.\nUse 'any' when granularity is not a concern. This value defaults to 1."
            },
            "checked": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the checkbox is selected."
            },
            "multiple": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies that a user can enter more than one value. This attribute can be used only when type='file' or type='email'."
            },
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies the value of an input element."
            },
            "variant": {
                "type": "Picklist",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The variant changes the appearance of an input field.\nAccepted variants include standard, label-inline, label-hidden, and label-stacked.\nThis value defaults to standard, which displays the label above the field.\nUse label-hidden to hide the label but make it available to assistive technology.\nUse label-inline to horizontally align the label and input field.\nUse label-stacked to place the label above the input field."
            },
            "disabled": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the input field is disabled and users cannot interact with it."
            },
            "read-only": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the input field is read-only and cannot be edited by users."
            },
            "required": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the input field must be filled out before the form is submitted."
            },
            "timezone": {
                "type": "Picklist",
                "values": timezones,
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies the time zone used when type='datetime' only. This value defaults to the user's Salesforce time zone setting."
            },
            "files": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A FileList that contains selected files. This attribute can be used only when type='file'."
            },
            "validity": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Represents the validity states that an element can be in, with respect to constraint validation."
            },
            "field-level-help": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Help text detailing the purpose and function of the input.\nThis attribute isn't supported for file, radio, toggle, and checkbox-button types."
            },
            "access-key": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies a shortcut key to activate or focus an element."
            },
            "checkValidity": {
                "type": "Method",
                "access": "global",
                "arguments": "message",
                "description": "Sets a custom error message to be displayed when a form is submitted."
            },
            "reportValidity": {
                "type": "Method",
                "access": "global",
                "arguments": "message",
                "description": "Displays the error messages and returns false if the input is invalid. If the input is valid, reportValidity() clears displayed error messages and returns true."
            },
            "focus": {
                "type": "Method",
                "access": "global",
                "arguments": "message",
                "description": "Sets focus on the input element."
            },
            "blur": {
                "type": "Method",
                "access": "global",
                "arguments": "message",
                "description": "Removes keyboard focus from the input element."
            },
            "showHelpMessageIfInvalid": {
                "type": "Method",
                "access": "global",
                "arguments": "message",
                "description": "Displays error messages on invalid fields. An invalid field fails at least one constraint validation and returns false when checkValidity() is called."
            }
        }
    },

    "lightning-input-address": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "address-label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The label of the address compound field."
            },
            "street-label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The label of the street field of the address."
            },
            "city-label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The label of the city field of the address."
            },
            "province-label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The label of the province field of the address."
            },
            "country-label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The label of the country field of the address."
            },
            "postal-code-label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The label of the postal code field of the address."
            },
            "province-options": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The array of label-value pairs for the province. Displays a dropdown menu of options."
            },
            "country-options": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The array of label-value pairs for the country. Displays a dropdown menu of options."
            },
            "street": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The street field of the address."
            },
            "city": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The city field of the address."
            },
            "province": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The province field of the address. If province-options is provided, this province value is selected by default."
            },
            "country": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The country field of the address. If country-options is provided, this country value is selected by default."
            },
            "postal-code": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The postal code field of the address."
            },
            "disabled": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the address fields are disabled and users cannot interact with them."
            },
            "show-address-lookup": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, address lookup using Google Maps is enabled."
            },
            "read-only": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the address fields are read-only and cannot be edited."
            },
            "required": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the address fields must be filled before the form is submitted."
            },
            "variant": {
                "type": "Picklist",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The variant changes the appearance of an input address field.\nAccepted variants include standard, label-hidden, label-inline, and label-stacked.\nThis value defaults to standard.\nUse label-hidden to hide the label but make it available to assistive technology.\nUse label-inline to horizontally align the label and input address field.\nUse label-stacked to place the label above the input address field."
            },
            "field-level-help": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Help text detailing the purpose and function of the input."
            },
            "validity": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Represents the validity states that an element can be in, with respect to constraint validation."
            }
        }
    },

    "lightning-input-field": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "readonly": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "false",
                "description": "Specifies whether the input fields are read-only. This value defaults to false."
            },
            "variant": {
                "type": "Picklist",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The variant changes the label position of an input field.\nAccepted variants include standard, label-hidden, label-inline, and label-stacked.\nIf variant is specified, the label position is determined by the variant.\nOtherwise, it is determined by the density setting of the parent form."
            },
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The field value, which overrides the existing value."
            },
            "field-name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The API name of the field to be displayed."
            },
            "disabled": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the field is disabled and users cannot interact with it.\nRead-only fields are also disabled by default."
            },
            "dirty": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Reserved for internal use. If present, the field has been modified by the user but not saved or submitted."
            }
        }
    },

    "lightning-input-location": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The label of the geolocation compound field."
            },
            "field-level-help": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Help text detailing the purpose and function of the input."
            },
            "latitude": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The latitude value. Latitude values must be within -90 and 90."
            },
            "longitude": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The longitude value. Longitude values must be within -180 and 180."
            },
            "disabled": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the geolocation fields are disabled and users cannot interact with them."
            },
            "read-only": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the geolocations fields are read-only and cannot be edited."
            },
            "required": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the geolocation fields must be filled out before the form is submitted.\nAn error message is displayed if a user interacts with the field\nand does not provide a value."
            },
            "variant": {
                "type": "Picklist",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The variant changes the appearance of a geolocation compound field.\nAccepted variants include standard, label-hidden, label-inline, and label-stacked.\nThis value defaults to standard.\nUse label-hidden to hide the label but make it available to assistive technology.\nUse label-inline to horizontally align the label and geolocation fields.\nUse label-stacked to place the label above the geolocation fields."
            },
            "validity": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Represents the validity states that an element can be in, with respect to constraint validation."
            }
        }
    },

    "lightning-input-name": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The label of the input name field."
            },
            "options": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Displays a list of salutation options, such as Dr. or Mrs., provided as label-value pairs."
            },
            "fields-to-display": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "[{type=string, value=firstName}, {type=string, value=salutation}, {type=string, value=lastName}]",
                "description": "List of fields to be displayed on the component. This value defaults to\n['firstName', 'salutation', 'lastName']. Other field values include middleName,\ninformalName, suffix."
            },
            "salutation": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Displays the Salutation field as a dropdown menu. An array of label-value pairs must be provided using the options attribute."
            },
            "first-name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Displays the First Name field."
            },
            "middle-name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Displays the Middle Name field."
            },
            "informal-name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Displays the Informal Name field."
            },
            "last-name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Displays the Last Name field."
            },
            "suffix": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Displays the Suffix field."
            },
            "disabled": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the input name field is disabled and users cannot interact with it."
            },
            "read-only": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the input name field is read-only and cannot be edited."
            },
            "required": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the input name field must be filled out before the form is submitted.\nA red asterisk is displayed on the Last Name field. An error\nmessage is displayed if a user interacts with the Last Name\nfield and does not provide a value."
            },
            "variant": {
                "type": "Picklist",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The variant changes the appearance of a name compound field.\nAccepted variants include standard, label-hidden, label-inline, and label-stacked.\nThis value defaults to standard.\nUse label-hidden to hide the label but make it available to assistive technology.\nUse label-inline to horizontally align the label and name fields.\nUse label-stacked to place the label above the name fields."
            },
            "field-level-help": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Help text detailing the purpose and function of the input."
            },
            "validity": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Represents the validity states that an element can be in, with respect to constraint validation."
            }
        }
    },

    "lightning-input-rich-text": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The label of the rich text editor."
            },
            "label-visible": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "false",
                "description": "If present, the label on the rich text editor is visible."
            },
            "placeholder": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Text that is displayed when the field is empty, to prompt the user for a valid entry."
            },
            "disabled-categories": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A comma-separated list of button categories to remove from the toolbar."
            },
            "formats": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A whitelist of formats. By default, the list is computed based on enabled categories.\nThe 'table' format is always enabled to support copying and pasting of tables if formats are not provided."
            },
            "variant": {
                "type": "Picklist",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The variant changes the appearance of the toolbar. Accepted variant is bottom-toolbar which causes\nthe toolbar to be displayed below the text box."
            },
            "message-when-bad-input": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when invalid input is detected."
            },
            "custom-buttons": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Reserved for internal use. Custom buttons to add to the toolbar."
            },
            "share-with-entity-id": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Entity ID to share the image with."
            },
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The HTML content in the rich text editor."
            },
            "valid": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies whether the editor content is valid. If invalid, the slds-has-error class is added. This value defaults to true."
            },
            "disabled": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the editor is disabled and users cannot interact with it."
            }
        }
    },

    "lightning-layout": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "horizontal-align": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Determines how to spread the layout items horizontally.\nThe alignment options are center, space, spread, and end."
            },
            "vertical-align": {
                "type": "Picklist",
                "values": ["start", "center", "end", "stretch"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "Determines how to align the layout items vertically in the container.\nThe alignment options are start, center, end, and stretch."
            },
            "pull-to-boundary": {
                "type": "Picklist",
                "values": ["small", "medium", "large."],
                "access": "global",
                "required": False,
                "default": "",
                "description": "Pulls layout items to the layout boundaries and corresponds\nto the padding size on the layout item. Possible values are small, medium, or large."
            },
            "multiple-rows": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, layout items wrap to the following line when they exceed the layout width."
            }
        }
    },

    "lightning-layout-item": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "flexibility": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Make the item fluid so that it absorbs any extra space in its\ncontainer or shrinks when there is less space. Allowed values are:\nauto (columns grow or shrink equally as space allows),\nshrink (columns shrink equally as space decreases),\nno-shrink (columns don't shrink as space reduces),\ngrow (columns grow equally as space increases),\nno-grow (columns don't grow as space increases),\nno-flex (columns don't grow or shrink as space changes).\nUse a comma-separated value for multiple options, such as 'auto, no-shrink'."
            },
            "alignment-bump": {
                "type": "Picklist",
                "values": ["left", "top", "right", "bottom"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies a direction to bump the alignment of adjacent layout items. Allowed values are left, top, right, bottom."
            },
            "padding": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Sets padding to either the right and left sides of a container,\nor all sides of a container. Allowed values are horizontal-small,\nhorizontal-medium, horizontal-large, around-small, around-medium, around-large."
            },
            "size": {
                "type": "Integer",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If the viewport is divided into 12 parts, size indicates the\nrelative space the container occupies. Size is expressed as\nan integer from 1 through 12. This applies for all device-types."
            },
            "small-device-size": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If the viewport is divided into 12 parts, this attribute indicates\nthe relative space the container occupies on device-types larger than\nmobile. It is expressed as an integer from 1 through 12."
            },
            "medium-device-size": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If the viewport is divided into 12 parts, this attribute indicates\nthe relative space the container occupies on device-types larger than\ntablet. It is expressed as an integer from 1 through 12."
            },
            "large-device-size": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If the viewport is divided into 12 parts, this attribute indicates\nthe relative space the container occupies on device-types larger than\ndesktop. It is expressed as an integer from 1 through 12."
            }
        }
    },

    "lightning-map": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "show-footer": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "false",
                "description": "If present, the footer element is displayed below the map.\nThe footer shows an 'Open in Google Maps' link that opens an external window\nto display the selected marker location in Google Maps. Default value is false."
            },
            "list-view": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "auto",
                "description": "Displays or hides the list of locations. Valid values are visible, hidden, or auto.\nThis value defaults to auto, which shows the list only when multiple markers are present.\nPassing in an invalid value hides the list view."
            },
            "zoom-level": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The zoom levels as defined by Google Maps API.\nIf a zoom level is not specified, a default zoom level is applied to accommodate all markers on the map."
            },
            "center": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A location to use as the map's center.\nIf center is not specified, the map centers automatically."
            },
            "markers-title": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Provides the heading title for the markers. Required if specifying multiple markers.\nThe title is displayed below the map as a header for the list of clickable addresses."
            },
            "map-markers": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "One or more objects with the address or latitude and longitude to be displayed on the map.\nIf latitude and longitude are provided, the address is ignored."
            }
        }
    },

    "lightning-menu-item": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A value associated with the menu item."
            },
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Text of the menu item."
            },
            "icon-name": {
                "type": "Picklist",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The name of an icon to display after the text of the menu item.",
                "values": icon_names
            },
            "prefix-icon-name": {
                "type": "Picklist",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The name of an icon to display before the text of the menu item.",
                "values": icon_names
            },
            "href": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "URL for a link to use for the menu item."
            },
            "draft-alternative-text": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Describes the reason for showing the draft indicator.\nThis is required when is-draft is present on the lightning-menu-item tag."
            },
            "is-draft": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, a draft indicator is shown on the menu item.\nA draft indicator is denoted by blue asterisk on the left of the menu item.\nWhen you use a draft indicator, include alternative text for accessibility using draft-alternative-text."
            },
            "access-key": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The keyboard shortcut for the menu item."
            },
            "tab-index": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Reserved for internal use. Use tabindex instead to indicate if an element should be focusable.\ntabindex can be set to 0 or -1.\nThe default tabindex value is 0, which means that the menu item is focusable and\nparticipates in sequential keyboard navigation. The value -1 means\nthat the menu item is focusable but does not participate in keyboard navigation."
            },
            "disabled": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the menu item is disabled and users cannot interact with it."
            },
            "checked": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, a check mark displays on the left of the menu item if it's selected."
            }
        }
    },

    "lightning-navigation": {
        "simple": False,
        "type": "lwc",
        "attribs": {}
    },

    "lightning-output-field": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "field-class": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A CSS class for the outer element, in addition to the component's base classes."
            },
            "variant": {
                "type": "Picklist",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Changes the appearance of the output. Accepted variants\ninclude standard and label-hidden. This value defaults to standard."
            },
            "field-name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The API name of the field to be displayed."
            }
        }
    },

    "lightning-pill": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "href": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The URL of the page that the link goes to."
            },
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The text label that displays in the pill."
            },
            "name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The name for the pill. This value is optional and can be used to identify the pill in a callback."
            },
            "variant": {
                "type": "Picklist",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The variant changes the appearance of the pill.\nAccepted variants include link, plain, and plainLink.\nThe default variant is link, which creates a link in the pill when you specify the href attribute.\nThe plain variant renders the pill without a link and ignores the href attribute.\nThe plainLink variant is reserved for internal use."
            },
            "has-error": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the pill is shown with a red border and an error icon on the left of the label."
            },
            "is-plain-link": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Reserved for internal use. Specifies whether the element variant is a plain link."
            },
            "tab-index": {
                "type": "Integer",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Reserved for internal use. Use tabindex instead to indicate if an element should be focusable.\nA value of 0 means that the pill is focusable and\nparticipates in sequential keyboard navigation. A value of -1 means\nthat the pill is focusable but does not participate in keyboard navigation."
            },
            "aria-selected": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies the aria-selected of an element."
            },
            "role": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies the role of an element."
            }
        }
    },

    "lightning-pill-container": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Aria label for the pill container."
            },
            "variant": {
                "type": "Picklist",
                "values": ["standard", "bare"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "The variant changes the appearance of the pill container. Accepted variants\ninclude standard and bare. This value defaults to standard."
            },
            "single-line": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies whether to keep the pills in a single line."
            },
            "is-collapsible": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies whether the pill container can be collapsed."
            },
            "is-expanded": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies whether the pill container is expanded."
            },
            "items": {
                "type": "Object",
                "access": "global",
                "required": False,
                "default": "",
                "description": "An array of items to be rendered as pills in a container."
            }
        }
    },

    "lightning-platform-resource-loader": {
        "simple": False,
        "type": "lwc",
        "attribs": {}
    },

    "lightning-platform-show-toast-event": {
        "simple": False,
        "type": "lwc",
        "attribs": {}
    },

    "lightning-progress-bar": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "0",
                "description": "The percentage value of the progress bar."
            },
            "variant": {
                "type": "Picklist",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The variant changes the appearance of the progress bar.\nAccepted variants include base or circular.\nThis value defaults to base."
            },
            "size": {
                "type": "Picklist",
                "values": ["x-small", "small", "medium", "large"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "The size of the progress bar.\nValid values are x-small, small, medium, and large.\nThe default value is medium."
            }
        }
    },

    "lightning-progress-indicator": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "type": {
                "type": "Picklist",
                "values": ["base", "path"],
                "access": "global",
                "required": False,
                "default": "base",
                "description": "Changes the visual pattern of the indicator. Valid values are base and path.\nThe default is base."
            },
            "variant": {
                "type": "Picklist",
                "access": "global",
                "required": False,
                "default": "base",
                "description": "Changes the appearance of the progress indicator for the base type only.\nValid values are base or shaded. The shaded variant adds a light gray border to the step indicators.\nThe default is base."
            },
            "current-step": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Set current-step to match the value attribute of one of progress-step components.\nIf current-step is not provided, the value of the first progress-step component is used."
            },
            "has-error": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "false",
                "description": "If present, the current step is in error state and a warning icon is displayed on the step indicator.\nOnly the base type can display errors."
            }
        }
    },

    "lightning-radio-group": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "type": {
                "type": "Picklist",
                "values": ["radio", "button"],
                "access": "global",
                "required": False,
                "default": "radio",
                "description": "The style of the radio group. Options are radio or button. The default is radio."
            },
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Text label for the radio group."
            },
            "options": {
                "type": "List",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Array of label-value pairs for each radio button."
            },
            "message-when-value-missing": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Optional message displayed when no radio button is selected and the required attribute is set to true."
            },
            "name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies the name of the radio button group. Only only one button can be selected if a name is specified\nfor the group."
            },
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies the value of the selected radio button."
            },
            "disabled": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the radio group is disabled and users cannot interact with it."
            },
            "required": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, a radio button must be selected before the form can be submitted."
            },
            "variant": {
                "type": "Picklist",
                "values": ["label-hidden", "label-inline", "label-stacked"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "The variant changes the appearance of the radio group.\nAccepted variants include standard, label-hidden, label-inline, and label-stacked.\nThis value defaults to standard.\nUse label-hidden to hide the label but make it available to assistive technology.\nUse label-inline to horizontally align the label and radio group.\nUse label-stacked to place the label above the radio group."
            },
            "validity": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Represents the validity states that an element can be in, with respect to constraint validation."
            }
        }
    },

    "lightning-record-edit-form": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "field-names": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Reserved for internal use. Names of the fields to include in the form."
            },
            "record-type-id": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The ID of the record type, which is required if you created\nmultiple record types but don't have a default."
            },
            "form-class": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A CSS class for the form element."
            },
            "layout-type": {
                "type": "Picklist",
                "values": ["Compact", "Full"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "The type of layout to use to display the form fields. Possible values: Compact, Full."
            },
            "density": {
                "type": "Picklist",
                "values": ["compact", "comfy", "auto"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "Sets the arrangement style of fields and labels in the form.\nAccepted values are compact, comfy, and auto (default).\nUse compact to display fields and their labels on the same line.\nUse comfy to display fields below their labels.\nUse auto to let the component dynamically set\nthe density according to the user's Display Density setting\nand the width of the form."
            },
            "record-id": {
                "type": "TrackObject",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The ID of the record to be displayed."
            },
            "object-api-name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The API name of the object."
            }
        }
    },

    "lightning-record-form": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "record-type-id": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The ID of the record type, which is required if you created\nmultiple record types but don't have a default."
            },
            "mode": {
                "type": "Picklist",
                "values": ["view", "edit", "readonly"],
                "access": "global",
                "required": False,
                "default": "view",
                "description": "Specifies the interaction and display style for the form.\nPossible values: view, edit, readonly.\nIf a record ID is not provided, the default mode is edit, which displays a form to create new records.\nIf a record ID is provided, the default mode is view, which displays field values with edit icons on updateable fields."
            },
            "layout-type": {
                "type": "Picklist",
                "values": ["Compact", "Full"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "The type of layout to use to display the form fields. Possible values: Compact, Full.\nWhen creating a new record, only the full layout is supported."
            },
            "density": {
                "type": "Picklist",
                "values": ["compact", "comfy", "auto"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "Sets the arrangement style of fields and labels in the form.\nAccepted values are compact, comfy, and auto (default).\nUse compact to display fields and their labels on the same line.\nUse comfy to display fields below their labels.\nUse auto to let the component dynamically set\nthe density according to the user's Display Density setting\nand the width of the form."
            },
            "record-id": {
                "type": "TrackObject",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The ID of the record to be displayed."
            },
            "object-api-name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The API name of the object."
            },
            "columns": {
                "type": "Integer",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies the number of columns for the form."
            },
            "fields": {
                "type": "List",
                "access": "global",
                "required": False,
                "default": "",
                "description": "List of fields to be displayed. The fields display in the order you list them."
            }
        }
    },

    "lightning-record-view-form": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "density": {
                "type": "Picklist",
                "values": ["compact", "comfy", "auto"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "Sets the arrangement style of fields and labels in the form.\nAccepted values are compact, comfy, and auto (default).\nUse compact to display fields and their labels on the same line.\nUse comfy to display fields below their labels.\nUse auto to let the component dynamically set\nthe density according to the user's Display Density setting\nand the width of the form."
            },
            "record-id": {
                "type": "TrackObject",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The ID of the record to be displayed."
            },
            "object-api-name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The API name of the object."
            }
        }
    },

    "lightning-relative-date-time": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The timestamp or JavaScript Date object to be formatted."
            }
        }
    },

    "lightning-slider": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "size": {
                "type": "Picklist",
                "values": ["xx-small", "x-small", "small", "medium", "large"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "The size of the slider.\nThe default is an empty string, which sets the slider to the width of the viewport. Accepted values are x-small, small, medium, and large."
            },
            "type": {
                "type": "Picklist",
                "values": ["vertical", "horizontal"],
                "access": "global",
                "required": False,
                "default": "horizontal",
                "description": "The type determines the orientation of the slider. Accepted values are vertical and horizontal. The default is horizontal."
            },
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Text label to describe the slider. Provide your own label to describe the slider."
            },
            "message-when-range-overflow": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when a range overflow is detected."
            },
            "message-when-range-underflow": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when a range underflow is detected."
            },
            "message-when-step-mismatch": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when a step mismatch is detected."
            },
            "message-when-value-missing": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when the value is missing."
            },
            "message-when-too-long": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when the value is too long."
            },
            "message-when-bad-input": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when a bad input is detected."
            },
            "message-when-pattern-mismatch": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when a pattern mismatch is detected."
            },
            "message-when-type-mismatch": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when a type mismatch is detected."
            },
            "min": {
                "type": "Number",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The minimum value of the input range. The default is 0."
            },
            "max": {
                "type": "Number",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The maximum value of the input range. The default is 100."
            },
            "step": {
                "type": "Number",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The step increment value of the input range.\nExample steps include 0.1, 1, or 10. The default is 1."
            },
            "disabled": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the slider is disabled and users cannot interact with it."
            },
            "variant": {
                "type": "Picklist",
                "values": ["standard", "label-hidden"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "The variant changes the appearance of the slider.\nAccepted variants include standard and label-hidden.\nThe default is standard."
            },
            "value": {
                "type": "Integer",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The numerical value of the slider. The default is 0."
            },
            "validity": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Represents the validity states of the slider input, with respect to constraint validation."
            }
        }
    },

    "lightning-spinner": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "alternative-text": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The alternative text used to describe the reason for the wait and need for a spinner."
            },
            "size": {
                "type": "Picklist",
                "values": ["small", "medium", "large"],
                "access": "global",
                "required": False,
                "default": "medium",
                "description": "The size of the spinner. Accepted sizes are small, medium, and large. This value defaults to medium."
            },
            "variant": {
                "type": "Picklist",
                "values": ["base", "brand", "inverse"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "The variant changes the appearance of the spinner.\nAccepted variants include base, brand, and inverse. The default is base."
            }
        }
    },

    "lightning-tab": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The optional string to be used during tabset's select event to determine which tab was clicked.\nThis string is also used by active-tab-value in tabset to open a tab."
            },
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The text displayed in the tab header."
            },
            "title": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies text that displays in a tooltip over the tab content."
            },
            "icon-name": {
                "type": "Picklist",
                "values": icon_names,
                "access": "global",
                "required": False,
                "default": "",
                "description": "The Lightning Design System name of an icon to display to the left of the tab label.\nSpecify the name in the format 'utility:down' where 'utility' is the category, and\n'down' is the icon to be displayed. Only utility icons can be used."

            },
            "icon-assistive-text": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The alternative text for the icon specified by icon-name."
            },
            "show-error-indicator": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies whether there's an error in the tab content.\nAn error icon is displayed to the right of the tab label."
            }
        }
    },

    "lightning-tabset": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "title": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Displays tooltip text when the mouse moves over the tabset."
            },
            "variant": {
                "type": "Picklist",
                "values": ["standard", "scoped", "vertical"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "The variant changes the appearance of the tabset. Accepted variants are standard, scoped, and vertical."
            },
            "active-tab-value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Sets a specific tab to open by default using a string that matches a tab's value string. If not used, the first tab opens by default."
            }
        }
    },

    "lightning-textarea": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Text that describes the textarea input field."
            },
            "placeholder": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Text that is displayed when the field is empty,\nto prompt the user for a valid entry."
            },
            "name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Specifies the name of an input element."
            },
            "message-when-bad-input": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when a bad input is detected."
            },
            "message-when-too-short": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when the value is too short."
            },
            "message-when-too-long": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when the value is too long."
            },
            "message-when-value-missing": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Error message to be displayed when the value is missing."
            },
            "access-key": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The keyboard shortcut for input field."
            },
            "max-length": {
                "type": "Integer",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The maximum number of characters allowed in the textarea."
            },
            "min-length": {
                "type": "Integer",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The minimum number of characters allowed in the textarea."
            },
            "value": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The value of the textarea input, also used as the default value during init."
            },
            "disabled": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the textarea field is disabled and users cannot interact with it."
            },
            "read-only": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the textarea field is read-only and cannot be edited."
            },
            "required": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the textarea field must be filled out before the form can be submitted."
            },
            "variant": {
                "type": "Picklist",
                "values": ["standard", "label-hidden", "label-inline", "label-stacked"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "The variant changes the appearance of the textarea.\nAccepted variants include standard, label-hidden, label-inline, and label-stacked.\nThis value defaults to standard.\nUse label-hidden to hide the label but make it available to assistive technology.\nUse label-inline to horizontally align the label and textarea.\nUse label-stacked to place the label above the textarea."
            },
            "validity": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Represents the validity states of the textarea input, with respect to constraint validation."
            },
            "field-level-help": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The help text that appears in a popover.\nSet field-level help to provide an informational tooltip on the textarea input field."
            }
        }
    },

    "lightning-tile": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The text label that displays in the tile as the heading and hover text."
            },
            "href": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The URL of the page that the link goes to."
            },
            "actions": {
                "type": "List",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A list of actions that's displayed in a dropdown menu."
            },
            "type": {
                "type": "Picklist",
                "values": ["standard", "media"],
                "access": "global",
                "required": False,
                "default": "",
                "description": "The tile type. Valid values are 'standard' and 'media'.\nThe default is 'standard'."
            }
        }
    },

    "lightning-tree": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "header": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The text that's displayed as the tree heading."
            },
            "items": {
                "type": "List",
                "access": "global",
                "required": False,
                "default": "",
                "description": "An array of key-value pairs that describe the tree. See the Documentation tab for more information."
            }
        }
    },

    "lightning-tree-grid": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "hide-checkbox-column": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "false",
                "description": "If present, the checkbox column for row selection is hidden."
            },
            "is-loading": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "false",
                "description": "If present, a spinner is displayed to indicate that more data is being loaded."
            },
            "key-field": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Required for better performance. Associates each row with a unique ID."
            },
            "max-column-width": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The maximum width for all columns. The default is 1000px."
            },
            "min-column-width": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The minimum width for all columns. The default is 50px."
            },
            "resize-column-disabled": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "false",
                "description": "If present, column resizing is disabled."
            },
            "row-number-offset": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Determines where to start counting the row number. The default is 0."
            },
            "selected-rows": {
                "type": "List",
                "access": "global",
                "required": False,
                "default": "[]",
                "description": "The array of unique row IDs that are selected."
            },
            "show-row-number-column": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "false",
                "description": "If present, the row number column are shown in the first column."
            },
            "columns": {
                "type": "List",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Array of the columns object that's used to define the data types.\nRequired properties include 'label', 'fieldName', and 'type'. The default type is 'text'.\nSee the Documentation tab for more information."
            },
            "data": {
                "type": "List",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The array of data to be displayed."
            },
            "expanded-rows": {
                "type": "List",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The array of unique row IDs for rows that are expanded."
            }
        }
    },

    "lightning-ui-list-api": {
        "simple": False,
        "type": "lwc",
        "attribs": {}
    },

    "lightning-ui-object-info-api": {
        "simple": False,
        "type": "lwc",
        "attribs": {}
    },

    "lightning-ui-record-api": {
        "simple": False,
        "type": "lwc",
        "attribs": {}
    },

    "lightning-vertical-navigation": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "compact": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, spacing between navigation items is reduced."
            },
            "shaded": {
                "type": "Boolean",
                "access": "global",
                "required": False,
                "default": "",
                "description": "If present, the vertical navigation is displayed on top of a shaded background."
            },
            "selected-item": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Name of the navigation item to make active.\nAn active item is highlighted in blue."
            }
        }
    },

    "lightning-vertical-navigation-item": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The text displayed for the navigation item."
            },
            "name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A unique identifier for the navigation item.\nThe name is used by the `select` event on lightning-vertical-navigation to identify which item is selected."
            },
            "href": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The URL of the page that the navigation item goes to."
            }
        }
    },

    "lightning-vertical-navigation-item-badge": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The text displayed for this navigation item."
            },
            "name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A unique identifier for this navigation item."
            },
            "badge-count": {
                "type": "Integer",
                "access": "global",
                "required": False,
                "default": "0",
                "description": "The number to show inside the badge. If this value is zero, the badge is hidden.\nThe default value is zero."
            },
            "assistive-text": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "Assistive text describing the number in the badge, which enhances accessibility and is not displayed to the user.\nThe default is \"New Items\"."
            },
            "href": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The URL of the page that the navigation item goes to."
            }
        }
    },

    "lightning-vertical-navigation-item-icon": {
        "simple": False,
        "type": "lwc",
        "attribs": {
            "label": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The text displayed for this navigation item."
            },
            "name": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "A unique identifier for this navigation item."
            },
            "icon-name": {
                "type": "Picklist",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The Lightning Design System name of the icon.\nNames are written in the format 'utility:down' where 'utility' is the category,\nand 'down' is the specific icon to be displayed.",
                "values": icon_names
            },
            "href": {
                "type": "String",
                "access": "global",
                "required": False,
                "default": "",
                "description": "The URL of the page that the navigation item goes to."
            }
        }
    }
}
