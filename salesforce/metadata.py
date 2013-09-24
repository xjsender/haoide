apex_completions = {
    "approvalattachment": {
        "name": "ApprovalAttachment",
        "constructors": {},
        "properties": {
            "id": "id$0",
            "status": "status$0",
            "postTemplateFields": "postTemplateFields$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "batchablecontext": {
        "name": "BatchableContext",
        "constructors": {},
        "properties": {},
        "methods": {
            "getChildJobId()\tId": "getChildJobId()$0",
            "getJobId()\tId": "getJobId()$0"
        }
    },
    "schedulable": {
        "name": "Schedulable",
        "constructors": {},
        "properties": {},
        "methods": {
            "execute(system.SchedulableContext param1)\tvoid": "execute($0)"
        }
    },
    "sparkplugdescriberesult": {
        "name": "SparkPlugDescribeResult",
        "constructors": {},
        "properties": {
            "name": "name$0",
            "outputParameters": "outputParameters$0",
            "inputParameters": "inputParameters$0"
        },
        "methods": {}

    },
    "noaccessexception": {
        "name": "NoAccessException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "usersummary": {
        "name": "UserSummary",
        "constructors": {},
        "properties": {
            "isActive": "isActive$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "messagesegmenttype": {
        "name": "MessageSegmentType",
        "constructors": {},
        "properties": {
            "FieldChange": "FieldChange$0",
            "Hashtag": "Hashtag$0",
            "FieldChangeValue": "FieldChangeValue$0",
            "FieldChangeName": "FieldChangeName$0",
            "Text": "Text$0",
            "Mention": "Mention$0",
            "ResourceLink": "ResourceLink$0",
            "Link": "Link$0",
            "EntityLink": "EntityLink$0",
            "MoreChanges": "MoreChanges$0"
        },
        "methods": {
            "values()\tLIST<ConnectApi.MessageSegmentType>": "values()$0"
        }
    },
    "test": {
        "name": "Test",
        "constructors": {},
        "properties": {},
        "methods": {
            "invokePage(System.PageReference p)\tComponent.apex.page": "invokePage($0)",
            "setCurrentPage(Object pageReference)\tvoid": "setCurrentPage($0)",
            "setCurrentPageReference(Object pageReference)\tvoid": "setCurrentPageReference($0)",
            "isRunningTest()\tBoolean": "isRunningTest()$0",
            "testInstall(system.InstallHandler script, system.Version version, Boolean isPush)\tvoid": "testInstall($0)",
            "testUninstall(system.UninstallHandler script)\tvoid": "testUninstall($0)",
            "setMock(system.Type interfaceType, Object mock)\tvoid": "setMock($0)",
            "setFixedSearchResults(LIST<String> searchResultsIds)\tvoid": "setFixedSearchResults($0)",
            "stopTest()\tvoid": "stopTest()$0",
            "startTest()\tvoid": "startTest()$0",
            "loadData(Schema.SObjectType sobjectType, String staticResourceName)\tLIST<SObject>": "loadData($0)",
            "testInstall(system.InstallHandler script, system.Version version)\tvoid": "testInstall($0)",
            "setReadOnlyApplicationMode(Boolean readOnlyApplicationMode)\tvoid": "setReadOnlyApplicationMode($0)"
        }
    },
    "plugin": {
        "name": "Plugin",
        "constructors": {},
        "properties": {},
        "methods": {
            "describe()\tProcess.PluginDescribeResult": "describe()$0",
            "invoke(Process.PluginRequest param1)\tProcess.PluginResult": "invoke($0)"
        }
    },
    "emailtosalesforcehandler": {
        "name": "EmailToSalesforceHandler",
        "constructors": {},
        "properties": {},
        "methods": {}

    },
    "massemailmessage": {
        "name": "MassEmailMessage",
        "constructors": {},
        "properties": {},
        "methods": {}

    },
    "workflowprocessstatus": {
        "name": "WorkflowProcessStatus",
        "constructors": {},
        "properties": {
            "Reassigned": "Reassigned$0",
            "Pending": "Pending$0",
            "Approved": "Approved$0",
            "NoResponse": "NoResponse$0",
            "Removed": "Removed$0",
            "Fault": "Fault$0",
            "Started": "Started$0",
            "Held": "Held$0",
            "Rejected": "Rejected$0"
        },
        "methods": {
            "values()\tLIST<ConnectApi.WorkflowProcessStatus>": "values()$0"
        }
    },
    "photo": {
        "name": "Photo",
        "constructors": {},
        "properties": {
            "fullEmailPhotoUrl": "fullEmailPhotoUrl$0",
            "standardEmailPhotoUrl": "standardEmailPhotoUrl$0",
            "smallPhotoUrl": "smallPhotoUrl$0",
            "largePhotoUrl": "largePhotoUrl$0",
            "url": "url$0",
            "photoVersionId": "photoVersionId$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "casecomment": {
        "name": "CaseComment",
        "constructors": {},
        "properties": {
            "id": "id$0",
            "published": "published$0",
            "createdBy": "createdBy$0",
            "text": "text$0",
            "createdDate": "createdDate$0",
            "actorType": "actorType$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "datacategorygroupsobjecttypepair": {
        "name": "DataCategoryGroupSobjectTypePair",
        "constructors": {},
        "properties": {},
        "methods": {}

    },
    "followingcounts": {
        "name": "FollowingCounts",
        "constructors": {},
        "properties": {
            "total": "total$0",
            "records": "records$0",
            "people": "people$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "groupmembershiprequest": {
        "name": "GroupMembershipRequest",
        "constructors": {},
        "properties": {
            "id": "id$0",
            "lastUpdateDate": "lastUpdateDate$0",
            "user": "user$0",
            "status": "status$0",
            "requestedGroup": "requestedGroup$0",
            "url": "url$0",
            "createdDate": "createdDate$0",
            "responseMessage": "responseMessage$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "groupinformationinput": {
        "name": "GroupInformationInput",
        "constructors": {},
        "properties": {
            "title": "title$0",
            "text": "text$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object": "convertToJavaObject($0)",
            "toString()\tString": "toString()$0"
        }
    },
    "securityexception": {
        "name": "SecurityException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "inboundemail": {
        "name": "InboundEmail",
        "constructors": {},
        "properties": {
            "subject": "subject$0",
            "messageId": "messageId$0",
            "replyTo": "replyTo$0",
            "inReplyTo": "inReplyTo$0",
            "references": "references$0",
            "plainTextBodyIsTruncated": "plainTextBodyIsTruncated$0",
            "htmlBodyIsTruncated": "htmlBodyIsTruncated$0",
            "textAttachments": "textAttachments$0",
            "ccAddresses": "ccAddresses$0",
            "fromName": "fromName$0",
            "binaryAttachments": "binaryAttachments$0",
            "headers": "headers$0",
            "htmlBody": "htmlBody$0",
            "toAddresses": "toAddresses$0",
            "fromAddress": "fromAddress$0",
            "plainTextBody": "plainTextBody$0"
        },
        "methods": {}

    },
    "appexchange": {
        "name": "AppExchange",
        "constructors": {},
        "properties": {},
        "methods": {
            "to18(String id)\tString": "to18($0)",
            "setCookie(String name, String value, String cookieDomainName, Integer cookieAge)\tvoid": "setCookie($0)",
            "getConfig(String section, String key)\tString": "getConfig($0)",
            "setDefaultLicenseTerms(String pkgVersionId, String orgId, String defaultLicenseStatus, Integer defaultLicenseLength, Integer defaultLicenseSeats)\tvoid": "setDefaultLicenseTerms($0)",
            "createOrg(String firstName, String lastName, String companyName, String email, String language, String adminUserName, String packageId, String evalUserName, Boolean isExtension)\tString": "createOrg($0)",
            "setLicenseManagementOrganization(String pkgVersionId, String orgId, String username, String password)\tString": "setLicenseManagementOrganization($0)",
            "getAuthenticatingUrl(String page)\tString": "getAuthenticatingUrl($0)",
            "getSiteId()\tString": "getSiteId()$0",
            "getTrialTemplates(String callerOrgId, String lmPkgId, String username)\tLIST<TrialTemplate>": "getTrialTemplates($0)",
            "provisionPackageLicense(String orgId, String allPackageId, Integer numLicenses, Date expirationDate, String status)\tString": "provisionPackageLicense($0)",
            "getOrgName(String orgId)\tString": "getOrgName($0)",
            "registerPackageVersion(String pkgVersionId)\tBoolean": "registerPackageVersion($0)",
            "setCookie(String name, String value)\tvoid": "setCookie($0)",
            "createPortalUser(SObject user, String accountId)\tId": "createPortalUser($0)",
            "updateSingleAsAdmin(SObject sobj)\tDatabase.SaveResult": "updateSingleAsAdmin($0)",
            "stopListingPopularityJob()\tvoid": "stopListingPopularityJob()$0",
            "getPortalAdminId()\tString": "getPortalAdminId()$0",
            "validateLMAInstalled(String username, String password)\tString": "validateLMAInstalled($0)",
            "movedPermanently(String location)\tvoid": "movedPermanently($0)",
            "getInstalledPackageVersions(String orgId)\tLIST<String>": "getInstalledPackageVersions($0)",
            "getCookie(String name)\tString": "getCookie($0)",
            "debug(String message)\tvoid": "debug($0)",
            "getPackageManifest(String pkgVersionId)\tString": "getPackageManifest($0)",
            "createSession(String appExchangeOrgId, String portalId, String siteId, String portalUserId)\tString": "createSession($0)",
            "calculateListingPopularity(String testUserName, String testCronString)\tvoid": "calculateListingPopularity($0)",
            "setHttpResponseStatus(Integer statusCode)\tvoid": "setHttpResponseStatus($0)",
            "validateOrgUser(String username, String password)\tString": "validateOrgUser($0)",
            "to15(String id)\tString": "to15($0)",
            "getPortalId()\tString": "getPortalId()$0",
            "isGuestUser()\tBoolean": "isGuestUser()$0",
            "getCrossInstanceEncryptedHash(Double appVersion, String value)\tString": "getCrossInstanceEncryptedHash($0)",
            "isDuplicateUserName(String username)\tBoolean": "isDuplicateUserName($0)"
        }
    },
    "feeditemtype": {
        "name": "FeedItemType",
        "constructors": {},
        "properties": {
            "CollaborationGroupUnarchived": "CollaborationGroupUnarchived$0",
            "BasicTemplateFeedItem": "BasicTemplateFeedItem$0",
            "CollaborationGroupCreated": "CollaborationGroupCreated$0",
            "PollPost": "PollPost$0",
            "ApprovalPost": "ApprovalPost$0",
            "CreateRecordEvent": "CreateRecordEvent$0",
            "DashboardComponentAlert": "DashboardComponentAlert$0",
            "DashboardComponentSnapshot": "DashboardComponentSnapshot$0",
            "CaseCommentPost": "CaseCommentPost$0",
            "AttachArticleEvent": "AttachArticleEvent$0",
            "TwitterPost": "TwitterPost$0",
            "CallLogPost": "CallLogPost$0",
            "ChangeStatusPost": "ChangeStatusPost$0",
            "TextPost": "TextPost$0",
            "LinkPost": "LinkPost$0",
            "EmailMessageEvent": "EmailMessageEvent$0",
            "TrackedChange": "TrackedChange$0",
            "RypplePost": "RypplePost$0",
            "UserStatus": "UserStatus$0",
            "ChatTranscriptPost": "ChatTranscriptPost$0",
            "FacebookPost": "FacebookPost$0",
            "ReplyPost": "ReplyPost$0",
            "ActivityEvent": "ActivityEvent$0",
            "ContentPost": "ContentPost$0"
        },
        "methods": {
            "values()\tLIST<ConnectApi.FeedItemType>": "values()$0"
        }
    },
    "sobjecttype": {
        "name": "SObjectType",
        "constructors": {},
        "properties": {},
        "methods": {
            "newSObject(Id id)\tSObject": "newSObject($0)",
            "newSObject()\tSObject": "newSObject()$0",
            "newSObject(Id recordTypeId, Boolean loadDefaultValues)\tSObject": "newSObject($0)",
            "getDescribe()\tSchema.DescribeSObjectResult": "getDescribe()$0"
        }
    },
    "querylocator": {
        "name": "QueryLocator",
        "constructors": {},
        "properties": {},
        "methods": {
            "iterator()\tDatabase.QueryLocatorIterator": "iterator()$0",
            "getQuery()\tString": "getQuery()$0"
        }
    },
    "user": {
        "name": "User",
        "constructors": {},
        "properties": {
            "isInThisCommunity": "isInThisCommunity$0",
            "lastName": "lastName$0",
            "firstName": "firstName$0",
            "title": "title$0",
            "userType": "userType$0",
            "companyName": "companyName$0",
            "photo": "photo$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "nodatafoundexception": {
        "name": "NoDataFoundException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "textsegment": {
        "name": "TextSegment",
        "constructors": {},
        "properties": {},
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "inboundenvelope": {
        "name": "InboundEnvelope",
        "constructors": {},
        "properties": {
            "fromAddress": "fromAddress$0",
            "toAddress": "toAddress$0"
        },
        "methods": {}

    },
    "currency": {
        "name": "CURRENCY",
        "constructors": {},
        "properties": {},
        "methods": {
            "format()\tString": "format()$0",
            "formatAmount()\tString": "formatAmount()$0",
            "newInstance(Decimal amount, String isoCode)\tCURRENCY": "newInstance($0)"
        }
    },
    "fieldchangesegment": {
        "name": "FieldChangeSegment",
        "constructors": {},
        "properties": {},
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "organizationsettings": {
        "name": "OrganizationSettings",
        "constructors": {},
        "properties": {
            "name": "name$0",
            "orgId": "orgId$0",
            "features": "features$0",
            "accessTimeout": "accessTimeout$0",
            "userSettings": "userSettings$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "usertype": {
        "name": "UserType",
        "constructors": {},
        "properties": {
            "ChatterOnly": "ChatterOnly$0",
            "Guest": "Guest$0",
            "ChatterGuest": "ChatterGuest$0",
            "Internal": "Internal$0",
            "Undefined": "Undefined$0",
            "Portal": "Portal$0",
            "System": "System$0"
        },
        "methods": {
            "values()\tLIST<ConnectApi.UserType>": "values()$0"
        }
    },
    "feedfavoritetype": {
        "name": "FeedFavoriteType",
        "constructors": {},
        "properties": {
            "Topic": "Topic$0",
            "ListView": "ListView$0",
            "Search": "Search$0"
        },
        "methods": {
            "values()\tLIST<ConnectApi.FeedFavoriteType>": "values()$0"
        }
    },
    "followingpage": {
        "name": "FollowingPage",
        "constructors": {},
        "properties": {
            "total": "total$0",
            "previousPageUrl": "previousPageUrl$0",
            "currentPageUrl": "currentPageUrl$0",
            "following": "following$0",
            "nextPageUrl": "nextPageUrl$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "motif": {
        "name": "Motif",
        "constructors": {},
        "properties": {
            "smallIconUrl": "smallIconUrl$0",
            "mediumIconUrl": "mediumIconUrl$0",
            "largeIconUrl": "largeIconUrl$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "mobilepushnotification": {
        "name": "MobilePushNotification",
        "constructors": {},
        "properties": {},
        "methods": {
            "setTtl(Integer ttl)\tvoid": "setTtl($0)",
            "setPayload(MAP<String,ANY> payload)\tvoid": "setPayload($0)",
            "send(String application, SET<String> users)\tvoid": "send($0)"
        }
    },
    "followerpage": {
        "name": "FollowerPage",
        "constructors": {},
        "properties": {
            "total": "total$0",
            "previousPageUrl": "previousPageUrl$0",
            "currentPageUrl": "currentPageUrl$0",
            "nextPageUrl": "nextPageUrl$0",
            "followers": "followers$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "contentattachmentinput": {
        "name": "ContentAttachmentInput",
        "constructors": {},
        "properties": {
            "contentDocumentId": "contentDocumentId$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object": "convertToJavaObject($0)",
            "toString()\tString": "toString()$0"
        }
    },
    "pattern": {
        "name": "Pattern",
        "constructors": {},
        "properties": {},
        "methods": {
            "split(String input, Integer n)\tLIST<String>": "split($0)",
            "matcher(String input)\tsystem.Matcher": "matcher($0)",
            "quote(String s)\tString": "quote($0)",
            "matches(String regex, String input)\tBoolean": "matches($0)",
            "compile(String regex)\tsystem.Pattern": "compile($0)",
            "pattern()\tString": "pattern()$0",
            "split(String input)\tLIST<String>": "split($0)"
        }
    },
    "groupvisibilitytype": {
        "name": "GroupVisibilityType",
        "constructors": {},
        "properties": {
            "PublicAccess": "PublicAccess$0",
            "PrivateAccess": "PrivateAccess$0"
        },
        "methods": {
            "values()\tLIST<ConnectApi.GroupVisibilityType>": "values()$0"
        }
    },
    "standardsetcontroller": {
        "name": "StandardSetController",
        "constructors": {},
        "properties": {},
        "methods": {
            "getListViewOptions()\tLIST<System.SelectOption>": "getListViewOptions()$0",
            "addFields(LIST<String> fieldNames)\tvoid": "addFields($0)",
            "next()\tvoid": "next()$0",
            "getRecord()\tSObject": "getRecord()$0",
            "reset()\tvoid": "reset()$0",
            "getFilterId()\tString": "getFilterId()$0",
            "setFilterId(String filterId)\tvoid": "setFilterId($0)",
            "last()\tvoid": "last()$0",
            "setPageSize(Integer pageSize)\tvoid": "setPageSize($0)",
            "getCompleteResult()\tBoolean": "getCompleteResult()$0",
            "cancel()\tSystem.PageReference": "cancel()$0",
            "setPageNumber(Integer pageNumber)\tvoid": "setPageNumber($0)",
            "setSelected(LIST<SObject> selected)\tvoid": "setSelected($0)",
            "getHasPrevious()\tBoolean": "getHasPrevious()$0",
            "first()\tvoid": "first()$0",
            "getPageSize()\tInteger": "getPageSize()$0",
            "getSelected()\tLIST<SObject>": "getSelected()$0",
            "getRecords()\tLIST<SObject>": "getRecords()$0",
            "getPageNumber()\tInteger": "getPageNumber()$0",
            "getResultSize()\tInteger": "getResultSize()$0",
            "getHasNext()\tBoolean": "getHasNext()$0",
            "previous()\tvoid": "previous()$0",
            "save()\tSystem.PageReference": "save()$0"
        }
    },
    "groupmemberpage": {
        "name": "GroupMemberPage",
        "constructors": {},
        "properties": {
            "nextPageUrl": "nextPageUrl$0",
            "myMembership": "myMembership$0",
            "previousPageUrl": "previousPageUrl$0",
            "currentPageUrl": "currentPageUrl$0",
            "totalMemberCount": "totalMemberCount$0",
            "members": "members$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "chattergroupinput": {
        "name": "ChatterGroupInput",
        "constructors": {},
        "properties": {
            "information": "information$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object": "convertToJavaObject($0)",
            "toString()\tString": "toString()$0"
        }
    },
    "fieldchangenamesegment": {
        "name": "FieldChangeNameSegment",
        "constructors": {},
        "properties": {},
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "map": {
        "name": "Map",
        "constructors": {},
        "properties": {},
        "methods": {
            "isEmpty()\tBoolean": "isEmpty()$0",
            "size()\tInteger": "size()$0",
            "values()\tLIST<String>": "values()$0",
            "containsKey(ANY key)\tBoolean": "containsKey($0)",
            "put(ANY key, ANY value)\tString": "put($0)",
            "getSObjectType()\tSchema.SObjectType": "getSObjectType()$0",
            "deepClone()\tMAP<String,String>": "deepClone()$0",
            "keySet()\tSET<String>": "keySet()$0",
            "clone()\tMAP<String,String>": "clone()$0",
            "get(ANY key)\tString": "get($0)",
            "putAll(MAP entries)\tvoid": "putAll($0)",
            "clear()\tvoid": "clear()$0",
            "remove(ANY key)\tString": "remove($0)",
            "putAll(LIST entries)\tvoid": "putAll($0)"
        }
    },
    "features": {
        "name": "Features",
        "constructors": {},
        "properties": {
            "chatterGlobalInfluence": "chatterGlobalInfluence$0",
            "chatterMessages": "chatterMessages$0",
            "publisherActions": "publisherActions$0",
            "defaultCurrencyIsoCode": "defaultCurrencyIsoCode$0",
            "chatter": "chatter$0",
            "dashboardComponentSnapshots": "dashboardComponentSnapshots$0",
            "chatterActivity": "chatterActivity$0",
            "filesOnComments": "filesOnComments$0",
            "files": "files$0",
            "feedPolling": "feedPolling$0",
            "viralInvitesAllowed": "viralInvitesAllowed$0",
            "trendingTopics": "trendingTopics$0",
            "groupsCanFollow": "groupsCanFollow$0",
            "thanksAllowed": "thanksAllowed$0",
            "multiCurrency": "multiCurrency$0",
            "chatterTopics": "chatterTopics$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "visualforceexception": {
        "name": "VisualforceException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "setupscope": {
        "name": "SetupScope",
        "constructors": {},
        "properties": {
            "ORGANIZATION": "ORGANIZATION$0",
            "USER": "USER$0",
            "PROFILE": "PROFILE$0"
        },
        "methods": {
            "values()\tLIST<system.SetupScope>": "values()$0"
        }
    },
    "chatter": {
        "name": "Chatter",
        "constructors": {},
        "properties": {},
        "methods": {
            "deleteSubscription(String communityId, String subscriptionId)\tvoid": "deleteSubscription($0)",
            "getSubscription(String communityId, String subscriptionId)\tConnectApi.Subscription": "getSubscription($0)",
            "getFollowers(String communityId, String recordId)\tConnectApi.FollowerPage": "getFollowers($0)",
            "getFollowers(String communityId, String recordId, Integer pageParam, Integer pageSize)\tConnectApi.FollowerPage": "getFollowers($0)"
        }
    },
    "searchexception": {
        "name": "SearchException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "cases": {
        "name": "Cases",
        "constructors": {},
        "properties": {},
        "methods": {
            "getCaseIdFromEmailThreadId(String emailThreadId)\tId": "getCaseIdFromEmailThreadId($0)"
        }
    },
    "sobject": {
        "name": "SObject",
        "constructors": {},
        "properties": {},
        "methods": {
            "put(String field, Object value)\tObject": "put($0)",
            "putSObject(String field, SObject value)\tSObject": "putSObject($0)",
            "getOptions()\tDatabase.DMLOptions": "getOptions()$0",
            "getSObjects(String field)\tLIST<SObject>": "getSObjects($0)",
            "clone(Boolean preserveId, Boolean deep)\tSObject": "clone($0)",
            "clone(Boolean preserveId)\tSObject": "clone($0)",
            "getSObjects(Schema.SObjectField field)\tLIST<SObject>": "getSObjects($0)",
            "clone(Boolean preserveId, Boolean deep, Boolean preserveReadOnlyTimestamps)\tSObject": "clone($0)",
            "putSObject(Schema.SObjectField field, SObject value)\tSObject": "putSObject($0)",
            "get(String field)\tObject": "get($0)",
            "addError(String msg, Boolean escape)\tvoid": "addError($0)",
            "put(Schema.SObjectField field, Object value)\tObject": "put($0)",
            "clone()\tSObject": "clone()$0",
            "getSObject(String field)\tSObject": "getSObject($0)",
            "get(Schema.SObjectField field)\tObject": "get($0)",
            "getSObjectType()\tSchema.SObjectType": "getSObjectType()$0",
            "addError(APEX_OBJECT msg)\tvoid": "addError($0)",
            "addError(APEX_OBJECT msg, Boolean escape)\tvoid": "addError($0)",
            "clone(Boolean preserveId, Boolean deep, Boolean preserveReadOnlyTimestamps, Boolean preserveAutoNumbers)\tSObject": "clone($0)",
            "getSObject(Schema.SObjectField field)\tSObject": "getSObject($0)",
            "getQuickActionName()\tString": "getQuickActionName()$0",
            "clear()\tvoid": "clear()$0",
            "addError(String msg)\tvoid": "addError($0)",
            "setOptions(APEX_OBJECT options)\tvoid": "setOptions($0)"
        }
    },
    "userchattersettings": {
        "name": "UserChatterSettings",
        "constructors": {},
        "properties": {
            "defaultGroupEmailFrequency": "defaultGroupEmailFrequency$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "boolean": {
        "name": "Boolean",
        "constructors": {},
        "properties": {},
        "methods": {
            "addError(String msg, Boolean escape)\tvoid": "addError($0)",
            "valueOf(Object a)\tBoolean": "valueOf($0)",
            "addError(APEX_OBJECT msg, Boolean escape)\tvoid": "addError($0)",
            "addError(String msg)\tvoid": "addError($0)",
            "addError(APEX_OBJECT msg)\tvoid": "addError($0)"
        }
    },
    "serializationexception": {
        "name": "SerializationException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "httprequest": {
        "name": "HttpRequest",
        "constructors": {},
        "properties": {},
        "methods": {
            "setMethod(String method)\tvoid": "setMethod($0)",
            "getBodyDocument()\tdom.Document": "getBodyDocument()$0",
            "getMethod()\tString": "getMethod()$0",
            "getBody()\tString": "getBody()$0",
            "toString()\tString": "toString()$0",
            "setClientCertificate(String clientCert, String password)\tvoid": "setClientCertificate($0)",
            "getEndpoint()\tString": "getEndpoint()$0",
            "setBodyDocument(ANY body)\tvoid": "setBodyDocument($0)",
            "getBodyAsBlob()\tBlob": "getBodyAsBlob()$0",
            "setClientCertificateName(String certDevName)\tvoid": "setClientCertificateName($0)",
            "getCompressed()\tBoolean": "getCompressed()$0",
            "setBodyAsBlob(Blob body)\tvoid": "setBodyAsBlob($0)",
            "setTimeout(Integer timeout)\tvoid": "setTimeout($0)",
            "getHeader(String key)\tString": "getHeader($0)",
            "setCompressed(Boolean compressed)\tvoid": "setCompressed($0)",
            "setHeader(String key, String value)\tvoid": "setHeader($0)",
            "setBody(String body)\tvoid": "setBody($0)",
            "setEndpoint(String endpoint)\tvoid": "setEndpoint($0)"
        }
    },
    "string": {
        "name": "String",
        "constructors": {},
        "properties": {},
        "methods": {
            "indexOf(String str, Integer startPos)\tInteger": "indexOf($0)",
            "indexOfAnyBut(String searchChars)\tInteger": "indexOfAnyBut($0)",
            "endsWithIgnoreCase(String suffix)\tBoolean": "endsWithIgnoreCase($0)",
            "removeStartIgnoreCase(String toRemove)\tString": "removeStartIgnoreCase($0)",
            "repeat(Integer numTimes)\tString": "repeat($0)",
            "isAllUpperCase()\tBoolean": "isAllUpperCase()$0",
            "isAlphanumeric()\tBoolean": "isAlphanumeric()$0",
            "unescapeXml()\tString": "unescapeXml()$0",
            "removeEndIgnoreCase(String toRemove)\tString": "removeEndIgnoreCase($0)",
            "unescapeHtml4()\tString": "unescapeHtml4()$0",
            "toUpperCase(String locale)\tString": "toUpperCase($0)",
            "escapeHtml4()\tString": "escapeHtml4()$0",
            "getCommonPrefix(LIST strings)\tString": "getCommonPrefix($0)",
            "unescapeHtml3()\tString": "unescapeHtml3()$0",
            "replace(String target, String replacement)\tString": "replace($0)",
            "join(APEX_OBJECT iterableObj, String separator)\tString": "join($0)",
            "remove(String toRemove)\tString": "remove($0)",
            "abbreviate(Integer maxWidth, Integer offset)\tString": "abbreviate($0)",
            "left(Integer len)\tString": "left($0)",
            "equals(String other)\tBoolean": "equals($0)",
            "mid(Integer pos, Integer len)\tString": "mid($0)",
            "equalsIgnoreCase(String other)\tBoolean": "equalsIgnoreCase($0)",
            "isEmpty(String str)\tBoolean": "isEmpty($0)",
            "indexOfDifference(String other)\tInteger": "indexOfDifference($0)",
            "isNumeric()\tBoolean": "isNumeric()$0",
            "indexOf(String str)\tInteger": "indexOf($0)",
            "valueOf(Double d)\tString": "valueOf($0)",
            "stripHtmlTags()\tString": "stripHtmlTags()$0",
            "substringAfterLast(String separator)\tString": "substringAfterLast($0)",
            "substringBefore(String separator)\tString": "substringBefore($0)",
            "lastIndexOfIgnoreCase(String searchStr)\tInteger": "lastIndexOfIgnoreCase($0)",
            "valueOf(Integer i)\tString": "valueOf($0)",
            "substring(Integer start)\tString": "substring($0)",
            "valueOf(Object o)\tString": "valueOf($0)",
            "capitalize()\tString": "capitalize()$0",
            "containsAny(String validChars)\tBoolean": "containsAny($0)",
            "split(String regex)\tLIST<String>": "split($0)",
            "center(Integer size)\tString": "center($0)",
            "isNotBlank(String str)\tBoolean": "isNotBlank($0)",
            "escapeXml()\tString": "escapeXml()$0",
            "valueOf(Decimal d)\tString": "valueOf($0)",
            "repeat(String separator, Integer numTimes)\tString": "repeat($0)",
            "containsOnly(String validChars)\tBoolean": "containsOnly($0)",
            "swapCase()\tString": "swapCase()$0",
            "indexOfIgnoreCase(String searchStr, Integer startPos)\tInteger": "indexOfIgnoreCase($0)",
            "contains(String str)\tBoolean": "contains($0)",
            "valueOf(Date d)\tString": "valueOf($0)",
            "split(String regex, Integer limit)\tLIST<String>": "split($0)",
            "isNotEmpty(String str)\tBoolean": "isNotEmpty($0)",
            "addError(APEX_OBJECT msg)\tvoid": "addError($0)",
            "leftPad(Integer len)\tString": "leftPad($0)",
            "countMatches(String searchStr)\tInteger": "countMatches($0)",
            "normalizeSpace()\tString": "normalizeSpace()$0",
            "indexOfIgnoreCase(String searchStr)\tInteger": "indexOfIgnoreCase($0)",
            "isAlphanumericSpace()\tBoolean": "isAlphanumericSpace()$0",
            "length()\tInteger": "length()$0",
            "replaceFirst(String regex, String replacement)\tString": "replaceFirst($0)",
            "substringAfter(String separator)\tString": "substringAfter($0)",
            "fromCharArray(LIST<Integer> charArr)\tString": "fromCharArray($0)",
            "addError(String msg)\tvoid": "addError($0)",
            "toUpperCase()\tString": "toUpperCase()$0",
            "containsIgnoreCase(String searchStr)\tBoolean": "containsIgnoreCase($0)",
            "deleteWhitespace()\tString": "deleteWhitespace()$0",
            "endsWith(String str)\tBoolean": "endsWith($0)",
            "containsNone(String invalidChars)\tBoolean": "containsNone($0)",
            "addError(String msg, Boolean escape)\tvoid": "addError($0)",
            "escapeSingleQuotes(String s)\tString": "escapeSingleQuotes($0)",
            "rightPad(Integer len)\tString": "rightPad($0)",
            "isAsciiPrintable()\tBoolean": "isAsciiPrintable()$0",
            "indexOfAny(String searchChars)\tInteger": "indexOfAny($0)",
            "reverse()\tString": "reverse()$0",
            "center(Integer size, String padStr)\tString": "center($0)",
            "toLowerCase()\tString": "toLowerCase()$0",
            "trim()\tString": "trim()$0",
            "substringBeforeLast(String separator)\tString": "substringBeforeLast($0)",
            "lastIndexOf(String searchStr, Integer startPos)\tInteger": "lastIndexOf($0)",
            "lastIndexOf(String str)\tInteger": "lastIndexOf($0)",
            "uncapitalize()\tString": "uncapitalize()$0",
            "hashCode()\tInteger": "hashCode()$0",
            "right(Integer len)\tString": "right($0)",
            "substringBetween(String tag)\tString": "substringBetween($0)",
            "valueOf(Long l)\tString": "valueOf($0)",
            "overlay(String overlay, Integer start, Integer end)\tString": "overlay($0)",
            "containsWhitespace()\tBoolean": "containsWhitespace()$0",
            "isAllLowerCase()\tBoolean": "isAllLowerCase()$0",
            "substring(Integer start, Integer end)\tString": "substring($0)",
            "isBlank(String str)\tBoolean": "isBlank($0)",
            "substringBetween(String open, String close)\tString": "substringBetween($0)",
            "lastIndexOfIgnoreCase(String searchStr, Integer startPos)\tInteger": "lastIndexOfIgnoreCase($0)",
            "startsWithIgnoreCase(String prefix)\tBoolean": "startsWithIgnoreCase($0)",
            "difference(String other)\tString": "difference($0)",
            "unescapeEcmaScript()\tString": "unescapeEcmaScript()$0",
            "escapeEcmaScript()\tString": "escapeEcmaScript()$0",
            "escapeHtml3()\tString": "escapeHtml3()$0",
            "rightPad(Integer len, String padStr)\tString": "rightPad($0)",
            "startsWith(String str)\tBoolean": "startsWith($0)",
            "splitByCharacterTypeCamelCase()\tLIST<String>": "splitByCharacterTypeCamelCase()$0",
            "getLevenshteinDistance(String other, Integer threshold)\tInteger": "getLevenshteinDistance($0)",
            "format(String format, LIST<String> arguments)\tString": "format($0)",
            "removeEnd(String toRemove)\tString": "removeEnd($0)",
            "isWhitespace()\tBoolean": "isWhitespace()$0",
            "splitByCharacterType()\tLIST<String>": "splitByCharacterType()$0",
            "leftPad(Integer len, String padStr)\tString": "leftPad($0)",
            "valueOf(Datetime dt)\tString": "valueOf($0)",
            "abbreviate(Integer maxWidth)\tString": "abbreviate($0)",
            "toLowerCase(String locale)\tString": "toLowerCase($0)",
            "isNumericSpace()\tBoolean": "isNumericSpace()$0",
            "valueOfGmt(Datetime dt)\tString": "valueOfGmt($0)",
            "removeStart(String toRemove)\tString": "removeStart($0)",
            "getLevenshteinDistance(String other)\tInteger": "getLevenshteinDistance($0)",
            "isAlpha()\tBoolean": "isAlpha()$0",
            "unescapeCsv()\tString": "unescapeCsv()$0",
            "addError(APEX_OBJECT msg, Boolean escape)\tvoid": "addError($0)",
            "isAlphaSpace()\tBoolean": "isAlphaSpace()$0",
            "escapeCsv()\tString": "escapeCsv()$0",
            "compareTo(String str)\tInteger": "compareTo($0)",
            "replaceAll(String regex, String replacement)\tString": "replaceAll($0)"
        }
    },
    "feedbody": {
        "name": "FeedBody",
        "constructors": {},
        "properties": {},
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "organization": {
        "name": "Organization",
        "constructors": {},
        "properties": {},
        "methods": {
            "getSettings()\tConnectApi.OrganizationSettings": "getSettings()$0"
        }
    },
    "community": {
        "name": "Community",
        "constructors": {},
        "properties": {
            "id": "id$0",
            "description": "description$0",
            "name": "name$0",
            "urlPathPrefix": "urlPathPrefix$0",
            "status": "status$0",
            "url": "url$0",
            "invitationsEnabled": "invitationsEnabled$0",
            "sendWelcomeEmail": "sendWelcomeEmail$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "feedpoll": {
        "name": "FeedPoll",
        "constructors": {},
        "properties": {
            "choices": "choices$0",
            "totalVoteCount": "totalVoteCount$0",
            "myChoiceId": "myChoiceId$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "approvalposttemplatefield": {
        "name": "ApprovalPostTemplateField",
        "constructors": {},
        "properties": {
            "displayValue": "displayValue$0",
            "record": "record$0",
            "displayName": "displayName$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "pollattachmentinput": {
        "name": "PollAttachmentInput",
        "constructors": {},
        "properties": {
            "pollChoices": "pollChoices$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object": "convertToJavaObject($0)",
            "toString()\tString": "toString()$0"
        }
    },
    "httpresponse": {
        "name": "HttpResponse",
        "constructors": {},
        "properties": {},
        "methods": {
            "getStatus()\tString": "getStatus()$0",
            "getBodyDocument()\tdom.Document": "getBodyDocument()$0",
            "setStatusCode(Integer statusCode)\tvoid": "setStatusCode($0)",
            "getBody()\tString": "getBody()$0",
            "getStatusCode()\tInteger": "getStatusCode()$0",
            "toString()\tString": "toString()$0",
            "getBodyAsBlob()\tBlob": "getBodyAsBlob()$0",
            "setBodyAsBlob(Blob body)\tvoid": "setBodyAsBlob($0)",
            "getHeader(String key)\tString": "getHeader($0)",
            "getXmlStreamReader()\tSystem.XmlStreamReader": "getXmlStreamReader()$0",
            "getHeaderKeys()\tLIST<String>": "getHeaderKeys()$0",
            "setHeader(String key, String value)\tvoid": "setHeader($0)",
            "setBody(String body)\tvoid": "setBody($0)",
            "setStatus(String status)\tvoid": "setStatus($0)"
        }
    },
    "linksegment": {
        "name": "LinkSegment",
        "constructors": {},
        "properties": {
            "url": "url$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "globalinfluence": {
        "name": "GlobalInfluence",
        "constructors": {},
        "properties": {
            "percentile": "percentile$0",
            "rank": "rank$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "interview": {
        "name": "Interview",
        "constructors": {},
        "properties": {},
        "methods": {
            "getVariableValue(String param1)\tObject": "getVariableValue($0)"
        }
    },
    "http": {
        "name": "Http",
        "constructors": {},
        "properties": {},
        "methods": {
            "toString()\tString": "toString()$0",
            "send(ANY request)\tSystem.HttpResponse": "send($0)"
        }
    },
    "restresponse": {
        "name": "RestResponse",
        "constructors": {},
        "properties": {
            "responseBody": "responseBody$0",
            "statusCode": "statusCode$0",
            "headers": "headers$0"
        },
        "methods": {
            "addHeader(String name, String value)\tvoid": "addHeader($0)"
        }
    },
    "commentpage": {
        "name": "CommentPage",
        "constructors": {},
        "properties": {
            "total": "total$0",
            "nextPageUrl": "nextPageUrl$0",
            "nextPageToken": "nextPageToken$0",
            "currentPageToken": "currentPageToken$0",
            "currentPageUrl": "currentPageUrl$0",
            "comments": "comments$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "parametertype": {
        "name": "ParameterType",
        "constructors": {},
        "properties": {
            "BOOLEAN": "BOOLEAN$0",
            "ID": "ID$0",
            "DATETIME": "DATETIME$0",
            "DATE": "DATE$0",
            "FLOAT": "FLOAT$0",
            "DECIMAL": "DECIMAL$0",
            "DOUBLE": "DOUBLE$0",
            "INTEGER": "INTEGER$0",
            "STRING": "STRING$0",
            "LONG": "LONG$0"
        },
        "methods": {
            "values()\tLIST<Process.PluginDescribeResult.ParameterType>": "values()$0"
        }
    },
    "actorwithid": {
        "name": "ActorWithId",
        "constructors": {},
        "properties": {
            "id": "id$0",
            "url": "url$0",
            "mySubscription": "mySubscription$0",
            "motif": "motif$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "xmlnode": {
        "name": "XmlNode",
        "constructors": {},
        "properties": {},
        "methods": {
            "addCommentNode(String text)\tdom.XmlNode": "addCommentNode($0)",
            "getChildElements()\tLIST<dom.XmlNode>": "getChildElements()$0",
            "getAttributeCount()\tInteger": "getAttributeCount()$0",
            "addTextNode(String text)\tdom.XmlNode": "addTextNode($0)",
            "setNamespace(String prefix, String namespace)\tvoid": "setNamespace($0)",
            "getNamespace()\tString": "getNamespace()$0",
            "getAttributeValueNs(String key, String keyNamespace)\tString": "getAttributeValueNs($0)",
            "getAttributeValue(String key, String keyNamespace)\tString": "getAttributeValue($0)",
            "getAttributeKeyAt(Integer index)\tString": "getAttributeKeyAt($0)",
            "removeAttribute(String key, String keyNamespace)\tBoolean": "removeAttribute($0)",
            "getPrefixFor(String namespace)\tString": "getPrefixFor($0)",
            "getText()\tString": "getText()$0",
            "getChildren()\tLIST<dom.XmlNode>": "getChildren()$0",
            "getName()\tString": "getName()$0",
            "getChildElement(String name, String namespace)\tdom.XmlNode": "getChildElement($0)",
            "getParent()\tdom.XmlNode": "getParent()$0",
            "getAttribute(String key, String keyNamespace)\tString": "getAttribute($0)",
            "setAttributeNs(String key, String value, String keyNamespace, String valueNamespace)\tvoid": "setAttributeNs($0)",
            "setAttribute(String key, String value)\tvoid": "setAttribute($0)",
            "getNamespaceFor(String prefix)\tString": "getNamespaceFor($0)",
            "getAttributeKeyNsAt(Integer index)\tString": "getAttributeKeyNsAt($0)",
            "removeChild(ANY child)\tBoolean": "removeChild($0)",
            "getNodeType()\tDom.XmlNodeType": "getNodeType()$0",
            "addChildElement(String name, String namespace, String prefix)\tdom.XmlNode": "addChildElement($0)"
        }
    },
    "connectapiexception": {
        "name": "ConnectApiException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getErrorCode()\tString": "getErrorCode()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "iterator": {
        "name": "Iterator",
        "constructors": {},
        "properties": {},
        "methods": {
            "next()\tObject": "next()$0",
            "hasNext()\tBoolean": "hasNext()$0"
        }
    },
    "action": {
        "name": "Action",
        "constructors": {},
        "properties": {},
        "methods": {
            "getExpression()\tString": "getExpression()$0",
            "invoke()\tSystem.PageReference": "invoke()$0"
        }
    },
    "chatterfavorites": {
        "name": "ChatterFavorites",
        "constructors": {},
        "properties": {},
        "methods": {
            "getFeedItems(String communityId, String subjectId, String favoriteId)\tConnectApi.FeedItemPage": "getFeedItems($0)",
            "getFavorite(String communityId, String subjectId, String favoriteId)\tConnectApi.FeedFavorite": "getFavorite($0)",
            "getFavorites(String communityId, String subjectId)\tConnectApi.FeedFavorites": "getFavorites($0)",
            "deleteFavorite(String communityId, String subjectId, String favoriteId)\tvoid": "deleteFavorite($0)",
            "setTestGetFeedItems(String communityId, String subjectId, String favoriteId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)\tvoid": "setTestGetFeedItems($0)",
            "setTestGetFeedItems(String communityId, String subjectId, String favoriteId, ConnectApi.FeedItemPage result)\tvoid": "setTestGetFeedItems($0)",
            "addFavorite(String communityId, String subjectId, String searchText)\tConnectApi.FeedFavorite": "addFavorite($0)",
            "addRecordFavorite(String communityId, String subjectId, String targetId)\tConnectApi.FeedFavorite": "addRecordFavorite($0)",
            "updateFavorite(String communityId, String subjectId, String favoriteId, Boolean updateLastViewDate)\tConnectApi.FeedFavorite": "updateFavorite($0)",
            "getFeedItems(String communityId, String subjectId, String favoriteId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)\tConnectApi.FeedItemPage": "getFeedItems($0)"
        }
    },
    "usergrouppage": {
        "name": "UserGroupPage",
        "constructors": {},
        "properties": {
            "total": "total$0",
            "previousPageUrl": "previousPageUrl$0",
            "currentPageUrl": "currentPageUrl$0",
            "groups": "groups$0",
            "nextPageUrl": "nextPageUrl$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "cookie": {
        "name": "Cookie",
        "constructors": {},
        "properties": {},
        "methods": {
            "getDomain()\tString": "getDomain()$0",
            "getName()\tString": "getName()$0",
            "getValue()\tString": "getValue()$0",
            "getMaxAge()\tInteger": "getMaxAge()$0",
            "isSecure()\tBoolean": "isSecure()$0",
            "getPath()\tString": "getPath()$0"
        }
    },
    "jsontoken": {
        "name": "JSONToken",
        "constructors": {},
        "properties": {
            "VALUE_EMBEDDED_OBJECT": "VALUE_EMBEDDED_OBJECT$0",
            "VALUE_TRUE": "VALUE_TRUE$0",
            "START_OBJECT": "START_OBJECT$0",
            "START_ARRAY": "START_ARRAY$0",
            "VALUE_STRING": "VALUE_STRING$0",
            "VALUE_None": "VALUE_None$0",
            "END_OBJECT": "END_OBJECT$0",
            "NOT_AVAILABLE": "NOT_AVAILABLE$0",
            "VALUE_NUMBER_INT": "VALUE_NUMBER_INT$0",
            "END_ARRAY": "END_ARRAY$0",
            "FIELD_NAME": "FIELD_NAME$0",
            "VALUE_NUMBER_FLOAT": "VALUE_NUMBER_FLOAT$0",
            "VALUE_FALSE": "VALUE_FALSE$0"
        },
        "methods": {
            "values()\tLIST<system.JSONToken>": "values()$0"
        }
    },
    "procedureexception": {
        "name": "ProcedureException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "staticresourcecalloutmock": {
        "name": "StaticResourceCalloutMock",
        "constructors": {},
        "properties": {},
        "methods": {
            "setHeader(String key, String val)\tvoid": "setHeader($0)",
            "setStatusCode(Integer code)\tvoid": "setStatusCode($0)",
            "respond(System.HttpRequest request)\tSystem.HttpResponse": "respond($0)",
            "setStaticResource(String staticResourceName)\tvoid": "setStaticResource($0)",
            "setStatus(String status)\tvoid": "setStatus($0)"
        }
    },
    "displaytype": {
        "name": "DisplayType",
        "constructors": {},
        "properties": {
            "ANYTYPE": "ANYTYPE$0",
            "PERCENT": "PERCENT$0",
            "DATE": "DATE$0",
            "MULTIPICKLIST": "MULTIPICKLIST$0",
            "EMAIL": "EMAIL$0",
            "PHONE": "PHONE$0",
            "PICKLIST": "PICKLIST$0",
            "DATACATEGORYGROUPREFERENCE": "DATACATEGORYGROUPREFERENCE$0",
            "INTEGER": "INTEGER$0",
            "TEXTAREA": "TEXTAREA$0",
            "STRING": "STRING$0",
            "REFERENCE": "REFERENCE$0",
            "ENCRYPTEDSTRING": "ENCRYPTEDSTRING$0",
            "BOOLEAN": "BOOLEAN$0",
            "BASE64": "BASE64$0",
            "CURRENCY": "CURRENCY$0",
            "DOUBLE": "DOUBLE$0",
            "URL": "URL$0",
            "TIME": "TIME$0",
            "ID": "ID$0",
            "LOCATION": "LOCATION$0",
            "DATETIME": "DATETIME$0",
            "COMBOBOX": "COMBOBOX$0",
            "COMPLEXVALUE": "COMPLEXVALUE$0"
        },
        "methods": {
            "values()\tLIST<Schema.DisplayType>": "values()$0"
        }
    },
    "xmlnodetype": {
        "name": "XmlNodeType",
        "constructors": {},
        "properties": {
            "ELEMENT": "ELEMENT$0",
            "TEXT": "TEXT$0",
            "COMMENT": "COMMENT$0"
        },
        "methods": {
            "values()\tLIST<Dom.XmlNodeType>": "values()$0"
        }
    },
    "soaptype": {
        "name": "SoapType",
        "constructors": {},
        "properties": {
            "METADATA_CUSTOMFIELD": "METADATA_CUSTOMFIELD$0",
            "ID": "ID$0",
            "INTEGER": "INTEGER$0",
            "METADATA_APEXTRIGGER": "METADATA_APEXTRIGGER$0",
            "TIME": "TIME$0",
            "DATE": "DATE$0",
            "EXECUTIONOVERLAY_SOQLRESULT": "EXECUTIONOVERLAY_SOQLRESULT$0",
            "SYMBOLTABLE": "SYMBOLTABLE$0",
            "STRING": "STRING$0",
            "ANYTYPE": "ANYTYPE$0",
            "BASE64BINARY": "BASE64BINARY$0",
            "BOOLEAN": "BOOLEAN$0",
            "DATETIME": "DATETIME$0",
            "METADATA_CUSTOMOBJECT": "METADATA_CUSTOMOBJECT$0",
            "METADATA_APEXCOMPONENT": "METADATA_APEXCOMPONENT$0",
            "METADATA_APEXCLASS": "METADATA_APEXCLASS$0",
            "EXECUTIONOVERLAY_APEXRESULT": "EXECUTIONOVERLAY_APEXRESULT$0",
            "EXECUTIONOVERLAY_HEAPDUMP": "EXECUTIONOVERLAY_HEAPDUMP$0",
            "DOUBLE": "DOUBLE$0",
            "METADATA_APEXPAGE": "METADATA_APEXPAGE$0"
        },
        "methods": {
            "values()\tLIST<Schema.SoapType>": "values()$0"
        }
    },
    "businesshours": {
        "name": "BusinessHours",
        "constructors": {},
        "properties": {},
        "methods": {
            "addGmt(Id businessHoursId, Datetime startDate, Long interval)\tDatetime": "addGmt($0)",
            "add(Id businessHoursId, Datetime startDate, Long interval)\tDatetime": "add($0)",
            "diff(String businessHoursId, Datetime startDate, Datetime endDate)\tLong": "diff($0)"
        }
    },
    "knowledgearticleversionstandardcontroller": {
        "name": "KnowledgeArticleVersionStandardController",
        "constructors": {},
        "properties": {},
        "methods": {
            "getSourceId()\tString": "getSourceId()$0",
            "cancel()\tSystem.PageReference": "cancel()$0",
            "view()\tSystem.PageReference": "view()$0",
            "edit()\tSystem.PageReference": "edit()$0",
            "addFields(LIST<String> fieldNames)\tvoid": "addFields($0)",
            "getSubject()\tSObject": "getSubject()$0",
            "getRecord()\tSObject": "getRecord()$0",
            "reset()\tvoid": "reset()$0",
            "selectDataCategory(String categoryGroup, String category)\tvoid": "selectDataCategory($0)",
            "delete()\tSystem.PageReference": "delete()$0",
            "getId()\tString": "getId()$0",
            "save()\tSystem.PageReference": "save()$0"
        }
    },
    "chattergroup": {
        "name": "ChatterGroup",
        "constructors": {},
        "properties": {
            "community": "community$0",
            "description": "description$0",
            "owner": "owner$0",
            "photo": "photo$0",
            "memberCount": "memberCount$0",
            "emailToChatterAddress": "emailToChatterAddress$0",
            "myRole": "myRole$0",
            "visibility": "visibility$0",
            "canHaveChatterGuests": "canHaveChatterGuests$0",
            "lastFeedItemPostDate": "lastFeedItemPostDate$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "json": {
        "name": "JSON",
        "constructors": {},
        "properties": {},
        "methods": {
            "createGenerator(Boolean pretty)\tsystem.JSONGenerator": "createGenerator($0)",
            "createParser(String jsonString)\tsystem.JSONParser": "createParser($0)",
            "serializePretty(Object o)\tString": "serializePretty($0)",
            "serialize(Object o)\tString": "serialize($0)",
            "deserializeUntyped(String jsonString)\tObject": "deserializeUntyped($0)",
            "deserializeStrict(String jsonString, system.Type apexType)\tObject": "deserializeStrict($0)",
            "deserialize(String jsonString, system.Type apexType)\tObject": "deserialize($0)"
        }
    },
    "feedfavorites": {
        "name": "FeedFavorites",
        "constructors": {},
        "properties": {
            "total": "total$0",
            "favorites": "favorites$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "chattergroupdetail": {
        "name": "ChatterGroupDetail",
        "constructors": {},
        "properties": {
            "fileCount": "fileCount$0",
            "information": "information$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "comparable": {
        "name": "Comparable",
        "constructors": {},
        "properties": {},
        "methods": {
            "compareTo(Object param1)\tInteger": "compareTo($0)"
        }
    },
    "notfoundexception": {
        "name": "NotFoundException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "plugindescriberesult": {
        "name": "PluginDescribeResult",
        "constructors": {},
        "properties": {
            "tag": "tag$0",
            "name": "name$0",
            "description": "description$0",
            "inputParameters": "inputParameters$0",
            "outputParameters": "outputParameters$0"
        },
        "methods": {}

    },
    "timezone": {
        "name": "TimeZone",
        "constructors": {},
        "properties": {},
        "methods": {
            "getOffset(Datetime dt)\tInteger": "getOffset($0)",
            "getID()\tString": "getID()$0",
            "getDisplayName()\tString": "getDisplayName()$0",
            "getTimeZone(String id)\tsystem.TimeZone": "getTimeZone($0)",
            "toString()\tString": "toString()$0"
        }
    },
    "abstractmessagebody": {
        "name": "AbstractMessageBody",
        "constructors": {},
        "properties": {
            "messageSegments": "messageSegments$0",
            "text": "text$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "emailtocasehandler": {
        "name": "EmailToCaseHandler",
        "constructors": {},
        "properties": {},
        "methods": {}

    },
    "assignmentruleheader": {
        "name": "AssignmentRuleHeader",
        "constructors": {},
        "properties": {
            "UseDefaultRule": "UseDefaultRule$0",
            "AssignmentRuleId": "AssignmentRuleId$0"
        },
        "methods": {}

    },
    "feedmodifiedinfo": {
        "name": "FeedModifiedInfo",
        "constructors": {},
        "properties": {
            "isModifiedToken": "isModifiedToken$0",
            "nextPollUrl": "nextPollUrl$0",
            "isModified": "isModified$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "groupmembershiptype": {
        "name": "GroupMembershipType",
        "constructors": {},
        "properties": {
            "GroupOwner": "GroupOwner$0",
            "NotAMemberPrivateRequested": "NotAMemberPrivateRequested$0",
            "NotAMember": "NotAMember$0",
            "StandardMember": "StandardMember$0",
            "GroupManager": "GroupManager$0"
        },
        "methods": {
            "values()\tLIST<ConnectApi.GroupMembershipType>": "values()$0"
        }
    },
    "groupemailfrequency": {
        "name": "GroupEmailFrequency",
        "constructors": {},
        "properties": {
            "UseDefault": "UseDefault$0",
            "Never": "Never$0",
            "DailyDigest": "DailyDigest$0",
            "EachPost": "EachPost$0",
            "WeeklyDigest": "WeeklyDigest$0"
        },
        "methods": {
            "values()\tLIST<ConnectApi.GroupEmailFrequency>": "values()$0"
        }
    },
    "type": {
        "name": "Type",
        "constructors": {},
        "properties": {},
        "methods": {
            "getName()\tString": "getName()$0",
            "toString()\tString": "toString()$0",
            "equals(Object o)\tBoolean": "equals($0)",
            "forName(String namespace, String clsName)\tsystem.Type": "forName($0)",
            "hashcode()\tInteger": "hashcode()$0",
            "forName(String clsName)\tsystem.Type": "forName($0)",
            "newInstance()\tObject": "newInstance()$0"
        }
    },
    "batchable": {
        "name": "Batchable",
        "constructors": {},
        "properties": {},
        "methods": {
            "start(Database.BatchableContext param1)\tsystem.Iterable": "start($0)",
            "finish(Database.BatchableContext param1)\tvoid": "finish($0)",
            "execute(Database.BatchableContext param1, LIST<ANY> param2)\tvoid": "execute($0)"
        }
    },
    "complexsegment": {
        "name": "ComplexSegment",
        "constructors": {},
        "properties": {
            "segments": "segments$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "caseactortype": {
        "name": "CaseActorType",
        "constructors": {},
        "properties": {
            "Customer": "Customer$0",
            "CustomerService": "CustomerService$0"
        },
        "methods": {
            "values()\tLIST<ConnectApi.CaseActorType>": "values()$0"
        }
    },
    "version": {
        "name": "Version",
        "constructors": {},
        "properties": {},
        "methods": {
            "patch()\tInteger": "patch()$0",
            "major()\tInteger": "major()$0",
            "minor()\tInteger": "minor()$0",
            "compareTo(system.Version other)\tInteger": "compareTo($0)"
        }
    },
    "inputparameter": {
        "name": "InputParameter",
        "constructors": {},
        "properties": {
            "description": "description$0",
            "name": "name$0",
            "required": "required$0",
            "parameterType": "parameterType$0"
        },
        "methods": {}

    },
    "date": {
        "name": "Date",
        "constructors": {},
        "properties": {},
        "methods": {
            "day()\tInteger": "day()$0",
            "dayOfYear()\tInteger": "dayOfYear()$0",
            "year()\tInteger": "year()$0",
            "valueOf(Object o)\tDate": "valueOf($0)",
            "parse(String str)\tDate": "parse($0)",
            "isLeapYear(Integer year)\tBoolean": "isLeapYear($0)",
            "newInstance(Integer year, Integer month, Integer day)\tDate": "newInstance($0)",
            "toStartOfMonth()\tDate": "toStartOfMonth()$0",
            "isSameDay(Date other)\tBoolean": "isSameDay($0)",
            "today()\tDate": "today()$0",
            "monthsBetween(Date other)\tInteger": "monthsBetween($0)",
            "toStartOfWeek()\tDate": "toStartOfWeek()$0",
            "format()\tString": "format()$0",
            "addError(String msg, Boolean escape)\tvoid": "addError($0)",
            "month()\tInteger": "month()$0",
            "valueOf(String str)\tDate": "valueOf($0)",
            "addYears(Integer years)\tDate": "addYears($0)",
            "addError(APEX_OBJECT msg)\tvoid": "addError($0)",
            "daysBetween(Date other)\tInteger": "daysBetween($0)",
            "addError(APEX_OBJECT msg, Boolean escape)\tvoid": "addError($0)",
            "addMonths(Integer months)\tDate": "addMonths($0)",
            "daysInMonth(Integer year, Integer month)\tInteger": "daysInMonth($0)",
            "addError(String msg)\tvoid": "addError($0)",
            "addDays(Integer days)\tDate": "addDays($0)"
        }
    },
    "feeditem": {
        "name": "FeedItem",
        "constructors": {},
        "properties": {
            "actor": "actor$0",
            "url": "url$0",
            "body": "body$0",
            "createdDate": "createdDate$0",
            "canShare": "canShare$0",
            "comments": "comments$0",
            "likesMessage": "likesMessage$0",
            "event": "event$0",
            "photoUrl": "photoUrl$0",
            "isDeleteRestricted": "isDeleteRestricted$0",
            "originalFeedItemActor": "originalFeedItemActor$0",
            "visibility": "visibility$0",
            "isBookmarkedByCurrentUser": "isBookmarkedByCurrentUser$0",
            "preamble": "preamble$0",
            "clientInfo": "clientInfo$0",
            "parent": "parent$0",
            "myLike": "myLike$0",
            "originalFeedItem": "originalFeedItem$0",
            "id": "id$0",
            "relativeCreatedDate": "relativeCreatedDate$0",
            "isLikedByCurrentUser": "isLikedByCurrentUser$0",
            "attachment": "attachment$0",
            "type": "type$0",
            "modifiedDate": "modifiedDate$0",
            "likes": "likes$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "touchhandledexception": {
        "name": "TouchHandledException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "chatteractivity": {
        "name": "ChatterActivity",
        "constructors": {},
        "properties": {
            "commentCount": "commentCount$0",
            "commentReceivedCount": "commentReceivedCount$0",
            "postCount": "postCount$0",
            "likeReceivedCount": "likeReceivedCount$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "basictemplateattachment": {
        "name": "BasicTemplateAttachment",
        "constructors": {},
        "properties": {
            "description": "description$0",
            "linkUrl": "linkUrl$0",
            "title": "title$0",
            "linkRecordId": "linkRecordId$0",
            "subtype": "subtype$0",
            "icon": "icon$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "exception": {
        "name": "Exception",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "apexpages": {
        "name": "ApexPages",
        "constructors": {},
        "properties": {},
        "methods": {
            "addMessage(ApexPages.Message message)\tvoid": "addMessage($0)",
            "getMessages()\tLIST<ApexPages.Message>": "getMessages()$0",
            "hasMessages(ApexPages.Severity severity)\tBoolean": "hasMessages($0)",
            "addMessages(APEX_OBJECT ex)\tvoid": "addMessages($0)",
            "hasMessages()\tBoolean": "hasMessages()$0",
            "currentPage()\tSystem.PageReference": "currentPage()$0"
        }
    },
    "iterable": {
        "name": "Iterable",
        "constructors": {},
        "properties": {},
        "methods": {
            "iterator()\tsystem.Iterator": "iterator()$0"
        }
    },
    "ideastandardsetcontroller": {
        "name": "IdeaStandardSetController",
        "constructors": {},
        "properties": {},
        "methods": {
            "getListViewOptions()\tLIST<System.SelectOption>": "getListViewOptions()$0",
            "addFields(LIST<String> fieldNames)\tvoid": "addFields($0)",
            "next()\tvoid": "next()$0",
            "getRecord()\tSObject": "getRecord()$0",
            "reset()\tvoid": "reset()$0",
            "getFilterId()\tString": "getFilterId()$0",
            "setFilterId(String filterId)\tvoid": "setFilterId($0)",
            "last()\tvoid": "last()$0",
            "setPageSize(Integer pageSize)\tvoid": "setPageSize($0)",
            "getCompleteResult()\tBoolean": "getCompleteResult()$0",
            "cancel()\tSystem.PageReference": "cancel()$0",
            "setPageNumber(Integer pageNumber)\tvoid": "setPageNumber($0)",
            "setSelected(LIST<SObject> selected)\tvoid": "setSelected($0)",
            "getHasPrevious()\tBoolean": "getHasPrevious()$0",
            "first()\tvoid": "first()$0",
            "getPageSize()\tInteger": "getPageSize()$0",
            "getSelected()\tLIST<SObject>": "getSelected()$0",
            "getIdeaList()\tLIST<Idea>": "getIdeaList()$0",
            "getRecords()\tLIST<SObject>": "getRecords()$0",
            "getPageNumber()\tInteger": "getPageNumber()$0",
            "getResultSize()\tInteger": "getResultSize()$0",
            "getHasNext()\tBoolean": "getHasNext()$0",
            "previous()\tvoid": "previous()$0",
            "save()\tSystem.PageReference": "save()$0"
        }
    },
    "limitexception": {
        "name": "LimitException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "crypto": {
        "name": "Crypto",
        "constructors": {},
        "properties": {},
        "methods": {
            "sign(String algorithmName, Blob input, Blob privateKey)\tBlob": "sign($0)",
            "decrypt(String algorithmName, Blob secretKey, Blob initializationVector, Blob encryptedData)\tBlob": "decrypt($0)",
            "decryptWithManagedIV(String algorithmName, Blob secretKey, Blob encryptedData)\tBlob": "decryptWithManagedIV($0)",
            "generateMac(String algorithmName, Blob input, Blob privateKey)\tBlob": "generateMac($0)",
            "encrypt(String algorithmName, Blob secretKey, Blob initializationVector, Blob clearData)\tBlob": "encrypt($0)",
            "getRandomInteger()\tInteger": "getRandomInteger()$0",
            "getRandomLong()\tLong": "getRandomLong()$0",
            "encryptWithManagedIV(String algorithmName, Blob secretKey, Blob clearData)\tBlob": "encryptWithManagedIV($0)",
            "generateDigest(String algorithmName, Blob input)\tBlob": "generateDigest($0)",
            "generateAesKey(Integer size)\tBlob": "generateAesKey($0)"
        }
    },
    "xmltag": {
        "name": "XmlTag",
        "constructors": {},
        "properties": {
            "SPACE": "SPACE$0",
            "START_ELEMENT": "START_ELEMENT$0",
            "END_DOCUMENT": "END_DOCUMENT$0",
            "END_ELEMENT": "END_ELEMENT$0",
            "NAMESPACE": "NAMESPACE$0",
            "NOTATION_DECLARATION": "NOTATION_DECLARATION$0",
            "COMMENT": "COMMENT$0",
            "DTD": "DTD$0",
            "CHARACTERS": "CHARACTERS$0",
            "ENTITY_DECLARATION": "ENTITY_DECLARATION$0",
            "START_DOCUMENT": "START_DOCUMENT$0",
            "ATTRIBUTE": "ATTRIBUTE$0",
            "CDATA": "CDATA$0",
            "ENTITY_REFERENCE": "ENTITY_REFERENCE$0",
            "PROCESSING_INSTRUCTION": "PROCESSING_INSTRUCTION$0"
        },
        "methods": {
            "values()\tLIST<system.XmlTag>": "values()$0"
        }
    },
    "leadconvert": {
        "name": "LeadConvert",
        "constructors": {},
        "properties": {},
        "methods": {}

    },
    "set": {
        "name": "Set",
        "constructors": {},
        "properties": {},
        "methods": {
            "containsAll(LIST elements)\tBoolean": "containsAll($0)",
            "remove(ANY element)\tBoolean": "remove($0)",
            "addAll(SET elements)\tBoolean": "addAll($0)",
            "clone()\tSET<String>": "clone()$0",
            "isEmpty()\tBoolean": "isEmpty()$0",
            "size()\tInteger": "size()$0",
            "removeAll(SET elements)\tBoolean": "removeAll($0)",
            "removeAll(LIST elements)\tBoolean": "removeAll($0)",
            "add(ANY element)\tBoolean": "add($0)",
            "contains(ANY element)\tBoolean": "contains($0)",
            "iterator()\tsystem.ListIterator": "iterator()$0",
            "addAll(LIST elements)\tBoolean": "addAll($0)",
            "clear()\tvoid": "clear()$0",
            "containsAll(SET elements)\tBoolean": "containsAll($0)",
            "retainAll(LIST elements)\tBoolean": "retainAll($0)",
            "retainAll(SET elements)\tBoolean": "retainAll($0)"
        }
    },
    "subscription": {
        "name": "Subscription",
        "constructors": {},
        "properties": {
            "id": "id$0",
            "community": "community$0",
            "subscriber": "subscriber$0",
            "url": "url$0",
            "subject": "subject$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "math": {
        "name": "Math",
        "constructors": {},
        "properties": {},
        "methods": {
            "mod(Long x, Long y)\tLong": "mod($0)",
            "floor(Double x)\tDouble": "floor($0)",
            "log(Double x)\tDouble": "log($0)",
            "acos(Decimal x)\tDecimal": "acos($0)",
            "sin(Double x)\tDouble": "sin($0)",
            "sin(Decimal x)\tDecimal": "sin($0)",
            "atan(Decimal x)\tDecimal": "atan($0)",
            "cos(Decimal x)\tDecimal": "cos($0)",
            "max(Decimal x, Decimal y)\tDecimal": "max($0)",
            "min(Double x, Double y)\tDouble": "min($0)",
            "signum(Decimal x)\tDecimal": "signum($0)",
            "atan(Double x)\tDouble": "atan($0)",
            "log10(Double x)\tDouble": "log10($0)",
            "round(Double x)\tInteger": "round($0)",
            "cbrt(Decimal x)\tDecimal": "cbrt($0)",
            "tanh(Double x)\tDouble": "tanh($0)",
            "min(Long x, Long y)\tLong": "min($0)",
            "pow(Double base, Double exp)\tDouble": "pow($0)",
            "random()\tDouble": "random()$0",
            "rint(Decimal x)\tDecimal": "rint($0)",
            "abs(Long x)\tLong": "abs($0)",
            "log(Decimal x)\tDecimal": "log($0)",
            "tanh(Decimal x)\tDecimal": "tanh($0)",
            "signum(Double x)\tDouble": "signum($0)",
            "max(Double x, Double y)\tDouble": "max($0)",
            "rint(Double x)\tDouble": "rint($0)",
            "cos(Double x)\tDouble": "cos($0)",
            "ceil(Decimal x)\tDecimal": "ceil($0)",
            "min(Decimal x, Decimal y)\tDecimal": "min($0)",
            "atan2(Double x, Double y)\tDouble": "atan2($0)",
            "abs(Decimal x)\tDecimal": "abs($0)",
            "sinh(Decimal x)\tDecimal": "sinh($0)",
            "max(Long x, Long y)\tLong": "max($0)",
            "sqrt(Decimal x)\tDecimal": "sqrt($0)",
            "cbrt(Double x)\tDouble": "cbrt($0)",
            "roundToLong(Double x)\tLong": "roundToLong($0)",
            "tan(Decimal x)\tDecimal": "tan($0)",
            "cosh(Double x)\tDouble": "cosh($0)",
            "ceil(Double x)\tDouble": "ceil($0)",
            "exp(Double x)\tDouble": "exp($0)",
            "asin(Decimal x)\tDecimal": "asin($0)",
            "exp(Decimal x)\tDecimal": "exp($0)",
            "max(Integer x, Integer y)\tInteger": "max($0)",
            "tan(Double x)\tDouble": "tan($0)",
            "abs(Double x)\tDouble": "abs($0)",
            "roundToLong(Decimal x)\tLong": "roundToLong($0)",
            "abs(Integer x)\tInteger": "abs($0)",
            "sinh(Double x)\tDouble": "sinh($0)",
            "log10(Decimal x)\tDecimal": "log10($0)",
            "asin(Double x)\tDouble": "asin($0)",
            "min(Integer x, Integer y)\tInteger": "min($0)",
            "atan2(Decimal x, Decimal y)\tDecimal": "atan2($0)",
            "mod(Integer x, Integer y)\tInteger": "mod($0)",
            "acos(Double x)\tDouble": "acos($0)",
            "cosh(Decimal x)\tDecimal": "cosh($0)",
            "sqrt(Double x)\tDouble": "sqrt($0)",
            "round(Decimal x)\tInteger": "round($0)",
            "floor(Decimal x)\tDecimal": "floor($0)"
        }
    },
    "dmloptions": {
        "name": "DMLOptions",
        "constructors": {},
        "properties": {
            "EmailHeader": "EmailHeader$0",
            "OptAllOrNone": "OptAllOrNone$0",
            "AssignmentRuleHeader": "AssignmentRuleHeader$0",
            "AllowFieldTruncation": "AllowFieldTruncation$0",
            "LocaleOptions": "LocaleOptions$0"
        },
        "methods": {}

    },
    "communitystatus": {
        "name": "CommunityStatus",
        "constructors": {},
        "properties": {
            "Inactive": "Inactive$0",
            "Live": "Live$0",
            "UnderConstruction": "UnderConstruction$0"
        },
        "methods": {
            "values()\tLIST<ConnectApi.CommunityStatus>": "values()$0"
        }
    },
    "severity": {
        "name": "Severity",
        "constructors": {},
        "properties": {
            "CONFIRM": "CONFIRM$0",
            "FATAL": "FATAL$0",
            "WARNING": "WARNING$0",
            "ERROR": "ERROR$0",
            "INFO": "INFO$0"
        },
        "methods": {
            "values()\tLIST<ApexPages.Severity>": "values()$0"
        }
    },
    "ideastandardcontroller": {
        "name": "IdeaStandardController",
        "constructors": {},
        "properties": {},
        "methods": {
            "getCommentList()\tLIST<IdeaComment>": "getCommentList()$0",
            "getSubject()\tSObject": "getSubject()$0",
            "getRecord()\tSObject": "getRecord()$0",
            "getId()\tString": "getId()$0",
            "view()\tSystem.PageReference": "view()$0",
            "reset()\tvoid": "reset()$0",
            "edit()\tSystem.PageReference": "edit()$0",
            "delete()\tSystem.PageReference": "delete()$0",
            "cancel()\tSystem.PageReference": "cancel()$0",
            "addFields(LIST<String> fieldNames)\tvoid": "addFields($0)",
            "save()\tSystem.PageReference": "save()$0"
        }
    },
    "chatterusers": {
        "name": "ChatterUsers",
        "constructors": {},
        "properties": {},
        "methods": {
            "updateChatterSettings(String communityId, String userId, ConnectApi.GroupEmailFrequency defaultGroupEmailFrequency)\tConnectApi.UserChatterSettings": "updateChatterSettings($0)",
            "getPhoto(String communityId, String userId)\tConnectApi.Photo": "getPhoto($0)",
            "follow(String communityId, String userId, String subjectId)\tConnectApi.Subscription": "follow($0)",
            "searchUsers(String communityId, String q, Integer pageParam, Integer pageSize)\tConnectApi.UserPage": "searchUsers($0)",
            "searchUsers(String communityId, String q, String searchContextId, Integer pageParam, Integer pageSize)\tConnectApi.UserPage": "searchUsers($0)",
            "setTestSearchUsers(String communityId, String q, String searchContextId, Integer pageParam, Integer pageSize, ConnectApi.UserPage result)\tvoid": "setTestSearchUsers($0)",
            "getFollowings(String communityId, String userId, String filterType, Integer pageParam, Integer pageSize)\tConnectApi.FollowingPage": "getFollowings($0)",
            "getFollowings(String communityId, String userId, String filterType)\tConnectApi.FollowingPage": "getFollowings($0)",
            "getUsers(String communityId, Integer pageParam, Integer pageSize)\tConnectApi.UserPage": "getUsers($0)",
            "searchUsers(String communityId, String q)\tConnectApi.UserPage": "searchUsers($0)",
            "setTestSearchUsers(String communityId, String q, ConnectApi.UserPage result)\tvoid": "setTestSearchUsers($0)",
            "deletePhoto(String communityId, String userId)\tvoid": "deletePhoto($0)",
            "getFollowings(String communityId, String userId, String filterType, Integer pageParam)\tConnectApi.FollowingPage": "getFollowings($0)",
            "getFollowings(String communityId, String userId, Integer pageParam, Integer pageSize)\tConnectApi.FollowingPage": "getFollowings($0)",
            "setPhoto(String communityId, String userId, String fileId, Integer versionNumber)\tConnectApi.Photo": "setPhoto($0)",
            "getFollowings(String communityId, String userId)\tConnectApi.FollowingPage": "getFollowings($0)",
            "setTestSearchUsers(String communityId, String q, Integer pageParam, Integer pageSize, ConnectApi.UserPage result)\tvoid": "setTestSearchUsers($0)",
            "getUser(String communityId, String userId)\tConnectApi.UserDetail": "getUser($0)",
            "getUsers(String communityId)\tConnectApi.UserPage": "getUsers($0)",
            "getFollowers(String communityId, String userId)\tConnectApi.FollowerPage": "getFollowers($0)",
            "getChatterSettings(String communityId, String userId)\tConnectApi.UserChatterSettings": "getChatterSettings($0)",
            "getFollowers(String communityId, String userId, Integer pageParam, Integer pageSize)\tConnectApi.FollowerPage": "getFollowers($0)",
            "getGroups(String communityId, String userId, Integer pageParam, Integer pageSize)\tConnectApi.UserGroupPage": "getGroups($0)",
            "getGroups(String communityId, String userId)\tConnectApi.UserGroupPage": "getGroups($0)",
            "setPhoto(String communityId, String userId, ConnectApi.BinaryInput fileUpload)\tConnectApi.Photo": "setPhoto($0)",
            "getFollowings(String communityId, String userId, Integer pageParam)\tConnectApi.FollowingPage": "getFollowings($0)"
        }
    },
    "recordsummary": {
        "name": "RecordSummary",
        "constructors": {},
        "properties": {},
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "licenseexception": {
        "name": "LicenseException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "chattergroups": {
        "name": "ChatterGroups",
        "constructors": {},
        "properties": {},
        "methods": {
            "getGroups(String communityId)\tConnectApi.ChatterGroupPage": "getGroups($0)",
            "setTestSearchGroups(String communityId, String q, Integer pageParam, Integer pageSize, ConnectApi.ChatterGroupPage result)\tvoid": "setTestSearchGroups($0)",
            "getMember(String communityId, String membershipId)\tConnectApi.GroupMember": "getMember($0)",
            "getGroupMembershipRequests(String communityId, String groupId)\tConnectApi.GroupMembershipRequests": "getGroupMembershipRequests($0)",
            "getFollowings(String communityId, String groupId, Integer pageParam)\tConnectApi.FollowingPage": "getFollowings($0)",
            "addMember(String communityId, String groupId, String userId)\tConnectApi.GroupMember": "addMember($0)",
            "getGroupMembershipRequest(String communityId, String requestId)\tConnectApi.GroupMembershipRequest": "getGroupMembershipRequest($0)",
            "updateGroup(String communityId, String groupId, ConnectApi.ChatterGroupInput groupInput)\tConnectApi.ChatterGroupDetail": "updateGroup($0)",
            "updateRequestStatus(String communityId, String requestId, ConnectApi.GroupMembershipRequestStatus status)\tConnectApi.GroupMembershipRequest": "updateRequestStatus($0)",
            "getMembers(String communityId, String groupId)\tConnectApi.GroupMemberPage": "getMembers($0)",
            "getMyChatterSettings(String communityId, String groupId)\tConnectApi.GroupChatterSettings": "getMyChatterSettings($0)",
            "getFollowings(String communityId, String groupId, String filterType)\tConnectApi.FollowingPage": "getFollowings($0)",
            "getFollowings(String communityId, String groupId)\tConnectApi.FollowingPage": "getFollowings($0)",
            "getPhoto(String communityId, String groupId)\tConnectApi.Photo": "getPhoto($0)",
            "updateMyChatterSettings(String communityId, String groupId, ConnectApi.GroupEmailFrequency emailFrequency)\tConnectApi.GroupChatterSettings": "updateMyChatterSettings($0)",
            "deletePhoto(String communityId, String groupId)\tvoid": "deletePhoto($0)",
            "getGroups(String communityId, Integer pageParam, Integer pageSize)\tConnectApi.ChatterGroupPage": "getGroups($0)",
            "setPhoto(String communityId, String groupId, String fileId, Integer versionNumber)\tConnectApi.Photo": "setPhoto($0)",
            "follow(String communityId, String groupId, String subjectId)\tConnectApi.Subscription": "follow($0)",
            "getMembers(String communityId, String groupId, Integer pageParam, Integer pageSize)\tConnectApi.GroupMemberPage": "getMembers($0)",
            "getGroup(String communityId, String groupId)\tConnectApi.ChatterGroupDetail": "getGroup($0)",
            "getFollowings(String communityId, String groupId, Integer pageParam, Integer pageSize)\tConnectApi.FollowingPage": "getFollowings($0)",
            "getGroupMembershipRequests(String communityId, String groupId, ConnectApi.GroupMembershipRequestStatus status)\tConnectApi.GroupMembershipRequests": "getGroupMembershipRequests($0)",
            "setPhoto(String communityId, String groupId, ConnectApi.BinaryInput fileUpload)\tConnectApi.Photo": "setPhoto($0)",
            "getFollowings(String communityId, String groupId, String filterType, Integer pageParam, Integer pageSize)\tConnectApi.FollowingPage": "getFollowings($0)",
            "searchGroups(String communityId, String q)\tConnectApi.ChatterGroupPage": "searchGroups($0)",
            "searchGroups(String communityId, String q, Integer pageParam, Integer pageSize)\tConnectApi.ChatterGroupPage": "searchGroups($0)",
            "requestGroupMembership(String communityId, String groupId)\tConnectApi.GroupMembershipRequest": "requestGroupMembership($0)",
            "deleteMember(String communityId, String membershipId)\tvoid": "deleteMember($0)",
            "getFollowings(String communityId, String groupId, String filterType, Integer pageParam)\tConnectApi.FollowingPage": "getFollowings($0)",
            "setTestSearchGroups(String communityId, String q, ConnectApi.ChatterGroupPage result)\tvoid": "setTestSearchGroups($0)"
        }
    },
    "id": {
        "name": "Id",
        "constructors": {},
        "properties": {},
        "methods": {
            "addError(String msg, Boolean escape)\tvoid": "addError($0)",
            "addError(APEX_OBJECT msg, Boolean escape)\tvoid": "addError($0)",
            "addError(APEX_OBJECT msg)\tvoid": "addError($0)",
            "valueOf(String str)\tId": "valueOf($0)",
            "getSobjectType()\tSchema.SObjectType": "getSobjectType()$0",
            "addError(String msg)\tvoid": "addError($0)"
        }
    },
    "userpage": {
        "name": "UserPage",
        "constructors": {},
        "properties": {
            "previousPageToken": "previousPageToken$0",
            "nextPageUrl": "nextPageUrl$0",
            "users": "users$0",
            "nextPageToken": "nextPageToken$0",
            "currentPageToken": "currentPageToken$0",
            "previousPageUrl": "previousPageUrl$0",
            "currentPageUrl": "currentPageUrl$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "logginglevel": {
        "name": "LoggingLevel",
        "constructors": {},
        "properties": {
            "FINE": "FINE$0",
            "WARN": "WARN$0",
            "FINER": "FINER$0",
            "INFO": "INFO$0",
            "FINEST": "FINEST$0",
            "ERROR": "ERROR$0",
            "INTERNAL": "INTERNAL$0",
            "DEBUG": "DEBUG$0"
        },
        "methods": {
            "values()\tLIST<system.LoggingLevel>": "values()$0"
        }
    },
    "chatterfeeds": {
        "name": "ChatterFeeds",
        "constructors": {},
        "properties": {},
        "methods": {
            "getFeedItemsFromFilterFeed(String communityId, String subjectId, String keyPrefix)\tConnectApi.FeedItemPage": "getFeedItemsFromFilterFeed($0)",
            "getCommentsForFeedItem(String communityId, String feedItemId, String pageParam, Integer pageSize)\tConnectApi.CommentPage": "getCommentsForFeedItem($0)",
            "postComment(String communityId, String feedItemId, String text)\tConnectApi.Comment": "postComment($0)",
            "getFeed(String communityId, ConnectApi.FeedType feedType, ConnectApi.FeedSortOrder sortParam)\tConnectApi.Feed": "getFeed($0)",
            "setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedItemPage result)\tvoid": "setTestSearchFeedItemsInFeed($0)",
            "getComment(String communityId, String commentId)\tConnectApi.Comment": "getComment($0)",
            "setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String q, ConnectApi.FeedItemPage result)\tvoid": "setTestSearchFeedItemsInFeed($0)",
            "setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, ConnectApi.FeedItemPage result)\tvoid": "setTestGetFeedItemsFromFeed($0)",
            "searchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String q)\tConnectApi.FeedItemPage": "searchFeedItemsInFeed($0)",
            "getFeed(String communityId, ConnectApi.FeedType feedType)\tConnectApi.Feed": "getFeed($0)",
            "getFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String subjectId)\tConnectApi.FeedItemPage": "getFeedItemsFromFeed($0)",
            "setTestSearchFeedItems(String communityId, String q, String pageParam, Integer pageSize, ConnectApi.FeedItemPage result)\tvoid": "setTestSearchFeedItems($0)",
            "deleteFeedItem(String communityId, String feedItemId)\tvoid": "deleteFeedItem($0)",
            "setTestSearchFeedItems(String communityId, String q, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)\tvoid": "setTestSearchFeedItems($0)",
            "getLikesForComment(String communityId, String commentId, Integer pageParam, Integer pageSize)\tConnectApi.ChatterLikePage": "getLikesForComment($0)",
            "setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String q, ConnectApi.FeedItemPage result)\tvoid": "setTestSearchFeedItemsInFeed($0)",
            "setTestGetFeedItemsFromFilterFeed(String communityId, String subjectId, String keyPrefix, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)\tvoid": "setTestGetFeedItemsFromFilterFeed($0)",
            "likeFeedItem(String communityId, String feedItemId)\tConnectApi.ChatterLike": "likeFeedItem($0)",
            "getFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)\tConnectApi.FeedItemPage": "getFeedItemsFromFeed($0)",
            "shareFeedItem(String communityId, ConnectApi.FeedType feedType, String subjectId, String originalFeedItemId)\tConnectApi.FeedItem": "shareFeedItem($0)",
            "getFilterFeed(String communityId, String subjectId, String keyPrefix, ConnectApi.FeedSortOrder sortParam)\tConnectApi.Feed": "getFilterFeed($0)",
            "setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)\tvoid": "setTestGetFeedItemsFromFeed($0)",
            "getLike(String communityId, String likeId)\tConnectApi.ChatterLike": "getLike($0)",
            "searchFeedItems(String communityId, String q, String pageParam, Integer pageSize)\tConnectApi.FeedItemPage": "searchFeedItems($0)",
            "getLikesForFeedItem(String communityId, String feedItemId, Integer pageParam, Integer pageSize)\tConnectApi.ChatterLikePage": "getLikesForFeedItem($0)",
            "searchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String q)\tConnectApi.FeedItemPage": "searchFeedItemsInFeed($0)",
            "setTestSearchFeedItems(String communityId, String q, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)\tvoid": "setTestSearchFeedItems($0)",
            "searchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q)\tConnectApi.FeedItemPage": "searchFeedItemsInFeed($0)",
            "setTestGetFeedItemsFromFilterFeed(String communityId, String subjectId, String keyPrefix, ConnectApi.FeedItemPage result)\tvoid": "setTestGetFeedItemsFromFilterFeed($0)",
            "getFeedPoll(String communityId, String feedItemId)\tConnectApi.FeedPoll": "getFeedPoll($0)",
            "searchFeedItemsInFilterFeed(String communityId, String subjectId, String keyPrefix, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q)\tConnectApi.FeedItemPage": "searchFeedItemsInFilterFeed($0)",
            "getFilterFeed(String communityId, String subjectId, String keyPrefix)\tConnectApi.Feed": "getFilterFeed($0)",
            "getFeedItemsFromFilterFeed(String communityId, String subjectId, String keyPrefix, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)\tConnectApi.FeedItemPage": "getFeedItemsFromFilterFeed($0)",
            "setTestSearchFeedItemsInFilterFeed(String communityId, String subjectId, String keyPrefix, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedItemPage result)\tvoid": "setTestSearchFeedItemsInFilterFeed($0)",
            "getFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)\tConnectApi.FeedItemPage": "getFeedItemsFromFeed($0)",
            "searchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q)\tConnectApi.FeedItemPage": "searchFeedItemsInFeed($0)",
            "isModified(String communityId, ConnectApi.FeedType feedType, String subjectId, String since)\tConnectApi.FeedModifiedInfo": "isModified($0)",
            "setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedItemPage result)\tvoid": "setTestSearchFeedItemsInFeed($0)",
            "setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, ConnectApi.FeedItemPage result)\tvoid": "setTestGetFeedItemsFromFeed($0)",
            "deleteLike(String communityId, String likeId)\tvoid": "deleteLike($0)",
            "getFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, ConnectApi.FeedSortOrder sortParam)\tConnectApi.Feed": "getFeed($0)",
            "setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)\tvoid": "setTestGetFeedItemsFromFeed($0)",
            "postFeedItem(String communityId, ConnectApi.FeedType feedType, String subjectId, ConnectApi.FeedItemInput feedItem, ConnectApi.BinaryInput feedItemFileUpload)\tConnectApi.FeedItem": "postFeedItem($0)",
            "setTestSearchFeedItemsInFilterFeed(String communityId, String subjectId, String keyPrefix, String q, ConnectApi.FeedItemPage result)\tvoid": "setTestSearchFeedItemsInFilterFeed($0)",
            "getLikesForFeedItem(String communityId, String feedItemId)\tConnectApi.ChatterLikePage": "getLikesForFeedItem($0)",
            "likeComment(String communityId, String commentId)\tConnectApi.ChatterLike": "likeComment($0)",
            "postFeedItem(String communityId, ConnectApi.FeedType feedType, String subjectId, String text)\tConnectApi.FeedItem": "postFeedItem($0)",
            "getFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType)\tConnectApi.FeedItemPage": "getFeedItemsFromFeed($0)",
            "postComment(String communityId, String feedItemId, ConnectApi.CommentInput comment, ConnectApi.BinaryInput feedItemFileUpload)\tConnectApi.Comment": "postComment($0)",
            "searchFeedItems(String communityId, String q, ConnectApi.FeedSortOrder sortParam)\tConnectApi.FeedItemPage": "searchFeedItems($0)",
            "getCommentsForFeedItem(String communityId, String feedItemId)\tConnectApi.CommentPage": "getCommentsForFeedItem($0)",
            "searchFeedItemsInFilterFeed(String communityId, String subjectId, String keyPrefix, String q)\tConnectApi.FeedItemPage": "searchFeedItemsInFilterFeed($0)",
            "searchFeedItems(String communityId, String q, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)\tConnectApi.FeedItemPage": "searchFeedItems($0)",
            "getFeedItem(String communityId, String feedItemId)\tConnectApi.FeedItem": "getFeedItem($0)",
            "updateBookmark(String communityId, String feedItemId, Boolean isBookmarkedByCurrentUser)\tConnectApi.FeedItem": "updateBookmark($0)",
            "setTestSearchFeedItems(String communityId, String q, ConnectApi.FeedItemPage result)\tvoid": "setTestSearchFeedItems($0)",
            "getLikesForComment(String communityId, String commentId)\tConnectApi.ChatterLikePage": "getLikesForComment($0)",
            "deleteComment(String communityId, String commentId)\tvoid": "deleteComment($0)",
            "getFeed(String communityId, ConnectApi.FeedType feedType, String subjectId)\tConnectApi.Feed": "getFeed($0)",
            "voteOnFeedPoll(String communityId, String feedItemId, String myChoiceId)\tConnectApi.FeedPoll": "voteOnFeedPoll($0)",
            "searchFeedItems(String communityId, String q)\tConnectApi.FeedItemPage": "searchFeedItems($0)"
        }
    },
    "fieldchangevaluesegment": {
        "name": "FieldChangeValueSegment",
        "constructors": {},
        "properties": {
            "url": "url$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "messagebody": {
        "name": "MessageBody",
        "constructors": {},
        "properties": {},
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "header": {
        "name": "Header",
        "constructors": {},
        "properties": {
            "value": "value$0",
            "name": "name$0"
        },
        "methods": {}

    },
    "groupmember": {
        "name": "GroupMember",
        "constructors": {},
        "properties": {
            "id": "id$0",
            "user": "user$0",
            "url": "url$0",
            "role": "role$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "actor": {
        "name": "Actor",
        "constructors": {},
        "properties": {
            "type": "type$0",
            "name": "name$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "network": {
        "name": "Network",
        "constructors": {},
        "properties": {},
        "methods": {
            "getNetworkId()\tString": "getNetworkId()$0",
            "forwardToAuthPage(String startUrl)\tSystem.PageReference": "forwardToAuthPage($0)",
            "forwardToAuthPage(String startUrl, String displayType)\tSystem.PageReference": "forwardToAuthPage($0)",
            "communitiesLanding()\tSystem.PageReference": "communitiesLanding()$0"
        }
    },
    "finalexception": {
        "name": "FinalException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "feedtype": {
        "name": "FeedType",
        "constructors": {},
        "properties": {
            "Company": "Company$0",
            "Topics": "Topics$0",
            "Groups": "Groups$0",
            "News": "News$0",
            "People": "People$0",
            "Record": "Record$0",
            "Bookmarks": "Bookmarks$0",
            "UserProfile": "UserProfile$0",
            "To": "To$0",
            "Files": "Files$0"
        },
        "methods": {
            "values()\tLIST<ConnectApi.FeedType>": "values()$0"
        }
    },
    "groupchattersettings": {
        "name": "GroupChatterSettings",
        "constructors": {},
        "properties": {
            "emailFrequency": "emailFrequency$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "dashboardcomponentattachment": {
        "name": "DashboardComponentAttachment",
        "constructors": {},
        "properties": {
            "lastRefreshDate": "lastRefreshDate$0",
            "fullSizeImageUrl": "fullSizeImageUrl$0",
            "componentId": "componentId$0",
            "dashboardBodyText": "dashboardBodyText$0",
            "lastRefreshDateDisplayText": "lastRefreshDateDisplayText$0",
            "thumbnailUrl": "thumbnailUrl$0",
            "dashboardId": "dashboardId$0",
            "runningUser": "runningUser$0",
            "componentName": "componentName$0",
            "dashboardName": "dashboardName$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "querylocatoriterator": {
        "name": "QueryLocatorIterator",
        "constructors": {},
        "properties": {},
        "methods": {
            "next()\tSObject": "next()$0",
            "hasNext()\tBoolean": "hasNext()$0"
        }
    },
    "phonenumber": {
        "name": "PhoneNumber",
        "constructors": {},
        "properties": {
            "type": "type$0",
            "phoneNumber": "phoneNumber$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "emptystackexception": {
        "name": "EmptyStackException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "time": {
        "name": "Time",
        "constructors": {},
        "properties": {},
        "methods": {
            "addError(String msg, Boolean escape)\tvoid": "addError($0)",
            "minute()\tInteger": "minute()$0",
            "hour()\tInteger": "hour()$0",
            "second()\tInteger": "second()$0",
            "addHours(Integer hours)\tTime": "addHours($0)",
            "addMilliseconds(Integer milliseconds)\tTime": "addMilliseconds($0)",
            "addError(APEX_OBJECT msg, Boolean escape)\tvoid": "addError($0)",
            "newInstance(Integer hour, Integer minute, Integer second, Integer millisecond)\tTime": "newInstance($0)",
            "millisecond()\tInteger": "millisecond()$0",
            "addError(String msg)\tvoid": "addError($0)",
            "addError(APEX_OBJECT msg)\tvoid": "addError($0)",
            "addSeconds(Integer seconds)\tTime": "addSeconds($0)",
            "addMinutes(Integer minutes)\tTime": "addMinutes($0)"
        }
    },
    "groupmembershiprequeststatus": {
        "name": "GroupMembershipRequestStatus",
        "constructors": {},
        "properties": {
            "Pending": "Pending$0",
            "Accepted": "Accepted$0",
            "Declined": "Declined$0"
        },
        "methods": {
            "values()\tLIST<ConnectApi.GroupMembershipRequestStatus>": "values()$0"
        }
    },
    "emailtemplateselector": {
        "name": "EmailTemplateSelector",
        "constructors": {},
        "properties": {},
        "methods": {
            "getDefaultEmailTemplateId(Id param1)\tId": "getDefaultEmailTemplateId($0)"
        }
    },
    "outputparameter": {
        "name": "OutputParameter",
        "constructors": {},
        "properties": {
            "description": "description$0",
            "name": "name$0",
            "parameterType": "parameterType$0"
        },
        "methods": {}

    },
    "invalidheaderexception": {
        "name": "InvalidHeaderException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "flowexception": {
        "name": "FlowException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "batchablecontextimpl": {
        "name": "BatchableContextImpl",
        "constructors": {},
        "properties": {},
        "methods": {
            "getChildJobId()\tId": "getChildJobId()$0",
            "getJobId()\tId": "getJobId()$0"
        }
    },
    "messagebodyinput": {
        "name": "MessageBodyInput",
        "constructors": {},
        "properties": {
            "messageSegments": "messageSegments$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object": "convertToJavaObject($0)",
            "toString()\tString": "toString()$0"
        }
    },
    "feedsortorder": {
        "name": "FeedSortOrder",
        "constructors": {},
        "properties": {
            "CreatedDateDesc": "CreatedDateDesc$0",
            "LastModifiedDateDesc": "LastModifiedDateDesc$0"
        },
        "methods": {
            "values()\tLIST<ConnectApi.FeedSortOrder>": "values()$0"
        }
    },
    "feediteminput": {
        "name": "FeedItemInput",
        "constructors": {},
        "properties": {
            "attachment": "attachment$0",
            "body": "body$0",
            "originalFeedItemId": "originalFeedItemId$0",
            "isBookmarkedByCurrentUser": "isBookmarkedByCurrentUser$0",
            "visibility": "visibility$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object": "convertToJavaObject($0)",
            "toString()\tString": "toString()$0"
        }
    },
    "encodingutil": {
        "name": "EncodingUtil",
        "constructors": {},
        "properties": {},
        "methods": {
            "base64Decode(String s)\tBlob": "base64Decode($0)",
            "urlEncode(String s, String enc)\tString": "urlEncode($0)",
            "convertToHex(Blob s)\tString": "convertToHex($0)",
            "urlDecode(String s, String enc)\tString": "urlDecode($0)",
            "base64Encode(Blob s)\tString": "base64Encode($0)"
        }
    },
    "morechangessegment": {
        "name": "MoreChangesSegment",
        "constructors": {},
        "properties": {
            "moreChangesCount": "moreChangesCount$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "comment": {
        "name": "Comment",
        "constructors": {},
        "properties": {
            "body": "body$0",
            "clientInfo": "clientInfo$0",
            "parent": "parent$0",
            "myLike": "myLike$0",
            "feedItem": "feedItem$0",
            "createdDate": "createdDate$0",
            "likes": "likes$0",
            "url": "url$0",
            "likesMessage": "likesMessage$0",
            "id": "id$0",
            "isDeleteRestricted": "isDeleteRestricted$0",
            "user": "user$0",
            "relativeCreatedDate": "relativeCreatedDate$0",
            "attachment": "attachment$0",
            "type": "type$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "ratelimitexception": {
        "name": "RateLimitException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getErrorCode()\tString": "getErrorCode()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "entitylinksegment": {
        "name": "EntityLinkSegment",
        "constructors": {},
        "properties": {
            "reference": "reference$0",
            "motif": "motif$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "messagesegment": {
        "name": "MessageSegment",
        "constructors": {},
        "properties": {
            "type": "type$0",
            "text": "text$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "textsegmentinput": {
        "name": "TextSegmentInput",
        "constructors": {},
        "properties": {
            "text": "text$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object": "convertToJavaObject($0)",
            "toString()\tString": "toString()$0"
        }
    },
    "emailheader": {
        "name": "EmailHeader",
        "constructors": {},
        "properties": {
            "TriggerUserEmail": "TriggerUserEmail$0",
            "TriggerOtherEmail": "TriggerOtherEmail$0",
            "TriggerAutoResponseEmail": "TriggerAutoResponseEmail$0"
        },
        "methods": {}

    },
    "jsonexception": {
        "name": "JSONException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "xmlstreamwriter": {
        "name": "XmlStreamWriter",
        "constructors": {},
        "properties": {},
        "methods": {
            "writeComment(String data)\tvoid": "writeComment($0)",
            "getXmlString()\tString": "getXmlString()$0",
            "writeStartDocument(String encoding, String version)\tvoid": "writeStartDocument($0)",
            "writeCData(String data)\tvoid": "writeCData($0)",
            "writeProcessingInstruction(String target, String data)\tvoid": "writeProcessingInstruction($0)",
            "writeEndDocument()\tvoid": "writeEndDocument()$0",
            "close()\tvoid": "close()$0",
            "writeDefaultNamespace(String namesapceURI)\tvoid": "writeDefaultNamespace($0)",
            "writeNamespace(String prefix, String namesapceURI)\tvoid": "writeNamespace($0)",
            "writeCharacters(String text)\tvoid": "writeCharacters($0)",
            "writeEmptyElement(String prefix, String localName, String namesapceURI)\tvoid": "writeEmptyElement($0)",
            "writeEndElement()\tvoid": "writeEndElement()$0",
            "setDefaultNamespace(String uri)\tvoid": "setDefaultNamespace($0)",
            "writeAttribute(String prefix, String namespaceURI, String localName, String value)\tvoid": "writeAttribute($0)",
            "writeStartElement(String prefix, String localName, String namesapceURI)\tvoid": "writeStartElement($0)"
        }
    },
    "mathexception": {
        "name": "MathException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "nosuchelementexception": {
        "name": "NoSuchElementException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "restcontext": {
        "name": "RestContext",
        "constructors": {},
        "properties": {
            "response": "response$0",
            "request": "request$0"
        },
        "methods": {}

    },
    "unexpectedexception": {
        "name": "UnexpectedException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "list": {
        "name": "LIST",
        "constructors": {},
        "properties": {},
        "methods": {
            "add(ANY element)\tObject": "add($0)",
            "deepClone(Boolean preserveId)\tLIST<String>": "deepClone($0)",
            "addAll(SET elements)\tvoid": "addAll($0)",
            "set(Integer index, ANY value)\tvoid": "set($0)",
            "get(Integer index)\tObject": "get($0)",
            "size()\tInteger": "size()$0",
            "add(Integer index, ANY element)\tvoid": "add($0)",
            "deepClone()\tLIST<String>": "deepClone()$0",
            "getSObjectType()\tSchema.SObjectType": "getSObjectType()$0",
            "deepClone(Boolean preserveId, Boolean preserveReadOnlyTimestamps, Boolean preserveAutoNumbers)\tLIST<String>": "deepClone($0)",
            "remove(Integer index)\tObject": "remove($0)",
            "iterator()\tsystem.ListIterator": "iterator()$0",
            "sort()\tvoid": "sort()$0",
            "deepClone(Boolean preserveId, Boolean preserveReadOnlyTimestamps)\tLIST<String>": "deepClone($0)",
            "clone()\tLIST<String>": "clone()$0",
            "isEmpty()\tBoolean": "isEmpty()$0",
            "clear()\tvoid": "clear()$0",
            "addAll(LIST elements)\tvoid": "addAll($0)"
        }
    },
    "message": {
        "name": "Message",
        "constructors": {},
        "properties": {},
        "methods": {
            "getSummary()\tString": "getSummary()$0",
            "getDetail()\tString": "getDetail()$0",
            "getComponentLabel()\tString": "getComponentLabel()$0",
            "getSeverity()\tApexPages.Severity": "getSeverity()$0"
        }
    },
    "system": {
        "name": "System",
        "constructors": {},
        "properties": {},
        "methods": {
            "isBatch()\tBoolean": "isBatch()$0",
            "assertEquals(ANY expected, ANY actual)\tvoid": "assertEquals($0)",
            "isScheduled()\tBoolean": "isScheduled()$0",
            "setPassword(Id userId, String password)\tvoid": "setPassword($0)",
            "purgeOldAsyncJobs(Date date)\tInteger": "purgeOldAsyncJobs($0)",
            "abortJob(String jobId)\tvoid": "abortJob($0)",
            "assertEquals(ANY expected, ANY actual, ANY msg)\tvoid": "assertEquals($0)",
            "resetPassword(Id userId, Boolean sendUserEmail)\tSystem.ResetPasswordResult": "resetPassword($0)",
            "currentPageReference()\tSystem.PageReference": "currentPageReference()$0",
            "now()\tDatetime": "now()$0",
            "runAs(Package.Version version)\tvoid": "runAs($0)",
            "assertNotEquals(ANY expected, ANY actual)\tvoid": "assertNotEquals($0)",
            "requestVersion()\tsystem.Version": "requestVersion()$0",
            "assert(Boolean condition, ANY msg)\tvoid": "assert($0)",
            "today()\tDate": "today()$0",
            "runAs(SObject user, ANY block)\tvoid": "runAs($0)",
            "assert(Boolean condition)\tvoid": "assert($0)",
            "scheduleBatch(APEX_OBJECT batchable, String jobName, Integer minutesFromNow, Integer scopeSize)\tString": "scheduleBatch($0)",
            "debug(APEX_OBJECT logLevel, ANY o)\tvoid": "debug($0)",
            "currentTimeMillis()\tLong": "currentTimeMillis()$0",
            "scheduleBatch(APEX_OBJECT batchable, String jobName, Integer minutesFromNow)\tString": "scheduleBatch($0)",
            "schedule(String jobName, String cronExp, APEX_OBJECT schedulable)\tString": "schedule($0)",
            "getApplicationReadWriteMode()\tsystem.ApplicationReadWriteMode": "getApplicationReadWriteMode()$0",
            "isFuture()\tBoolean": "isFuture()$0",
            "debug(ANY o)\tvoid": "debug($0)",
            "assertNotEquals(ANY expected, ANY actual, ANY msg)\tvoid": "assertNotEquals($0)",
            "submit(LIST ids, String commments, String nextApprover)\tLIST<Id>": "submit($0)",
            "process(LIST workitemIds, String action, String commments, String nextApprover)\tLIST<Id>": "process($0)"
        }
    },
    "urlrewriter": {
        "name": "UrlRewriter",
        "constructors": {},
        "properties": {},
        "methods": {
            "generateUrlFor(LIST<System.PageReference> param1)\tLIST<System.PageReference>": "generateUrlFor($0)",
            "mapRequestUrl(System.PageReference param1)\tSystem.PageReference": "mapRequestUrl($0)"
        }
    },
    "xmlstreamreader": {
        "name": "XmlStreamReader",
        "constructors": {},
        "properties": {},
        "methods": {
            "getEventType()\tsystem.XmlTag": "getEventType()$0",
            "getPrefix()\tString": "getPrefix()$0",
            "getLocation()\tString": "getLocation()$0",
            "getAttributeType(Integer index)\tString": "getAttributeType($0)",
            "getNamespaceURIAt(Integer index)\tString": "getNamespaceURIAt($0)",
            "getAttributeLocalName(Integer index)\tString": "getAttributeLocalName($0)",
            "getNamespacePrefix(Integer index)\tString": "getNamespacePrefix($0)",
            "getAttributeCount()\tInteger": "getAttributeCount()$0",
            "getAttributePrefix(Integer index)\tString": "getAttributePrefix($0)",
            "getNamespace()\tString": "getNamespace()$0",
            "getLocalName()\tString": "getLocalName()$0",
            "isEndElement()\tBoolean": "isEndElement()$0",
            "isWhitespace()\tBoolean": "isWhitespace()$0",
            "getNamespaceURI(String prefix)\tString": "getNamespaceURI($0)",
            "hasName()\tBoolean": "hasName()$0",
            "getAttributeNamespace(Integer index)\tString": "getAttributeNamespace($0)",
            "hasNext()\tBoolean": "hasNext()$0",
            "getAttributeValue(String namespaceURI, String localName)\tString": "getAttributeValue($0)",
            "getNamespaceCount()\tInteger": "getNamespaceCount()$0",
            "getText()\tString": "getText()$0",
            "getPIData()\tString": "getPIData()$0",
            "getPITarget()\tString": "getPITarget()$0",
            "toString()\tString": "toString()$0",
            "getAttributeValueAt(Integer index)\tString": "getAttributeValueAt($0)",
            "setNamespaceAware(Boolean flag)\tvoid": "setNamespaceAware($0)",
            "nextTag()\tInteger": "nextTag()$0",
            "getVersion()\tString": "getVersion()$0",
            "isCharacters()\tBoolean": "isCharacters()$0",
            "next()\tInteger": "next()$0",
            "hasText()\tBoolean": "hasText()$0",
            "isStartElement()\tBoolean": "isStartElement()$0",
            "setCoalescing(Boolean flag)\tvoid": "setCoalescing($0)"
        }
    },
    "querylocatorchunkiterator": {
        "name": "QueryLocatorChunkIterator",
        "constructors": {},
        "properties": {},
        "methods": {
            "next()\tLIST<SObject>": "next()$0",
            "hasNext()\tBoolean": "hasNext()$0"
        }
    },
    "icon": {
        "name": "Icon",
        "constructors": {},
        "properties": {
            "height": "height$0",
            "url": "url$0",
            "width": "width$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "pluginresult": {
        "name": "PluginResult",
        "constructors": {},
        "properties": {
            "outputParameters": "outputParameters$0"
        },
        "methods": {}

    },
    "records": {
        "name": "Records",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMotif(String communityId, String idOrPrefix)\tConnectApi.Motif": "getMotif($0)"
        }
    },
    "emailattachment": {
        "name": "EmailAttachment",
        "constructors": {},
        "properties": {},
        "methods": {}

    },
    "dmlexception": {
        "name": "DmlException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getCause()\tException": "getCause()$0",
            "getDmlFieldNames(Integer index)\tLIST<String>": "getDmlFieldNames($0)",
            "getDmlType(Integer index)\tsystem.StatusCode": "getDmlType($0)",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "getDmlStatusCode(Integer index)\tString": "getDmlStatusCode($0)",
            "getNumDml()\tInteger": "getNumDml()$0",
            "getDmlMessage(Integer index)\tString": "getDmlMessage($0)",
            "getMessage()\tString": "getMessage()$0",
            "getDmlFields(Integer index)\tLIST<Schema.SObjectField>": "getDmlFields($0)",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getDmlId(Integer index)\tString": "getDmlId($0)",
            "getDmlIndex(Integer index)\tInteger": "getDmlIndex($0)",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "chatterlike": {
        "name": "ChatterLike",
        "constructors": {},
        "properties": {
            "id": "id$0",
            "user": "user$0",
            "url": "url$0",
            "likedItem": "likedItem$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "feeditemattachment": {
        "name": "FeedItemAttachment",
        "constructors": {},
        "properties": {
            "type": "type$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "linkattachmentinput": {
        "name": "LinkAttachmentInput",
        "constructors": {},
        "properties": {
            "urlName": "urlName$0",
            "url": "url$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object": "convertToJavaObject($0)",
            "toString()\tString": "toString()$0"
        }
    },
    "statuscode": {
        "name": "StatusCode",
        "constructors": {},
        "properties": {
            "DUPLICATE_CASE_SOLUTION": "DUPLICATE_CASE_SOLUTION$0",
            "INVALID_TYPE_FOR_OPERATION": "INVALID_TYPE_FOR_OPERATION$0",
            "USER_OWNS_PORTAL_ACCOUNT_EXCEPTION": "USER_OWNS_PORTAL_ACCOUNT_EXCEPTION$0",
            "PACKAGE_LICENSE_REQUIRED": "PACKAGE_LICENSE_REQUIRED$0",
            "INVALID_SETUP_OWNER": "INVALID_SETUP_OWNER$0",
            "DELETE_REQUIRED_ON_CASCADE": "DELETE_REQUIRED_ON_CASCADE$0",
            "INVALID_TYPE": "INVALID_TYPE$0",
            "TEMPLATE_NOT_FOUND": "TEMPLATE_NOT_FOUND$0",
            "INVALID_ID_FIELD": "INVALID_ID_FIELD$0",
            "WEBLINK_SIZE_LIMIT_EXCEEDED": "WEBLINK_SIZE_LIMIT_EXCEEDED$0",
            "CANNOT_DISABLE_LAST_ADMIN": "CANNOT_DISABLE_LAST_ADMIN$0",
            "MISSING_ARGUMENT": "MISSING_ARGUMENT$0",
            "LIMIT_EXCEEDED": "LIMIT_EXCEEDED$0",
            "NUMBER_OUTSIDE_VALID_RANGE": "NUMBER_OUTSIDE_VALID_RANGE$0",
            "INVALID_ASSIGNMENT_RULE": "INVALID_ASSIGNMENT_RULE$0",
            "CUSTOM_TAB_LIMIT_EXCEEDED": "CUSTOM_TAB_LIMIT_EXCEEDED$0",
            "MANAGER_NOT_DEFINED": "MANAGER_NOT_DEFINED$0",
            "INVALID_DATA_CATEGORY_GROUP_REFERENCE": "INVALID_DATA_CATEGORY_GROUP_REFERENCE$0",
            "DUPLICATE_MASTER_LABEL": "DUPLICATE_MASTER_LABEL$0",
            "STORAGE_LIMIT_EXCEEDED": "STORAGE_LIMIT_EXCEEDED$0",
            "DUPLICATE_EXTERNAL_ID": "DUPLICATE_EXTERNAL_ID$0",
            "TRANSFER_REQUIRES_READ": "TRANSFER_REQUIRES_READ$0",
            "CANNOT_CASCADE_PRODUCT_ACTIVE": "CANNOT_CASCADE_PRODUCT_ACTIVE$0",
            "ENTITY_FAILED_IFLASTMODIFIED_ON_UPDATE": "ENTITY_FAILED_IFLASTMODIFIED_ON_UPDATE$0",
            "UNVERIFIED_SENDER_ADDRESS": "UNVERIFIED_SENDER_ADDRESS$0",
            "MAX_RULE_ENTRIES_EXCEEDED": "MAX_RULE_ENTRIES_EXCEEDED$0",
            "CANNOT_DEACTIVATE_DIVISION": "CANNOT_DEACTIVATE_DIVISION$0",
            "INVALID_CROSS_REFERENCE_KEY": "INVALID_CROSS_REFERENCE_KEY$0",
            "INVALID_OR_None_FOR_RESTRICTED_PICKLIST": "INVALID_OR_None_FOR_RESTRICTED_PICKLIST$0",
            "CIRCULAR_DEPENDENCY": "CIRCULAR_DEPENDENCY$0",
            "INVALID_CROSS_REFERENCE_TYPE_FOR_FIELD": "INVALID_CROSS_REFERENCE_TYPE_FOR_FIELD$0",
            "CANNOT_EXECUTE_FLOW_TRIGGER": "CANNOT_EXECUTE_FLOW_TRIGGER$0",
            "INVALID_MESSAGE_ID_REFERENCE": "INVALID_MESSAGE_ID_REFERENCE$0",
            "INSUFFICIENT_ACCESS_ON_CROSS_REFERENCE_ENTITY": "INSUFFICIENT_ACCESS_ON_CROSS_REFERENCE_ENTITY$0",
            "INVALID_ASSIGNEE_TYPE": "INVALID_ASSIGNEE_TYPE$0",
            "BCC_NOT_ALLOWED_IF_BCC_COMPLIANCE_ENABLED": "BCC_NOT_ALLOWED_IF_BCC_COMPLIANCE_ENABLED$0",
            "INVALID_BATCH_OPERATION": "INVALID_BATCH_OPERATION$0",
            "SINGLE_EMAIL_LIMIT_EXCEEDED": "SINGLE_EMAIL_LIMIT_EXCEEDED$0",
            "UNKNOWN_EXCEPTION": "UNKNOWN_EXCEPTION$0",
            "INVALID_CURRENCY_CORP_RATE": "INVALID_CURRENCY_CORP_RATE$0",
            "TEMPLATE_NOT_ACTIVE": "TEMPLATE_NOT_ACTIVE$0",
            "CANNOT_RENAME_APEX_REFERENCED_FIELD": "CANNOT_RENAME_APEX_REFERENCED_FIELD$0",
            "CANT_UNSET_CORP_CURRENCY": "CANT_UNSET_CORP_CURRENCY$0",
            "MAX_ACTIONS_PER_RULE_EXCEEDED": "MAX_ACTIONS_PER_RULE_EXCEEDED$0",
            "IMAGE_TOO_LARGE": "IMAGE_TOO_LARGE$0",
            "FILTERED_LOOKUP_LIMIT_EXCEEDED": "FILTERED_LOOKUP_LIMIT_EXCEEDED$0",
            "ASSIGNEE_TYPE_REQUIRED": "ASSIGNEE_TYPE_REQUIRED$0",
            "DUPLICATE_CUSTOM_TAB_MOTIF": "DUPLICATE_CUSTOM_TAB_MOTIF$0",
            "INVALID_PACKAGE_VERSION": "INVALID_PACKAGE_VERSION$0",
            "NO_INACTIVE_DIVISION_MEMBERS": "NO_INACTIVE_DIVISION_MEMBERS$0",
            "INVALID_CURRENCY_ISO": "INVALID_CURRENCY_ISO$0",
            "MERGE_FAILED": "MERGE_FAILED$0",
            "TEXT_DATA_OUTSIDE_SUPPORTED_CHARSET": "TEXT_DATA_OUTSIDE_SUPPORTED_CHARSET$0",
            "INVALID_PARTNER_NETWORK_STATUS": "INVALID_PARTNER_NETWORK_STATUS$0",
            "CANNOT_RENAME_REFERENCED_FIELD": "CANNOT_RENAME_REFERENCED_FIELD$0",
            "CANNOT_REPARENT_RECORD": "CANNOT_REPARENT_RECORD$0",
            "INSUFFICIENT_ACCESS_OR_READONLY": "INSUFFICIENT_ACCESS_OR_READONLY$0",
            "REQUIRED_FIELD_MISSING": "REQUIRED_FIELD_MISSING$0",
            "ALREADY_IN_PROCESS": "ALREADY_IN_PROCESS$0",
            "MAXIMUM_SIZE_OF_ATTACHMENT": "MAXIMUM_SIZE_OF_ATTACHMENT$0",
            "QUERY_TIMEOUT": "QUERY_TIMEOUT$0",
            "INVALID_CURRENCY_CONV_RATE": "INVALID_CURRENCY_CONV_RATE$0",
            "INVALID_FIELD_WHEN_USING_TEMPLATE": "INVALID_FIELD_WHEN_USING_TEMPLATE$0",
            "CANNOT_CREATE_ANOTHER_MANAGED_PACKAGE": "CANNOT_CREATE_ANOTHER_MANAGED_PACKAGE$0",
            "FAILED_ACTIVATION": "FAILED_ACTIVATION$0",
            "MAX_ACTIVE_RULES_EXCEEDED": "MAX_ACTIVE_RULES_EXCEEDED$0",
            "INVALID_SIGNUP_COUNTRY": "INVALID_SIGNUP_COUNTRY$0",
            "INVALID_INET_ADDRESS": "INVALID_INET_ADDRESS$0",
            "CANNOT_MODIFY_MANAGED_OBJECT": "CANNOT_MODIFY_MANAGED_OBJECT$0",
            "WEBLINK_URL_INVALID": "WEBLINK_URL_INVALID$0",
            "MAX_TASK_DESCRIPTION_EXCEEEDED": "MAX_TASK_DESCRIPTION_EXCEEEDED$0",
            "PRIVATE_CONTACT_ON_ASSET": "PRIVATE_CONTACT_ON_ASSET$0",
            "INVALID_CREDIT_CARD_INFO": "INVALID_CREDIT_CARD_INFO$0",
            "INVALID_ACCESS_LEVEL": "INVALID_ACCESS_LEVEL$0",
            "CANNOT_ENABLE_IP_RESTRICT_REQUESTS": "CANNOT_ENABLE_IP_RESTRICT_REQUESTS$0",
            "BAD_CUSTOM_ENTITY_PARENT_DOMAIN": "BAD_CUSTOM_ENTITY_PARENT_DOMAIN$0",
            "INVALID_READ_ONLY_USER_DML": "INVALID_READ_ONLY_USER_DML$0",
            "NONUNIQUE_SHIPPING_ADDRESS": "NONUNIQUE_SHIPPING_ADDRESS$0",
            "CANNOT_CHANGE_FIELD_TYPE_OF_APEX_REFERENCED_FIELD": "CANNOT_CHANGE_FIELD_TYPE_OF_APEX_REFERENCED_FIELD$0",
            "PACKAGING_API_INSTALL_FAILED": "PACKAGING_API_INSTALL_FAILED$0",
            "INVALID_FIELD": "INVALID_FIELD$0",
            "MALFORMED_ID": "MALFORMED_ID$0",
            "CHILD_SHARE_FAILS_PARENT": "CHILD_SHARE_FAILS_PARENT$0",
            "INVALID_STATUS": "INVALID_STATUS$0",
            "INVALID_EMAIL_ADDRESS": "INVALID_EMAIL_ADDRESS$0",
            "CANT_DISABLE_CORP_CURRENCY": "CANT_DISABLE_CORP_CURRENCY$0",
            "SHARE_NEEDED_FOR_CHILD_OWNER": "SHARE_NEEDED_FOR_CHILD_OWNER$0",
            "UNSPECIFIED_EMAIL_ADDRESS": "UNSPECIFIED_EMAIL_ADDRESS$0",
            "INVALID_OWNER": "INVALID_OWNER$0",
            "ENVIRONMENT_HUB_MEMBERSHIP_ERROR_JOINING_HUB": "ENVIRONMENT_HUB_MEMBERSHIP_ERROR_JOINING_HUB$0",
            "TOO_MANY_APEX_REQUESTS": "TOO_MANY_APEX_REQUESTS$0",
            "TERRITORY_REALIGN_IN_PROGRESS": "TERRITORY_REALIGN_IN_PROGRESS$0",
            "NUM_HISTORY_FIELDS_BY_SOBJECT_EXCEEDED": "NUM_HISTORY_FIELDS_BY_SOBJECT_EXCEEDED$0",
            "DUPLICATE_VALUE": "DUPLICATE_VALUE$0",
            "MAX_TM_RULE_ITEMS_EXCEEDED": "MAX_TM_RULE_ITEMS_EXCEEDED$0",
            "ENTITY_IS_LOCKED": "ENTITY_IS_LOCKED$0",
            "INVALID_GOOGLE_DOCS_URL": "INVALID_GOOGLE_DOCS_URL$0",
            "REQUIRED_FEATURE_MISSING": "REQUIRED_FEATURE_MISSING$0",
            "INVALID_OAUTH_URL": "INVALID_OAUTH_URL$0",
            "HTML_FILE_UPLOAD_NOT_ALLOWED": "HTML_FILE_UPLOAD_NOT_ALLOWED$0",
            "SELF_REFERENCE_FROM_FLOW": "SELF_REFERENCE_FROM_FLOW$0",
            "ERROR_IN_MAILER": "ERROR_IN_MAILER$0",
            "MAX_FORMULAS_PER_RULE_EXCEEDED": "MAX_FORMULAS_PER_RULE_EXCEEDED$0",
            "FIELD_FILTER_VALIDATION_EXCEPTION": "FIELD_FILTER_VALIDATION_EXCEPTION$0",
            "SELF_REFERENCE_FROM_TRIGGER": "SELF_REFERENCE_FROM_TRIGGER$0",
            "ALL_OR_NONE_OPERATION_ROLLED_BACK": "ALL_OR_NONE_OPERATION_ROLLED_BACK$0",
            "CUSTOM_INDEX_EXISTS": "CUSTOM_INDEX_EXISTS$0",
            "DELETE_FAILED": "DELETE_FAILED$0",
            "MAXIMUM_CCEMAILS_EXCEEDED": "MAXIMUM_CCEMAILS_EXCEEDED$0",
            "ENVIRONMENT_HUB_MEMBERSHIP_USER_ALREADY_IN_HUB": "ENVIRONMENT_HUB_MEMBERSHIP_USER_ALREADY_IN_HUB$0",
            "MAXIMUM_SIZE_OF_DOCUMENT": "MAXIMUM_SIZE_OF_DOCUMENT$0",
            "MIXED_DML_OPERATION": "MIXED_DML_OPERATION$0",
            "CANNOT_INSERT_UPDATE_ACTIVATE_ENTITY": "CANNOT_INSERT_UPDATE_ACTIVATE_ENTITY$0",
            "MAX_APPROVAL_STEPS_EXCEEDED": "MAX_APPROVAL_STEPS_EXCEEDED$0",
            "PORTAL_USER_ALREADY_EXISTS_FOR_CONTACT": "PORTAL_USER_ALREADY_EXISTS_FOR_CONTACT$0",
            "INVALID_EMPTY_KEY_OWNER": "INVALID_EMPTY_KEY_OWNER$0",
            "TABSET_LIMIT_EXCEEDED": "TABSET_LIMIT_EXCEEDED$0",
            "INVALID_TYPE_ON_FIELD_IN_RECORD": "INVALID_TYPE_ON_FIELD_IN_RECORD$0",
            "INVALID_PERSON_ACCOUNT_OPERATION": "INVALID_PERSON_ACCOUNT_OPERATION$0",
            "INVALID_QUERY_LOCATOR": "INVALID_QUERY_LOCATOR$0",
            "CUSTOM_ENTITY_OR_FIELD_LIMIT": "CUSTOM_ENTITY_OR_FIELD_LIMIT$0",
            "DUPLICATE_USERNAME": "DUPLICATE_USERNAME$0",
            "CANNOT_UPDATE_CONVERTED_LEAD": "CANNOT_UPDATE_CONVERTED_LEAD$0",
            "INVALID_OPERATOR": "INVALID_OPERATOR$0",
            "FIELD_CUSTOM_VALIDATION_EXCEPTION": "FIELD_CUSTOM_VALIDATION_EXCEPTION$0",
            "INACTIVE_OWNER_OR_USER": "INACTIVE_OWNER_OR_USER$0",
            "CUSTOM_LINK_LIMIT_EXCEEDED": "CUSTOM_LINK_LIMIT_EXCEEDED$0",
            "UNAVAILABLE_RECORDTYPE_EXCEPTION": "UNAVAILABLE_RECORDTYPE_EXCEPTION$0",
            "CANNOT_RENAME_REFERENCED_OBJECT": "CANNOT_RENAME_REFERENCED_OBJECT$0",
            "MASSMAIL_RETRY_LIMIT_EXCEEDED": "MASSMAIL_RETRY_LIMIT_EXCEEDED$0",
            "ENTITY_IS_DELETED": "ENTITY_IS_DELETED$0",
            "DUPLICATE_CUSTOM_ENTITY_DEFINITION": "DUPLICATE_CUSTOM_ENTITY_DEFINITION$0",
            "DEPENDENCY_EXISTS": "DEPENDENCY_EXISTS$0",
            "CANNOT_DELETE_MANAGED_OBJECT": "CANNOT_DELETE_MANAGED_OBJECT$0",
            "OPTED_OUT_OF_MASS_MAIL": "OPTED_OUT_OF_MASS_MAIL$0",
            "FIELD_INTEGRITY_EXCEPTION": "FIELD_INTEGRITY_EXCEPTION$0",
            "INVALID_FILTER_ACTION": "INVALID_FILTER_ACTION$0",
            "INVALID_DATA_URI": "INVALID_DATA_URI$0",
            "EMAIL_NOT_PROCESSED_DUE_TO_PRIOR_ERROR": "EMAIL_NOT_PROCESSED_DUE_TO_PRIOR_ERROR$0",
            "INVALID_SESSION_ID": "INVALID_SESSION_ID$0",
            "USER_WITH_APEX_SHARES_EXCEPTION": "USER_WITH_APEX_SHARES_EXCEPTION$0",
            "NO_ATTACHMENT_PERMISSION": "NO_ATTACHMENT_PERMISSION$0",
            "OP_WITH_INVALID_USER_TYPE_EXCEPTION": "OP_WITH_INVALID_USER_TYPE_EXCEPTION$0",
            "INVALID_CONTENT_TYPE": "INVALID_CONTENT_TYPE$0",
            "INVALID_MASTER_OR_TRANSLATED_SOLUTION": "INVALID_MASTER_OR_TRANSLATED_SOLUTION$0",
            "NO_APPLICABLE_PROCESS": "NO_APPLICABLE_PROCESS$0",
            "NO_SUCH_USER_EXISTS": "NO_SUCH_USER_EXISTS$0",
            "PORTAL_NO_ACCESS": "PORTAL_NO_ACCESS$0",
            "TOO_MANY_POSSIBLE_USERS_EXIST": "TOO_MANY_POSSIBLE_USERS_EXIST$0",
            "COLLISION_DETECTED": "COLLISION_DETECTED$0",
            "ENVIRONMENT_HUB_MEMBERSHIP_CONFLICT": "ENVIRONMENT_HUB_MEMBERSHIP_CONFLICT$0",
            "CUSTOM_FIELD_INDEX_LIMIT_EXCEEDED": "CUSTOM_FIELD_INDEX_LIMIT_EXCEEDED$0",
            "INVALID_ARGUMENT_TYPE": "INVALID_ARGUMENT_TYPE$0",
            "CUSTOM_CLOB_FIELD_LIMIT_EXCEEDED": "CUSTOM_CLOB_FIELD_LIMIT_EXCEEDED$0",
            "CANNOT_CHANGE_FIELD_TYPE_OF_REFERENCED_FIELD": "CANNOT_CHANGE_FIELD_TYPE_OF_REFERENCED_FIELD$0",
            "IP_RANGE_LIMIT_EXCEEDED": "IP_RANGE_LIMIT_EXCEEDED$0",
            "DUPLICATE_COMM_NICKNAME": "DUPLICATE_COMM_NICKNAME$0",
            "REQUEST_RUNNING_TOO_LONG": "REQUEST_RUNNING_TOO_LONG$0",
            "INVALID_LINEITEM_CLONE_STATE": "INVALID_LINEITEM_CLONE_STATE$0",
            "DUPLICATE_DEVELOPER_NAME": "DUPLICATE_DEVELOPER_NAME$0",
            "MASS_MAIL_LIMIT_EXCEEDED": "MASS_MAIL_LIMIT_EXCEEDED$0",
            "PACKAGING_API_UNINSTALL_FAILED": "PACKAGING_API_UNINSTALL_FAILED$0",
            "INVALID_FIELD_FOR_INSERT_UPDATE": "INVALID_FIELD_FOR_INSERT_UPDATE$0",
            "NO_MASS_MAIL_PERMISSION": "NO_MASS_MAIL_PERMISSION$0",
            "LICENSE_LIMIT_EXCEEDED": "LICENSE_LIMIT_EXCEEDED$0",
            "UNSUPPORTED_APEX_TRIGGER_OPERATON": "UNSUPPORTED_APEX_TRIGGER_OPERATON$0",
            "STANDARD_PRICE_NOT_DEFINED": "STANDARD_PRICE_NOT_DEFINED$0",
            "WRONG_CONTROLLER_TYPE": "WRONG_CONTROLLER_TYPE$0",
            "UNABLE_TO_LOCK_ROW": "UNABLE_TO_LOCK_ROW$0",
            "MAXIMUM_HIERARCHY_LEVELS_REACHED": "MAXIMUM_HIERARCHY_LEVELS_REACHED$0",
            "UNDELETE_FAILED": "UNDELETE_FAILED$0",
            "STRING_TOO_LONG": "STRING_TOO_LONG$0",
            "ENVIRONMENT_HUB_MEMBERSHIP_USER_NOT_ORG_ADMIN": "ENVIRONMENT_HUB_MEMBERSHIP_USER_NOT_ORG_ADMIN$0",
            "CANNOT_DELETE_LAST_DATED_CONVERSION_RATE": "CANNOT_DELETE_LAST_DATED_CONVERSION_RATE$0",
            "CUSTOM_METADATA_LIMIT_EXCEEDED": "CUSTOM_METADATA_LIMIT_EXCEEDED$0",
            "TOO_MANY_ENUM_VALUE": "TOO_MANY_ENUM_VALUE$0",
            "COMMUNITY_NOT_ACCESSIBLE": "COMMUNITY_NOT_ACCESSIBLE$0",
            "MAX_TM_RULES_EXCEEDED": "MAX_TM_RULES_EXCEEDED$0",
            "ENTITY_IS_ARCHIVED": "ENTITY_IS_ARCHIVED$0",
            "EMPTY_SCONTROL_FILE_NAME": "EMPTY_SCONTROL_FILE_NAME$0",
            "LIGHT_PORTAL_USER_EXCEPTION": "LIGHT_PORTAL_USER_EXCEPTION$0",
            "MAX_RULES_EXCEEDED": "MAX_RULES_EXCEEDED$0",
            "CANNOT_RENAME_APEX_REFERENCED_OBJECT": "CANNOT_RENAME_APEX_REFERENCED_OBJECT$0",
            "DELETE_OPERATION_TOO_LARGE": "DELETE_OPERATION_TOO_LARGE$0",
            "MAXIMUM_DASHBOARD_COMPONENTS_EXCEEDED": "MAXIMUM_DASHBOARD_COMPONENTS_EXCEEDED$0",
            "RECORD_IN_USE_BY_WORKFLOW": "RECORD_IN_USE_BY_WORKFLOW$0",
            "INVALID_OPERATION": "INVALID_OPERATION$0",
            "DUPLICATE_SENDER_DISPLAY_NAME": "DUPLICATE_SENDER_DISPLAY_NAME$0",
            "INVALID_SAVE_AS_ACTIVITY_FLAG": "INVALID_SAVE_AS_ACTIVITY_FLAG$0"
        },
        "methods": {
            "values()\tLIST<system.StatusCode>": "values()$0"
        }
    },
    "usersettings": {
        "name": "UserSettings",
        "constructors": {},
        "properties": {
            "canModifyAllData": "canModifyAllData$0",
            "canFollow": "canFollow$0",
            "userLocale": "userLocale$0",
            "canViewAllData": "canViewAllData$0",
            "canViewAllUsers": "canViewAllUsers$0",
            "hasFileSync": "hasFileSync$0",
            "externalUser": "externalUser$0",
            "approvalPosts": "approvalPosts$0",
            "currencySymbol": "currencySymbol$0",
            "canOwnGroups": "canOwnGroups$0",
            "canViewPublicFiles": "canViewPublicFiles$0",
            "userId": "userId$0",
            "userDefaultCurrencyIsoCode": "userDefaultCurrencyIsoCode$0",
            "canViewFullUserProfile": "canViewFullUserProfile$0",
            "canViewAllGroups": "canViewAllGroups$0",
            "hasAccessToInternalOrg": "hasAccessToInternalOrg$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "hashtagsegment": {
        "name": "HashtagSegment",
        "constructors": {},
        "properties": {
            "tag": "tag$0",
            "url": "url$0",
            "topicUrl": "topicUrl$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "feeditemattachmentinput": {
        "name": "FeedItemAttachmentInput",
        "constructors": {},
        "properties": {},
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "convertToJavaObject(java:common.api.AppVersion param1)\tjava:java.lang.Object": "convertToJavaObject($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "mentionsegmentinput": {
        "name": "MentionSegmentInput",
        "constructors": {},
        "properties": {
            "id": "id$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object": "convertToJavaObject($0)",
            "toString()\tString": "toString()$0"
        }
    },
    "feedfavorite": {
        "name": "FeedFavorite",
        "constructors": {},
        "properties": {
            "id": "id$0",
            "community": "community$0",
            "user": "user$0",
            "name": "name$0",
            "searchText": "searchText$0",
            "lastViewDate": "lastViewDate$0",
            "type": "type$0",
            "createdBy": "createdBy$0",
            "url": "url$0",
            "target": "target$0",
            "feedUrl": "feedUrl$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "xmlexception": {
        "name": "XmlException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "site": {
        "name": "Site",
        "constructors": {},
        "properties": {},
        "methods": {
            "getErrorMessage()\tString": "getErrorMessage()$0",
            "changePassword(String newPassword, String verifyNewPassword, String oldPassword)\tSystem.PageReference": "changePassword($0)",
            "createPortalUser(SObject user, String accountId, String password)\tId": "createPortalUser($0)",
            "createPortalUser(SObject user, String accountId, String password, Boolean sendEmailConfirmation)\tId": "createPortalUser($0)",
            "login(String username, String password, String startUrl)\tSystem.PageReference": "login($0)",
            "setPortalUserAsAuthProvider(SObject user, String accountId)\tvoid": "setPortalUserAsAuthProvider($0)",
            "isPasswordExpired()\tBoolean": "isPasswordExpired()$0",
            "getPrefix()\tString": "getPrefix()$0",
            "getAdminId()\tId": "getAdminId()$0",
            "getCurrentSiteUrl()\tString": "getCurrentSiteUrl()$0",
            "forgotPassword(String username)\tBoolean": "forgotPassword($0)",
            "isLoginEnabled()\tBoolean": "isLoginEnabled()$0",
            "createPortalUser(SObject user, String accountId)\tId": "createPortalUser($0)",
            "isRegistrationEnabled()\tBoolean": "isRegistrationEnabled()$0",
            "getDomain()\tString": "getDomain()$0",
            "getName()\tString": "getName()$0",
            "getErrorDescription()\tString": "getErrorDescription()$0",
            "createPersonAccountPortalUser(SObject user, String ownerId, String recordTypeId, String password)\tId": "createPersonAccountPortalUser($0)",
            "getOriginalUrl()\tString": "getOriginalUrl()$0",
            "changePassword(String newPassword, String verifyNewPassword)\tSystem.PageReference": "changePassword($0)",
            "getTemplate()\tSystem.PageReference": "getTemplate()$0",
            "getAdminEmail()\tString": "getAdminEmail()$0",
            "getCustomWebAddress()\tString": "getCustomWebAddress()$0",
            "getAnalyticsTrackingCode()\tString": "getAnalyticsTrackingCode()$0",
            "createPersonAccountPortalUser(SObject user, String ownerId, String password)\tId": "createPersonAccountPortalUser($0)"
        }
    },
    "contentattachment": {
        "name": "ContentAttachment",
        "constructors": {},
        "properties": {
            "id": "id$0",
            "renditionUrl": "renditionUrl$0",
            "fileExtension": "fileExtension$0",
            "title": "title$0",
            "downloadUrl": "downloadUrl$0",
            "hasImagePreview": "hasImagePreview$0",
            "isInMyFileSync": "isInMyFileSync$0",
            "hasPdfPreview": "hasPdfPreview$0",
            "description": "description$0",
            "fileType": "fileType$0",
            "checksum": "checksum$0",
            "mimeType": "mimeType$0",
            "fileSize": "fileSize$0",
            "versionId": "versionId$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "calloutexception": {
        "name": "CalloutException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "chatterlikepage": {
        "name": "ChatterLikePage",
        "constructors": {},
        "properties": {
            "total": "total$0",
            "previousPageToken": "previousPageToken$0",
            "nextPageUrl": "nextPageUrl$0",
            "nextPageToken": "nextPageToken$0",
            "currentPageToken": "currentPageToken$0",
            "previousPageUrl": "previousPageUrl$0",
            "currentPageUrl": "currentPageUrl$0",
            "likes": "likes$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "resourcelinksegment": {
        "name": "ResourceLinkSegment",
        "constructors": {},
        "properties": {
            "url": "url$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "asyncexception": {
        "name": "AsyncException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "nonepointerexception": {
        "name": "NonePointerException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "stringexception": {
        "name": "StringException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "sobjectfield": {
        "name": "SObjectField",
        "constructors": {},
        "properties": {},
        "methods": {
            "getDescribe()\tSchema.DescribeFieldResult": "getDescribe()$0"
        }
    },
    "invalidreadonlyuserdmlexception": {
        "name": "InvalidReadOnlyUserDmlException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "assertexception": {
        "name": "AssertException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "integer": {
        "name": "Integer",
        "constructors": {},
        "properties": {},
        "methods": {
            "addError(String msg, Boolean escape)\tvoid": "addError($0)",
            "valueOf(Object o)\tInteger": "valueOf($0)",
            "addError(APEX_OBJECT msg, Boolean escape)\tvoid": "addError($0)",
            "valueOf(String i)\tInteger": "valueOf($0)",
            "format()\tString": "format()$0",
            "addError(String msg)\tvoid": "addError($0)",
            "addError(APEX_OBJECT msg)\tvoid": "addError($0)"
        }
    },
    "commenttype": {
        "name": "CommentType",
        "constructors": {},
        "properties": {
            "TextComment": "TextComment$0",
            "ContentComment": "ContentComment$0"
        },
        "methods": {
            "values()\tLIST<ConnectApi.CommentType>": "values()$0"
        }
    },
    "emailexception": {
        "name": "EmailException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getCause()\tException": "getCause()$0",
            "getDmlFieldNames(Integer index)\tLIST<String>": "getDmlFieldNames($0)",
            "getDmlType(Integer index)\tsystem.StatusCode": "getDmlType($0)",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "getDmlStatusCode(Integer index)\tString": "getDmlStatusCode($0)",
            "getNumDml()\tInteger": "getNumDml()$0",
            "getDmlMessage(Integer index)\tString": "getDmlMessage($0)",
            "getMessage()\tString": "getMessage()$0",
            "getDmlFields(Integer index)\tLIST<Schema.SObjectField>": "getDmlFields($0)",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getDmlId(Integer index)\tString": "getDmlId($0)",
            "getDmlIndex(Integer index)\tInteger": "getDmlIndex($0)",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "matcher": {
        "name": "Matcher",
        "constructors": {},
        "properties": {},
        "methods": {
            "regionStart()\tInteger": "regionStart()$0",
            "quoteReplacement(String s)\tString": "quoteReplacement($0)",
            "requireEnd()\tBoolean": "requireEnd()$0",
            "matches()\tBoolean": "matches()$0",
            "end(Integer grp)\tInteger": "end($0)",
            "reset()\tsystem.Matcher": "reset()$0",
            "useTransparentBounds(Boolean b)\tsystem.Matcher": "useTransparentBounds($0)",
            "hitEnd()\tBoolean": "hitEnd()$0",
            "lookingAt()\tBoolean": "lookingAt()$0",
            "find(Integer start)\tBoolean": "find($0)",
            "useAnchoringBounds(Boolean b)\tsystem.Matcher": "useAnchoringBounds($0)",
            "replaceFirst(String replacement)\tString": "replaceFirst($0)",
            "group()\tString": "group()$0",
            "pattern()\tsystem.Pattern": "pattern()$0",
            "hasTransparentBounds()\tBoolean": "hasTransparentBounds()$0",
            "reset(String input)\tsystem.Matcher": "reset($0)",
            "regionEnd()\tInteger": "regionEnd()$0",
            "find()\tBoolean": "find()$0",
            "region(Integer start, Integer ending)\tsystem.Matcher": "region($0)",
            "start(Integer grp)\tInteger": "start($0)",
            "start()\tInteger": "start()$0",
            "group(Integer start)\tString": "group($0)",
            "hasAnchoringBounds()\tBoolean": "hasAnchoringBounds()$0",
            "usePattern(system.Pattern p)\tsystem.Matcher": "usePattern($0)",
            "replaceAll(String replacement)\tString": "replaceAll($0)",
            "end()\tInteger": "end()$0",
            "groupCount()\tInteger": "groupCount()$0"
        }
    },
    "blob": {
        "name": "Blob",
        "constructors": {},
        "properties": {},
        "methods": {
            "size()\tInteger": "size()$0",
            "valueOf(String o)\tBlob": "valueOf($0)",
            "toPdf(String o)\tBlob": "toPdf($0)",
            "toString()\tString": "toString()$0"
        }
    },
    "url": {
        "name": "Url",
        "constructors": {},
        "properties": {},
        "methods": {
            "sameFile(system.Url other)\tBoolean": "sameFile($0)",
            "getProtocol()\tString": "getProtocol()$0",
            "getCurrentRequestUrl()\tsystem.Url": "getCurrentRequestUrl()$0",
            "getFile()\tString": "getFile()$0",
            "getDefaultPort()\tInteger": "getDefaultPort()$0",
            "toExternalForm()\tString": "toExternalForm()$0",
            "getSalesforceBaseUrl()\tsystem.Url": "getSalesforceBaseUrl()$0",
            "getUserInfo()\tString": "getUserInfo()$0",
            "getAuthority()\tString": "getAuthority()$0",
            "getRef()\tString": "getRef()$0",
            "getFileFieldURL(String objectId, String fieldName)\tString": "getFileFieldURL($0)",
            "getQuery()\tString": "getQuery()$0",
            "getPort()\tInteger": "getPort()$0",
            "getHost()\tString": "getHost()$0",
            "getPath()\tString": "getPath()$0"
        }
    },
    "address": {
        "name": "Address",
        "constructors": {},
        "properties": {
            "formattedAddress": "formattedAddress$0",
            "zip": "zip$0",
            "street": "street$0",
            "city": "city$0",
            "state": "state$0",
            "country": "country$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "clientinfo": {
        "name": "ClientInfo",
        "constructors": {},
        "properties": {
            "applicationUrl": "applicationUrl$0",
            "applicationName": "applicationName$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "schema": {
        "name": "Schema",
        "constructors": {},
        "properties": {},
        "methods": {
            "getAppDescribe(String appName)\tMAP<String,Schema.SObjectType>": "getAppDescribe($0)",
            "getModuleDescribe(String moduleName)\tMAP<String,Schema.SObjectType>": "getModuleDescribe($0)",
            "getGlobalDescribe()\tMAP<String,Schema.SObjectType>": "getGlobalDescribe()$0",
            "describeDataCategoryGroups(LIST<String> sobjects)\tLIST<Schema.DescribeDataCategoryGroupResult>": "describeDataCategoryGroups($0)",
            "getModuleDescribe()\tMAP<String,Schema.SObjectType>": "getModuleDescribe()$0",
            "describeDataCategoryGroupStructures(LIST<Schema.DataCategoryGroupSobjectTypePair> pairs, Boolean topCategoriesOnly)\tLIST<Schema.DescribeDataCategoryGroupStructureResult>": "describeDataCategoryGroupStructures($0)"
        }
    },
    "linksegmentinput": {
        "name": "LinkSegmentInput",
        "constructors": {},
        "properties": {
            "url": "url$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object": "convertToJavaObject($0)",
            "toString()\tString": "toString()$0"
        }
    },
    "restrequest": {
        "name": "RestRequest",
        "constructors": {},
        "properties": {
            "remoteAddress": "remoteAddress$0",
            "params": "params$0",
            "httpMethod": "httpMethod$0",
            "resourcePath": "resourcePath$0",
            "requestBody": "requestBody$0",
            "requestURI": "requestURI$0",
            "headers": "headers$0"
        },
        "methods": {
            "addParameter(String name, String value)\tvoid": "addParameter($0)",
            "addHeader(String name, String value)\tvoid": "addHeader($0)"
        }
    },
    "mobilepushpayload": {
        "name": "MobilePushPayload",
        "constructors": {},
        "properties": {},
        "methods": {
            "apple(String alert, String sound, Integer badgeCount, MAP<String,ANY> userData)\tMAP<String,ANY>": "apple($0)",
            "apple(String alertBody, String actionLocKey, String locKey, LIST<String> locArgs, String launchImage, String sound, Integer badgeCount, MAP<String,ANY> userData)\tMAP<String,ANY>": "apple($0)"
        }
    },
    "invalidparametervalueexception": {
        "name": "InvalidParameterValueException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "messaging": {
        "name": "Messaging",
        "constructors": {},
        "properties": {},
        "methods": {
            "sendEmailMessage(LIST<Id> emailMessagesIds, Boolean allOrNothing)\tLIST<Messaging.SendEmailResult>": "sendEmailMessage($0)",
            "sendEmailMessage(LIST<Id> emailMessagesIds)\tLIST<Messaging.SendEmailResult>": "sendEmailMessage($0)",
            "reserveMassEmailCapacity(Integer count)\tvoid": "reserveMassEmailCapacity($0)",
            "reserveSingleEmailCapacity(Integer count)\tvoid": "reserveSingleEmailCapacity($0)",
            "sendEmail(LIST<Messaging.Email> emailMessages, Boolean allOrNothing)\tLIST<Messaging.SendEmailResult>": "sendEmail($0)",
            "sendEmail(LIST<Messaging.Email> emailMessages)\tLIST<Messaging.SendEmailResult>": "sendEmail($0)"
        }
    },
    "applicationreadwritemode": {
        "name": "ApplicationReadWriteMode",
        "constructors": {},
        "properties": {
            "READ_ONLY": "READ_ONLY$0",
            "DEFAULT": "DEFAULT$0"
        },
        "methods": {
            "values()\tLIST<system.ApplicationReadWriteMode>": "values()$0"
        }
    },
    "sparkplugparameter": {
        "name": "SparkPlugParameter",
        "constructors": {},
        "properties": {
            "required": "required$0",
            "name": "name$0",
            "parameterType": "parameterType$0"
        },
        "methods": {}

    },
    "sparkplugapi": {
        "name": "SparkPlugApi",
        "constructors": {},
        "properties": {},
        "methods": {
            "describePlugins()\tLIST<Process.SparkPlugApi.SparkPlugDescribeResult>": "describePlugins()$0",
            "invokePluginWithJson(String className, String parameters)\tString": "invokePluginWithJson($0)",
            "describePlugin(String className)\tProcess.SparkPlugApi.SparkPlugDescribeResult": "describePlugin($0)"
        }
    },
    "groupmembershiprequests": {
        "name": "GroupMembershipRequests",
        "constructors": {},
        "properties": {
            "total": "total$0",
            "requests": "requests$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "double": {
        "name": "Double",
        "constructors": {},
        "properties": {},
        "methods": {
            "addError(String msg, Boolean escape)\tvoid": "addError($0)",
            "addError(APEX_OBJECT msg, Boolean escape)\tvoid": "addError($0)",
            "intValue()\tInteger": "intValue()$0",
            "valueOf(String str)\tDouble": "valueOf($0)",
            "round()\tLong": "round()$0",
            "format()\tString": "format()$0",
            "valueOf(Object o)\tDouble": "valueOf($0)",
            "addError(String msg)\tvoid": "addError($0)",
            "longValue()\tLong": "longValue()$0",
            "addError(APEX_OBJECT msg)\tvoid": "addError($0)"
        }
    },
    "typeexception": {
        "name": "TypeException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "pagereference": {
        "name": "PageReference",
        "constructors": {},
        "properties": {},
        "methods": {
            "getRedirect()\tBoolean": "getRedirect()$0",
            "getUrl()\tString": "getUrl()$0",
            "getCookies()\tMAP<String,System.Cookie>": "getCookies()$0",
            "getAnchor()\tString": "getAnchor()$0",
            "getContent()\tBlob": "getContent()$0",
            "setRedirect(Boolean redirect)\tSystem.PageReference": "setRedirect($0)",
            "setCookies(LIST<System.Cookie> cookies)\tvoid": "setCookies($0)",
            "getHeaders()\tMAP<String,String>": "getHeaders()$0",
            "setAnchor(String anchor)\tSystem.PageReference": "setAnchor($0)",
            "getContentAsPDF()\tBlob": "getContentAsPDF()$0",
            "getParameters()\tMAP<String,String>": "getParameters()$0"
        }
    },
    "long": {
        "name": "Long",
        "constructors": {},
        "properties": {},
        "methods": {
            "addError(String msg, Boolean escape)\tvoid": "addError($0)",
            "addError(APEX_OBJECT msg, Boolean escape)\tvoid": "addError($0)",
            "intValue()\tInteger": "intValue()$0",
            "format()\tString": "format()$0",
            "valueOf(String str)\tLong": "valueOf($0)",
            "addError(String msg)\tvoid": "addError($0)",
            "addError(APEX_OBJECT msg)\tvoid": "addError($0)"
        }
    },
    "queryexception": {
        "name": "QueryException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "feed": {
        "name": "Feed",
        "constructors": {},
        "properties": {
            "isModifiedUrl": "isModifiedUrl$0",
            "feedItemsUrl": "feedItemsUrl$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "standardcontroller": {
        "name": "StandardController",
        "constructors": {},
        "properties": {},
        "methods": {
            "getSubject()\tSObject": "getSubject()$0",
            "getRecord()\tSObject": "getRecord()$0",
            "getId()\tString": "getId()$0",
            "view()\tSystem.PageReference": "view()$0",
            "reset()\tvoid": "reset()$0",
            "edit()\tSystem.PageReference": "edit()$0",
            "delete()\tSystem.PageReference": "delete()$0",
            "cancel()\tSystem.PageReference": "cancel()$0",
            "addFields(LIST<String> fieldNames)\tvoid": "addFields($0)",
            "save()\tSystem.PageReference": "save()$0"
        }
    },
    "binaryattachment": {
        "name": "BinaryAttachment",
        "constructors": {},
        "properties": {
            "body": "body$0",
            "fileName": "fileName$0",
            "mimeTypeSubType": "mimeTypeSubType$0"
        },
        "methods": {}

    },
    "mentionsegment": {
        "name": "MentionSegment",
        "constructors": {},
        "properties": {
            "user": "user$0",
            "name": "name$0",
            "accessible": "accessible$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "userdetail": {
        "name": "UserDetail",
        "constructors": {},
        "properties": {
            "phoneNumbers": "phoneNumbers$0",
            "isActive": "isActive$0",
            "managerId": "managerId$0",
            "groupCount": "groupCount$0",
            "email": "email$0",
            "chatterActivity": "chatterActivity$0",
            "address": "address$0",
            "followersCount": "followersCount$0",
            "chatterInfluence": "chatterInfluence$0",
            "followingCounts": "followingCounts$0",
            "managerName": "managerName$0",
            "username": "username$0",
            "aboutMe": "aboutMe$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "handledexception": {
        "name": "HandledException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "decimal": {
        "name": "Decimal",
        "constructors": {},
        "properties": {},
        "methods": {
            "longValue()\tLong": "longValue()$0",
            "toPlainString()\tString": "toPlainString()$0",
            "intValue()\tInteger": "intValue()$0",
            "doubleValue()\tDouble": "doubleValue()$0",
            "setScale(Integer scale)\tDecimal": "setScale($0)",
            "valueOf(String str)\tDecimal": "valueOf($0)",
            "pow(Integer exponent)\tDecimal": "pow($0)",
            "divide(Decimal divisor, Integer scale)\tDecimal": "divide($0)",
            "valueOf(Long lng)\tDecimal": "valueOf($0)",
            "stripTrailingZeros()\tDecimal": "stripTrailingZeros()$0",
            "valueOf(Double dbl)\tDecimal": "valueOf($0)",
            "setScale(Integer scale, system.RoundingMode roundingMode)\tDecimal": "setScale($0)",
            "precision()\tInteger": "precision()$0",
            "round(system.RoundingMode roundingMode)\tLong": "round($0)",
            "addError(String msg, Boolean escape)\tvoid": "addError($0)",
            "abs()\tDecimal": "abs()$0",
            "round()\tLong": "round()$0",
            "addError(APEX_OBJECT msg, Boolean escape)\tvoid": "addError($0)",
            "addError(APEX_OBJECT msg)\tvoid": "addError($0)",
            "scale()\tInteger": "scale()$0",
            "divide(Decimal divisor, Integer scale, APEX_OBJECT roundingMode)\tDecimal": "divide($0)",
            "format()\tString": "format()$0",
            "addError(String msg)\tvoid": "addError($0)"
        }
    },
    "publishingservice": {
        "name": "PublishingService",
        "constructors": {},
        "properties": {},
        "methods": {
            "completeTranslation(String articleVersionId)\tvoid": "completeTranslation($0)",
            "deleteArchivedArticleVersion(String articleId, Integer versionNumber)\tvoid": "deleteArchivedArticleVersion($0)",
            "setTranslationToIncomplete(String articleVersionId)\tvoid": "setTranslationToIncomplete($0)",
            "publishArticle(String articleId, Boolean flagAsNew)\tvoid": "publishArticle($0)",
            "deleteArchivedArticle(String articleId)\tvoid": "deleteArchivedArticle($0)",
            "assignDraftArticleTask(String articleId, String assigneeId, String instructions, Datetime dueDate, Boolean sendEmailNotification)\tvoid": "assignDraftArticleTask($0)",
            "editArchivedArticle(String articleId)\tString": "editArchivedArticle($0)",
            "restoreOldVersion(String articleId, Integer versionNumber)\tString": "restoreOldVersion($0)",
            "cancelScheduledArchivingOfArticle(String articleId)\tvoid": "cancelScheduledArchivingOfArticle($0)",
            "deleteDraftTranslation(String articleVersionId)\tvoid": "deleteDraftTranslation($0)",
            "editPublishedTranslation(String articleId, String language, Boolean unpublish)\tString": "editPublishedTranslation($0)",
            "deleteDraftArticle(String articleId)\tvoid": "deleteDraftArticle($0)",
            "archiveOnlineArticle(String articleId, Datetime scheduledDate)\tvoid": "archiveOnlineArticle($0)",
            "assignDraftTranslationTask(String translationVersionId, String assigneeId, String instructions, Datetime dueDate, Boolean sendEmailNotification)\tvoid": "assignDraftTranslationTask($0)",
            "scheduleForPublication(String articleId, Datetime scheduledDate)\tvoid": "scheduleForPublication($0)",
            "submitForTranslation(String articleId, String language, String assigneeId, Datetime dueDate)\tString": "submitForTranslation($0)",
            "editOnlineArticle(String articleId, Boolean unpublish)\tString": "editOnlineArticle($0)",
            "cancelScheduledPublicationOfArticle(String articleId)\tvoid": "cancelScheduledPublicationOfArticle($0)"
        }
    },
    "sobjectexception": {
        "name": "SObjectException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "stack": {
        "name": "Stack",
        "constructors": {},
        "properties": {},
        "methods": {
            "empty()\tBoolean": "empty()$0",
            "pop()\tString": "pop()$0",
            "peek()\tString": "peek()$0",
            "push(String item)\tvoid": "push($0)"
        }
    },
    "multistaticresourcecalloutmock": {
        "name": "MultiStaticResourceCalloutMock",
        "constructors": {},
        "properties": {},
        "methods": {
            "setHeader(String key, String val)\tvoid": "setHeader($0)",
            "setStatusCode(Integer code)\tvoid": "setStatusCode($0)",
            "respond(System.HttpRequest request)\tSystem.HttpResponse": "respond($0)",
            "setStaticResource(String url, String staticResourceName)\tvoid": "setStaticResource($0)",
            "setStatus(String status)\tvoid": "setStatus($0)"
        }
    },
    "communitypage": {
        "name": "CommunityPage",
        "constructors": {},
        "properties": {
            "total": "total$0",
            "communities": "communities$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "httpcalloutmock": {
        "name": "HttpCalloutMock",
        "constructors": {},
        "properties": {},
        "methods": {
            "respond(System.HttpRequest param1)\tSystem.HttpResponse": "respond($0)"
        }
    },
    "jsonparser": {
        "name": "JSONParser",
        "constructors": {},
        "properties": {},
        "methods": {
            "nextValue()\tsystem.JSONToken": "nextValue()$0",
            "getCurrentToken()\tsystem.JSONToken": "getCurrentToken()$0",
            "readValueAsStrict(system.Type apexType)\tObject": "readValueAsStrict($0)",
            "getBlobValue()\tBlob": "getBlobValue()$0",
            "getTimeValue()\tTime": "getTimeValue()$0",
            "getText()\tString": "getText()$0",
            "getBooleanValue()\tBoolean": "getBooleanValue()$0",
            "hasCurrentToken()\tBoolean": "hasCurrentToken()$0",
            "getDateValue()\tDate": "getDateValue()$0",
            "getLongValue()\tLong": "getLongValue()$0",
            "getDateTimeValue()\tDatetime": "getDateTimeValue()$0",
            "getLastClearedToken()\tsystem.JSONToken": "getLastClearedToken()$0",
            "getCurrentName()\tString": "getCurrentName()$0",
            "getDoubleValue()\tDouble": "getDoubleValue()$0",
            "skipChildren()\tvoid": "skipChildren()$0",
            "getDecimalValue()\tDecimal": "getDecimalValue()$0",
            "clearCurrentToken()\tvoid": "clearCurrentToken()$0",
            "getIntegerValue()\tInteger": "getIntegerValue()$0",
            "readValueAs(system.Type apexType)\tObject": "readValueAs($0)",
            "nextToken()\tsystem.JSONToken": "nextToken()$0",
            "getIdValue()\tId": "getIdValue()$0"
        }
    },
    "userinfo": {
        "name": "UserInfo",
        "constructors": {},
        "properties": {},
        "methods": {
            "getName()\tString": "getName()$0",
            "getUserEmail()\tString": "getUserEmail()$0",
            "getSessionId()\tString": "getSessionId()$0",
            "getLastName()\tString": "getLastName()$0",
            "getUserId()\tString": "getUserId()$0",
            "getUserRoleId()\tString": "getUserRoleId()$0",
            "getTimeZone()\tsystem.TimeZone": "getTimeZone()$0",
            "getDefaultCurrency()\tString": "getDefaultCurrency()$0",
            "getUserType()\tString": "getUserType()$0",
            "getUiThemeDisplayed()\tString": "getUiThemeDisplayed()$0",
            "getLocale()\tString": "getLocale()$0",
            "isCurrentUserLicensed(String namespacePrefix)\tBoolean": "isCurrentUserLicensed($0)",
            "getOrganizationName()\tString": "getOrganizationName()$0",
            "getLanguage()\tString": "getLanguage()$0",
            "isMultiCurrencyOrganization()\tBoolean": "isMultiCurrencyOrganization()$0",
            "getUserName()\tString": "getUserName()$0",
            "getFirstName()\tString": "getFirstName()$0",
            "getProfileId()\tString": "getProfileId()$0",
            "getOrganizationId()\tString": "getOrganizationId()$0",
            "getUiTheme()\tString": "getUiTheme()$0"
        }
    },
    "textattachment": {
        "name": "TextAttachment",
        "constructors": {},
        "properties": {
            "body": "body$0",
            "fileName": "fileName$0",
            "charset": "charset$0",
            "mimeTypeSubType": "mimeTypeSubType$0",
            "bodyIsTruncated": "bodyIsTruncated$0"
        },
        "methods": {}

    },
    "feeditempage": {
        "name": "FeedItemPage",
        "constructors": {},
        "properties": {
            "isModifiedToken": "isModifiedToken$0",
            "items": "items$0",
            "nextPageUrl": "nextPageUrl$0",
            "isModifiedUrl": "isModifiedUrl$0",
            "nextPageToken": "nextPageToken$0",
            "currentPageToken": "currentPageToken$0",
            "currentPageUrl": "currentPageUrl$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "hashtagsegmentinput": {
        "name": "HashtagSegmentInput",
        "constructors": {},
        "properties": {
            "tag": "tag$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object": "convertToJavaObject($0)",
            "toString()\tString": "toString()$0"
        }
    },
    "inboundemailresult": {
        "name": "InboundEmailResult",
        "constructors": {},
        "properties": {
            "message": "message$0",
            "success": "success$0"
        },
        "methods": {}

    },
    "linkattachment": {
        "name": "LinkAttachment",
        "constructors": {},
        "properties": {
            "url": "url$0",
            "title": "title$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "selectoption": {
        "name": "SelectOption",
        "constructors": {},
        "properties": {},
        "methods": {
            "getDisabled()\tBoolean": "getDisabled()$0",
            "setValue(String value)\tvoid": "setValue($0)",
            "getLabel()\tString": "getLabel()$0",
            "setEscapeItem(Boolean disabled)\tvoid": "setEscapeItem($0)",
            "getEscapeItem()\tBoolean": "getEscapeItem()$0",
            "setLabel(String label)\tvoid": "setLabel($0)",
            "getValue()\tString": "getValue()$0",
            "setDisabled(Boolean disabled)\tvoid": "setDisabled($0)"
        }
    },
    "binaryinput": {
        "name": "BinaryInput",
        "constructors": {},
        "properties": {},
        "methods": {
            "getContentType()\tString": "getContentType()$0",
            "getFilename()\tString": "getFilename()$0",
            "toString()\tString": "toString()$0",
            "getBlobValue()\tBlob": "getBlobValue()$0"
        }
    },
    "feedpollchoice": {
        "name": "FeedPollChoice",
        "constructors": {},
        "properties": {
            "id": "id$0",
            "text": "text$0",
            "voteCountRatio": "voteCountRatio$0",
            "position": "position$0",
            "voteCount": "voteCount$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "feeditemattachmenttype": {
        "name": "FeedItemAttachmentType",
        "constructors": {},
        "properties": {
            "Poll": "Poll$0",
            "Approval": "Approval$0",
            "DashboardComponent": "DashboardComponent$0",
            "Content": "Content$0",
            "Link": "Link$0",
            "BasicTemplate": "BasicTemplate$0",
            "CaseComment": "CaseComment$0"
        },
        "methods": {
            "values()\tLIST<ConnectApi.FeedItemAttachmentType>": "values()$0"
        }
    },
    "singleemailmessage": {
        "name": "SingleEmailMessage",
        "constructors": {},
        "properties": {},
        "methods": {}

    },
    "database": {
        "name": "Database",
        "constructors": {},
        "properties": {},
        "methods": {
            "undelete(LIST<SObject> sobjects, Boolean allOrNothing)\tLIST<Database.UndeleteResult>": "undelete($0)",
            "executeBatch(APEX_OBJECT batchable)\tString": "executeBatch($0)",
            "update(LIST<SObject> sobjects, APEX_OBJECT allOrNothing)\tLIST<Database.SaveResult>": "update($0)",
            "insert(SObject sobject, Boolean allOrNothing)\tDatabase.SaveResult": "insert($0)",
            "undelete(LIST<Id> ids)\tLIST<Database.UndeleteResult>": "undelete($0)",
            "delete(LIST<Id> ids)\tLIST<Database.DeleteResult>": "delete($0)",
            "insert(SObject sobject)\tDatabase.SaveResult": "insert($0)",
            "delete(Id id)\tDatabase.DeleteResult": "delete($0)",
            "delete(SObject sobject)\tDatabase.DeleteResult": "delete($0)",
            "emptyRecycleBin(LIST<SObject> sobjects)\tLIST<Database.EmptyRecycleBinResult>": "emptyRecycleBin($0)",
            "undelete(Id id)\tDatabase.UndeleteResult": "undelete($0)",
            "insert(LIST<SObject> sobjects)\tLIST<Database.SaveResult>": "insert($0)",
            "setSavepoint()\tSystem.Savepoint": "setSavepoint()$0",
            "undelete(SObject sobject, Boolean allOrNothing)\tDatabase.UndeleteResult": "undelete($0)",
            "upsert(SObject sobject, Boolean allOrNothing)\tDatabase.UpsertResult": "upsert($0)",
            "insert(SObject sobject, APEX_OBJECT DmlOptions)\tDatabase.SaveResult": "insert($0)",
            "executeBatch(APEX_OBJECT batchable, Integer batchSize)\tString": "executeBatch($0)",
            "upsert(LIST<SObject> sobjects, Boolean allOrNothing)\tLIST<Database.UpsertResult>": "upsert($0)",
            "upsert(LIST<SObject> sobjects, Schema.SObjectField field, Boolean allOrNothing)\tLIST<Database.UpsertResult>": "upsert($0)",
            "emptyRecycleBin(SObject sobject)\tDatabase.EmptyRecycleBinResult": "emptyRecycleBin($0)",
            "convertLead(Database.LeadConvert leadConvert)\tDatabase.LeadConvertResult": "convertLead($0)",
            "delete(LIST<SObject> sobjects)\tLIST<Database.DeleteResult>": "delete($0)",
            "undelete(LIST<Id> ids, Boolean allOrNothing)\tLIST<Database.UndeleteResult>": "undelete($0)",
            "delete(SObject sobject, Boolean allOrNothing)\tDatabase.DeleteResult": "delete($0)",
            "update(SObject sobject)\tDatabase.SaveResult": "update($0)",
            "update(SObject sobject, Boolean allOrNothing)\tDatabase.SaveResult": "update($0)",
            "delete(LIST<Id> ids, Boolean allOrNothing)\tLIST<Database.DeleteResult>": "delete($0)",
            "emptyRecycleBin(LIST<Id> ids)\tLIST<Database.EmptyRecycleBinResult>": "emptyRecycleBin($0)",
            "upsert(SObject sobject, Schema.SObjectField field, Boolean allOrNothing)\tDatabase.UpsertResult": "upsert($0)",
            "convertLead(LIST<Database.LeadConvert> leadConverts)\tLIST<Database.LeadConvertResult>": "convertLead($0)",
            "undelete(Id id, Boolean allOrNothing)\tDatabase.UndeleteResult": "undelete($0)",
            "getQueryLocator(LIST<SObject> query)\tDatabase.QueryLocator": "getQueryLocator($0)",
            "convertLead(LIST<Database.LeadConvert> leadConverts, Boolean allOrNothing)\tLIST<Database.LeadConvertResult>": "convertLead($0)",
            "insert(LIST<SObject> sobjects, APEX_OBJECT DmlOptions)\tLIST<Database.SaveResult>": "insert($0)",
            "insert(LIST<SObject> sobjects, Boolean allOrNothing)\tLIST<Database.SaveResult>": "insert($0)",
            "upsert(LIST<SObject> sobjects)\tLIST<Database.UpsertResult>": "upsert($0)",
            "delete(LIST<SObject> sobjects, Boolean allOrNothing)\tLIST<Database.DeleteResult>": "delete($0)",
            "undelete(SObject sobject)\tDatabase.UndeleteResult": "undelete($0)",
            "countQuery(String query)\tInteger": "countQuery($0)",
            "getQueryLocator(String query)\tDatabase.QueryLocator": "getQueryLocator($0)",
            "upsert(SObject sobject, Schema.SObjectField field)\tDatabase.UpsertResult": "upsert($0)",
            "update(LIST<SObject> sobjects)\tLIST<Database.SaveResult>": "update($0)",
            "update(LIST<SObject> sobjects, Boolean allOrNothing)\tLIST<Database.SaveResult>": "update($0)",
            "upsert(SObject sobject)\tDatabase.UpsertResult": "upsert($0)",
            "delete(Id id, Boolean allOrNothing)\tDatabase.DeleteResult": "delete($0)",
            "query(String query)\tLIST<SObject>": "query($0)",
            "undelete(LIST<SObject> sobjects)\tLIST<Database.UndeleteResult>": "undelete($0)",
            "convertLead(Database.LeadConvert leadConvert, Boolean allOrNothing)\tDatabase.LeadConvertResult": "convertLead($0)",
            "rollback(System.Savepoint savepoint)\tvoid": "rollback($0)",
            "upsert(LIST<SObject> sobjects, Schema.SObjectField field)\tLIST<Database.UpsertResult>": "upsert($0)",
            "update(SObject sobject, APEX_OBJECT allOrNothing)\tDatabase.SaveResult": "update($0)"
        }
    },
    "unauthenticateduser": {
        "name": "UnauthenticatedUser",
        "constructors": {},
        "properties": {},
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "filesummary": {
        "name": "FileSummary",
        "constructors": {},
        "properties": {
            "renditionUrl": "renditionUrl$0",
            "fileExtension": "fileExtension$0",
            "title": "title$0",
            "flashRenditionStatus": "flashRenditionStatus$0",
            "downloadUrl": "downloadUrl$0",
            "contentSize": "contentSize$0",
            "contentUrl": "contentUrl$0",
            "isInMyFileSync": "isInMyFileSync$0",
            "owner": "owner$0",
            "versionNumber": "versionNumber$0",
            "pdfRenditionStatus": "pdfRenditionStatus$0",
            "description": "description$0",
            "fileType": "fileType$0",
            "checksum": "checksum$0",
            "mimeType": "mimeType$0",
            "thumb720By480RenditionStatus": "thumb720By480RenditionStatus$0",
            "origin": "origin$0",
            "thumb120By90RenditionStatus": "thumb120By90RenditionStatus$0",
            "modifiedDate": "modifiedDate$0",
            "thumb240By180RenditionStatus": "thumb240By180RenditionStatus$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "webservicemock": {
        "name": "WebServiceMock",
        "constructors": {},
        "properties": {},
        "methods": {
            "doInvoke(Object param1, Object param2, MAP<String,ANY> param3, String param4, String param5, String param6, String param7, String param8, String param9)\tvoid": "doInvoke($0)"
        }
    },
    "jsongenerator": {
        "name": "JSONGenerator",
        "constructors": {},
        "properties": {},
        "methods": {
            "writeNoneField(String fieldName)\tvoid": "writeNoneField($0)",
            "writeTime(Time t)\tvoid": "writeTime($0)",
            "writeDateTimeField(String fieldName, Datetime dt)\tvoid": "writeDateTimeField($0)",
            "writeStartArray()\tvoid": "writeStartArray()$0",
            "writeBoolean(Boolean b)\tvoid": "writeBoolean($0)",
            "writeBooleanField(String fieldName, Boolean b)\tvoid": "writeBooleanField($0)",
            "writeNumber(Double d)\tvoid": "writeNumber($0)",
            "writeDateTime(Datetime dt)\tvoid": "writeDateTime($0)",
            "writeIdField(String fieldName, Id id)\tvoid": "writeIdField($0)",
            "writeObjectField(String fieldName, Object o)\tvoid": "writeObjectField($0)",
            "writeNumberField(String fieldName, Integer i)\tvoid": "writeNumberField($0)",
            "writeNumberField(String fieldName, Decimal d)\tvoid": "writeNumberField($0)",
            "writeNumberField(String fieldName, Double d)\tvoid": "writeNumberField($0)",
            "writeStartObject()\tvoid": "writeStartObject()$0",
            "writeBlobField(String fieldName, Blob b)\tvoid": "writeBlobField($0)",
            "writeBlob(Blob b)\tvoid": "writeBlob($0)",
            "writeNone()\tvoid": "writeNone()$0",
            "writeFieldName(String fieldName)\tvoid": "writeFieldName($0)",
            "getAsString()\tString": "getAsString()$0",
            "writeObject(Object o)\tvoid": "writeObject($0)",
            "writeDate(Date d)\tvoid": "writeDate($0)",
            "writeDateField(String fieldName, Date d)\tvoid": "writeDateField($0)",
            "close()\tvoid": "close()$0",
            "writeId(Id id)\tvoid": "writeId($0)",
            "writeEndArray()\tvoid": "writeEndArray()$0",
            "writeNumber(Decimal d)\tvoid": "writeNumber($0)",
            "writeNumber(Integer i)\tvoid": "writeNumber($0)",
            "isClosed()\tBoolean": "isClosed()$0",
            "writeTimeField(String fieldName, Time t)\tvoid": "writeTimeField($0)",
            "writeNumber(Long lng)\tvoid": "writeNumber($0)",
            "writeString(String str)\tvoid": "writeString($0)",
            "writeNumberField(String fieldName, Long lng)\tvoid": "writeNumberField($0)",
            "writeStringField(String fieldName, String str)\tvoid": "writeStringField($0)",
            "writeEndObject()\tvoid": "writeEndObject()$0"
        }
    },
    "answers": {
        "name": "Answers",
        "constructors": {},
        "properties": {},
        "methods": {
            "setBestReply(String questionId, String bestReplyId)\tvoid": "setBestReply($0)",
            "findSimilar(SObject question)\tLIST<Id>": "findSimilar($0)"
        }
    },
    "pluginrequest": {
        "name": "PluginRequest",
        "constructors": {},
        "properties": {
            "inputParameters": "inputParameters$0"
        },
        "methods": {}

    },
    "emailfileattachment": {
        "name": "EmailFileAttachment",
        "constructors": {},
        "properties": {},
        "methods": {}

    },
    "document": {
        "name": "Document",
        "constructors": {},
        "properties": {},
        "methods": {
            "getRootElement()\tdom.XmlNode": "getRootElement()$0",
            "toXmlString()\tString": "toXmlString()$0",
            "load(String xml)\tvoid": "load($0)",
            "createRootElement(String name, String namespace, String prefix)\tdom.XmlNode": "createRootElement($0)"
        }
    },
    "inboundemailhandler": {
        "name": "InboundEmailHandler",
        "constructors": {},
        "properties": {},
        "methods": {
            "handleInboundEmail(Messaging.InboundEmail param1, Messaging.InboundEnvelope param2)\tMessaging.InboundEmailResult": "handleInboundEmail($0)"
        }
    },
    "unsupportedoperationexception": {
        "name": "UnsupportedOperationException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "communities": {
        "name": "Communities",
        "constructors": {},
        "properties": {},
        "methods": {
            "getCommunity(String communityId)\tConnectApi.Community": "getCommunity($0)",
            "getCommunities(ConnectApi.CommunityStatus status)\tConnectApi.CommunityPage": "getCommunities($0)",
            "getCommunities()\tConnectApi.CommunityPage": "getCommunities()$0"
        }
    },
    "chattergrouppage": {
        "name": "ChatterGroupPage",
        "constructors": {},
        "properties": {
            "previousPageUrl": "previousPageUrl$0",
            "currentPageUrl": "currentPageUrl$0",
            "groups": "groups$0",
            "nextPageUrl": "nextPageUrl$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "newfileattachmentinput": {
        "name": "NewFileAttachmentInput",
        "constructors": {},
        "properties": {
            "description": "description$0",
            "title": "title$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object": "convertToJavaObject($0)",
            "toString()\tString": "toString()$0"
        }
    },
    "schedulablecontext": {
        "name": "SchedulableContext",
        "constructors": {},
        "properties": {},
        "methods": {
            "getTriggerId()\tId": "getTriggerId()$0"
        }
    },
    "listexception": {
        "name": "ListException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "requiredfeaturemissingexception": {
        "name": "RequiredFeatureMissingException",
        "constructors": {},
        "properties": {},
        "methods": {
            "getMessage()\tString": "getMessage()$0",
            "getStackTraceString()\tString": "getStackTraceString()$0",
            "getLineNumber()\tInteger": "getLineNumber()$0",
            "setMessage(String message)\tvoid": "setMessage($0)",
            "initCause(APEX_OBJECT cause)\tvoid": "initCause($0)",
            "getCause()\tException": "getCause()$0",
            "getTypeName()\tString": "getTypeName()$0"
        }
    },
    "component": {
        "name": "Component",
        "constructors": {},
        "properties": {
            "id": "id$0",
            "expressions": "expressions$0",
            "parent": "parent$0",
            "componentIterations": "componentIterations$0",
            "rendered": "rendered$0",
            "childComponents": "childComponents$0",
            "facets": "facets$0"
        },
        "methods": {
            "getComponentById(String id)\tApexPages.Component": "getComponentById($0)"
        }
    },
    "ideas": {
        "name": "Ideas",
        "constructors": {},
        "properties": {},
        "methods": {
            "findSimilar(SObject idea)\tLIST<Id>": "findSimilar($0)",
            "getReadRecentReplies(String userId, String communityId)\tLIST<Id>": "getReadRecentReplies($0)",
            "markRead(String ideaId)\tvoid": "markRead($0)",
            "getUnreadRecentReplies(String userId, String communityId)\tLIST<Id>": "getUnreadRecentReplies($0)",
            "getAllRecentReplies(String userId, String communityId)\tLIST<Id>": "getAllRecentReplies($0)"
        }
    },
    "commentinput": {
        "name": "CommentInput",
        "constructors": {},
        "properties": {
            "attachment": "attachment$0",
            "body": "body$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object": "convertToJavaObject($0)",
            "toString()\tString": "toString()$0"
        }
    },
    "datetime": {
        "name": "Datetime",
        "constructors": {},
        "properties": {},
        "methods": {
            "day()\tInteger": "day()$0",
            "newInstance(Date date, Time time)\tDatetime": "newInstance($0)",
            "newInstance(Integer year, Integer month, Integer day, Integer hour, Integer minute, Integer second)\tDatetime": "newInstance($0)",
            "format(String dateformat)\tString": "format($0)",
            "addSeconds(Integer seconds)\tDatetime": "addSeconds($0)",
            "time()\tTime": "time()$0",
            "timeGmt()\tTime": "timeGmt()$0",
            "now()\tDatetime": "now()$0",
            "dayOfYear()\tInteger": "dayOfYear()$0",
            "format(String dateformat, String timezone)\tString": "format($0)",
            "parse(String str)\tDatetime": "parse($0)",
            "newInstanceGmt(Integer year, Integer month, Integer day)\tDatetime": "newInstanceGmt($0)",
            "addHours(Integer hours)\tDatetime": "addHours($0)",
            "yearGmt()\tInteger": "yearGmt()$0",
            "minute()\tInteger": "minute()$0",
            "month()\tInteger": "month()$0",
            "minuteGmt()\tInteger": "minuteGmt()$0",
            "second()\tInteger": "second()$0",
            "newInstanceGmt(Date date, Time time)\tDatetime": "newInstanceGmt($0)",
            "addDays(Integer days)\tDatetime": "addDays($0)",
            "dayOfYearGmt()\tInteger": "dayOfYearGmt()$0",
            "newInstanceGmt(Integer year, Integer month, Integer day, Integer hour, Integer minute, Integer second)\tDatetime": "newInstanceGmt($0)",
            "addMonths(Integer months)\tDatetime": "addMonths($0)",
            "newInstance(Integer year, Integer month, Integer day)\tDatetime": "newInstance($0)",
            "isSameDay(Datetime other)\tBoolean": "isSameDay($0)",
            "format()\tString": "format()$0",
            "secondGmt()\tInteger": "secondGmt()$0",
            "valueOf(String str)\tDatetime": "valueOf($0)",
            "formatLong()\tString": "formatLong()$0",
            "millisecondGmt()\tInteger": "millisecondGmt()$0",
            "valueOfGmt(String str)\tDatetime": "valueOfGmt($0)",
            "year()\tInteger": "year()$0",
            "hour()\tInteger": "hour()$0",
            "date()\tDate": "date()$0",
            "monthGmt()\tInteger": "monthGmt()$0",
            "valueOf(Object o)\tDatetime": "valueOf($0)",
            "hourGmt()\tInteger": "hourGmt()$0",
            "addMinutes(Integer minutes)\tDatetime": "addMinutes($0)",
            "addYears(Integer years)\tDatetime": "addYears($0)",
            "formatGmt(String dateformat)\tString": "formatGmt($0)",
            "getTime()\tLong": "getTime()$0",
            "addError(String msg, Boolean escape)\tvoid": "addError($0)",
            "newInstance(Long time)\tDatetime": "newInstance($0)",
            "dayGmt()\tInteger": "dayGmt()$0",
            "addError(APEX_OBJECT msg, Boolean escape)\tvoid": "addError($0)",
            "addError(APEX_OBJECT msg)\tvoid": "addError($0)",
            "dateGmt()\tDate": "dateGmt()$0",
            "addError(String msg)\tvoid": "addError($0)",
            "millisecond()\tInteger": "millisecond()$0"
        }
    },
    "messagesegmentinput": {
        "name": "MessageSegmentInput",
        "constructors": {},
        "properties": {},
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "convertToJavaObject(java:common.api.AppVersion param1)\tjava:java.lang.Object": "convertToJavaObject($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "chattergroupsummary": {
        "name": "ChatterGroupSummary",
        "constructors": {},
        "properties": {
            "fileCount": "fileCount$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "groupinformation": {
        "name": "GroupInformation",
        "constructors": {},
        "properties": {
            "title": "title$0",
            "text": "text$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "reference": {
        "name": "Reference",
        "constructors": {},
        "properties": {
            "id": "id$0",
            "url": "url$0"
        },
        "methods": {
            "equals(Object obj)\tBoolean": "equals($0)",
            "hashCode()\tInteger": "hashCode()$0",
            "getBuildVersion()\tDouble": "getBuildVersion()$0",
            "toString()\tString": "toString()$0"
        }
    },
    "feeditemvisibilitytype": {
        "name": "FeedItemVisibilityType",
        "constructors": {},
        "properties": {
            "AllUsers": "AllUsers$0",
            "InternalUsers": "InternalUsers$0"
        },
        "methods": {
            "values()\tLIST<ConnectApi.FeedItemVisibilityType>": "values()$0"
        }
    },
    "componentiteration": {
        "name": "ComponentIteration",
        "constructors": {},
        "properties": {
            "parent": "parent$0",
            "iterationValue": "iterationValue$0",
            "childComponents": "childComponents$0"
        },
        "methods": {
            "getComponentById(String id)\tApexPages.Component": "getComponentById($0)"
        }
    }
}