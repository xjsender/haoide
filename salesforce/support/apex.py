apex_namespaces = {
     # "Schema" : ["SoapType", "SObjectField", "DisplayType", "SObjectType", "DataCategoryGroupSobjectTypePair"],
    "Process" : ["Plugin", "PluginResult", "PluginRequest", "ParameterType", "SparkPlugDescribeResult", "OutputParameter", "SparkPlugApi", "SparkPlugParameter", "InputParameter", "PluginDescribeResult"],
    "dom" : ["XmlNode", "Document", "XmlNodeType"],
     # "Database" : ["AssignmentRuleHeader", "QueryLocatorIterator", "BatchableContext", "Batchable", "QueryLocator", "BatchableContextImpl", "QueryLocatorChunkIterator", "LeadConvert", "DMLOptions", "EmailHeader"],
     # "Messaging" : ["BinaryAttachment", "EmailFileAttachment", "Header", "TextAttachment", "MassEmailMessage", "EmailToSalesforceHandler", "InboundEmailResult", "SingleEmailMessage", "InboundEmail", "EmailAttachment", "InboundEnvelope", "InboundEmailHandler"],
    "Flow" : ["Interview"],
     # "Site" : ["UrlRewriter"],
    "ConnectApi" : ["FeedItemAttachmentType", "PollAttachmentInput", "ChatterGroupPage", "MentionSegmentInput", "Address", "MessageSegment", "TextSegment", "FollowingCounts", "ChatterGroupDetail", "FollowerPage", "ChatterGroups", "ChatterActivity", "GroupInformation", "UnauthenticatedUser", "ConnectApiException", "Community", "Motif", "ContentAttachment", "ChatterLikePage", "Actor", "Features", "MoreChangesSegment", "ChatterLike", "ApprovalAttachment", "WorkflowProcessStatus", "ChatterFavorites", "MessageSegmentType", "Records", "BinaryInput", "FeedModifiedInfo", "Communities", "ChatterUsers", "NewFileAttachmentInput", "FeedItemInput", "FollowingPage", "UserChatterSettings", "Reference", "ComplexSegment", "CaseComment", "GroupMembershipRequestStatus", "MessageSegmentInput", "FeedSortOrder", "TextSegmentInput", "ChatterGroupInput", "ActorWithId", "ChatterFeeds", "FeedType", "ClientInfo", "ApprovalPostTemplateField", "Organization", "OrganizationSettings", "FeedItemType", "DashboardComponentAttachment", "FeedItemVisibilityType", "GroupVisibilityType", "GroupMembershipRequest", "FeedPoll", "BasicTemplateAttachment", "UserDetail", "FeedItem", "Chatter", "ChatterGroupSummary", "CommentInput", "FeedFavorite", "RecordSummary", "FieldChangeNameSegment", "User", "ChatterGroup", "GroupEmailFrequency", "UserPage", "GroupMembershipRequests", "CommentPage", "ContentAttachmentInput", "UserSummary", "UserGroupPage", "MentionSegment", "MessageBodyInput", "GroupMemberPage", "CommentType", "Icon", "Photo", "FieldChangeSegment", "FeedFavoriteType", "FileSummary", "CaseActorType", "HashtagSegment", "FeedBody", "PhoneNumber", "FeedItemPage", "LinkSegmentInput", "LinkSegment", "UserSettings", "MessageBody", "Feed", "GroupChatterSettings", "HashtagSegmentInput", "RateLimitException", "EntityLinkSegment", "GroupMember", "LinkAttachmentInput", "UserType", "FeedItemAttachment", "FieldChangeValueSegment", "FeedItemAttachmentInput", "CommunityPage", "Subscription", "ResourceLinkSegment", "NotFoundException", "GroupInformationInput", "FeedFavorites", "Comment", "FeedPollChoice", "GroupMembershipType", "AbstractMessageBody", "LinkAttachment", "GlobalInfluence", "CommunityStatus"],
    "MobilePNS" : ["MobilePushNotification", "MobilePushPayload"],
     # "System" : ["CalloutException", "Iterator", "InvalidParameterValueException", "BusinessHours", "NoSuchElementException", "LoggingLevel", "System", "XmlTag", "NonePointerException", "WebServiceMock", "TimeZone", "Site", "NoAccessException", "HttpCalloutMock", "Datetime", "TouchHandledException", "String", "DmlException", "Integer", "RestContext", "Map", "JSONGenerator", "XmlException", "ListException", "ApexPages", "ProcedureException", "Cases", "SetupScope", "StringException", "NoDataFoundException", "SerializationException", "JSONToken", "Id", "SearchException", "InvalidReadOnlyUserDmlException", "SchedulableContext", "Cookie", "InvalidHeaderException", "Set", "StatusCode", "CURRENCY", "JSONException", "Database", "AssertException", "EncodingUtil", "Test", "RestRequest", "Boolean", "EmailException", "FinalException", "Date", "UnexpectedException", "Exception", "Schedulable", "Type", "Version", "PageReference", "Long", "Comparable", "Math", "Blob", "Answers", "AppExchange", "Schema", "HandledException", "RequiredFeatureMissingException", "Iterable", "JSON", "HttpResponse", "Time", "MathException", "LimitException", "Communities", "RestResponse", "SelectOption", "SObjectException", "XmlStreamReader", "JSONParser", "MultiStaticResourceCalloutMock", "Double", "SecurityException", "Url", "TypeException", "Network", "FlowException", "Crypto", "List", "Decimal", "SObject", "UnsupportedOperationException", "AsyncException", "Http", "XmlStreamWriter", "Matcher", "StaticResourceCalloutMock", "ApplicationReadWriteMode", "Messaging", "VisualforceException", "QueryException", "LicenseException", "Pattern", "HttpRequest", "Ideas", "UserInfo"],
    "KbManagement" : ["PublishingService"],
    "Support" : ["EmailToCaseHandler", "EmailTemplateSelector"],
     # "ApexPages" : ["IdeaStandardSetController", "Component", "StandardController", "IdeaStandardController", "KnowledgeArticleVersionStandardController", "ComponentIteration", "StandardSetController", "Message", "Severity", "Action"],
    "Apex" : ["Stack", "EmptyStackException"]
}

apex_completions = {
    "limits" : {
        "name" : "Limits",
        "constructors" : {},
        "properties" : {},
        "customize" : True,
        "methods" : {
            "getAggregateQueries()\tInteger" : "getAggregateQueries()$0",
            "getLimitAggregateQueries()\tInteger" : "getLimitAggregateQueries()$0",
            "getCallouts()\tInteger" : "getCallouts()$0",
            "getLimitCallouts()\tInteger" : "getLimitCallouts()$0",
            "getChildRelationshipsDescribes()\tInteger" : "getChildRelationshipsDescribes()$0",
            "getLimitChildRelationshipsDescribes()\tInteger" : "getLimitChildRelationshipsDescribes()$0",
            "getCpuTime()\tInteger" : "getCpuTime()$0",
            "getLimitCpuTime()\tInteger" : "getLimitCpuTime()$0",
            "getDMLRows()\tInteger" : "getDMLRows()$0",
            "getLimitDMLRows()\tInteger" : "getLimitDMLRows()$0",
            "getDMLStatements()\tInteger" : "getDMLStatements()$0",
            "getLimitDMLStatements()\tInteger" : "getLimitDMLStatements()$0",
            "getFieldsDescribes()\tInteger" : "getFieldsDescribes()$0",
            "getLimitFieldsDescribes()\tInteger" : "getLimitFieldsDescribes()$0",
            "getFutureCalls()\tInteger" : "getFutureCalls()$0",
            "getLimitFutureCalls()\tInteger" : "getLimitFutureCalls()$0",
            "getHeapSize()\tInteger" : "getHeapSize()$0",
            "getLimitHeapSize()\tInteger" : "getLimitHeapSize()$0",
            "getInteractionQueries()\tInteger" : "getInteractionQueries()$0",
            "getLimitInteractionQueries()\tInteger" : "getLimitInteractionQueries()$0",
            "getQueries()\tInteger" : "getQueries()$0",
            "getLimitQueries()\tInteger" : "getLimitQueries()$0",
            "getPickListDescribes()\tInteger" : "getPickListDescribes()$0",
            "getLimitPickListDescribes()\tInteger" : "getLimitPickListDescribes()$0",
            "getQueryLocatorRows()\tInteger" : "getQueryLocatorRows()$0",
            "getLimitQueryLocatorRows()\tInteger" : "getLimitQueryLocatorRows()$0",
            "getQueryRows()\tInteger" : "getQueryRows()$0",
            "getLimitQueryRows()\tInteger" : "getLimitQueryRows()$0",
            "getRecordTypesDescribes()\tInteger" : "getRecordTypesDescribes()$0",
            "getLimitRecordTypesDescribes()\tInteger" : "getLimitRecordTypesDescribes()$0",
            "getSoslQueries()\tInteger" : "getSoslQueries()$0",
            "getLimitSoslQueries()\tInteger" : "getLimitSoslQueries()$0"
        }
    },
    "saveresult" : {
        "name" : "SaveResult",
        "constructors" : {},
        "properties" : {},
        "customize" : True,
        "methods" : {
            "getErrors()\tDatabase.Error[]" : "getErrors()$0",
            "getId()\tId" : "getId()$0",
            "isSuccess()\tBoolean" : "isSuccess()$0"
        }
    },
    "singleemailmessage" : {
        "name" : "SingleEmailMessage",
        "constructors" : {},
        "properties" : {},
        "customize" : True,
        "methods" : {
            "setBccAddresses(String[])\tvoid" : "setBccAddresses($1)$0",
            "setCcAddresses(String[])\tvoid" : "setCcAddresses($1)$0",
            "setCharset(String)\tvoid" : "setCharset($1)$0",
            "setDocumentAttachments(ID[])\tvoid" : "setDocumentAttachments($1)$0",
            "setFileAttachments(EmailFileAttachment[])\tvoid" : "setFileAttachments($1)$0",
            "setHtmlBody(String)\tvoid" : "setHtmlBody($1)$0",
            "setInReplyTo(String)\tvoid" : "setInReplyTo($1)$0",
            "setPlainTextBody(String)\tvoid" : "setPlainTextBody($1)$0",
            "setOrgWideEmailAddressId(ID)\tvoid" : "setOrgWideEmailAddressId($1)$0",
            "setReferences(String)\tvoid" : "setReferences($1)$0",
            "setSubject(String)\tvoid" : "setSubject($1)$0",
            "setTargetObjectId(ID)\tvoid" : "setTargetObjectId($1)$0",
            "setToAddresses(String[])\tvoid" : "setToAddresses($1)$0",
            "setWhatId()\tvoid" : "setWhatId($1)$0"
        }
    },
    "trigger" : {
        "name" : "Trigger",
        "constructors" : {},
        "methods" : {},
        "customize" : True,
        "properties" : {
            "isExecuting\tBoolean" : "isExecuting$0",
            "isInsert\tBoolean" : "isInsert$0",
            "isUpdate\tBoolean" : "isUpdate$0",
            "isDelete\tBoolean" : "isDelete$0",
            "isBefore\tBoolean" : "isBefore$0",
            "isAfter\tBoolean" : "isAfter$0",
            "isUndelete\tBoolean" : "isUndelete$0",
            "new\tList<Sobject>" : "new$0",
            "newMap\tMap<Id, Sobject>" : "newMap$0",
            "old\tList<Sobject>" : "old$0",
            "oldMap\tMap<Id, Sobject>" : "oldMap$0",
            "size\tInteger" : "size$0"
        }
    },
    "organization" : {
        "constructors" : {},
        "name" : "Organization",
        "properties" : {},
        "methods" : {
            "getSettings()\tConnectApi.OrganizationSettings" : "getSettings()$0"
        }
    },
    "getdeletedresult" : {
        "constructors" : {},
        "name" : "GetDeletedResult",
        "properties" : {},
        "methods" : {
            "getDeletedRecords()\tLIST<Database.DeletedRecord>" : "getDeletedRecords()$0",
            "getEarliestDateAvailable()\tDate" : "getEarliestDateAvailable()$0",
            "getLatestDateCovered()\tDate" : "getLatestDateCovered()$0"
        }
    },
    "pollattachmentinput" : {
        "constructors" : {},
        "name" : "PollAttachmentInput",
        "properties" : {
            "pollChoices" : "pollChoices$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object" : "convertToJavaObject($1)$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "chatter" : {
        "constructors" : {},
        "name" : "Chatter",
        "properties" : {},
        "methods" : {
            "getFollowers(String communityId, String recordId, Integer pageParam, Integer pageSize)\tConnectApi.FollowerPage" : "getFollowers($1)$0",
            "getFollowers(String communityId, String recordId)\tConnectApi.FollowerPage" : "getFollowers($1)$0",
            "getSubscription(String communityId, String subscriptionId)\tConnectApi.Subscription" : "getSubscription($1)$0",
            "deleteSubscription(String communityId, String subscriptionId)\tvoid" : "deleteSubscription($1)$0"
        }
    },
    "inboundemailresult" : {
        "constructors" : {},
        "name" : "InboundEmailResult",
        "properties" : {
            "message" : "message$0",
            "success" : "success$0"
        },
        "methods" : {}

    },
    "dmloptions" : {
        "constructors" : {},
        "name" : "DMLOptions",
        "properties" : {
            "LocaleOptions" : "LocaleOptions$0",
            "EmailHeader" : "EmailHeader$0",
            "AssignmentRuleHeader" : "AssignmentRuleHeader$0",
            "OptAllOrNone" : "OptAllOrNone$0",
            "AllowFieldTruncation" : "AllowFieldTruncation$0"
        },
        "methods" : {}

    },
    "feeditempage" : {
        "constructors" : {},
        "name" : "FeedItemPage",
        "properties" : {
            "isModifiedToken" : "isModifiedToken$0",
            "items" : "items$0",
            "isModifiedUrl" : "isModifiedUrl$0",
            "currentPageUrl" : "currentPageUrl$0",
            "nextPageUrl" : "nextPageUrl$0",
            "currentPageToken" : "currentPageToken$0",
            "nextPageToken" : "nextPageToken$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "plugindescriberesult" : {
        "constructors" : {},
        "name" : "PluginDescribeResult",
        "properties" : {
            "outputParameters" : "outputParameters$0",
            "tag" : "tag$0",
            "inputParameters" : "inputParameters$0",
            "name" : "name$0",
            "description" : "description$0"
        },
        "methods" : {}

    },
    "messagebody" : {
        "constructors" : {},
        "name" : "MessageBody",
        "properties" : {},
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "linksegmentinput" : {
        "constructors" : {},
        "name" : "LinkSegmentInput",
        "properties" : {
            "url" : "url$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object" : "convertToJavaObject($1)$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "linkattachmentinput" : {
        "constructors" : {},
        "name" : "LinkAttachmentInput",
        "properties" : {
            "urlName" : "urlName$0",
            "url" : "url$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object" : "convertToJavaObject($1)$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "parametertype" : {
        "constructors" : {},
        "name" : "ParameterType",
        "properties" : {
            "FLOAT" : "FLOAT$0",
            "DECIMAL" : "DECIMAL$0",
            "DOUBLE" : "DOUBLE$0",
            "DATE" : "DATE$0",
            "DATETIME" : "DATETIME$0",
            "LONG" : "LONG$0",
            "ID" : "ID$0",
            "BOOLEAN" : "BOOLEAN$0",
            "INTEGER" : "INTEGER$0",
            "STRING" : "STRING$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0",
            "values()\tLIST<Process.PluginDescribeResult.ParameterType>" : "values()$0"
        }
    },
    "topicpage" : {
        "constructors" : {},
        "name" : "TopicPage",
        "properties" : {
            "currentPageUrl" : "currentPageUrl$0",
            "nextPageUrl" : "nextPageUrl$0",
            "topics" : "topics$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "deleteresult" : {
        "constructors" : {},
        "name" : "DeleteResult",
        "properties" : {},
        "methods" : {
            "getErrors()\tLIST<Database.Error>" : "getErrors()$0",
            "isSuccess()\tBoolean" : "isSuccess()$0",
            "getId()\tId" : "getId()$0"
        }
    },
    "httpresponse" : {
        "constructors" : {},
        "name" : "HttpResponse",
        "properties" : {},
        "methods" : {
            "setHeader(String key, String value)\tvoid" : "setHeader($1)$0",
            "getXmlStreamReader()\tSystem.XmlStreamReader" : "getXmlStreamReader()$0",
            "getStatusCode()\tInteger" : "getStatusCode()$0",
            "getBody()\tString" : "getBody()$0",
            "getStatus()\tString" : "getStatus()$0",
            "getHeaderKeys()\tLIST<String>" : "getHeaderKeys()$0",
            "setStatus(String status)\tvoid" : "setStatus($1)$0",
            "setBodyAsBlob(Blob body)\tvoid" : "setBodyAsBlob($1)$0",
            "getBodyAsBlob()\tBlob" : "getBodyAsBlob()$0",
            "getBodyDocument()\tdom.Document" : "getBodyDocument()$0",
            "toString()\tString" : "toString()$0",
            "setBody(String body)\tvoid" : "setBody($1)$0",
            "getHeader(String key)\tString" : "getHeader($1)$0",
            "setStatusCode(Integer statusCode)\tvoid" : "setStatusCode($1)$0"
        }
    },
    "reportformat" : {
        "constructors" : {},
        "name" : "ReportFormat",
        "properties" : {
            "MULTI_BLOCK" : "MULTI_BLOCK$0",
            "TABULAR" : "TABULAR$0",
            "SUMMARY" : "SUMMARY$0",
            "MATRIX" : "MATRIX$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<reports.ReportFormat>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "chatterconversation" : {
        "constructors" : {},
        "name" : "ChatterConversation",
        "properties" : {
            "read" : "read$0",
            "conversationId" : "conversationId$0",
            "conversationUrl" : "conversationUrl$0",
            "members" : "members$0",
            "messages" : "messages$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "describeiconresult" : {
        "constructors" : {},
        "name" : "DescribeIconResult",
        "properties" : {},
        "methods" : {
            "getUrl()\tString" : "getUrl()$0",
            "getWidth()\tInteger" : "getWidth()$0",
            "getTheme()\tString" : "getTheme()$0",
            "getContentType()\tString" : "getContentType()$0",
            "getHeight()\tInteger" : "getHeight()$0"
        }
    },
    "messagesegmenttype" : {
        "constructors" : {},
        "name" : "MessageSegmentType",
        "properties" : {
            "MoreChanges" : "MoreChanges$0",
            "FieldChange" : "FieldChange$0",
            "Hashtag" : "Hashtag$0",
            "FieldChangeName" : "FieldChangeName$0",
            "EntityLink" : "EntityLink$0",
            "Mention" : "Mention$0",
            "ResourceLink" : "ResourceLink$0",
            "FieldChangeValue" : "FieldChangeValue$0",
            "Text" : "Text$0",
            "Link" : "Link$0"
        },
        "methods" : {
            "values()\tLIST<ConnectApi.MessageSegmentType>" : "values()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "reportrunexception" : {
        "constructors" : {},
        "name" : "ReportRunException",
        "properties" : {},
        "methods" : {
            "getTypeName()\tString" : "getTypeName()$0"
        }
    },
    "mobilepushnotification" : {
        "constructors" : {},
        "name" : "MobilePushNotification",
        "properties" : {},
        "methods" : {
            "send(String application, SET<String> users)\tvoid" : "send($1)$0",
            "setPayload(MAP<String,ANY> payload)\tvoid" : "setPayload($1)$0",
            "setTtl(Integer ttl)\tvoid" : "setTtl($1)$0"
        }
    },
    "textattachment" : {
        "constructors" : {},
        "name" : "TextAttachment",
        "properties" : {
            "charset" : "charset$0",
            "mimeTypeSubType" : "mimeTypeSubType$0",
            "body" : "body$0",
            "fileName" : "fileName$0",
            "bodyIsTruncated" : "bodyIsTruncated$0"
        },
        "methods" : {}

    },
    "approvalposttemplatefield" : {
        "constructors" : {},
        "name" : "ApprovalPostTemplateField",
        "properties" : {
            "displayValue" : "displayValue$0",
            "record" : "record$0",
            "displayName" : "displayName$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "abstractrecordfield" : {
        "constructors" : {},
        "name" : "AbstractRecordField",
        "properties" : {
            "type" : "type$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "searchexception" : {
        "constructors" : {},
        "name" : "SearchException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "zonepage" : {
        "constructors" : {},
        "name" : "ZonePage",
        "properties" : {
            "currentPageUrl" : "currentPageUrl$0",
            "nextPageUrl" : "nextPageUrl$0",
            "zones" : "zones$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "feedmodifiedinfo" : {
        "constructors" : {},
        "name" : "FeedModifiedInfo",
        "properties" : {
            "isModifiedToken" : "isModifiedToken$0",
            "isModified" : "isModified$0",
            "nextPollUrl" : "nextPollUrl$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "topicsort" : {
        "constructors" : {},
        "name" : "TopicSort",
        "properties" : {
            "PopularDesc" : "PopularDesc$0",
            "AlphaAsc" : "AlphaAsc$0"
        },
        "methods" : {
            "values()\tLIST<ConnectApi.TopicSort>" : "values()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "interview" : {
        "constructors" : {},
        "name" : "Interview",
        "properties" : {},
        "methods" : {
            "getVariableValue(String variableName)\tObject" : "getVariableValue($1)$0"
        }
    },
    "icon" : {
        "constructors" : {},
        "name" : "Icon",
        "properties" : {
            "width" : "width$0",
            "url" : "url$0",
            "height" : "height$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "iterable" : {
        "constructors" : {},
        "name" : "Iterable",
        "properties" : {},
        "methods" : {
            "iterator()\tsystem.Iterator" : "iterator()$0"
        }
    },
    "selectoption" : {
        "constructors" : {},
        "name" : "SelectOption",
        "properties" : {},
        "methods" : {
            "getLabel()\tString" : "getLabel()$0",
            "getValue()\tString" : "getValue()$0",
            "setLabel(String label)\tvoid" : "setLabel($1)$0",
            "getDisabled()\tBoolean" : "getDisabled()$0",
            "setEscapeItem(Boolean disabled)\tvoid" : "setEscapeItem($1)$0",
            "getEscapeItem()\tBoolean" : "getEscapeItem()$0",
            "setValue(String value)\tvoid" : "setValue($1)$0",
            "setDisabled(Boolean disabled)\tvoid" : "setDisabled($1)$0"
        }
    },
    "zonesearchresulttype" : {
        "constructors" : {},
        "name" : "ZoneSearchResultType",
        "properties" : {
            "Article" : "Article$0",
            "Question" : "Question$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<ConnectApi.ZoneSearchResultType>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "groupvisibilitytype" : {
        "constructors" : {},
        "name" : "GroupVisibilityType",
        "properties" : {
            "PublicAccess" : "PublicAccess$0",
            "PrivateAccess" : "PrivateAccess$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0",
            "values()\tLIST<ConnectApi.GroupVisibilityType>" : "values()$0"
        }
    },
    "batchable" : {
        "constructors" : {},
        "name" : "Batchable",
        "properties" : {},
        "methods" : {
            "execute(Database.BatchableContext param1, LIST<ANY> param2)\tvoid" : "execute($1)$0",
            "start(Database.BatchableContext param1)\tsystem.Iterable" : "start($1)$0",
            "finish(Database.BatchableContext param1)\tvoid" : "finish($1)$0"
        }
    },
    "reportextendedmetadata" : {
        "constructors" : {},
        "name" : "ReportExtendedMetadata",
        "properties" : {},
        "methods" : {
            "setGroupingColumnInfo(MAP<String,reports.GroupingColumn> groupingColumnInfo)\tvoid" : "setGroupingColumnInfo($1)$0",
            "getAggregateColumnInfo()\tMAP<String,reports.AggregateColumn>" : "getAggregateColumnInfo()$0",
            "setDetailColumnInfo(MAP<String,reports.DetailColumn> detailColumnInfo)\tvoid" : "setDetailColumnInfo($1)$0",
            "setAggregateColumnInfo(MAP<String,reports.AggregateColumn> aggregateColumnInfo)\tvoid" : "setAggregateColumnInfo($1)$0",
            "getDetailColumnInfo()\tMAP<String,reports.DetailColumn>" : "getDetailColumnInfo()$0",
            "getGroupingColumnInfo()\tMAP<String,reports.GroupingColumn>" : "getGroupingColumnInfo()$0"
        }
    },
    "nosuchelementexception" : {
        "constructors" : {},
        "name" : "NoSuchElementException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "exception" : {
        "constructors" : {},
        "name" : "Exception",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "schedulable" : {
        "constructors" : {},
        "name" : "Schedulable",
        "properties" : {},
        "methods" : {
            "execute(system.SchedulableContext param1)\tvoid" : "execute($1)$0"
        }
    },
    "cookie" : {
        "constructors" : {},
        "name" : "Cookie",
        "properties" : {},
        "methods" : {
            "getPath()\tString" : "getPath()$0",
            "getDomain()\tString" : "getDomain()$0",
            "getName()\tString" : "getName()$0",
            "getValue()\tString" : "getValue()$0",
            "isSecure()\tBoolean" : "isSecure()$0",
            "getMaxAge()\tInteger" : "getMaxAge()$0"
        }
    },
    "chattergroupinput" : {
        "constructors" : {},
        "name" : "ChatterGroupInput",
        "properties" : {
            "isArchived" : "isArchived$0",
            "name" : "name$0",
            "canHaveChatterGuests" : "canHaveChatterGuests$0",
            "information" : "information$0",
            "isAutoArchiveDisabled" : "isAutoArchiveDisabled$0",
            "owner" : "owner$0",
            "description" : "description$0",
            "visibility" : "visibility$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object" : "convertToJavaObject($1)$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "cases" : {
        "constructors" : {},
        "name" : "Cases",
        "properties" : {},
        "methods" : {
            "getCaseIdFromEmailThreadId(String emailThreadId)\tId" : "getCaseIdFromEmailThreadId($1)$0"
        }
    },
    "reporttypecolumncategory" : {
        "constructors" : {},
        "name" : "ReportTypeColumnCategory",
        "properties" : {},
        "methods" : {
            "setLabel(String label)\tvoid" : "setLabel($1)$0",
            "setColumns(MAP<String,reports.ReportTypeColumn> columns)\tvoid" : "setColumns($1)$0",
            "getLabel()\tString" : "getLabel()$0",
            "getColumns()\tMAP<String,reports.ReportTypeColumn>" : "getColumns()$0"
        }
    },
    "describelayoutcomponent" : {
        "constructors" : {},
        "name" : "DescribeLayoutComponent",
        "properties" : {},
        "methods" : {
            "getType()\tString" : "getType()$0",
            "getDisplayLines()\tInteger" : "getDisplayLines()$0",
            "getValue()\tString" : "getValue()$0",
            "getTabOrder()\tInteger" : "getTabOrder()$0"
        }
    },
    "chatterlike" : {
        "constructors" : {},
        "name" : "ChatterLike",
        "properties" : {
            "likedItem" : "likedItem$0",
            "url" : "url$0",
            "user" : "user$0",
            "id" : "id$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "applicationreadwritemode" : {
        "constructors" : {},
        "name" : "ApplicationReadWriteMode",
        "properties" : {
            "DEFAULT" : "DEFAULT$0",
            "READ_ONLY" : "READ_ONLY$0"
        },
        "methods" : {
            "values()\tLIST<system.ApplicationReadWriteMode>" : "values()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "entitylinksegment" : {
        "constructors" : {},
        "name" : "EntityLinkSegment",
        "properties" : {
            "reference" : "reference$0",
            "motif" : "motif$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "encodingutil" : {
        "constructors" : {},
        "name" : "EncodingUtil",
        "properties" : {},
        "methods" : {
            "convertToHex(Blob s)\tString" : "convertToHex($1)$0",
            "urlEncode(String s, String enc)\tString" : "urlEncode($1)$0",
            "base64Encode(Blob s)\tString" : "base64Encode($1)$0",
            "urlDecode(String s, String enc)\tString" : "urlDecode($1)$0",
            "base64Decode(String s)\tBlob" : "base64Decode($1)$0"
        }
    },
    "reportinstance" : {
        "constructors" : {},
        "name" : "ReportInstance",
        "properties" : {},
        "methods" : {
            "getUrl()\tString" : "getUrl()$0",
            "getReportId()\tId" : "getReportId()$0",
            "setUrl(String url)\tvoid" : "setUrl($1)$0",
            "setReportId(Id reportId)\tvoid" : "setReportId($1)$0"
        }
    },
    "livechatroutingroute" : {
        "constructors" : {},
        "name" : "LiveChatRoutingRoute",
        "properties" : {},
        "methods" : {
            "getChatKey()\tString" : "getChatKey()$0",
            "getUserId()\tString" : "getUserId()$0"
        }
    },
    "invalidfilterexception" : {
        "constructors" : {},
        "name" : "InvalidFilterException",
        "properties" : {},
        "methods" : {
            "getTypeName()\tString" : "getTypeName()$0",
            "getFilterErrorMap()\tMAP<String,String>" : "getFilterErrorMap()$0"
        }
    },
    "userprofiles" : {
        "constructors" : {},
        "name" : "UserProfiles",
        "properties" : {},
        "methods" : {
            "getUserProfile(String communityId, String userId)\tConnectApi.UserProfile" : "getUserProfile($1)$0"
        }
    },
    "unauthenticateduser" : {
        "constructors" : {},
        "name" : "UnauthenticatedUser",
        "properties" : {},
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "morechangessegment" : {
        "constructors" : {},
        "name" : "MoreChangesSegment",
        "properties" : {
            "moreChanges" : "moreChanges$0",
            "moreChangesCount" : "moreChangesCount$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "feedtype" : {
        "constructors" : {},
        "name" : "FeedType",
        "properties" : {
            "Bookmarks" : "Bookmarks$0",
            "News" : "News$0",
            "UserProfile" : "UserProfile$0",
            "To" : "To$0",
            "Company" : "Company$0",
            "Topics" : "Topics$0",
            "Moderation" : "Moderation$0",
            "Record" : "Record$0",
            "Files" : "Files$0",
            "People" : "People$0",
            "Groups" : "Groups$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<ConnectApi.FeedType>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "timezone" : {
        "constructors" : {},
        "name" : "TimeZone",
        "properties" : {},
        "methods" : {
            "getTimeZone(String id)\tsystem.TimeZone" : "getTimeZone($1)$0",
            "toString()\tString" : "toString()$0",
            "getDisplayName()\tString" : "getDisplayName()$0",
            "getID()\tString" : "getID()$0",
            "getOffset(Datetime dt)\tInteger" : "getOffset($1)$0"
        }
    },
    "approvalattachment" : {
        "constructors" : {},
        "name" : "ApprovalAttachment",
        "properties" : {
            "postTemplateFields" : "postTemplateFields$0",
            "status" : "status$0",
            "id" : "id$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "organizationsettings" : {
        "constructors" : {},
        "name" : "OrganizationSettings",
        "properties" : {
            "accessTimeout" : "accessTimeout$0",
            "userSettings" : "userSettings$0",
            "name" : "name$0",
            "features" : "features$0",
            "orgId" : "orgId$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "inboundenvelope" : {
        "constructors" : {},
        "name" : "InboundEnvelope",
        "properties" : {
            "fromAddress" : "fromAddress$0",
            "toAddress" : "toAddress$0"
        },
        "methods" : {}

    },
    "outputparameter" : {
        "constructors" : {},
        "name" : "OutputParameter",
        "properties" : {
            "parameterType" : "parameterType$0",
            "name" : "name$0",
            "description" : "description$0"
        },
        "methods" : {}

    },
    "feeditemtopicpage" : {
        "constructors" : {},
        "name" : "FeedItemTopicPage",
        "properties" : {
            "canAssignTopics" : "canAssignTopics$0",
            "topics" : "topics$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "commentinput" : {
        "constructors" : {},
        "name" : "CommentInput",
        "properties" : {
            "body" : "body$0",
            "attachment" : "attachment$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object" : "convertToJavaObject($1)$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "topics" : {
        "constructors" : {},
        "name" : "Topics",
        "properties" : {},
        "methods" : {
            "getRecentlyTalkingAboutTopicsForGroup(String communityId, String groupId)\tConnectApi.TopicPage" : "getRecentlyTalkingAboutTopicsForGroup($1)$0",
            "getTopicSuggestionsForText(String communityId, String text)\tConnectApi.TopicSuggestionPage" : "getTopicSuggestionsForText($1)$0",
            "getTopics(String communityId, Integer pageParam, Integer pageSize, ConnectApi.TopicSort sortParam)\tConnectApi.TopicPage" : "getTopics($1)$0",
            "unassignTopic(String communityId, String recordId, String topicId)\tvoid" : "unassignTopic($1)$0",
            "updateTopic(String communityId, String topicId, ConnectApi.TopicInput topic)\tConnectApi.Topic" : "updateTopic($1)$0",
            "assignTopic(String communityId, String recordId, String topicId)\tConnectApi.Topic" : "assignTopic($1)$0",
            "getTopics(String communityId, String recordId)\tConnectApi.TopicPage" : "getTopics($1)$0",
            "setTestGetRecentlyTalkingAboutTopicsForUser(String communityId, String userId, ConnectApi.TopicPage result)\tvoid" : "setTestGetRecentlyTalkingAboutTopicsForUser($1)$0",
            "getTrendingTopics(String communityId, Integer maxResults)\tConnectApi.TopicPage" : "getTrendingTopics($1)$0",
            "getTopics(String communityId)\tConnectApi.TopicPage" : "getTopics($1)$0",
            "setTestGetTopicSuggestions(String communityId, String recordId, Integer maxResults, ConnectApi.TopicSuggestionPage result)\tvoid" : "setTestGetTopicSuggestions($1)$0",
            "setTestGetTopicSuggestionsForText(String communityId, String text, ConnectApi.TopicSuggestionPage result)\tvoid" : "setTestGetTopicSuggestionsForText($1)$0",
            "assignTopicByName(String communityId, String recordId, String topicName)\tConnectApi.Topic" : "assignTopicByName($1)$0",
            "getRelatedTopics(String communityId, String topicId)\tConnectApi.TopicPage" : "getRelatedTopics($1)$0",
            "getTopicSuggestions(String communityId, String recordId)\tConnectApi.TopicSuggestionPage" : "getTopicSuggestions($1)$0",
            "getTrendingTopics(String communityId)\tConnectApi.TopicPage" : "getTrendingTopics($1)$0",
            "setTestGetTrendingTopics(String communityId, Integer maxResults, ConnectApi.TopicPage result)\tvoid" : "setTestGetTrendingTopics($1)$0",
            "deleteTopic(String communityId, String topicId)\tvoid" : "deleteTopic($1)$0",
            "setTestGetTrendingTopics(String communityId, ConnectApi.TopicPage result)\tvoid" : "setTestGetTrendingTopics($1)$0",
            "getTopic(String communityId, String topicId)\tConnectApi.Topic" : "getTopic($1)$0",
            "setTestGetTopicSuggestions(String communityId, String recordId, ConnectApi.TopicSuggestionPage result)\tvoid" : "setTestGetTopicSuggestions($1)$0",
            "getGroupsRecentlyTalkingAboutTopic(String communityId, String topicId)\tConnectApi.ChatterGroupSummaryPage" : "getGroupsRecentlyTalkingAboutTopic($1)$0",
            "getTopics(String communityId, ConnectApi.TopicSort sortParam)\tConnectApi.TopicPage" : "getTopics($1)$0",
            "setTestGetRecentlyTalkingAboutTopicsForGroup(String communityId, String groupId, ConnectApi.TopicPage result)\tvoid" : "setTestGetRecentlyTalkingAboutTopicsForGroup($1)$0",
            "getTopicSuggestions(String communityId, String recordId, Integer maxResults)\tConnectApi.TopicSuggestionPage" : "getTopicSuggestions($1)$0",
            "getTopics(String communityId, String q, Integer pageParam, Integer pageSize)\tConnectApi.TopicPage" : "getTopics($1)$0",
            "setTestGetTopicSuggestionsForText(String communityId, String text, Integer maxResults, ConnectApi.TopicSuggestionPage result)\tvoid" : "setTestGetTopicSuggestionsForText($1)$0",
            "getTopicSuggestionsForText(String communityId, String text, Integer maxResults)\tConnectApi.TopicSuggestionPage" : "getTopicSuggestionsForText($1)$0",
            "getTopics(String communityId, Integer pageParam, Integer pageSize)\tConnectApi.TopicPage" : "getTopics($1)$0",
            "setTestGetRelatedTopics(String communityId, String topicId, ConnectApi.TopicPage result)\tvoid" : "setTestGetRelatedTopics($1)$0",
            "getTopics(String communityId, String q, Integer pageParam, Integer pageSize, ConnectApi.TopicSort sortParam)\tConnectApi.TopicPage" : "getTopics($1)$0",
            "getTopics(String communityId, String q, ConnectApi.TopicSort sortParam)\tConnectApi.TopicPage" : "getTopics($1)$0",
            "getRecentlyTalkingAboutTopicsForUser(String communityId, String userId)\tConnectApi.TopicPage" : "getRecentlyTalkingAboutTopicsForUser($1)$0",
            "setTestGetGroupsRecentlyTalkingAboutTopic(String communityId, String topicId, ConnectApi.ChatterGroupSummaryPage result)\tvoid" : "setTestGetGroupsRecentlyTalkingAboutTopic($1)$0"
        }
    },
    "quickactionrequest" : {
        "constructors" : {},
        "name" : "QuickActionRequest",
        "properties" : {},
        "methods" : {
            "setQuickActionName(String param1)\tvoid" : "setQuickActionName($1)$0",
            "setContextId(Id param1)\tvoid" : "setContextId($1)$0",
            "getContextId()\tId" : "getContextId()$0",
            "getRecord()\tSObject" : "getRecord()$0",
            "setRecord(SObject param1)\tvoid" : "setRecord($1)$0",
            "getQuickActionName()\tString" : "getQuickActionName()$0"
        }
    },
    "fieldchangenamesegment" : {
        "constructors" : {},
        "name" : "FieldChangeNameSegment",
        "properties" : {},
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "chatterconversationpage" : {
        "constructors" : {},
        "name" : "ChatterConversationPage",
        "properties" : {
            "currentPageUrl" : "currentPageUrl$0",
            "nextPageUrl" : "nextPageUrl$0",
            "conversations" : "conversations$0",
            "nextPageToken" : "nextPageToken$0",
            "currentPageToken" : "currentPageToken$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "reporttype" : {
        "constructors" : {},
        "name" : "ReportType",
        "properties" : {},
        "methods" : {
            "getType()\tString" : "getType()$0",
            "setType(String type)\tvoid" : "setType($1)$0",
            "getLabel()\tString" : "getLabel()$0",
            "setLabel(String label)\tvoid" : "setLabel($1)$0"
        }
    },
    "database" : {
        "constructors" : {},
        "name" : "Database",
        "properties" : ["AssignmentRuleHeader", "QueryLocatorIterator", "BatchableContext", "Batchable", "QueryLocator", "BatchableContextImpl", "QueryLocatorChunkIterator", "LeadConvert", "DMLOptions", "EmailHeader"],
        "methods" : {
            "convertLead(LIST<Database.LeadConvert> leadConverts, Boolean allOrNothing)\tLIST<Database.LeadConvertResult>" : "convertLead($1)$0",
            "convertLead(Database.LeadConvert leadConvert)\tDatabase.LeadConvertResult" : "convertLead($1)$0",
            "merge(SObject master, Id duplicate, Boolean allOrNothing)\tDatabase.MergeResult" : "merge($1)$0",
            "delete(LIST<SObject> sobjects, Boolean allOrNothing)\tLIST<Database.DeleteResult>" : "delete($1)$0",
            "delete(Id id)\tDatabase.DeleteResult" : "delete($1)$0",
            "delete(SObject sobject, Boolean allOrNothing)\tDatabase.DeleteResult" : "delete($1)$0",
            "getQueryLocator(LIST<SObject> query)\tDatabase.QueryLocator" : "getQueryLocator($1)$0",
            "undelete(Id id, Boolean allOrNothing)\tDatabase.UndeleteResult" : "undelete($1)$0",
            "update(SObject sobject, APEX_OBJECT allOrNothing)\tDatabase.SaveResult" : "update($1)$0",
            "delete(Id id, Boolean allOrNothing)\tDatabase.DeleteResult" : "delete($1)$0",
            "rollback(System.Savepoint savepoint)\tvoid" : "rollback($1)$0",
            "undelete(LIST<Id> ids, Boolean allOrNothing)\tLIST<Database.UndeleteResult>" : "undelete($1)$0",
            "query(String query)\tLIST<SObject>" : "query($1)$0",
            "update(LIST<SObject> sobjects)\tLIST<Database.SaveResult>" : "update($1)$0",
            "merge(SObject master, SObject duplicate, Boolean allOrNothing)\tDatabase.MergeResult" : "merge($1)$0",
            "update(SObject sobject)\tDatabase.SaveResult" : "update($1)$0",
            "merge(SObject master, LIST<Id> duplicates)\tLIST<Database.MergeResult>" : "merge($1)$0",
            "delete(LIST<SObject> sobjects)\tLIST<Database.DeleteResult>" : "delete($1)$0",
            "upsert(LIST<SObject> sobjects, Schema.SObjectField field)\tLIST<Database.UpsertResult>" : "upsert($1)$0",
            "update(LIST<SObject> sobjects, APEX_OBJECT allOrNothing)\tLIST<Database.SaveResult>" : "update($1)$0",
            "emptyRecycleBin(LIST<SObject> sobjects)\tLIST<Database.EmptyRecycleBinResult>" : "emptyRecycleBin($1)$0",
            "upsert(SObject sobject, Boolean allOrNothing)\tDatabase.UpsertResult" : "upsert($1)$0",
            "setSavepoint()\tSystem.Savepoint" : "setSavepoint()$0",
            "insert(SObject sobject)\tDatabase.SaveResult" : "insert($1)$0",
            "emptyRecycleBin(SObject sobject)\tDatabase.EmptyRecycleBinResult" : "emptyRecycleBin($1)$0",
            "undelete(SObject sobject, Boolean allOrNothing)\tDatabase.UndeleteResult" : "undelete($1)$0",
            "update(LIST<SObject> sobjects, Boolean allOrNothing)\tLIST<Database.SaveResult>" : "update($1)$0",
            "countQuery(String query)\tInteger" : "countQuery($1)$0",
            "insert(LIST<SObject> sobjects)\tLIST<Database.SaveResult>" : "insert($1)$0",
            "insert(LIST<SObject> sobjects, Boolean allOrNothing)\tLIST<Database.SaveResult>" : "insert($1)$0",
            "merge(SObject master, LIST<Id> duplicates, Boolean allOrNothing)\tLIST<Database.MergeResult>" : "merge($1)$0",
            "convertLead(Database.LeadConvert leadConvert, Boolean allOrNothing)\tDatabase.LeadConvertResult" : "convertLead($1)$0",
            "undelete(Id id)\tDatabase.UndeleteResult" : "undelete($1)$0",
            "insert(SObject sobject, Boolean allOrNothing)\tDatabase.SaveResult" : "insert($1)$0",
            "executeBatch(APEX_OBJECT batchable)\tString" : "executeBatch($1)$0",
            "upsert(SObject sobject, Schema.SObjectField field, Boolean allOrNothing)\tDatabase.UpsertResult" : "upsert($1)$0",
            "insert(SObject sobject, APEX_OBJECT DmlOptions)\tDatabase.SaveResult" : "insert($1)$0",
            "upsert(SObject sobject, Schema.SObjectField field)\tDatabase.UpsertResult" : "upsert($1)$0",
            "update(SObject sobject, Boolean allOrNothing)\tDatabase.SaveResult" : "update($1)$0",
            "merge(SObject master, Id duplicate)\tDatabase.MergeResult" : "merge($1)$0",
            "undelete(SObject sobject)\tDatabase.UndeleteResult" : "undelete($1)$0",
            "insert(LIST<SObject> sobjects, APEX_OBJECT DmlOptions)\tLIST<Database.SaveResult>" : "insert($1)$0",
            "undelete(LIST<SObject> sobjects, Boolean allOrNothing)\tLIST<Database.UndeleteResult>" : "undelete($1)$0",
            "undelete(LIST<Id> ids)\tLIST<Database.UndeleteResult>" : "undelete($1)$0",
            "delete(SObject sobject)\tDatabase.DeleteResult" : "delete($1)$0",
            "undelete(LIST<SObject> sobjects)\tLIST<Database.UndeleteResult>" : "undelete($1)$0",
            "merge(SObject master, SObject duplicate)\tDatabase.MergeResult" : "merge($1)$0",
            "executeBatch(APEX_OBJECT batchable, Integer batchSize)\tString" : "executeBatch($1)$0",
            "upsert(LIST<SObject> sobjects, Schema.SObjectField field, Boolean allOrNothing)\tLIST<Database.UpsertResult>" : "upsert($1)$0",
            "upsert(LIST<SObject> sobjects)\tLIST<Database.UpsertResult>" : "upsert($1)$0",
            "merge(SObject master, LIST<SObject> duplicates, Boolean allOrNothing)\tLIST<Database.MergeResult>" : "merge($1)$0",
            "delete(LIST<Id> ids, Boolean allOrNothing)\tLIST<Database.DeleteResult>" : "delete($1)$0",
            "convertLead(LIST<Database.LeadConvert> leadConverts)\tLIST<Database.LeadConvertResult>" : "convertLead($1)$0",
            "getUpdated(String sobjectType, Datetime startDate, Datetime endDate)\tDatabase.GetUpdatedResult" : "getUpdated($1)$0",
            "delete(LIST<Id> ids)\tLIST<Database.DeleteResult>" : "delete($1)$0",
            "merge(SObject master, LIST<SObject> duplicates)\tLIST<Database.MergeResult>" : "merge($1)$0",
            "upsert(SObject sobject)\tDatabase.UpsertResult" : "upsert($1)$0",
            "emptyRecycleBin(LIST<Id> ids)\tLIST<Database.EmptyRecycleBinResult>" : "emptyRecycleBin($1)$0",
            "getDeleted(String sobjectType, Datetime startDate, Datetime endDate)\tDatabase.GetDeletedResult" : "getDeleted($1)$0",
            "getQueryLocator(String query)\tDatabase.QueryLocator" : "getQueryLocator($1)$0",
            "upsert(LIST<SObject> sobjects, Boolean allOrNothing)\tLIST<Database.UpsertResult>" : "upsert($1)$0"
        }
    },
    "moderationflags" : {
        "constructors" : {},
        "name" : "ModerationFlags",
        "properties" : {
            "flagCount" : "flagCount$0",
            "flaggedByMe" : "flaggedByMe$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "followingcounts" : {
        "constructors" : {},
        "name" : "FollowingCounts",
        "properties" : {
            "total" : "total$0",
            "records" : "records$0",
            "people" : "people$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "restrequest" : {
        "constructors" : {},
        "name" : "RestRequest",
        "properties" : {
            "requestURI" : "requestURI$0",
            "resourcePath" : "resourcePath$0",
            "headers" : "headers$0",
            "requestBody" : "requestBody$0",
            "remoteAddress" : "remoteAddress$0",
            "httpMethod" : "httpMethod$0",
            "params" : "params$0"
        },
        "methods" : {
            "addHeader(String name, String value)\tvoid" : "addHeader($1)$0",
            "addParameter(String name, String value)\tvoid" : "addParameter($1)$0"
        }
    },
    "emailmessage" : {
        "constructors" : {},
        "name" : "EmailMessage",
        "properties" : {
            "direction" : "direction$0",
            "emailMessageId" : "emailMessageId$0",
            "subject" : "subject$0",
            "toAddresses" : "toAddresses$0",
            "textBody" : "textBody$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "feedpoll" : {
        "constructors" : {},
        "name" : "FeedPoll",
        "properties" : {
            "totalVoteCount" : "totalVoteCount$0",
            "choices" : "choices$0",
            "myChoiceId" : "myChoiceId$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "describesobjectresult" : {
        "constructors" : {},
        "name" : "DescribeSObjectResult",
        "properties" : {},
        "methods" : {
            "getRecordTypeInfosByName()\tMAP<String,Schema.RecordTypeInfo>" : "getRecordTypeInfosByName()$0",
            "isQueryable()\tBoolean" : "isQueryable()$0",
            "getSObjectType()\tSchema.SObjectType" : "getSObjectType()$0",
            "isDeletable()\tBoolean" : "isDeletable()$0",
            "isCustom()\tBoolean" : "isCustom()$0",
            "getLocalName()\tString" : "getLocalName()$0",
            "getFields()\tSchema.SObjectTypeFields" : "getFields()$0",
            "isCustomSetting()\tBoolean" : "isCustomSetting()$0",
            "isUpdateable()\tBoolean" : "isUpdateable()$0",
            "getName()\tString" : "getName()$0",
            "isCreateable()\tBoolean" : "isCreateable()$0",
            "getFieldSets()\tSchema.SObjectTypeFieldSets" : "getFieldSets()$0",
            "isAccessible()\tBoolean" : "isAccessible()$0",
            "isFeedEnabled()\tBoolean" : "isFeedEnabled()$0",
            "getRecordTypeInfos()\tLIST<Schema.RecordTypeInfo>" : "getRecordTypeInfos()$0",
            "isMergeable()\tBoolean" : "isMergeable()$0",
            "getRecordTypeInfosById()\tMAP<Id,Schema.RecordTypeInfo>" : "getRecordTypeInfosById()$0",
            "isSearchable()\tBoolean" : "isSearchable()$0",
            "isDeprecatedAndHidden()\tBoolean" : "isDeprecatedAndHidden()$0",
            "getLabel()\tString" : "getLabel()$0",
            "getKeyPrefix()\tString" : "getKeyPrefix()$0",
            "isUndeletable()\tBoolean" : "isUndeletable()$0",
            "getLabelPlural()\tString" : "getLabelPlural()$0",
            "getChildRelationships()\tLIST<Schema.ChildRelationship>" : "getChildRelationships()$0"
        }
    },
    "zones" : {
        "constructors" : {},
        "name" : "Zones",
        "properties" : {},
        "methods" : {
            "getZones(String communityId)\tConnectApi.ZonePage" : "getZones($1)$0",
            "setTestSearchInZone(String communityId, String zoneId, String q, ConnectApi.ZoneSearchResultType filter, ConnectApi.ZoneSearchPage result)\tvoid" : "setTestSearchInZone($1)$0",
            "getZones(String communityId, Integer pageParam, Integer pageSize)\tConnectApi.ZonePage" : "getZones($1)$0",
            "setTestSearchInZone(String communityId, String zoneId, String q, ConnectApi.ZoneSearchResultType filter, String pageParam, Integer pageSize, ConnectApi.ZoneSearchPage result)\tvoid" : "setTestSearchInZone($1)$0",
            "getZone(String communityId, String zoneId)\tConnectApi.Zone" : "getZone($1)$0",
            "searchInZone(String communityId, String zoneId, String q, ConnectApi.ZoneSearchResultType filter)\tConnectApi.ZoneSearchPage" : "searchInZone($1)$0",
            "searchInZone(String communityId, String zoneId, String q, ConnectApi.ZoneSearchResultType filter, String pageParam, Integer pageSize)\tConnectApi.ZoneSearchPage" : "searchInZone($1)$0"
        }
    },
    "contentattachment" : {
        "constructors" : {},
        "name" : "ContentAttachment",
        "properties" : {
            "fileExtension" : "fileExtension$0",
            "id" : "id$0",
            "isInMyFileSync" : "isInMyFileSync$0",
            "downloadUrl" : "downloadUrl$0",
            "renditionUrl" : "renditionUrl$0",
            "fileSize" : "fileSize$0",
            "fileType" : "fileType$0",
            "checksum" : "checksum$0",
            "versionId" : "versionId$0",
            "hasImagePreview" : "hasImagePreview$0",
            "hasPdfPreview" : "hasPdfPreview$0",
            "mimeType" : "mimeType$0",
            "title" : "title$0",
            "description" : "description$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "fieldchangesegment" : {
        "constructors" : {},
        "name" : "FieldChangeSegment",
        "properties" : {},
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "assertexception" : {
        "constructors" : {},
        "name" : "AssertException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "mentioncompletion" : {
        "constructors" : {},
        "name" : "MentionCompletion",
        "properties" : {
            "recordId" : "recordId$0",
            "additionalLabel" : "additionalLabel$0",
            "photoUrl" : "photoUrl$0",
            "name" : "name$0",
            "description" : "description$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "listexception" : {
        "constructors" : {},
        "name" : "ListException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "json" : {
        "constructors" : {},
        "name" : "JSON",
        "properties" : {},
        "methods" : {
            "serialize(Object o)\tString" : "serialize($1)$0",
            "createParser(String jsonString)\tsystem.JSONParser" : "createParser($1)$0",
            "createGenerator(Boolean pretty)\tsystem.JSONGenerator" : "createGenerator($1)$0",
            "deserializeUntyped(String jsonString)\tObject" : "deserializeUntyped($1)$0",
            "deserializeStrict(String jsonString, system.Type apexType)\tObject" : "deserializeStrict($1)$0",
            "deserialize(String jsonString, system.Type apexType)\tObject" : "deserialize($1)$0",
            "serializePretty(Object o)\tString" : "serializePretty($1)$0"
        }
    },
    "clientinfo" : {
        "constructors" : {},
        "name" : "ClientInfo",
        "properties" : {
            "applicationUrl" : "applicationUrl$0",
            "applicationName" : "applicationName$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "groupinformationinput" : {
        "constructors" : {},
        "name" : "GroupInformationInput",
        "properties" : {
            "text" : "text$0",
            "title" : "title$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object" : "convertToJavaObject($1)$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "instanceaccessexception" : {
        "constructors" : {},
        "name" : "InstanceAccessException",
        "properties" : {},
        "methods" : {
            "getTypeName()\tString" : "getTypeName()$0"
        }
    },
    "hashtagsegment" : {
        "constructors" : {},
        "name" : "HashtagSegment",
        "properties" : {
            "tag" : "tag$0",
            "url" : "url$0",
            "topicUrl" : "topicUrl$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "motif" : {
        "constructors" : {},
        "name" : "Motif",
        "properties" : {
            "mediumIconUrl" : "mediumIconUrl$0",
            "largeIconUrl" : "largeIconUrl$0",
            "color" : "color$0",
            "smallIconUrl" : "smallIconUrl$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "groupmembershiprequest" : {
        "constructors" : {},
        "name" : "GroupMembershipRequest",
        "properties" : {
            "url" : "url$0",
            "user" : "user$0",
            "id" : "id$0",
            "createdDate" : "createdDate$0",
            "lastUpdateDate" : "lastUpdateDate$0",
            "status" : "status$0",
            "requestedGroup" : "requestedGroup$0",
            "responseMessage" : "responseMessage$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "feeditem" : {
        "constructors" : {},
        "name" : "FeedItem",
        "properties" : {
            "myLike" : "myLike$0",
            "preamble" : "preamble$0",
            "isBookmarkedByCurrentUser" : "isBookmarkedByCurrentUser$0",
            "createdDate" : "createdDate$0",
            "attachment" : "attachment$0",
            "originalFeedItem" : "originalFeedItem$0",
            "canShare" : "canShare$0",
            "topics" : "topics$0",
            "likes" : "likes$0",
            "clientInfo" : "clientInfo$0",
            "visibility" : "visibility$0",
            "body" : "body$0",
            "parent" : "parent$0",
            "isDeleteRestricted" : "isDeleteRestricted$0",
            "id" : "id$0",
            "event" : "event$0",
            "type" : "type$0",
            "relativeCreatedDate" : "relativeCreatedDate$0",
            "modifiedDate" : "modifiedDate$0",
            "isLikedByCurrentUser" : "isLikedByCurrentUser$0",
            "url" : "url$0",
            "actor" : "actor$0",
            "originalFeedItemActor" : "originalFeedItemActor$0",
            "likesMessage" : "likesMessage$0",
            "photoUrl" : "photoUrl$0",
            "moderationFlags" : "moderationFlags$0",
            "comments" : "comments$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "communities" : {
        "constructors" : {},
        "name" : "Communities",
        "properties" : {},
        "methods" : {
            "communitiesLanding(String startUrl)\tSystem.PageReference" : "communitiesLanding($1)$0",
            "login(String username, String password, String startUrl)\tSystem.PageReference" : "login($1)$0",
            "communitiesLanding()\tSystem.PageReference" : "communitiesLanding()$0",
            "internalLogin(String startUrl)\tSystem.PageReference" : "internalLogin($1)$0",
            "forwardToAuthPage(String startUrl)\tSystem.PageReference" : "forwardToAuthPage($1)$0",
            "getCSS()\tString" : "getCSS()$0"
        }
    },
    "feedfavorites" : {
        "constructors" : {},
        "name" : "FeedFavorites",
        "properties" : {
            "total" : "total$0",
            "favorites" : "favorites$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "address" : {
        "constructors" : {},
        "name" : "Address",
        "properties" : {
            "country" : "country$0",
            "street" : "street$0",
            "state" : "state$0",
            "city" : "city$0",
            "zip" : "zip$0",
            "formattedAddress" : "formattedAddress$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "records" : {
        "constructors" : {},
        "name" : "Records",
        "properties" : {},
        "methods" : {
            "getMotif(String communityId, String idOrPrefix)\tConnectApi.Motif" : "getMotif($1)$0"
        }
    },
    "groupmember" : {
        "constructors" : {},
        "name" : "GroupMember",
        "properties" : {
            "url" : "url$0",
            "user" : "user$0",
            "id" : "id$0",
            "role" : "role$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "calloutexception" : {
        "constructors" : {},
        "name" : "CalloutException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "detailcolumn" : {
        "constructors" : {},
        "name" : "DetailColumn",
        "properties" : {},
        "methods" : {
            "setDataType(reports.ColumnDataType dataType)\tvoid" : "setDataType($1)$0",
            "setName(String name)\tvoid" : "setName($1)$0",
            "getLabel()\tString" : "getLabel()$0",
            "setLabel(String label)\tvoid" : "setLabel($1)$0",
            "getDataType()\treports.ColumnDataType" : "getDataType()$0",
            "setDataType(String value)\tvoid" : "setDataType($1)$0",
            "getName()\tString" : "getName()$0"
        }
    },
    "feeditemtype" : {
        "constructors" : {},
        "name" : "FeedItemType",
        "properties" : {
            "ApprovalPost" : "ApprovalPost$0",
            "DashboardComponentAlert" : "DashboardComponentAlert$0",
            "CanvasPost" : "CanvasPost$0",
            "PollPost" : "PollPost$0",
            "MilestoneEvent" : "MilestoneEvent$0",
            "AttachArticleEvent" : "AttachArticleEvent$0",
            "CallLogPost" : "CallLogPost$0",
            "CaseCommentPost" : "CaseCommentPost$0",
            "FacebookPost" : "FacebookPost$0",
            "SocialPost" : "SocialPost$0",
            "RypplePost" : "RypplePost$0",
            "BasicTemplateFeedItem" : "BasicTemplateFeedItem$0",
            "AnnouncementPost" : "AnnouncementPost$0",
            "LinkPost" : "LinkPost$0",
            "CollaborationGroupCreated" : "CollaborationGroupCreated$0",
            "ChangeStatusPost" : "ChangeStatusPost$0",
            "TrackedChange" : "TrackedChange$0",
            "CreateRecordEvent" : "CreateRecordEvent$0",
            "EmailMessageEvent" : "EmailMessageEvent$0",
            "ChatTranscriptPost" : "ChatTranscriptPost$0",
            "CollaborationGroupUnarchived" : "CollaborationGroupUnarchived$0",
            "ContentPost" : "ContentPost$0",
            "DashboardComponentSnapshot" : "DashboardComponentSnapshot$0",
            "ReplyPost" : "ReplyPost$0",
            "UserStatus" : "UserStatus$0",
            "TextPost" : "TextPost$0",
            "ActivityEvent" : "ActivityEvent$0"
        },
        "methods" : {
            "values()\tLIST<ConnectApi.FeedItemType>" : "values()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "emailaddress" : {
        "constructors" : {},
        "name" : "EmailAddress",
        "properties" : {
            "emailAddress" : "emailAddress$0",
            "displayName" : "displayName$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "currencyrecordfield" : {
        "constructors" : {},
        "name" : "CurrencyRecordField",
        "properties" : {},
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "filesummary" : {
        "constructors" : {},
        "name" : "FileSummary",
        "properties" : {},
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "chattergroupdetail" : {
        "constructors" : {},
        "name" : "ChatterGroupDetail",
        "properties" : {
            "information" : "information$0",
            "pendingRequests" : "pendingRequests$0",
            "fileCount" : "fileCount$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "dategranularity" : {
        "constructors" : {},
        "name" : "DateGranularity",
        "properties" : {
            "QUARTER" : "QUARTER$0",
            "FISCAL_PERIOD" : "FISCAL_PERIOD$0",
            "DAY" : "DAY$0",
            "YEAR" : "YEAR$0",
            "FISCAL_QUARTER" : "FISCAL_QUARTER$0",
            "MONTH" : "MONTH$0",
            "DAY_IN_MONTH" : "DAY_IN_MONTH$0",
            "FISCAL_WEEK" : "FISCAL_WEEK$0",
            "FISCAL_YEAR" : "FISCAL_YEAR$0",
            "NONE" : "NONE$0",
            "MONTH_IN_YEAR" : "MONTH_IN_YEAR$0",
            "WEEK" : "WEEK$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<reports.DateGranularity>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "accountcreator" : {
        "constructors" : {},
        "name" : "AccountCreator",
        "properties" : {},
        "methods" : {
            "createAccount(String param1, String param2, Id param3)\tString" : "createAccount($1)$0"
        }
    },
    "casecomment" : {
        "constructors" : {},
        "name" : "CaseComment",
        "properties" : {
            "actorType" : "actorType$0",
            "eventType" : "eventType$0",
            "text" : "text$0",
            "id" : "id$0",
            "published" : "published$0",
            "createdDate" : "createdDate$0",
            "createdBy" : "createdBy$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "undeleteresult" : {
        "constructors" : {},
        "name" : "UndeleteResult",
        "properties" : {},
        "methods" : {
            "getErrors()\tLIST<Database.Error>" : "getErrors()$0",
            "isSuccess()\tBoolean" : "isSuccess()$0",
            "getId()\tId" : "getId()$0"
        }
    },
    "xmlnode" : {
        "constructors" : {},
        "name" : "XmlNode",
        "properties" : {},
        "methods" : {
            "getAttributeKeyAt(Integer index)\tString" : "getAttributeKeyAt($1)$0",
            "addChildElement(String name, String namespace, String prefix)\tdom.XmlNode" : "addChildElement($1)$0",
            "setAttribute(String key, String value)\tvoid" : "setAttribute($1)$0",
            "removeChild(ANY child)\tBoolean" : "removeChild($1)$0",
            "getAttributeValueNs(String key, String keyNamespace)\tString" : "getAttributeValueNs($1)$0",
            "getAttribute(String key, String keyNamespace)\tString" : "getAttribute($1)$0",
            "getName()\tString" : "getName()$0",
            "getChildElements()\tLIST<dom.XmlNode>" : "getChildElements()$0",
            "getNamespace()\tString" : "getNamespace()$0",
            "getAttributeValue(String key, String keyNamespace)\tString" : "getAttributeValue($1)$0",
            "getNamespaceFor(String prefix)\tString" : "getNamespaceFor($1)$0",
            "getAttributeCount()\tInteger" : "getAttributeCount()$0",
            "getChildElement(String name, String namespace)\tdom.XmlNode" : "getChildElement($1)$0",
            "setAttributeNs(String key, String value, String keyNamespace, String valueNamespace)\tvoid" : "setAttributeNs($1)$0",
            "getText()\tString" : "getText()$0",
            "getPrefixFor(String namespace)\tString" : "getPrefixFor($1)$0",
            "setNamespace(String prefix, String namespace)\tvoid" : "setNamespace($1)$0",
            "addTextNode(String text)\tdom.XmlNode" : "addTextNode($1)$0",
            "getParent()\tdom.XmlNode" : "getParent()$0",
            "getAttributeKeyNsAt(Integer index)\tString" : "getAttributeKeyNsAt($1)$0",
            "getNodeType()\tDom.XmlNodeType" : "getNodeType()$0",
            "getChildren()\tLIST<dom.XmlNode>" : "getChildren()$0",
            "removeAttribute(String key, String keyNamespace)\tBoolean" : "removeAttribute($1)$0",
            "addCommentNode(String text)\tdom.XmlNode" : "addCommentNode($1)$0"
        }
    },
    "error" : {
        "constructors" : {},
        "name" : "Error",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getStatusCode()\tsystem.StatusCode" : "getStatusCode()$0",
            "getFields()\tLIST<String>" : "getFields()$0"
        }
    },
    "context" : {
        "constructors" : {},
        "name" : "Context",
        "properties" : {
            "sobjects" : "sobjects$0"
        },
        "methods" : {}

    },
    "dimension" : {
        "constructors" : {},
        "name" : "Dimension",
        "properties" : {},
        "methods" : {
            "getGroupings()\tLIST<reports.GroupingValue>" : "getGroupings()$0",
            "setGroupings(LIST<reports.GroupingValue> groupings)\tvoid" : "setGroupings($1)$0"
        }
    },
    "emailmessagedirection" : {
        "constructors" : {},
        "name" : "EmailMessageDirection",
        "properties" : {
            "Inbound" : "Inbound$0",
            "Outbound" : "Outbound$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<ConnectApi.EmailMessageDirection>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "trackedchangeitem" : {
        "constructors" : {},
        "name" : "TrackedChangeItem",
        "properties" : {
            "oldValue" : "oldValue$0",
            "newValue" : "newValue$0",
            "fieldName" : "fieldName$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "comparable" : {
        "constructors" : {},
        "name" : "Comparable",
        "properties" : {},
        "methods" : {
            "compareTo(Object param1)\tInteger" : "compareTo($1)$0"
        }
    },
    "procedureexception" : {
        "constructors" : {},
        "name" : "ProcedureException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "schedulablecontext" : {
        "constructors" : {},
        "name" : "SchedulableContext",
        "properties" : {},
        "methods" : {
            "getTriggerId()\tId" : "getTriggerId()$0"
        }
    },
    "sobject" : {
        "constructors" : {},
        "name" : "SObject",
        "properties" : {},
        "methods" : {
            "clone(Boolean preserveId, Boolean deep, Boolean preserveReadOnlyTimestamps)\tSObject" : "clone($1)$0",
            "getSObject(Schema.SObjectField field)\tSObject" : "getSObject($1)$0",
            "clear()\tvoid" : "clear()$0",
            "get(Schema.SObjectField field)\tObject" : "get($1)$0",
            "clone(Boolean preserveId)\tSObject" : "clone($1)$0",
            "clone(Boolean preserveId, Boolean deep, Boolean preserveReadOnlyTimestamps, Boolean preserveAutoNumbers)\tSObject" : "clone($1)$0",
            "putSObject(String field, SObject value)\tSObject" : "putSObject($1)$0",
            "put(String field, Object value)\tObject" : "put($1)$0",
            "get(String field)\tObject" : "get($1)$0",
            "addError(APEX_OBJECT msg)\tvoid" : "addError($1)$0",
            "setOptions(APEX_OBJECT options)\tvoid" : "setOptions($1)$0",
            "put(Schema.SObjectField field, Object value)\tObject" : "put($1)$0",
            "addError(String msg)\tvoid" : "addError($1)$0",
            "getSObjects(Schema.SObjectField field)\tLIST<SObject>" : "getSObjects($1)$0",
            "getSObject(String field)\tSObject" : "getSObject($1)$0",
            "getSObjectType()\tSchema.SObjectType" : "getSObjectType()$0",
            "getQuickActionName()\tString" : "getQuickActionName()$0",
            "addError(APEX_OBJECT msg, Boolean escape)\tvoid" : "addError($1)$0",
            "clone()\tSObject" : "clone()$0",
            "addError(String msg, Boolean escape)\tvoid" : "addError($1)$0",
            "putSObject(Schema.SObjectField field, SObject value)\tSObject" : "putSObject($1)$0",
            "getOptions()\tDatabase.DMLOptions" : "getOptions()$0",
            "clone(Boolean preserveId, Boolean deep)\tSObject" : "clone($1)$0",
            "getSObjects(String field)\tLIST<SObject>" : "getSObjects($1)$0"
        }
    },
    "userprofile" : {
        "constructors" : {},
        "name" : "UserProfile",
        "properties" : {
            "url" : "url$0",
            "tabs" : "tabs$0",
            "capabilities" : "capabilities$0",
            "id" : "id$0",
            "userDetail" : "userDetail$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "picklistentry" : {
        "constructors" : {},
        "name" : "PicklistEntry",
        "properties" : {},
        "methods" : {
            "isActive()\tBoolean" : "isActive()$0",
            "isDefaultValue()\tBoolean" : "isDefaultValue()$0",
            "getLabel()\tString" : "getLabel()$0",
            "getValue()\tString" : "getValue()$0"
        }
    },
    "currency" : {
        "constructors" : {},
        "name" : "CURRENCY",
        "properties" : {},
        "methods" : {
            "formatAmount()\tString" : "formatAmount()$0",
            "newInstance(Decimal amount, String isoCode)\tCURRENCY" : "newInstance($1)$0",
            "format()\tString" : "format()$0"
        }
    },
    "staticresourcecalloutmock" : {
        "constructors" : {},
        "name" : "StaticResourceCalloutMock",
        "properties" : {},
        "methods" : {
            "respond(System.HttpRequest request)\tSystem.HttpResponse" : "respond($1)$0",
            "setHeader(String key, String val)\tvoid" : "setHeader($1)$0",
            "setStaticResource(String staticResourceName)\tvoid" : "setStaticResource($1)$0",
            "setStatusCode(Integer code)\tvoid" : "setStatusCode($1)$0",
            "setStatus(String status)\tvoid" : "setStatus($1)$0"
        }
    },
    "emailfileattachment" : {
        "constructors" : {},
        "name" : "EmailFileAttachment",
        "properties" : {},
        "methods" : {
            "setFileName(String param1)\tvoid" : "setFileName($1)$0",
            "setInline(Boolean param1)\tvoid" : "setInline($1)$0",
            "setContentType(String param1)\tvoid" : "setContentType($1)$0",
            "getBody()\tBlob" : "getBody()$0",
            "getFileName()\tString" : "getFileName()$0",
            "getContentType()\tString" : "getContentType()$0",
            "setBody(Blob param1)\tvoid" : "setBody($1)$0",
            "getInline()\tBoolean" : "getInline()$0"
        }
    },
    "mentionsegment" : {
        "constructors" : {},
        "name" : "MentionSegment",
        "properties" : {
            "record" : "record$0",
            "accessible" : "accessible$0",
            "user" : "user$0",
            "name" : "name$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "crypto" : {
        "constructors" : {},
        "name" : "Crypto",
        "properties" : {},
        "methods" : {
            "getRandomInteger()\tInteger" : "getRandomInteger()$0",
            "encrypt(String algorithmName, Blob secretKey, Blob initializationVector, Blob clearData)\tBlob" : "encrypt($1)$0",
            "decrypt(String algorithmName, Blob secretKey, Blob initializationVector, Blob encryptedData)\tBlob" : "decrypt($1)$0",
            "sign(String algorithmName, Blob input, Blob privateKey)\tBlob" : "sign($1)$0",
            "generateMac(String algorithmName, Blob input, Blob privateKey)\tBlob" : "generateMac($1)$0",
            "generateAesKey(Integer size)\tBlob" : "generateAesKey($1)$0",
            "encryptWithManagedIV(String algorithmName, Blob secretKey, Blob clearData)\tBlob" : "encryptWithManagedIV($1)$0",
            "decryptWithManagedIV(String algorithmName, Blob secretKey, Blob encryptedData)\tBlob" : "decryptWithManagedIV($1)$0",
            "generateDigest(String algorithmName, Blob input)\tBlob" : "generateDigest($1)$0",
            "getRandomLong()\tLong" : "getRandomLong()$0"
        }
    },
    "set" : {
        "constructors" : {},
        "name" : "Set",
        "properties" : {},
        "methods" : {
            "retainAll(SET elements)\tBoolean" : "retainAll($1)$0",
            "addAll(LIST elements)\tBoolean" : "addAll($1)$0",
            "clear()\tvoid" : "clear()$0",
            "iterator()\tsystem.ListIterator" : "iterator()$0",
            "clone()\tSET<String>" : "clone()$0",
            "contains(ANY element)\tBoolean" : "contains($1)$0",
            "retainAll(LIST elements)\tBoolean" : "retainAll($1)$0",
            "removeAll(SET elements)\tBoolean" : "removeAll($1)$0",
            "addAll(SET elements)\tBoolean" : "addAll($1)$0",
            "remove(ANY element)\tBoolean" : "remove($1)$0",
            "containsAll(LIST elements)\tBoolean" : "containsAll($1)$0",
            "removeAll(LIST elements)\tBoolean" : "removeAll($1)$0",
            "equals(ANY obj)\tBoolean" : "equals($1)$0",
            "containsAll(SET elements)\tBoolean" : "containsAll($1)$0",
            "size()\tInteger" : "size()$0",
            "add(ANY element)\tBoolean" : "add($1)$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "isEmpty()\tBoolean" : "isEmpty()$0"
        }
    },
    "reportdetailrow" : {
        "constructors" : {},
        "name" : "ReportDetailRow",
        "properties" : {},
        "methods" : {
            "setDataCells(LIST<reports.ReportDataCell> dataCells)\tvoid" : "setDataCells($1)$0",
            "getDataCells()\tLIST<reports.ReportDataCell>" : "getDataCells()$0"
        }
    },
    "recordfield" : {
        "constructors" : {},
        "name" : "RecordField",
        "properties" : {},
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "touchhandledexception" : {
        "constructors" : {},
        "name" : "TouchHandledException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "describequickactiondefaultvalue" : {
        "constructors" : {},
        "name" : "DescribeQuickActionDefaultValue",
        "properties" : {},
        "methods" : {
            "getDefaultValue()\tString" : "getDefaultValue()$0",
            "getField()\tString" : "getField()$0"
        }
    },
    "emailtemplateselector" : {
        "constructors" : {},
        "name" : "EmailTemplateSelector",
        "properties" : {},
        "methods" : {
            "getDefaultEmailTemplateId(Id param1)\tId" : "getDefaultEmailTemplateId($1)$0"
        }
    },
    "pagereference" : {
        "constructors" : {},
        "name" : "PageReference",
        "properties" : {},
        "methods" : {
            "getCookies()\tMAP<String,System.Cookie>" : "getCookies()$0",
            "getParameters()\tMAP<String,String>" : "getParameters()$0",
            "getContentAsPDF()\tBlob" : "getContentAsPDF()$0",
            "getContent()\tBlob" : "getContent()$0",
            "setCookies(LIST<System.Cookie> cookies)\tvoid" : "setCookies($1)$0",
            "getHeaders()\tMAP<String,String>" : "getHeaders()$0",
            "getUrl()\tString" : "getUrl()$0",
            "getRedirect()\tBoolean" : "getRedirect()$0",
            "setAnchor(String anchor)\tSystem.PageReference" : "setAnchor($1)$0",
            "setRedirect(Boolean redirect)\tSystem.PageReference" : "setRedirect($1)$0",
            "getAnchor()\tString" : "getAnchor()$0"
        }
    },
    "flowexception" : {
        "constructors" : {},
        "name" : "FlowException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "mentioncompletionpage" : {
        "constructors" : {},
        "name" : "MentionCompletionPage",
        "properties" : {
            "currentPageUrl" : "currentPageUrl$0",
            "nextPageUrl" : "nextPageUrl$0",
            "mentionCompletions" : "mentionCompletions$0",
            "previousPageUrl" : "previousPageUrl$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "publishingservice" : {
        "constructors" : {},
        "name" : "PublishingService",
        "properties" : {},
        "methods" : {
            "editOnlineArticle(String articleId, Boolean unpublish)\tString" : "editOnlineArticle($1)$0",
            "editPublishedTranslation(String articleId, String language, Boolean unpublish)\tString" : "editPublishedTranslation($1)$0",
            "deleteArchivedArticle(String articleId)\tvoid" : "deleteArchivedArticle($1)$0",
            "restoreOldVersion(String articleId, Integer versionNumber)\tString" : "restoreOldVersion($1)$0",
            "deleteDraftTranslation(String articleVersionId)\tvoid" : "deleteDraftTranslation($1)$0",
            "scheduleForPublication(String articleId, Datetime scheduledDate)\tvoid" : "scheduleForPublication($1)$0",
            "deleteArchivedArticleVersion(String articleId, Integer versionNumber)\tvoid" : "deleteArchivedArticleVersion($1)$0",
            "deleteDraftArticle(String articleId)\tvoid" : "deleteDraftArticle($1)$0",
            "setTranslationToIncomplete(String articleVersionId)\tvoid" : "setTranslationToIncomplete($1)$0",
            "assignDraftTranslationTask(String translationVersionId, String assigneeId, String instructions, Datetime dueDate, Boolean sendEmailNotification)\tvoid" : "assignDraftTranslationTask($1)$0",
            "editArchivedArticle(String articleId)\tString" : "editArchivedArticle($1)$0",
            "cancelScheduledPublicationOfArticle(String articleId)\tvoid" : "cancelScheduledPublicationOfArticle($1)$0",
            "submitForTranslation(String articleId, String language, String assigneeId, Datetime dueDate)\tString" : "submitForTranslation($1)$0",
            "completeTranslation(String articleVersionId)\tvoid" : "completeTranslation($1)$0",
            "cancelScheduledArchivingOfArticle(String articleId)\tvoid" : "cancelScheduledArchivingOfArticle($1)$0",
            "publishArticle(String articleId, Boolean flagAsNew)\tvoid" : "publishArticle($1)$0",
            "assignDraftArticleTask(String articleId, String assigneeId, String instructions, Datetime dueDate, Boolean sendEmailNotification)\tvoid" : "assignDraftArticleTask($1)$0",
            "archiveOnlineArticle(String articleId, Datetime scheduledDate)\tvoid" : "archiveOnlineArticle($1)$0"
        }
    },
    "describeavailablequickactionresult" : {
        "constructors" : {},
        "name" : "DescribeAvailableQuickActionResult",
        "properties" : {},
        "methods" : {
            "getType()\tString" : "getType()$0",
            "getLabel()\tString" : "getLabel()$0",
            "getName()\tString" : "getName()$0"
        }
    },
    "restcontext" : {
        "constructors" : {},
        "name" : "RestContext",
        "properties" : {
            "response" : "response$0",
            "request" : "request$0"
        },
        "methods" : {}

    },
    "emptystackexception" : {
        "constructors" : {},
        "name" : "EmptyStackException",
        "properties" : {},
        "methods" : {
            "getTypeName()\tString" : "getTypeName()$0"
        }
    },
    "xmlstreamwriter" : {
        "constructors" : {},
        "name" : "XmlStreamWriter",
        "properties" : {},
        "methods" : {
            "writeComment(String data)\tvoid" : "writeComment($1)$0",
            "writeEndElement()\tvoid" : "writeEndElement()$0",
            "writeNamespace(String prefix, String namesapceURI)\tvoid" : "writeNamespace($1)$0",
            "getXmlString()\tString" : "getXmlString()$0",
            "writeCData(String data)\tvoid" : "writeCData($1)$0",
            "close()\tvoid" : "close()$0",
            "writeDefaultNamespace(String namesapceURI)\tvoid" : "writeDefaultNamespace($1)$0",
            "writeAttribute(String prefix, String namespaceURI, String localName, String value)\tvoid" : "writeAttribute($1)$0",
            "writeProcessingInstruction(String target, String data)\tvoid" : "writeProcessingInstruction($1)$0",
            "writeEmptyElement(String prefix, String localName, String namesapceURI)\tvoid" : "writeEmptyElement($1)$0",
            "writeStartElement(String prefix, String localName, String namesapceURI)\tvoid" : "writeStartElement($1)$0",
            "setDefaultNamespace(String uri)\tvoid" : "setDefaultNamespace($1)$0",
            "writeCharacters(String text)\tvoid" : "writeCharacters($1)$0",
            "writeEndDocument()\tvoid" : "writeEndDocument()$0",
            "writeStartDocument(String encoding, String version)\tvoid" : "writeStartDocument($1)$0"
        }
    },
    "trackedchangeattachment" : {
        "constructors" : {},
        "name" : "TrackedChangeAttachment",
        "properties" : {
            "changes" : "changes$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "invalidheaderexception" : {
        "constructors" : {},
        "name" : "InvalidHeaderException",
        "properties" : {},
        "methods" : {
            "getTypeName()\tString" : "getTypeName()$0"
        }
    },
    "zonesearchresult" : {
        "constructors" : {},
        "name" : "ZoneSearchResult",
        "properties" : {
            "voteCount" : "voteCount$0",
            "title" : "title$0",
            "id" : "id$0",
            "hasBestAnswer" : "hasBestAnswer$0",
            "type" : "type$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "messaging" : {
        "constructors" : {},
        "name" : "Messaging",
        "properties" : ["BinaryAttachment", "EmailFileAttachment", "Header", "TextAttachment", "MassEmailMessage", "EmailToSalesforceHandler", "InboundEmailResult", "SingleEmailMessage", "InboundEmail", "EmailAttachment", "InboundEnvelope", "InboundEmailHandler"],
        "methods" : {
            "sendEmailMessage(LIST<Id> emailMessagesIds, Boolean allOrNothing)\tLIST<Messaging.SendEmailResult>" : "sendEmailMessage($1)$0",
            "sendEmailMessage(LIST<Id> emailMessagesIds)\tLIST<Messaging.SendEmailResult>" : "sendEmailMessage($1)$0",
            "sendEmail(LIST<Messaging.Email> emailMessages, Boolean allOrNothing)\tLIST<Messaging.SendEmailResult>" : "sendEmail($1)$0",
            "sendEmail(LIST<Messaging.Email> emailMessages)\tLIST<Messaging.SendEmailResult>" : "sendEmail($1)$0",
            "reserveMassEmailCapacity(Integer count)\tvoid" : "reserveMassEmailCapacity($1)$0",
            "reserveSingleEmailCapacity(Integer count)\tvoid" : "reserveSingleEmailCapacity($1)$0"
        }
    },
    "mentionvalidations" : {
        "constructors" : {},
        "name" : "MentionValidations",
        "properties" : {
            "mentionValidations" : "mentionValidations$0",
            "hasErrors" : "hasErrors$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "zoneshowin" : {
        "constructors" : {},
        "name" : "ZoneShowIn",
        "properties" : {
            "Internal" : "Internal$0",
            "Community" : "Community$0",
            "Portal" : "Portal$0"
        },
        "methods" : {
            "values()\tLIST<ConnectApi.ZoneShowIn>" : "values()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "mentions" : {
        "constructors" : {},
        "name" : "Mentions",
        "properties" : {},
        "methods" : {
            "getMentionValidations(String communityId, String parentId, LIST<String> recordIds, ConnectApi.FeedItemVisibilityType visibility)\tConnectApi.MentionValidations" : "getMentionValidations($1)$0",
            "getMentionCompletions(String communityId, String q, String contextId)\tConnectApi.MentionCompletionPage" : "getMentionCompletions($1)$0",
            "setTestGetMentionCompletions(String communityId, String q, String contextId, ConnectApi.MentionCompletionType type, Integer pageParam, Integer pageSize, ConnectApi.MentionCompletionPage result)\tvoid" : "setTestGetMentionCompletions($1)$0",
            "getMentionCompletions(String communityId, String q, String contextId, ConnectApi.MentionCompletionType type, Integer pageParam, Integer pageSize)\tConnectApi.MentionCompletionPage" : "getMentionCompletions($1)$0",
            "setTestGetMentionCompletions(String communityId, String q, String contextId, ConnectApi.MentionCompletionPage result)\tvoid" : "setTestGetMentionCompletions($1)$0"
        }
    },
    "dmlexception" : {
        "constructors" : {},
        "name" : "DmlException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getDmlId(Integer index)\tString" : "getDmlId($1)$0",
            "getDmlMessage(Integer index)\tString" : "getDmlMessage($1)$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getNumDml()\tInteger" : "getNumDml()$0",
            "getDmlFields(Integer index)\tLIST<Schema.SObjectField>" : "getDmlFields($1)$0",
            "getDmlType(Integer index)\tsystem.StatusCode" : "getDmlType($1)$0",
            "getDmlIndex(Integer index)\tInteger" : "getDmlIndex($1)$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "getDmlFieldNames(Integer index)\tLIST<String>" : "getDmlFieldNames($1)$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getDmlStatusCode(Integer index)\tString" : "getDmlStatusCode($1)$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "mentionsegmentinput" : {
        "constructors" : {},
        "name" : "MentionSegmentInput",
        "properties" : {
            "id" : "id$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object" : "convertToJavaObject($1)$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "photo" : {
        "constructors" : {},
        "name" : "Photo",
        "properties" : {
            "smallPhotoUrl" : "smallPhotoUrl$0",
            "standardEmailPhotoUrl" : "standardEmailPhotoUrl$0",
            "photoVersionId" : "photoVersionId$0",
            "url" : "url$0",
            "largePhotoUrl" : "largePhotoUrl$0",
            "fullEmailPhotoUrl" : "fullEmailPhotoUrl$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "groupmembershiptype" : {
        "constructors" : {},
        "name" : "GroupMembershipType",
        "properties" : {
            "GroupManager" : "GroupManager$0",
            "StandardMember" : "StandardMember$0",
            "GroupOwner" : "GroupOwner$0",
            "NotAMemberPrivateRequested" : "NotAMemberPrivateRequested$0",
            "NotAMember" : "NotAMember$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<ConnectApi.GroupMembershipType>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "describelayoutitem" : {
        "constructors" : {},
        "name" : "DescribeLayoutItem",
        "properties" : {},
        "methods" : {
            "isEditable()\tBoolean" : "isEditable()$0",
            "isPlaceholder()\tBoolean" : "isPlaceholder()$0",
            "getLabel()\tString" : "getLabel()$0",
            "isRequired()\tBoolean" : "isRequired()$0",
            "getLayoutComponents()\tLIST<QuickAction.DescribeLayoutComponent>" : "getLayoutComponents()$0"
        }
    },
    "canvastemplateattachment" : {
        "constructors" : {},
        "name" : "CanvasTemplateAttachment",
        "properties" : {
            "thumbnailUrl" : "thumbnailUrl$0",
            "icon" : "icon$0",
            "developerName" : "developerName$0",
            "height" : "height$0",
            "title" : "title$0",
            "parameters" : "parameters$0",
            "description" : "description$0",
            "namespacePrefix" : "namespacePrefix$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "reportfilter" : {
        "constructors" : {},
        "name" : "ReportFilter",
        "properties" : {},
        "methods" : {
            "getColumn()\tString" : "getColumn()$0",
            "getOperator()\tString" : "getOperator()$0",
            "getValue()\tString" : "getValue()$0",
            "setColumn(String column)\tvoid" : "setColumn($1)$0",
            "setValue(String value)\tvoid" : "setValue($1)$0",
            "setOperator(String operator)\tvoid" : "setOperator($1)$0"
        }
    },
    "typeexception" : {
        "constructors" : {},
        "name" : "TypeException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "finalexception" : {
        "constructors" : {},
        "name" : "FinalException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "boolean" : {
        "constructors" : {},
        "name" : "Boolean",
        "properties" : {},
        "methods" : {
            "addError(APEX_OBJECT msg, Boolean escape)\tvoid" : "addError($1)$0",
            "addError(String msg)\tvoid" : "addError($1)$0",
            "addError(String msg, Boolean escape)\tvoid" : "addError($1)$0",
            "addError(APEX_OBJECT msg)\tvoid" : "addError($1)$0",
            "valueOf(Object a)\tBoolean" : "valueOf($1)$0"
        }
    },
    "reporttypemetadata" : {
        "constructors" : {},
        "name" : "ReportTypeMetadata",
        "properties" : {},
        "methods" : {
            "setCategories(LIST<reports.ReportTypeColumnCategory> categories)\tvoid" : "setCategories($1)$0",
            "getCategories()\tLIST<reports.ReportTypeColumnCategory>" : "getCategories()$0"
        }
    },
    "chattergrouppage" : {
        "constructors" : {},
        "name" : "ChatterGroupPage",
        "properties" : {
            "currentPageUrl" : "currentPageUrl$0",
            "nextPageUrl" : "nextPageUrl$0",
            "groups" : "groups$0",
            "previousPageUrl" : "previousPageUrl$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "abstractrecordview" : {
        "constructors" : {},
        "name" : "AbstractRecordView",
        "properties" : {},
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "securityexception" : {
        "constructors" : {},
        "name" : "SecurityException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "actorwithid" : {
        "constructors" : {},
        "name" : "ActorWithId",
        "properties" : {
            "mySubscription" : "mySubscription$0",
            "url" : "url$0",
            "id" : "id$0",
            "motif" : "motif$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "pattern" : {
        "constructors" : {},
        "name" : "Pattern",
        "properties" : {},
        "methods" : {
            "pattern()\tString" : "pattern()$0",
            "compile(String regex)\tsystem.Pattern" : "compile($1)$0",
            "matches(String regex, String input)\tBoolean" : "matches($1)$0",
            "split(String input, Integer n)\tLIST<String>" : "split($1)$0",
            "matcher(String input)\tsystem.Matcher" : "matcher($1)$0",
            "quote(String s)\tString" : "quote($1)$0",
            "split(String input)\tLIST<String>" : "split($1)$0"
        }
    },
    "community" : {
        "constructors" : {},
        "name" : "Community",
        "properties" : {
            "url" : "url$0",
            "description" : "description$0",
            "id" : "id$0",
            "invitationsEnabled" : "invitationsEnabled$0",
            "sendWelcomeEmail" : "sendWelcomeEmail$0",
            "status" : "status$0",
            "urlPathPrefix" : "urlPathPrefix$0",
            "name" : "name$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "workflowprocessstatus" : {
        "constructors" : {},
        "name" : "WorkflowProcessStatus",
        "properties" : {
            "Removed" : "Removed$0",
            "Fault" : "Fault$0",
            "Started" : "Started$0",
            "Rejected" : "Rejected$0",
            "Pending" : "Pending$0",
            "Approved" : "Approved$0",
            "Held" : "Held$0",
            "Reassigned" : "Reassigned$0",
            "NoResponse" : "NoResponse$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<ConnectApi.WorkflowProcessStatus>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "comment" : {
        "constructors" : {},
        "name" : "Comment",
        "properties" : {
            "feedItem" : "feedItem$0",
            "id" : "id$0",
            "myLike" : "myLike$0",
            "type" : "type$0",
            "user" : "user$0",
            "relativeCreatedDate" : "relativeCreatedDate$0",
            "createdDate" : "createdDate$0",
            "likes" : "likes$0",
            "parent" : "parent$0",
            "url" : "url$0",
            "attachment" : "attachment$0",
            "clientInfo" : "clientInfo$0",
            "likesMessage" : "likesMessage$0",
            "body" : "body$0",
            "moderationFlags" : "moderationFlags$0",
            "isDeleteRestricted" : "isDeleteRestricted$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "zone" : {
        "constructors" : {},
        "name" : "Zone",
        "properties" : {
            "isChatterAnswers" : "isChatterAnswers$0",
            "description" : "description$0",
            "id" : "id$0",
            "visibility" : "visibility$0",
            "visibilityId" : "visibilityId$0",
            "name" : "name$0",
            "isActive" : "isActive$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "abstractmessagebody" : {
        "constructors" : {},
        "name" : "AbstractMessageBody",
        "properties" : {
            "text" : "text$0",
            "messageSegments" : "messageSegments$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "email" : {
        "constructors" : {},
        "name" : "Email",
        "properties" : {},
        "methods" : {
            "getUseSignature()\tBoolean" : "getUseSignature()$0",
            "getSaveAsActivity()\tBoolean" : "getSaveAsActivity()$0",
            "setReplyTo(String param1)\tvoid" : "setReplyTo($1)$0",
            "setSenderDisplayName(String param1)\tvoid" : "setSenderDisplayName($1)$0",
            "getReplyTo()\tString" : "getReplyTo()$0",
            "setBccSender(Boolean param1)\tvoid" : "setBccSender($1)$0",
            "setSaveAsActivity(Boolean param1)\tvoid" : "setSaveAsActivity($1)$0",
            "getBccSender()\tBoolean" : "getBccSender()$0",
            "setSubject(String param1)\tvoid" : "setSubject($1)$0",
            "getSenderDisplayName()\tString" : "getSenderDisplayName()$0",
            "setUseSignature(Boolean param1)\tvoid" : "setUseSignature($1)$0",
            "getSubject()\tString" : "getSubject()$0",
            "setEmailPriority(String param1)\tvoid" : "setEmailPriority($1)$0",
            "getEmailPriority()\tString" : "getEmailPriority()$0"
        }
    },
    "userdetail" : {
        "constructors" : {},
        "name" : "UserDetail",
        "properties" : {
            "username" : "username$0",
            "chatterActivity" : "chatterActivity$0",
            "followingCounts" : "followingCounts$0",
            "email" : "email$0",
            "phoneNumbers" : "phoneNumbers$0",
            "groupCount" : "groupCount$0",
            "address" : "address$0",
            "thanksReceived" : "thanksReceived$0",
            "aboutMe" : "aboutMe$0",
            "managerId" : "managerId$0",
            "chatterInfluence" : "chatterInfluence$0",
            "managerName" : "managerName$0",
            "followersCount" : "followersCount$0",
            "isActive" : "isActive$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "querylocatorchunkiterator" : {
        "constructors" : {},
        "name" : "QueryLocatorChunkIterator",
        "properties" : {},
        "methods" : {
            "next()\tLIST<SObject>" : "next()$0",
            "hasNext()\tBoolean" : "hasNext()$0"
        }
    },
    "chatterlikepage" : {
        "constructors" : {},
        "name" : "ChatterLikePage",
        "properties" : {
            "total" : "total$0",
            "previousPageToken" : "previousPageToken$0",
            "previousPageUrl" : "previousPageUrl$0",
            "currentPageUrl" : "currentPageUrl$0",
            "nextPageUrl" : "nextPageUrl$0",
            "currentPageToken" : "currentPageToken$0",
            "nextPageToken" : "nextPageToken$0",
            "likes" : "likes$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "groupmembershiprequeststatus" : {
        "constructors" : {},
        "name" : "GroupMembershipRequestStatus",
        "properties" : {
            "Accepted" : "Accepted$0",
            "Declined" : "Declined$0",
            "Pending" : "Pending$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<ConnectApi.GroupMembershipRequestStatus>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "querylocatoriterator" : {
        "constructors" : {},
        "name" : "QueryLocatorIterator",
        "properties" : {},
        "methods" : {
            "next()\tSObject" : "next()$0",
            "hasNext()\tBoolean" : "hasNext()$0"
        }
    },
    "saveresult" : {
        "constructors" : {},
        "name" : "SaveResult",
        "properties" : {},
        "methods" : {
            "getErrors()\tLIST<Database.Error>" : "getErrors()$0",
            "isSuccess()\tBoolean" : "isSuccess()$0",
            "getId()\tId" : "getId()$0"
        }
    },
    "jsonparser" : {
        "constructors" : {},
        "name" : "JSONParser",
        "properties" : {},
        "methods" : {
            "skipChildren()\tvoid" : "skipChildren()$0",
            "readValueAsStrict(system.Type apexType)\tObject" : "readValueAsStrict($1)$0",
            "getBlobValue()\tBlob" : "getBlobValue()$0",
            "getCurrentName()\tString" : "getCurrentName()$0",
            "getDecimalValue()\tDecimal" : "getDecimalValue()$0",
            "getLastClearedToken()\tsystem.JSONToken" : "getLastClearedToken()$0",
            "getLongValue()\tLong" : "getLongValue()$0",
            "getCurrentToken()\tsystem.JSONToken" : "getCurrentToken()$0",
            "getDoubleValue()\tDouble" : "getDoubleValue()$0",
            "getText()\tString" : "getText()$0",
            "getTimeValue()\tTime" : "getTimeValue()$0",
            "readValueAs(system.Type apexType)\tObject" : "readValueAs($1)$0",
            "getBooleanValue()\tBoolean" : "getBooleanValue()$0",
            "getIdValue()\tId" : "getIdValue()$0",
            "nextValue()\tsystem.JSONToken" : "nextValue()$0",
            "getIntegerValue()\tInteger" : "getIntegerValue()$0",
            "clearCurrentToken()\tvoid" : "clearCurrentToken()$0",
            "nextToken()\tsystem.JSONToken" : "nextToken()$0",
            "hasCurrentToken()\tBoolean" : "hasCurrentToken()$0",
            "getDateValue()\tDate" : "getDateValue()$0",
            "getDateTimeValue()\tDatetime" : "getDateTimeValue()$0"
        }
    },
    "feedfavorite" : {
        "constructors" : {},
        "name" : "FeedFavorite",
        "properties" : {
            "searchText" : "searchText$0",
            "url" : "url$0",
            "community" : "community$0",
            "id" : "id$0",
            "type" : "type$0",
            "lastViewDate" : "lastViewDate$0",
            "user" : "user$0",
            "feedUrl" : "feedUrl$0",
            "createdBy" : "createdBy$0",
            "name" : "name$0",
            "target" : "target$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "topicsuggestionpage" : {
        "constructors" : {},
        "name" : "TopicSuggestionPage",
        "properties" : {
            "topicSuggestions" : "topicSuggestions$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "feedsortorder" : {
        "constructors" : {},
        "name" : "FeedSortOrder",
        "properties" : {
            "CreatedDateDesc" : "CreatedDateDesc$0",
            "LastModifiedDateDesc" : "LastModifiedDateDesc$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<ConnectApi.FeedSortOrder>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "plugin" : {
        "constructors" : {},
        "name" : "Plugin",
        "properties" : {},
        "methods" : {
            "invoke(Process.PluginRequest param1)\tProcess.PluginResult" : "invoke($1)$0",
            "describe()\tProcess.PluginDescribeResult" : "describe()$0"
        }
    },
    "apexpages" : {
        "constructors" : {},
        "name" : "ApexPages",
        "properties" : ["IdeaStandardSetController", "Component", "StandardController", "IdeaStandardController", "KnowledgeArticleVersionStandardController", "ComponentIteration", "StandardSetController", "Message", "Severity", "Action"],
        "methods" : {
            "currentPage()\tSystem.PageReference" : "currentPage()$0",
            "getMessages()\tLIST<ApexPages.Message>" : "getMessages()$0",
            "hasMessages()\tBoolean" : "hasMessages()$0",
            "hasMessages(ApexPages.Severity severity)\tBoolean" : "hasMessages($1)$0",
            "addMessage(ApexPages.Message message)\tvoid" : "addMessage($1)$0",
            "addMessages(APEX_OBJECT ex)\tvoid" : "addMessages($1)$0"
        }
    },
    "recordfieldtype" : {
        "constructors" : {},
        "name" : "RecordFieldType",
        "properties" : {
            "Blank" : "Blank$0",
            "Date" : "Date$0",
            "Time" : "Time$0",
            "Email" : "Email$0",
            "Boolean" : "Boolean$0",
            "Address" : "Address$0",
            "Currency" : "Currency$0",
            "LastModifiedBy" : "LastModifiedBy$0",
            "Compound" : "Compound$0",
            "CreatedBy" : "CreatedBy$0",
            "Location" : "Location$0",
            "Reference" : "Reference$0",
            "Text" : "Text$0",
            "DateTime" : "DateTime$0",
            "Number" : "Number$0",
            "Percent" : "Percent$0",
            "Picklist" : "Picklist$0",
            "Phone" : "Phone$0",
            "Name" : "Name$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<ConnectApi.RecordFieldType>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "xmlnodetype" : {
        "constructors" : {},
        "name" : "XmlNodeType",
        "properties" : {
            "TEXT" : "TEXT$0",
            "COMMENT" : "COMMENT$0",
            "ELEMENT" : "ELEMENT$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<Dom.XmlNodeType>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "serializationexception" : {
        "constructors" : {},
        "name" : "SerializationException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "groupinformation" : {
        "constructors" : {},
        "name" : "GroupInformation",
        "properties" : {
            "text" : "text$0",
            "title" : "title$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "aggregatecolumn" : {
        "constructors" : {},
        "name" : "AggregateColumn",
        "properties" : {},
        "methods" : {
            "getLabel()\tString" : "getLabel()$0",
            "setDataType(reports.ColumnDataType dataType)\tvoid" : "setDataType($1)$0",
            "setName(String name)\tvoid" : "setName($1)$0",
            "getName()\tString" : "getName()$0",
            "setLabel(String label)\tvoid" : "setLabel($1)$0",
            "setAcrossGroupingContext(String acrossGroupingContext)\tvoid" : "setAcrossGroupingContext($1)$0",
            "getDataType()\treports.ColumnDataType" : "getDataType()$0",
            "setDownGroupingContext(String downGroupingContext)\tvoid" : "setDownGroupingContext($1)$0",
            "getAcrossGroupingContext()\tString" : "getAcrossGroupingContext()$0",
            "setDataType(String value)\tvoid" : "setDataType($1)$0",
            "getDownGroupingContext()\tString" : "getDownGroupingContext()$0"
        }
    },
    "version" : {
        "constructors" : {},
        "name" : "Version",
        "properties" : {},
        "methods" : {
            "patch()\tInteger" : "patch()$0",
            "compareTo(system.Version other)\tInteger" : "compareTo($1)$0",
            "minor()\tInteger" : "minor()$0",
            "major()\tInteger" : "major()$0"
        }
    },
    "feeddensity" : {
        "constructors" : {},
        "name" : "FeedDensity",
        "properties" : {
            "AllUpdates" : "AllUpdates$0",
            "FewerUpdates" : "FewerUpdates$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<ConnectApi.FeedDensity>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "businesshours" : {
        "constructors" : {},
        "name" : "BusinessHours",
        "properties" : {},
        "methods" : {
            "add(Id businessHoursId, Datetime startDate, Long interval)\tDatetime" : "add($1)$0",
            "addGmt(Id businessHoursId, Datetime startDate, Long interval)\tDatetime" : "addGmt($1)$0",
            "diff(String businessHoursId, Datetime startDate, Datetime endDate)\tLong" : "diff($1)$0",
            "isWithin(String businessHoursId, Datetime targetDate)\tBoolean" : "isWithin($1)$0",
            "nextStartDate(Id businessHoursId, Datetime targetDate)\tDatetime" : "nextStartDate($1)$0"
        }
    },
    "noaccessexception" : {
        "constructors" : {},
        "name" : "NoAccessException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "urlrewriter" : {
        "constructors" : {},
        "name" : "UrlRewriter",
        "properties" : {},
        "methods" : {
            "mapRequestUrl(System.PageReference param1)\tSystem.PageReference" : "mapRequestUrl($1)$0",
            "generateUrlFor(LIST<System.PageReference> param1)\tLIST<System.PageReference>" : "generateUrlFor($1)$0"
        }
    },
    "double" : {
        "constructors" : {},
        "name" : "Double",
        "properties" : {},
        "methods" : {
            "addError(APEX_OBJECT msg, Boolean escape)\tvoid" : "addError($1)$0",
            "addError(String msg)\tvoid" : "addError($1)$0",
            "addError(String msg, Boolean escape)\tvoid" : "addError($1)$0",
            "addError(APEX_OBJECT msg)\tvoid" : "addError($1)$0",
            "format()\tString" : "format()$0",
            "round()\tLong" : "round()$0",
            "valueOf(Object o)\tDouble" : "valueOf($1)$0",
            "valueOf(String str)\tDouble" : "valueOf($1)$0",
            "longValue()\tLong" : "longValue()$0",
            "intValue()\tInteger" : "intValue()$0"
        }
    },
    "childrelationship" : {
        "constructors" : {},
        "name" : "ChildRelationship",
        "properties" : {},
        "methods" : {
            "isRestrictedDelete()\tBoolean" : "isRestrictedDelete()$0",
            "isCascadeDelete()\tBoolean" : "isCascadeDelete()$0",
            "getField()\tSchema.SObjectField" : "getField()$0",
            "getChildSObject()\tSchema.SObjectType" : "getChildSObject()$0",
            "isDeprecatedAndHidden()\tBoolean" : "isDeprecatedAndHidden()$0",
            "getRelationshipName()\tString" : "getRelationshipName()$0"
        }
    },
    "map" : {
        "constructors" : {},
        "name" : "Map",
        "properties" : {},
        "methods" : {
            "clone()\tMAP<String,String>" : "clone()$0",
            "putAll(LIST entries)\tvoid" : "putAll($1)$0",
            "deepClone()\tMAP<String,String>" : "deepClone()$0",
            "clear()\tvoid" : "clear()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "remove(ANY key)\tString" : "remove($1)$0",
            "put(ANY key, ANY value)\tString" : "put($1)$0",
            "getSObjectType()\tSchema.SObjectType" : "getSObjectType()$0",
            "values()\tLIST<String>" : "values()$0",
            "get(ANY key)\tString" : "get($1)$0",
            "equals(ANY obj)\tBoolean" : "equals($1)$0",
            "keySet()\tSET<String>" : "keySet()$0",
            "containsKey(ANY key)\tBoolean" : "containsKey($1)$0",
            "size()\tInteger" : "size()$0",
            "putAll(MAP entries)\tvoid" : "putAll($1)$0",
            "isEmpty()\tBoolean" : "isEmpty()$0"
        }
    },
    "feed" : {
        "constructors" : {},
        "name" : "Feed",
        "properties" : {
            "feedItemsUrl" : "feedItemsUrl$0",
            "isModifiedUrl" : "isModifiedUrl$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "usergrouppage" : {
        "constructors" : {},
        "name" : "UserGroupPage",
        "properties" : {
            "currentPageUrl" : "currentPageUrl$0",
            "nextPageUrl" : "nextPageUrl$0",
            "total" : "total$0",
            "groups" : "groups$0",
            "previousPageUrl" : "previousPageUrl$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "datacategorygroupsobjecttypepair" : {
        "constructors" : {},
        "name" : "DataCategoryGroupSobjectTypePair",
        "properties" : {},
        "methods" : {
            "setDataCategoryGroupName(String param1)\tvoid" : "setDataCategoryGroupName($1)$0",
            "getDataCategoryGroupName()\tString" : "getDataCategoryGroupName()$0",
            "setSobject(String param1)\tvoid" : "setSobject($1)$0",
            "getSobject()\tString" : "getSobject()$0"
        }
    },
    "textsegmentinput" : {
        "constructors" : {},
        "name" : "TextSegmentInput",
        "properties" : {
            "text" : "text$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object" : "convertToJavaObject($1)$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "action" : {
        "constructors" : {},
        "name" : "Action",
        "properties" : {},
        "methods" : {
            "invoke()\tSystem.PageReference" : "invoke()$0",
            "getExpression()\tString" : "getExpression()$0"
        }
    },
    "feedfavoritetype" : {
        "constructors" : {},
        "name" : "FeedFavoriteType",
        "properties" : {
            "ListView" : "ListView$0",
            "Search" : "Search$0",
            "Topic" : "Topic$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0",
            "values()\tLIST<ConnectApi.FeedFavoriteType>" : "values()$0"
        }
    },
    "chatteractivity" : {
        "constructors" : {},
        "name" : "ChatterActivity",
        "properties" : {
            "postCount" : "postCount$0",
            "commentCount" : "commentCount$0",
            "commentReceivedCount" : "commentReceivedCount$0",
            "likeReceivedCount" : "likeReceivedCount$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "dashboardcomponentattachment" : {
        "constructors" : {},
        "name" : "DashboardComponentAttachment",
        "properties" : {
            "thumbnailUrl" : "thumbnailUrl$0",
            "lastRefreshDate" : "lastRefreshDate$0",
            "componentName" : "componentName$0",
            "dashboardName" : "dashboardName$0",
            "runningUser" : "runningUser$0",
            "fullSizeImageUrl" : "fullSizeImageUrl$0",
            "componentId" : "componentId$0",
            "dashboardBodyText" : "dashboardBodyText$0",
            "dashboardId" : "dashboardId$0",
            "lastRefreshDateDisplayText" : "lastRefreshDateDisplayText$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "mentioncompletiontype" : {
        "constructors" : {},
        "name" : "MentionCompletionType",
        "properties" : {
            "All" : "All$0",
            "User" : "User$0",
            "Group" : "Group$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<ConnectApi.MentionCompletionType>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "getupdatedresult" : {
        "constructors" : {},
        "name" : "GetUpdatedResult",
        "properties" : {},
        "methods" : {
            "getIds()\tLIST<Id>" : "getIds()$0",
            "getLatestDateCovered()\tDate" : "getLatestDateCovered()$0"
        }
    },
    "communitymoderation" : {
        "constructors" : {},
        "name" : "CommunityModeration",
        "properties" : {},
        "methods" : {
            "addFlagToComment(String communityId, String commentId)\tConnectApi.ModerationFlags" : "addFlagToComment($1)$0",
            "addFlagToFeedItem(String communityId, String feedItemId)\tConnectApi.ModerationFlags" : "addFlagToFeedItem($1)$0",
            "removeFlagFromFeedItem(String communityId, String feedItemId, String userId)\tvoid" : "removeFlagFromFeedItem($1)$0",
            "removeFlagFromComment(String communityId, String commentId, String userId)\tvoid" : "removeFlagFromComment($1)$0",
            "getFlagsOnComment(String communityId, String commentId)\tConnectApi.ModerationFlags" : "getFlagsOnComment($1)$0",
            "getFlagsOnFeedItem(String communityId, String feedItemId)\tConnectApi.ModerationFlags" : "getFlagsOnFeedItem($1)$0"
        }
    },
    "messagebodyinput" : {
        "constructors" : {},
        "name" : "MessageBodyInput",
        "properties" : {
            "messageSegments" : "messageSegments$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object" : "convertToJavaObject($1)$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "userinfo" : {
        "constructors" : {},
        "name" : "UserInfo",
        "properties" : {},
        "methods" : {
            "getSessionId()\tString" : "getSessionId()$0",
            "getUserName()\tString" : "getUserName()$0",
            "getFirstName()\tString" : "getFirstName()$0",
            "getUserType()\tString" : "getUserType()$0",
            "getLocale()\tString" : "getLocale()$0",
            "isCurrentUserLicensed(String namespacePrefix)\tBoolean" : "isCurrentUserLicensed($1)$0",
            "getUserRoleId()\tString" : "getUserRoleId()$0",
            "getOrganizationName()\tString" : "getOrganizationName()$0",
            "getUiTheme()\tString" : "getUiTheme()$0",
            "getTimeZone()\tsystem.TimeZone" : "getTimeZone()$0",
            "getLastName()\tString" : "getLastName()$0",
            "getOrganizationId()\tString" : "getOrganizationId()$0",
            "isMultiCurrencyOrganization()\tBoolean" : "isMultiCurrencyOrganization()$0",
            "getUiThemeDisplayed()\tString" : "getUiThemeDisplayed()$0",
            "getName()\tString" : "getName()$0",
            "getProfileId()\tString" : "getProfileId()$0",
            "getUserId()\tString" : "getUserId()$0",
            "getUserEmail()\tString" : "getUserEmail()$0",
            "getDefaultCurrency()\tString" : "getDefaultCurrency()$0",
            "getLanguage()\tString" : "getLanguage()$0"
        }
    },
    "photoinput" : {
        "constructors" : {},
        "name" : "PhotoInput",
        "properties" : {
            "cropX" : "cropX$0",
            "cropY" : "cropY$0",
            "fileId" : "fileId$0",
            "cropSize" : "cropSize$0",
            "versionNumber" : "versionNumber$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object" : "convertToJavaObject($1)$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "groupingvalue" : {
        "constructors" : {},
        "name" : "GroupingValue",
        "properties" : {},
        "methods" : {
            "getValue()\tObject" : "getValue()$0",
            "getLabel()\tString" : "getLabel()$0",
            "setLabel(String label)\tvoid" : "setLabel($1)$0",
            "getGroupings()\tLIST<reports.GroupingValue>" : "getGroupings()$0",
            "setGroupings(LIST<reports.GroupingValue> groupings)\tvoid" : "setGroupings($1)$0",
            "setValue(Object value)\tvoid" : "setValue($1)$0",
            "getKey()\tString" : "getKey()$0",
            "setKey(String key)\tvoid" : "setKey($1)$0"
        }
    },
    "deletedrecord" : {
        "constructors" : {},
        "name" : "DeletedRecord",
        "properties" : {},
        "methods" : {
            "getDeletedDate()\tDate" : "getDeletedDate()$0",
            "getId()\tId" : "getId()$0"
        }
    },
    "userchattersettings" : {
        "constructors" : {},
        "name" : "UserChatterSettings",
        "properties" : {
            "defaultGroupEmailFrequency" : "defaultGroupEmailFrequency$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "string" : {
        "constructors" : {},
        "name" : "String",
        "properties" : {},
        "methods" : {
            "replaceFirst(String regex, String replacement)\tString" : "replaceFirst($1)$0",
            "normalizeSpace()\tString" : "normalizeSpace()$0",
            "substringBeforeLast(String separator)\tString" : "substringBeforeLast($1)$0",
            "unescapeCsv()\tString" : "unescapeCsv()$0",
            "substringBetween(String tag)\tString" : "substringBetween($1)$0",
            "isAlphaSpace()\tBoolean" : "isAlphaSpace()$0",
            "isAlpha()\tBoolean" : "isAlpha()$0",
            "isAllLowerCase()\tBoolean" : "isAllLowerCase()$0",
            "difference(String other)\tString" : "difference($1)$0",
            "isNotBlank(String str)\tBoolean" : "isNotBlank($1)$0",
            "substringBetween(String open, String close)\tString" : "substringBetween($1)$0",
            "containsWhitespace()\tBoolean" : "containsWhitespace()$0",
            "lastIndexOf(String str)\tInteger" : "lastIndexOf($1)$0",
            "reverse()\tString" : "reverse()$0",
            "splitByCharacterType()\tLIST<String>" : "splitByCharacterType()$0",
            "indexOf(String str, Integer startPos)\tInteger" : "indexOf($1)$0",
            "abbreviate(Integer maxWidth, Integer offset)\tString" : "abbreviate($1)$0",
            "center(Integer size)\tString" : "center($1)$0",
            "valueOf(Object o)\tString" : "valueOf($1)$0",
            "addError(String msg, Boolean escape)\tvoid" : "addError($1)$0",
            "substringAfterLast(String separator)\tString" : "substringAfterLast($1)$0",
            "length()\tInteger" : "length()$0",
            "valueOfGmt(Datetime dt)\tString" : "valueOfGmt($1)$0",
            "equals(String other)\tBoolean" : "equals($1)$0",
            "left(Integer len)\tString" : "left($1)$0",
            "toUpperCase(String locale)\tString" : "toUpperCase($1)$0",
            "splitByCharacterTypeCamelCase()\tLIST<String>" : "splitByCharacterTypeCamelCase()$0",
            "lastIndexOfIgnoreCase(String searchStr, Integer startPos)\tInteger" : "lastIndexOfIgnoreCase($1)$0",
            "getLevenshteinDistance(String other, Integer threshold)\tInteger" : "getLevenshteinDistance($1)$0",
            "contains(String str)\tBoolean" : "contains($1)$0",
            "valueOf(Decimal d)\tString" : "valueOf($1)$0",
            "addError(APEX_OBJECT msg)\tvoid" : "addError($1)$0",
            "uncapitalize()\tString" : "uncapitalize()$0",
            "removeStartIgnoreCase(String toRemove)\tString" : "removeStartIgnoreCase($1)$0",
            "unescapeEcmaScript()\tString" : "unescapeEcmaScript()$0",
            "swapCase()\tString" : "swapCase()$0",
            "indexOfAnyBut(String searchChars)\tInteger" : "indexOfAnyBut($1)$0",
            "split(String regex)\tLIST<String>" : "split($1)$0",
            "indexOf(String str)\tInteger" : "indexOf($1)$0",
            "unescapeHtml4()\tString" : "unescapeHtml4()$0",
            "escapeHtml4()\tString" : "escapeHtml4()$0",
            "leftPad(Integer len, String padStr)\tString" : "leftPad($1)$0",
            "right(Integer len)\tString" : "right($1)$0",
            "join(APEX_OBJECT iterableObj, String separator)\tString" : "join($1)$0",
            "startsWith(String str)\tBoolean" : "startsWith($1)$0",
            "lastIndexOfIgnoreCase(String searchStr)\tInteger" : "lastIndexOfIgnoreCase($1)$0",
            "substringBefore(String separator)\tString" : "substringBefore($1)$0",
            "escapeHtml3()\tString" : "escapeHtml3()$0",
            "escapeXml()\tString" : "escapeXml()$0",
            "toLowerCase(String locale)\tString" : "toLowerCase($1)$0",
            "isNumericSpace()\tBoolean" : "isNumericSpace()$0",
            "isAllUpperCase()\tBoolean" : "isAllUpperCase()$0",
            "isBlank(String str)\tBoolean" : "isBlank($1)$0",
            "startsWithIgnoreCase(String prefix)\tBoolean" : "startsWithIgnoreCase($1)$0",
            "containsNone(String invalidChars)\tBoolean" : "containsNone($1)$0",
            "isAsciiPrintable()\tBoolean" : "isAsciiPrintable()$0",
            "repeat(Integer numTimes)\tString" : "repeat($1)$0",
            "deleteWhitespace()\tString" : "deleteWhitespace()$0",
            "format(String format, LIST<String> arguments)\tString" : "format($1)$0",
            "indexOfDifference(String other)\tInteger" : "indexOfDifference($1)$0",
            "isNumeric()\tBoolean" : "isNumeric()$0",
            "getCommonPrefix(LIST strings)\tString" : "getCommonPrefix($1)$0",
            "isNotEmpty(String str)\tBoolean" : "isNotEmpty($1)$0",
            "endsWith(String str)\tBoolean" : "endsWith($1)$0",
            "escapeCsv()\tString" : "escapeCsv()$0",
            "toLowerCase()\tString" : "toLowerCase()$0",
            "addError(String msg)\tvoid" : "addError($1)$0",
            "indexOfAny(String searchChars)\tInteger" : "indexOfAny($1)$0",
            "stripHtmlTags()\tString" : "stripHtmlTags()$0",
            "repeat(String separator, Integer numTimes)\tString" : "repeat($1)$0",
            "isEmpty(String str)\tBoolean" : "isEmpty($1)$0",
            "abbreviate(Integer maxWidth)\tString" : "abbreviate($1)$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "endsWithIgnoreCase(String suffix)\tBoolean" : "endsWithIgnoreCase($1)$0",
            "indexOfIgnoreCase(String searchStr)\tInteger" : "indexOfIgnoreCase($1)$0",
            "addError(APEX_OBJECT msg, Boolean escape)\tvoid" : "addError($1)$0",
            "unescapeXml()\tString" : "unescapeXml()$0",
            "isAlphanumeric()\tBoolean" : "isAlphanumeric()$0",
            "isAlphanumericSpace()\tBoolean" : "isAlphanumericSpace()$0",
            "substring(Integer start, Integer end)\tString" : "substring($1)$0",
            "escapeEcmaScript()\tString" : "escapeEcmaScript()$0",
            "getLevenshteinDistance(String other)\tInteger" : "getLevenshteinDistance($1)$0",
            "overlay(String overlay, Integer start, Integer end)\tString" : "overlay($1)$0",
            "lastIndexOf(String searchStr, Integer startPos)\tInteger" : "lastIndexOf($1)$0",
            "valueOf(Datetime dt)\tString" : "valueOf($1)$0",
            "unescapeHtml3()\tString" : "unescapeHtml3()$0",
            "fromCharArray(LIST<Integer> charArr)\tString" : "fromCharArray($1)$0",
            "rightPad(Integer len, String padStr)\tString" : "rightPad($1)$0",
            "valueOf(Integer i)\tString" : "valueOf($1)$0",
            "isWhitespace()\tBoolean" : "isWhitespace()$0",
            "removeEnd(String toRemove)\tString" : "removeEnd($1)$0",
            "trim()\tString" : "trim()$0",
            "indexOfIgnoreCase(String searchStr, Integer startPos)\tInteger" : "indexOfIgnoreCase($1)$0",
            "rightPad(Integer len)\tString" : "rightPad($1)$0",
            "valueOf(Double d)\tString" : "valueOf($1)$0",
            "containsIgnoreCase(String searchStr)\tBoolean" : "containsIgnoreCase($1)$0",
            "containsOnly(String validChars)\tBoolean" : "containsOnly($1)$0",
            "replace(String target, String replacement)\tString" : "replace($1)$0",
            "mid(Integer pos, Integer len)\tString" : "mid($1)$0",
            "center(Integer size, String padStr)\tString" : "center($1)$0",
            "compareTo(String str)\tInteger" : "compareTo($1)$0",
            "removeEndIgnoreCase(String toRemove)\tString" : "removeEndIgnoreCase($1)$0",
            "replaceAll(String regex, String replacement)\tString" : "replaceAll($1)$0",
            "substringAfter(String separator)\tString" : "substringAfter($1)$0",
            "remove(String toRemove)\tString" : "remove($1)$0",
            "split(String regex, Integer limit)\tLIST<String>" : "split($1)$0",
            "escapeSingleQuotes(String s)\tString" : "escapeSingleQuotes($1)$0",
            "valueOf(Date d)\tString" : "valueOf($1)$0",
            "equalsIgnoreCase(String other)\tBoolean" : "equalsIgnoreCase($1)$0",
            "containsAny(String validChars)\tBoolean" : "containsAny($1)$0",
            "countMatches(String searchStr)\tInteger" : "countMatches($1)$0",
            "leftPad(Integer len)\tString" : "leftPad($1)$0",
            "toUpperCase()\tString" : "toUpperCase()$0",
            "capitalize()\tString" : "capitalize()$0",
            "valueOf(Long l)\tString" : "valueOf($1)$0",
            "substring(Integer start)\tString" : "substring($1)$0",
            "removeStart(String toRemove)\tString" : "removeStart($1)$0"
        }
    },
    "jsonexception" : {
        "constructors" : {},
        "name" : "JSONException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "blankrecordfield" : {
        "constructors" : {},
        "name" : "BlankRecordField",
        "properties" : {},
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "usertype" : {
        "constructors" : {},
        "name" : "UserType",
        "properties" : {
            "Undefined" : "Undefined$0",
            "System" : "System$0",
            "Internal" : "Internal$0",
            "ChatterOnly" : "ChatterOnly$0",
            "ChatterGuest" : "ChatterGuest$0",
            "Guest" : "Guest$0",
            "Portal" : "Portal$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<ConnectApi.UserType>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "topic" : {
        "constructors" : {},
        "name" : "Topic",
        "properties" : {
            "talkingAbout" : "talkingAbout$0",
            "url" : "url$0",
            "description" : "description$0",
            "id" : "id$0",
            "createdDate" : "createdDate$0",
            "name" : "name$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "livechatroutingresult" : {
        "constructors" : {},
        "name" : "LiveChatRoutingResult",
        "properties" : {},
        "methods" : {
            "getChatKey()\tString" : "getChatKey()$0",
            "isSuccess()\tBoolean" : "isSuccess()$0"
        }
    },
    "commentpage" : {
        "constructors" : {},
        "name" : "CommentPage",
        "properties" : {
            "total" : "total$0",
            "comments" : "comments$0",
            "currentPageUrl" : "currentPageUrl$0",
            "nextPageUrl" : "nextPageUrl$0",
            "currentPageToken" : "currentPageToken$0",
            "nextPageToken" : "nextPageToken$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "processrequest" : {
        "constructors" : {},
        "name" : "ProcessRequest",
        "properties" : {},
        "methods" : {
            "setNextApproverIds(LIST<Id> param1)\tvoid" : "setNextApproverIds($1)$0",
            "setComments(String param1)\tvoid" : "setComments($1)$0",
            "getComments()\tString" : "getComments()$0",
            "getNextApproverIds()\tLIST<Id>" : "getNextApproverIds()$0"
        }
    },
    "leadconvertresult" : {
        "constructors" : {},
        "name" : "LeadConvertResult",
        "properties" : {},
        "methods" : {
            "getLeadId()\tId" : "getLeadId()$0",
            "getContactId()\tId" : "getContactId()$0",
            "isSuccess()\tBoolean" : "isSuccess()$0",
            "getErrors()\tLIST<Database.Error>" : "getErrors()$0",
            "getOpportunityId()\tId" : "getOpportunityId()$0",
            "getAccountId()\tId" : "getAccountId()$0"
        }
    },
    "filteroperator" : {
        "constructors" : {},
        "name" : "FilterOperator",
        "properties" : {},
        "methods" : {
            "setLabel(String label)\tvoid" : "setLabel($1)$0",
            "setName(String name)\tvoid" : "setName($1)$0",
            "getLabel()\tString" : "getLabel()$0",
            "getName()\tString" : "getName()$0"
        }
    },
    "ideastandardsetcontroller" : {
        "constructors" : {},
        "name" : "IdeaStandardSetController",
        "properties" : {},
        "methods" : {
            "last()\tvoid" : "last()$0",
            "getPageNumber()\tInteger" : "getPageNumber()$0",
            "getRecords()\tLIST<SObject>" : "getRecords()$0",
            "setPageSize(Integer pageSize)\tvoid" : "setPageSize($1)$0",
            "getRecord()\tSObject" : "getRecord()$0",
            "previous()\tvoid" : "previous()$0",
            "addFields(LIST<String> fieldNames)\tvoid" : "addFields($1)$0",
            "getSelected()\tLIST<SObject>" : "getSelected()$0",
            "setFilterId(String filterId)\tvoid" : "setFilterId($1)$0",
            "reset()\tvoid" : "reset()$0",
            "getHasNext()\tBoolean" : "getHasNext()$0",
            "getListViewOptions()\tLIST<System.SelectOption>" : "getListViewOptions()$0",
            "save()\tSystem.PageReference" : "save()$0",
            "next()\tvoid" : "next()$0",
            "setSelected(LIST<SObject> selected)\tvoid" : "setSelected($1)$0",
            "setPageNumber(Integer pageNumber)\tvoid" : "setPageNumber($1)$0",
            "getResultSize()\tInteger" : "getResultSize()$0",
            "getHasPrevious()\tBoolean" : "getHasPrevious()$0",
            "getFilterId()\tString" : "getFilterId()$0",
            "first()\tvoid" : "first()$0",
            "getIdeaList()\tLIST<Idea>" : "getIdeaList()$0",
            "getCompleteResult()\tBoolean" : "getCompleteResult()$0",
            "getPageSize()\tInteger" : "getPageSize()$0",
            "cancel()\tSystem.PageReference" : "cancel()$0"
        }
    },
    "handledexception" : {
        "constructors" : {},
        "name" : "HandledException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "site" : {
        "constructors" : {},
        "name" : "Site",
        "properties" : ["UrlRewriter"],
        "methods" : {
            "getAnalyticsTrackingCode()\tString" : "getAnalyticsTrackingCode()$0",
            "getPrefix()\tString" : "getPrefix()$0",
            "getOriginalUrl()\tString" : "getOriginalUrl()$0",
            "getCurrentSiteUrl()\tString" : "getCurrentSiteUrl()$0",
            "changePassword(String newPassword, String verifyNewPassword)\tSystem.PageReference" : "changePassword($1)$0",
            "getAdminEmail()\tString" : "getAdminEmail()$0",
            "getTemplate()\tSystem.PageReference" : "getTemplate()$0",
            "createPortalUser(SObject user, String accountId, String password, Boolean sendEmailConfirmation)\tId" : "createPortalUser($1)$0",
            "getErrorMessage()\tString" : "getErrorMessage()$0",
            "isRegistrationEnabled()\tBoolean" : "isRegistrationEnabled()$0",
            "getName()\tString" : "getName()$0",
            "forgotPassword(String username)\tBoolean" : "forgotPassword($1)$0",
            "createPersonAccountPortalUser(SObject user, String ownerId, String recordTypeId, String password)\tId" : "createPersonAccountPortalUser($1)$0",
            "createPortalUser(SObject user, String accountId)\tId" : "createPortalUser($1)$0",
            "isLoginEnabled()\tBoolean" : "isLoginEnabled()$0",
            "login(String username, String password, String startUrl)\tSystem.PageReference" : "login($1)$0",
            "createPortalUser(SObject user, String accountId, String password)\tId" : "createPortalUser($1)$0",
            "changePassword(String newPassword, String verifyNewPassword, String oldPassword)\tSystem.PageReference" : "changePassword($1)$0",
            "getCustomWebAddress()\tString" : "getCustomWebAddress()$0",
            "isPasswordExpired()\tBoolean" : "isPasswordExpired()$0",
            "getAdminId()\tId" : "getAdminId()$0",
            "getDomain()\tString" : "getDomain()$0",
            "createPersonAccountPortalUser(SObject user, String ownerId, String password)\tId" : "createPersonAccountPortalUser($1)$0",
            "setPortalUserAsAuthProvider(SObject user, String accountId)\tvoid" : "setPortalUserAsAuthProvider($1)$0",
            "getErrorDescription()\tString" : "getErrorDescription()$0"
        }
    },
    "actiondml" : {
        "constructors" : {},
        "name" : "ActionDml",
        "properties" : {},
        "methods" : {
            "invoke()\tvoid" : "invoke()$0"
        }
    },
    "restresponse" : {
        "constructors" : {},
        "name" : "RestResponse",
        "properties" : {
            "headers" : "headers$0",
            "statusCode" : "statusCode$0",
            "responseBody" : "responseBody$0"
        },
        "methods" : {
            "addHeader(String name, String value)\tvoid" : "addHeader($1)$0"
        }
    },
    "describedatacategorygroupstructureresult" : {
        "constructors" : {},
        "name" : "DescribeDataCategoryGroupStructureResult",
        "properties" : {},
        "methods" : {
            "getTopCategories()\tLIST<Schema.DataCategory>" : "getTopCategories()$0",
            "getName()\tString" : "getName()$0",
            "getSobject()\tString" : "getSobject()$0",
            "getLabel()\tString" : "getLabel()$0",
            "getDescription()\tString" : "getDescription()$0"
        }
    },
    "unexpectedexception" : {
        "constructors" : {},
        "name" : "UnexpectedException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "describefieldresult" : {
        "constructors" : {},
        "name" : "DescribeFieldResult",
        "properties" : {},
        "methods" : {
            "isNamePointing()\tBoolean" : "isNamePointing()$0",
            "isRestrictedDelete()\tBoolean" : "isRestrictedDelete()$0",
            "getInlineHelpText()\tString" : "getInlineHelpText()$0",
            "getByteLength()\tInteger" : "getByteLength()$0",
            "getReferenceTo()\tLIST<Schema.SObjectType>" : "getReferenceTo()$0",
            "isRestrictedPicklist()\tBoolean" : "isRestrictedPicklist()$0",
            "getType()\tSchema.DisplayType" : "getType()$0",
            "isNameField()\tBoolean" : "isNameField()$0",
            "getLength()\tInteger" : "getLength()$0",
            "isDependentPicklist()\tBoolean" : "isDependentPicklist()$0",
            "getPicklistValues()\tLIST<Schema.PicklistEntry>" : "getPicklistValues()$0",
            "isExternalId()\tBoolean" : "isExternalId()$0",
            "isHtmlFormatted()\tBoolean" : "isHtmlFormatted()$0",
            "isCascadeDelete()\tBoolean" : "isCascadeDelete()$0",
            "getDigits()\tInteger" : "getDigits()$0",
            "isSortable()\tBoolean" : "isSortable()$0",
            "isAccessible()\tBoolean" : "isAccessible()$0",
            "isCaseSensitive()\tBoolean" : "isCaseSensitive()$0",
            "isUnique()\tBoolean" : "isUnique()$0",
            "getLocalName()\tString" : "getLocalName()$0",
            "isAutoNumber()\tBoolean" : "isAutoNumber()$0",
            "getDefaultValueFormula()\tString" : "getDefaultValueFormula()$0",
            "getRelationshipOrder()\tInteger" : "getRelationshipOrder()$0",
            "isDisplayLocationInDecimal()\tBoolean" : "isDisplayLocationInDecimal()$0",
            "getLabel()\tString" : "getLabel()$0",
            "isNillable()\tBoolean" : "isNillable()$0",
            "getScale()\tInteger" : "getScale()$0",
            "isCalculated()\tBoolean" : "isCalculated()$0",
            "getController()\tSchema.SObjectField" : "getController()$0",
            "isDefaultedOnCreate()\tBoolean" : "isDefaultedOnCreate()$0",
            "isWriteRequiresMasterRead()\tBoolean" : "isWriteRequiresMasterRead()$0",
            "isPermissionable()\tBoolean" : "isPermissionable()$0",
            "getName()\tString" : "getName()$0",
            "isUpdateable()\tBoolean" : "isUpdateable()$0",
            "isCreateable()\tBoolean" : "isCreateable()$0",
            "getSobjectField()\tSchema.SObjectField" : "getSobjectField()$0",
            "isGroupable()\tBoolean" : "isGroupable()$0",
            "getSoapType()\tSchema.SoapType" : "getSoapType()$0",
            "isCustom()\tBoolean" : "isCustom()$0",
            "isFilterable()\tBoolean" : "isFilterable()$0",
            "isDeprecatedAndHidden()\tBoolean" : "isDeprecatedAndHidden()$0",
            "getCalculatedFormula()\tString" : "getCalculatedFormula()$0",
            "getDefaultValue()\tObject" : "getDefaultValue()$0",
            "isIdLookup()\tBoolean" : "isIdLookup()$0",
            "getPrecision()\tInteger" : "getPrecision()$0",
            "getRelationshipName()\tString" : "getRelationshipName()$0"
        }
    },
    "chatterusers" : {
        "constructors" : {},
        "name" : "ChatterUsers",
        "properties" : {},
        "methods" : {
            "searchUsers(String communityId, String q, Integer pageParam, Integer pageSize)\tConnectApi.UserPage" : "searchUsers($1)$0",
            "getFollowings(String communityId, String userId)\tConnectApi.FollowingPage" : "getFollowings($1)$0",
            "searchUsers(String communityId, String q)\tConnectApi.UserPage" : "searchUsers($1)$0",
            "getUsers(String communityId)\tConnectApi.UserPage" : "getUsers($1)$0",
            "getGroups(String communityId, String userId)\tConnectApi.UserGroupPage" : "getGroups($1)$0",
            "getFollowers(String communityId, String userId, Integer pageParam, Integer pageSize)\tConnectApi.FollowerPage" : "getFollowers($1)$0",
            "setPhoto(String communityId, String userId, ConnectApi.BinaryInput fileUpload)\tConnectApi.Photo" : "setPhoto($1)$0",
            "setPhotoWithAttributes(String communityId, String userId, ConnectApi.PhotoInput photo)\tConnectApi.Photo" : "setPhotoWithAttributes($1)$0",
            "setTestSearchUsers(String communityId, String q, Integer pageParam, Integer pageSize, ConnectApi.UserPage result)\tvoid" : "setTestSearchUsers($1)$0",
            "getUser(String communityId, String userId)\tConnectApi.UserDetail" : "getUser($1)$0",
            "getFollowings(String communityId, String userId, String filterType, Integer pageParam, Integer pageSize)\tConnectApi.FollowingPage" : "getFollowings($1)$0",
            "getFollowings(String communityId, String userId, String filterType)\tConnectApi.FollowingPage" : "getFollowings($1)$0",
            "updateUser(String communityId, String userId, ConnectApi.UserInput userInput)\tConnectApi.UserDetail" : "updateUser($1)$0",
            "getFollowers(String communityId, String userId)\tConnectApi.FollowerPage" : "getFollowers($1)$0",
            "follow(String communityId, String userId, String subjectId)\tConnectApi.Subscription" : "follow($1)$0",
            "getFollowings(String communityId, String userId, String filterType, Integer pageParam)\tConnectApi.FollowingPage" : "getFollowings($1)$0",
            "setTestSearchUsers(String communityId, String q, ConnectApi.UserPage result)\tvoid" : "setTestSearchUsers($1)$0",
            "getChatterSettings(String communityId, String userId)\tConnectApi.UserChatterSettings" : "getChatterSettings($1)$0",
            "setPhoto(String communityId, String userId, String fileId, Integer versionNumber)\tConnectApi.Photo" : "setPhoto($1)$0",
            "getPhoto(String communityId, String userId)\tConnectApi.Photo" : "getPhoto($1)$0",
            "getUsers(String communityId, Integer pageParam, Integer pageSize)\tConnectApi.UserPage" : "getUsers($1)$0",
            "getFollowings(String communityId, String userId, Integer pageParam, Integer pageSize)\tConnectApi.FollowingPage" : "getFollowings($1)$0",
            "searchUsers(String communityId, String q, String searchContextId, Integer pageParam, Integer pageSize)\tConnectApi.UserPage" : "searchUsers($1)$0",
            "updateChatterSettings(String communityId, String userId, ConnectApi.GroupEmailFrequency defaultGroupEmailFrequency)\tConnectApi.UserChatterSettings" : "updateChatterSettings($1)$0",
            "setPhotoWithAttributes(String communityId, String userId, ConnectApi.PhotoInput photo, ConnectApi.BinaryInput fileUpload)\tConnectApi.Photo" : "setPhotoWithAttributes($1)$0",
            "getFollowings(String communityId, String userId, Integer pageParam)\tConnectApi.FollowingPage" : "getFollowings($1)$0",
            "getGroups(String communityId, String userId, Integer pageParam, Integer pageSize)\tConnectApi.UserGroupPage" : "getGroups($1)$0",
            "setTestSearchUsers(String communityId, String q, String searchContextId, Integer pageParam, Integer pageSize, ConnectApi.UserPage result)\tvoid" : "setTestSearchUsers($1)$0",
            "deletePhoto(String communityId, String userId)\tvoid" : "deletePhoto($1)$0"
        }
    },
    "canvasattachmentinput" : {
        "constructors" : {},
        "name" : "CanvasAttachmentInput",
        "properties" : {
            "thumbnailUrl" : "thumbnailUrl$0",
            "height" : "height$0",
            "developerName" : "developerName$0",
            "title" : "title$0",
            "parameters" : "parameters$0",
            "description" : "description$0",
            "namespacePrefix" : "namespacePrefix$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object" : "convertToJavaObject($1)$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "inputparameter" : {
        "constructors" : {},
        "name" : "InputParameter",
        "properties" : {
            "required" : "required$0",
            "parameterType" : "parameterType$0",
            "name" : "name$0",
            "description" : "description$0"
        },
        "methods" : {}

    },
    "messagesegment" : {
        "constructors" : {},
        "name" : "MessageSegment",
        "properties" : {
            "text" : "text$0",
            "type" : "type$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "filepublishstatus" : {
        "constructors" : {},
        "name" : "FilePublishStatus",
        "properties" : {
            "PublicAccess" : "PublicAccess$0",
            "PendingAccess" : "PendingAccess$0",
            "PrivateAccess" : "PrivateAccess$0"
        },
        "methods" : {
            "values()\tLIST<ConnectApi.FilePublishStatus>" : "values()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "usercapabilities" : {
        "constructors" : {},
        "name" : "UserCapabilities",
        "properties" : {
            "canViewFullProfile" : "canViewFullProfile$0",
            "isModerator" : "isModerator$0",
            "canDirectMessage" : "canDirectMessage$0",
            "canEdit" : "canEdit$0",
            "canFollow" : "canFollow$0",
            "canChat" : "canChat$0",
            "canViewFeed" : "canViewFeed$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "processsubmitrequest" : {
        "constructors" : {},
        "name" : "ProcessSubmitRequest",
        "properties" : {},
        "methods" : {
            "setObjectId(String param1)\tvoid" : "setObjectId($1)$0",
            "getObjectId()\tString" : "getObjectId()$0"
        }
    },
    "chatterconversationsummary" : {
        "constructors" : {},
        "name" : "ChatterConversationSummary",
        "properties" : {
            "latestMessage" : "latestMessage$0",
            "url" : "url$0",
            "read" : "read$0",
            "members" : "members$0",
            "id" : "id$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "datacategory" : {
        "constructors" : {},
        "name" : "DataCategory",
        "properties" : {},
        "methods" : {
            "getChildCategories()\tLIST<Schema.DataCategory>" : "getChildCategories()$0",
            "getLabel()\tString" : "getLabel()$0",
            "getName()\tString" : "getName()$0"
        }
    },
    "file" : {
        "constructors" : {},
        "name" : "File",
        "properties" : {
            "contentSize" : "contentSize$0",
            "pdfRenditionStatus" : "pdfRenditionStatus$0",
            "isInMyFileSync" : "isInMyFileSync$0",
            "renditionUrl" : "renditionUrl$0",
            "owner" : "owner$0",
            "thumb720By480RenditionStatus" : "thumb720By480RenditionStatus$0",
            "checksum" : "checksum$0",
            "thumb240By180RenditionStatus" : "thumb240By180RenditionStatus$0",
            "mimeType" : "mimeType$0",
            "renditionUrl240By180" : "renditionUrl240By180$0",
            "origin" : "origin$0",
            "description" : "description$0",
            "fileExtension" : "fileExtension$0",
            "renditionUrl720By480" : "renditionUrl720By480$0",
            "downloadUrl" : "downloadUrl$0",
            "sharingRole" : "sharingRole$0",
            "modifiedDate" : "modifiedDate$0",
            "flashRenditionStatus" : "flashRenditionStatus$0",
            "fileType" : "fileType$0",
            "thumb120By90RenditionStatus" : "thumb120By90RenditionStatus$0",
            "versionNumber" : "versionNumber$0",
            "publishStatus" : "publishStatus$0",
            "contentUrl" : "contentUrl$0",
            "title" : "title$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "nullpointerexception" : {
        "constructors" : {},
        "name" : "NullPointerException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "chattermessage" : {
        "constructors" : {},
        "name" : "ChatterMessage",
        "properties" : {
            "url" : "url$0",
            "conversationId" : "conversationId$0",
            "conversationUrl" : "conversationUrl$0",
            "id" : "id$0",
            "body" : "body$0",
            "recipients" : "recipients$0",
            "sender" : "sender$0",
            "sentDate" : "sentDate$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "quickactionresult" : {
        "constructors" : {},
        "name" : "QuickActionResult",
        "properties" : {},
        "methods" : {
            "getErrors()\tLIST<Database.Error>" : "getErrors()$0",
            "isCreated()\tBoolean" : "isCreated()$0",
            "isSuccess()\tBoolean" : "isSuccess()$0",
            "getIds()\tLIST<Id>" : "getIds()$0"
        }
    },
    "nodatafoundexception" : {
        "constructors" : {},
        "name" : "NoDataFoundException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "mergeresult" : {
        "constructors" : {},
        "name" : "MergeResult",
        "properties" : {},
        "methods" : {
            "getErrors()\tLIST<Database.Error>" : "getErrors()$0",
            "getMergedRecordIds()\tLIST<String>" : "getMergedRecordIds()$0",
            "isSuccess()\tBoolean" : "isSuccess()$0",
            "getUpdatedRelatedIds()\tLIST<String>" : "getUpdatedRelatedIds()$0",
            "getId()\tId" : "getId()$0"
        }
    },
    "zonesearchpage" : {
        "constructors" : {},
        "name" : "ZoneSearchPage",
        "properties" : {
            "currentPageUrl" : "currentPageUrl$0",
            "nextPageUrl" : "nextPageUrl$0",
            "currentPageToken" : "currentPageToken$0",
            "nextPageToken" : "nextPageToken$0",
            "items" : "items$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "inboundsocialpostresult" : {
        "constructors" : {},
        "name" : "InboundSocialPostResult",
        "properties" : {},
        "methods" : {
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "setSuccess(Boolean success)\tvoid" : "setSuccess($1)$0"
        }
    },
    "followingpage" : {
        "constructors" : {},
        "name" : "FollowingPage",
        "properties" : {
            "currentPageUrl" : "currentPageUrl$0",
            "nextPageUrl" : "nextPageUrl$0",
            "total" : "total$0",
            "following" : "following$0",
            "previousPageUrl" : "previousPageUrl$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "reportmanager" : {
        "constructors" : {},
        "name" : "ReportManager",
        "properties" : {},
        "methods" : {
            "runReport(Id reportId, Boolean includeDetails)\treports.ReportResults" : "runReport($1)$0",
            "runReport(Id reportId)\treports.ReportResults" : "runReport($1)$0",
            "describeReport(Id reportId)\treports.ReportDescribeResult" : "describeReport($1)$0"
        }
    },
    "limitexception" : {
        "constructors" : {},
        "name" : "LimitException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "url" : {
        "constructors" : {},
        "name" : "Url",
        "properties" : {},
        "methods" : {
            "getProtocol()\tString" : "getProtocol()$0",
            "sameFile(system.Url other)\tBoolean" : "sameFile($1)$0",
            "getSalesforceBaseUrl()\tsystem.Url" : "getSalesforceBaseUrl()$0",
            "getRef()\tString" : "getRef()$0",
            "getCurrentRequestUrl()\tsystem.Url" : "getCurrentRequestUrl()$0",
            "getFileFieldURL(String objectId, String fieldName)\tString" : "getFileFieldURL($1)$0",
            "getHost()\tString" : "getHost()$0",
            "getPath()\tString" : "getPath()$0",
            "getFile()\tString" : "getFile()$0",
            "getUserInfo()\tString" : "getUserInfo()$0",
            "getAuthority()\tString" : "getAuthority()$0",
            "getQuery()\tString" : "getQuery()$0",
            "getDefaultPort()\tInteger" : "getDefaultPort()$0",
            "toExternalForm()\tString" : "toExternalForm()$0",
            "getPort()\tInteger" : "getPort()$0"
        }
    },
    "reportfactwithdetails" : {
        "constructors" : {},
        "name" : "ReportFactWithDetails",
        "properties" : {},
        "methods" : {
            "getRows()\tLIST<reports.ReportDetailRow>" : "getRows()$0",
            "setRows(LIST<reports.ReportDetailRow> rows)\tvoid" : "setRows($1)$0"
        }
    },
    "applauncherapexcontroller" : {
        "constructors" : {},
        "name" : "AppLauncherApexController",
        "properties" : {},
        "methods" : {
            "getApps()\tLIST<AppMenuItem>" : "getApps()$0"
        }
    },
    "chattermessages" : {
        "constructors" : {},
        "name" : "ChatterMessages",
        "properties" : {},
        "methods" : {
            "searchConversations(String q)\tConnectApi.ChatterConversationPage" : "searchConversations($1)$0",
            "sendMessage(String text, String recipients)\tConnectApi.ChatterMessage" : "sendMessage($1)$0",
            "getMessages(String pageParam, Integer pageSize)\tConnectApi.ChatterMessagePage" : "getMessages($1)$0",
            "getUnreadCount()\tConnectApi.UnreadConversationCount" : "getUnreadCount()$0",
            "searchConversation(String conversationId, String pageParam, Integer pageSize, String q)\tConnectApi.ChatterConversation" : "searchConversation($1)$0",
            "markConversationRead(String conversationId, Boolean read)\tConnectApi.ChatterConversationSummary" : "markConversationRead($1)$0",
            "getConversation(String conversationId, String pageParam, Integer pageSize)\tConnectApi.ChatterConversation" : "getConversation($1)$0",
            "searchConversations(String pageParam, Integer pageSize, String q)\tConnectApi.ChatterConversationPage" : "searchConversations($1)$0",
            "getMessage(String messageId)\tConnectApi.ChatterMessage" : "getMessage($1)$0",
            "getConversations()\tConnectApi.ChatterConversationPage" : "getConversations()$0",
            "searchConversation(String conversationId, String q)\tConnectApi.ChatterConversation" : "searchConversation($1)$0",
            "getConversation(String conversationId)\tConnectApi.ChatterConversation" : "getConversation($1)$0",
            "searchMessages(String pageParam, Integer pageSize, String q)\tConnectApi.ChatterMessagePage" : "searchMessages($1)$0",
            "getMessages()\tConnectApi.ChatterMessagePage" : "getMessages()$0",
            "searchMessages(String q)\tConnectApi.ChatterMessagePage" : "searchMessages($1)$0",
            "getConversations(String pageParam, Integer pageSize)\tConnectApi.ChatterConversationPage" : "getConversations($1)$0",
            "replyToMessage(String text, String inReplyTo)\tConnectApi.ChatterMessage" : "replyToMessage($1)$0"
        }
    },
    "queryexception" : {
        "constructors" : {},
        "name" : "QueryException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "reportlinkformula" : {
        "constructors" : {},
        "name" : "ReportLinkFormula",
        "properties" : {},
        "methods" : {
            "getImage()\treports.ReportImageFormula" : "getImage()$0",
            "setTarget(String target)\tvoid" : "setTarget($1)$0",
            "getTarget()\tString" : "getTarget()$0",
            "getText()\tString" : "getText()$0",
            "getUrl()\tString" : "getUrl()$0",
            "setUrl(String url)\tvoid" : "setUrl($1)$0",
            "setImage(reports.ReportImageFormula image)\tvoid" : "setImage($1)$0",
            "setText(String text)\tvoid" : "setText($1)$0"
        }
    },
    "groupingcolumn" : {
        "constructors" : {},
        "name" : "GroupingColumn",
        "properties" : {},
        "methods" : {
            "setDataType(reports.ColumnDataType dataType)\tvoid" : "setDataType($1)$0",
            "setName(String name)\tvoid" : "setName($1)$0",
            "getLabel()\tString" : "getLabel()$0",
            "setLabel(String label)\tvoid" : "setLabel($1)$0",
            "setGroupingLevel(Integer groupingLevel)\tvoid" : "setGroupingLevel($1)$0",
            "getDataType()\treports.ColumnDataType" : "getDataType()$0",
            "setDataType(String value)\tvoid" : "setDataType($1)$0",
            "getGroupingLevel()\tInteger" : "getGroupingLevel()$0",
            "getName()\tString" : "getName()$0"
        }
    },
    "xmlstreamreader" : {
        "constructors" : {},
        "name" : "XmlStreamReader",
        "properties" : {},
        "methods" : {
            "getPrefix()\tString" : "getPrefix()$0",
            "isWhitespace()\tBoolean" : "isWhitespace()$0",
            "getVersion()\tString" : "getVersion()$0",
            "hasNext()\tBoolean" : "hasNext()$0",
            "getPITarget()\tString" : "getPITarget()$0",
            "getText()\tString" : "getText()$0",
            "isCharacters()\tBoolean" : "isCharacters()$0",
            "getLocation()\tString" : "getLocation()$0",
            "getAttributeLocalName(Integer index)\tString" : "getAttributeLocalName($1)$0",
            "getAttributePrefix(Integer index)\tString" : "getAttributePrefix($1)$0",
            "hasName()\tBoolean" : "hasName()$0",
            "isEndElement()\tBoolean" : "isEndElement()$0",
            "getPIData()\tString" : "getPIData()$0",
            "getNamespace()\tString" : "getNamespace()$0",
            "hasText()\tBoolean" : "hasText()$0",
            "getNamespacePrefix(Integer index)\tString" : "getNamespacePrefix($1)$0",
            "getAttributeCount()\tInteger" : "getAttributeCount()$0",
            "getEventType()\tsystem.XmlTag" : "getEventType()$0",
            "getAttributeValue(String namespaceURI, String localName)\tString" : "getAttributeValue($1)$0",
            "getNamespaceURIAt(Integer index)\tString" : "getNamespaceURIAt($1)$0",
            "getAttributeValueAt(Integer index)\tString" : "getAttributeValueAt($1)$0",
            "getAttributeNamespace(Integer index)\tString" : "getAttributeNamespace($1)$0",
            "toString()\tString" : "toString()$0",
            "setCoalescing(Boolean flag)\tvoid" : "setCoalescing($1)$0",
            "getLocalName()\tString" : "getLocalName()$0",
            "next()\tInteger" : "next()$0",
            "isStartElement()\tBoolean" : "isStartElement()$0",
            "getAttributeType(Integer index)\tString" : "getAttributeType($1)$0",
            "getNamespaceURI(String prefix)\tString" : "getNamespaceURI($1)$0",
            "getNamespaceCount()\tInteger" : "getNamespaceCount()$0",
            "setNamespaceAware(Boolean flag)\tvoid" : "setNamespaceAware($1)$0",
            "nextTag()\tInteger" : "nextTag()$0"
        }
    },
    "visualforceexception" : {
        "constructors" : {},
        "name" : "VisualforceException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "integer" : {
        "constructors" : {},
        "name" : "Integer",
        "properties" : {},
        "methods" : {
            "addError(APEX_OBJECT msg, Boolean escape)\tvoid" : "addError($1)$0",
            "addError(String msg)\tvoid" : "addError($1)$0",
            "addError(String msg, Boolean escape)\tvoid" : "addError($1)$0",
            "addError(APEX_OBJECT msg)\tvoid" : "addError($1)$0",
            "format()\tString" : "format()$0",
            "valueOf(Object o)\tInteger" : "valueOf($1)$0",
            "valueOf(String i)\tInteger" : "valueOf($1)$0"
        }
    },
    "sortorder" : {
        "constructors" : {},
        "name" : "SortOrder",
        "properties" : {
            "Ascending" : "Ascending$0",
            "Descending" : "Descending$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<ConnectApi.SortOrder>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "document" : {
        "constructors" : {},
        "name" : "Document",
        "properties" : {},
        "methods" : {
            "createRootElement(String name, String namespace, String prefix)\tdom.XmlNode" : "createRootElement($1)$0",
            "getRootElement()\tdom.XmlNode" : "getRootElement()$0",
            "load(String xml)\tvoid" : "load($1)$0",
            "toXmlString()\tString" : "toXmlString()$0"
        }
    },
    "complexsegment" : {
        "constructors" : {},
        "name" : "ComplexSegment",
        "properties" : {
            "segments" : "segments$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "communitypage" : {
        "constructors" : {},
        "name" : "CommunityPage",
        "properties" : {
            "total" : "total$0",
            "communities" : "communities$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "ideas" : {
        "constructors" : {},
        "name" : "Ideas",
        "properties" : {},
        "methods" : {
            "getReadRecentReplies(String userId, String communityId)\tLIST<Id>" : "getReadRecentReplies($1)$0",
            "findSimilar(SObject idea)\tLIST<Id>" : "findSimilar($1)$0",
            "getUnreadRecentReplies(String userId, String communityId)\tLIST<Id>" : "getUnreadRecentReplies($1)$0",
            "getAllRecentReplies(String userId, String communityId)\tLIST<Id>" : "getAllRecentReplies($1)$0",
            "markRead(String ideaId)\tvoid" : "markRead($1)$0"
        }
    },
    "reportdescriberesult" : {
        "constructors" : {},
        "name" : "ReportDescribeResult",
        "properties" : {},
        "methods" : {
            "getReportMetadata()\treports.ReportMetadata" : "getReportMetadata()$0",
            "getReportExtendedMetadata()\treports.ReportExtendedMetadata" : "getReportExtendedMetadata()$0",
            "setReportExtendedMetadata(reports.ReportExtendedMetadata reportExtendedMetadata)\tvoid" : "setReportExtendedMetadata($1)$0",
            "setReportTypeMetadata(reports.ReportTypeMetadata reportTypeMetadata)\tvoid" : "setReportTypeMetadata($1)$0",
            "getReportTypeMetadata()\treports.ReportTypeMetadata" : "getReportTypeMetadata()$0",
            "setReportMetadata(reports.ReportMetadata reportMetadata)\tvoid" : "setReportMetadata($1)$0"
        }
    },
    "reference" : {
        "constructors" : {},
        "name" : "Reference",
        "properties" : {
            "url" : "url$0",
            "id" : "id$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "upsertresult" : {
        "constructors" : {},
        "name" : "UpsertResult",
        "properties" : {},
        "methods" : {
            "getErrors()\tLIST<Database.Error>" : "getErrors()$0",
            "isCreated()\tBoolean" : "isCreated()$0",
            "isSuccess()\tBoolean" : "isSuccess()$0",
            "getId()\tId" : "getId()$0"
        }
    },
    "sobjecttype" : {
        "constructors" : {},
        "name" : "SObjectType",
        "properties" : {},
        "methods" : {
            "getDescribe()\tSchema.DescribeSObjectResult" : "getDescribe()$0",
            "newSObject(Id recordTypeId, Boolean loadDefaultValues)\tSObject" : "newSObject($1)$0",
            "newSObject(Id id)\tSObject" : "newSObject($1)$0",
            "newSObject()\tSObject" : "newSObject()$0"
        }
    },
    "basictemplateattachment" : {
        "constructors" : {},
        "name" : "BasicTemplateAttachment",
        "properties" : {
            "icon" : "icon$0",
            "linkUrl" : "linkUrl$0",
            "subtype" : "subtype$0",
            "linkRecordId" : "linkRecordId$0",
            "title" : "title$0",
            "description" : "description$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "reportinstanceattributes" : {
        "constructors" : {},
        "name" : "ReportInstanceAttributes",
        "properties" : {},
        "methods" : {
            "setOwnerId(Id ownerId)\tvoid" : "setOwnerId($1)$0",
            "getCompletionDate()\tString" : "getCompletionDate()$0",
            "setCompletionDate(String completionDate)\tvoid" : "setCompletionDate($1)$0",
            "getRequestDate()\tString" : "getRequestDate()$0",
            "setRequestDate(String requestDate)\tvoid" : "setRequestDate($1)$0",
            "setId(Id id)\tvoid" : "setId($1)$0",
            "getId()\tId" : "getId()$0",
            "getStatus()\tString" : "getStatus()$0",
            "getOwnerId()\tId" : "getOwnerId()$0",
            "setStatus(String status)\tvoid" : "setStatus($1)$0"
        }
    },
    "globalinfluence" : {
        "constructors" : {},
        "name" : "GlobalInfluence",
        "properties" : {
            "percentile" : "percentile$0",
            "rank" : "rank$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "feeditemattachmenttype" : {
        "constructors" : {},
        "name" : "FeedItemAttachmentType",
        "properties" : {
            "Poll" : "Poll$0",
            "TrackedChange" : "TrackedChange$0",
            "Approval" : "Approval$0",
            "CaseComment" : "CaseComment$0",
            "DashboardComponent" : "DashboardComponent$0",
            "Canvas" : "Canvas$0",
            "RecordSnapshot" : "RecordSnapshot$0",
            "Content" : "Content$0",
            "EmailMessage" : "EmailMessage$0",
            "BasicTemplate" : "BasicTemplate$0",
            "Link" : "Link$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<ConnectApi.FeedItemAttachmentType>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "ideastandardcontroller" : {
        "constructors" : {},
        "name" : "IdeaStandardController",
        "properties" : {},
        "methods" : {
            "getSubject()\tSObject" : "getSubject()$0",
            "delete()\tSystem.PageReference" : "delete()$0",
            "edit()\tSystem.PageReference" : "edit()$0",
            "reset()\tvoid" : "reset()$0",
            "getId()\tString" : "getId()$0",
            "getCommentList()\tLIST<IdeaComment>" : "getCommentList()$0",
            "cancel()\tSystem.PageReference" : "cancel()$0",
            "getRecord()\tSObject" : "getRecord()$0",
            "save()\tSystem.PageReference" : "save()$0",
            "view()\tSystem.PageReference" : "view()$0",
            "addFields(LIST<String> fieldNames)\tvoid" : "addFields($1)$0"
        }
    },
    "feediteminput" : {
        "constructors" : {},
        "name" : "FeedItemInput",
        "properties" : {
            "originalFeedItemId" : "originalFeedItemId$0",
            "body" : "body$0",
            "isBookmarkedByCurrentUser" : "isBookmarkedByCurrentUser$0",
            "visibility" : "visibility$0",
            "attachment" : "attachment$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object" : "convertToJavaObject($1)$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "commenttype" : {
        "constructors" : {},
        "name" : "CommentType",
        "properties" : {
            "TextComment" : "TextComment$0",
            "ContentComment" : "ContentComment$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<ConnectApi.CommentType>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "jsongenerator" : {
        "constructors" : {},
        "name" : "JSONGenerator",
        "properties" : {},
        "methods" : {
            "writeBlob(Blob b)\tvoid" : "writeBlob($1)$0",
            "writeNull()\tvoid" : "writeNull()$0",
            "close()\tvoid" : "close()$0",
            "writeDate(Date d)\tvoid" : "writeDate($1)$0",
            "writeObject(Object o)\tvoid" : "writeObject($1)$0",
            "writeTime(Time t)\tvoid" : "writeTime($1)$0",
            "writeStartObject()\tvoid" : "writeStartObject()$0",
            "writeEndObject()\tvoid" : "writeEndObject()$0",
            "writeNumber(Integer i)\tvoid" : "writeNumber($1)$0",
            "writeStringField(String fieldName, String str)\tvoid" : "writeStringField($1)$0",
            "writeDateTime(Datetime dt)\tvoid" : "writeDateTime($1)$0",
            "writeId(Id id)\tvoid" : "writeId($1)$0",
            "writeTimeField(String fieldName, Time t)\tvoid" : "writeTimeField($1)$0",
            "writeNumberField(String fieldName, Double d)\tvoid" : "writeNumberField($1)$0",
            "writeNumber(Long lng)\tvoid" : "writeNumber($1)$0",
            "writeFieldName(String fieldName)\tvoid" : "writeFieldName($1)$0",
            "isClosed()\tBoolean" : "isClosed()$0",
            "writeNumberField(String fieldName, Decimal d)\tvoid" : "writeNumberField($1)$0",
            "writeBooleanField(String fieldName, Boolean b)\tvoid" : "writeBooleanField($1)$0",
            "writeBoolean(Boolean b)\tvoid" : "writeBoolean($1)$0",
            "writeBlobField(String fieldName, Blob b)\tvoid" : "writeBlobField($1)$0",
            "getAsString()\tString" : "getAsString()$0",
            "writeNullField(String fieldName)\tvoid" : "writeNullField($1)$0",
            "writeEndArray()\tvoid" : "writeEndArray()$0",
            "writeDateTimeField(String fieldName, Datetime dt)\tvoid" : "writeDateTimeField($1)$0",
            "writeNumberField(String fieldName, Integer i)\tvoid" : "writeNumberField($1)$0",
            "writeStartArray()\tvoid" : "writeStartArray()$0",
            "writeString(String str)\tvoid" : "writeString($1)$0",
            "writeDateField(String fieldName, Date d)\tvoid" : "writeDateField($1)$0",
            "writeIdField(String fieldName, Id id)\tvoid" : "writeIdField($1)$0",
            "writeNumber(Decimal d)\tvoid" : "writeNumber($1)$0",
            "writeNumber(Double d)\tvoid" : "writeNumber($1)$0",
            "writeObjectField(String fieldName, Object o)\tvoid" : "writeObjectField($1)$0",
            "writeNumberField(String fieldName, Long lng)\tvoid" : "writeNumberField($1)$0"
        }
    },
    "newfileattachmentinput" : {
        "constructors" : {},
        "name" : "NewFileAttachmentInput",
        "properties" : {
            "title" : "title$0",
            "description" : "description$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object" : "convertToJavaObject($1)$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "xmltag" : {
        "constructors" : {},
        "name" : "XmlTag",
        "properties" : {
            "SPACE" : "SPACE$0",
            "START_ELEMENT" : "START_ELEMENT$0",
            "END_DOCUMENT" : "END_DOCUMENT$0",
            "CHARACTERS" : "CHARACTERS$0",
            "PROCESSING_INSTRUCTION" : "PROCESSING_INSTRUCTION$0",
            "END_ELEMENT" : "END_ELEMENT$0",
            "CDATA" : "CDATA$0",
            "ENTITY_REFERENCE" : "ENTITY_REFERENCE$0",
            "ENTITY_DECLARATION" : "ENTITY_DECLARATION$0",
            "ATTRIBUTE" : "ATTRIBUTE$0",
            "DTD" : "DTD$0",
            "START_DOCUMENT" : "START_DOCUMENT$0",
            "NAMESPACE" : "NAMESPACE$0",
            "COMMENT" : "COMMENT$0",
            "NOTATION_DECLARATION" : "NOTATION_DECLARATION$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<system.XmlTag>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "recordview" : {
        "constructors" : {},
        "name" : "RecordView",
        "properties" : {
            "sections" : "sections$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "invalidreadonlyuserdmlexception" : {
        "constructors" : {},
        "name" : "InvalidReadOnlyUserDmlException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "casecommenteventtype" : {
        "constructors" : {},
        "name" : "CaseCommentEventType",
        "properties" : {
            "NewInternal" : "NewInternal$0",
            "NewPublishedByCustomer" : "NewPublishedByCustomer$0",
            "PublishExistingByCustomer" : "PublishExistingByCustomer$0",
            "PublishExisting" : "PublishExisting$0",
            "NewPublished" : "NewPublished$0",
            "UnpublishExistingByCustomer" : "UnpublishExistingByCustomer$0",
            "UnpublishExsiting" : "UnpublishExsiting$0"
        },
        "methods" : {
            "values()\tLIST<ConnectApi.CaseCommentEventType>" : "values()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "subscription" : {
        "constructors" : {},
        "name" : "Subscription",
        "properties" : {
            "url" : "url$0",
            "subscriber" : "subscriber$0",
            "subject" : "subject$0",
            "community" : "community$0",
            "id" : "id$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "sendemailresult" : {
        "constructors" : {},
        "name" : "SendEmailResult",
        "properties" : {},
        "methods" : {
            "getErrors()\tLIST<Messaging.SendEmailError>" : "getErrors()$0",
            "isSuccess()\tBoolean" : "isSuccess()$0"
        }
    },
    "leadconvert" : {
        "constructors" : {},
        "name" : "LeadConvert",
        "properties" : {},
        "methods" : {
            "setOwnerId(Id param1)\tvoid" : "setOwnerId($1)$0",
            "setSendNotificationEmail(Boolean param1)\tvoid" : "setSendNotificationEmail($1)$0",
            "getLeadId()\tId" : "getLeadId()$0",
            "isOverwriteLeadSource()\tBoolean" : "isOverwriteLeadSource()$0",
            "isSendNotificationEmail()\tBoolean" : "isSendNotificationEmail()$0",
            "getContactId()\tId" : "getContactId()$0",
            "getOpportunityName()\tString" : "getOpportunityName()$0",
            "setConvertedStatus(String param1)\tvoid" : "setConvertedStatus($1)$0",
            "isDoNotCreateOpportunity()\tBoolean" : "isDoNotCreateOpportunity()$0",
            "getOwnerId()\tId" : "getOwnerId()$0",
            "setDoNotCreateOpportunity(Boolean param1)\tvoid" : "setDoNotCreateOpportunity($1)$0",
            "getAccountId()\tId" : "getAccountId()$0",
            "getConvertedStatus()\tString" : "getConvertedStatus()$0",
            "setOverwriteLeadSource(Boolean param1)\tvoid" : "setOverwriteLeadSource($1)$0",
            "setAccountId(Id param1)\tvoid" : "setAccountId($1)$0",
            "setOpportunityName(String param1)\tvoid" : "setOpportunityName($1)$0",
            "setLeadId(Id param1)\tvoid" : "setLeadId($1)$0",
            "setContactId(Id param1)\tvoid" : "setContactId($1)$0"
        }
    },
    "describelayoutsection" : {
        "constructors" : {},
        "name" : "DescribeLayoutSection",
        "properties" : {},
        "methods" : {
            "getRows()\tInteger" : "getRows()$0",
            "getColumns()\tInteger" : "getColumns()$0",
            "getLayoutRows()\tLIST<QuickAction.DescribeLayoutRow>" : "getLayoutRows()$0",
            "isUseCollapsibleSection()\tBoolean" : "isUseCollapsibleSection()$0",
            "isUseHeading()\tBoolean" : "isUseHeading()$0",
            "getHeading()\tString" : "getHeading()$0"
        }
    },
    "component" : {
        "constructors" : {},
        "name" : "Component",
        "properties" : {
            "expressions" : "expressions$0",
            "childComponents" : "childComponents$0",
            "componentIterations" : "componentIterations$0",
            "id" : "id$0",
            "facets" : "facets$0",
            "rendered" : "rendered$0",
            "parent" : "parent$0"
        },
        "methods" : {
            "getComponentById(String id)\tApexPages.Component" : "getComponentById($1)$0"
        }
    },
    "binaryattachment" : {
        "constructors" : {},
        "name" : "BinaryAttachment",
        "properties" : {
            "mimeTypeSubType" : "mimeTypeSubType$0",
            "body" : "body$0",
            "fileName" : "fileName$0"
        },
        "methods" : {}

    },
    "metadataexception" : {
        "constructors" : {},
        "name" : "MetadataException",
        "properties" : {},
        "methods" : {
            "getTypeName()\tString" : "getTypeName()$0"
        }
    },
    "chatterfavorites" : {
        "constructors" : {},
        "name" : "ChatterFavorites",
        "properties" : {},
        "methods" : {
            "setTestGetFeedItems(String communityId, String subjectId, String favoriteId, Integer recentCommentCount, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)\tvoid" : "setTestGetFeedItems($1)$0",
            "getFeedItems(String communityId, String subjectId, String favoriteId, Integer recentCommentCount, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)\tConnectApi.FeedItemPage" : "getFeedItems($1)$0",
            "getFeedItems(String communityId, String subjectId, String favoriteId)\tConnectApi.FeedItemPage" : "getFeedItems($1)$0",
            "updateFavorite(String communityId, String subjectId, String favoriteId, Boolean updateLastViewDate)\tConnectApi.FeedFavorite" : "updateFavorite($1)$0",
            "setTestGetFeedItems(String communityId, String subjectId, String favoriteId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)\tvoid" : "setTestGetFeedItems($1)$0",
            "setTestGetFeedItems(String communityId, String subjectId, String favoriteId, ConnectApi.FeedItemPage result)\tvoid" : "setTestGetFeedItems($1)$0",
            "addFavorite(String communityId, String subjectId, String searchText)\tConnectApi.FeedFavorite" : "addFavorite($1)$0",
            "getFavorites(String communityId, String subjectId)\tConnectApi.FeedFavorites" : "getFavorites($1)$0",
            "getFavorite(String communityId, String subjectId, String favoriteId)\tConnectApi.FeedFavorite" : "getFavorite($1)$0",
            "getFeedItems(String communityId, String subjectId, String favoriteId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)\tConnectApi.FeedItemPage" : "getFeedItems($1)$0",
            "deleteFavorite(String communityId, String subjectId, String favoriteId)\tvoid" : "deleteFavorite($1)$0",
            "addRecordFavorite(String communityId, String subjectId, String targetId)\tConnectApi.FeedFavorite" : "addRecordFavorite($1)$0"
        }
    },
    "usersummary" : {
        "constructors" : {},
        "name" : "UserSummary",
        "properties" : {
            "isActive" : "isActive$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "describetabsetresult" : {
        "constructors" : {},
        "name" : "DescribeTabSetResult",
        "properties" : {},
        "methods" : {
            "getLogoUrl()\tString" : "getLogoUrl()$0",
            "isSelected()\tBoolean" : "isSelected()$0",
            "getNamespace()\tString" : "getNamespace()$0",
            "getLabel()\tString" : "getLabel()$0",
            "getTabs()\tLIST<Schema.DescribeTabResult>" : "getTabs()$0"
        }
    },
    "network" : {
        "constructors" : {},
        "name" : "Network",
        "properties" : {},
        "methods" : {
            "getNetworkId()\tString" : "getNetworkId()$0",
            "forwardToAuthPage(String startUrl)\tSystem.PageReference" : "forwardToAuthPage($1)$0",
            "forwardToAuthPage(String startUrl, String displayType)\tSystem.PageReference" : "forwardToAuthPage($1)$0",
            "communitiesLanding()\tSystem.PageReference" : "communitiesLanding()$0"
        }
    },
    "feeditemattachment" : {
        "constructors" : {},
        "name" : "FeedItemAttachment",
        "properties" : {
            "type" : "type$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "asyncexception" : {
        "constructors" : {},
        "name" : "AsyncException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "fieldchangevaluetype" : {
        "constructors" : {},
        "name" : "FieldChangeValueType",
        "properties" : {
            "OldValue" : "OldValue$0",
            "NewValue" : "NewValue$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<ConnectApi.FieldChangeValueType>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "reportresults" : {
        "constructors" : {},
        "name" : "ReportResults",
        "properties" : {},
        "methods" : {
            "setFactMap(MAP<String,reports.ReportFact> factMap)\tvoid" : "setFactMap($1)$0",
            "setReportMetadata(reports.ReportMetadata reportMetadata)\tvoid" : "setReportMetadata($1)$0",
            "setReportExtendedMetadata(reports.ReportExtendedMetadata reportExtendedMetadata)\tvoid" : "setReportExtendedMetadata($1)$0",
            "setGroupingsDown(reports.Dimension groupingsDown)\tvoid" : "setGroupingsDown($1)$0",
            "getAllData()\tBoolean" : "getAllData()$0",
            "getAttributes()\tMAP<String,String>" : "getAttributes()$0",
            "setGroupingsAcross(reports.Dimension groupingsAcross)\tvoid" : "setGroupingsAcross($1)$0",
            "setAllData(Boolean allData)\tvoid" : "setAllData($1)$0",
            "getFactMap()\tMAP<String,reports.ReportFact>" : "getFactMap()$0",
            "getReportMetadata()\treports.ReportMetadata" : "getReportMetadata()$0",
            "setAttributes(MAP<String,String> attributes)\tvoid" : "setAttributes($1)$0",
            "getReportExtendedMetadata()\treports.ReportExtendedMetadata" : "getReportExtendedMetadata()$0",
            "getHasDetailRows()\tBoolean" : "getHasDetailRows()$0",
            "setHasDetailRows(Boolean hasDetailRows)\tvoid" : "setHasDetailRows($1)$0",
            "getGroupingsDown()\treports.Dimension" : "getGroupingsDown()$0",
            "getGroupingsAcross()\treports.Dimension" : "getGroupingsAcross()$0"
        }
    },
    "binaryinput" : {
        "constructors" : {},
        "name" : "BinaryInput",
        "properties" : {},
        "methods" : {
            "getBlobValue()\tBlob" : "getBlobValue()$0",
            "getContentType()\tString" : "getContentType()$0",
            "toString()\tString" : "toString()$0",
            "getFilename()\tString" : "getFilename()$0"
        }
    },
    "displaytype" : {
        "constructors" : {},
        "name" : "DisplayType",
        "properties" : {
            "COMPLEXVALUE" : "COMPLEXVALUE$0",
            "ANYTYPE" : "ANYTYPE$0",
            "ID" : "ID$0",
            "BOOLEAN" : "BOOLEAN$0",
            "CURRENCY" : "CURRENCY$0",
            "TIME" : "TIME$0",
            "INTEGER" : "INTEGER$0",
            "LOCATION" : "LOCATION$0",
            "URL" : "URL$0",
            "PICKLIST" : "PICKLIST$0",
            "MULTIPICKLIST" : "MULTIPICKLIST$0",
            "ENCRYPTEDSTRING" : "ENCRYPTEDSTRING$0",
            "DATACATEGORYGROUPREFERENCE" : "DATACATEGORYGROUPREFERENCE$0",
            "TEXTAREA" : "TEXTAREA$0",
            "STRING" : "STRING$0",
            "DATE" : "DATE$0",
            "EMAIL" : "EMAIL$0",
            "PHONE" : "PHONE$0",
            "COMBOBOX" : "COMBOBOX$0",
            "BASE64" : "BASE64$0",
            "DOUBLE" : "DOUBLE$0",
            "DATETIME" : "DATETIME$0",
            "PERCENT" : "PERCENT$0",
            "REFERENCE" : "REFERENCE$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0",
            "values()\tLIST<Schema.DisplayType>" : "values()$0"
        }
    },
    "blob" : {
        "constructors" : {},
        "name" : "Blob",
        "properties" : {},
        "methods" : {
            "valueOf(String o)\tBlob" : "valueOf($1)$0",
            "size()\tInteger" : "size()$0",
            "toString()\tString" : "toString()$0",
            "toPdf(String o)\tBlob" : "toPdf($1)$0"
        }
    },
    "resetpasswordresult" : {
        "constructors" : {},
        "name" : "ResetPasswordResult",
        "properties" : {},
        "methods" : {
            "getPassword()\tString" : "getPassword()$0"
        }
    },
    "pluginrequest" : {
        "constructors" : {},
        "name" : "PluginRequest",
        "properties" : {
            "inputParameters" : "inputParameters$0"
        },
        "methods" : {}

    },
    "reportfact" : {
        "constructors" : {},
        "name" : "ReportFact",
        "properties" : {},
        "methods" : {
            "getAggregates()\tLIST<reports.SummaryValue>" : "getAggregates()$0",
            "setAggregates(LIST<reports.SummaryValue> aggregates)\tvoid" : "setAggregates($1)$0",
            "getKey()\tString" : "getKey()$0",
            "setKey(String key)\tvoid" : "setKey($1)$0"
        }
    },
    "pluginresult" : {
        "constructors" : {},
        "name" : "PluginResult",
        "properties" : {
            "outputParameters" : "outputParameters$0"
        },
        "methods" : {}

    },
    "reportcurrency" : {
        "constructors" : {},
        "name" : "ReportCurrency",
        "properties" : {},
        "methods" : {
            "getCurrencyCode()\tString" : "getCurrencyCode()$0",
            "setCurrencyCode(String currencyCode)\tvoid" : "setCurrencyCode($1)$0",
            "setAmount(Decimal amount)\tvoid" : "setAmount($1)$0",
            "getAmount()\tDecimal" : "getAmount()$0"
        }
    },
    "singleemailmessage" : {
        "constructors" : {},
        "name" : "SingleEmailMessage",
        "properties" : {},
        "methods" : {
            "getToAddresses()\tLIST<String>" : "getToAddresses()$0",
            "setHtmlBody(String param1)\tvoid" : "setHtmlBody($1)$0",
            "getEmailPriority()\tString" : "getEmailPriority()$0",
            "setReplyTo(String param1)\tvoid" : "setReplyTo($1)$0",
            "getFileAttachments()\tLIST<Messaging.EmailFileAttachment>" : "getFileAttachments()$0",
            "setDocumentAttachments(LIST<String> param1)\tvoid" : "setDocumentAttachments($1)$0",
            "setCcAddresses(LIST<String> param1)\tvoid" : "setCcAddresses($1)$0",
            "getTargetObjectId()\tId" : "getTargetObjectId()$0",
            "getPlainTextBody()\tString" : "getPlainTextBody()$0",
            "getSaveAsActivity()\tBoolean" : "getSaveAsActivity()$0",
            "getReferences()\tString" : "getReferences()$0",
            "setSaveAsActivity(Boolean param1)\tvoid" : "setSaveAsActivity($1)$0",
            "getBccSender()\tBoolean" : "getBccSender()$0",
            "setUseSignature(Boolean param1)\tvoid" : "setUseSignature($1)$0",
            "setPlainTextBody(String param1)\tvoid" : "setPlainTextBody($1)$0",
            "getSenderDisplayName()\tString" : "getSenderDisplayName()$0",
            "setWhatId(Id param1)\tvoid" : "setWhatId($1)$0",
            "isUserMail()\tBoolean" : "isUserMail()$0",
            "getSubject()\tString" : "getSubject()$0",
            "setSubject(String param1)\tvoid" : "setSubject($1)$0",
            "setBccSender(Boolean param1)\tvoid" : "setBccSender($1)$0",
            "setReferences(String param1)\tvoid" : "setReferences($1)$0",
            "getInReplyTo()\tString" : "getInReplyTo()$0",
            "setOrgWideEmailAddressId(Id param1)\tvoid" : "setOrgWideEmailAddressId($1)$0",
            "getUseSignature()\tBoolean" : "getUseSignature()$0",
            "getDocumentAttachments()\tLIST<String>" : "getDocumentAttachments()$0",
            "setBccAddresses(LIST<String> param1)\tvoid" : "setBccAddresses($1)$0",
            "setFileAttachments(LIST<Messaging.EmailFileAttachment> param1)\tvoid" : "setFileAttachments($1)$0",
            "getReplyTo()\tString" : "getReplyTo()$0",
            "setCharset(String param1)\tvoid" : "setCharset($1)$0",
            "getTemplateId()\tId" : "getTemplateId()$0",
            "setTargetObjectId(Id param1)\tvoid" : "setTargetObjectId($1)$0",
            "getCcAddresses()\tLIST<String>" : "getCcAddresses()$0",
            "getCharset()\tString" : "getCharset()$0",
            "setTemplateId(Id param1)\tvoid" : "setTemplateId($1)$0",
            "getHtmlBody()\tString" : "getHtmlBody()$0",
            "setSenderDisplayName(String param1)\tvoid" : "setSenderDisplayName($1)$0",
            "setEmailPriority(String param1)\tvoid" : "setEmailPriority($1)$0",
            "setToAddresses(LIST<String> param1)\tvoid" : "setToAddresses($1)$0",
            "getBccAddresses()\tLIST<String>" : "getBccAddresses()$0",
            "getOrgWideEmailAddressId()\tId" : "getOrgWideEmailAddressId()$0",
            "setInReplyTo(String param1)\tvoid" : "setInReplyTo($1)$0",
            "getWhatId()\tId" : "getWhatId()$0"
        }
    },
    "reportmetadata" : {
        "constructors" : {},
        "name" : "ReportMetadata",
        "properties" : {},
        "methods" : {
            "setDeveloperName(String developerName)\tvoid" : "setDeveloperName($1)$0",
            "setGroupingsAcross(LIST<reports.GroupingInfo> groupingsAcross)\tvoid" : "setGroupingsAcross($1)$0",
            "setCurrencyCode(String currencyCode)\tvoid" : "setCurrencyCode($1)$0",
            "getCurrencyCode()\tString" : "getCurrencyCode()$0",
            "getId()\tId" : "getId()$0",
            "setGroupingsDown(LIST<reports.GroupingInfo> groupingsDown)\tvoid" : "setGroupingsDown($1)$0",
            "getReportType()\treports.ReportType" : "getReportType()$0",
            "setName(String name)\tvoid" : "setName($1)$0",
            "getName()\tString" : "getName()$0",
            "getDeveloperName()\tString" : "getDeveloperName()$0",
            "setAggregates(LIST<String> aggregates)\tvoid" : "setAggregates($1)$0",
            "getReportFilters()\tLIST<reports.ReportFilter>" : "getReportFilters()$0",
            "setDetailColumns(LIST<String> detailColumns)\tvoid" : "setDetailColumns($1)$0",
            "getGroupingsDown()\tLIST<reports.GroupingInfo>" : "getGroupingsDown()$0",
            "setReportBooleanFilter(String reportBooleanFilter)\tvoid" : "setReportBooleanFilter($1)$0",
            "getReportFormat()\treports.ReportFormat" : "getReportFormat()$0",
            "setReportType(reports.ReportType reportType)\tvoid" : "setReportType($1)$0",
            "getReportBooleanFilter()\tString" : "getReportBooleanFilter()$0",
            "setReportFormat(String value)\tvoid" : "setReportFormat($1)$0",
            "getGroupingsAcross()\tLIST<reports.GroupingInfo>" : "getGroupingsAcross()$0",
            "setReportFormat(reports.ReportFormat reportFormat)\tvoid" : "setReportFormat($1)$0",
            "setId(Id id)\tvoid" : "setId($1)$0",
            "setReportFilters(LIST<reports.ReportFilter> reportFilters)\tvoid" : "setReportFilters($1)$0",
            "getAggregates()\tLIST<String>" : "getAggregates()$0",
            "getDetailColumns()\tLIST<String>" : "getDetailColumns()$0"
        }
    },
    "reportchartcomponent" : {
        "constructors" : {},
        "name" : "ReportChartComponent",
        "properties" : {},
        "methods" : {
            "getIncludeContext()\tBoolean" : "getIncludeContext()$0",
            "getSize()\tString" : "getSize()$0",
            "getShowTitle()\tBoolean" : "getShowTitle()$0",
            "getCacheData()\tBoolean" : "getCacheData()$0",
            "getContextFilterableField()\tString" : "getContextFilterableField()$0",
            "getHideOnError()\tBoolean" : "getHideOnError()$0"
        }
    },
    "columndatatype" : {
        "constructors" : {},
        "name" : "ColumnDataType",
        "properties" : {
            "COMBOBOX_DATA" : "COMBOBOX_DATA$0",
            "BOOLEAN_DATA" : "BOOLEAN_DATA$0",
            "STRING_DATA" : "STRING_DATA$0",
            "EMAIL_DATA" : "EMAIL_DATA$0",
            "REFERENCE_DATA" : "REFERENCE_DATA$0",
            "DATE_DATA" : "DATE_DATA$0",
            "TIME_DATA" : "TIME_DATA$0",
            "DOUBLE_DATA" : "DOUBLE_DATA$0",
            "URL_DATA" : "URL_DATA$0",
            "PICKLIST_DATA" : "PICKLIST_DATA$0",
            "PHONE_DATA" : "PHONE_DATA$0",
            "MULTIPICKLIST_DATA" : "MULTIPICKLIST_DATA$0",
            "PERCENT_DATA" : "PERCENT_DATA$0",
            "CURRENCY_DATA" : "CURRENCY_DATA$0",
            "TEXTAREA_DATA" : "TEXTAREA_DATA$0",
            "DATETIME_DATA" : "DATETIME_DATA$0",
            "INT_DATA" : "INT_DATA$0",
            "ID_DATA" : "ID_DATA$0"
        },
        "methods" : {
            "values()\tLIST<reports.ColumnDataType>" : "values()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "math" : {
        "constructors" : {},
        "name" : "Math",
        "properties" : {},
        "methods" : {
            "abs(Double x)\tDouble" : "abs($1)$0",
            "log10(Double x)\tDouble" : "log10($1)$0",
            "min(Integer x, Integer y)\tInteger" : "min($1)$0",
            "sqrt(Decimal x)\tDecimal" : "sqrt($1)$0",
            "sin(Decimal x)\tDecimal" : "sin($1)$0",
            "roundToLong(Decimal x)\tLong" : "roundToLong($1)$0",
            "cosh(Decimal x)\tDecimal" : "cosh($1)$0",
            "abs(Integer x)\tInteger" : "abs($1)$0",
            "log10(Decimal x)\tDecimal" : "log10($1)$0",
            "pow(Double base, Double exp)\tDouble" : "pow($1)$0",
            "round(Double x)\tInteger" : "round($1)$0",
            "sin(Double x)\tDouble" : "sin($1)$0",
            "max(Double x, Double y)\tDouble" : "max($1)$0",
            "cbrt(Double x)\tDouble" : "cbrt($1)$0",
            "cos(Decimal x)\tDecimal" : "cos($1)$0",
            "sinh(Double x)\tDouble" : "sinh($1)$0",
            "exp(Double x)\tDouble" : "exp($1)$0",
            "log(Decimal x)\tDecimal" : "log($1)$0",
            "mod(Long x, Long y)\tLong" : "mod($1)$0",
            "abs(Decimal x)\tDecimal" : "abs($1)$0",
            "min(Double x, Double y)\tDouble" : "min($1)$0",
            "mod(Integer x, Integer y)\tInteger" : "mod($1)$0",
            "cos(Double x)\tDouble" : "cos($1)$0",
            "atan2(Double x, Double y)\tDouble" : "atan2($1)$0",
            "atan2(Decimal x, Decimal y)\tDecimal" : "atan2($1)$0",
            "log(Double x)\tDouble" : "log($1)$0",
            "rint(Double x)\tDouble" : "rint($1)$0",
            "max(Integer x, Integer y)\tInteger" : "max($1)$0",
            "signum(Double x)\tDouble" : "signum($1)$0",
            "tanh(Decimal x)\tDecimal" : "tanh($1)$0",
            "roundToLong(Double x)\tLong" : "roundToLong($1)$0",
            "max(Long x, Long y)\tLong" : "max($1)$0",
            "tan(Double x)\tDouble" : "tan($1)$0",
            "asin(Decimal x)\tDecimal" : "asin($1)$0",
            "min(Decimal x, Decimal y)\tDecimal" : "min($1)$0",
            "random()\tDouble" : "random()$0",
            "acos(Double x)\tDouble" : "acos($1)$0",
            "sinh(Decimal x)\tDecimal" : "sinh($1)$0",
            "tan(Decimal x)\tDecimal" : "tan($1)$0",
            "cosh(Double x)\tDouble" : "cosh($1)$0",
            "acos(Decimal x)\tDecimal" : "acos($1)$0",
            "ceil(Decimal x)\tDecimal" : "ceil($1)$0",
            "atan(Decimal x)\tDecimal" : "atan($1)$0",
            "exp(Decimal x)\tDecimal" : "exp($1)$0",
            "floor(Decimal x)\tDecimal" : "floor($1)$0",
            "abs(Long x)\tLong" : "abs($1)$0",
            "round(Decimal x)\tInteger" : "round($1)$0",
            "floor(Double x)\tDouble" : "floor($1)$0",
            "atan(Double x)\tDouble" : "atan($1)$0",
            "signum(Decimal x)\tDecimal" : "signum($1)$0",
            "tanh(Double x)\tDouble" : "tanh($1)$0",
            "asin(Double x)\tDouble" : "asin($1)$0",
            "cbrt(Decimal x)\tDecimal" : "cbrt($1)$0",
            "min(Long x, Long y)\tLong" : "min($1)$0",
            "rint(Decimal x)\tDecimal" : "rint($1)$0",
            "max(Decimal x, Decimal y)\tDecimal" : "max($1)$0",
            "sqrt(Double x)\tDouble" : "sqrt($1)$0",
            "ceil(Double x)\tDouble" : "ceil($1)$0"
        }
    },
    "topicsuggestion" : {
        "constructors" : {},
        "name" : "TopicSuggestion",
        "properties" : {
            "existingTopic" : "existingTopic$0",
            "name" : "name$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "reporttypecolumn" : {
        "constructors" : {},
        "name" : "ReportTypeColumn",
        "properties" : {},
        "methods" : {
            "setDataType(reports.ColumnDataType dataType)\tvoid" : "setDataType($1)$0",
            "setName(String name)\tvoid" : "setName($1)$0",
            "getLabel()\tString" : "getLabel()$0",
            "getFilterValues()\tLIST<reports.FilterValue>" : "getFilterValues()$0",
            "setLabel(String label)\tvoid" : "setLabel($1)$0",
            "setFilterable(Boolean filterable)\tvoid" : "setFilterable($1)$0",
            "getDataType()\treports.ColumnDataType" : "getDataType()$0",
            "getFilterable()\tBoolean" : "getFilterable()$0",
            "setDataType(String value)\tvoid" : "setDataType($1)$0",
            "setFilterValues(LIST<reports.FilterValue> filterValues)\tvoid" : "setFilterValues($1)$0",
            "getName()\tString" : "getName()$0"
        }
    },
    "phonenumber" : {
        "constructors" : {},
        "name" : "PhoneNumber",
        "properties" : {
            "type" : "type$0",
            "phoneNumber" : "phoneNumber$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "httprequest" : {
        "constructors" : {},
        "name" : "HttpRequest",
        "properties" : {},
        "methods" : {
            "getCompressed()\tBoolean" : "getCompressed()$0",
            "getBodyAsBlob()\tBlob" : "getBodyAsBlob()$0",
            "getBody()\tString" : "getBody()$0",
            "setTimeout(Integer timeout)\tvoid" : "setTimeout($1)$0",
            "getEndpoint()\tString" : "getEndpoint()$0",
            "toString()\tString" : "toString()$0",
            "setBodyDocument(ANY body)\tvoid" : "setBodyDocument($1)$0",
            "setBodyAsBlob(Blob body)\tvoid" : "setBodyAsBlob($1)$0",
            "setEndpoint(String endpoint)\tvoid" : "setEndpoint($1)$0",
            "setClientCertificate(String clientCert, String password)\tvoid" : "setClientCertificate($1)$0",
            "getBodyDocument()\tdom.Document" : "getBodyDocument()$0",
            "setHeader(String key, String value)\tvoid" : "setHeader($1)$0",
            "getMethod()\tString" : "getMethod()$0",
            "setClientCertificateName(String certDevName)\tvoid" : "setClientCertificateName($1)$0",
            "setCompressed(Boolean compressed)\tvoid" : "setCompressed($1)$0",
            "setBody(String body)\tvoid" : "setBody($1)$0",
            "getHeader(String key)\tString" : "getHeader($1)$0",
            "setMethod(String method)\tvoid" : "setMethod($1)$0"
        }
    },
    "describequickactionresult" : {
        "constructors" : {},
        "name" : "DescribeQuickActionResult",
        "properties" : {},
        "methods" : {
            "getTargetParentField()\tString" : "getTargetParentField()$0",
            "getDefaultValues()\tLIST<QuickAction.DescribeQuickActionDefaultValue>" : "getDefaultValues()$0",
            "getColors()\tLIST<Schema.DescribeColorResult>" : "getColors()$0",
            "getHeight()\tInteger" : "getHeight()$0",
            "getCanvasApplicationName()\tString" : "getCanvasApplicationName()$0",
            "getIcons()\tLIST<Schema.DescribeIconResult>" : "getIcons()$0",
            "getWidth()\tInteger" : "getWidth()$0",
            "getSourceSobjectType()\tString" : "getSourceSobjectType()$0",
            "getIconUrl()\tString" : "getIconUrl()$0",
            "getTargetSobjectType()\tString" : "getTargetSobjectType()$0",
            "getVisualforcePageName()\tString" : "getVisualforcePageName()$0",
            "getTargetRecordTypeId()\tString" : "getTargetRecordTypeId()$0",
            "getIconName()\tString" : "getIconName()$0",
            "getLayout()\tQuickAction.DescribeLayoutSection" : "getLayout()$0",
            "getMiniIconUrl()\tString" : "getMiniIconUrl()$0"
        }
    },
    "sparkplugparameter" : {
        "constructors" : {},
        "name" : "SparkPlugParameter",
        "properties" : {
            "required" : "required$0",
            "parameterType" : "parameterType$0",
            "name" : "name$0"
        },
        "methods" : {}

    },
    "logginglevel" : {
        "constructors" : {},
        "name" : "LoggingLevel",
        "properties" : {
            "INTERNAL" : "INTERNAL$0",
            "DEBUG" : "DEBUG$0",
            "FINER" : "FINER$0",
            "FINE" : "FINE$0",
            "FINEST" : "FINEST$0",
            "INFO" : "INFO$0",
            "ERROR" : "ERROR$0",
            "WARN" : "WARN$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0",
            "values()\tLIST<system.LoggingLevel>" : "values()$0"
        }
    },
    "textsegment" : {
        "constructors" : {},
        "name" : "TextSegment",
        "properties" : {},
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "recordtypeinfo" : {
        "constructors" : {},
        "name" : "RecordTypeInfo",
        "properties" : {},
        "methods" : {
            "getRecordTypeId()\tId" : "getRecordTypeId()$0",
            "isDefaultRecordTypeMapping()\tBoolean" : "isDefaultRecordTypeMapping()$0",
            "getName()\tString" : "getName()$0",
            "isAvailable()\tBoolean" : "isAvailable()$0"
        }
    },
    "emailheader" : {
        "constructors" : {},
        "name" : "EmailHeader",
        "properties" : {
            "TriggerUserEmail" : "TriggerUserEmail$0",
            "TriggerAutoResponseEmail" : "TriggerAutoResponseEmail$0",
            "TriggerOtherEmail" : "TriggerOtherEmail$0"
        },
        "methods" : {}

    },
    "assignmentruleheader" : {
        "constructors" : {},
        "name" : "AssignmentRuleHeader",
        "properties" : {
            "UseDefaultRule" : "UseDefaultRule$0",
            "AssignmentRuleId" : "AssignmentRuleId$0"
        },
        "methods" : {}

    },
    "recordviewsection" : {
        "constructors" : {},
        "name" : "RecordViewSection",
        "properties" : {
            "isCollapsible" : "isCollapsible$0",
            "fields" : "fields$0",
            "columnCount" : "columnCount$0",
            "heading" : "heading$0",
            "columnOrder" : "columnOrder$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "mergerequest" : {
        "constructors" : {},
        "name" : "MergeRequest",
        "properties" : {},
        "methods" : {
            "setRecordToMergeIds(LIST<String> param1)\tvoid" : "setRecordToMergeIds($1)$0",
            "getRecordToMergeIds()\tLIST<String>" : "getRecordToMergeIds()$0",
            "getMasterRecord()\tSObject" : "getMasterRecord()$0",
            "setMasterRecord(SObject param1)\tvoid" : "setMasterRecord($1)$0"
        }
    },
    "date" : {
        "constructors" : {},
        "name" : "Date",
        "properties" : {},
        "methods" : {
            "month()\tInteger" : "month()$0",
            "isLeapYear(Integer year)\tBoolean" : "isLeapYear($1)$0",
            "parse(String str)\tDate" : "parse($1)$0",
            "addYears(Integer years)\tDate" : "addYears($1)$0",
            "addError(APEX_OBJECT msg)\tvoid" : "addError($1)$0",
            "valueOf(Object o)\tDate" : "valueOf($1)$0",
            "daysBetween(Date other)\tInteger" : "daysBetween($1)$0",
            "addError(String msg)\tvoid" : "addError($1)$0",
            "year()\tInteger" : "year()$0",
            "day()\tInteger" : "day()$0",
            "format()\tString" : "format()$0",
            "monthsBetween(Date other)\tInteger" : "monthsBetween($1)$0",
            "today()\tDate" : "today()$0",
            "valueOf(String str)\tDate" : "valueOf($1)$0",
            "dayOfYear()\tInteger" : "dayOfYear()$0",
            "toStartOfWeek()\tDate" : "toStartOfWeek()$0",
            "daysInMonth(Integer year, Integer month)\tInteger" : "daysInMonth($1)$0",
            "newInstance(Integer year, Integer month, Integer day)\tDate" : "newInstance($1)$0",
            "addError(String msg, Boolean escape)\tvoid" : "addError($1)$0",
            "toStartOfMonth()\tDate" : "toStartOfMonth()$0",
            "addMonths(Integer months)\tDate" : "addMonths($1)$0",
            "addError(APEX_OBJECT msg, Boolean escape)\tvoid" : "addError($1)$0",
            "addDays(Integer days)\tDate" : "addDays($1)$0",
            "isSameDay(Date other)\tBoolean" : "isSameDay($1)$0"
        }
    },
    "stack" : {
        "constructors" : {},
        "name" : "Stack",
        "properties" : {},
        "methods" : {
            "peek()\tString" : "peek()$0",
            "empty()\tBoolean" : "empty()$0",
            "push(String item)\tvoid" : "push($1)$0",
            "pop()\tString" : "pop()$0"
        }
    },
    "userprofiletabtype" : {
        "constructors" : {},
        "name" : "UserProfileTabType",
        "properties" : {
            "Feed" : "Feed$0",
            "Overview" : "Overview$0",
            "CustomWeb" : "CustomWeb$0",
            "CustomVisualForce" : "CustomVisualForce$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<ConnectApi.UserProfileTabType>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "feedbody" : {
        "constructors" : {},
        "name" : "FeedBody",
        "properties" : {},
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "querylocator" : {
        "constructors" : {},
        "name" : "QueryLocator",
        "properties" : {},
        "methods" : {
            "iterator()\tDatabase.QueryLocatorIterator" : "iterator()$0",
            "getQuery()\tString" : "getQuery()$0"
        }
    },
    "iterator" : {
        "constructors" : {},
        "name" : "Iterator",
        "properties" : {},
        "methods" : {
            "next()\tObject" : "next()$0",
            "hasNext()\tBoolean" : "hasNext()$0"
        }
    },
    "standardcontroller" : {
        "constructors" : {},
        "name" : "StandardController",
        "properties" : {},
        "methods" : {
            "getSubject()\tSObject" : "getSubject()$0",
            "delete()\tSystem.PageReference" : "delete()$0",
            "edit()\tSystem.PageReference" : "edit()$0",
            "reset()\tvoid" : "reset()$0",
            "getId()\tString" : "getId()$0",
            "save()\tSystem.PageReference" : "save()$0",
            "cancel()\tSystem.PageReference" : "cancel()$0",
            "getRecord()\tSObject" : "getRecord()$0",
            "view()\tSystem.PageReference" : "view()$0",
            "addFields(LIST<String> fieldNames)\tvoid" : "addFields($1)$0"
        }
    },
    "emptyrecyclebinresult" : {
        "constructors" : {},
        "name" : "EmptyRecycleBinResult",
        "properties" : {},
        "methods" : {
            "getErrors()\tLIST<Database.Error>" : "getErrors()$0",
            "isSuccess()\tBoolean" : "isSuccess()$0",
            "getId()\tId" : "getId()$0"
        }
    },
    "filesharingtype" : {
        "constructors" : {},
        "name" : "FileSharingType",
        "properties" : {
            "WorkspaceManaged" : "WorkspaceManaged$0",
            "Admin" : "Admin$0",
            "Owner" : "Owner$0",
            "Collaborator" : "Collaborator$0",
            "Viewer" : "Viewer$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<ConnectApi.FileSharingType>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "describetabresult" : {
        "constructors" : {},
        "name" : "DescribeTabResult",
        "properties" : {},
        "methods" : {
            "getIcons()\tLIST<Schema.DescribeIconResult>" : "getIcons()$0",
            "isCustom()\tBoolean" : "isCustom()$0",
            "getColors()\tLIST<Schema.DescribeColorResult>" : "getColors()$0",
            "getSobjectName()\tString" : "getSobjectName()$0",
            "getLabel()\tString" : "getLabel()$0",
            "getUrl()\tString" : "getUrl()$0",
            "getIconUrl()\tString" : "getIconUrl()$0",
            "getMiniIconUrl()\tString" : "getMiniIconUrl()$0"
        }
    },
    "fieldset" : {
        "constructors" : {},
        "name" : "FieldSet",
        "properties" : {},
        "methods" : {
            "getName()\tString" : "getName()$0",
            "getFields()\tLIST<Schema.FieldSetMember>" : "getFields()$0",
            "getDescription()\tString" : "getDescription()$0",
            "getNameSpace()\tString" : "getNameSpace()$0",
            "getSObjectType()\tSchema.SObjectType" : "getSObjectType()$0",
            "getLabel()\tString" : "getLabel()$0"
        }
    },
    "severity" : {
        "constructors" : {},
        "name" : "Severity",
        "properties" : {
            "FATAL" : "FATAL$0",
            "ERROR" : "ERROR$0",
            "WARNING" : "WARNING$0",
            "INFO" : "INFO$0",
            "CONFIRM" : "CONFIRM$0"
        },
        "methods" : {
            "values()\tLIST<ApexPages.Severity>" : "values()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "chattergroup" : {
        "constructors" : {},
        "name" : "ChatterGroup",
        "properties" : {
            "isArchived" : "isArchived$0",
            "emailToChatterAddress" : "emailToChatterAddress$0",
            "owner" : "owner$0",
            "photo" : "photo$0",
            "myRole" : "myRole$0",
            "community" : "community$0",
            "canHaveChatterGuests" : "canHaveChatterGuests$0",
            "memberCount" : "memberCount$0",
            "isAutoArchiveDisabled" : "isAutoArchiveDisabled$0",
            "lastFeedItemPostDate" : "lastFeedItemPostDate$0",
            "description" : "description$0",
            "visibility" : "visibility$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "reportfactwithsummaries" : {
        "constructors" : {},
        "name" : "ReportFactWithSummaries",
        "properties" : {},
        "methods" : {}

    },
    "test" : {
        "constructors" : {},
        "name" : "Test",
        "properties" : {},
        "methods" : {
            "invokePage(System.PageReference p)\tComponent.apex.page" : "invokePage($1)$0",
            "startTest()\tvoid" : "startTest()$0",
            "loadData(Schema.SObjectType sobjectType, String staticResourceName)\tLIST<SObject>" : "loadData($1)$0",
            "testUninstall(system.UninstallHandler script)\tvoid" : "testUninstall($1)$0",
            "isRunningTest()\tBoolean" : "isRunningTest()$0",
            "setMock(system.Type interfaceType, Object mock)\tvoid" : "setMock($1)$0",
            "setCurrentPageReference(Object pageReference)\tvoid" : "setCurrentPageReference($1)$0",
            "stopTest()\tvoid" : "stopTest()$0",
            "setFixedSearchResults(LIST<String> searchResultsIds)\tvoid" : "setFixedSearchResults($1)$0",
            "testInstall(system.InstallHandler script, system.Version version)\tvoid" : "testInstall($1)$0",
            "testInstall(system.InstallHandler script, system.Version version, Boolean isPush)\tvoid" : "testInstall($1)$0",
            "setReadOnlyApplicationMode(Boolean readOnlyApplicationMode)\tvoid" : "setReadOnlyApplicationMode($1)$0",
            "setCurrentPage(Object pageReference)\tvoid" : "setCurrentPage($1)$0"
        }
    },
    "describelayoutrow" : {
        "constructors" : {},
        "name" : "DescribeLayoutRow",
        "properties" : {},
        "methods" : {
            "getLayoutItems()\tLIST<QuickAction.DescribeLayoutItem>" : "getLayoutItems()$0",
            "getNumItems()\tInteger" : "getNumItems()$0"
        }
    },
    "id" : {
        "constructors" : {},
        "name" : "Id",
        "properties" : {},
        "methods" : {
            "addError(APEX_OBJECT msg, Boolean escape)\tvoid" : "addError($1)$0",
            "addError(String msg)\tvoid" : "addError($1)$0",
            "addError(String msg, Boolean escape)\tvoid" : "addError($1)$0",
            "addError(APEX_OBJECT msg)\tvoid" : "addError($1)$0",
            "valueOf(String str)\tId" : "valueOf($1)$0",
            "getSobjectType()\tSchema.SObjectType" : "getSobjectType()$0"
        }
    },
    "userinput" : {
        "constructors" : {},
        "name" : "UserInput",
        "properties" : {
            "aboutMe" : "aboutMe$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object" : "convertToJavaObject($1)$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "sparkplugdescriberesult" : {
        "constructors" : {},
        "name" : "SparkPlugDescribeResult",
        "properties" : {
            "outputParameters" : "outputParameters$0",
            "inputParameters" : "inputParameters$0",
            "name" : "name$0"
        },
        "methods" : {}

    },
    "groupinginfo" : {
        "constructors" : {},
        "name" : "GroupingInfo",
        "properties" : {},
        "methods" : {
            "setDateGranularity(reports.DateGranularity dateGranularity)\tvoid" : "setDateGranularity($1)$0",
            "getSortOrder()\treports.ColumnSortOrder" : "getSortOrder()$0",
            "setName(String name)\tvoid" : "setName($1)$0",
            "getName()\tString" : "getName()$0",
            "getDateGranularity()\treports.DateGranularity" : "getDateGranularity()$0",
            "setSortOrder(String value)\tvoid" : "setSortOrder($1)$0",
            "setSortOrder(reports.ColumnSortOrder sortOrder)\tvoid" : "setSortOrder($1)$0",
            "setDateGranularity(String value)\tvoid" : "setDateGranularity($1)$0"
        }
    },
    "mentionvalidation" : {
        "constructors" : {},
        "name" : "MentionValidation",
        "properties" : {
            "recordId" : "recordId$0",
            "validationStatus" : "validationStatus$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "groupmemberpage" : {
        "constructors" : {},
        "name" : "GroupMemberPage",
        "properties" : {
            "totalMemberCount" : "totalMemberCount$0",
            "previousPageUrl" : "previousPageUrl$0",
            "currentPageUrl" : "currentPageUrl$0",
            "nextPageUrl" : "nextPageUrl$0",
            "members" : "members$0",
            "myMembership" : "myMembership$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "emailattachment" : {
        "constructors" : {},
        "name" : "EmailAttachment",
        "properties" : {},
        "methods" : {
            "setFileName(String param1)\tvoid" : "setFileName($1)$0",
            "setContentType(String param1)\tvoid" : "setContentType($1)$0",
            "getBody()\tBlob" : "getBody()$0",
            "getContentType()\tString" : "getContentType()$0",
            "setBody(Blob param1)\tvoid" : "setBody($1)$0",
            "getFileName()\tString" : "getFileName()$0"
        }
    },
    "resourcelinksegment" : {
        "constructors" : {},
        "name" : "ResourceLinkSegment",
        "properties" : {
            "url" : "url$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "groupchattersettings" : {
        "constructors" : {},
        "name" : "GroupChatterSettings",
        "properties" : {
            "emailFrequency" : "emailFrequency$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "summaryvalue" : {
        "constructors" : {},
        "name" : "SummaryValue",
        "properties" : {},
        "methods" : {
            "getValue()\tObject" : "getValue()$0",
            "setValue(Object value)\tvoid" : "setValue($1)$0",
            "getLabel()\tString" : "getLabel()$0",
            "setLabel(String label)\tvoid" : "setLabel($1)$0"
        }
    },
    "licensingandprovisioning" : {
        "constructors" : {},
        "name" : "LicensingAndProvisioning",
        "properties" : {},
        "methods" : {
            "linkTenantAccount(String serviceProviderKey, String tenantExternalId, String accountId)\tvoid" : "linkTenantAccount($1)$0",
            "replaceTenantAccountLink(String serviceProviderKey, String oldTenantExternalId, String newTenantExternalId)\tvoid" : "replaceTenantAccountLink($1)$0"
        }
    },
    "sparkplugapi" : {
        "constructors" : {},
        "name" : "SparkPlugApi",
        "properties" : {},
        "methods" : {
            "describePlugins()\tLIST<Process.SparkPlugApi.SparkPlugDescribeResult>" : "describePlugins()$0",
            "invokePluginWithJson(String className, String parameters)\tString" : "invokePluginWithJson($1)$0",
            "describePlugin(String className)\tProcess.SparkPlugApi.SparkPlugDescribeResult" : "describePlugin($1)$0"
        }
    },
    "labeledrecordfield" : {
        "constructors" : {},
        "name" : "LabeledRecordField",
        "properties" : {
            "text" : "text$0",
            "label" : "label$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "long" : {
        "constructors" : {},
        "name" : "Long",
        "properties" : {},
        "methods" : {
            "addError(APEX_OBJECT msg, Boolean escape)\tvoid" : "addError($1)$0",
            "addError(String msg)\tvoid" : "addError($1)$0",
            "addError(String msg, Boolean escape)\tvoid" : "addError($1)$0",
            "addError(APEX_OBJECT msg)\tvoid" : "addError($1)$0",
            "format()\tString" : "format()$0",
            "valueOf(String str)\tLong" : "valueOf($1)$0",
            "intValue()\tInteger" : "intValue()$0"
        }
    },
    "connectapiexception" : {
        "constructors" : {},
        "name" : "ConnectApiException",
        "properties" : {},
        "methods" : {
            "getErrorCode()\tString" : "getErrorCode()$0",
            "getTypeName()\tString" : "getTypeName()$0"
        }
    },
    "statuscode" : {
        "constructors" : {},
        "name" : "StatusCode",
        "properties" : {
            "FIELD_FILTER_VALIDATION_EXCEPTION" : "FIELD_FILTER_VALIDATION_EXCEPTION$0",
            "INVALID_SIGNUP_COUNTRY" : "INVALID_SIGNUP_COUNTRY$0",
            "COLLISION_DETECTED" : "COLLISION_DETECTED$0",
            "INVALID_BATCH_OPERATION" : "INVALID_BATCH_OPERATION$0",
            "NO_ATTACHMENT_PERMISSION" : "NO_ATTACHMENT_PERMISSION$0",
            "DUPLICATE_USERNAME" : "DUPLICATE_USERNAME$0",
            "INVALID_FILTER_ACTION" : "INVALID_FILTER_ACTION$0",
            "MIXED_DML_OPERATION" : "MIXED_DML_OPERATION$0",
            "INVALID_READ_ONLY_USER_DML" : "INVALID_READ_ONLY_USER_DML$0",
            "NO_INACTIVE_DIVISION_MEMBERS" : "NO_INACTIVE_DIVISION_MEMBERS$0",
            "REQUEST_RUNNING_TOO_LONG" : "REQUEST_RUNNING_TOO_LONG$0",
            "STORAGE_LIMIT_EXCEEDED" : "STORAGE_LIMIT_EXCEEDED$0",
            "UNABLE_TO_LOCK_ROW" : "UNABLE_TO_LOCK_ROW$0",
            "CANNOT_DELETE_LAST_DATED_CONVERSION_RATE" : "CANNOT_DELETE_LAST_DATED_CONVERSION_RATE$0",
            "CUSTOM_FIELD_INDEX_LIMIT_EXCEEDED" : "CUSTOM_FIELD_INDEX_LIMIT_EXCEEDED$0",
            "DELETE_REQUIRED_ON_CASCADE" : "DELETE_REQUIRED_ON_CASCADE$0",
            "CANNOT_CHANGE_FIELD_TYPE_OF_APEX_REFERENCED_FIELD" : "CANNOT_CHANGE_FIELD_TYPE_OF_APEX_REFERENCED_FIELD$0",
            "CANNOT_RENAME_APEX_REFERENCED_OBJECT" : "CANNOT_RENAME_APEX_REFERENCED_OBJECT$0",
            "MAX_TM_RULE_ITEMS_EXCEEDED" : "MAX_TM_RULE_ITEMS_EXCEEDED$0",
            "STRING_TOO_LONG" : "STRING_TOO_LONG$0",
            "STANDARD_PRICE_NOT_DEFINED" : "STANDARD_PRICE_NOT_DEFINED$0",
            "INVALID_GOOGLE_DOCS_URL" : "INVALID_GOOGLE_DOCS_URL$0",
            "FIELD_CUSTOM_VALIDATION_EXCEPTION" : "FIELD_CUSTOM_VALIDATION_EXCEPTION$0",
            "USER_OWNS_PORTAL_ACCOUNT_EXCEPTION" : "USER_OWNS_PORTAL_ACCOUNT_EXCEPTION$0",
            "CANNOT_ENABLE_IP_RESTRICT_REQUESTS" : "CANNOT_ENABLE_IP_RESTRICT_REQUESTS$0",
            "TEMPLATE_NOT_FOUND" : "TEMPLATE_NOT_FOUND$0",
            "ASSIGNEE_TYPE_REQUIRED" : "ASSIGNEE_TYPE_REQUIRED$0",
            "NO_SUCH_USER_EXISTS" : "NO_SUCH_USER_EXISTS$0",
            "TRANSFER_REQUIRES_READ" : "TRANSFER_REQUIRES_READ$0",
            "DUPLICATE_CASE_SOLUTION" : "DUPLICATE_CASE_SOLUTION$0",
            "CANNOT_RENAME_REFERENCED_OBJECT" : "CANNOT_RENAME_REFERENCED_OBJECT$0",
            "CANNOT_INSERT_UPDATE_ACTIVATE_ENTITY" : "CANNOT_INSERT_UPDATE_ACTIVATE_ENTITY$0",
            "ALL_OR_NONE_OPERATION_ROLLED_BACK" : "ALL_OR_NONE_OPERATION_ROLLED_BACK$0",
            "INVALID_FIELD_WHEN_USING_TEMPLATE" : "INVALID_FIELD_WHEN_USING_TEMPLATE$0",
            "INVALID_SUBDOMAIN" : "INVALID_SUBDOMAIN$0",
            "DUPLICATE_CUSTOM_ENTITY_DEFINITION" : "DUPLICATE_CUSTOM_ENTITY_DEFINITION$0",
            "EMAIL_NOT_PROCESSED_DUE_TO_PRIOR_ERROR" : "EMAIL_NOT_PROCESSED_DUE_TO_PRIOR_ERROR$0",
            "INACTIVE_OWNER_OR_USER" : "INACTIVE_OWNER_OR_USER$0",
            "OP_WITH_INVALID_USER_TYPE_EXCEPTION" : "OP_WITH_INVALID_USER_TYPE_EXCEPTION$0",
            "COMMUNITY_NOT_ACCESSIBLE" : "COMMUNITY_NOT_ACCESSIBLE$0",
            "PACKAGING_API_INSTALL_FAILED" : "PACKAGING_API_INSTALL_FAILED$0",
            "DELETE_FAILED" : "DELETE_FAILED$0",
            "CANNOT_REPARENT_RECORD" : "CANNOT_REPARENT_RECORD$0",
            "INVALID_LINEITEM_CLONE_STATE" : "INVALID_LINEITEM_CLONE_STATE$0",
            "TOO_MANY_POSSIBLE_USERS_EXIST" : "TOO_MANY_POSSIBLE_USERS_EXIST$0",
            "MAXIMUM_DASHBOARD_COMPONENTS_EXCEEDED" : "MAXIMUM_DASHBOARD_COMPONENTS_EXCEEDED$0",
            "CANNOT_MODIFY_MANAGED_OBJECT" : "CANNOT_MODIFY_MANAGED_OBJECT$0",
            "INVALID_FIELD_FOR_INSERT_UPDATE" : "INVALID_FIELD_FOR_INSERT_UPDATE$0",
            "INVALID_PARTNER_NETWORK_STATUS" : "INVALID_PARTNER_NETWORK_STATUS$0",
            "RECORD_IN_USE_BY_WORKFLOW" : "RECORD_IN_USE_BY_WORKFLOW$0",
            "DUPLICATE_SENDER_DISPLAY_NAME" : "DUPLICATE_SENDER_DISPLAY_NAME$0",
            "UNDELETE_FAILED" : "UNDELETE_FAILED$0",
            "HTML_FILE_UPLOAD_NOT_ALLOWED" : "HTML_FILE_UPLOAD_NOT_ALLOWED$0",
            "INVALID_DATA_CATEGORY_GROUP_REFERENCE" : "INVALID_DATA_CATEGORY_GROUP_REFERENCE$0",
            "CHILD_SHARE_FAILS_PARENT" : "CHILD_SHARE_FAILS_PARENT$0",
            "INVALID_CURRENCY_ISO" : "INVALID_CURRENCY_ISO$0",
            "DUPLICATE_COMM_NICKNAME" : "DUPLICATE_COMM_NICKNAME$0",
            "MAX_ACTIVE_RULES_EXCEEDED" : "MAX_ACTIVE_RULES_EXCEEDED$0",
            "UNKNOWN_EXCEPTION" : "UNKNOWN_EXCEPTION$0",
            "INVALID_CROSS_REFERENCE_KEY" : "INVALID_CROSS_REFERENCE_KEY$0",
            "INVALID_CURRENCY_CORP_RATE" : "INVALID_CURRENCY_CORP_RATE$0",
            "INVALID_SETUP_OWNER" : "INVALID_SETUP_OWNER$0",
            "MAXIMUM_HIERARCHY_LEVELS_REACHED" : "MAXIMUM_HIERARCHY_LEVELS_REACHED$0",
            "INVALID_TYPE" : "INVALID_TYPE$0",
            "USER_WITH_APEX_SHARES_EXCEPTION" : "USER_WITH_APEX_SHARES_EXCEPTION$0",
            "INVALID_QUERY_LOCATOR" : "INVALID_QUERY_LOCATOR$0",
            "UNSPECIFIED_EMAIL_ADDRESS" : "UNSPECIFIED_EMAIL_ADDRESS$0",
            "INVALID_ASSIGNMENT_RULE" : "INVALID_ASSIGNMENT_RULE$0",
            "SUBDOMAIN_IN_USE" : "SUBDOMAIN_IN_USE$0",
            "MAX_RULE_ENTRIES_EXCEEDED" : "MAX_RULE_ENTRIES_EXCEEDED$0",
            "ENTITY_IS_LOCKED" : "ENTITY_IS_LOCKED$0",
            "ENTITY_IS_ARCHIVED" : "ENTITY_IS_ARCHIVED$0",
            "INVALID_CROSS_REFERENCE_TYPE_FOR_FIELD" : "INVALID_CROSS_REFERENCE_TYPE_FOR_FIELD$0",
            "INVALID_STATUS" : "INVALID_STATUS$0",
            "MANAGER_NOT_DEFINED" : "MANAGER_NOT_DEFINED$0",
            "SINGLE_EMAIL_LIMIT_EXCEEDED" : "SINGLE_EMAIL_LIMIT_EXCEEDED$0",
            "UNSUPPORTED_APEX_TRIGGER_OPERATON" : "UNSUPPORTED_APEX_TRIGGER_OPERATON$0",
            "UNAVAILABLE_RECORDTYPE_EXCEPTION" : "UNAVAILABLE_RECORDTYPE_EXCEPTION$0",
            "FAILED_ACTIVATION" : "FAILED_ACTIVATION$0",
            "TABSET_LIMIT_EXCEEDED" : "TABSET_LIMIT_EXCEEDED$0",
            "ALREADY_IN_PROCESS" : "ALREADY_IN_PROCESS$0",
            "MISSING_ARGUMENT" : "MISSING_ARGUMENT$0",
            "MALFORMED_ID" : "MALFORMED_ID$0",
            "INVALID_FIELD" : "INVALID_FIELD$0",
            "MAX_ACTIONS_PER_RULE_EXCEEDED" : "MAX_ACTIONS_PER_RULE_EXCEEDED$0",
            "FIELD_INTEGRITY_EXCEPTION" : "FIELD_INTEGRITY_EXCEPTION$0",
            "INVALID_SESSION_ID" : "INVALID_SESSION_ID$0",
            "SHARE_NEEDED_FOR_CHILD_OWNER" : "SHARE_NEEDED_FOR_CHILD_OWNER$0",
            "WEBLINK_SIZE_LIMIT_EXCEEDED" : "WEBLINK_SIZE_LIMIT_EXCEEDED$0",
            "NO_APPLICABLE_PROCESS" : "NO_APPLICABLE_PROCESS$0",
            "INVALID_MESSAGE_ID_REFERENCE" : "INVALID_MESSAGE_ID_REFERENCE$0",
            "CANNOT_FREEZE_SELF" : "CANNOT_FREEZE_SELF$0",
            "WEBLINK_URL_INVALID" : "WEBLINK_URL_INVALID$0",
            "TEXT_DATA_OUTSIDE_SUPPORTED_CHARSET" : "TEXT_DATA_OUTSIDE_SUPPORTED_CHARSET$0",
            "INVALID_DATA_URI" : "INVALID_DATA_URI$0",
            "INVALID_TYPE_FOR_OPERATION" : "INVALID_TYPE_FOR_OPERATION$0",
            "CUSTOM_TAB_LIMIT_EXCEEDED" : "CUSTOM_TAB_LIMIT_EXCEEDED$0",
            "CANNOT_CREATE_ANOTHER_MANAGED_PACKAGE" : "CANNOT_CREATE_ANOTHER_MANAGED_PACKAGE$0",
            "INVALID_PACKAGE_VERSION" : "INVALID_PACKAGE_VERSION$0",
            "SELF_REFERENCE_FROM_TRIGGER" : "SELF_REFERENCE_FROM_TRIGGER$0",
            "INVALID_OPERATOR" : "INVALID_OPERATOR$0",
            "ENVIRONMENT_HUB_MEMBERSHIP_USER_ALREADY_IN_HUB" : "ENVIRONMENT_HUB_MEMBERSHIP_USER_ALREADY_IN_HUB$0",
            "DELETE_OPERATION_TOO_LARGE" : "DELETE_OPERATION_TOO_LARGE$0",
            "INVALID_CURRENCY_CONV_RATE" : "INVALID_CURRENCY_CONV_RATE$0",
            "CANNOT_EXECUTE_FLOW_TRIGGER" : "CANNOT_EXECUTE_FLOW_TRIGGER$0",
            "PORTAL_NO_ACCESS" : "PORTAL_NO_ACCESS$0",
            "INVALID_EMAIL_ADDRESS" : "INVALID_EMAIL_ADDRESS$0",
            "INVALID_OPERATION" : "INVALID_OPERATION$0",
            "LIMIT_EXCEEDED" : "LIMIT_EXCEEDED$0",
            "PACKAGE_LICENSE_REQUIRED" : "PACKAGE_LICENSE_REQUIRED$0",
            "INVALID_OR_NULL_FOR_RESTRICTED_PICKLIST" : "INVALID_OR_NULL_FOR_RESTRICTED_PICKLIST$0",
            "REQUIRED_FEATURE_MISSING" : "REQUIRED_FEATURE_MISSING$0",
            "INVALID_CREDIT_CARD_INFO" : "INVALID_CREDIT_CARD_INFO$0",
            "NUMBER_OUTSIDE_VALID_RANGE" : "NUMBER_OUTSIDE_VALID_RANGE$0",
            "BCC_NOT_ALLOWED_IF_BCC_COMPLIANCE_ENABLED" : "BCC_NOT_ALLOWED_IF_BCC_COMPLIANCE_ENABLED$0",
            "CANT_DISABLE_CORP_CURRENCY" : "CANT_DISABLE_CORP_CURRENCY$0",
            "MAX_FORMULAS_PER_RULE_EXCEEDED" : "MAX_FORMULAS_PER_RULE_EXCEEDED$0",
            "ENVIRONMENT_HUB_MEMBERSHIP_CONFLICT" : "ENVIRONMENT_HUB_MEMBERSHIP_CONFLICT$0",
            "INVALID_ID_FIELD" : "INVALID_ID_FIELD$0",
            "INSUFFICIENT_ACCESS_OR_READONLY" : "INSUFFICIENT_ACCESS_OR_READONLY$0",
            "MAX_TASK_DESCRIPTION_EXCEEEDED" : "MAX_TASK_DESCRIPTION_EXCEEEDED$0",
            "DEPENDENCY_EXISTS" : "DEPENDENCY_EXISTS$0",
            "MAXIMUM_CCEMAILS_EXCEEDED" : "MAXIMUM_CCEMAILS_EXCEEDED$0",
            "CANNOT_CASCADE_PRODUCT_ACTIVE" : "CANNOT_CASCADE_PRODUCT_ACTIVE$0",
            "DUPLICATE_VALUE" : "DUPLICATE_VALUE$0",
            "INVALID_CONTENT_TYPE" : "INVALID_CONTENT_TYPE$0",
            "UNVERIFIED_SENDER_ADDRESS" : "UNVERIFIED_SENDER_ADDRESS$0",
            "MAXIMUM_SIZE_OF_DOCUMENT" : "MAXIMUM_SIZE_OF_DOCUMENT$0",
            "CIRCULAR_DEPENDENCY" : "CIRCULAR_DEPENDENCY$0",
            "ENVIRONMENT_HUB_MEMBERSHIP_USER_NOT_ORG_ADMIN" : "ENVIRONMENT_HUB_MEMBERSHIP_USER_NOT_ORG_ADMIN$0",
            "ENTITY_IS_DELETED" : "ENTITY_IS_DELETED$0",
            "IP_RANGE_LIMIT_EXCEEDED" : "IP_RANGE_LIMIT_EXCEEDED$0",
            "CANNOT_PASSWORD_LOCKOUT" : "CANNOT_PASSWORD_LOCKOUT$0",
            "INVALID_PERSON_ACCOUNT_OPERATION" : "INVALID_PERSON_ACCOUNT_OPERATION$0",
            "FILTERED_LOOKUP_LIMIT_EXCEEDED" : "FILTERED_LOOKUP_LIMIT_EXCEEDED$0",
            "CANT_UNSET_CORP_CURRENCY" : "CANT_UNSET_CORP_CURRENCY$0",
            "INVALID_SAVE_AS_ACTIVITY_FLAG" : "INVALID_SAVE_AS_ACTIVITY_FLAG$0",
            "REQUIRED_FIELD_MISSING" : "REQUIRED_FIELD_MISSING$0",
            "NUM_HISTORY_FIELDS_BY_SOBJECT_EXCEEDED" : "NUM_HISTORY_FIELDS_BY_SOBJECT_EXCEEDED$0",
            "SELF_REFERENCE_FROM_FLOW" : "SELF_REFERENCE_FROM_FLOW$0",
            "DUPLICATE_MASTER_LABEL" : "DUPLICATE_MASTER_LABEL$0",
            "DUPLICATE_EXTERNAL_ID" : "DUPLICATE_EXTERNAL_ID$0",
            "INVALID_OAUTH_URL" : "INVALID_OAUTH_URL$0",
            "ENVIRONMENT_HUB_MEMBERSHIP_ERROR_JOINING_HUB" : "ENVIRONMENT_HUB_MEMBERSHIP_ERROR_JOINING_HUB$0",
            "CUSTOM_CLOB_FIELD_LIMIT_EXCEEDED" : "CUSTOM_CLOB_FIELD_LIMIT_EXCEEDED$0",
            "ENTITY_FAILED_IFLASTMODIFIED_ON_UPDATE" : "ENTITY_FAILED_IFLASTMODIFIED_ON_UPDATE$0",
            "CUSTOM_APEX_ERROR" : "CUSTOM_APEX_ERROR$0",
            "EMPTY_SCONTROL_FILE_NAME" : "EMPTY_SCONTROL_FILE_NAME$0",
            "CANNOT_DISABLE_LAST_ADMIN" : "CANNOT_DISABLE_LAST_ADMIN$0",
            "INVALID_ACCESS_LEVEL" : "INVALID_ACCESS_LEVEL$0",
            "INVALID_TYPE_ON_FIELD_IN_RECORD" : "INVALID_TYPE_ON_FIELD_IN_RECORD$0",
            "CANNOT_DELETE_MANAGED_OBJECT" : "CANNOT_DELETE_MANAGED_OBJECT$0",
            "LICENSE_LIMIT_EXCEEDED" : "LICENSE_LIMIT_EXCEEDED$0",
            "INSUFFICIENT_ACCESS_ON_CROSS_REFERENCE_ENTITY" : "INSUFFICIENT_ACCESS_ON_CROSS_REFERENCE_ENTITY$0",
            "IMAGE_TOO_LARGE" : "IMAGE_TOO_LARGE$0",
            "MAX_APPROVAL_STEPS_EXCEEDED" : "MAX_APPROVAL_STEPS_EXCEEDED$0",
            "CANNOT_CHANGE_FIELD_TYPE_OF_REFERENCED_FIELD" : "CANNOT_CHANGE_FIELD_TYPE_OF_REFERENCED_FIELD$0",
            "TEMPLATE_NOT_ACTIVE" : "TEMPLATE_NOT_ACTIVE$0",
            "INVALID_MASTER_OR_TRANSLATED_SOLUTION" : "INVALID_MASTER_OR_TRANSLATED_SOLUTION$0",
            "CUSTOM_ENTITY_OR_FIELD_LIMIT" : "CUSTOM_ENTITY_OR_FIELD_LIMIT$0",
            "PRIVATE_CONTACT_ON_ASSET" : "PRIVATE_CONTACT_ON_ASSET$0",
            "OPTED_OUT_OF_MASS_MAIL" : "OPTED_OUT_OF_MASS_MAIL$0",
            "QUERY_TIMEOUT" : "QUERY_TIMEOUT$0",
            "LIGHT_PORTAL_USER_EXCEPTION" : "LIGHT_PORTAL_USER_EXCEPTION$0",
            "DUPLICATE_DEVELOPER_NAME" : "DUPLICATE_DEVELOPER_NAME$0",
            "MASS_MAIL_LIMIT_EXCEEDED" : "MASS_MAIL_LIMIT_EXCEEDED$0",
            "CANNOT_UPDATE_CONVERTED_LEAD" : "CANNOT_UPDATE_CONVERTED_LEAD$0",
            "CUSTOM_LINK_LIMIT_EXCEEDED" : "CUSTOM_LINK_LIMIT_EXCEEDED$0",
            "INVALID_ASSIGNEE_TYPE" : "INVALID_ASSIGNEE_TYPE$0",
            "MASSMAIL_RETRY_LIMIT_EXCEEDED" : "MASSMAIL_RETRY_LIMIT_EXCEEDED$0",
            "CUSTOM_METADATA_LIMIT_EXCEEDED" : "CUSTOM_METADATA_LIMIT_EXCEEDED$0",
            "BAD_CUSTOM_ENTITY_PARENT_DOMAIN" : "BAD_CUSTOM_ENTITY_PARENT_DOMAIN$0",
            "INVALID_OWNER" : "INVALID_OWNER$0",
            "PACKAGING_API_UNINSTALL_FAILED" : "PACKAGING_API_UNINSTALL_FAILED$0",
            "INVALID_ARGUMENT_TYPE" : "INVALID_ARGUMENT_TYPE$0",
            "ERROR_IN_MAILER" : "ERROR_IN_MAILER$0",
            "NONUNIQUE_SHIPPING_ADDRESS" : "NONUNIQUE_SHIPPING_ADDRESS$0",
            "PORTAL_USER_ALREADY_EXISTS_FOR_CONTACT" : "PORTAL_USER_ALREADY_EXISTS_FOR_CONTACT$0",
            "MAX_TM_RULES_EXCEEDED" : "MAX_TM_RULES_EXCEEDED$0",
            "WRONG_CONTROLLER_TYPE" : "WRONG_CONTROLLER_TYPE$0",
            "MERGE_FAILED" : "MERGE_FAILED$0",
            "TOO_MANY_APEX_REQUESTS" : "TOO_MANY_APEX_REQUESTS$0",
            "CUSTOM_INDEX_EXISTS" : "CUSTOM_INDEX_EXISTS$0",
            "INVALID_INET_ADDRESS" : "INVALID_INET_ADDRESS$0",
            "DUPLICATE_CUSTOM_TAB_MOTIF" : "DUPLICATE_CUSTOM_TAB_MOTIF$0",
            "INVALID_EMPTY_KEY_OWNER" : "INVALID_EMPTY_KEY_OWNER$0",
            "CANNOT_RENAME_REFERENCED_FIELD" : "CANNOT_RENAME_REFERENCED_FIELD$0",
            "CANNOT_RENAME_APEX_REFERENCED_FIELD" : "CANNOT_RENAME_APEX_REFERENCED_FIELD$0",
            "TERRITORY_REALIGN_IN_PROGRESS" : "TERRITORY_REALIGN_IN_PROGRESS$0",
            "CANNOT_DEACTIVATE_DIVISION" : "CANNOT_DEACTIVATE_DIVISION$0",
            "TOO_MANY_ENUM_VALUE" : "TOO_MANY_ENUM_VALUE$0",
            "NO_MASS_MAIL_PERMISSION" : "NO_MASS_MAIL_PERMISSION$0",
            "MAXIMUM_SIZE_OF_ATTACHMENT" : "MAXIMUM_SIZE_OF_ATTACHMENT$0",
            "MAX_RULES_EXCEEDED" : "MAX_RULES_EXCEEDED$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0",
            "values()\tLIST<system.StatusCode>" : "values()$0"
        }
    },
    "invalidparametervalueexception" : {
        "constructors" : {},
        "name" : "InvalidParameterValueException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "feeditemattachmentinput" : {
        "constructors" : {},
        "name" : "FeedItemAttachmentInput",
        "properties" : {},
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0",
            "convertToJavaObject(java:common.api.AppVersion param1)\tjava:java.lang.Object" : "convertToJavaObject($1)$0"
        }
    },
    "userpage" : {
        "constructors" : {},
        "name" : "UserPage",
        "properties" : {
            "previousPageToken" : "previousPageToken$0",
            "previousPageUrl" : "previousPageUrl$0",
            "currentPageUrl" : "currentPageUrl$0",
            "nextPageUrl" : "nextPageUrl$0",
            "currentPageToken" : "currentPageToken$0",
            "nextPageToken" : "nextPageToken$0",
            "users" : "users$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "daterecordfield" : {
        "constructors" : {},
        "name" : "DateRecordField",
        "properties" : {
            "dateValue" : "dateValue$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "processworkitemrequest" : {
        "constructors" : {},
        "name" : "ProcessWorkitemRequest",
        "properties" : {},
        "methods" : {
            "setAction(String param1)\tvoid" : "setAction($1)$0",
            "getAction()\tString" : "getAction()$0",
            "getWorkitemId()\tString" : "getWorkitemId()$0",
            "setWorkitemId(String param1)\tvoid" : "setWorkitemId($1)$0"
        }
    },
    "referencerecordfield" : {
        "constructors" : {},
        "name" : "ReferenceRecordField",
        "properties" : {
            "reference" : "reference$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "feeditemvisibilitytype" : {
        "constructors" : {},
        "name" : "FeedItemVisibilityType",
        "properties" : {
            "AllUsers" : "AllUsers$0",
            "InternalUsers" : "InternalUsers$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<ConnectApi.FeedItemVisibilityType>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "xmlexception" : {
        "constructors" : {},
        "name" : "XmlException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "linkattachment" : {
        "constructors" : {},
        "name" : "LinkAttachment",
        "properties" : {
            "url" : "url$0",
            "title" : "title$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "http" : {
        "constructors" : {},
        "name" : "Http",
        "properties" : {},
        "methods" : {
            "send(ANY request)\tSystem.HttpResponse" : "send($1)$0",
            "toString()\tString" : "toString()$0"
        }
    },
    "userprofiletab" : {
        "constructors" : {},
        "name" : "UserProfileTab",
        "properties" : {
            "tabType" : "tabType$0",
            "isDefault" : "isDefault$0",
            "id" : "id$0",
            "tabUrl" : "tabUrl$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "liveagentrealtimesystem" : {
        "constructors" : {},
        "name" : "LiveAgentRealTimeSystem",
        "properties" : {},
        "methods" : {
            "routeChatRequests(LIST<LiveAgent.LiveChatRoutingRoute> routes)\tLIST<LiveAgent.LiveChatRoutingResult>" : "routeChatRequests($1)$0",
            "setButtonStatus(String liveChatButtonId, Boolean online)\tvoid" : "setButtonStatus($1)$0"
        }
    },
    "licenseexception" : {
        "constructors" : {},
        "name" : "LicenseException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "unreadconversationcount" : {
        "constructors" : {},
        "name" : "UnreadConversationCount",
        "properties" : {
            "unreadCount" : "unreadCount$0",
            "hasMore" : "hasMore$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "soaptype" : {
        "constructors" : {},
        "name" : "SoapType",
        "properties" : {
            "METADATA_CUSTOMOBJECT" : "METADATA_CUSTOMOBJECT$0",
            "METADATA_APEXTRIGGER" : "METADATA_APEXTRIGGER$0",
            "ANYTYPE" : "ANYTYPE$0",
            "DATE" : "DATE$0",
            "SYMBOLTABLE" : "SYMBOLTABLE$0",
            "ID" : "ID$0",
            "METADATA_APEXCLASS" : "METADATA_APEXCLASS$0",
            "BOOLEAN" : "BOOLEAN$0",
            "BASE64BINARY" : "BASE64BINARY$0",
            "APEXCODECOVERAGE_COVERAGE" : "APEXCODECOVERAGE_COVERAGE$0",
            "INTEGER" : "INTEGER$0",
            "METADATA_APEXCOMPONENT" : "METADATA_APEXCOMPONENT$0",
            "EXECUTIONOVERLAY_HEAPDUMP" : "EXECUTIONOVERLAY_HEAPDUMP$0",
            "METADATA_APEXPAGE" : "METADATA_APEXPAGE$0",
            "DOUBLE" : "DOUBLE$0",
            "DATETIME" : "DATETIME$0",
            "TIME" : "TIME$0",
            "METADATA_CUSTOMFIELD" : "METADATA_CUSTOMFIELD$0",
            "EXECUTIONOVERLAY_APEXRESULT" : "EXECUTIONOVERLAY_APEXRESULT$0",
            "EXECUTIONOVERLAY_SOQLRESULT" : "EXECUTIONOVERLAY_SOQLRESULT$0",
            "STRING" : "STRING$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0",
            "values()\tLIST<Schema.SoapType>" : "values()$0"
        }
    },
    "describedatacategorygroupresult" : {
        "constructors" : {},
        "name" : "DescribeDataCategoryGroupResult",
        "properties" : {},
        "methods" : {
            "getCategoryCount()\tInteger" : "getCategoryCount()$0",
            "getName()\tString" : "getName()$0",
            "getSobject()\tString" : "getSobject()$0",
            "getLabel()\tString" : "getLabel()$0",
            "getDescription()\tString" : "getDescription()$0"
        }
    },
    "chatterfeeds" : {
        "constructors" : {},
        "name" : "ChatterFeeds",
        "properties" : {},
        "methods" : {
            "getFeedItemsFromFilterFeed(String communityId, String subjectId, String keyPrefix)\tConnectApi.FeedItemPage" : "getFeedItemsFromFilterFeed($1)$0",
            "deleteLike(String communityId, String likeId)\tvoid" : "deleteLike($1)$0",
            "setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String q, ConnectApi.FeedItemPage result)\tvoid" : "setTestSearchFeedItemsInFeed($1)$0",
            "getFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, ConnectApi.FeedSortOrder sortParam)\tConnectApi.Feed" : "getFeed($1)$0",
            "setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String q, ConnectApi.FeedItemPage result)\tvoid" : "setTestSearchFeedItemsInFeed($1)$0",
            "getComment(String communityId, String commentId)\tConnectApi.Comment" : "getComment($1)$0",
            "setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedItemPage result)\tvoid" : "setTestSearchFeedItemsInFeed($1)$0",
            "getFilterFeed(String communityId, String subjectId, String keyPrefix, ConnectApi.FeedSortOrder sortParam)\tConnectApi.Feed" : "getFilterFeed($1)$0",
            "setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, ConnectApi.FeedItemPage result)\tvoid" : "setTestGetFeedItemsFromFeed($1)$0",
            "searchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q)\tConnectApi.FeedItemPage" : "searchFeedItemsInFeed($1)$0",
            "voteOnFeedPoll(String communityId, String feedItemId, String myChoiceId)\tConnectApi.FeedPoll" : "voteOnFeedPoll($1)$0",
            "deleteFeedItem(String communityId, String feedItemId)\tvoid" : "deleteFeedItem($1)$0",
            "getLike(String communityId, String likeId)\tConnectApi.ChatterLike" : "getLike($1)$0",
            "setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedItemPage result)\tvoid" : "setTestSearchFeedItemsInFeed($1)$0",
            "postFeedItem(String communityId, ConnectApi.FeedType feedType, String subjectId, ConnectApi.FeedItemInput feedItem, ConnectApi.BinaryInput feedItemFileUpload)\tConnectApi.FeedItem" : "postFeedItem($1)$0",
            "searchFeedItemsInFilterFeed(String communityId, String subjectId, String keyPrefix, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q)\tConnectApi.FeedItemPage" : "searchFeedItemsInFilterFeed($1)$0",
            "postFeedItem(String communityId, ConnectApi.FeedType feedType, String subjectId, String text)\tConnectApi.FeedItem" : "postFeedItem($1)$0",
            "getFeed(String communityId, ConnectApi.FeedType feedType, String subjectId)\tConnectApi.Feed" : "getFeed($1)$0",
            "postComment(String communityId, String feedItemId, ConnectApi.CommentInput comment, ConnectApi.BinaryInput feedItemFileUpload)\tConnectApi.Comment" : "postComment($1)$0",
            "searchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, ConnectApi.FeedDensity density, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q)\tConnectApi.FeedItemPage" : "searchFeedItemsInFeed($1)$0",
            "searchFeedItemsInFilterFeed(String communityId, String subjectId, String keyPrefix, String q)\tConnectApi.FeedItemPage" : "searchFeedItemsInFilterFeed($1)$0",
            "setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)\tvoid" : "setTestGetFeedItemsFromFeed($1)$0",
            "setTestSearchFeedItems(String communityId, String q, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)\tvoid" : "setTestSearchFeedItems($1)$0",
            "shareFeedItem(String communityId, ConnectApi.FeedType feedType, String subjectId, String originalFeedItemId)\tConnectApi.FeedItem" : "shareFeedItem($1)$0",
            "isModified(String communityId, ConnectApi.FeedType feedType, String subjectId, String since)\tConnectApi.FeedModifiedInfo" : "isModified($1)$0",
            "searchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String q)\tConnectApi.FeedItemPage" : "searchFeedItemsInFeed($1)$0",
            "getFilterFeed(String communityId, String subjectId, String keyPrefix)\tConnectApi.Feed" : "getFilterFeed($1)$0",
            "searchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String q)\tConnectApi.FeedItemPage" : "searchFeedItemsInFeed($1)$0",
            "getFeed(String communityId, ConnectApi.FeedType feedType)\tConnectApi.Feed" : "getFeed($1)$0",
            "setTestSearchFeedItems(String communityId, String q, String pageParam, Integer pageSize, ConnectApi.FeedItemPage result)\tvoid" : "setTestSearchFeedItems($1)$0",
            "setTestGetFeedItemsFromFilterFeed(String communityId, String subjectId, String keyPrefix, ConnectApi.FeedItemPage result)\tvoid" : "setTestGetFeedItemsFromFilterFeed($1)$0",
            "setTestSearchFeedItemsInFilterFeed(String communityId, String subjectId, String keyPrefix, Integer recentCommentCount, ConnectApi.FeedDensity density, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedItemPage result)\tvoid" : "setTestSearchFeedItemsInFilterFeed($1)$0",
            "setTestSearchFeedItems(String communityId, String q, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)\tvoid" : "setTestSearchFeedItems($1)$0",
            "getFeedItem(String communityId, String feedItemId)\tConnectApi.FeedItem" : "getFeedItem($1)$0",
            "postComment(String communityId, String feedItemId, String text)\tConnectApi.Comment" : "postComment($1)$0",
            "getFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType)\tConnectApi.FeedItemPage" : "getFeedItemsFromFeed($1)$0",
            "setTestSearchFeedItems(String communityId, String q, ConnectApi.FeedItemPage result)\tvoid" : "setTestSearchFeedItems($1)$0",
            "searchFeedItems(String communityId, String q, ConnectApi.FeedSortOrder sortParam)\tConnectApi.FeedItemPage" : "searchFeedItems($1)$0",
            "searchFeedItemsInFilterFeed(String communityId, String subjectId, String keyPrefix, Integer recentCommentCount, ConnectApi.FeedDensity density, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q)\tConnectApi.FeedItemPage" : "searchFeedItemsInFilterFeed($1)$0",
            "setTestSearchFeedItemsInFilterFeed(String communityId, String subjectId, String keyPrefix, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedItemPage result)\tvoid" : "setTestSearchFeedItemsInFilterFeed($1)$0",
            "setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)\tvoid" : "setTestGetFeedItemsFromFeed($1)$0",
            "searchFeedItems(String communityId, String q, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)\tConnectApi.FeedItemPage" : "searchFeedItems($1)$0",
            "setTestGetFeedItemsFromFilterFeed(String communityId, String subjectId, String keyPrefix, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)\tvoid" : "setTestGetFeedItemsFromFilterFeed($1)$0",
            "getCommentsForFeedItem(String communityId, String feedItemId)\tConnectApi.CommentPage" : "getCommentsForFeedItem($1)$0",
            "getLikesForFeedItem(String communityId, String feedItemId, Integer pageParam, Integer pageSize)\tConnectApi.ChatterLikePage" : "getLikesForFeedItem($1)$0",
            "setTestSearchFeedItems(String communityId, String q, Integer recentCommentCount, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)\tvoid" : "setTestSearchFeedItems($1)$0",
            "setTestSearchFeedItemsInFilterFeed(String communityId, String subjectId, String keyPrefix, String q, ConnectApi.FeedItemPage result)\tvoid" : "setTestSearchFeedItemsInFilterFeed($1)$0",
            "getFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)\tConnectApi.FeedItemPage" : "getFeedItemsFromFeed($1)$0",
            "likeFeedItem(String communityId, String feedItemId)\tConnectApi.ChatterLike" : "likeFeedItem($1)$0",
            "searchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q)\tConnectApi.FeedItemPage" : "searchFeedItemsInFeed($1)$0",
            "updateBookmark(String communityId, String feedItemId, Boolean isBookmarkedByCurrentUser)\tConnectApi.FeedItem" : "updateBookmark($1)$0",
            "getLikesForComment(String communityId, String commentId)\tConnectApi.ChatterLikePage" : "getLikesForComment($1)$0",
            "getFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)\tConnectApi.FeedItemPage" : "getFeedItemsFromFeed($1)$0",
            "getFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, ConnectApi.FeedDensity density, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)\tConnectApi.FeedItemPage" : "getFeedItemsFromFeed($1)$0",
            "searchFeedItems(String communityId, String q, Integer recentCommentCount, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)\tConnectApi.FeedItemPage" : "searchFeedItems($1)$0",
            "getFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, Integer recentCommentCount, ConnectApi.FeedDensity density, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)\tConnectApi.FeedItemPage" : "getFeedItemsFromFeed($1)$0",
            "setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)\tvoid" : "setTestGetFeedItemsFromFeed($1)$0",
            "getFeed(String communityId, ConnectApi.FeedType feedType, ConnectApi.FeedSortOrder sortParam)\tConnectApi.Feed" : "getFeed($1)$0",
            "setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedItemPage result)\tvoid" : "setTestSearchFeedItemsInFeed($1)$0",
            "setTestGetFeedItemsFromFilterFeed(String communityId, String subjectId, String keyPrefix, Integer recentCommentCount, ConnectApi.FeedDensity density, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)\tvoid" : "setTestGetFeedItemsFromFilterFeed($1)$0",
            "likeComment(String communityId, String commentId)\tConnectApi.ChatterLike" : "likeComment($1)$0",
            "getFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String subjectId)\tConnectApi.FeedItemPage" : "getFeedItemsFromFeed($1)$0",
            "getLikesForFeedItem(String communityId, String feedItemId)\tConnectApi.ChatterLikePage" : "getLikesForFeedItem($1)$0",
            "searchFeedItems(String communityId, String q)\tConnectApi.FeedItemPage" : "searchFeedItems($1)$0",
            "searchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q)\tConnectApi.FeedItemPage" : "searchFeedItemsInFeed($1)$0",
            "setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, ConnectApi.FeedItemPage result)\tvoid" : "setTestGetFeedItemsFromFeed($1)$0",
            "getLikesForComment(String communityId, String commentId, Integer pageParam, Integer pageSize)\tConnectApi.ChatterLikePage" : "getLikesForComment($1)$0",
            "setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, ConnectApi.FeedDensity density, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedItemPage result)\tvoid" : "setTestSearchFeedItemsInFeed($1)$0",
            "deleteComment(String communityId, String commentId)\tvoid" : "deleteComment($1)$0",
            "getCommentsForFeedItem(String communityId, String feedItemId, String pageParam, Integer pageSize)\tConnectApi.CommentPage" : "getCommentsForFeedItem($1)$0",
            "searchFeedItems(String communityId, String q, String pageParam, Integer pageSize)\tConnectApi.FeedItemPage" : "searchFeedItems($1)$0",
            "getFeedPoll(String communityId, String feedItemId)\tConnectApi.FeedPoll" : "getFeedPoll($1)$0",
            "setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, Integer recentCommentCount, ConnectApi.FeedDensity density, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)\tvoid" : "setTestGetFeedItemsFromFeed($1)$0",
            "getFeedItemsFromFilterFeed(String communityId, String subjectId, String keyPrefix, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)\tConnectApi.FeedItemPage" : "getFeedItemsFromFilterFeed($1)$0",
            "getFeedItemsFromFilterFeed(String communityId, String subjectId, String keyPrefix, Integer recentCommentCount, ConnectApi.FeedDensity density, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)\tConnectApi.FeedItemPage" : "getFeedItemsFromFilterFeed($1)$0"
        }
    },
    "setupscope" : {
        "constructors" : {},
        "name" : "SetupScope",
        "properties" : {
            "ORGANIZATION" : "ORGANIZATION$0",
            "PROFILE" : "PROFILE$0",
            "USER" : "USER$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<system.SetupScope>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "livechatroutingrequest" : {
        "constructors" : {},
        "name" : "LiveChatRoutingRequest",
        "properties" : {},
        "methods" : {
            "getChatKey()\tString" : "getChatKey()$0",
            "getLiveChatButtonId()\tString" : "getLiveChatButtonId()$0"
        }
    },
    "time" : {
        "constructors" : {},
        "name" : "Time",
        "properties" : {},
        "methods" : {
            "addError(String msg)\tvoid" : "addError($1)$0",
            "hour()\tInteger" : "hour()$0",
            "newInstance(Integer hour, Integer minute, Integer second, Integer millisecond)\tTime" : "newInstance($1)$0",
            "addHours(Integer hours)\tTime" : "addHours($1)$0",
            "minute()\tInteger" : "minute()$0",
            "addError(APEX_OBJECT msg, Boolean escape)\tvoid" : "addError($1)$0",
            "millisecond()\tInteger" : "millisecond()$0",
            "addError(String msg, Boolean escape)\tvoid" : "addError($1)$0",
            "addError(APEX_OBJECT msg)\tvoid" : "addError($1)$0",
            "second()\tInteger" : "second()$0",
            "addMinutes(Integer minutes)\tTime" : "addMinutes($1)$0",
            "addMilliseconds(Integer milliseconds)\tTime" : "addMilliseconds($1)$0",
            "addSeconds(Integer seconds)\tTime" : "addSeconds($1)$0"
        }
    },
    "grouparchivestatus" : {
        "constructors" : {},
        "name" : "GroupArchiveStatus",
        "properties" : {
            "All" : "All$0",
            "NotArchived" : "NotArchived$0",
            "Archived" : "Archived$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<ConnectApi.GroupArchiveStatus>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "groupemailfrequency" : {
        "constructors" : {},
        "name" : "GroupEmailFrequency",
        "properties" : {
            "Never" : "Never$0",
            "EachPost" : "EachPost$0",
            "DailyDigest" : "DailyDigest$0",
            "UseDefault" : "UseDefault$0",
            "WeeklyDigest" : "WeeklyDigest$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<ConnectApi.GroupEmailFrequency>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "massemailmessage" : {
        "constructors" : {},
        "name" : "MassEmailMessage",
        "properties" : {},
        "methods" : {
            "setBccSender(Boolean param1)\tvoid" : "setBccSender($1)$0",
            "setSenderDisplayName(String param1)\tvoid" : "setSenderDisplayName($1)$0",
            "setWhatIds(LIST<Id> param1)\tvoid" : "setWhatIds($1)$0",
            "setReplyTo(String param1)\tvoid" : "setReplyTo($1)$0",
            "setSaveAsActivity(Boolean param1)\tvoid" : "setSaveAsActivity($1)$0",
            "getWhatIds()\tLIST<Id>" : "getWhatIds()$0",
            "getBccSender()\tBoolean" : "getBccSender()$0",
            "getSenderDisplayName()\tString" : "getSenderDisplayName()$0",
            "getSubject()\tString" : "getSubject()$0",
            "getDescription()\tString" : "getDescription()$0",
            "getUseSignature()\tBoolean" : "getUseSignature()$0",
            "getSaveAsActivity()\tBoolean" : "getSaveAsActivity()$0",
            "getTargetObjectIds()\tLIST<Id>" : "getTargetObjectIds()$0",
            "getReplyTo()\tString" : "getReplyTo()$0",
            "getTemplateId()\tId" : "getTemplateId()$0",
            "setDescription(String param1)\tvoid" : "setDescription($1)$0",
            "setSubject(String param1)\tvoid" : "setSubject($1)$0",
            "setTargetObjectIds(LIST<Id> param1)\tvoid" : "setTargetObjectIds($1)$0",
            "setTemplateId(Id param1)\tvoid" : "setTemplateId($1)$0",
            "setUseSignature(Boolean param1)\tvoid" : "setUseSignature($1)$0",
            "setEmailPriority(String param1)\tvoid" : "setEmailPriority($1)$0",
            "getEmailPriority()\tString" : "getEmailPriority()$0"
        }
    },
    "inboundsocialposthandlerimpl" : {
        "constructors" : {},
        "name" : "InboundSocialPostHandlerImpl",
        "properties" : {},
        "methods" : {
            "usePersonAccount()\tBoolean" : "usePersonAccount()$0",
            "getMaxNumberOfDaysClosedToReopenCase()\tInteger" : "getMaxNumberOfDaysClosedToReopenCase()$0",
            "getDefaultAccountId()\tString" : "getDefaultAccountId()$0",
            "handleInboundSocialPost(SocialPost post, SocialPersona persona, MAP<String,ANY> rawData)\tSocial.InboundSocialPostResult" : "handleInboundSocialPost($1)$0"
        }
    },
    "chattergroupsummary" : {
        "constructors" : {},
        "name" : "ChatterGroupSummary",
        "properties" : {
            "fileCount" : "fileCount$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "features" : {
        "constructors" : {},
        "name" : "Features",
        "properties" : {
            "dashboardComponentSnapshots" : "dashboardComponentSnapshots$0",
            "filesOnComments" : "filesOnComments$0",
            "chatterGlobalInfluence" : "chatterGlobalInfluence$0",
            "files" : "files$0",
            "chatterActivity" : "chatterActivity$0",
            "feedPolling" : "feedPolling$0",
            "chatter" : "chatter$0",
            "groupsCanFollow" : "groupsCanFollow$0",
            "viralInvitesAllowed" : "viralInvitesAllowed$0",
            "trendingTopics" : "trendingTopics$0",
            "defaultCurrencyIsoCode" : "defaultCurrencyIsoCode$0",
            "thanksAllowed" : "thanksAllowed$0",
            "multiCurrency" : "multiCurrency$0",
            "chatterAnswers" : "chatterAnswers$0",
            "ideas" : "ideas$0",
            "communityModeration" : "communityModeration$0",
            "mobileNotificationsEnabled" : "mobileNotificationsEnabled$0",
            "publisherActions" : "publisherActions$0",
            "chatterMessages" : "chatterMessages$0",
            "chatterTopics" : "chatterTopics$0",
            "connectRecords" : "connectRecords$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "picklistrecordfield" : {
        "constructors" : {},
        "name" : "PicklistRecordField",
        "properties" : {},
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "schema" : {
        "constructors" : {},
        "name" : "Schema",
        "properties" : ["SoapType", "SObjectField", "DisplayType", "SObjectType", "DataCategoryGroupSobjectTypePair"],
        "methods" : {
            "getModuleDescribe(String moduleName)\tMAP<String,Schema.SObjectType>" : "getModuleDescribe($1)$0",
            "describeDataCategoryGroupStructures(LIST<Schema.DataCategoryGroupSobjectTypePair> pairs, Boolean topCategoriesOnly)\tLIST<Schema.DescribeDataCategoryGroupStructureResult>" : "describeDataCategoryGroupStructures($1)$0",
            "describeDataCategoryGroups(LIST<String> sobjects)\tLIST<Schema.DescribeDataCategoryGroupResult>" : "describeDataCategoryGroups($1)$0",
            "describeTabs()\tLIST<Schema.DescribeTabSetResult>" : "describeTabs()$0",
            "describeSObjects(LIST<String> types)\tLIST<Schema.DescribeSObjectResult>" : "describeSObjects($1)$0",
            "getAppDescribe(String appName)\tMAP<String,Schema.SObjectType>" : "getAppDescribe($1)$0",
            "getGlobalDescribe()\tMAP<String,Schema.SObjectType>" : "getGlobalDescribe()$0",
            "getModuleDescribe()\tMAP<String,Schema.SObjectType>" : "getModuleDescribe()$0"
        }
    },
    "linksegment" : {
        "constructors" : {},
        "name" : "LinkSegment",
        "properties" : {
            "url" : "url$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "mobilepushpayload" : {
        "constructors" : {},
        "name" : "MobilePushPayload",
        "properties" : {},
        "methods" : {
            "apple(String alert, String sound, Integer badgeCount, MAP<String,ANY> userData)\tMAP<String,ANY>" : "apple($1)$0",
            "apple(String alertBody, String actionLocKey, String locKey, LIST<String> locArgs, String launchImage, String sound, Integer badgeCount, MAP<String,ANY> userData)\tMAP<String,ANY>" : "apple($1)$0"
        }
    },
    "httpcalloutmock" : {
        "constructors" : {},
        "name" : "HttpCalloutMock",
        "properties" : {},
        "methods" : {
            "respond(System.HttpRequest param1)\tSystem.HttpResponse" : "respond($1)$0"
        }
    },
    "recordsnapshotattachment" : {
        "constructors" : {},
        "name" : "RecordSnapshotAttachment",
        "properties" : {
            "recordView" : "recordView$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "appexchange" : {
        "constructors" : {},
        "name" : "AppExchange",
        "properties" : {},
        "methods" : {
            "getAuthenticatingUrl(String page)\tString" : "getAuthenticatingUrl($1)$0",
            "provisionPackageLicense(String orgId, String allPackageId, Integer numLicenses, Date expirationDate, String status)\tString" : "provisionPackageLicense($1)$0",
            "createOrg(String firstName, String lastName, String companyName, String email, String language, String adminUserName, String packageId, String evalUserName, Boolean isExtension)\tString" : "createOrg($1)$0",
            "to15(String id)\tString" : "to15($1)$0",
            "stopListingPopularityJob()\tvoid" : "stopListingPopularityJob()$0",
            "getCookie(String name)\tString" : "getCookie($1)$0",
            "createSession(String appExchangeOrgId, String portalId, String siteId, String portalUserId)\tString" : "createSession($1)$0",
            "getTrialTemplates(String callerOrgId, String lmPkgId, String username)\tLIST<TrialTemplate>" : "getTrialTemplates($1)$0",
            "isGuestUser()\tBoolean" : "isGuestUser()$0",
            "setLicenseManagementOrganization(String pkgVersionId, String orgId, String username, String password)\tString" : "setLicenseManagementOrganization($1)$0",
            "calculateListingPopularity(String testUserName, String testCronString)\tvoid" : "calculateListingPopularity($1)$0",
            "setCookie(String name, String value, String cookieDomainName, Integer cookieAge)\tvoid" : "setCookie($1)$0",
            "debug(String message)\tvoid" : "debug($1)$0",
            "isDuplicateUserName(String username)\tBoolean" : "isDuplicateUserName($1)$0",
            "validateOrgUser(String username, String password)\tString" : "validateOrgUser($1)$0",
            "createPortalUser(SObject user, String accountId)\tId" : "createPortalUser($1)$0",
            "movedPermanently(String location)\tvoid" : "movedPermanently($1)$0",
            "getOrgName(String orgId)\tString" : "getOrgName($1)$0",
            "updateSingleAsAdmin(SObject sobj)\tDatabase.SaveResult" : "updateSingleAsAdmin($1)$0",
            "setCookie(String name, String value)\tvoid" : "setCookie($1)$0",
            "getInstalledPackageVersions(String orgId)\tLIST<String>" : "getInstalledPackageVersions($1)$0",
            "to18(String id)\tString" : "to18($1)$0",
            "validateLMAInstalled(String username, String password)\tString" : "validateLMAInstalled($1)$0",
            "getPortalId()\tString" : "getPortalId()$0",
            "registerPackageVersion(String pkgVersionId)\tBoolean" : "registerPackageVersion($1)$0",
            "getSiteId()\tString" : "getSiteId()$0",
            "setDefaultLicenseTerms(String pkgVersionId, String orgId, String defaultLicenseStatus, Integer defaultLicenseLength, Integer defaultLicenseSeats)\tvoid" : "setDefaultLicenseTerms($1)$0",
            "setHttpResponseStatus(Integer statusCode)\tvoid" : "setHttpResponseStatus($1)$0",
            "getPortalAdminId()\tString" : "getPortalAdminId()$0",
            "getConfig(String section, String key)\tString" : "getConfig($1)$0",
            "getCrossInstanceEncryptedHash(Double appVersion, String value)\tString" : "getCrossInstanceEncryptedHash($1)$0",
            "getPackageManifest(String pkgVersionId)\tString" : "getPackageManifest($1)$0"
        }
    },
    "emailexception" : {
        "constructors" : {},
        "name" : "EmailException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getDmlId(Integer index)\tString" : "getDmlId($1)$0",
            "getDmlMessage(Integer index)\tString" : "getDmlMessage($1)$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getNumDml()\tInteger" : "getNumDml()$0",
            "getDmlFields(Integer index)\tLIST<Schema.SObjectField>" : "getDmlFields($1)$0",
            "getDmlType(Integer index)\tsystem.StatusCode" : "getDmlType($1)$0",
            "getDmlIndex(Integer index)\tInteger" : "getDmlIndex($1)$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "getDmlFieldNames(Integer index)\tLIST<String>" : "getDmlFieldNames($1)$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getDmlStatusCode(Integer index)\tString" : "getDmlStatusCode($1)$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "knowledgearticleversionstandardcontroller" : {
        "constructors" : {},
        "name" : "KnowledgeArticleVersionStandardController",
        "properties" : {},
        "methods" : {
            "delete()\tSystem.PageReference" : "delete()$0",
            "getRecord()\tSObject" : "getRecord()$0",
            "getId()\tString" : "getId()$0",
            "getSourceId()\tString" : "getSourceId()$0",
            "edit()\tSystem.PageReference" : "edit()$0",
            "getSubject()\tSObject" : "getSubject()$0",
            "reset()\tvoid" : "reset()$0",
            "view()\tSystem.PageReference" : "view()$0",
            "selectDataCategory(String categoryGroup, String category)\tvoid" : "selectDataCategory($1)$0",
            "save()\tSystem.PageReference" : "save()$0",
            "cancel()\tSystem.PageReference" : "cancel()$0",
            "addFields(LIST<String> fieldNames)\tvoid" : "addFields($1)$0"
        }
    },
    "header" : {
        "constructors" : {},
        "name" : "Header",
        "properties" : {
            "value" : "value$0",
            "name" : "name$0"
        },
        "methods" : {}

    },
    "mathexception" : {
        "constructors" : {},
        "name" : "MathException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "fieldchangevaluesegment" : {
        "constructors" : {},
        "name" : "FieldChangeValueSegment",
        "properties" : {
            "valueType" : "valueType$0",
            "url" : "url$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "columnsortorder" : {
        "constructors" : {},
        "name" : "ColumnSortOrder",
        "properties" : {
            "ASCENDING" : "ASCENDING$0",
            "DESCENDING" : "DESCENDING$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<reports.ColumnSortOrder>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "webservicemock" : {
        "constructors" : {},
        "name" : "WebServiceMock",
        "properties" : {},
        "methods" : {
            "doInvoke(Object param1, Object param2, MAP<String,ANY> param3, String param4, String param5, String param6, String param7, String param8, String param9)\tvoid" : "doInvoke($1)$0"
        }
    },
    "actor" : {
        "constructors" : {},
        "name" : "Actor",
        "properties" : {
            "name" : "name$0",
            "type" : "type$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "recordsummary" : {
        "constructors" : {},
        "name" : "RecordSummary",
        "properties" : {},
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "filtervalue" : {
        "constructors" : {},
        "name" : "FilterValue",
        "properties" : {},
        "methods" : {
            "setLabel(String label)\tvoid" : "setLabel($1)$0",
            "setName(String name)\tvoid" : "setName($1)$0",
            "getLabel()\tString" : "getLabel()$0",
            "getName()\tString" : "getName()$0"
        }
    },
    "docscontroller" : {
        "constructors" : {},
        "name" : "DocsController",
        "properties" : {},
        "methods" : {}

    },
    "sobjectexception" : {
        "constructors" : {},
        "name" : "SObjectException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "ratelimitexception" : {
        "constructors" : {},
        "name" : "RateLimitException",
        "properties" : {},
        "methods" : {
            "getErrorCode()\tString" : "getErrorCode()$0",
            "getTypeName()\tString" : "getTypeName()$0"
        }
    },
    "multistaticresourcecalloutmock" : {
        "constructors" : {},
        "name" : "MultiStaticResourceCalloutMock",
        "properties" : {},
        "methods" : {
            "respond(System.HttpRequest request)\tSystem.HttpResponse" : "respond($1)$0",
            "setHeader(String key, String val)\tvoid" : "setHeader($1)$0",
            "setStaticResource(String url, String staticResourceName)\tvoid" : "setStaticResource($1)$0",
            "setStatusCode(Integer code)\tvoid" : "setStatusCode($1)$0",
            "setStatus(String status)\tvoid" : "setStatus($1)$0"
        }
    },
    "processresult" : {
        "constructors" : {},
        "name" : "ProcessResult",
        "properties" : {},
        "methods" : {
            "getEntityId()\tString" : "getEntityId()$0",
            "getInstanceStatus()\tString" : "getInstanceStatus()$0",
            "getInstanceId()\tString" : "getInstanceId()$0",
            "getNewWorkitemIds()\tLIST<Id>" : "getNewWorkitemIds()$0",
            "getErrors()\tLIST<Database.Error>" : "getErrors()$0",
            "getActorIds()\tLIST<Id>" : "getActorIds()$0",
            "isSuccess()\tBoolean" : "isSuccess()$0"
        }
    },
    "type" : {
        "constructors" : {},
        "name" : "Type",
        "properties" : {},
        "methods" : {
            "newInstance()\tObject" : "newInstance()$0",
            "getName()\tString" : "getName()$0",
            "forName(String clsName)\tsystem.Type" : "forName($1)$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object o)\tBoolean" : "equals($1)$0",
            "forName(String namespace, String clsName)\tsystem.Type" : "forName($1)$0"
        }
    },
    "chattermessagepage" : {
        "constructors" : {},
        "name" : "ChatterMessagePage",
        "properties" : {
            "currentPageUrl" : "currentPageUrl$0",
            "nextPageUrl" : "nextPageUrl$0",
            "currentPageToken" : "currentPageToken$0",
            "nextPageToken" : "nextPageToken$0",
            "messages" : "messages$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "matcher" : {
        "constructors" : {},
        "name" : "Matcher",
        "properties" : {},
        "methods" : {
            "find()\tBoolean" : "find()$0",
            "group()\tString" : "group()$0",
            "start(Integer grp)\tInteger" : "start($1)$0",
            "regionStart()\tInteger" : "regionStart()$0",
            "group(Integer start)\tString" : "group($1)$0",
            "hitEnd()\tBoolean" : "hitEnd()$0",
            "regionEnd()\tInteger" : "regionEnd()$0",
            "hasTransparentBounds()\tBoolean" : "hasTransparentBounds()$0",
            "region(Integer start, Integer ending)\tsystem.Matcher" : "region($1)$0",
            "requireEnd()\tBoolean" : "requireEnd()$0",
            "reset()\tsystem.Matcher" : "reset()$0",
            "start()\tInteger" : "start()$0",
            "lookingAt()\tBoolean" : "lookingAt()$0",
            "find(Integer start)\tBoolean" : "find($1)$0",
            "groupCount()\tInteger" : "groupCount()$0",
            "hasAnchoringBounds()\tBoolean" : "hasAnchoringBounds()$0",
            "reset(String input)\tsystem.Matcher" : "reset($1)$0",
            "replaceAll(String replacement)\tString" : "replaceAll($1)$0",
            "pattern()\tsystem.Pattern" : "pattern()$0",
            "end(Integer grp)\tInteger" : "end($1)$0",
            "useAnchoringBounds(Boolean b)\tsystem.Matcher" : "useAnchoringBounds($1)$0",
            "usePattern(system.Pattern p)\tsystem.Matcher" : "usePattern($1)$0",
            "end()\tInteger" : "end()$0",
            "quoteReplacement(String s)\tString" : "quoteReplacement($1)$0",
            "useTransparentBounds(Boolean b)\tsystem.Matcher" : "useTransparentBounds($1)$0",
            "matches()\tBoolean" : "matches()$0",
            "replaceFirst(String replacement)\tString" : "replaceFirst($1)$0"
        }
    },
    "list" : {
        "constructors" : {},
        "name" : "LIST",
        "properties" : {},
        "methods" : {
            "add(Integer index, ANY element)\tvoid" : "add($1)$0",
            "remove(Integer index)\tObject" : "remove($1)$0",
            "deepClone(Boolean preserveId)\tLIST<String>" : "deepClone($1)$0",
            "deepClone(Boolean preserveId, Boolean preserveReadOnlyTimestamps)\tLIST<String>" : "deepClone($1)$0",
            "clear()\tvoid" : "clear()$0",
            "clone()\tLIST<String>" : "clone()$0",
            "iterator()\tsystem.ListIterator" : "iterator()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "get(Integer index)\tObject" : "get($1)$0",
            "getSObjectType()\tSchema.SObjectType" : "getSObjectType()$0",
            "set(Integer index, ANY value)\tvoid" : "set($1)$0",
            "addAll(SET elements)\tvoid" : "addAll($1)$0",
            "equals(ANY obj)\tBoolean" : "equals($1)$0",
            "add(ANY element)\tObject" : "add($1)$0",
            "sort()\tvoid" : "sort()$0",
            "size()\tInteger" : "size()$0",
            "deepClone(Boolean preserveId, Boolean preserveReadOnlyTimestamps, Boolean preserveAutoNumbers)\tLIST<String>" : "deepClone($1)$0",
            "addAll(LIST elements)\tvoid" : "addAll($1)$0",
            "deepClone()\tLIST<String>" : "deepClone()$0",
            "isEmpty()\tBoolean" : "isEmpty()$0"
        }
    },
    "mentionvalidationstatus" : {
        "constructors" : {},
        "name" : "MentionValidationStatus",
        "properties" : {
            "Inaccessible" : "Inaccessible$0",
            "Disallowed" : "Disallowed$0",
            "Ok" : "Ok$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0",
            "values()\tLIST<ConnectApi.MentionValidationStatus>" : "values()$0"
        }
    },
    "followerpage" : {
        "constructors" : {},
        "name" : "FollowerPage",
        "properties" : {
            "currentPageUrl" : "currentPageUrl$0",
            "nextPageUrl" : "nextPageUrl$0",
            "previousPageUrl" : "previousPageUrl$0",
            "total" : "total$0",
            "followers" : "followers$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "componentiteration" : {
        "constructors" : {},
        "name" : "ComponentIteration",
        "properties" : {
            "iterationValue" : "iterationValue$0",
            "childComponents" : "childComponents$0",
            "parent" : "parent$0"
        },
        "methods" : {
            "getComponentById(String id)\tApexPages.Component" : "getComponentById($1)$0"
        }
    },
    "recordcolumnorder" : {
        "constructors" : {},
        "name" : "RecordColumnOrder",
        "properties" : {
            "LeftRight" : "LeftRight$0",
            "TopDown" : "TopDown$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0",
            "values()\tLIST<ConnectApi.RecordColumnOrder>" : "values()$0"
        }
    },
    "percentrecordfield" : {
        "constructors" : {},
        "name" : "PercentRecordField",
        "properties" : {
            "value" : "value$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "jsontoken" : {
        "constructors" : {},
        "name" : "JSONToken",
        "properties" : {
            "VALUE_TRUE" : "VALUE_TRUE$0",
            "START_OBJECT" : "START_OBJECT$0",
            "START_ARRAY" : "START_ARRAY$0",
            "FIELD_NAME" : "FIELD_NAME$0",
            "VALUE_EMBEDDED_OBJECT" : "VALUE_EMBEDDED_OBJECT$0",
            "VALUE_STRING" : "VALUE_STRING$0",
            "VALUE_FALSE" : "VALUE_FALSE$0",
            "VALUE_NUMBER_FLOAT" : "VALUE_NUMBER_FLOAT$0",
            "VALUE_NUMBER_INT" : "VALUE_NUMBER_INT$0",
            "NOT_AVAILABLE" : "NOT_AVAILABLE$0",
            "VALUE_NULL" : "VALUE_NULL$0",
            "END_OBJECT" : "END_OBJECT$0",
            "END_ARRAY" : "END_ARRAY$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<system.JSONToken>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "compoundrecordfield" : {
        "constructors" : {},
        "name" : "CompoundRecordField",
        "properties" : {
            "fields" : "fields$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "message" : {
        "constructors" : {},
        "name" : "Message",
        "properties" : {},
        "methods" : {
            "getSeverity()\tApexPages.Severity" : "getSeverity()$0",
            "getComponentLabel()\tString" : "getComponentLabel()$0",
            "getDetail()\tString" : "getDetail()$0",
            "getSummary()\tString" : "getSummary()$0"
        }
    },
    "notfoundexception" : {
        "constructors" : {},
        "name" : "NotFoundException",
        "properties" : {},
        "methods" : {
            "getTypeName()\tString" : "getTypeName()$0"
        }
    },
    "communitystatus" : {
        "constructors" : {},
        "name" : "CommunityStatus",
        "properties" : {
            "Inactive" : "Inactive$0",
            "Live" : "Live$0",
            "UnderConstruction" : "UnderConstruction$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "values()\tLIST<ConnectApi.CommunityStatus>" : "values()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "contentattachmentinput" : {
        "constructors" : {},
        "name" : "ContentAttachmentInput",
        "properties" : {
            "contentDocumentId" : "contentDocumentId$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object" : "convertToJavaObject($1)$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "chattergroups" : {
        "constructors" : {},
        "name" : "ChatterGroups",
        "properties" : {},
        "methods" : {
            "setTestSearchGroups(String communityId, String q, ConnectApi.ChatterGroupPage result)\tvoid" : "setTestSearchGroups($1)$0",
            "updateGroupMember(String communityId, String membershipId, ConnectApi.GroupMembershipType role)\tConnectApi.GroupMember" : "updateGroupMember($1)$0",
            "setTestSearchGroups(String communityId, String q, Integer pageParam, Integer pageSize, ConnectApi.ChatterGroupPage result)\tvoid" : "setTestSearchGroups($1)$0",
            "deleteGroup(String communityId, String groupId)\tvoid" : "deleteGroup($1)$0",
            "deleteMember(String communityId, String membershipId)\tvoid" : "deleteMember($1)$0",
            "setPhotoWithAttributes(String communityId, String groupId, ConnectApi.PhotoInput photo, ConnectApi.BinaryInput fileUpload)\tConnectApi.Photo" : "setPhotoWithAttributes($1)$0",
            "setPhotoWithAttributes(String communityId, String groupId, ConnectApi.PhotoInput photo)\tConnectApi.Photo" : "setPhotoWithAttributes($1)$0",
            "updateGroup(String communityId, String groupId, ConnectApi.ChatterGroupInput groupInput)\tConnectApi.ChatterGroupDetail" : "updateGroup($1)$0",
            "getFollowings(String communityId, String groupId, Integer pageParam, Integer pageSize)\tConnectApi.FollowingPage" : "getFollowings($1)$0",
            "getGroups(String communityId, ConnectApi.GroupArchiveStatus archiveStatus, Integer pageParam, Integer pageSize)\tConnectApi.ChatterGroupPage" : "getGroups($1)$0",
            "getGroups(String communityId, Integer pageParam, Integer pageSize)\tConnectApi.ChatterGroupPage" : "getGroups($1)$0",
            "getFollowings(String communityId, String groupId, Integer pageParam)\tConnectApi.FollowingPage" : "getFollowings($1)$0",
            "updateRequestStatus(String communityId, String requestId, ConnectApi.GroupMembershipRequestStatus status)\tConnectApi.GroupMembershipRequest" : "updateRequestStatus($1)$0",
            "getMembers(String communityId, String groupId, Integer pageParam, Integer pageSize)\tConnectApi.GroupMemberPage" : "getMembers($1)$0",
            "getFollowings(String communityId, String groupId, String filterType, Integer pageParam)\tConnectApi.FollowingPage" : "getFollowings($1)$0",
            "getFollowings(String communityId, String groupId, String filterType, Integer pageParam, Integer pageSize)\tConnectApi.FollowingPage" : "getFollowings($1)$0",
            "getMyChatterSettings(String communityId, String groupId)\tConnectApi.GroupChatterSettings" : "getMyChatterSettings($1)$0",
            "getPhoto(String communityId, String groupId)\tConnectApi.Photo" : "getPhoto($1)$0",
            "setTestSearchGroups(String communityId, String q, ConnectApi.GroupArchiveStatus archiveStatus, Integer pageParam, Integer pageSize, ConnectApi.ChatterGroupPage result)\tvoid" : "setTestSearchGroups($1)$0",
            "updateMyChatterSettings(String communityId, String groupId, ConnectApi.GroupEmailFrequency emailFrequency)\tConnectApi.GroupChatterSettings" : "updateMyChatterSettings($1)$0",
            "getMembers(String communityId, String groupId)\tConnectApi.GroupMemberPage" : "getMembers($1)$0",
            "addMemberWithRole(String communityId, String groupId, String userId, ConnectApi.GroupMembershipType role)\tConnectApi.GroupMember" : "addMemberWithRole($1)$0",
            "getGroupMembershipRequest(String communityId, String requestId)\tConnectApi.GroupMembershipRequest" : "getGroupMembershipRequest($1)$0",
            "getGroup(String communityId, String groupId)\tConnectApi.ChatterGroupDetail" : "getGroup($1)$0",
            "requestGroupMembership(String communityId, String groupId)\tConnectApi.GroupMembershipRequest" : "requestGroupMembership($1)$0",
            "searchGroups(String communityId, String q, ConnectApi.GroupArchiveStatus archiveStatus, Integer pageParam, Integer pageSize)\tConnectApi.ChatterGroupPage" : "searchGroups($1)$0",
            "setPhoto(String communityId, String groupId, String fileId, Integer versionNumber)\tConnectApi.Photo" : "setPhoto($1)$0",
            "searchGroups(String communityId, String q, Integer pageParam, Integer pageSize)\tConnectApi.ChatterGroupPage" : "searchGroups($1)$0",
            "setPhoto(String communityId, String groupId, ConnectApi.BinaryInput fileUpload)\tConnectApi.Photo" : "setPhoto($1)$0",
            "addMember(String communityId, String groupId, String userId)\tConnectApi.GroupMember" : "addMember($1)$0",
            "getGroups(String communityId)\tConnectApi.ChatterGroupPage" : "getGroups($1)$0",
            "createGroup(String communityId, ConnectApi.ChatterGroupInput groupInput)\tConnectApi.ChatterGroupDetail" : "createGroup($1)$0",
            "searchGroups(String communityId, String q)\tConnectApi.ChatterGroupPage" : "searchGroups($1)$0",
            "getGroupMembershipRequests(String communityId, String groupId)\tConnectApi.GroupMembershipRequests" : "getGroupMembershipRequests($1)$0",
            "getGroupMembershipRequests(String communityId, String groupId, ConnectApi.GroupMembershipRequestStatus status)\tConnectApi.GroupMembershipRequests" : "getGroupMembershipRequests($1)$0",
            "getMember(String communityId, String membershipId)\tConnectApi.GroupMember" : "getMember($1)$0",
            "follow(String communityId, String groupId, String subjectId)\tConnectApi.Subscription" : "follow($1)$0",
            "deletePhoto(String communityId, String groupId)\tvoid" : "deletePhoto($1)$0",
            "getFollowings(String communityId, String groupId, String filterType)\tConnectApi.FollowingPage" : "getFollowings($1)$0",
            "getFollowings(String communityId, String groupId)\tConnectApi.FollowingPage" : "getFollowings($1)$0"
        }
    },
    "decimal" : {
        "constructors" : {},
        "name" : "Decimal",
        "properties" : {},
        "methods" : {
            "valueOf(Long lng)\tDecimal" : "valueOf($1)$0",
            "doubleValue()\tDouble" : "doubleValue()$0",
            "pow(Integer exponent)\tDecimal" : "pow($1)$0",
            "precision()\tInteger" : "precision()$0",
            "toPlainString()\tString" : "toPlainString()$0",
            "valueOf(String str)\tDecimal" : "valueOf($1)$0",
            "addError(APEX_OBJECT msg)\tvoid" : "addError($1)$0",
            "stripTrailingZeros()\tDecimal" : "stripTrailingZeros()$0",
            "valueOf(Double dbl)\tDecimal" : "valueOf($1)$0",
            "round(system.RoundingMode roundingMode)\tLong" : "round($1)$0",
            "addError(String msg)\tvoid" : "addError($1)$0",
            "format()\tString" : "format()$0",
            "setScale(Integer scale)\tDecimal" : "setScale($1)$0",
            "intValue()\tInteger" : "intValue()$0",
            "addError(APEX_OBJECT msg, Boolean escape)\tvoid" : "addError($1)$0",
            "longValue()\tLong" : "longValue()$0",
            "addError(String msg, Boolean escape)\tvoid" : "addError($1)$0",
            "divide(Decimal divisor, Integer scale, APEX_OBJECT roundingMode)\tDecimal" : "divide($1)$0",
            "setScale(Integer scale, system.RoundingMode roundingMode)\tDecimal" : "setScale($1)$0",
            "round()\tLong" : "round()$0",
            "abs()\tDecimal" : "abs()$0",
            "divide(Decimal divisor, Integer scale)\tDecimal" : "divide($1)$0",
            "scale()\tInteger" : "scale()$0"
        }
    },
    "inboundsocialposthandler" : {
        "constructors" : {},
        "name" : "InboundSocialPostHandler",
        "properties" : {},
        "methods" : {
            "handleInboundSocialPost(SocialPost param1, SocialPersona param2, MAP<String,ANY> param3)\tSocial.InboundSocialPostResult" : "handleInboundSocialPost($1)$0"
        }
    },
    "datetime" : {
        "constructors" : {},
        "name" : "Datetime",
        "properties" : {},
        "methods" : {
            "newInstance(Integer year, Integer month, Integer day, Integer hour, Integer minute, Integer second)\tDatetime" : "newInstance($1)$0",
            "newInstanceGmt(Integer year, Integer month, Integer day, Integer hour, Integer minute, Integer second)\tDatetime" : "newInstanceGmt($1)$0",
            "dayGmt()\tInteger" : "dayGmt()$0",
            "yearGmt()\tInteger" : "yearGmt()$0",
            "secondGmt()\tInteger" : "secondGmt()$0",
            "now()\tDatetime" : "now()$0",
            "valueOf(Object o)\tDatetime" : "valueOf($1)$0",
            "second()\tInteger" : "second()$0",
            "newInstance(Integer year, Integer month, Integer day)\tDatetime" : "newInstance($1)$0",
            "addError(String msg)\tvoid" : "addError($1)$0",
            "format(String dateformat)\tString" : "format($1)$0",
            "day()\tInteger" : "day()$0",
            "newInstanceGmt(Integer year, Integer month, Integer day)\tDatetime" : "newInstanceGmt($1)$0",
            "format()\tString" : "format()$0",
            "isSameDay(Datetime other)\tBoolean" : "isSameDay($1)$0",
            "dayOfYear()\tInteger" : "dayOfYear()$0",
            "addError(APEX_OBJECT msg, Boolean escape)\tvoid" : "addError($1)$0",
            "millisecond()\tInteger" : "millisecond()$0",
            "addError(String msg, Boolean escape)\tvoid" : "addError($1)$0",
            "addMinutes(Integer minutes)\tDatetime" : "addMinutes($1)$0",
            "hourGmt()\tInteger" : "hourGmt()$0",
            "date()\tDate" : "date()$0",
            "formatLong()\tString" : "formatLong()$0",
            "millisecondGmt()\tInteger" : "millisecondGmt()$0",
            "getTime()\tLong" : "getTime()$0",
            "month()\tInteger" : "month()$0",
            "monthGmt()\tInteger" : "monthGmt()$0",
            "addDays(Integer days)\tDatetime" : "addDays($1)$0",
            "formatGmt(String dateformat)\tString" : "formatGmt($1)$0",
            "minute()\tInteger" : "minute()$0",
            "time()\tTime" : "time()$0",
            "year()\tInteger" : "year()$0",
            "newInstance(Long time)\tDatetime" : "newInstance($1)$0",
            "dateGmt()\tDate" : "dateGmt()$0",
            "addError(APEX_OBJECT msg)\tvoid" : "addError($1)$0",
            "dayOfYearGmt()\tInteger" : "dayOfYearGmt()$0",
            "minuteGmt()\tInteger" : "minuteGmt()$0",
            "newInstance(Date date, Time time)\tDatetime" : "newInstance($1)$0",
            "timeGmt()\tTime" : "timeGmt()$0",
            "addYears(Integer years)\tDatetime" : "addYears($1)$0",
            "valueOf(String str)\tDatetime" : "valueOf($1)$0",
            "hour()\tInteger" : "hour()$0",
            "valueOfGmt(String str)\tDatetime" : "valueOfGmt($1)$0",
            "parse(String str)\tDatetime" : "parse($1)$0",
            "format(String dateformat, String timezone)\tString" : "format($1)$0",
            "newInstanceGmt(Date date, Time time)\tDatetime" : "newInstanceGmt($1)$0",
            "addSeconds(Integer seconds)\tDatetime" : "addSeconds($1)$0",
            "addMonths(Integer months)\tDatetime" : "addMonths($1)$0",
            "addHours(Integer hours)\tDatetime" : "addHours($1)$0"
        }
    },
    "describecolorresult" : {
        "constructors" : {},
        "name" : "DescribeColorResult",
        "properties" : {},
        "methods" : {
            "getColor()\tString" : "getColor()$0",
            "getTheme()\tString" : "getTheme()$0",
            "getContext()\tString" : "getContext()$0"
        }
    },
    "caseactortype" : {
        "constructors" : {},
        "name" : "CaseActorType",
        "properties" : {
            "Customer" : "Customer$0",
            "CustomerService" : "CustomerService$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0",
            "values()\tLIST<ConnectApi.CaseActorType>" : "values()$0"
        }
    },
    "standardsetcontroller" : {
        "constructors" : {},
        "name" : "StandardSetController",
        "properties" : {},
        "methods" : {
            "last()\tvoid" : "last()$0",
            "getPageNumber()\tInteger" : "getPageNumber()$0",
            "getRecords()\tLIST<SObject>" : "getRecords()$0",
            "setPageSize(Integer pageSize)\tvoid" : "setPageSize($1)$0",
            "getRecord()\tSObject" : "getRecord()$0",
            "previous()\tvoid" : "previous()$0",
            "addFields(LIST<String> fieldNames)\tvoid" : "addFields($1)$0",
            "getSelected()\tLIST<SObject>" : "getSelected()$0",
            "setFilterId(String filterId)\tvoid" : "setFilterId($1)$0",
            "reset()\tvoid" : "reset()$0",
            "getHasNext()\tBoolean" : "getHasNext()$0",
            "getListViewOptions()\tLIST<System.SelectOption>" : "getListViewOptions()$0",
            "save()\tSystem.PageReference" : "save()$0",
            "next()\tvoid" : "next()$0",
            "setSelected(LIST<SObject> selected)\tvoid" : "setSelected($1)$0",
            "setPageNumber(Integer pageNumber)\tvoid" : "setPageNumber($1)$0",
            "getResultSize()\tInteger" : "getResultSize()$0",
            "getHasPrevious()\tBoolean" : "getHasPrevious()$0",
            "getFilterId()\tString" : "getFilterId()$0",
            "first()\tvoid" : "first()$0",
            "getCompleteResult()\tBoolean" : "getCompleteResult()$0",
            "getPageSize()\tInteger" : "getPageSize()$0",
            "cancel()\tSystem.PageReference" : "cancel()$0"
        }
    },
    "reportimageformula" : {
        "constructors" : {},
        "name" : "ReportImageFormula",
        "properties" : {},
        "methods" : {
            "getText()\tString" : "getText()$0",
            "getHeight()\tString" : "getHeight()$0",
            "setText(String text)\tvoid" : "setText($1)$0",
            "getWidth()\tString" : "getWidth()$0",
            "setImgSrc(String imgSrc)\tvoid" : "setImgSrc($1)$0",
            "setHeight(String height)\tvoid" : "setHeight($1)$0",
            "setWidth(String width)\tvoid" : "setWidth($1)$0",
            "getImgSrc()\tString" : "getImgSrc()$0"
        }
    },
    "emailtosalesforcehandler" : {
        "constructors" : {},
        "name" : "EmailToSalesforceHandler",
        "properties" : {},
        "methods" : {}

    },
    "inboundemailhandler" : {
        "constructors" : {},
        "name" : "InboundEmailHandler",
        "properties" : {},
        "methods" : {
            "handleInboundEmail(Messaging.InboundEmail param1, Messaging.InboundEnvelope param2)\tMessaging.InboundEmailResult" : "handleInboundEmail($1)$0"
        }
    },
    "messagesegmentinput" : {
        "constructors" : {},
        "name" : "MessageSegmentInput",
        "properties" : {},
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0",
            "convertToJavaObject(java:common.api.AppVersion param1)\tjava:java.lang.Object" : "convertToJavaObject($1)$0"
        }
    },
    "inboundemail" : {
        "constructors" : {},
        "name" : "InboundEmail",
        "properties" : {
            "fromAddress" : "fromAddress$0",
            "binaryAttachments" : "binaryAttachments$0",
            "subject" : "subject$0",
            "toAddresses" : "toAddresses$0",
            "ccAddresses" : "ccAddresses$0",
            "htmlBodyIsTruncated" : "htmlBodyIsTruncated$0",
            "messageId" : "messageId$0",
            "plainTextBodyIsTruncated" : "plainTextBodyIsTruncated$0",
            "plainTextBody" : "plainTextBody$0",
            "fromName" : "fromName$0",
            "replyTo" : "replyTo$0",
            "htmlBody" : "htmlBody$0",
            "textAttachments" : "textAttachments$0",
            "inReplyTo" : "inReplyTo$0",
            "references" : "references$0",
            "headers" : "headers$0"
        },
        "methods" : {}

    },
    "referencewithdaterecordfield" : {
        "constructors" : {},
        "name" : "ReferenceWithDateRecordField",
        "properties" : {
            "dateValue" : "dateValue$0",
            "reference" : "reference$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "answers" : {
        "constructors" : {},
        "name" : "Answers",
        "properties" : {},
        "methods" : {
            "setBestReply(String questionId, String bestReplyId)\tvoid" : "setBestReply($1)$0",
            "findSimilar(SObject question)\tLIST<Id>" : "findSimilar($1)$0"
        }
    },
    "system" : {
        "constructors" : {},
        "name" : "System",
        "properties" : ["CalloutException", "Iterator", "InvalidParameterValueException", "BusinessHours", "NoSuchElementException", "LoggingLevel", "System", "XmlTag", "NonePointerException", "WebServiceMock", "TimeZone", "Site", "NoAccessException", "HttpCalloutMock", "Datetime", "TouchHandledException", "String", "DmlException", "Integer", "RestContext", "Map", "JSONGenerator", "XmlException", "ListException", "ApexPages", "ProcedureException", "Cases", "SetupScope", "StringException", "NoDataFoundException", "SerializationException", "JSONToken", "Id", "SearchException", "InvalidReadOnlyUserDmlException", "SchedulableContext", "Cookie", "InvalidHeaderException", "Set", "StatusCode", "CURRENCY", "JSONException", "Database", "AssertException", "EncodingUtil", "Test", "RestRequest", "Boolean", "EmailException", "FinalException", "Date", "UnexpectedException", "Exception", "Schedulable", "Type", "Version", "PageReference", "Long", "Comparable", "Math", "Blob", "Answers", "AppExchange", "Schema", "HandledException", "RequiredFeatureMissingException", "Iterable", "JSON", "HttpResponse", "Time", "MathException", "LimitException", "Communities", "RestResponse", "SelectOption", "SObjectException", "XmlStreamReader", "JSONParser", "MultiStaticResourceCalloutMock", "Double", "SecurityException", "Url", "TypeException", "Network", "FlowException", "Crypto", "List", "Decimal", "SObject", "UnsupportedOperationException", "AsyncException", "Http", "XmlStreamWriter", "Matcher", "StaticResourceCalloutMock", "ApplicationReadWriteMode", "Messaging", "VisualforceException", "QueryException", "LicenseException", "Pattern", "HttpRequest", "Ideas", "UserInfo"],
        "methods" : {
            "debug(ANY o)\tvoid" : "debug($1)$0",
            "abortJob(String jobId)\tvoid" : "abortJob($1)$0",
            "isFuture()\tBoolean" : "isFuture()$0",
            "scheduleBatch(APEX_OBJECT batchable, String jobName, Integer minutesFromNow, Integer scopeSize)\tString" : "scheduleBatch($1)$0",
            "assertNotEquals(ANY expected, ANY actual)\tvoid" : "assertNotEquals($1)$0",
            "purgeOldAsyncJobs(Date date)\tInteger" : "purgeOldAsyncJobs($1)$0",
            "currentPageReference()\tSystem.PageReference" : "currentPageReference()$0",
            "setPassword(Id userId, String password)\tvoid" : "setPassword($1)$0",
            "now()\tDatetime" : "now()$0",
            "assertEquals(ANY expected, ANY actual)\tvoid" : "assertEquals($1)$0",
            "schedule(String jobName, String cronExp, APEX_OBJECT schedulable)\tString" : "schedule($1)$0",
            "isBatch()\tBoolean" : "isBatch()$0",
            "assertNotEquals(ANY expected, ANY actual, ANY msg)\tvoid" : "assertNotEquals($1)$0",
            "process(LIST workitemIds, String action, String commments, String nextApprover)\tLIST<Id>" : "process($1)$0",
            "currentTimeMillis()\tLong" : "currentTimeMillis()$0",
            "runAs(Package.Version version)\tvoid" : "runAs($1)$0",
            "isScheduled()\tBoolean" : "isScheduled()$0",
            "today()\tDate" : "today()$0",
            "scheduleBatch(APEX_OBJECT batchable, String jobName, Integer minutesFromNow)\tString" : "scheduleBatch($1)$0",
            "submit(LIST ids, String commments, String nextApprover)\tLIST<Id>" : "submit($1)$0",
            "resetPassword(Id userId, Boolean sendUserEmail)\tSystem.ResetPasswordResult" : "resetPassword($1)$0",
            "runAs(SObject user, ANY block)\tvoid" : "runAs($1)$0",
            "assert(Boolean condition)\tvoid" : "assert($1)$0",
            "debug(APEX_OBJECT logLevel, ANY o)\tvoid" : "debug($1)$0",
            "assertEquals(ANY expected, ANY actual, ANY msg)\tvoid" : "assertEquals($1)$0",
            "requestVersion()\tsystem.Version" : "requestVersion()$0",
            "assert(Boolean condition, ANY msg)\tvoid" : "assert($1)$0",
            "getApplicationReadWriteMode()\tsystem.ApplicationReadWriteMode" : "getApplicationReadWriteMode()$0"
        }
    },
    "emailtocasehandler" : {
        "constructors" : {},
        "name" : "EmailToCaseHandler",
        "properties" : {},
        "methods" : {}

    },
    "batchablecontext" : {
        "constructors" : {},
        "name" : "BatchableContext",
        "properties" : {},
        "methods" : {
            "getChildJobId()\tId" : "getChildJobId()$0",
            "getJobId()\tId" : "getJobId()$0"
        }
    },
    "unsupportedoperationexception" : {
        "constructors" : {},
        "name" : "UnsupportedOperationException",
        "properties" : {},
        "methods" : {
            "getTypeName()\tString" : "getTypeName()$0"
        }
    },
    "usersettings" : {
        "constructors" : {},
        "name" : "UserSettings",
        "properties" : {
            "approvalPosts" : "approvalPosts$0",
            "userDefaultCurrencyIsoCode" : "userDefaultCurrencyIsoCode$0",
            "hasRestDataApiAccess" : "hasRestDataApiAccess$0",
            "userLocale" : "userLocale$0",
            "fileSyncStorageLimit" : "fileSyncStorageLimit$0",
            "canOwnGroups" : "canOwnGroups$0",
            "canModifyAllData" : "canModifyAllData$0",
            "externalUser" : "externalUser$0",
            "currencySymbol" : "currencySymbol$0",
            "canViewAllData" : "canViewAllData$0",
            "userId" : "userId$0",
            "hasAccessToInternalOrg" : "hasAccessToInternalOrg$0",
            "canViewFullUserProfile" : "canViewFullUserProfile$0",
            "canViewAllUsers" : "canViewAllUsers$0",
            "canFollow" : "canFollow$0",
            "canViewAllGroups" : "canViewAllGroups$0",
            "hasFileSync" : "hasFileSync$0",
            "canViewPublicFiles" : "canViewPublicFiles$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "topicinput" : {
        "constructors" : {},
        "name" : "TopicInput",
        "properties" : {
            "name" : "name$0",
            "description" : "description$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object" : "convertToJavaObject($1)$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "requiredfeaturemissingexception" : {
        "constructors" : {},
        "name" : "RequiredFeatureMissingException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    },
    "sendemailerror" : {
        "constructors" : {},
        "name" : "SendEmailError",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getStatusCode()\tsystem.StatusCode" : "getStatusCode()$0",
            "getTargetObjectId()\tString" : "getTargetObjectId()$0",
            "getFields()\tLIST<String>" : "getFields()$0"
        }
    },
    "groupmembershiprequests" : {
        "constructors" : {},
        "name" : "GroupMembershipRequests",
        "properties" : {
            "total" : "total$0",
            "requests" : "requests$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "fieldsetmember" : {
        "constructors" : {},
        "name" : "FieldSetMember",
        "properties" : {},
        "methods" : {
            "getFieldPath()\tString" : "getFieldPath()$0",
            "getDbRequired()\tBoolean" : "getDbRequired()$0",
            "getType()\tSchema.DisplayType" : "getType()$0",
            "getLabel()\tString" : "getLabel()$0",
            "getRequired()\tBoolean" : "getRequired()$0"
        }
    },
    "livechatrouter" : {
        "constructors" : {},
        "name" : "LiveChatRouter",
        "properties" : {},
        "methods" : {
            "doRouting(LIST<LiveAgent.LiveChatRoutingRequest> param1)\tvoid" : "doRouting($1)$0"
        }
    },
    "reportdatacell" : {
        "constructors" : {},
        "name" : "ReportDataCell",
        "properties" : {},
        "methods" : {
            "getValue()\tObject" : "getValue()$0",
            "setValue(Object value)\tvoid" : "setValue($1)$0",
            "getLabel()\tString" : "getLabel()$0",
            "setLabel(String label)\tvoid" : "setLabel($1)$0"
        }
    },
    "batchablecontextimpl" : {
        "constructors" : {},
        "name" : "BatchableContextImpl",
        "properties" : {},
        "methods" : {
            "getChildJobId()\tId" : "getChildJobId()$0",
            "getJobId()\tId" : "getJobId()$0"
        }
    },
    "user" : {
        "constructors" : {},
        "name" : "User",
        "properties" : {
            "photo" : "photo$0",
            "userType" : "userType$0",
            "lastName" : "lastName$0",
            "title" : "title$0",
            "isInThisCommunity" : "isInThisCommunity$0",
            "companyName" : "companyName$0",
            "firstName" : "firstName$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "sobjectfield" : {
        "constructors" : {},
        "name" : "SObjectField",
        "properties" : {},
        "methods" : {
            "getDescribe()\tSchema.DescribeFieldResult" : "getDescribe()$0"
        }
    },
    "feedpollchoice" : {
        "constructors" : {},
        "name" : "FeedPollChoice",
        "properties" : {
            "position" : "position$0",
            "voteCount" : "voteCount$0",
            "text" : "text$0",
            "id" : "id$0",
            "voteCountRatio" : "voteCountRatio$0"
        },
        "methods" : {
            "getBuildVersion()\tDouble" : "getBuildVersion()$0",
            "toString()\tString" : "toString()$0",
            "hashCode()\tInteger" : "hashCode()$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "hashtagsegmentinput" : {
        "constructors" : {},
        "name" : "HashtagSegmentInput",
        "properties" : {
            "tag" : "tag$0"
        },
        "methods" : {
            "hashCode()\tInteger" : "hashCode()$0",
            "toString()\tString" : "toString()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object" : "convertToJavaObject($1)$0",
            "equals(Object obj)\tBoolean" : "equals($1)$0"
        }
    },
    "stringexception" : {
        "constructors" : {},
        "name" : "StringException",
        "properties" : {},
        "methods" : {
            "getMessage()\tString" : "getMessage()$0",
            "getLineNumber()\tInteger" : "getLineNumber()$0",
            "setMessage(String message)\tvoid" : "setMessage($1)$0",
            "getTypeName()\tString" : "getTypeName()$0",
            "getStackTraceString()\tString" : "getStackTraceString()$0",
            "initCause(APEX_OBJECT cause)\tvoid" : "initCause($1)$0",
            "getCause()\tException" : "getCause()$0"
        }
    }
}
