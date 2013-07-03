apex_completions = {
    'AbstractMessageBody' : {
        'AbstractMessageBody.equals(Object obj) --> Boolean' : 'equals($0)',
        'AbstractMessageBody.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'AbstractMessageBody.hashCode() --> Integer' : 'hashCode()$0',
        'AbstractMessageBody.toString() --> String' : 'toString()$0'
    },
    'Action' : {
        'Action.getExpression() --> String' : 'getExpression()$0',
        'Action.invoke() --> System.PageReference' : 'invoke()$0'
    },
    'Actor' : {
        'Actor.equals(Object obj) --> Boolean' : 'equals($0)',
        'Actor.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'Actor.hashCode() --> Integer' : 'hashCode()$0',
        'Actor.toString() --> String' : 'toString()$0'
    },
    'ActorWithId' : {
        'ActorWithId.equals(Object obj) --> Boolean' : 'equals($0)',
        'ActorWithId.hashCode() --> Integer' : 'hashCode()$0',
        'ActorWithId.toString() --> String' : 'toString()$0'
    },
    'Address' : {
        'Address.equals(Object obj) --> Boolean' : 'equals($0)',
        'Address.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'Address.hashCode() --> Integer' : 'hashCode()$0',
        'Address.toString() --> String' : 'toString()$0'
    },
    'Answers' : {
        'Answers.findSimilar(SObject question) --> LIST<Id>' : 'findSimilar($0)',
        'Answers.setBestReply(String questionId, String bestReplyId) --> void' : 'setBestReply($0)'
    },
    'ApexPages' : {
        'ApexPages.addMessage(ApexPages.Message message) --> void' : 'addMessage($0)',
        'ApexPages.addMessages(APEX_OBJECT ex) --> void' : 'addMessages($0)',
        'ApexPages.currentPage() --> System.PageReference' : 'currentPage()$0',
        'ApexPages.getMessages() --> LIST<ApexPages.Message>' : 'getMessages()$0',
        'ApexPages.hasMessages() --> Boolean' : 'hasMessages()$0',
        'ApexPages.hasMessages(ApexPages.Severity severity) --> Boolean' : 'hasMessages($0)'
    },
    'AppExchange' : {
        'AppExchange.calculateListingPopularity(String testUserName, String testCronString) --> void' : 'calculateListingPopularity($0)',
        'AppExchange.createOrg(String firstName, String lastName, String companyName, String email, String language, String adminUserName, String packageId, String evalUserName, Boolean isExtension) --> String' : 'createOrg($0)',
        'AppExchange.createPortalUser(SObject user, String accountId) --> Id' : 'createPortalUser($0)',
        'AppExchange.createSession(String appExchangeOrgId, String portalId, String siteId, String portalUserId) --> String' : 'createSession($0)',
        'AppExchange.debug(String message) --> void' : 'debug($0)',
        'AppExchange.getAuthenticatingUrl(String page) --> String' : 'getAuthenticatingUrl($0)',
        'AppExchange.getConfig(String section, String key) --> String' : 'getConfig($0)',
        'AppExchange.getCookie(String name) --> String' : 'getCookie($0)',
        'AppExchange.getCrossInstanceEncryptedHash(Double appVersion, String value) --> String' : 'getCrossInstanceEncryptedHash($0)',
        'AppExchange.getInstalledPackageVersions(String orgId) --> LIST<String>' : 'getInstalledPackageVersions($0)',
        'AppExchange.getOrgName(String orgId) --> String' : 'getOrgName($0)',
        'AppExchange.getPackageManifest(String pkgVersionId) --> String' : 'getPackageManifest($0)',
        'AppExchange.getPortalAdminId() --> String' : 'getPortalAdminId()$0',
        'AppExchange.getPortalId() --> String' : 'getPortalId()$0',
        'AppExchange.getSiteId() --> String' : 'getSiteId()$0',
        'AppExchange.getTrialTemplates(String callerOrgId, String lmPkgId, String username) --> LIST<TrialTemplate>' : 'getTrialTemplates($0)',
        'AppExchange.isDuplicateUserName(String username) --> Boolean' : 'isDuplicateUserName($0)',
        'AppExchange.isGuestUser() --> Boolean' : 'isGuestUser()$0',
        'AppExchange.movedPermanently(String location) --> void' : 'movedPermanently($0)',
        'AppExchange.provisionPackageLicense(String orgId, String allPackageId, Integer numLicenses, Date expirationDate, String status) --> String' : 'provisionPackageLicense($0)',
        'AppExchange.registerPackageVersion(String pkgVersionId) --> Boolean' : 'registerPackageVersion($0)',
        'AppExchange.setCookie(String name, String value) --> void' : 'setCookie($0)',
        'AppExchange.setCookie(String name, String value, String cookieDomainName, Integer cookieAge) --> void' : 'setCookie($0)',
        'AppExchange.setDefaultLicenseTerms(String pkgVersionId, String orgId, String defaultLicenseStatus, Integer defaultLicenseLength, Integer defaultLicenseSeats) --> void' : 'setDefaultLicenseTerms($0)',
        'AppExchange.setHttpResponseStatus(Integer statusCode) --> void' : 'setHttpResponseStatus($0)',
        'AppExchange.setLicenseManagementOrganization(String pkgVersionId, String orgId, String username, String password) --> String' : 'setLicenseManagementOrganization($0)',
        'AppExchange.stopListingPopularityJob() --> void' : 'stopListingPopularityJob()$0',
        'AppExchange.to15(String id) --> String' : 'to15($0)',
        'AppExchange.to18(String id) --> String' : 'to18($0)',
        'AppExchange.updateSingleAsAdmin(SObject sobj) --> Database.SaveResult' : 'updateSingleAsAdmin($0)',
        'AppExchange.validateLMAInstalled(String username, String password) --> String' : 'validateLMAInstalled($0)',
        'AppExchange.validateOrgUser(String username, String password) --> String' : 'validateOrgUser($0)'
    },
    'ApplicationReadWriteMode' : {
        'ApplicationReadWriteMode.values() --> LIST<system.ApplicationReadWriteMode>' : 'values()$0'
    },
    'ApprovalAttachment' : {
        'ApprovalAttachment.equals(Object obj) --> Boolean' : 'equals($0)',
        'ApprovalAttachment.hashCode() --> Integer' : 'hashCode()$0',
        'ApprovalAttachment.toString() --> String' : 'toString()$0'
    },
    'ApprovalPostTemplateField' : {
        'ApprovalPostTemplateField.equals(Object obj) --> Boolean' : 'equals($0)',
        'ApprovalPostTemplateField.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'ApprovalPostTemplateField.hashCode() --> Integer' : 'hashCode()$0',
        'ApprovalPostTemplateField.toString() --> String' : 'toString()$0'
    },
    'AssertException' : {
        'AssertException.getCause() --> Exception' : 'getCause()$0',
        'AssertException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'AssertException.getMessage() --> String' : 'getMessage()$0',
        'AssertException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'AssertException.getTypeName() --> String' : 'getTypeName()$0',
        'AssertException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'AssertException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'AssignmentRuleHeader' : {},
    'AsyncException' : {
        'AsyncException.getCause() --> Exception' : 'getCause()$0',
        'AsyncException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'AsyncException.getMessage() --> String' : 'getMessage()$0',
        'AsyncException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'AsyncException.getTypeName() --> String' : 'getTypeName()$0',
        'AsyncException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'AsyncException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'BasicTemplateAttachment' : {
        'BasicTemplateAttachment.equals(Object obj) --> Boolean' : 'equals($0)',
        'BasicTemplateAttachment.hashCode() --> Integer' : 'hashCode()$0',
        'BasicTemplateAttachment.toString() --> String' : 'toString()$0'
    },
    'Batchable' : {
        'Batchable.execute(Database.BatchableContext param1, LIST<ANY> param2) --> void' : 'execute($0)',
        'Batchable.finish(Database.BatchableContext param1) --> void' : 'finish($0)',
        'Batchable.start(Database.BatchableContext param1) --> system.Iterable' : 'start($0)'
    },
    'BatchableContext' : {
        'BatchableContext.getChildJobId() --> Id' : 'getChildJobId()$0',
        'BatchableContext.getJobId() --> Id' : 'getJobId()$0'
    },
    'BatchableContextImpl' : {
        'BatchableContextImpl.getChildJobId() --> Id' : 'getChildJobId()$0',
        'BatchableContextImpl.getJobId() --> Id' : 'getJobId()$0'
    },
    'BinaryAttachment' : {},
    'BinaryInput' : {
        'BinaryInput.getBlobValue() --> Blob' : 'getBlobValue()$0',
        'BinaryInput.getContentType() --> String' : 'getContentType()$0',
        'BinaryInput.getFilename() --> String' : 'getFilename()$0',
        'BinaryInput.toString() --> String' : 'toString()$0'
    },
    'Blob' : {
        'Blob.size() --> Integer' : 'size()$0',
        'Blob.toPdf(String o) --> Blob' : 'toPdf($0)',
        'Blob.toString() --> String' : 'toString()$0',
        'Blob.valueOf(String o) --> Blob' : 'valueOf($0)'
    },
    'Boolean' : {
        'Boolean.addError(APEX_OBJECT msg) --> void' : 'addError($0)',
        'Boolean.addError(APEX_OBJECT msg, Boolean escape) --> void' : 'addError($0)',
        'Boolean.addError(String msg) --> void' : 'addError($0)',
        'Boolean.addError(String msg, Boolean escape) --> void' : 'addError($0)',
        'Boolean.valueOf(Object a) --> Boolean' : 'valueOf($0)'
    },
    'BusinessHours' : {
        'BusinessHours.add(Id businessHoursId, Datetime startDate, Long interval) --> Datetime' : 'add($0)',
        'BusinessHours.addGmt(Id businessHoursId, Datetime startDate, Long interval) --> Datetime' : 'addGmt($0)',
        'BusinessHours.diff(String businessHoursId, Datetime startDate, Datetime endDate) --> Long' : 'diff($0)'
    },
    'CURRENCY' : {
        'CURRENCY.format() --> String' : 'format()$0',
        'CURRENCY.formatAmount() --> String' : 'formatAmount()$0',
        'CURRENCY.newInstance(Decimal amount, String isoCode) --> CURRENCY' : 'newInstance($0)'
    },
    'CalloutException' : {
        'CalloutException.getCause() --> Exception' : 'getCause()$0',
        'CalloutException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'CalloutException.getMessage() --> String' : 'getMessage()$0',
        'CalloutException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'CalloutException.getTypeName() --> String' : 'getTypeName()$0',
        'CalloutException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'CalloutException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'CaseActorType' : {
        'CaseActorType.values() --> LIST<ConnectApi.CaseActorType>' : 'values()$0'
    },
    'CaseComment' : {
        'CaseComment.equals(Object obj) --> Boolean' : 'equals($0)',
        'CaseComment.hashCode() --> Integer' : 'hashCode()$0',
        'CaseComment.toString() --> String' : 'toString()$0'
    },
    'Cases' : {
        'Cases.getCaseIdFromEmailThreadId(String emailThreadId) --> Id' : 'getCaseIdFromEmailThreadId($0)'
    },
    'Chatter' : {
        'Chatter.deleteSubscription(String communityId, String subscriptionId) --> void' : 'deleteSubscription($0)',
        'Chatter.getFollowers(String communityId, String recordId) --> ConnectApi.FollowerPage' : 'getFollowers($0)',
        'Chatter.getFollowers(String communityId, String recordId, Integer pageParam, Integer pageSize) --> ConnectApi.FollowerPage' : 'getFollowers($0)',
        'Chatter.getSubscription(String communityId, String subscriptionId) --> ConnectApi.Subscription' : 'getSubscription($0)'
    },
    'ChatterActivity' : {
        'ChatterActivity.equals(Object obj) --> Boolean' : 'equals($0)',
        'ChatterActivity.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'ChatterActivity.hashCode() --> Integer' : 'hashCode()$0',
        'ChatterActivity.toString() --> String' : 'toString()$0'
    },
    'ChatterFavorites' : {
        'ChatterFavorites.addFavorite(String communityId, String subjectId, String searchText) --> ConnectApi.FeedFavorite' : 'addFavorite($0)',
        'ChatterFavorites.addRecordFavorite(String communityId, String subjectId, String targetId) --> ConnectApi.FeedFavorite' : 'addRecordFavorite($0)',
        'ChatterFavorites.deleteFavorite(String communityId, String subjectId, String favoriteId) --> void' : 'deleteFavorite($0)',
        'ChatterFavorites.getFavorite(String communityId, String subjectId, String favoriteId) --> ConnectApi.FeedFavorite' : 'getFavorite($0)',
        'ChatterFavorites.getFavorites(String communityId, String subjectId) --> ConnectApi.FeedFavorites' : 'getFavorites($0)',
        'ChatterFavorites.getFeedItems(String communityId, String subjectId, String favoriteId) --> ConnectApi.FeedItemPage' : 'getFeedItems($0)',
        'ChatterFavorites.getFeedItems(String communityId, String subjectId, String favoriteId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam) --> ConnectApi.FeedItemPage' : 'getFeedItems($0)',
        'ChatterFavorites.setTestGetFeedItems(String communityId, String subjectId, String favoriteId, ConnectApi.FeedItemPage result) --> void' : 'setTestGetFeedItems($0)',
        'ChatterFavorites.setTestGetFeedItems(String communityId, String subjectId, String favoriteId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result) --> void' : 'setTestGetFeedItems($0)',
        'ChatterFavorites.updateFavorite(String communityId, String subjectId, String favoriteId, Boolean updateLastViewDate) --> ConnectApi.FeedFavorite' : 'updateFavorite($0)'
    },
    'ChatterFeeds' : {
        'ChatterFeeds.deleteComment(String communityId, String commentId) --> void' : 'deleteComment($0)',
        'ChatterFeeds.deleteFeedItem(String communityId, String feedItemId) --> void' : 'deleteFeedItem($0)',
        'ChatterFeeds.deleteLike(String communityId, String likeId) --> void' : 'deleteLike($0)',
        'ChatterFeeds.getComment(String communityId, String commentId) --> ConnectApi.Comment' : 'getComment($0)',
        'ChatterFeeds.getCommentsForFeedItem(String communityId, String feedItemId) --> ConnectApi.CommentPage' : 'getCommentsForFeedItem($0)',
        'ChatterFeeds.getCommentsForFeedItem(String communityId, String feedItemId, String pageParam, Integer pageSize) --> ConnectApi.CommentPage' : 'getCommentsForFeedItem($0)',
        'ChatterFeeds.getFeed(String communityId, ConnectApi.FeedType feedType) --> ConnectApi.Feed' : 'getFeed($0)',
        'ChatterFeeds.getFeed(String communityId, ConnectApi.FeedType feedType, ConnectApi.FeedSortOrder sortParam) --> ConnectApi.Feed' : 'getFeed($0)',
        'ChatterFeeds.getFeed(String communityId, ConnectApi.FeedType feedType, String subjectId) --> ConnectApi.Feed' : 'getFeed($0)',
        'ChatterFeeds.getFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, ConnectApi.FeedSortOrder sortParam) --> ConnectApi.Feed' : 'getFeed($0)',
        'ChatterFeeds.getFeedItem(String communityId, String feedItemId) --> ConnectApi.FeedItem' : 'getFeedItem($0)',
        'ChatterFeeds.getFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType) --> ConnectApi.FeedItemPage' : 'getFeedItemsFromFeed($0)',
        'ChatterFeeds.getFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam) --> ConnectApi.FeedItemPage' : 'getFeedItemsFromFeed($0)',
        'ChatterFeeds.getFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String subjectId) --> ConnectApi.FeedItemPage' : 'getFeedItemsFromFeed($0)',
        'ChatterFeeds.getFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam) --> ConnectApi.FeedItemPage' : 'getFeedItemsFromFeed($0)',
        'ChatterFeeds.getFeedItemsFromFilterFeed(String communityId, String subjectId, String keyPrefix) --> ConnectApi.FeedItemPage' : 'getFeedItemsFromFilterFeed($0)',
        'ChatterFeeds.getFeedItemsFromFilterFeed(String communityId, String subjectId, String keyPrefix, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam) --> ConnectApi.FeedItemPage' : 'getFeedItemsFromFilterFeed($0)',
        'ChatterFeeds.getFeedPoll(String communityId, String feedItemId) --> ConnectApi.FeedPoll' : 'getFeedPoll($0)',
        'ChatterFeeds.getFilterFeed(String communityId, String subjectId, String keyPrefix) --> ConnectApi.Feed' : 'getFilterFeed($0)',
        'ChatterFeeds.getFilterFeed(String communityId, String subjectId, String keyPrefix, ConnectApi.FeedSortOrder sortParam) --> ConnectApi.Feed' : 'getFilterFeed($0)',
        'ChatterFeeds.getLike(String communityId, String likeId) --> ConnectApi.ChatterLike' : 'getLike($0)',
        'ChatterFeeds.getLikesForComment(String communityId, String commentId) --> ConnectApi.ChatterLikePage' : 'getLikesForComment($0)',
        'ChatterFeeds.getLikesForComment(String communityId, String commentId, Integer pageParam, Integer pageSize) --> ConnectApi.ChatterLikePage' : 'getLikesForComment($0)',
        'ChatterFeeds.getLikesForFeedItem(String communityId, String feedItemId) --> ConnectApi.ChatterLikePage' : 'getLikesForFeedItem($0)',
        'ChatterFeeds.getLikesForFeedItem(String communityId, String feedItemId, Integer pageParam, Integer pageSize) --> ConnectApi.ChatterLikePage' : 'getLikesForFeedItem($0)',
        'ChatterFeeds.isModified(String communityId, ConnectApi.FeedType feedType, String subjectId, String since) --> ConnectApi.FeedModifiedInfo' : 'isModified($0)',
        'ChatterFeeds.likeComment(String communityId, String commentId) --> ConnectApi.ChatterLike' : 'likeComment($0)',
        'ChatterFeeds.likeFeedItem(String communityId, String feedItemId) --> ConnectApi.ChatterLike' : 'likeFeedItem($0)',
        'ChatterFeeds.postComment(String communityId, String feedItemId, ConnectApi.CommentInput comment, ConnectApi.BinaryInput feedItemFileUpload) --> ConnectApi.Comment' : 'postComment($0)',
        'ChatterFeeds.postComment(String communityId, String feedItemId, String text) --> ConnectApi.Comment' : 'postComment($0)',
        'ChatterFeeds.postFeedItem(String communityId, ConnectApi.FeedType feedType, String subjectId, ConnectApi.FeedItemInput feedItem, ConnectApi.BinaryInput feedItemFileUpload) --> ConnectApi.FeedItem' : 'postFeedItem($0)',
        'ChatterFeeds.postFeedItem(String communityId, ConnectApi.FeedType feedType, String subjectId, String text) --> ConnectApi.FeedItem' : 'postFeedItem($0)',
        'ChatterFeeds.searchFeedItems(String communityId, String q) --> ConnectApi.FeedItemPage' : 'searchFeedItems($0)',
        'ChatterFeeds.searchFeedItems(String communityId, String q, ConnectApi.FeedSortOrder sortParam) --> ConnectApi.FeedItemPage' : 'searchFeedItems($0)',
        'ChatterFeeds.searchFeedItems(String communityId, String q, String pageParam, Integer pageSize) --> ConnectApi.FeedItemPage' : 'searchFeedItems($0)',
        'ChatterFeeds.searchFeedItems(String communityId, String q, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam) --> ConnectApi.FeedItemPage' : 'searchFeedItems($0)',
        'ChatterFeeds.searchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q) --> ConnectApi.FeedItemPage' : 'searchFeedItemsInFeed($0)',
        'ChatterFeeds.searchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String q) --> ConnectApi.FeedItemPage' : 'searchFeedItemsInFeed($0)',
        'ChatterFeeds.searchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q) --> ConnectApi.FeedItemPage' : 'searchFeedItemsInFeed($0)',
        'ChatterFeeds.searchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String q) --> ConnectApi.FeedItemPage' : 'searchFeedItemsInFeed($0)',
        'ChatterFeeds.searchFeedItemsInFilterFeed(String communityId, String subjectId, String keyPrefix, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q) --> ConnectApi.FeedItemPage' : 'searchFeedItemsInFilterFeed($0)',
        'ChatterFeeds.searchFeedItemsInFilterFeed(String communityId, String subjectId, String keyPrefix, String q) --> ConnectApi.FeedItemPage' : 'searchFeedItemsInFilterFeed($0)',
        'ChatterFeeds.setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, ConnectApi.FeedItemPage result) --> void' : 'setTestGetFeedItemsFromFeed($0)',
        'ChatterFeeds.setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result) --> void' : 'setTestGetFeedItemsFromFeed($0)',
        'ChatterFeeds.setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, ConnectApi.FeedItemPage result) --> void' : 'setTestGetFeedItemsFromFeed($0)',
        'ChatterFeeds.setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result) --> void' : 'setTestGetFeedItemsFromFeed($0)',
        'ChatterFeeds.setTestGetFeedItemsFromFilterFeed(String communityId, String subjectId, String keyPrefix, ConnectApi.FeedItemPage result) --> void' : 'setTestGetFeedItemsFromFilterFeed($0)',
        'ChatterFeeds.setTestGetFeedItemsFromFilterFeed(String communityId, String subjectId, String keyPrefix, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result) --> void' : 'setTestGetFeedItemsFromFilterFeed($0)',
        'ChatterFeeds.setTestSearchFeedItems(String communityId, String q, ConnectApi.FeedItemPage result) --> void' : 'setTestSearchFeedItems($0)',
        'ChatterFeeds.setTestSearchFeedItems(String communityId, String q, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result) --> void' : 'setTestSearchFeedItems($0)',
        'ChatterFeeds.setTestSearchFeedItems(String communityId, String q, String pageParam, Integer pageSize, ConnectApi.FeedItemPage result) --> void' : 'setTestSearchFeedItems($0)',
        'ChatterFeeds.setTestSearchFeedItems(String communityId, String q, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result) --> void' : 'setTestSearchFeedItems($0)',
        'ChatterFeeds.setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedItemPage result) --> void' : 'setTestSearchFeedItemsInFeed($0)',
        'ChatterFeeds.setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String q, ConnectApi.FeedItemPage result) --> void' : 'setTestSearchFeedItemsInFeed($0)',
        'ChatterFeeds.setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedItemPage result) --> void' : 'setTestSearchFeedItemsInFeed($0)',
        'ChatterFeeds.setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String q, ConnectApi.FeedItemPage result) --> void' : 'setTestSearchFeedItemsInFeed($0)',
        'ChatterFeeds.setTestSearchFeedItemsInFilterFeed(String communityId, String subjectId, String keyPrefix, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedItemPage result) --> void' : 'setTestSearchFeedItemsInFilterFeed($0)',
        'ChatterFeeds.setTestSearchFeedItemsInFilterFeed(String communityId, String subjectId, String keyPrefix, String q, ConnectApi.FeedItemPage result) --> void' : 'setTestSearchFeedItemsInFilterFeed($0)',
        'ChatterFeeds.shareFeedItem(String communityId, ConnectApi.FeedType feedType, String subjectId, String originalFeedItemId) --> ConnectApi.FeedItem' : 'shareFeedItem($0)',
        'ChatterFeeds.updateBookmark(String communityId, String feedItemId, Boolean isBookmarkedByCurrentUser) --> ConnectApi.FeedItem' : 'updateBookmark($0)',
        'ChatterFeeds.voteOnFeedPoll(String communityId, String feedItemId, String myChoiceId) --> ConnectApi.FeedPoll' : 'voteOnFeedPoll($0)'
    },
    'ChatterGroup' : {
        'ChatterGroup.equals(Object obj) --> Boolean' : 'equals($0)',
        'ChatterGroup.hashCode() --> Integer' : 'hashCode()$0',
        'ChatterGroup.toString() --> String' : 'toString()$0'
    },
    'ChatterGroupDetail' : {
        'ChatterGroupDetail.equals(Object obj) --> Boolean' : 'equals($0)',
        'ChatterGroupDetail.hashCode() --> Integer' : 'hashCode()$0',
        'ChatterGroupDetail.toString() --> String' : 'toString()$0'
    },
    'ChatterGroupInput' : {
        'ChatterGroupInput.convertToJavaObject(java:common.api.AppVersion currentVersion) --> java:java.lang.Object' : 'convertToJavaObject($0)',
        'ChatterGroupInput.equals(Object obj) --> Boolean' : 'equals($0)',
        'ChatterGroupInput.hashCode() --> Integer' : 'hashCode()$0',
        'ChatterGroupInput.toString() --> String' : 'toString()$0'
    },
    'ChatterGroupPage' : {
        'ChatterGroupPage.equals(Object obj) --> Boolean' : 'equals($0)',
        'ChatterGroupPage.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'ChatterGroupPage.hashCode() --> Integer' : 'hashCode()$0',
        'ChatterGroupPage.toString() --> String' : 'toString()$0'
    },
    'ChatterGroupSummary' : {
        'ChatterGroupSummary.equals(Object obj) --> Boolean' : 'equals($0)',
        'ChatterGroupSummary.hashCode() --> Integer' : 'hashCode()$0',
        'ChatterGroupSummary.toString() --> String' : 'toString()$0'
    },
    'ChatterGroups' : {
        'ChatterGroups.addMember(String communityId, String groupId, String userId) --> ConnectApi.GroupMember' : 'addMember($0)',
        'ChatterGroups.deleteMember(String communityId, String membershipId) --> void' : 'deleteMember($0)',
        'ChatterGroups.deletePhoto(String communityId, String groupId) --> void' : 'deletePhoto($0)',
        'ChatterGroups.follow(String communityId, String groupId, String subjectId) --> ConnectApi.Subscription' : 'follow($0)',
        'ChatterGroups.getFollowings(String communityId, String groupId) --> ConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterGroups.getFollowings(String communityId, String groupId, Integer pageParam) --> ConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterGroups.getFollowings(String communityId, String groupId, Integer pageParam, Integer pageSize) --> ConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterGroups.getFollowings(String communityId, String groupId, String filterType) --> ConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterGroups.getFollowings(String communityId, String groupId, String filterType, Integer pageParam) --> ConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterGroups.getFollowings(String communityId, String groupId, String filterType, Integer pageParam, Integer pageSize) --> ConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterGroups.getGroup(String communityId, String groupId) --> ConnectApi.ChatterGroupDetail' : 'getGroup($0)',
        'ChatterGroups.getGroupMembershipRequest(String communityId, String requestId) --> ConnectApi.GroupMembershipRequest' : 'getGroupMembershipRequest($0)',
        'ChatterGroups.getGroupMembershipRequests(String communityId, String groupId) --> ConnectApi.GroupMembershipRequests' : 'getGroupMembershipRequests($0)',
        'ChatterGroups.getGroupMembershipRequests(String communityId, String groupId, ConnectApi.GroupMembershipRequestStatus status) --> ConnectApi.GroupMembershipRequests' : 'getGroupMembershipRequests($0)',
        'ChatterGroups.getGroups(String communityId) --> ConnectApi.ChatterGroupPage' : 'getGroups($0)',
        'ChatterGroups.getGroups(String communityId, Integer pageParam, Integer pageSize) --> ConnectApi.ChatterGroupPage' : 'getGroups($0)',
        'ChatterGroups.getMember(String communityId, String membershipId) --> ConnectApi.GroupMember' : 'getMember($0)',
        'ChatterGroups.getMembers(String communityId, String groupId) --> ConnectApi.GroupMemberPage' : 'getMembers($0)',
        'ChatterGroups.getMembers(String communityId, String groupId, Integer pageParam, Integer pageSize) --> ConnectApi.GroupMemberPage' : 'getMembers($0)',
        'ChatterGroups.getMyChatterSettings(String communityId, String groupId) --> ConnectApi.GroupChatterSettings' : 'getMyChatterSettings($0)',
        'ChatterGroups.getPhoto(String communityId, String groupId) --> ConnectApi.Photo' : 'getPhoto($0)',
        'ChatterGroups.requestGroupMembership(String communityId, String groupId) --> ConnectApi.GroupMembershipRequest' : 'requestGroupMembership($0)',
        'ChatterGroups.searchGroups(String communityId, String q) --> ConnectApi.ChatterGroupPage' : 'searchGroups($0)',
        'ChatterGroups.searchGroups(String communityId, String q, Integer pageParam, Integer pageSize) --> ConnectApi.ChatterGroupPage' : 'searchGroups($0)',
        'ChatterGroups.setPhoto(String communityId, String groupId, ConnectApi.BinaryInput fileUpload) --> ConnectApi.Photo' : 'setPhoto($0)',
        'ChatterGroups.setPhoto(String communityId, String groupId, String fileId, Integer versionNumber) --> ConnectApi.Photo' : 'setPhoto($0)',
        'ChatterGroups.setTestSearchGroups(String communityId, String q, ConnectApi.ChatterGroupPage result) --> void' : 'setTestSearchGroups($0)',
        'ChatterGroups.setTestSearchGroups(String communityId, String q, Integer pageParam, Integer pageSize, ConnectApi.ChatterGroupPage result) --> void' : 'setTestSearchGroups($0)',
        'ChatterGroups.updateGroup(String communityId, String groupId, ConnectApi.ChatterGroupInput groupInput) --> ConnectApi.ChatterGroupDetail' : 'updateGroup($0)',
        'ChatterGroups.updateMyChatterSettings(String communityId, String groupId, ConnectApi.GroupEmailFrequency emailFrequency) --> ConnectApi.GroupChatterSettings' : 'updateMyChatterSettings($0)',
        'ChatterGroups.updateRequestStatus(String communityId, String requestId, ConnectApi.GroupMembershipRequestStatus status) --> ConnectApi.GroupMembershipRequest' : 'updateRequestStatus($0)'
    },
    'ChatterLike' : {
        'ChatterLike.equals(Object obj) --> Boolean' : 'equals($0)',
        'ChatterLike.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'ChatterLike.hashCode() --> Integer' : 'hashCode()$0',
        'ChatterLike.toString() --> String' : 'toString()$0'
    },
    'ChatterLikePage' : {
        'ChatterLikePage.equals(Object obj) --> Boolean' : 'equals($0)',
        'ChatterLikePage.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'ChatterLikePage.hashCode() --> Integer' : 'hashCode()$0',
        'ChatterLikePage.toString() --> String' : 'toString()$0'
    },
    'ChatterUsers' : {
        'ChatterUsers.deletePhoto(String communityId, String userId) --> void' : 'deletePhoto($0)',
        'ChatterUsers.follow(String communityId, String userId, String subjectId) --> ConnectApi.Subscription' : 'follow($0)',
        'ChatterUsers.getChatterSettings(String communityId, String userId) --> ConnectApi.UserChatterSettings' : 'getChatterSettings($0)',
        'ChatterUsers.getFollowers(String communityId, String userId) --> ConnectApi.FollowerPage' : 'getFollowers($0)',
        'ChatterUsers.getFollowers(String communityId, String userId, Integer pageParam, Integer pageSize) --> ConnectApi.FollowerPage' : 'getFollowers($0)',
        'ChatterUsers.getFollowings(String communityId, String userId) --> ConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterUsers.getFollowings(String communityId, String userId, Integer pageParam) --> ConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterUsers.getFollowings(String communityId, String userId, Integer pageParam, Integer pageSize) --> ConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterUsers.getFollowings(String communityId, String userId, String filterType) --> ConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterUsers.getFollowings(String communityId, String userId, String filterType, Integer pageParam) --> ConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterUsers.getFollowings(String communityId, String userId, String filterType, Integer pageParam, Integer pageSize) --> ConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterUsers.getGroups(String communityId, String userId) --> ConnectApi.UserGroupPage' : 'getGroups($0)',
        'ChatterUsers.getGroups(String communityId, String userId, Integer pageParam, Integer pageSize) --> ConnectApi.UserGroupPage' : 'getGroups($0)',
        'ChatterUsers.getPhoto(String communityId, String userId) --> ConnectApi.Photo' : 'getPhoto($0)',
        'ChatterUsers.getUser(String communityId, String userId) --> ConnectApi.UserDetail' : 'getUser($0)',
        'ChatterUsers.getUsers(String communityId) --> ConnectApi.UserPage' : 'getUsers($0)',
        'ChatterUsers.getUsers(String communityId, Integer pageParam, Integer pageSize) --> ConnectApi.UserPage' : 'getUsers($0)',
        'ChatterUsers.searchUsers(String communityId, String q) --> ConnectApi.UserPage' : 'searchUsers($0)',
        'ChatterUsers.searchUsers(String communityId, String q, Integer pageParam, Integer pageSize) --> ConnectApi.UserPage' : 'searchUsers($0)',
        'ChatterUsers.searchUsers(String communityId, String q, String searchContextId, Integer pageParam, Integer pageSize) --> ConnectApi.UserPage' : 'searchUsers($0)',
        'ChatterUsers.setPhoto(String communityId, String userId, ConnectApi.BinaryInput fileUpload) --> ConnectApi.Photo' : 'setPhoto($0)',
        'ChatterUsers.setPhoto(String communityId, String userId, String fileId, Integer versionNumber) --> ConnectApi.Photo' : 'setPhoto($0)',
        'ChatterUsers.setTestSearchUsers(String communityId, String q, ConnectApi.UserPage result) --> void' : 'setTestSearchUsers($0)',
        'ChatterUsers.setTestSearchUsers(String communityId, String q, Integer pageParam, Integer pageSize, ConnectApi.UserPage result) --> void' : 'setTestSearchUsers($0)',
        'ChatterUsers.setTestSearchUsers(String communityId, String q, String searchContextId, Integer pageParam, Integer pageSize, ConnectApi.UserPage result) --> void' : 'setTestSearchUsers($0)',
        'ChatterUsers.updateChatterSettings(String communityId, String userId, ConnectApi.GroupEmailFrequency defaultGroupEmailFrequency) --> ConnectApi.UserChatterSettings' : 'updateChatterSettings($0)'
    },
    'ClientInfo' : {
        'ClientInfo.equals(Object obj) --> Boolean' : 'equals($0)',
        'ClientInfo.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'ClientInfo.hashCode() --> Integer' : 'hashCode()$0',
        'ClientInfo.toString() --> String' : 'toString()$0'
    },
    'Comment' : {
        'Comment.equals(Object obj) --> Boolean' : 'equals($0)',
        'Comment.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'Comment.hashCode() --> Integer' : 'hashCode()$0',
        'Comment.toString() --> String' : 'toString()$0'
    },
    'CommentInput' : {
        'CommentInput.convertToJavaObject(java:common.api.AppVersion currentVersion) --> java:java.lang.Object' : 'convertToJavaObject($0)',
        'CommentInput.equals(Object obj) --> Boolean' : 'equals($0)',
        'CommentInput.hashCode() --> Integer' : 'hashCode()$0',
        'CommentInput.toString() --> String' : 'toString()$0'
    },
    'CommentPage' : {
        'CommentPage.equals(Object obj) --> Boolean' : 'equals($0)',
        'CommentPage.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'CommentPage.hashCode() --> Integer' : 'hashCode()$0',
        'CommentPage.toString() --> String' : 'toString()$0'
    },
    'CommentType' : {
        'CommentType.values() --> LIST<ConnectApi.CommentType>' : 'values()$0'
    },
    'Communities' : {
        'Communities.getCommunities() --> ConnectApi.CommunityPage' : 'getCommunities()$0',
        'Communities.getCommunities(ConnectApi.CommunityStatus status) --> ConnectApi.CommunityPage' : 'getCommunities($0)',
        'Communities.getCommunity(String communityId) --> ConnectApi.Community' : 'getCommunity($0)'
    },
    'Community' : {
        'Community.equals(Object obj) --> Boolean' : 'equals($0)',
        'Community.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'Community.hashCode() --> Integer' : 'hashCode()$0',
        'Community.toString() --> String' : 'toString()$0'
    },
    'CommunityPage' : {
        'CommunityPage.equals(Object obj) --> Boolean' : 'equals($0)',
        'CommunityPage.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'CommunityPage.hashCode() --> Integer' : 'hashCode()$0',
        'CommunityPage.toString() --> String' : 'toString()$0'
    },
    'CommunityStatus' : {
        'CommunityStatus.values() --> LIST<ConnectApi.CommunityStatus>' : 'values()$0'
    },
    'Comparable' : {
        'Comparable.compareTo(Object param1) --> Integer' : 'compareTo($0)'
    },
    'ComplexSegment' : {
        'ComplexSegment.equals(Object obj) --> Boolean' : 'equals($0)',
        'ComplexSegment.hashCode() --> Integer' : 'hashCode()$0',
        'ComplexSegment.toString() --> String' : 'toString()$0'
    },
    'Component' : {
        'Component.getComponentById(String id) --> ApexPages.Component' : 'getComponentById($0)'
    },
    'ComponentIteration' : {
        'ComponentIteration.getComponentById(String id) --> ApexPages.Component' : 'getComponentById($0)'
    },
    'ConnectApiException' : {
        'ConnectApiException.getErrorCode() --> String' : 'getErrorCode()$0',
        'ConnectApiException.getTypeName() --> String' : 'getTypeName()$0'
    },
    'ContentAttachment' : {
        'ContentAttachment.equals(Object obj) --> Boolean' : 'equals($0)',
        'ContentAttachment.hashCode() --> Integer' : 'hashCode()$0',
        'ContentAttachment.toString() --> String' : 'toString()$0'
    },
    'ContentAttachmentInput' : {
        'ContentAttachmentInput.convertToJavaObject(java:common.api.AppVersion currentVersion) --> java:java.lang.Object' : 'convertToJavaObject($0)',
        'ContentAttachmentInput.equals(Object obj) --> Boolean' : 'equals($0)',
        'ContentAttachmentInput.hashCode() --> Integer' : 'hashCode()$0',
        'ContentAttachmentInput.toString() --> String' : 'toString()$0'
    },
    'Cookie' : {
        'Cookie.getDomain() --> String' : 'getDomain()$0',
        'Cookie.getMaxAge() --> Integer' : 'getMaxAge()$0',
        'Cookie.getName() --> String' : 'getName()$0',
        'Cookie.getPath() --> String' : 'getPath()$0',
        'Cookie.getValue() --> String' : 'getValue()$0',
        'Cookie.isSecure() --> Boolean' : 'isSecure()$0'
    },
    'Crypto' : {
        'Crypto.decrypt(String algorithmName, Blob secretKey, Blob initializationVector, Blob encryptedData) --> Blob' : 'decrypt($0)',
        'Crypto.decryptWithManagedIV(String algorithmName, Blob secretKey, Blob encryptedData) --> Blob' : 'decryptWithManagedIV($0)',
        'Crypto.encrypt(String algorithmName, Blob secretKey, Blob initializationVector, Blob clearData) --> Blob' : 'encrypt($0)',
        'Crypto.encryptWithManagedIV(String algorithmName, Blob secretKey, Blob clearData) --> Blob' : 'encryptWithManagedIV($0)',
        'Crypto.generateAesKey(Integer size) --> Blob' : 'generateAesKey($0)',
        'Crypto.generateDigest(String algorithmName, Blob input) --> Blob' : 'generateDigest($0)',
        'Crypto.generateMac(String algorithmName, Blob input, Blob privateKey) --> Blob' : 'generateMac($0)',
        'Crypto.getRandomInteger() --> Integer' : 'getRandomInteger()$0',
        'Crypto.getRandomLong() --> Long' : 'getRandomLong()$0',
        'Crypto.sign(String algorithmName, Blob input, Blob privateKey) --> Blob' : 'sign($0)'
    },
    'DMLOptions' : {},
    'DashboardComponentAttachment' : {
        'DashboardComponentAttachment.equals(Object obj) --> Boolean' : 'equals($0)',
        'DashboardComponentAttachment.hashCode() --> Integer' : 'hashCode()$0',
        'DashboardComponentAttachment.toString() --> String' : 'toString()$0'
    },
    'DataCategoryGroupSobjectTypePair' : {},
    'Database' : {
        'Database.convertLead(Database.LeadConvert leadConvert) --> Database.LeadConvertResult' : 'convertLead($0)',
        'Database.convertLead(Database.LeadConvert leadConvert, Boolean allOrNothing) --> Database.LeadConvertResult' : 'convertLead($0)',
        'Database.convertLead(LIST<Database.LeadConvert> leadConverts) --> LIST<Database.LeadConvertResult>' : 'convertLead($0)',
        'Database.convertLead(LIST<Database.LeadConvert> leadConverts, Boolean allOrNothing) --> LIST<Database.LeadConvertResult>' : 'convertLead($0)',
        'Database.countQuery(String query) --> Integer' : 'countQuery($0)',
        'Database.delete(Id id) --> Database.DeleteResult' : 'delete($0)',
        'Database.delete(Id id, Boolean allOrNothing) --> Database.DeleteResult' : 'delete($0)',
        'Database.delete(LIST<Id> ids) --> LIST<Database.DeleteResult>' : 'delete($0)',
        'Database.delete(LIST<Id> ids, Boolean allOrNothing) --> LIST<Database.DeleteResult>' : 'delete($0)',
        'Database.delete(LIST<SObject> sobjects) --> LIST<Database.DeleteResult>' : 'delete($0)',
        'Database.delete(LIST<SObject> sobjects, Boolean allOrNothing) --> LIST<Database.DeleteResult>' : 'delete($0)',
        'Database.delete(SObject sobject) --> Database.DeleteResult' : 'delete($0)',
        'Database.delete(SObject sobject, Boolean allOrNothing) --> Database.DeleteResult' : 'delete($0)',
        'Database.emptyRecycleBin(LIST<Id> ids) --> LIST<Database.EmptyRecycleBinResult>' : 'emptyRecycleBin($0)',
        'Database.emptyRecycleBin(LIST<SObject> sobjects) --> LIST<Database.EmptyRecycleBinResult>' : 'emptyRecycleBin($0)',
        'Database.emptyRecycleBin(SObject sobject) --> Database.EmptyRecycleBinResult' : 'emptyRecycleBin($0)',
        'Database.executeBatch(APEX_OBJECT batchable) --> String' : 'executeBatch($0)',
        'Database.executeBatch(APEX_OBJECT batchable, Integer batchSize) --> String' : 'executeBatch($0)',
        'Database.getQueryLocator(LIST<SObject> query) --> Database.QueryLocator' : 'getQueryLocator($0)',
        'Database.getQueryLocator(String query) --> Database.QueryLocator' : 'getQueryLocator($0)',
        'Database.insert(LIST<SObject> sobjects) --> LIST<Database.SaveResult>' : 'insert($0)',
        'Database.insert(LIST<SObject> sobjects, APEX_OBJECT DmlOptions) --> LIST<Database.SaveResult>' : 'insert($0)',
        'Database.insert(LIST<SObject> sobjects, Boolean allOrNothing) --> LIST<Database.SaveResult>' : 'insert($0)',
        'Database.insert(SObject sobject) --> Database.SaveResult' : 'insert($0)',
        'Database.insert(SObject sobject, APEX_OBJECT DmlOptions) --> Database.SaveResult' : 'insert($0)',
        'Database.insert(SObject sobject, Boolean allOrNothing) --> Database.SaveResult' : 'insert($0)',
        'Database.query(String query) --> LIST<SObject>' : 'query($0)',
        'Database.rollback(System.Savepoint savepoint) --> void' : 'rollback($0)',
        'Database.setSavepoint() --> System.Savepoint' : 'setSavepoint()$0',
        'Database.undelete(Id id) --> Database.UndeleteResult' : 'undelete($0)',
        'Database.undelete(Id id, Boolean allOrNothing) --> Database.UndeleteResult' : 'undelete($0)',
        'Database.undelete(LIST<Id> ids) --> LIST<Database.UndeleteResult>' : 'undelete($0)',
        'Database.undelete(LIST<Id> ids, Boolean allOrNothing) --> LIST<Database.UndeleteResult>' : 'undelete($0)',
        'Database.undelete(LIST<SObject> sobjects) --> LIST<Database.UndeleteResult>' : 'undelete($0)',
        'Database.undelete(LIST<SObject> sobjects, Boolean allOrNothing) --> LIST<Database.UndeleteResult>' : 'undelete($0)',
        'Database.undelete(SObject sobject) --> Database.UndeleteResult' : 'undelete($0)',
        'Database.undelete(SObject sobject, Boolean allOrNothing) --> Database.UndeleteResult' : 'undelete($0)',
        'Database.update(LIST<SObject> sobjects) --> LIST<Database.SaveResult>' : 'update($0)',
        'Database.update(LIST<SObject> sobjects, APEX_OBJECT allOrNothing) --> LIST<Database.SaveResult>' : 'update($0)',
        'Database.update(LIST<SObject> sobjects, Boolean allOrNothing) --> LIST<Database.SaveResult>' : 'update($0)',
        'Database.update(SObject sobject) --> Database.SaveResult' : 'update($0)',
        'Database.update(SObject sobject, APEX_OBJECT allOrNothing) --> Database.SaveResult' : 'update($0)',
        'Database.update(SObject sobject, Boolean allOrNothing) --> Database.SaveResult' : 'update($0)',
        'Database.upsert(LIST<SObject> sobjects) --> LIST<Database.UpsertResult>' : 'upsert($0)',
        'Database.upsert(LIST<SObject> sobjects, Boolean allOrNothing) --> LIST<Database.UpsertResult>' : 'upsert($0)',
        'Database.upsert(LIST<SObject> sobjects, Schema.SObjectField field) --> LIST<Database.UpsertResult>' : 'upsert($0)',
        'Database.upsert(LIST<SObject> sobjects, Schema.SObjectField field, Boolean allOrNothing) --> LIST<Database.UpsertResult>' : 'upsert($0)',
        'Database.upsert(SObject sobject) --> Database.UpsertResult' : 'upsert($0)',
        'Database.upsert(SObject sobject, Boolean allOrNothing) --> Database.UpsertResult' : 'upsert($0)',
        'Database.upsert(SObject sobject, Schema.SObjectField field) --> Database.UpsertResult' : 'upsert($0)',
        'Database.upsert(SObject sobject, Schema.SObjectField field, Boolean allOrNothing) --> Database.UpsertResult' : 'upsert($0)'
    },
    'Date' : {
        'Date.addDays(Integer days) --> Date' : 'addDays($0)',
        'Date.addError(APEX_OBJECT msg) --> void' : 'addError($0)',
        'Date.addError(APEX_OBJECT msg, Boolean escape) --> void' : 'addError($0)',
        'Date.addError(String msg) --> void' : 'addError($0)',
        'Date.addError(String msg, Boolean escape) --> void' : 'addError($0)',
        'Date.addMonths(Integer months) --> Date' : 'addMonths($0)',
        'Date.addYears(Integer years) --> Date' : 'addYears($0)',
        'Date.day() --> Integer' : 'day()$0',
        'Date.dayOfYear() --> Integer' : 'dayOfYear()$0',
        'Date.daysBetween(Date other) --> Integer' : 'daysBetween($0)',
        'Date.daysInMonth(Integer year, Integer month) --> Integer' : 'daysInMonth($0)',
        'Date.format() --> String' : 'format()$0',
        'Date.isLeapYear(Integer year) --> Boolean' : 'isLeapYear($0)',
        'Date.isSameDay(Date other) --> Boolean' : 'isSameDay($0)',
        'Date.month() --> Integer' : 'month()$0',
        'Date.monthsBetween(Date other) --> Integer' : 'monthsBetween($0)',
        'Date.newInstance(Integer year, Integer month, Integer day) --> Date' : 'newInstance($0)',
        'Date.parse(String str) --> Date' : 'parse($0)',
        'Date.toStartOfMonth() --> Date' : 'toStartOfMonth()$0',
        'Date.toStartOfWeek() --> Date' : 'toStartOfWeek()$0',
        'Date.today() --> Date' : 'today()$0',
        'Date.valueOf(Object o) --> Date' : 'valueOf($0)',
        'Date.valueOf(String str) --> Date' : 'valueOf($0)',
        'Date.year() --> Integer' : 'year()$0'
    },
    'Datetime' : {
        'Datetime.addDays(Integer days) --> Datetime' : 'addDays($0)',
        'Datetime.addError(APEX_OBJECT msg) --> void' : 'addError($0)',
        'Datetime.addError(APEX_OBJECT msg, Boolean escape) --> void' : 'addError($0)',
        'Datetime.addError(String msg) --> void' : 'addError($0)',
        'Datetime.addError(String msg, Boolean escape) --> void' : 'addError($0)',
        'Datetime.addHours(Integer hours) --> Datetime' : 'addHours($0)',
        'Datetime.addMinutes(Integer minutes) --> Datetime' : 'addMinutes($0)',
        'Datetime.addMonths(Integer months) --> Datetime' : 'addMonths($0)',
        'Datetime.addSeconds(Integer seconds) --> Datetime' : 'addSeconds($0)',
        'Datetime.addYears(Integer years) --> Datetime' : 'addYears($0)',
        'Datetime.date() --> Date' : 'date()$0',
        'Datetime.dateGmt() --> Date' : 'dateGmt()$0',
        'Datetime.day() --> Integer' : 'day()$0',
        'Datetime.dayGmt() --> Integer' : 'dayGmt()$0',
        'Datetime.dayOfYear() --> Integer' : 'dayOfYear()$0',
        'Datetime.dayOfYearGmt() --> Integer' : 'dayOfYearGmt()$0',
        'Datetime.format() --> String' : 'format()$0',
        'Datetime.format(String dateformat) --> String' : 'format($0)',
        'Datetime.format(String dateformat, String timezone) --> String' : 'format($0)',
        'Datetime.formatGmt(String dateformat) --> String' : 'formatGmt($0)',
        'Datetime.formatLong() --> String' : 'formatLong()$0',
        'Datetime.getTime() --> Long' : 'getTime()$0',
        'Datetime.hour() --> Integer' : 'hour()$0',
        'Datetime.hourGmt() --> Integer' : 'hourGmt()$0',
        'Datetime.isSameDay(Datetime other) --> Boolean' : 'isSameDay($0)',
        'Datetime.millisecond() --> Integer' : 'millisecond()$0',
        'Datetime.millisecondGmt() --> Integer' : 'millisecondGmt()$0',
        'Datetime.minute() --> Integer' : 'minute()$0',
        'Datetime.minuteGmt() --> Integer' : 'minuteGmt()$0',
        'Datetime.month() --> Integer' : 'month()$0',
        'Datetime.monthGmt() --> Integer' : 'monthGmt()$0',
        'Datetime.newInstance(Date date, Time time) --> Datetime' : 'newInstance($0)',
        'Datetime.newInstance(Integer year, Integer month, Integer day) --> Datetime' : 'newInstance($0)',
        'Datetime.newInstance(Integer year, Integer month, Integer day, Integer hour, Integer minute, Integer second) --> Datetime' : 'newInstance($0)',
        'Datetime.newInstance(Long time) --> Datetime' : 'newInstance($0)',
        'Datetime.newInstanceGmt(Date date, Time time) --> Datetime' : 'newInstanceGmt($0)',
        'Datetime.newInstanceGmt(Integer year, Integer month, Integer day) --> Datetime' : 'newInstanceGmt($0)',
        'Datetime.newInstanceGmt(Integer year, Integer month, Integer day, Integer hour, Integer minute, Integer second) --> Datetime' : 'newInstanceGmt($0)',
        'Datetime.now() --> Datetime' : 'now()$0',
        'Datetime.parse(String str) --> Datetime' : 'parse($0)',
        'Datetime.second() --> Integer' : 'second()$0',
        'Datetime.secondGmt() --> Integer' : 'secondGmt()$0',
        'Datetime.time() --> Time' : 'time()$0',
        'Datetime.timeGmt() --> Time' : 'timeGmt()$0',
        'Datetime.valueOf(Object o) --> Datetime' : 'valueOf($0)',
        'Datetime.valueOf(String str) --> Datetime' : 'valueOf($0)',
        'Datetime.valueOfGmt(String str) --> Datetime' : 'valueOfGmt($0)',
        'Datetime.year() --> Integer' : 'year()$0',
        'Datetime.yearGmt() --> Integer' : 'yearGmt()$0'
    },
    'Decimal' : {
        'Decimal.abs() --> Decimal' : 'abs()$0',
        'Decimal.addError(APEX_OBJECT msg) --> void' : 'addError($0)',
        'Decimal.addError(APEX_OBJECT msg, Boolean escape) --> void' : 'addError($0)',
        'Decimal.addError(String msg) --> void' : 'addError($0)',
        'Decimal.addError(String msg, Boolean escape) --> void' : 'addError($0)',
        'Decimal.divide(Decimal divisor, Integer scale) --> Decimal' : 'divide($0)',
        'Decimal.divide(Decimal divisor, Integer scale, APEX_OBJECT roundingMode) --> Decimal' : 'divide($0)',
        'Decimal.doubleValue() --> Double' : 'doubleValue()$0',
        'Decimal.format() --> String' : 'format()$0',
        'Decimal.intValue() --> Integer' : 'intValue()$0',
        'Decimal.longValue() --> Long' : 'longValue()$0',
        'Decimal.pow(Integer exponent) --> Decimal' : 'pow($0)',
        'Decimal.precision() --> Integer' : 'precision()$0',
        'Decimal.round() --> Long' : 'round()$0',
        'Decimal.round(system.RoundingMode roundingMode) --> Long' : 'round($0)',
        'Decimal.scale() --> Integer' : 'scale()$0',
        'Decimal.setScale(Integer scale) --> Decimal' : 'setScale($0)',
        'Decimal.setScale(Integer scale, system.RoundingMode roundingMode) --> Decimal' : 'setScale($0)',
        'Decimal.stripTrailingZeros() --> Decimal' : 'stripTrailingZeros()$0',
        'Decimal.toPlainString() --> String' : 'toPlainString()$0',
        'Decimal.valueOf(Double dbl) --> Decimal' : 'valueOf($0)',
        'Decimal.valueOf(Long lng) --> Decimal' : 'valueOf($0)',
        'Decimal.valueOf(String str) --> Decimal' : 'valueOf($0)'
    },
    'DisplayType' : {
        'DisplayType.values() --> LIST<Schema.DisplayType>' : 'values()$0'
    },
    'DmlException' : {
        'DmlException.getCause() --> Exception' : 'getCause()$0',
        'DmlException.getDmlFieldNames(Integer index) --> LIST<String>' : 'getDmlFieldNames($0)',
        'DmlException.getDmlFields(Integer index) --> LIST<Schema.SObjectField>' : 'getDmlFields($0)',
        'DmlException.getDmlId(Integer index) --> String' : 'getDmlId($0)',
        'DmlException.getDmlIndex(Integer index) --> Integer' : 'getDmlIndex($0)',
        'DmlException.getDmlMessage(Integer index) --> String' : 'getDmlMessage($0)',
        'DmlException.getDmlStatusCode(Integer index) --> String' : 'getDmlStatusCode($0)',
        'DmlException.getDmlType(Integer index) --> system.StatusCode' : 'getDmlType($0)',
        'DmlException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'DmlException.getMessage() --> String' : 'getMessage()$0',
        'DmlException.getNumDml() --> Integer' : 'getNumDml()$0',
        'DmlException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'DmlException.getTypeName() --> String' : 'getTypeName()$0',
        'DmlException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'DmlException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'Document' : {
        'Document.createRootElement(String name, String namespace, String prefix) --> dom.XmlNode' : 'createRootElement($0)',
        'Document.getRootElement() --> dom.XmlNode' : 'getRootElement()$0',
        'Document.load(String xml) --> void' : 'load($0)',
        'Document.toXmlString() --> String' : 'toXmlString()$0'
    },
    'Double' : {
        'Double.addError(APEX_OBJECT msg) --> void' : 'addError($0)',
        'Double.addError(APEX_OBJECT msg, Boolean escape) --> void' : 'addError($0)',
        'Double.addError(String msg) --> void' : 'addError($0)',
        'Double.addError(String msg, Boolean escape) --> void' : 'addError($0)',
        'Double.format() --> String' : 'format()$0',
        'Double.intValue() --> Integer' : 'intValue()$0',
        'Double.longValue() --> Long' : 'longValue()$0',
        'Double.round() --> Long' : 'round()$0',
        'Double.valueOf(Object o) --> Double' : 'valueOf($0)',
        'Double.valueOf(String str) --> Double' : 'valueOf($0)'
    },
    'EmailAttachment' : {},
    'EmailException' : {
        'EmailException.getCause() --> Exception' : 'getCause()$0',
        'EmailException.getDmlFieldNames(Integer index) --> LIST<String>' : 'getDmlFieldNames($0)',
        'EmailException.getDmlFields(Integer index) --> LIST<Schema.SObjectField>' : 'getDmlFields($0)',
        'EmailException.getDmlId(Integer index) --> String' : 'getDmlId($0)',
        'EmailException.getDmlIndex(Integer index) --> Integer' : 'getDmlIndex($0)',
        'EmailException.getDmlMessage(Integer index) --> String' : 'getDmlMessage($0)',
        'EmailException.getDmlStatusCode(Integer index) --> String' : 'getDmlStatusCode($0)',
        'EmailException.getDmlType(Integer index) --> system.StatusCode' : 'getDmlType($0)',
        'EmailException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'EmailException.getMessage() --> String' : 'getMessage()$0',
        'EmailException.getNumDml() --> Integer' : 'getNumDml()$0',
        'EmailException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'EmailException.getTypeName() --> String' : 'getTypeName()$0',
        'EmailException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'EmailException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'EmailFileAttachment' : {},
    'EmailHeader' : {},
    'EmailTemplateSelector' : {
        'EmailTemplateSelector.getDefaultEmailTemplateId(Id param1) --> Id' : 'getDefaultEmailTemplateId($0)'
    },
    'EmailToCaseHandler' : {},
    'EmailToSalesforceHandler' : {},
    'EmptyStackException' : {
        'EmptyStackException.getTypeName() --> String' : 'getTypeName()$0'
    },
    'EncodingUtil' : {
        'EncodingUtil.base64Decode(String s) --> Blob' : 'base64Decode($0)',
        'EncodingUtil.base64Encode(Blob s) --> String' : 'base64Encode($0)',
        'EncodingUtil.convertToHex(Blob s) --> String' : 'convertToHex($0)',
        'EncodingUtil.urlDecode(String s, String enc) --> String' : 'urlDecode($0)',
        'EncodingUtil.urlEncode(String s, String enc) --> String' : 'urlEncode($0)'
    },
    'EntityLinkSegment' : {
        'EntityLinkSegment.equals(Object obj) --> Boolean' : 'equals($0)',
        'EntityLinkSegment.hashCode() --> Integer' : 'hashCode()$0',
        'EntityLinkSegment.toString() --> String' : 'toString()$0'
    },
    'Exception' : {
        'Exception.getCause() --> Exception' : 'getCause()$0',
        'Exception.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'Exception.getMessage() --> String' : 'getMessage()$0',
        'Exception.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'Exception.getTypeName() --> String' : 'getTypeName()$0',
        'Exception.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'Exception.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'Features' : {
        'Features.equals(Object obj) --> Boolean' : 'equals($0)',
        'Features.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'Features.hashCode() --> Integer' : 'hashCode()$0',
        'Features.toString() --> String' : 'toString()$0'
    },
    'Feed' : {
        'Feed.equals(Object obj) --> Boolean' : 'equals($0)',
        'Feed.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'Feed.hashCode() --> Integer' : 'hashCode()$0',
        'Feed.toString() --> String' : 'toString()$0'
    },
    'FeedBody' : {
        'FeedBody.equals(Object obj) --> Boolean' : 'equals($0)',
        'FeedBody.hashCode() --> Integer' : 'hashCode()$0',
        'FeedBody.toString() --> String' : 'toString()$0'
    },
    'FeedFavorite' : {
        'FeedFavorite.equals(Object obj) --> Boolean' : 'equals($0)',
        'FeedFavorite.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'FeedFavorite.hashCode() --> Integer' : 'hashCode()$0',
        'FeedFavorite.toString() --> String' : 'toString()$0'
    },
    'FeedFavoriteType' : {
        'FeedFavoriteType.values() --> LIST<ConnectApi.FeedFavoriteType>' : 'values()$0'
    },
    'FeedFavorites' : {
        'FeedFavorites.equals(Object obj) --> Boolean' : 'equals($0)',
        'FeedFavorites.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'FeedFavorites.hashCode() --> Integer' : 'hashCode()$0',
        'FeedFavorites.toString() --> String' : 'toString()$0'
    },
    'FeedItem' : {
        'FeedItem.equals(Object obj) --> Boolean' : 'equals($0)',
        'FeedItem.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'FeedItem.hashCode() --> Integer' : 'hashCode()$0',
        'FeedItem.toString() --> String' : 'toString()$0'
    },
    'FeedItemAttachment' : {
        'FeedItemAttachment.equals(Object obj) --> Boolean' : 'equals($0)',
        'FeedItemAttachment.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'FeedItemAttachment.hashCode() --> Integer' : 'hashCode()$0',
        'FeedItemAttachment.toString() --> String' : 'toString()$0'
    },
    'FeedItemAttachmentInput' : {
        'FeedItemAttachmentInput.convertToJavaObject(java:common.api.AppVersion param1) --> java:java.lang.Object' : 'convertToJavaObject($0)',
        'FeedItemAttachmentInput.equals(Object obj) --> Boolean' : 'equals($0)',
        'FeedItemAttachmentInput.hashCode() --> Integer' : 'hashCode()$0',
        'FeedItemAttachmentInput.toString() --> String' : 'toString()$0'
    },
    'FeedItemAttachmentType' : {
        'FeedItemAttachmentType.values() --> LIST<ConnectApi.FeedItemAttachmentType>' : 'values()$0'
    },
    'FeedItemInput' : {
        'FeedItemInput.convertToJavaObject(java:common.api.AppVersion currentVersion) --> java:java.lang.Object' : 'convertToJavaObject($0)',
        'FeedItemInput.equals(Object obj) --> Boolean' : 'equals($0)',
        'FeedItemInput.hashCode() --> Integer' : 'hashCode()$0',
        'FeedItemInput.toString() --> String' : 'toString()$0'
    },
    'FeedItemPage' : {
        'FeedItemPage.equals(Object obj) --> Boolean' : 'equals($0)',
        'FeedItemPage.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'FeedItemPage.hashCode() --> Integer' : 'hashCode()$0',
        'FeedItemPage.toString() --> String' : 'toString()$0'
    },
    'FeedItemType' : {
        'FeedItemType.values() --> LIST<ConnectApi.FeedItemType>' : 'values()$0'
    },
    'FeedItemVisibilityType' : {
        'FeedItemVisibilityType.values() --> LIST<ConnectApi.FeedItemVisibilityType>' : 'values()$0'
    },
    'FeedModifiedInfo' : {
        'FeedModifiedInfo.equals(Object obj) --> Boolean' : 'equals($0)',
        'FeedModifiedInfo.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'FeedModifiedInfo.hashCode() --> Integer' : 'hashCode()$0',
        'FeedModifiedInfo.toString() --> String' : 'toString()$0'
    },
    'FeedPoll' : {
        'FeedPoll.equals(Object obj) --> Boolean' : 'equals($0)',
        'FeedPoll.hashCode() --> Integer' : 'hashCode()$0',
        'FeedPoll.toString() --> String' : 'toString()$0'
    },
    'FeedPollChoice' : {
        'FeedPollChoice.equals(Object obj) --> Boolean' : 'equals($0)',
        'FeedPollChoice.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'FeedPollChoice.hashCode() --> Integer' : 'hashCode()$0',
        'FeedPollChoice.toString() --> String' : 'toString()$0'
    },
    'FeedSortOrder' : {
        'FeedSortOrder.values() --> LIST<ConnectApi.FeedSortOrder>' : 'values()$0'
    },
    'FeedType' : {
        'FeedType.values() --> LIST<ConnectApi.FeedType>' : 'values()$0'
    },
    'FieldChangeNameSegment' : {
        'FieldChangeNameSegment.equals(Object obj) --> Boolean' : 'equals($0)',
        'FieldChangeNameSegment.hashCode() --> Integer' : 'hashCode()$0',
        'FieldChangeNameSegment.toString() --> String' : 'toString()$0'
    },
    'FieldChangeSegment' : {
        'FieldChangeSegment.equals(Object obj) --> Boolean' : 'equals($0)',
        'FieldChangeSegment.hashCode() --> Integer' : 'hashCode()$0',
        'FieldChangeSegment.toString() --> String' : 'toString()$0'
    },
    'FieldChangeValueSegment' : {
        'FieldChangeValueSegment.equals(Object obj) --> Boolean' : 'equals($0)',
        'FieldChangeValueSegment.hashCode() --> Integer' : 'hashCode()$0',
        'FieldChangeValueSegment.toString() --> String' : 'toString()$0'
    },
    'FileSummary' : {
        'FileSummary.equals(Object obj) --> Boolean' : 'equals($0)',
        'FileSummary.hashCode() --> Integer' : 'hashCode()$0',
        'FileSummary.toString() --> String' : 'toString()$0'
    },
    'FinalException' : {
        'FinalException.getCause() --> Exception' : 'getCause()$0',
        'FinalException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'FinalException.getMessage() --> String' : 'getMessage()$0',
        'FinalException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'FinalException.getTypeName() --> String' : 'getTypeName()$0',
        'FinalException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'FinalException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'FlowException' : {
        'FlowException.getCause() --> Exception' : 'getCause()$0',
        'FlowException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'FlowException.getMessage() --> String' : 'getMessage()$0',
        'FlowException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'FlowException.getTypeName() --> String' : 'getTypeName()$0',
        'FlowException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'FlowException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'FollowerPage' : {
        'FollowerPage.equals(Object obj) --> Boolean' : 'equals($0)',
        'FollowerPage.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'FollowerPage.hashCode() --> Integer' : 'hashCode()$0',
        'FollowerPage.toString() --> String' : 'toString()$0'
    },
    'FollowingCounts' : {
        'FollowingCounts.equals(Object obj) --> Boolean' : 'equals($0)',
        'FollowingCounts.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'FollowingCounts.hashCode() --> Integer' : 'hashCode()$0',
        'FollowingCounts.toString() --> String' : 'toString()$0'
    },
    'FollowingPage' : {
        'FollowingPage.equals(Object obj) --> Boolean' : 'equals($0)',
        'FollowingPage.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'FollowingPage.hashCode() --> Integer' : 'hashCode()$0',
        'FollowingPage.toString() --> String' : 'toString()$0'
    },
    'GlobalInfluence' : {
        'GlobalInfluence.equals(Object obj) --> Boolean' : 'equals($0)',
        'GlobalInfluence.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'GlobalInfluence.hashCode() --> Integer' : 'hashCode()$0',
        'GlobalInfluence.toString() --> String' : 'toString()$0'
    },
    'GroupChatterSettings' : {
        'GroupChatterSettings.equals(Object obj) --> Boolean' : 'equals($0)',
        'GroupChatterSettings.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'GroupChatterSettings.hashCode() --> Integer' : 'hashCode()$0',
        'GroupChatterSettings.toString() --> String' : 'toString()$0'
    },
    'GroupEmailFrequency' : {
        'GroupEmailFrequency.values() --> LIST<ConnectApi.GroupEmailFrequency>' : 'values()$0'
    },
    'GroupInformation' : {
        'GroupInformation.equals(Object obj) --> Boolean' : 'equals($0)',
        'GroupInformation.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'GroupInformation.hashCode() --> Integer' : 'hashCode()$0',
        'GroupInformation.toString() --> String' : 'toString()$0'
    },
    'GroupInformationInput' : {
        'GroupInformationInput.convertToJavaObject(java:common.api.AppVersion currentVersion) --> java:java.lang.Object' : 'convertToJavaObject($0)',
        'GroupInformationInput.equals(Object obj) --> Boolean' : 'equals($0)',
        'GroupInformationInput.hashCode() --> Integer' : 'hashCode()$0',
        'GroupInformationInput.toString() --> String' : 'toString()$0'
    },
    'GroupMember' : {
        'GroupMember.equals(Object obj) --> Boolean' : 'equals($0)',
        'GroupMember.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'GroupMember.hashCode() --> Integer' : 'hashCode()$0',
        'GroupMember.toString() --> String' : 'toString()$0'
    },
    'GroupMemberPage' : {
        'GroupMemberPage.equals(Object obj) --> Boolean' : 'equals($0)',
        'GroupMemberPage.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'GroupMemberPage.hashCode() --> Integer' : 'hashCode()$0',
        'GroupMemberPage.toString() --> String' : 'toString()$0'
    },
    'GroupMembershipRequest' : {
        'GroupMembershipRequest.equals(Object obj) --> Boolean' : 'equals($0)',
        'GroupMembershipRequest.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'GroupMembershipRequest.hashCode() --> Integer' : 'hashCode()$0',
        'GroupMembershipRequest.toString() --> String' : 'toString()$0'
    },
    'GroupMembershipRequestStatus' : {
        'GroupMembershipRequestStatus.values() --> LIST<ConnectApi.GroupMembershipRequestStatus>' : 'values()$0'
    },
    'GroupMembershipRequests' : {
        'GroupMembershipRequests.equals(Object obj) --> Boolean' : 'equals($0)',
        'GroupMembershipRequests.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'GroupMembershipRequests.hashCode() --> Integer' : 'hashCode()$0',
        'GroupMembershipRequests.toString() --> String' : 'toString()$0'
    },
    'GroupMembershipType' : {
        'GroupMembershipType.values() --> LIST<ConnectApi.GroupMembershipType>' : 'values()$0'
    },
    'GroupVisibilityType' : {
        'GroupVisibilityType.values() --> LIST<ConnectApi.GroupVisibilityType>' : 'values()$0'
    },
    'HandledException' : {
        'HandledException.getCause() --> Exception' : 'getCause()$0',
        'HandledException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'HandledException.getMessage() --> String' : 'getMessage()$0',
        'HandledException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'HandledException.getTypeName() --> String' : 'getTypeName()$0',
        'HandledException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'HandledException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'HashtagSegment' : {
        'HashtagSegment.equals(Object obj) --> Boolean' : 'equals($0)',
        'HashtagSegment.hashCode() --> Integer' : 'hashCode()$0',
        'HashtagSegment.toString() --> String' : 'toString()$0'
    },
    'HashtagSegmentInput' : {
        'HashtagSegmentInput.convertToJavaObject(java:common.api.AppVersion currentVersion) --> java:java.lang.Object' : 'convertToJavaObject($0)',
        'HashtagSegmentInput.equals(Object obj) --> Boolean' : 'equals($0)',
        'HashtagSegmentInput.hashCode() --> Integer' : 'hashCode()$0',
        'HashtagSegmentInput.toString() --> String' : 'toString()$0'
    },
    'Header' : {},
    'Http' : {
        'Http.send(ANY request) --> System.HttpResponse' : 'send($0)',
        'Http.toString() --> String' : 'toString()$0'
    },
    'HttpCalloutMock' : {
        'HttpCalloutMock.respond(System.HttpRequest param1) --> System.HttpResponse' : 'respond($0)'
    },
    'HttpRequest' : {
        'HttpRequest.getBody() --> String' : 'getBody()$0',
        'HttpRequest.getBodyAsBlob() --> Blob' : 'getBodyAsBlob()$0',
        'HttpRequest.getBodyDocument() --> dom.Document' : 'getBodyDocument()$0',
        'HttpRequest.getCompressed() --> Boolean' : 'getCompressed()$0',
        'HttpRequest.getEndpoint() --> String' : 'getEndpoint()$0',
        'HttpRequest.getHeader(String key) --> String' : 'getHeader($0)',
        'HttpRequest.getMethod() --> String' : 'getMethod()$0',
        'HttpRequest.setBody(String body) --> void' : 'setBody($0)',
        'HttpRequest.setBodyAsBlob(Blob body) --> void' : 'setBodyAsBlob($0)',
        'HttpRequest.setBodyDocument(ANY body) --> void' : 'setBodyDocument($0)',
        'HttpRequest.setClientCertificate(String clientCert, String password) --> void' : 'setClientCertificate($0)',
        'HttpRequest.setClientCertificateName(String certDevName) --> void' : 'setClientCertificateName($0)',
        'HttpRequest.setCompressed(Boolean compressed) --> void' : 'setCompressed($0)',
        'HttpRequest.setEndpoint(String endpoint) --> void' : 'setEndpoint($0)',
        'HttpRequest.setHeader(String key, String value) --> void' : 'setHeader($0)',
        'HttpRequest.setMethod(String method) --> void' : 'setMethod($0)',
        'HttpRequest.setTimeout(Integer timeout) --> void' : 'setTimeout($0)',
        'HttpRequest.toString() --> String' : 'toString()$0'
    },
    'HttpResponse' : {
        'HttpResponse.getBody() --> String' : 'getBody()$0',
        'HttpResponse.getBodyAsBlob() --> Blob' : 'getBodyAsBlob()$0',
        'HttpResponse.getBodyDocument() --> dom.Document' : 'getBodyDocument()$0',
        'HttpResponse.getHeader(String key) --> String' : 'getHeader($0)',
        'HttpResponse.getHeaderKeys() --> LIST<String>' : 'getHeaderKeys()$0',
        'HttpResponse.getStatus() --> String' : 'getStatus()$0',
        'HttpResponse.getStatusCode() --> Integer' : 'getStatusCode()$0',
        'HttpResponse.getXmlStreamReader() --> System.XmlStreamReader' : 'getXmlStreamReader()$0',
        'HttpResponse.setBody(String body) --> void' : 'setBody($0)',
        'HttpResponse.setBodyAsBlob(Blob body) --> void' : 'setBodyAsBlob($0)',
        'HttpResponse.setHeader(String key, String value) --> void' : 'setHeader($0)',
        'HttpResponse.setStatus(String status) --> void' : 'setStatus($0)',
        'HttpResponse.setStatusCode(Integer statusCode) --> void' : 'setStatusCode($0)',
        'HttpResponse.toString() --> String' : 'toString()$0'
    },
    'Icon' : {
        'Icon.equals(Object obj) --> Boolean' : 'equals($0)',
        'Icon.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'Icon.hashCode() --> Integer' : 'hashCode()$0',
        'Icon.toString() --> String' : 'toString()$0'
    },
    'Id' : {
        'Id.addError(APEX_OBJECT msg) --> void' : 'addError($0)',
        'Id.addError(APEX_OBJECT msg, Boolean escape) --> void' : 'addError($0)',
        'Id.addError(String msg) --> void' : 'addError($0)',
        'Id.addError(String msg, Boolean escape) --> void' : 'addError($0)',
        'Id.getSobjectType() --> Schema.SObjectType' : 'getSobjectType()$0',
        'Id.valueOf(String str) --> Id' : 'valueOf($0)'
    },
    'IdeaStandardController' : {
        'IdeaStandardController.addFields(LIST<String> fieldNames) --> void' : 'addFields($0)',
        'IdeaStandardController.cancel() --> System.PageReference' : 'cancel()$0',
        'IdeaStandardController.delete() --> System.PageReference' : 'delete()$0',
        'IdeaStandardController.edit() --> System.PageReference' : 'edit()$0',
        'IdeaStandardController.getCommentList() --> LIST<IdeaComment>' : 'getCommentList()$0',
        'IdeaStandardController.getId() --> String' : 'getId()$0',
        'IdeaStandardController.getRecord() --> SObject' : 'getRecord()$0',
        'IdeaStandardController.getSubject() --> SObject' : 'getSubject()$0',
        'IdeaStandardController.reset() --> void' : 'reset()$0',
        'IdeaStandardController.save() --> System.PageReference' : 'save()$0',
        'IdeaStandardController.view() --> System.PageReference' : 'view()$0'
    },
    'IdeaStandardSetController' : {
        'IdeaStandardSetController.addFields(LIST<String> fieldNames) --> void' : 'addFields($0)',
        'IdeaStandardSetController.cancel() --> System.PageReference' : 'cancel()$0',
        'IdeaStandardSetController.first() --> void' : 'first()$0',
        'IdeaStandardSetController.getCompleteResult() --> Boolean' : 'getCompleteResult()$0',
        'IdeaStandardSetController.getFilterId() --> String' : 'getFilterId()$0',
        'IdeaStandardSetController.getHasNext() --> Boolean' : 'getHasNext()$0',
        'IdeaStandardSetController.getHasPrevious() --> Boolean' : 'getHasPrevious()$0',
        'IdeaStandardSetController.getIdeaList() --> LIST<Idea>' : 'getIdeaList()$0',
        'IdeaStandardSetController.getListViewOptions() --> LIST<System.SelectOption>' : 'getListViewOptions()$0',
        'IdeaStandardSetController.getPageNumber() --> Integer' : 'getPageNumber()$0',
        'IdeaStandardSetController.getPageSize() --> Integer' : 'getPageSize()$0',
        'IdeaStandardSetController.getRecord() --> SObject' : 'getRecord()$0',
        'IdeaStandardSetController.getRecords() --> LIST<SObject>' : 'getRecords()$0',
        'IdeaStandardSetController.getResultSize() --> Integer' : 'getResultSize()$0',
        'IdeaStandardSetController.getSelected() --> LIST<SObject>' : 'getSelected()$0',
        'IdeaStandardSetController.last() --> void' : 'last()$0',
        'IdeaStandardSetController.next() --> void' : 'next()$0',
        'IdeaStandardSetController.previous() --> void' : 'previous()$0',
        'IdeaStandardSetController.reset() --> void' : 'reset()$0',
        'IdeaStandardSetController.save() --> System.PageReference' : 'save()$0',
        'IdeaStandardSetController.setFilterId(String filterId) --> void' : 'setFilterId($0)',
        'IdeaStandardSetController.setPageNumber(Integer pageNumber) --> void' : 'setPageNumber($0)',
        'IdeaStandardSetController.setPageSize(Integer pageSize) --> void' : 'setPageSize($0)',
        'IdeaStandardSetController.setSelected(LIST<SObject> selected) --> void' : 'setSelected($0)'
    },
    'Ideas' : {
        'Ideas.findSimilar(SObject idea) --> LIST<Id>' : 'findSimilar($0)',
        'Ideas.getAllRecentReplies(String userId, String communityId) --> LIST<Id>' : 'getAllRecentReplies($0)',
        'Ideas.getReadRecentReplies(String userId, String communityId) --> LIST<Id>' : 'getReadRecentReplies($0)',
        'Ideas.getUnreadRecentReplies(String userId, String communityId) --> LIST<Id>' : 'getUnreadRecentReplies($0)',
        'Ideas.markRead(String ideaId) --> void' : 'markRead($0)'
    },
    'InboundEmail' : {},
    'InboundEmailHandler' : {
        'InboundEmailHandler.handleInboundEmail(Messaging.InboundEmail param1, Messaging.InboundEnvelope param2) --> Messaging.InboundEmailResult' : 'handleInboundEmail($0)'
    },
    'InboundEmailResult' : {},
    'InboundEnvelope' : {},
    'InputParameter' : {},
    'Integer' : {
        'Integer.addError(APEX_OBJECT msg) --> void' : 'addError($0)',
        'Integer.addError(APEX_OBJECT msg, Boolean escape) --> void' : 'addError($0)',
        'Integer.addError(String msg) --> void' : 'addError($0)',
        'Integer.addError(String msg, Boolean escape) --> void' : 'addError($0)',
        'Integer.format() --> String' : 'format()$0',
        'Integer.valueOf(Object o) --> Integer' : 'valueOf($0)',
        'Integer.valueOf(String i) --> Integer' : 'valueOf($0)'
    },
    'Interview' : {
        'Interview.getVariableValue(String param1) --> Object' : 'getVariableValue($0)'
    },
    'InvalidHeaderException' : {
        'InvalidHeaderException.getTypeName() --> String' : 'getTypeName()$0'
    },
    'InvalidParameterValueException' : {
        'InvalidParameterValueException.getCause() --> Exception' : 'getCause()$0',
        'InvalidParameterValueException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'InvalidParameterValueException.getMessage() --> String' : 'getMessage()$0',
        'InvalidParameterValueException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'InvalidParameterValueException.getTypeName() --> String' : 'getTypeName()$0',
        'InvalidParameterValueException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'InvalidParameterValueException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'InvalidReadOnlyUserDmlException' : {
        'InvalidReadOnlyUserDmlException.getCause() --> Exception' : 'getCause()$0',
        'InvalidReadOnlyUserDmlException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'InvalidReadOnlyUserDmlException.getMessage() --> String' : 'getMessage()$0',
        'InvalidReadOnlyUserDmlException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'InvalidReadOnlyUserDmlException.getTypeName() --> String' : 'getTypeName()$0',
        'InvalidReadOnlyUserDmlException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'InvalidReadOnlyUserDmlException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'Iterable' : {
        'Iterable.iterator() --> system.Iterator' : 'iterator()$0'
    },
    'Iterator' : {
        'Iterator.hasNext() --> Boolean' : 'hasNext()$0',
        'Iterator.next() --> Object' : 'next()$0'
    },
    'JSON' : {
        'JSON.createGenerator(Boolean pretty) --> system.JSONGenerator' : 'createGenerator($0)',
        'JSON.createParser(String jsonString) --> system.JSONParser' : 'createParser($0)',
        'JSON.deserialize(String jsonString, system.Type apexType) --> Object' : 'deserialize($0)',
        'JSON.deserializeStrict(String jsonString, system.Type apexType) --> Object' : 'deserializeStrict($0)',
        'JSON.deserializeUntyped(String jsonString) --> Object' : 'deserializeUntyped($0)',
        'JSON.serialize(Object o) --> String' : 'serialize($0)',
        'JSON.serializePretty(Object o) --> String' : 'serializePretty($0)'
    },
    'JSONException' : {
        'JSONException.getCause() --> Exception' : 'getCause()$0',
        'JSONException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'JSONException.getMessage() --> String' : 'getMessage()$0',
        'JSONException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'JSONException.getTypeName() --> String' : 'getTypeName()$0',
        'JSONException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'JSONException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'JSONGenerator' : {
        'JSONGenerator.close() --> void' : 'close()$0',
        'JSONGenerator.getAsString() --> String' : 'getAsString()$0',
        'JSONGenerator.isClosed() --> Boolean' : 'isClosed()$0',
        'JSONGenerator.writeBlob(Blob b) --> void' : 'writeBlob($0)',
        'JSONGenerator.writeBlobField(String fieldName, Blob b) --> void' : 'writeBlobField($0)',
        'JSONGenerator.writeBoolean(Boolean b) --> void' : 'writeBoolean($0)',
        'JSONGenerator.writeBooleanField(String fieldName, Boolean b) --> void' : 'writeBooleanField($0)',
        'JSONGenerator.writeDate(Date d) --> void' : 'writeDate($0)',
        'JSONGenerator.writeDateField(String fieldName, Date d) --> void' : 'writeDateField($0)',
        'JSONGenerator.writeDateTime(Datetime dt) --> void' : 'writeDateTime($0)',
        'JSONGenerator.writeDateTimeField(String fieldName, Datetime dt) --> void' : 'writeDateTimeField($0)',
        'JSONGenerator.writeEndArray() --> void' : 'writeEndArray()$0',
        'JSONGenerator.writeEndObject() --> void' : 'writeEndObject()$0',
        'JSONGenerator.writeFieldName(String fieldName) --> void' : 'writeFieldName($0)',
        'JSONGenerator.writeId(Id id) --> void' : 'writeId($0)',
        'JSONGenerator.writeIdField(String fieldName, Id id) --> void' : 'writeIdField($0)',
        'JSONGenerator.writeNull() --> void' : 'writeNull()$0',
        'JSONGenerator.writeNullField(String fieldName) --> void' : 'writeNullField($0)',
        'JSONGenerator.writeNumber(Decimal d) --> void' : 'writeNumber($0)',
        'JSONGenerator.writeNumber(Double d) --> void' : 'writeNumber($0)',
        'JSONGenerator.writeNumber(Integer i) --> void' : 'writeNumber($0)',
        'JSONGenerator.writeNumber(Long lng) --> void' : 'writeNumber($0)',
        'JSONGenerator.writeNumberField(String fieldName, Decimal d) --> void' : 'writeNumberField($0)',
        'JSONGenerator.writeNumberField(String fieldName, Double d) --> void' : 'writeNumberField($0)',
        'JSONGenerator.writeNumberField(String fieldName, Integer i) --> void' : 'writeNumberField($0)',
        'JSONGenerator.writeNumberField(String fieldName, Long lng) --> void' : 'writeNumberField($0)',
        'JSONGenerator.writeObject(Object o) --> void' : 'writeObject($0)',
        'JSONGenerator.writeObjectField(String fieldName, Object o) --> void' : 'writeObjectField($0)',
        'JSONGenerator.writeStartArray() --> void' : 'writeStartArray()$0',
        'JSONGenerator.writeStartObject() --> void' : 'writeStartObject()$0',
        'JSONGenerator.writeString(String str) --> void' : 'writeString($0)',
        'JSONGenerator.writeStringField(String fieldName, String str) --> void' : 'writeStringField($0)',
        'JSONGenerator.writeTime(Time t) --> void' : 'writeTime($0)',
        'JSONGenerator.writeTimeField(String fieldName, Time t) --> void' : 'writeTimeField($0)'
    },
    'JSONParser' : {
        'JSONParser.clearCurrentToken() --> void' : 'clearCurrentToken()$0',
        'JSONParser.getBlobValue() --> Blob' : 'getBlobValue()$0',
        'JSONParser.getBooleanValue() --> Boolean' : 'getBooleanValue()$0',
        'JSONParser.getCurrentName() --> String' : 'getCurrentName()$0',
        'JSONParser.getCurrentToken() --> system.JSONToken' : 'getCurrentToken()$0',
        'JSONParser.getDateTimeValue() --> Datetime' : 'getDateTimeValue()$0',
        'JSONParser.getDateValue() --> Date' : 'getDateValue()$0',
        'JSONParser.getDecimalValue() --> Decimal' : 'getDecimalValue()$0',
        'JSONParser.getDoubleValue() --> Double' : 'getDoubleValue()$0',
        'JSONParser.getIdValue() --> Id' : 'getIdValue()$0',
        'JSONParser.getIntegerValue() --> Integer' : 'getIntegerValue()$0',
        'JSONParser.getLastClearedToken() --> system.JSONToken' : 'getLastClearedToken()$0',
        'JSONParser.getLongValue() --> Long' : 'getLongValue()$0',
        'JSONParser.getText() --> String' : 'getText()$0',
        'JSONParser.getTimeValue() --> Time' : 'getTimeValue()$0',
        'JSONParser.hasCurrentToken() --> Boolean' : 'hasCurrentToken()$0',
        'JSONParser.nextToken() --> system.JSONToken' : 'nextToken()$0',
        'JSONParser.nextValue() --> system.JSONToken' : 'nextValue()$0',
        'JSONParser.readValueAs(system.Type apexType) --> Object' : 'readValueAs($0)',
        'JSONParser.readValueAsStrict(system.Type apexType) --> Object' : 'readValueAsStrict($0)',
        'JSONParser.skipChildren() --> void' : 'skipChildren()$0'
    },
    'JSONToken' : {
        'JSONToken.values() --> LIST<system.JSONToken>' : 'values()$0'
    },
    'KnowledgeArticleVersionStandardController' : {
        'KnowledgeArticleVersionStandardController.addFields(LIST<String> fieldNames) --> void' : 'addFields($0)',
        'KnowledgeArticleVersionStandardController.cancel() --> System.PageReference' : 'cancel()$0',
        'KnowledgeArticleVersionStandardController.delete() --> System.PageReference' : 'delete()$0',
        'KnowledgeArticleVersionStandardController.edit() --> System.PageReference' : 'edit()$0',
        'KnowledgeArticleVersionStandardController.getId() --> String' : 'getId()$0',
        'KnowledgeArticleVersionStandardController.getRecord() --> SObject' : 'getRecord()$0',
        'KnowledgeArticleVersionStandardController.getSourceId() --> String' : 'getSourceId()$0',
        'KnowledgeArticleVersionStandardController.getSubject() --> SObject' : 'getSubject()$0',
        'KnowledgeArticleVersionStandardController.reset() --> void' : 'reset()$0',
        'KnowledgeArticleVersionStandardController.save() --> System.PageReference' : 'save()$0',
        'KnowledgeArticleVersionStandardController.selectDataCategory(String categoryGroup, String category) --> void' : 'selectDataCategory($0)',
        'KnowledgeArticleVersionStandardController.view() --> System.PageReference' : 'view()$0'
    },
    'LIST' : {
        'LIST.add(ANY element) --> Object' : 'add($0)',
        'LIST.add(Integer index, ANY element) --> void' : 'add($0)',
        'LIST.addAll(LIST elements) --> void' : 'addAll($0)',
        'LIST.addAll(SET elements) --> void' : 'addAll($0)',
        'LIST.clear() --> void' : 'clear()$0',
        'LIST.clone() --> LIST<String>' : 'clone()$0',
        'LIST.deepClone() --> LIST<String>' : 'deepClone()$0',
        'LIST.deepClone(Boolean preserveId) --> LIST<String>' : 'deepClone($0)',
        'LIST.deepClone(Boolean preserveId, Boolean preserveReadOnlyTimestamps) --> LIST<String>' : 'deepClone($0)',
        'LIST.deepClone(Boolean preserveId, Boolean preserveReadOnlyTimestamps, Boolean preserveAutoNumbers) --> LIST<String>' : 'deepClone($0)',
        'LIST.get(Integer index) --> Object' : 'get($0)',
        'LIST.getSObjectType() --> Schema.SObjectType' : 'getSObjectType()$0',
        'LIST.isEmpty() --> Boolean' : 'isEmpty()$0',
        'LIST.iterator() --> system.ListIterator' : 'iterator()$0',
        'LIST.remove(Integer index) --> Object' : 'remove($0)',
        'LIST.set(Integer index, ANY value) --> void' : 'set($0)',
        'LIST.size() --> Integer' : 'size()$0',
        'LIST.sort() --> void' : 'sort()$0'
    },
    'LeadConvert' : {},
    'LicenseException' : {
        'LicenseException.getCause() --> Exception' : 'getCause()$0',
        'LicenseException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'LicenseException.getMessage() --> String' : 'getMessage()$0',
        'LicenseException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'LicenseException.getTypeName() --> String' : 'getTypeName()$0',
        'LicenseException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'LicenseException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'LimitException' : {
        'LimitException.getCause() --> Exception' : 'getCause()$0',
        'LimitException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'LimitException.getMessage() --> String' : 'getMessage()$0',
        'LimitException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'LimitException.getTypeName() --> String' : 'getTypeName()$0',
        'LimitException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'LimitException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'LinkAttachment' : {
        'LinkAttachment.equals(Object obj) --> Boolean' : 'equals($0)',
        'LinkAttachment.hashCode() --> Integer' : 'hashCode()$0',
        'LinkAttachment.toString() --> String' : 'toString()$0'
    },
    'LinkAttachmentInput' : {
        'LinkAttachmentInput.convertToJavaObject(java:common.api.AppVersion currentVersion) --> java:java.lang.Object' : 'convertToJavaObject($0)',
        'LinkAttachmentInput.equals(Object obj) --> Boolean' : 'equals($0)',
        'LinkAttachmentInput.hashCode() --> Integer' : 'hashCode()$0',
        'LinkAttachmentInput.toString() --> String' : 'toString()$0'
    },
    'LinkSegment' : {
        'LinkSegment.equals(Object obj) --> Boolean' : 'equals($0)',
        'LinkSegment.hashCode() --> Integer' : 'hashCode()$0',
        'LinkSegment.toString() --> String' : 'toString()$0'
    },
    'LinkSegmentInput' : {
        'LinkSegmentInput.convertToJavaObject(java:common.api.AppVersion currentVersion) --> java:java.lang.Object' : 'convertToJavaObject($0)',
        'LinkSegmentInput.equals(Object obj) --> Boolean' : 'equals($0)',
        'LinkSegmentInput.hashCode() --> Integer' : 'hashCode()$0',
        'LinkSegmentInput.toString() --> String' : 'toString()$0'
    },
    'ListException' : {
        'ListException.getCause() --> Exception' : 'getCause()$0',
        'ListException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'ListException.getMessage() --> String' : 'getMessage()$0',
        'ListException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'ListException.getTypeName() --> String' : 'getTypeName()$0',
        'ListException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'ListException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'LoggingLevel' : {
        'LoggingLevel.values() --> LIST<system.LoggingLevel>' : 'values()$0'
    },
    'Long' : {
        'Long.addError(APEX_OBJECT msg) --> void' : 'addError($0)',
        'Long.addError(APEX_OBJECT msg, Boolean escape) --> void' : 'addError($0)',
        'Long.addError(String msg) --> void' : 'addError($0)',
        'Long.addError(String msg, Boolean escape) --> void' : 'addError($0)',
        'Long.format() --> String' : 'format()$0',
        'Long.intValue() --> Integer' : 'intValue()$0',
        'Long.valueOf(String str) --> Long' : 'valueOf($0)'
    },
    'Map' : {
        'Map.clear() --> void' : 'clear()$0',
        'Map.clone() --> MAP<String,String>' : 'clone()$0',
        'Map.containsKey(ANY key) --> Boolean' : 'containsKey($0)',
        'Map.deepClone() --> MAP<String,String>' : 'deepClone()$0',
        'Map.get(ANY key) --> String' : 'get($0)',
        'Map.getSObjectType() --> Schema.SObjectType' : 'getSObjectType()$0',
        'Map.isEmpty() --> Boolean' : 'isEmpty()$0',
        'Map.keySet() --> SET<String>' : 'keySet()$0',
        'Map.put(ANY key, ANY value) --> String' : 'put($0)',
        'Map.putAll(LIST entries) --> void' : 'putAll($0)',
        'Map.putAll(MAP entries) --> void' : 'putAll($0)',
        'Map.remove(ANY key) --> String' : 'remove($0)',
        'Map.size() --> Integer' : 'size()$0',
        'Map.values() --> LIST<String>' : 'values()$0'
    },
    'MassEmailMessage' : {},
    'Matcher' : {
        'Matcher.end() --> Integer' : 'end()$0',
        'Matcher.end(Integer grp) --> Integer' : 'end($0)',
        'Matcher.find() --> Boolean' : 'find()$0',
        'Matcher.find(Integer start) --> Boolean' : 'find($0)',
        'Matcher.group() --> String' : 'group()$0',
        'Matcher.group(Integer start) --> String' : 'group($0)',
        'Matcher.groupCount() --> Integer' : 'groupCount()$0',
        'Matcher.hasAnchoringBounds() --> Boolean' : 'hasAnchoringBounds()$0',
        'Matcher.hasTransparentBounds() --> Boolean' : 'hasTransparentBounds()$0',
        'Matcher.hitEnd() --> Boolean' : 'hitEnd()$0',
        'Matcher.lookingAt() --> Boolean' : 'lookingAt()$0',
        'Matcher.matches() --> Boolean' : 'matches()$0',
        'Matcher.pattern() --> system.Pattern' : 'pattern()$0',
        'Matcher.quoteReplacement(String s) --> String' : 'quoteReplacement($0)',
        'Matcher.region(Integer start, Integer ending) --> system.Matcher' : 'region($0)',
        'Matcher.regionEnd() --> Integer' : 'regionEnd()$0',
        'Matcher.regionStart() --> Integer' : 'regionStart()$0',
        'Matcher.replaceAll(String replacement) --> String' : 'replaceAll($0)',
        'Matcher.replaceFirst(String replacement) --> String' : 'replaceFirst($0)',
        'Matcher.requireEnd() --> Boolean' : 'requireEnd()$0',
        'Matcher.reset() --> system.Matcher' : 'reset()$0',
        'Matcher.reset(String input) --> system.Matcher' : 'reset($0)',
        'Matcher.start() --> Integer' : 'start()$0',
        'Matcher.start(Integer grp) --> Integer' : 'start($0)',
        'Matcher.useAnchoringBounds(Boolean b) --> system.Matcher' : 'useAnchoringBounds($0)',
        'Matcher.usePattern(system.Pattern p) --> system.Matcher' : 'usePattern($0)',
        'Matcher.useTransparentBounds(Boolean b) --> system.Matcher' : 'useTransparentBounds($0)'
    },
    'Math' : {
        'Math.abs(Decimal x) --> Decimal' : 'abs($0)',
        'Math.abs(Double x) --> Double' : 'abs($0)',
        'Math.abs(Integer x) --> Integer' : 'abs($0)',
        'Math.abs(Long x) --> Long' : 'abs($0)',
        'Math.acos(Decimal x) --> Decimal' : 'acos($0)',
        'Math.acos(Double x) --> Double' : 'acos($0)',
        'Math.asin(Decimal x) --> Decimal' : 'asin($0)',
        'Math.asin(Double x) --> Double' : 'asin($0)',
        'Math.atan(Decimal x) --> Decimal' : 'atan($0)',
        'Math.atan(Double x) --> Double' : 'atan($0)',
        'Math.atan2(Decimal x, Decimal y) --> Decimal' : 'atan2($0)',
        'Math.atan2(Double x, Double y) --> Double' : 'atan2($0)',
        'Math.cbrt(Decimal x) --> Decimal' : 'cbrt($0)',
        'Math.cbrt(Double x) --> Double' : 'cbrt($0)',
        'Math.ceil(Decimal x) --> Decimal' : 'ceil($0)',
        'Math.ceil(Double x) --> Double' : 'ceil($0)',
        'Math.cos(Decimal x) --> Decimal' : 'cos($0)',
        'Math.cos(Double x) --> Double' : 'cos($0)',
        'Math.cosh(Decimal x) --> Decimal' : 'cosh($0)',
        'Math.cosh(Double x) --> Double' : 'cosh($0)',
        'Math.exp(Decimal x) --> Decimal' : 'exp($0)',
        'Math.exp(Double x) --> Double' : 'exp($0)',
        'Math.floor(Decimal x) --> Decimal' : 'floor($0)',
        'Math.floor(Double x) --> Double' : 'floor($0)',
        'Math.log(Decimal x) --> Decimal' : 'log($0)',
        'Math.log(Double x) --> Double' : 'log($0)',
        'Math.log10(Decimal x) --> Decimal' : 'log10($0)',
        'Math.log10(Double x) --> Double' : 'log10($0)',
        'Math.max(Decimal x, Decimal y) --> Decimal' : 'max($0)',
        'Math.max(Double x, Double y) --> Double' : 'max($0)',
        'Math.max(Integer x, Integer y) --> Integer' : 'max($0)',
        'Math.max(Long x, Long y) --> Long' : 'max($0)',
        'Math.min(Decimal x, Decimal y) --> Decimal' : 'min($0)',
        'Math.min(Double x, Double y) --> Double' : 'min($0)',
        'Math.min(Integer x, Integer y) --> Integer' : 'min($0)',
        'Math.min(Long x, Long y) --> Long' : 'min($0)',
        'Math.mod(Integer x, Integer y) --> Integer' : 'mod($0)',
        'Math.mod(Long x, Long y) --> Long' : 'mod($0)',
        'Math.pow(Double base, Double exp) --> Double' : 'pow($0)',
        'Math.random() --> Double' : 'random()$0',
        'Math.rint(Decimal x) --> Decimal' : 'rint($0)',
        'Math.rint(Double x) --> Double' : 'rint($0)',
        'Math.round(Decimal x) --> Integer' : 'round($0)',
        'Math.round(Double x) --> Integer' : 'round($0)',
        'Math.roundToLong(Decimal x) --> Long' : 'roundToLong($0)',
        'Math.roundToLong(Double x) --> Long' : 'roundToLong($0)',
        'Math.signum(Decimal x) --> Decimal' : 'signum($0)',
        'Math.signum(Double x) --> Double' : 'signum($0)',
        'Math.sin(Decimal x) --> Decimal' : 'sin($0)',
        'Math.sin(Double x) --> Double' : 'sin($0)',
        'Math.sinh(Decimal x) --> Decimal' : 'sinh($0)',
        'Math.sinh(Double x) --> Double' : 'sinh($0)',
        'Math.sqrt(Decimal x) --> Decimal' : 'sqrt($0)',
        'Math.sqrt(Double x) --> Double' : 'sqrt($0)',
        'Math.tan(Decimal x) --> Decimal' : 'tan($0)',
        'Math.tan(Double x) --> Double' : 'tan($0)',
        'Math.tanh(Decimal x) --> Decimal' : 'tanh($0)',
        'Math.tanh(Double x) --> Double' : 'tanh($0)'
    },
    'MathException' : {
        'MathException.getCause() --> Exception' : 'getCause()$0',
        'MathException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'MathException.getMessage() --> String' : 'getMessage()$0',
        'MathException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'MathException.getTypeName() --> String' : 'getTypeName()$0',
        'MathException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'MathException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'MentionSegment' : {
        'MentionSegment.equals(Object obj) --> Boolean' : 'equals($0)',
        'MentionSegment.hashCode() --> Integer' : 'hashCode()$0',
        'MentionSegment.toString() --> String' : 'toString()$0'
    },
    'MentionSegmentInput' : {
        'MentionSegmentInput.convertToJavaObject(java:common.api.AppVersion currentVersion) --> java:java.lang.Object' : 'convertToJavaObject($0)',
        'MentionSegmentInput.equals(Object obj) --> Boolean' : 'equals($0)',
        'MentionSegmentInput.hashCode() --> Integer' : 'hashCode()$0',
        'MentionSegmentInput.toString() --> String' : 'toString()$0'
    },
    'Message' : {
        'Message.getComponentLabel() --> String' : 'getComponentLabel()$0',
        'Message.getDetail() --> String' : 'getDetail()$0',
        'Message.getSeverity() --> ApexPages.Severity' : 'getSeverity()$0',
        'Message.getSummary() --> String' : 'getSummary()$0'
    },
    'MessageBody' : {
        'MessageBody.equals(Object obj) --> Boolean' : 'equals($0)',
        'MessageBody.hashCode() --> Integer' : 'hashCode()$0',
        'MessageBody.toString() --> String' : 'toString()$0'
    },
    'MessageBodyInput' : {
        'MessageBodyInput.convertToJavaObject(java:common.api.AppVersion currentVersion) --> java:java.lang.Object' : 'convertToJavaObject($0)',
        'MessageBodyInput.equals(Object obj) --> Boolean' : 'equals($0)',
        'MessageBodyInput.hashCode() --> Integer' : 'hashCode()$0',
        'MessageBodyInput.toString() --> String' : 'toString()$0'
    },
    'MessageSegment' : {
        'MessageSegment.equals(Object obj) --> Boolean' : 'equals($0)',
        'MessageSegment.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'MessageSegment.hashCode() --> Integer' : 'hashCode()$0',
        'MessageSegment.toString() --> String' : 'toString()$0'
    },
    'MessageSegmentInput' : {
        'MessageSegmentInput.convertToJavaObject(java:common.api.AppVersion param1) --> java:java.lang.Object' : 'convertToJavaObject($0)',
        'MessageSegmentInput.equals(Object obj) --> Boolean' : 'equals($0)',
        'MessageSegmentInput.hashCode() --> Integer' : 'hashCode()$0',
        'MessageSegmentInput.toString() --> String' : 'toString()$0'
    },
    'MessageSegmentType' : {
        'MessageSegmentType.values() --> LIST<ConnectApi.MessageSegmentType>' : 'values()$0'
    },
    'Messaging' : {
        'Messaging.reserveMassEmailCapacity(Integer count) --> void' : 'reserveMassEmailCapacity($0)',
        'Messaging.reserveSingleEmailCapacity(Integer count) --> void' : 'reserveSingleEmailCapacity($0)',
        'Messaging.sendEmail(LIST<Messaging.Email> emailMessages) --> LIST<Messaging.SendEmailResult>' : 'sendEmail($0)',
        'Messaging.sendEmail(LIST<Messaging.Email> emailMessages, Boolean allOrNothing) --> LIST<Messaging.SendEmailResult>' : 'sendEmail($0)',
        'Messaging.sendEmailMessage(LIST<Id> emailMessagesIds) --> LIST<Messaging.SendEmailResult>' : 'sendEmailMessage($0)',
        'Messaging.sendEmailMessage(LIST<Id> emailMessagesIds, Boolean allOrNothing) --> LIST<Messaging.SendEmailResult>' : 'sendEmailMessage($0)'
    },
    'MobilePushNotification' : {
        'MobilePushNotification.send(String application, SET<String> users) --> void' : 'send($0)',
        'MobilePushNotification.setPayload(MAP<String,ANY> payload) --> void' : 'setPayload($0)',
        'MobilePushNotification.setTtl(Integer ttl) --> void' : 'setTtl($0)'
    },
    'MobilePushPayload' : {
        'MobilePushPayload.apple(String alert, String sound, Integer badgeCount, MAP<String,ANY> userData) --> MAP<String,ANY>' : 'apple($0)',
        'MobilePushPayload.apple(String alertBody, String actionLocKey, String locKey, LIST<String> locArgs, String launchImage, String sound, Integer badgeCount, MAP<String,ANY> userData) --> MAP<String,ANY>' : 'apple($0)'
    },
    'MoreChangesSegment' : {
        'MoreChangesSegment.equals(Object obj) --> Boolean' : 'equals($0)',
        'MoreChangesSegment.hashCode() --> Integer' : 'hashCode()$0',
        'MoreChangesSegment.toString() --> String' : 'toString()$0'
    },
    'Motif' : {
        'Motif.equals(Object obj) --> Boolean' : 'equals($0)',
        'Motif.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'Motif.hashCode() --> Integer' : 'hashCode()$0',
        'Motif.toString() --> String' : 'toString()$0'
    },
    'MultiStaticResourceCalloutMock' : {
        'MultiStaticResourceCalloutMock.respond(System.HttpRequest request) --> System.HttpResponse' : 'respond($0)',
        'MultiStaticResourceCalloutMock.setHeader(String key, String val) --> void' : 'setHeader($0)',
        'MultiStaticResourceCalloutMock.setStaticResource(String url, String staticResourceName) --> void' : 'setStaticResource($0)',
        'MultiStaticResourceCalloutMock.setStatus(String status) --> void' : 'setStatus($0)',
        'MultiStaticResourceCalloutMock.setStatusCode(Integer code) --> void' : 'setStatusCode($0)'
    },
    'Network' : {
        'Network.communitiesLanding() --> System.PageReference' : 'communitiesLanding()$0',
        'Network.forwardToAuthPage(String startUrl) --> System.PageReference' : 'forwardToAuthPage($0)',
        'Network.forwardToAuthPage(String startUrl, String displayType) --> System.PageReference' : 'forwardToAuthPage($0)',
        'Network.getNetworkId() --> String' : 'getNetworkId()$0'
    },
    'NewFileAttachmentInput' : {
        'NewFileAttachmentInput.convertToJavaObject(java:common.api.AppVersion currentVersion) --> java:java.lang.Object' : 'convertToJavaObject($0)',
        'NewFileAttachmentInput.equals(Object obj) --> Boolean' : 'equals($0)',
        'NewFileAttachmentInput.hashCode() --> Integer' : 'hashCode()$0',
        'NewFileAttachmentInput.toString() --> String' : 'toString()$0'
    },
    'NoAccessException' : {
        'NoAccessException.getCause() --> Exception' : 'getCause()$0',
        'NoAccessException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'NoAccessException.getMessage() --> String' : 'getMessage()$0',
        'NoAccessException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'NoAccessException.getTypeName() --> String' : 'getTypeName()$0',
        'NoAccessException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'NoAccessException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'NoDataFoundException' : {
        'NoDataFoundException.getCause() --> Exception' : 'getCause()$0',
        'NoDataFoundException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'NoDataFoundException.getMessage() --> String' : 'getMessage()$0',
        'NoDataFoundException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'NoDataFoundException.getTypeName() --> String' : 'getTypeName()$0',
        'NoDataFoundException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'NoDataFoundException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'NoSuchElementException' : {
        'NoSuchElementException.getCause() --> Exception' : 'getCause()$0',
        'NoSuchElementException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'NoSuchElementException.getMessage() --> String' : 'getMessage()$0',
        'NoSuchElementException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'NoSuchElementException.getTypeName() --> String' : 'getTypeName()$0',
        'NoSuchElementException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'NoSuchElementException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'NotFoundException' : {
        'NotFoundException.getTypeName() --> String' : 'getTypeName()$0'
    },
    'NullPointerException' : {
        'NullPointerException.getCause() --> Exception' : 'getCause()$0',
        'NullPointerException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'NullPointerException.getMessage() --> String' : 'getMessage()$0',
        'NullPointerException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'NullPointerException.getTypeName() --> String' : 'getTypeName()$0',
        'NullPointerException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'NullPointerException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'Organization' : {
        'Organization.getSettings() --> ConnectApi.OrganizationSettings' : 'getSettings()$0'
    },
    'OrganizationSettings' : {
        'OrganizationSettings.equals(Object obj) --> Boolean' : 'equals($0)',
        'OrganizationSettings.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'OrganizationSettings.hashCode() --> Integer' : 'hashCode()$0',
        'OrganizationSettings.toString() --> String' : 'toString()$0'
    },
    'OutputParameter' : {},
    'PageReference' : {
        'PageReference.getAnchor() --> String' : 'getAnchor()$0',
        'PageReference.getContent() --> Blob' : 'getContent()$0',
        'PageReference.getContentAsPDF() --> Blob' : 'getContentAsPDF()$0',
        'PageReference.getCookies() --> MAP<String,System.Cookie>' : 'getCookies()$0',
        'PageReference.getHeaders() --> MAP<String,String>' : 'getHeaders()$0',
        'PageReference.getParameters() --> MAP<String,String>' : 'getParameters()$0',
        'PageReference.getRedirect() --> Boolean' : 'getRedirect()$0',
        'PageReference.getUrl() --> String' : 'getUrl()$0',
        'PageReference.setAnchor(String anchor) --> System.PageReference' : 'setAnchor($0)',
        'PageReference.setCookies(LIST<System.Cookie> cookies) --> void' : 'setCookies($0)',
        'PageReference.setRedirect(Boolean redirect) --> System.PageReference' : 'setRedirect($0)'
    },
    'ParameterType' : {
        'ParameterType.values() --> LIST<Process.PluginDescribeResult.ParameterType>' : 'values()$0'
    },
    'Pattern' : {
        'Pattern.compile(String regex) --> system.Pattern' : 'compile($0)',
        'Pattern.matcher(String input) --> system.Matcher' : 'matcher($0)',
        'Pattern.matches(String regex, String input) --> Boolean' : 'matches($0)',
        'Pattern.pattern() --> String' : 'pattern()$0',
        'Pattern.quote(String s) --> String' : 'quote($0)',
        'Pattern.split(String input) --> LIST<String>' : 'split($0)',
        'Pattern.split(String input, Integer n) --> LIST<String>' : 'split($0)'
    },
    'PhoneNumber' : {
        'PhoneNumber.equals(Object obj) --> Boolean' : 'equals($0)',
        'PhoneNumber.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'PhoneNumber.hashCode() --> Integer' : 'hashCode()$0',
        'PhoneNumber.toString() --> String' : 'toString()$0'
    },
    'Photo' : {
        'Photo.equals(Object obj) --> Boolean' : 'equals($0)',
        'Photo.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'Photo.hashCode() --> Integer' : 'hashCode()$0',
        'Photo.toString() --> String' : 'toString()$0'
    },
    'Plugin' : {
        'Plugin.describe() --> Process.PluginDescribeResult' : 'describe()$0',
        'Plugin.invoke(Process.PluginRequest param1) --> Process.PluginResult' : 'invoke($0)'
    },
    'PluginDescribeResult' : {},
    'PluginRequest' : {},
    'PluginResult' : {},
    'PollAttachmentInput' : {
        'PollAttachmentInput.convertToJavaObject(java:common.api.AppVersion currentVersion) --> java:java.lang.Object' : 'convertToJavaObject($0)',
        'PollAttachmentInput.equals(Object obj) --> Boolean' : 'equals($0)',
        'PollAttachmentInput.hashCode() --> Integer' : 'hashCode()$0',
        'PollAttachmentInput.toString() --> String' : 'toString()$0'
    },
    'ProcedureException' : {
        'ProcedureException.getCause() --> Exception' : 'getCause()$0',
        'ProcedureException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'ProcedureException.getMessage() --> String' : 'getMessage()$0',
        'ProcedureException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'ProcedureException.getTypeName() --> String' : 'getTypeName()$0',
        'ProcedureException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'ProcedureException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'PublishingService' : {
        'PublishingService.archiveOnlineArticle(String articleId, Datetime scheduledDate) --> void' : 'archiveOnlineArticle($0)',
        'PublishingService.assignDraftArticleTask(String articleId, String assigneeId, String instructions, Datetime dueDate, Boolean sendEmailNotification) --> void' : 'assignDraftArticleTask($0)',
        'PublishingService.assignDraftTranslationTask(String translationVersionId, String assigneeId, String instructions, Datetime dueDate, Boolean sendEmailNotification) --> void' : 'assignDraftTranslationTask($0)',
        'PublishingService.cancelScheduledArchivingOfArticle(String articleId) --> void' : 'cancelScheduledArchivingOfArticle($0)',
        'PublishingService.cancelScheduledPublicationOfArticle(String articleId) --> void' : 'cancelScheduledPublicationOfArticle($0)',
        'PublishingService.completeTranslation(String articleVersionId) --> void' : 'completeTranslation($0)',
        'PublishingService.deleteArchivedArticle(String articleId) --> void' : 'deleteArchivedArticle($0)',
        'PublishingService.deleteArchivedArticleVersion(String articleId, Integer versionNumber) --> void' : 'deleteArchivedArticleVersion($0)',
        'PublishingService.deleteDraftArticle(String articleId) --> void' : 'deleteDraftArticle($0)',
        'PublishingService.deleteDraftTranslation(String articleVersionId) --> void' : 'deleteDraftTranslation($0)',
        'PublishingService.editArchivedArticle(String articleId) --> String' : 'editArchivedArticle($0)',
        'PublishingService.editOnlineArticle(String articleId, Boolean unpublish) --> String' : 'editOnlineArticle($0)',
        'PublishingService.editPublishedTranslation(String articleId, String language, Boolean unpublish) --> String' : 'editPublishedTranslation($0)',
        'PublishingService.publishArticle(String articleId, Boolean flagAsNew) --> void' : 'publishArticle($0)',
        'PublishingService.restoreOldVersion(String articleId, Integer versionNumber) --> String' : 'restoreOldVersion($0)',
        'PublishingService.scheduleForPublication(String articleId, Datetime scheduledDate) --> void' : 'scheduleForPublication($0)',
        'PublishingService.setTranslationToIncomplete(String articleVersionId) --> void' : 'setTranslationToIncomplete($0)',
        'PublishingService.submitForTranslation(String articleId, String language, String assigneeId, Datetime dueDate) --> String' : 'submitForTranslation($0)'
    },
    'QueryException' : {
        'QueryException.getCause() --> Exception' : 'getCause()$0',
        'QueryException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'QueryException.getMessage() --> String' : 'getMessage()$0',
        'QueryException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'QueryException.getTypeName() --> String' : 'getTypeName()$0',
        'QueryException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'QueryException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'QueryLocator' : {
        'QueryLocator.getQuery() --> String' : 'getQuery()$0',
        'QueryLocator.iterator() --> Database.QueryLocatorIterator' : 'iterator()$0'
    },
    'QueryLocatorChunkIterator' : {
        'QueryLocatorChunkIterator.hasNext() --> Boolean' : 'hasNext()$0',
        'QueryLocatorChunkIterator.next() --> LIST<SObject>' : 'next()$0'
    },
    'QueryLocatorIterator' : {
        'QueryLocatorIterator.hasNext() --> Boolean' : 'hasNext()$0',
        'QueryLocatorIterator.next() --> SObject' : 'next()$0'
    },
    'RateLimitException' : {
        'RateLimitException.getErrorCode() --> String' : 'getErrorCode()$0',
        'RateLimitException.getTypeName() --> String' : 'getTypeName()$0'
    },
    'RecordSummary' : {
        'RecordSummary.equals(Object obj) --> Boolean' : 'equals($0)',
        'RecordSummary.hashCode() --> Integer' : 'hashCode()$0',
        'RecordSummary.toString() --> String' : 'toString()$0'
    },
    'Records' : {
        'Records.getMotif(String communityId, String idOrPrefix) --> ConnectApi.Motif' : 'getMotif($0)'
    },
    'Reference' : {
        'Reference.equals(Object obj) --> Boolean' : 'equals($0)',
        'Reference.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'Reference.hashCode() --> Integer' : 'hashCode()$0',
        'Reference.toString() --> String' : 'toString()$0'
    },
    'RequiredFeatureMissingException' : {
        'RequiredFeatureMissingException.getCause() --> Exception' : 'getCause()$0',
        'RequiredFeatureMissingException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'RequiredFeatureMissingException.getMessage() --> String' : 'getMessage()$0',
        'RequiredFeatureMissingException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'RequiredFeatureMissingException.getTypeName() --> String' : 'getTypeName()$0',
        'RequiredFeatureMissingException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'RequiredFeatureMissingException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'ResourceLinkSegment' : {
        'ResourceLinkSegment.equals(Object obj) --> Boolean' : 'equals($0)',
        'ResourceLinkSegment.hashCode() --> Integer' : 'hashCode()$0',
        'ResourceLinkSegment.toString() --> String' : 'toString()$0'
    },
    'RestContext' : {},
    'RestRequest' : {
        'RestRequest.addHeader(String name, String value) --> void' : 'addHeader($0)',
        'RestRequest.addParameter(String name, String value) --> void' : 'addParameter($0)'
    },
    'RestResponse' : {
        'RestResponse.addHeader(String name, String value) --> void' : 'addHeader($0)'
    },
    'SObject' : {
        'SObject.addError(APEX_OBJECT msg) --> void' : 'addError($0)',
        'SObject.addError(APEX_OBJECT msg, Boolean escape) --> void' : 'addError($0)',
        'SObject.addError(String msg) --> void' : 'addError($0)',
        'SObject.addError(String msg, Boolean escape) --> void' : 'addError($0)',
        'SObject.clear() --> void' : 'clear()$0',
        'SObject.clone() --> SObject' : 'clone()$0',
        'SObject.clone(Boolean preserveId) --> SObject' : 'clone($0)',
        'SObject.clone(Boolean preserveId, Boolean deep) --> SObject' : 'clone($0)',
        'SObject.clone(Boolean preserveId, Boolean deep, Boolean preserveReadOnlyTimestamps) --> SObject' : 'clone($0)',
        'SObject.clone(Boolean preserveId, Boolean deep, Boolean preserveReadOnlyTimestamps, Boolean preserveAutoNumbers) --> SObject' : 'clone($0)',
        'SObject.get(Schema.SObjectField field) --> Object' : 'get($0)',
        'SObject.get(String field) --> Object' : 'get($0)',
        'SObject.getOptions() --> Database.DMLOptions' : 'getOptions()$0',
        'SObject.getQuickActionName() --> String' : 'getQuickActionName()$0',
        'SObject.getSObject(Schema.SObjectField field) --> SObject' : 'getSObject($0)',
        'SObject.getSObject(String field) --> SObject' : 'getSObject($0)',
        'SObject.getSObjectType() --> Schema.SObjectType' : 'getSObjectType()$0',
        'SObject.getSObjects(Schema.SObjectField field) --> LIST<SObject>' : 'getSObjects($0)',
        'SObject.getSObjects(String field) --> LIST<SObject>' : 'getSObjects($0)',
        'SObject.put(Schema.SObjectField field, Object value) --> Object' : 'put($0)',
        'SObject.put(String field, Object value) --> Object' : 'put($0)',
        'SObject.putSObject(Schema.SObjectField field, SObject value) --> SObject' : 'putSObject($0)',
        'SObject.putSObject(String field, SObject value) --> SObject' : 'putSObject($0)',
        'SObject.setOptions(APEX_OBJECT options) --> void' : 'setOptions($0)'
    },
    'SObjectException' : {
        'SObjectException.getCause() --> Exception' : 'getCause()$0',
        'SObjectException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'SObjectException.getMessage() --> String' : 'getMessage()$0',
        'SObjectException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'SObjectException.getTypeName() --> String' : 'getTypeName()$0',
        'SObjectException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'SObjectException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'SObjectField' : {
        'SObjectField.getDescribe() --> Schema.DescribeFieldResult' : 'getDescribe()$0'
    },
    'SObjectType' : {
        'SObjectType.getDescribe() --> Schema.DescribeSObjectResult' : 'getDescribe()$0',
        'SObjectType.newSObject() --> SObject' : 'newSObject()$0',
        'SObjectType.newSObject(Id id) --> SObject' : 'newSObject($0)',
        'SObjectType.newSObject(Id recordTypeId, Boolean loadDefaultValues) --> SObject' : 'newSObject($0)'
    },
    'Schedulable' : {
        'Schedulable.execute(system.SchedulableContext param1) --> void' : 'execute($0)'
    },
    'SchedulableContext' : {
        'SchedulableContext.getTriggerId() --> Id' : 'getTriggerId()$0'
    },
    'Schema' : {
        'Schema.describeDataCategoryGroupStructures(LIST<Schema.DataCategoryGroupSobjectTypePair> pairs, Boolean topCategoriesOnly) --> LIST<Schema.DescribeDataCategoryGroupStructureResult>' : 'describeDataCategoryGroupStructures($0)',
        'Schema.describeDataCategoryGroups(LIST<String> sobjects) --> LIST<Schema.DescribeDataCategoryGroupResult>' : 'describeDataCategoryGroups($0)',
        'Schema.getAppDescribe(String appName) --> MAP<String,Schema.SObjectType>' : 'getAppDescribe($0)',
        'Schema.getGlobalDescribe() --> MAP<String,Schema.SObjectType>' : 'getGlobalDescribe()$0',
        'Schema.getModuleDescribe() --> MAP<String,Schema.SObjectType>' : 'getModuleDescribe()$0',
        'Schema.getModuleDescribe(String moduleName) --> MAP<String,Schema.SObjectType>' : 'getModuleDescribe($0)'
    },
    'SearchException' : {
        'SearchException.getCause() --> Exception' : 'getCause()$0',
        'SearchException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'SearchException.getMessage() --> String' : 'getMessage()$0',
        'SearchException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'SearchException.getTypeName() --> String' : 'getTypeName()$0',
        'SearchException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'SearchException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'SecurityException' : {
        'SecurityException.getCause() --> Exception' : 'getCause()$0',
        'SecurityException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'SecurityException.getMessage() --> String' : 'getMessage()$0',
        'SecurityException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'SecurityException.getTypeName() --> String' : 'getTypeName()$0',
        'SecurityException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'SecurityException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'SelectOption' : {
        'SelectOption.getDisabled() --> Boolean' : 'getDisabled()$0',
        'SelectOption.getEscapeItem() --> Boolean' : 'getEscapeItem()$0',
        'SelectOption.getLabel() --> String' : 'getLabel()$0',
        'SelectOption.getValue() --> String' : 'getValue()$0',
        'SelectOption.setDisabled(Boolean disabled) --> void' : 'setDisabled($0)',
        'SelectOption.setEscapeItem(Boolean disabled) --> void' : 'setEscapeItem($0)',
        'SelectOption.setLabel(String label) --> void' : 'setLabel($0)',
        'SelectOption.setValue(String value) --> void' : 'setValue($0)'
    },
    'SerializationException' : {
        'SerializationException.getCause() --> Exception' : 'getCause()$0',
        'SerializationException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'SerializationException.getMessage() --> String' : 'getMessage()$0',
        'SerializationException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'SerializationException.getTypeName() --> String' : 'getTypeName()$0',
        'SerializationException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'SerializationException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'Set' : {
        'Set.add(ANY element) --> Boolean' : 'add($0)',
        'Set.addAll(LIST elements) --> Boolean' : 'addAll($0)',
        'Set.addAll(SET elements) --> Boolean' : 'addAll($0)',
        'Set.clear() --> void' : 'clear()$0',
        'Set.clone() --> SET<String>' : 'clone()$0',
        'Set.contains(ANY element) --> Boolean' : 'contains($0)',
        'Set.containsAll(LIST elements) --> Boolean' : 'containsAll($0)',
        'Set.containsAll(SET elements) --> Boolean' : 'containsAll($0)',
        'Set.isEmpty() --> Boolean' : 'isEmpty()$0',
        'Set.iterator() --> system.ListIterator' : 'iterator()$0',
        'Set.remove(ANY element) --> Boolean' : 'remove($0)',
        'Set.removeAll(LIST elements) --> Boolean' : 'removeAll($0)',
        'Set.removeAll(SET elements) --> Boolean' : 'removeAll($0)',
        'Set.retainAll(LIST elements) --> Boolean' : 'retainAll($0)',
        'Set.retainAll(SET elements) --> Boolean' : 'retainAll($0)',
        'Set.size() --> Integer' : 'size()$0'
    },
    'SetupScope' : {
        'SetupScope.values() --> LIST<system.SetupScope>' : 'values()$0'
    },
    'Severity' : {
        'Severity.values() --> LIST<ApexPages.Severity>' : 'values()$0'
    },
    'SingleEmailMessage' : {},
    'Site' : {
        'Site.changePassword(String newPassword, String verifyNewPassword) --> System.PageReference' : 'changePassword($0)',
        'Site.changePassword(String newPassword, String verifyNewPassword, String oldPassword) --> System.PageReference' : 'changePassword($0)',
        'Site.createPersonAccountPortalUser(SObject user, String ownerId, String password) --> Id' : 'createPersonAccountPortalUser($0)',
        'Site.createPersonAccountPortalUser(SObject user, String ownerId, String recordTypeId, String password) --> Id' : 'createPersonAccountPortalUser($0)',
        'Site.createPortalUser(SObject user, String accountId) --> Id' : 'createPortalUser($0)',
        'Site.createPortalUser(SObject user, String accountId, String password) --> Id' : 'createPortalUser($0)',
        'Site.createPortalUser(SObject user, String accountId, String password, Boolean sendEmailConfirmation) --> Id' : 'createPortalUser($0)',
        'Site.forgotPassword(String username) --> Boolean' : 'forgotPassword($0)',
        'Site.getAdminEmail() --> String' : 'getAdminEmail()$0',
        'Site.getAdminId() --> Id' : 'getAdminId()$0',
        'Site.getAnalyticsTrackingCode() --> String' : 'getAnalyticsTrackingCode()$0',
        'Site.getCurrentSiteUrl() --> String' : 'getCurrentSiteUrl()$0',
        'Site.getCustomWebAddress() --> String' : 'getCustomWebAddress()$0',
        'Site.getDomain() --> String' : 'getDomain()$0',
        'Site.getErrorDescription() --> String' : 'getErrorDescription()$0',
        'Site.getErrorMessage() --> String' : 'getErrorMessage()$0',
        'Site.getName() --> String' : 'getName()$0',
        'Site.getOriginalUrl() --> String' : 'getOriginalUrl()$0',
        'Site.getPrefix() --> String' : 'getPrefix()$0',
        'Site.getTemplate() --> System.PageReference' : 'getTemplate()$0',
        'Site.isLoginEnabled() --> Boolean' : 'isLoginEnabled()$0',
        'Site.isPasswordExpired() --> Boolean' : 'isPasswordExpired()$0',
        'Site.isRegistrationEnabled() --> Boolean' : 'isRegistrationEnabled()$0',
        'Site.login(String username, String password, String startUrl) --> System.PageReference' : 'login($0)',
        'Site.setPortalUserAsAuthProvider(SObject user, String accountId) --> void' : 'setPortalUserAsAuthProvider($0)'
    },
    'SoapType' : {
        'SoapType.values() --> LIST<Schema.SoapType>' : 'values()$0'
    },
    'SparkPlugApi' : {
        'SparkPlugApi.describePlugin(String className) --> Process.SparkPlugApi.SparkPlugDescribeResult' : 'describePlugin($0)',
        'SparkPlugApi.describePlugins() --> LIST<Process.SparkPlugApi.SparkPlugDescribeResult>' : 'describePlugins()$0',
        'SparkPlugApi.invokePluginWithJson(String className, String parameters) --> String' : 'invokePluginWithJson($0)'
    },
    'SparkPlugDescribeResult' : {},
    'SparkPlugParameter' : {},
    'Stack' : {
        'Stack.empty() --> Boolean' : 'empty()$0',
        'Stack.peek() --> String' : 'peek()$0',
        'Stack.pop() --> String' : 'pop()$0',
        'Stack.push(String item) --> void' : 'push($0)'
    },
    'StandardController' : {
        'StandardController.addFields(LIST<String> fieldNames) --> void' : 'addFields($0)',
        'StandardController.cancel() --> System.PageReference' : 'cancel()$0',
        'StandardController.delete() --> System.PageReference' : 'delete()$0',
        'StandardController.edit() --> System.PageReference' : 'edit()$0',
        'StandardController.getId() --> String' : 'getId()$0',
        'StandardController.getRecord() --> SObject' : 'getRecord()$0',
        'StandardController.getSubject() --> SObject' : 'getSubject()$0',
        'StandardController.reset() --> void' : 'reset()$0',
        'StandardController.save() --> System.PageReference' : 'save()$0',
        'StandardController.view() --> System.PageReference' : 'view()$0'
    },
    'StandardSetController' : {
        'StandardSetController.addFields(LIST<String> fieldNames) --> void' : 'addFields($0)',
        'StandardSetController.cancel() --> System.PageReference' : 'cancel()$0',
        'StandardSetController.first() --> void' : 'first()$0',
        'StandardSetController.getCompleteResult() --> Boolean' : 'getCompleteResult()$0',
        'StandardSetController.getFilterId() --> String' : 'getFilterId()$0',
        'StandardSetController.getHasNext() --> Boolean' : 'getHasNext()$0',
        'StandardSetController.getHasPrevious() --> Boolean' : 'getHasPrevious()$0',
        'StandardSetController.getListViewOptions() --> LIST<System.SelectOption>' : 'getListViewOptions()$0',
        'StandardSetController.getPageNumber() --> Integer' : 'getPageNumber()$0',
        'StandardSetController.getPageSize() --> Integer' : 'getPageSize()$0',
        'StandardSetController.getRecord() --> SObject' : 'getRecord()$0',
        'StandardSetController.getRecords() --> LIST<SObject>' : 'getRecords()$0',
        'StandardSetController.getResultSize() --> Integer' : 'getResultSize()$0',
        'StandardSetController.getSelected() --> LIST<SObject>' : 'getSelected()$0',
        'StandardSetController.last() --> void' : 'last()$0',
        'StandardSetController.next() --> void' : 'next()$0',
        'StandardSetController.previous() --> void' : 'previous()$0',
        'StandardSetController.reset() --> void' : 'reset()$0',
        'StandardSetController.save() --> System.PageReference' : 'save()$0',
        'StandardSetController.setFilterId(String filterId) --> void' : 'setFilterId($0)',
        'StandardSetController.setPageNumber(Integer pageNumber) --> void' : 'setPageNumber($0)',
        'StandardSetController.setPageSize(Integer pageSize) --> void' : 'setPageSize($0)',
        'StandardSetController.setSelected(LIST<SObject> selected) --> void' : 'setSelected($0)'
    },
    'StaticResourceCalloutMock' : {
        'StaticResourceCalloutMock.respond(System.HttpRequest request) --> System.HttpResponse' : 'respond($0)',
        'StaticResourceCalloutMock.setHeader(String key, String val) --> void' : 'setHeader($0)',
        'StaticResourceCalloutMock.setStaticResource(String staticResourceName) --> void' : 'setStaticResource($0)',
        'StaticResourceCalloutMock.setStatus(String status) --> void' : 'setStatus($0)',
        'StaticResourceCalloutMock.setStatusCode(Integer code) --> void' : 'setStatusCode($0)'
    },
    'StatusCode' : {
        'StatusCode.values() --> LIST<system.StatusCode>' : 'values()$0'
    },
    'String' : {
        'String.abbreviate(Integer maxWidth) --> String' : 'abbreviate($0)',
        'String.abbreviate(Integer maxWidth, Integer offset) --> String' : 'abbreviate($0)',
        'String.addError(APEX_OBJECT msg) --> void' : 'addError($0)',
        'String.addError(APEX_OBJECT msg, Boolean escape) --> void' : 'addError($0)',
        'String.addError(String msg) --> void' : 'addError($0)',
        'String.addError(String msg, Boolean escape) --> void' : 'addError($0)',
        'String.capitalize() --> String' : 'capitalize()$0',
        'String.center(Integer size) --> String' : 'center($0)',
        'String.center(Integer size, String padStr) --> String' : 'center($0)',
        'String.compareTo(String str) --> Integer' : 'compareTo($0)',
        'String.contains(String str) --> Boolean' : 'contains($0)',
        'String.containsAny(String validChars) --> Boolean' : 'containsAny($0)',
        'String.containsIgnoreCase(String searchStr) --> Boolean' : 'containsIgnoreCase($0)',
        'String.containsNone(String invalidChars) --> Boolean' : 'containsNone($0)',
        'String.containsOnly(String validChars) --> Boolean' : 'containsOnly($0)',
        'String.containsWhitespace() --> Boolean' : 'containsWhitespace()$0',
        'String.countMatches(String searchStr) --> Integer' : 'countMatches($0)',
        'String.deleteWhitespace() --> String' : 'deleteWhitespace()$0',
        'String.difference(String other) --> String' : 'difference($0)',
        'String.endsWith(String str) --> Boolean' : 'endsWith($0)',
        'String.endsWithIgnoreCase(String suffix) --> Boolean' : 'endsWithIgnoreCase($0)',
        'String.equals(String other) --> Boolean' : 'equals($0)',
        'String.equalsIgnoreCase(String other) --> Boolean' : 'equalsIgnoreCase($0)',
        'String.escapeCsv() --> String' : 'escapeCsv()$0',
        'String.escapeEcmaScript() --> String' : 'escapeEcmaScript()$0',
        'String.escapeHtml3() --> String' : 'escapeHtml3()$0',
        'String.escapeHtml4() --> String' : 'escapeHtml4()$0',
        'String.escapeSingleQuotes(String s) --> String' : 'escapeSingleQuotes($0)',
        'String.escapeXml() --> String' : 'escapeXml()$0',
        'String.format(String format, LIST<String> arguments) --> String' : 'format($0)',
        'String.fromCharArray(LIST<Integer> charArr) --> String' : 'fromCharArray($0)',
        'String.getCommonPrefix(LIST strings) --> String' : 'getCommonPrefix($0)',
        'String.getLevenshteinDistance(String other) --> Integer' : 'getLevenshteinDistance($0)',
        'String.getLevenshteinDistance(String other, Integer threshold) --> Integer' : 'getLevenshteinDistance($0)',
        'String.hashCode() --> Integer' : 'hashCode()$0',
        'String.indexOf(String str) --> Integer' : 'indexOf($0)',
        'String.indexOf(String str, Integer startPos) --> Integer' : 'indexOf($0)',
        'String.indexOfAny(String searchChars) --> Integer' : 'indexOfAny($0)',
        'String.indexOfAnyBut(String searchChars) --> Integer' : 'indexOfAnyBut($0)',
        'String.indexOfDifference(String other) --> Integer' : 'indexOfDifference($0)',
        'String.indexOfIgnoreCase(String searchStr) --> Integer' : 'indexOfIgnoreCase($0)',
        'String.indexOfIgnoreCase(String searchStr, Integer startPos) --> Integer' : 'indexOfIgnoreCase($0)',
        'String.isAllLowerCase() --> Boolean' : 'isAllLowerCase()$0',
        'String.isAllUpperCase() --> Boolean' : 'isAllUpperCase()$0',
        'String.isAlpha() --> Boolean' : 'isAlpha()$0',
        'String.isAlphaSpace() --> Boolean' : 'isAlphaSpace()$0',
        'String.isAlphanumeric() --> Boolean' : 'isAlphanumeric()$0',
        'String.isAlphanumericSpace() --> Boolean' : 'isAlphanumericSpace()$0',
        'String.isAsciiPrintable() --> Boolean' : 'isAsciiPrintable()$0',
        'String.isBlank(String str) --> Boolean' : 'isBlank($0)',
        'String.isEmpty(String str) --> Boolean' : 'isEmpty($0)',
        'String.isNotBlank(String str) --> Boolean' : 'isNotBlank($0)',
        'String.isNotEmpty(String str) --> Boolean' : 'isNotEmpty($0)',
        'String.isNumeric() --> Boolean' : 'isNumeric()$0',
        'String.isNumericSpace() --> Boolean' : 'isNumericSpace()$0',
        'String.isWhitespace() --> Boolean' : 'isWhitespace()$0',
        'String.join(APEX_OBJECT iterableObj, String separator) --> String' : 'join($0)',
        'String.lastIndexOf(String searchStr, Integer startPos) --> Integer' : 'lastIndexOf($0)',
        'String.lastIndexOf(String str) --> Integer' : 'lastIndexOf($0)',
        'String.lastIndexOfIgnoreCase(String searchStr) --> Integer' : 'lastIndexOfIgnoreCase($0)',
        'String.lastIndexOfIgnoreCase(String searchStr, Integer startPos) --> Integer' : 'lastIndexOfIgnoreCase($0)',
        'String.left(Integer len) --> String' : 'left($0)',
        'String.leftPad(Integer len) --> String' : 'leftPad($0)',
        'String.leftPad(Integer len, String padStr) --> String' : 'leftPad($0)',
        'String.length() --> Integer' : 'length()$0',
        'String.mid(Integer pos, Integer len) --> String' : 'mid($0)',
        'String.normalizeSpace() --> String' : 'normalizeSpace()$0',
        'String.overlay(String overlay, Integer start, Integer end) --> String' : 'overlay($0)',
        'String.remove(String toRemove) --> String' : 'remove($0)',
        'String.removeEnd(String toRemove) --> String' : 'removeEnd($0)',
        'String.removeEndIgnoreCase(String toRemove) --> String' : 'removeEndIgnoreCase($0)',
        'String.removeStart(String toRemove) --> String' : 'removeStart($0)',
        'String.removeStartIgnoreCase(String toRemove) --> String' : 'removeStartIgnoreCase($0)',
        'String.repeat(Integer numTimes) --> String' : 'repeat($0)',
        'String.repeat(String separator, Integer numTimes) --> String' : 'repeat($0)',
        'String.replace(String target, String replacement) --> String' : 'replace($0)',
        'String.replaceAll(String regex, String replacement) --> String' : 'replaceAll($0)',
        'String.replaceFirst(String regex, String replacement) --> String' : 'replaceFirst($0)',
        'String.reverse() --> String' : 'reverse()$0',
        'String.right(Integer len) --> String' : 'right($0)',
        'String.rightPad(Integer len) --> String' : 'rightPad($0)',
        'String.rightPad(Integer len, String padStr) --> String' : 'rightPad($0)',
        'String.split(String regex) --> LIST<String>' : 'split($0)',
        'String.split(String regex, Integer limit) --> LIST<String>' : 'split($0)',
        'String.splitByCharacterType() --> LIST<String>' : 'splitByCharacterType()$0',
        'String.splitByCharacterTypeCamelCase() --> LIST<String>' : 'splitByCharacterTypeCamelCase()$0',
        'String.startsWith(String str) --> Boolean' : 'startsWith($0)',
        'String.startsWithIgnoreCase(String prefix) --> Boolean' : 'startsWithIgnoreCase($0)',
        'String.stripHtmlTags() --> String' : 'stripHtmlTags()$0',
        'String.substring(Integer start) --> String' : 'substring($0)',
        'String.substring(Integer start, Integer end) --> String' : 'substring($0)',
        'String.substringAfter(String separator) --> String' : 'substringAfter($0)',
        'String.substringAfterLast(String separator) --> String' : 'substringAfterLast($0)',
        'String.substringBefore(String separator) --> String' : 'substringBefore($0)',
        'String.substringBeforeLast(String separator) --> String' : 'substringBeforeLast($0)',
        'String.substringBetween(String open, String close) --> String' : 'substringBetween($0)',
        'String.substringBetween(String tag) --> String' : 'substringBetween($0)',
        'String.swapCase() --> String' : 'swapCase()$0',
        'String.toLowerCase() --> String' : 'toLowerCase()$0',
        'String.toLowerCase(String locale) --> String' : 'toLowerCase($0)',
        'String.toUpperCase() --> String' : 'toUpperCase()$0',
        'String.toUpperCase(String locale) --> String' : 'toUpperCase($0)',
        'String.trim() --> String' : 'trim()$0',
        'String.uncapitalize() --> String' : 'uncapitalize()$0',
        'String.unescapeCsv() --> String' : 'unescapeCsv()$0',
        'String.unescapeEcmaScript() --> String' : 'unescapeEcmaScript()$0',
        'String.unescapeHtml3() --> String' : 'unescapeHtml3()$0',
        'String.unescapeHtml4() --> String' : 'unescapeHtml4()$0',
        'String.unescapeXml() --> String' : 'unescapeXml()$0',
        'String.valueOf(Date d) --> String' : 'valueOf($0)',
        'String.valueOf(Datetime dt) --> String' : 'valueOf($0)',
        'String.valueOf(Decimal d) --> String' : 'valueOf($0)',
        'String.valueOf(Double d) --> String' : 'valueOf($0)',
        'String.valueOf(Integer i) --> String' : 'valueOf($0)',
        'String.valueOf(Long l) --> String' : 'valueOf($0)',
        'String.valueOf(Object o) --> String' : 'valueOf($0)',
        'String.valueOfGmt(Datetime dt) --> String' : 'valueOfGmt($0)'
    },
    'StringException' : {
        'StringException.getCause() --> Exception' : 'getCause()$0',
        'StringException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'StringException.getMessage() --> String' : 'getMessage()$0',
        'StringException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'StringException.getTypeName() --> String' : 'getTypeName()$0',
        'StringException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'StringException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'Subscription' : {
        'Subscription.equals(Object obj) --> Boolean' : 'equals($0)',
        'Subscription.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'Subscription.hashCode() --> Integer' : 'hashCode()$0',
        'Subscription.toString() --> String' : 'toString()$0'
    },
    'System' : {
        'System.abortJob(String jobId) --> void' : 'abortJob($0)',
        'System.assert(Boolean condition) --> void' : 'assert($0)',
        'System.assert(Boolean condition, ANY msg) --> void' : 'assert($0)',
        'System.assertEquals(ANY expected, ANY actual) --> void' : 'assertEquals($0)',
        'System.assertEquals(ANY expected, ANY actual, ANY msg) --> void' : 'assertEquals($0)',
        'System.assertNotEquals(ANY expected, ANY actual) --> void' : 'assertNotEquals($0)',
        'System.assertNotEquals(ANY expected, ANY actual, ANY msg) --> void' : 'assertNotEquals($0)',
        'System.currentPageReference() --> System.PageReference' : 'currentPageReference()$0',
        'System.currentTimeMillis() --> Long' : 'currentTimeMillis()$0',
        'System.debug(ANY o) --> void' : 'debug($0)',
        'System.debug(APEX_OBJECT logLevel, ANY o) --> void' : 'debug($0)',
        'System.getApplicationReadWriteMode() --> system.ApplicationReadWriteMode' : 'getApplicationReadWriteMode()$0',
        'System.isBatch() --> Boolean' : 'isBatch()$0',
        'System.isFuture() --> Boolean' : 'isFuture()$0',
        'System.isScheduled() --> Boolean' : 'isScheduled()$0',
        'System.now() --> Datetime' : 'now()$0',
        'System.process(LIST workitemIds, String action, String commments, String nextApprover) --> LIST<Id>' : 'process($0)',
        'System.purgeOldAsyncJobs(Date date) --> Integer' : 'purgeOldAsyncJobs($0)',
        'System.requestVersion() --> system.Version' : 'requestVersion()$0',
        'System.resetPassword(Id userId, Boolean sendUserEmail) --> System.ResetPasswordResult' : 'resetPassword($0)',
        'System.runAs(Package.Version version) --> void' : 'runAs($0)',
        'System.runAs(SObject user, ANY block) --> void' : 'runAs($0)',
        'System.schedule(String jobName, String cronExp, APEX_OBJECT schedulable) --> String' : 'schedule($0)',
        'System.scheduleBatch(APEX_OBJECT batchable, String jobName, Integer minutesFromNow) --> String' : 'scheduleBatch($0)',
        'System.scheduleBatch(APEX_OBJECT batchable, String jobName, Integer minutesFromNow, Integer scopeSize) --> String' : 'scheduleBatch($0)',
        'System.setPassword(Id userId, String password) --> void' : 'setPassword($0)',
        'System.submit(LIST ids, String commments, String nextApprover) --> LIST<Id>' : 'submit($0)',
        'System.today() --> Date' : 'today()$0'
    },
    'Test' : {
        'Test.invokePage(System.PageReference p) --> Component.apex.page' : 'invokePage($0)',
        'Test.isRunningTest() --> Boolean' : 'isRunningTest()$0',
        'Test.loadData(Schema.SObjectType sobjectType, String staticResourceName) --> LIST<SObject>' : 'loadData($0)',
        'Test.setCurrentPage(Object pageReference) --> void' : 'setCurrentPage($0)',
        'Test.setCurrentPageReference(Object pageReference) --> void' : 'setCurrentPageReference($0)',
        'Test.setFixedSearchResults(LIST<String> searchResultsIds) --> void' : 'setFixedSearchResults($0)',
        'Test.setMock(system.Type interfaceType, Object mock) --> void' : 'setMock($0)',
        'Test.setReadOnlyApplicationMode(Boolean readOnlyApplicationMode) --> void' : 'setReadOnlyApplicationMode($0)',
        'Test.startTest() --> void' : 'startTest()$0',
        'Test.stopTest() --> void' : 'stopTest()$0',
        'Test.testInstall(system.InstallHandler script, system.Version version) --> void' : 'testInstall($0)',
        'Test.testInstall(system.InstallHandler script, system.Version version, Boolean isPush) --> void' : 'testInstall($0)',
        'Test.testUninstall(system.UninstallHandler script) --> void' : 'testUninstall($0)'
    },
    'TextAttachment' : {},
    'TextSegment' : {
        'TextSegment.equals(Object obj) --> Boolean' : 'equals($0)',
        'TextSegment.hashCode() --> Integer' : 'hashCode()$0',
        'TextSegment.toString() --> String' : 'toString()$0'
    },
    'TextSegmentInput' : {
        'TextSegmentInput.convertToJavaObject(java:common.api.AppVersion currentVersion) --> java:java.lang.Object' : 'convertToJavaObject($0)',
        'TextSegmentInput.equals(Object obj) --> Boolean' : 'equals($0)',
        'TextSegmentInput.hashCode() --> Integer' : 'hashCode()$0',
        'TextSegmentInput.toString() --> String' : 'toString()$0'
    },
    'Time' : {
        'Time.addError(APEX_OBJECT msg) --> void' : 'addError($0)',
        'Time.addError(APEX_OBJECT msg, Boolean escape) --> void' : 'addError($0)',
        'Time.addError(String msg) --> void' : 'addError($0)',
        'Time.addError(String msg, Boolean escape) --> void' : 'addError($0)',
        'Time.addHours(Integer hours) --> Time' : 'addHours($0)',
        'Time.addMilliseconds(Integer milliseconds) --> Time' : 'addMilliseconds($0)',
        'Time.addMinutes(Integer minutes) --> Time' : 'addMinutes($0)',
        'Time.addSeconds(Integer seconds) --> Time' : 'addSeconds($0)',
        'Time.hour() --> Integer' : 'hour()$0',
        'Time.millisecond() --> Integer' : 'millisecond()$0',
        'Time.minute() --> Integer' : 'minute()$0',
        'Time.newInstance(Integer hour, Integer minute, Integer second, Integer millisecond) --> Time' : 'newInstance($0)',
        'Time.second() --> Integer' : 'second()$0'
    },
    'TimeZone' : {
        'TimeZone.getDisplayName() --> String' : 'getDisplayName()$0',
        'TimeZone.getID() --> String' : 'getID()$0',
        'TimeZone.getOffset(Datetime dt) --> Integer' : 'getOffset($0)',
        'TimeZone.getTimeZone(String id) --> system.TimeZone' : 'getTimeZone($0)',
        'TimeZone.toString() --> String' : 'toString()$0'
    },
    'TouchHandledException' : {
        'TouchHandledException.getCause() --> Exception' : 'getCause()$0',
        'TouchHandledException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'TouchHandledException.getMessage() --> String' : 'getMessage()$0',
        'TouchHandledException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'TouchHandledException.getTypeName() --> String' : 'getTypeName()$0',
        'TouchHandledException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'TouchHandledException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'Type' : {
        'Type.equals(Object o) --> Boolean' : 'equals($0)',
        'Type.forName(String clsName) --> system.Type' : 'forName($0)',
        'Type.forName(String namespace, String clsName) --> system.Type' : 'forName($0)',
        'Type.getName() --> String' : 'getName()$0',
        'Type.hashcode() --> Integer' : 'hashcode()$0',
        'Type.newInstance() --> Object' : 'newInstance()$0',
        'Type.toString() --> String' : 'toString()$0'
    },
    'TypeException' : {
        'TypeException.getCause() --> Exception' : 'getCause()$0',
        'TypeException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'TypeException.getMessage() --> String' : 'getMessage()$0',
        'TypeException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'TypeException.getTypeName() --> String' : 'getTypeName()$0',
        'TypeException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'TypeException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'UnauthenticatedUser' : {
        'UnauthenticatedUser.equals(Object obj) --> Boolean' : 'equals($0)',
        'UnauthenticatedUser.hashCode() --> Integer' : 'hashCode()$0',
        'UnauthenticatedUser.toString() --> String' : 'toString()$0'
    },
    'UnexpectedException' : {
        'UnexpectedException.getCause() --> Exception' : 'getCause()$0',
        'UnexpectedException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'UnexpectedException.getMessage() --> String' : 'getMessage()$0',
        'UnexpectedException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'UnexpectedException.getTypeName() --> String' : 'getTypeName()$0',
        'UnexpectedException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'UnexpectedException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'UnsupportedOperationException' : {
        'UnsupportedOperationException.getTypeName() --> String' : 'getTypeName()$0'
    },
    'Url' : {
        'Url.getAuthority() --> String' : 'getAuthority()$0',
        'Url.getCurrentRequestUrl() --> system.Url' : 'getCurrentRequestUrl()$0',
        'Url.getDefaultPort() --> Integer' : 'getDefaultPort()$0',
        'Url.getFile() --> String' : 'getFile()$0',
        'Url.getFileFieldURL(String objectId, String fieldName) --> String' : 'getFileFieldURL($0)',
        'Url.getHost() --> String' : 'getHost()$0',
        'Url.getPath() --> String' : 'getPath()$0',
        'Url.getPort() --> Integer' : 'getPort()$0',
        'Url.getProtocol() --> String' : 'getProtocol()$0',
        'Url.getQuery() --> String' : 'getQuery()$0',
        'Url.getRef() --> String' : 'getRef()$0',
        'Url.getSalesforceBaseUrl() --> system.Url' : 'getSalesforceBaseUrl()$0',
        'Url.getUserInfo() --> String' : 'getUserInfo()$0',
        'Url.sameFile(system.Url other) --> Boolean' : 'sameFile($0)',
        'Url.toExternalForm() --> String' : 'toExternalForm()$0'
    },
    'UrlRewriter' : {
        'UrlRewriter.generateUrlFor(LIST<System.PageReference> param1) --> LIST<System.PageReference>' : 'generateUrlFor($0)',
        'UrlRewriter.mapRequestUrl(System.PageReference param1) --> System.PageReference' : 'mapRequestUrl($0)'
    },
    'User' : {
        'User.equals(Object obj) --> Boolean' : 'equals($0)',
        'User.hashCode() --> Integer' : 'hashCode()$0',
        'User.toString() --> String' : 'toString()$0'
    },
    'UserChatterSettings' : {
        'UserChatterSettings.equals(Object obj) --> Boolean' : 'equals($0)',
        'UserChatterSettings.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'UserChatterSettings.hashCode() --> Integer' : 'hashCode()$0',
        'UserChatterSettings.toString() --> String' : 'toString()$0'
    },
    'UserDetail' : {
        'UserDetail.equals(Object obj) --> Boolean' : 'equals($0)',
        'UserDetail.hashCode() --> Integer' : 'hashCode()$0',
        'UserDetail.toString() --> String' : 'toString()$0'
    },
    'UserGroupPage' : {
        'UserGroupPage.equals(Object obj) --> Boolean' : 'equals($0)',
        'UserGroupPage.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'UserGroupPage.hashCode() --> Integer' : 'hashCode()$0',
        'UserGroupPage.toString() --> String' : 'toString()$0'
    },
    'UserInfo' : {
        'UserInfo.getDefaultCurrency() --> String' : 'getDefaultCurrency()$0',
        'UserInfo.getFirstName() --> String' : 'getFirstName()$0',
        'UserInfo.getLanguage() --> String' : 'getLanguage()$0',
        'UserInfo.getLastName() --> String' : 'getLastName()$0',
        'UserInfo.getLocale() --> String' : 'getLocale()$0',
        'UserInfo.getName() --> String' : 'getName()$0',
        'UserInfo.getOrganizationId() --> String' : 'getOrganizationId()$0',
        'UserInfo.getOrganizationName() --> String' : 'getOrganizationName()$0',
        'UserInfo.getProfileId() --> String' : 'getProfileId()$0',
        'UserInfo.getSessionId() --> String' : 'getSessionId()$0',
        'UserInfo.getTimeZone() --> system.TimeZone' : 'getTimeZone()$0',
        'UserInfo.getUiTheme() --> String' : 'getUiTheme()$0',
        'UserInfo.getUiThemeDisplayed() --> String' : 'getUiThemeDisplayed()$0',
        'UserInfo.getUserEmail() --> String' : 'getUserEmail()$0',
        'UserInfo.getUserId() --> String' : 'getUserId()$0',
        'UserInfo.getUserName() --> String' : 'getUserName()$0',
        'UserInfo.getUserRoleId() --> String' : 'getUserRoleId()$0',
        'UserInfo.getUserType() --> String' : 'getUserType()$0',
        'UserInfo.isCurrentUserLicensed(String namespacePrefix) --> Boolean' : 'isCurrentUserLicensed($0)',
        'UserInfo.isMultiCurrencyOrganization() --> Boolean' : 'isMultiCurrencyOrganization()$0'
    },
    'UserPage' : {
        'UserPage.equals(Object obj) --> Boolean' : 'equals($0)',
        'UserPage.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'UserPage.hashCode() --> Integer' : 'hashCode()$0',
        'UserPage.toString() --> String' : 'toString()$0'
    },
    'UserSettings' : {
        'UserSettings.equals(Object obj) --> Boolean' : 'equals($0)',
        'UserSettings.getBuildVersion() --> Double' : 'getBuildVersion()$0',
        'UserSettings.hashCode() --> Integer' : 'hashCode()$0',
        'UserSettings.toString() --> String' : 'toString()$0'
    },
    'UserSummary' : {
        'UserSummary.equals(Object obj) --> Boolean' : 'equals($0)',
        'UserSummary.hashCode() --> Integer' : 'hashCode()$0',
        'UserSummary.toString() --> String' : 'toString()$0'
    },
    'UserType' : {
        'UserType.values() --> LIST<ConnectApi.UserType>' : 'values()$0'
    },
    'Version' : {
        'Version.compareTo(system.Version other) --> Integer' : 'compareTo($0)',
        'Version.major() --> Integer' : 'major()$0',
        'Version.minor() --> Integer' : 'minor()$0',
        'Version.patch() --> Integer' : 'patch()$0'
    },
    'VisualforceException' : {
        'VisualforceException.getCause() --> Exception' : 'getCause()$0',
        'VisualforceException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'VisualforceException.getMessage() --> String' : 'getMessage()$0',
        'VisualforceException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'VisualforceException.getTypeName() --> String' : 'getTypeName()$0',
        'VisualforceException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'VisualforceException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'WebServiceMock' : {
        'WebServiceMock.doInvoke(Object param1, Object param2, MAP<String,ANY> param3, String param4, String param5, String param6, String param7, String param8, String param9) --> void' : 'doInvoke($0)'
    },
    'WorkflowProcessStatus' : {
        'WorkflowProcessStatus.values() --> LIST<ConnectApi.WorkflowProcessStatus>' : 'values()$0'
    },
    'XmlException' : {
        'XmlException.getCause() --> Exception' : 'getCause()$0',
        'XmlException.getLineNumber() --> Integer' : 'getLineNumber()$0',
        'XmlException.getMessage() --> String' : 'getMessage()$0',
        'XmlException.getStackTraceString() --> String' : 'getStackTraceString()$0',
        'XmlException.getTypeName() --> String' : 'getTypeName()$0',
        'XmlException.initCause(APEX_OBJECT cause) --> void' : 'initCause($0)',
        'XmlException.setMessage(String message) --> void' : 'setMessage($0)'
    },
    'XmlNode' : {
        'XmlNode.addChildElement(String name, String namespace, String prefix) --> dom.XmlNode' : 'addChildElement($0)',
        'XmlNode.addCommentNode(String text) --> dom.XmlNode' : 'addCommentNode($0)',
        'XmlNode.addTextNode(String text) --> dom.XmlNode' : 'addTextNode($0)',
        'XmlNode.getAttribute(String key, String keyNamespace) --> String' : 'getAttribute($0)',
        'XmlNode.getAttributeCount() --> Integer' : 'getAttributeCount()$0',
        'XmlNode.getAttributeKeyAt(Integer index) --> String' : 'getAttributeKeyAt($0)',
        'XmlNode.getAttributeKeyNsAt(Integer index) --> String' : 'getAttributeKeyNsAt($0)',
        'XmlNode.getAttributeValue(String key, String keyNamespace) --> String' : 'getAttributeValue($0)',
        'XmlNode.getAttributeValueNs(String key, String keyNamespace) --> String' : 'getAttributeValueNs($0)',
        'XmlNode.getChildElement(String name, String namespace) --> dom.XmlNode' : 'getChildElement($0)',
        'XmlNode.getChildElements() --> LIST<dom.XmlNode>' : 'getChildElements()$0',
        'XmlNode.getChildren() --> LIST<dom.XmlNode>' : 'getChildren()$0',
        'XmlNode.getName() --> String' : 'getName()$0',
        'XmlNode.getNamespace() --> String' : 'getNamespace()$0',
        'XmlNode.getNamespaceFor(String prefix) --> String' : 'getNamespaceFor($0)',
        'XmlNode.getNodeType() --> Dom.XmlNodeType' : 'getNodeType()$0',
        'XmlNode.getParent() --> dom.XmlNode' : 'getParent()$0',
        'XmlNode.getPrefixFor(String namespace) --> String' : 'getPrefixFor($0)',
        'XmlNode.getText() --> String' : 'getText()$0',
        'XmlNode.removeAttribute(String key, String keyNamespace) --> Boolean' : 'removeAttribute($0)',
        'XmlNode.removeChild(ANY child) --> Boolean' : 'removeChild($0)',
        'XmlNode.setAttribute(String key, String value) --> void' : 'setAttribute($0)',
        'XmlNode.setAttributeNs(String key, String value, String keyNamespace, String valueNamespace) --> void' : 'setAttributeNs($0)',
        'XmlNode.setNamespace(String prefix, String namespace) --> void' : 'setNamespace($0)'
    },
    'XmlNodeType' : {
        'XmlNodeType.values() --> LIST<Dom.XmlNodeType>' : 'values()$0'
    },
    'XmlStreamReader' : {
        'XmlStreamReader.getAttributeCount() --> Integer' : 'getAttributeCount()$0',
        'XmlStreamReader.getAttributeLocalName(Integer index) --> String' : 'getAttributeLocalName($0)',
        'XmlStreamReader.getAttributeNamespace(Integer index) --> String' : 'getAttributeNamespace($0)',
        'XmlStreamReader.getAttributePrefix(Integer index) --> String' : 'getAttributePrefix($0)',
        'XmlStreamReader.getAttributeType(Integer index) --> String' : 'getAttributeType($0)',
        'XmlStreamReader.getAttributeValue(String namespaceURI, String localName) --> String' : 'getAttributeValue($0)',
        'XmlStreamReader.getAttributeValueAt(Integer index) --> String' : 'getAttributeValueAt($0)',
        'XmlStreamReader.getEventType() --> system.XmlTag' : 'getEventType()$0',
        'XmlStreamReader.getLocalName() --> String' : 'getLocalName()$0',
        'XmlStreamReader.getLocation() --> String' : 'getLocation()$0',
        'XmlStreamReader.getNamespace() --> String' : 'getNamespace()$0',
        'XmlStreamReader.getNamespaceCount() --> Integer' : 'getNamespaceCount()$0',
        'XmlStreamReader.getNamespacePrefix(Integer index) --> String' : 'getNamespacePrefix($0)',
        'XmlStreamReader.getNamespaceURI(String prefix) --> String' : 'getNamespaceURI($0)',
        'XmlStreamReader.getNamespaceURIAt(Integer index) --> String' : 'getNamespaceURIAt($0)',
        'XmlStreamReader.getPIData() --> String' : 'getPIData()$0',
        'XmlStreamReader.getPITarget() --> String' : 'getPITarget()$0',
        'XmlStreamReader.getPrefix() --> String' : 'getPrefix()$0',
        'XmlStreamReader.getText() --> String' : 'getText()$0',
        'XmlStreamReader.getVersion() --> String' : 'getVersion()$0',
        'XmlStreamReader.hasName() --> Boolean' : 'hasName()$0',
        'XmlStreamReader.hasNext() --> Boolean' : 'hasNext()$0',
        'XmlStreamReader.hasText() --> Boolean' : 'hasText()$0',
        'XmlStreamReader.isCharacters() --> Boolean' : 'isCharacters()$0',
        'XmlStreamReader.isEndElement() --> Boolean' : 'isEndElement()$0',
        'XmlStreamReader.isStartElement() --> Boolean' : 'isStartElement()$0',
        'XmlStreamReader.isWhitespace() --> Boolean' : 'isWhitespace()$0',
        'XmlStreamReader.next() --> Integer' : 'next()$0',
        'XmlStreamReader.nextTag() --> Integer' : 'nextTag()$0',
        'XmlStreamReader.setCoalescing(Boolean flag) --> void' : 'setCoalescing($0)',
        'XmlStreamReader.setNamespaceAware(Boolean flag) --> void' : 'setNamespaceAware($0)',
        'XmlStreamReader.toString() --> String' : 'toString()$0'
    },
    'XmlStreamWriter' : {
        'XmlStreamWriter.close() --> void' : 'close()$0',
        'XmlStreamWriter.getXmlString() --> String' : 'getXmlString()$0',
        'XmlStreamWriter.setDefaultNamespace(String uri) --> void' : 'setDefaultNamespace($0)',
        'XmlStreamWriter.writeAttribute(String prefix, String namespaceURI, String localName, String value) --> void' : 'writeAttribute($0)',
        'XmlStreamWriter.writeCData(String data) --> void' : 'writeCData($0)',
        'XmlStreamWriter.writeCharacters(String text) --> void' : 'writeCharacters($0)',
        'XmlStreamWriter.writeComment(String data) --> void' : 'writeComment($0)',
        'XmlStreamWriter.writeDefaultNamespace(String namesapceURI) --> void' : 'writeDefaultNamespace($0)',
        'XmlStreamWriter.writeEmptyElement(String prefix, String localName, String namesapceURI) --> void' : 'writeEmptyElement($0)',
        'XmlStreamWriter.writeEndDocument() --> void' : 'writeEndDocument()$0',
        'XmlStreamWriter.writeEndElement() --> void' : 'writeEndElement()$0',
        'XmlStreamWriter.writeNamespace(String prefix, String namesapceURI) --> void' : 'writeNamespace($0)',
        'XmlStreamWriter.writeProcessingInstruction(String target, String data) --> void' : 'writeProcessingInstruction($0)',
        'XmlStreamWriter.writeStartDocument(String encoding, String version) --> void' : 'writeStartDocument($0)',
        'XmlStreamWriter.writeStartElement(String prefix, String localName, String namesapceURI) --> void' : 'writeStartElement($0)'
    },
    'XmlTag' : {
        'XmlTag.values() --> LIST<system.XmlTag>' : 'values()$0'
    }
}