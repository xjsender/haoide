# Attributes which type is ApexPages.PageReference
page_reference_attrs = [
    "page",
    "template",
    "pageName",
    "finishLocation"
]

# ["apex", "messaging","chatter", "chatteranswers", "chatteranswers", "flow", "ideas", "site", "social", "support"]

tag_defs = {
    "apex:actionFunction": {
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
            "reRender": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            },
            "status": {
                "type": "String"
            },
            "timeout": {
                "type": "Integer"
            }
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:actionPoller": {
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
            "reRender": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            },
            "status": {
                "type": "String"
            },
            "timeout": {
                "type": "Integer"
            }
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:actionRegion": {
        "attribs": {
            "id": {
                "type": "String"
            },
            "immediate": {
                "type": "Boolean"
            },
            "renderRegionOnly": {
                "type": "Boolean"
            },
            "rendered": {
                "type": "Boolean"
            }
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:actionStatus": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:actionSupport": {
        "attribs": {
            "action": {
                "type": "ApexPages.Action"
            },
            "disableDefault": {
                "type": "Boolean"
            },
            "disabled": {
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
            "reRender": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            },
            "status": {
                "type": "String"
            },
            "timeout": {
                "type": "Integer"
            }
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:areaSeries": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:attribute": {
        "attribs": {
            "access": {
                "type": "Picklist",
                "values": [
                    "public",
                    "global"
                ]
            },
            "assignTo": {
                "type": "Object"
            },
            "default": {
                "type": "Boolean"
            },
            "description": {
                "type": "String"
            },
            "encode": {
                "type": "String"
            },
            "id": {
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
                    "Object"
                ]
            }
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:axis": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:barSeries": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:canvasApp": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:chart": {
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
            "renderTo": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:chartLabel": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:chartTips": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:column": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:commandButton": {
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
            "reRender": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:commandLink": {
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
            "reRender": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:component": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:componentBody": {
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:composition": {
        "attribs": {
            "rendered": {
                "type": "String"
            },
            "template": {
                "type": "ApexPages.PageReference"
            }
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:dataList": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:dataTable": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:define": {
        "attribs": {
            "name": {
                "type": "String"
            }
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:detail": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:dynamicComponent": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:emailPublisher": {
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
            "reRender": {
                "type": "Object"
            },
            "rendered": {
                "type": "Boolean"
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
        },
        "type": "visualforce"
    },
    "apex:enhancedList": {
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
            "reRender": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:facet": {
        "attribs": {
            "name": {
                "type": "String"
            }
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:flash": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:form": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:gaugeSeries": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:iframe": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:image": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:include": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:includeLightning": {
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:includeScript": {
        "attribs": {
            "id": {
                "type": "String"
            },
            "value": {
                "type": "Object",
                "values": [
                    "{!URLFOR(\\$Resource.$1, '$2')}",
                    "{!\\$Resource.$1}"
                ]
            }
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:inlineEditSupport": {
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
        },
        "simple": True,
        "type": "visualforce"
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
        },
        "type": "visualforce"
    },
    "apex:inputCheckbox": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:inputField": {
        "attribs": {
            "id": {
                "type": "String"
            },
            "label": {
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
            "onselect": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            },
            "required": {
                "type": "Boolean"
            },
            "showDatePicker": {
                "type": "Boolean"
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:inputFile": {
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
                "type": "java:\\/\\/java.lang.Boolean"
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:inputHidden": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:inputSecret": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:inputText": {
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
            "lang": {
                "type": "String"
            },
            "list": {
                "type": "Object"
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:inputTextarea": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:insert": {
        "attribs": {
            "name": {
                "type": "String"
            }
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:legend": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:lineSeries": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:listViews": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:logCallPublisher": {
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
            "reRender": {
                "type": "Object"
            },
            "rendered": {
                "type": "Boolean"
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
        },
        "type": "visualforce"
    },
    "apex:map": {
        "attribs": {
            "center": {
                "type": "Object",
                "values": [
                    "${1:1 Market Street, San Francisco, CA}",
                    "${1:{latitude: 37.794, longitude: -122.395\\}}",
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
        },
        "type": "visualforce"
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
                "type": "Boolean"
            }
        },
        "type": "visualforce"
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
                    "${1:{latitude: 37.794, longitude: -122.395\\}}",
                    "${1:Map<String, Double>}"
                ]
            },
            "rendered": {
                "type": "Boolean"
            },
            "title": {
                "type": "String"
            }
        },
        "type": "visualforce"
    },
    "apex:message": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:messages": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:milestoneTracker": {
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
        },
        "type": "visualforce"
    },
    "apex:outputField": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:outputLabel": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:outputLink": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:outputPanel": {
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
                    "inline",
                    "block",
                    "none"
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:outputText": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:page": {
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
                    "application/vnd.ms-doc#${1:fileName}",
                    "application/vnd.ms-ppt#${1:fileName}",
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
                "type": "Picklist",
                "values": [
                    "html-4.01-strict",
                    "xhtml-1.0-transitional",
                    "xhtml-1.1-basic",
                    "html-5.0"
                ]
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
            "lightningStylesheets": {
                "type": "Boolean"
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
            "showQuickActionVfHeader": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:pageBlock": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:pageBlockButtons": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:pageBlockSection": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:pageBlockSectionItem": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:pageBlockTable": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:pageMessage": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:pageMessages": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:panelBar": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:panelBarItem": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:panelGrid": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:panelGroup": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:param": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:pieSeries": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:radarSeries": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:relatedList": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:remoteObjectField": {
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
        },
        "simple": False,
        "type": "visualforce"
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
                "type": "Boolean"
            },
            "retrieve": {
                "type": "String"
            },
            "update": {
                "type": "String"
            }
        },
        "type": "visualforce"
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
                "type": "Boolean"
            },
            "retrieve": {
                "type": "String"
            },
            "update": {
                "type": "String"
            }
        },
        "type": "visualforce"
    },
    "apex:repeat": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:scatterSeries": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:scontrol": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:sectionHeader": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:selectCheckboxes": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:selectList": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:selectOption": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:selectOptions": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:selectRadio": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:slds": {
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:stylesheet": {
        "attribs": {
            "id": {
                "type": "String"
            },
            "value": {
                "type": "Object",
                "values": [
                    "{!URLFOR(\\$Resource.$1, '$2')}",
                    "{!\\$Resource.$1}"
                ]
            }
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:tab": {
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
            "reRender": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:tabPanel": {
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
            "reRender": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:toolbar": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:toolbarGroup": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "apex:variable": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "apex:vote": {
        "attribs": {
            "id": {
                "type": "String"
            },
            "objectId": {
                "type": "String"
            },
            "reRender": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        },
        "simple": False,
        "type": "visualforce"
    },
    "chatter:feed": {
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
            "reRender": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            },
            "showPublisher": {
                "type": "Boolean"
            }
        },
        "simple": True,
        "type": "visualforce"
    },
    "chatter:feedWithFollowers": {
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
            "reRender": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            },
            "showHeader": {
                "type": "Boolean"
            }
        },
        "simple": True,
        "type": "visualforce"
    },
    "chatter:follow": {
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
            "reRender": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        },
        "simple": True,
        "type": "visualforce"
    },
    "chatter:followers": {
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
        },
        "simple": True,
        "type": "visualforce"
    },
    "chatter:newsfeed": {
        "attribs": {
            "id": {
                "type": "String"
            },
            "onComplete": {
                "type": "String"
            },
            "reRender": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        },
        "simple": True,
        "type": "visualforce"
    },
    "chatter:userPhotoUpload": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "chatteranswers:aboutme": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "chatteranswers:allfeeds": {
        "attribs": {
            "articleLanguage": {
                "type": "String"
            },
            "communityId": {
                "type": "id"
            },
            "filterOptions": {
                "type": "Picklist",
                "values": [
                    "AllQuestions",
                    "UnansweredQuestions",
                    "UnsolvedQuestions",
                    "SolvedQuestions",
                    "MyQuestions",
                    "MostPopular",
                    "DatePosted",
                    "RecentActivity"
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "chatteranswers:changepassword": {
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        },
        "simple": False,
        "type": "visualforce"
    },
    "chatteranswers:datacategoryfilter": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "chatteranswers:feedfilter": {
        "attribs": {
            "filterOptions": {
                "type": "Picklist",
                "values": [
                    "AllQuestions",
                    "UnansweredQuestions",
                    "UnsolvedQuestions",
                    "SolvedQuestions",
                    "MyQuestions",
                    "MostPopular",
                    "DatePosted",
                    "RecentActivity"
                ]
            },
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        },
        "simple": False,
        "type": "visualforce"
    },
    "chatteranswers:feeds": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "chatteranswers:forgotpassword": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "chatteranswers:forgotpasswordconfirm": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "chatteranswers:guestsignin": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "chatteranswers:help": {
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        },
        "simple": False,
        "type": "visualforce"
    },
    "chatteranswers:login": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "chatteranswers:registration": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "chatteranswers:searchask": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "chatteranswers:singleitemfeed": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "flow:interview": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
"ideas:detailOutputLink": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "ideas:listOutputLink": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "ideas:profileListOutputLink": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "messaging:attachment": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "messaging:emailHeader": {
        "attribs": {
            "id": {
                "type": "String"
            },
            "name": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        },
        "simple": False,
        "type": "visualforce"
    },
    "messaging:emailTemplate": {
        "attribs": {
            "id": {
                "type": "String"
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
            "rendered": {
                "type": "Boolean"
            },
            "replyTo": {
                "type": "String"
            },
            "subject": {
                "type": "String"
            }
        },
        "simple": False,
        "type": "visualforce"
    },
    "messaging:htmlEmailBody": {
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        },
        "simple": False,
        "type": "visualforce"
    },
    "messaging:plainTextEmailBody": {
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        },
        "simple": False,
        "type": "visualforce"
    },
    "site:googleAnalyticsTracking": {
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        },
        "simple": False,
        "type": "visualforce"
    },
    "site:previewAsAdmin": {
        "attribs": {
            "id": {
                "type": "String"
            },
            "rendered": {
                "type": "Boolean"
            }
        },
        "simple": False,
        "type": "visualforce"
    },
    "social:profileViewer": {
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
        },
        "simple": False,
        "type": "visualforce"
    },
    "support:clickToDial": {
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
        },
        "simple": False,
        "type": "visualforce"
    }
}
