apex_completions = {
    'AbstractMessageBody' : {
        'AbstractMessageBody.equals(Object obj)\tBoolean' : 'equals($0)',
        'AbstractMessageBody.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'AbstractMessageBody.hashCode()\tInteger' : 'hashCode()$0',
        'AbstractMessageBody.toString()\tString' : 'toString()$0'
    },
    'Action' : {
        'Action.getExpression()\tString' : 'getExpression()$0',
        'Action.invoke()\tSystem.PageReference' : 'invoke()$0'
    },
    'Actor' : {
        'Actor.equals(Object obj)\tBoolean' : 'equals($0)',
        'Actor.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'Actor.hashCode()\tInteger' : 'hashCode()$0',
        'Actor.toString()\tString' : 'toString()$0'
    },
    'ActorWithId' : {
        'ActorWithId.equals(Object obj)\tBoolean' : 'equals($0)',
        'ActorWithId.hashCode()\tInteger' : 'hashCode()$0',
        'ActorWithId.toString()\tString' : 'toString()$0'
    },
    'Address' : {
        'Address.equals(Object obj)\tBoolean' : 'equals($0)',
        'Address.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'Address.hashCode()\tInteger' : 'hashCode()$0',
        'Address.toString()\tString' : 'toString()$0'
    },
    'Answers' : {
        'Answers.findSimilar(SObject question)\tLIST<Id>' : 'findSimilar($0)',
        'Answers.setBestReply(String questionId, String bestReplyId)\tvoid' : 'setBestReply($0)'
    },
    'ApexPages' : {
        'ApexPages.addMessage(ApexPages.Message message)\tvoid' : 'addMessage($0)',
        'ApexPages.addMessages(APEX_OBJECT ex)\tvoid' : 'addMessages($0)',
        'ApexPages.currentPage()\tSystem.PageReference' : 'currentPage()$0',
        'ApexPages.getMessages()\tLIST<ApexPages.Message>' : 'getMessages()$0',
        'ApexPages.hasMessages()\tBoolean' : 'hasMessages()$0',
        'ApexPages.hasMessages(ApexPages.Severity severity)\tBoolean' : 'hasMessages($0)'
    },
    'AppExchange' : {
        'AppExchange.calculateListingPopularity(String testUserName, String testCronString)\tvoid' : 'calculateListingPopularity($0)',
        'AppExchange.createOrg(String firstName, String lastName, String companyName, String email, String language, String adminUserName, String packageId, String evalUserName, Boolean isExtension)\tString' : 'createOrg($0)',
        'AppExchange.createPortalUser(SObject user, String accountId)\tId' : 'createPortalUser($0)',
        'AppExchange.createSession(String appExchangeOrgId, String portalId, String siteId, String portalUserId)\tString' : 'createSession($0)',
        'AppExchange.debug(String message)\tvoid' : 'debug($0)',
        'AppExchange.getAuthenticatingUrl(String page)\tString' : 'getAuthenticatingUrl($0)',
        'AppExchange.getConfig(String section, String key)\tString' : 'getConfig($0)',
        'AppExchange.getCookie(String name)\tString' : 'getCookie($0)',
        'AppExchange.getCrossInstanceEncryptedHash(Double appVersion, String value)\tString' : 'getCrossInstanceEncryptedHash($0)',
        'AppExchange.getInstalledPackageVersions(String orgId)\tLIST<String>' : 'getInstalledPackageVersions($0)',
        'AppExchange.getOrgName(String orgId)\tString' : 'getOrgName($0)',
        'AppExchange.getPackageManifest(String pkgVersionId)\tString' : 'getPackageManifest($0)',
        'AppExchange.getPortalAdminId()\tString' : 'getPortalAdminId()$0',
        'AppExchange.getPortalId()\tString' : 'getPortalId()$0',
        'AppExchange.getSiteId()\tString' : 'getSiteId()$0',
        'AppExchange.getTrialTemplates(String callerOrgId, String lmPkgId, String username)\tLIST<TrialTemplate>' : 'getTrialTemplates($0)',
        'AppExchange.isDuplicateUserName(String username)\tBoolean' : 'isDuplicateUserName($0)',
        'AppExchange.isGuestUser()\tBoolean' : 'isGuestUser()$0',
        'AppExchange.movedPermanently(String location)\tvoid' : 'movedPermanently($0)',
        'AppExchange.provisionPackageLicense(String orgId, String allPackageId, Integer numLicenses, Date expirationDate, String status)\tString' : 'provisionPackageLicense($0)',
        'AppExchange.registerPackageVersion(String pkgVersionId)\tBoolean' : 'registerPackageVersion($0)',
        'AppExchange.setCookie(String name, String value)\tvoid' : 'setCookie($0)',
        'AppExchange.setCookie(String name, String value, String cookieDomainName, Integer cookieAge)\tvoid' : 'setCookie($0)',
        'AppExchange.setDefaultLicenseTerms(String pkgVersionId, String orgId, String defaultLicenseStatus, Integer defaultLicenseLength, Integer defaultLicenseSeats)\tvoid' : 'setDefaultLicenseTerms($0)',
        'AppExchange.setHttpResponseStatus(Integer statusCode)\tvoid' : 'setHttpResponseStatus($0)',
        'AppExchange.setLicenseManagementOrganization(String pkgVersionId, String orgId, String username, String password)\tString' : 'setLicenseManagementOrganization($0)',
        'AppExchange.stopListingPopularityJob()\tvoid' : 'stopListingPopularityJob()$0',
        'AppExchange.to15(String id)\tString' : 'to15($0)',
        'AppExchange.to18(String id)\tString' : 'to18($0)',
        'AppExchange.updateSingleAsAdmin(SObject sobj)\tDatabase.SaveResult' : 'updateSingleAsAdmin($0)',
        'AppExchange.validateLMAInstalled(String username, String password)\tString' : 'validateLMAInstalled($0)',
        'AppExchange.validateOrgUser(String username, String password)\tString' : 'validateOrgUser($0)'
    },
    'ApplicationReadWriteMode' : {
        'ApplicationReadWriteMode.values()\tLIST<system.ApplicationReadWriteMode>' : 'values()$0'
    },
    'ApprovalAttachment' : {
        'ApprovalAttachment.equals(Object obj)\tBoolean' : 'equals($0)',
        'ApprovalAttachment.hashCode()\tInteger' : 'hashCode()$0',
        'ApprovalAttachment.toString()\tString' : 'toString()$0'
    },
    'ApprovalPostTemplateField' : {
        'ApprovalPostTemplateField.equals(Object obj)\tBoolean' : 'equals($0)',
        'ApprovalPostTemplateField.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'ApprovalPostTemplateField.hashCode()\tInteger' : 'hashCode()$0',
        'ApprovalPostTemplateField.toString()\tString' : 'toString()$0'
    },
    'AssertException' : {
        'AssertException.getCause()\tException' : 'getCause()$0',
        'AssertException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'AssertException.getMessage()\tString' : 'getMessage()$0',
        'AssertException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'AssertException.getTypeName()\tString' : 'getTypeName()$0',
        'AssertException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'AssertException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'AssignmentRuleHeader' : {},
    'AsyncException' : {
        'AsyncException.getCause()\tException' : 'getCause()$0',
        'AsyncException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'AsyncException.getMessage()\tString' : 'getMessage()$0',
        'AsyncException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'AsyncException.getTypeName()\tString' : 'getTypeName()$0',
        'AsyncException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'AsyncException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'BasicTemplateAttachment' : {
        'BasicTemplateAttachment.equals(Object obj)\tBoolean' : 'equals($0)',
        'BasicTemplateAttachment.hashCode()\tInteger' : 'hashCode()$0',
        'BasicTemplateAttachment.toString()\tString' : 'toString()$0'
    },
    'Batchable' : {
        'Batchable.execute(Database.BatchableContext param1, LIST<ANY> param2)\tvoid' : 'execute($0)',
        'Batchable.finish(Database.BatchableContext param1)\tvoid' : 'finish($0)',
        'Batchable.start(Database.BatchableContext param1)\tsystem.Iterable' : 'start($0)'
    },
    'BatchableContext' : {
        'BatchableContext.getChildJobId()\tId' : 'getChildJobId()$0',
        'BatchableContext.getJobId()\tId' : 'getJobId()$0'
    },
    'BatchableContextImpl' : {
        'BatchableContextImpl.getChildJobId()\tId' : 'getChildJobId()$0',
        'BatchableContextImpl.getJobId()\tId' : 'getJobId()$0'
    },
    'BinaryAttachment' : {},
    'BinaryInput' : {
        'BinaryInput.getBlobValue()\tBlob' : 'getBlobValue()$0',
        'BinaryInput.getContentType()\tString' : 'getContentType()$0',
        'BinaryInput.getFilename()\tString' : 'getFilename()$0',
        'BinaryInput.toString()\tString' : 'toString()$0'
    },
    'Blob' : {
        'Blob.size()\tInteger' : 'size()$0',
        'Blob.toPdf(String o)\tBlob' : 'toPdf($0)',
        'Blob.toString()\tString' : 'toString()$0',
        'Blob.valueOf(String o)\tBlob' : 'valueOf($0)'
    },
    'Boolean' : {
        'Boolean.addError(APEX_OBJECT msg)\tvoid' : 'addError($0)',
        'Boolean.addError(APEX_OBJECT msg, Boolean escape)\tvoid' : 'addError($0)',
        'Boolean.addError(String msg)\tvoid' : 'addError($0)',
        'Boolean.addError(String msg, Boolean escape)\tvoid' : 'addError($0)',
        'Boolean.valueOf(Object a)\tBoolean' : 'valueOf($0)'
    },
    'BusinessHours' : {
        'BusinessHours.add(Id businessHoursId, Datetime startDate, Long interval)\tDatetime' : 'add($0)',
        'BusinessHours.addGmt(Id businessHoursId, Datetime startDate, Long interval)\tDatetime' : 'addGmt($0)',
        'BusinessHours.diff(String businessHoursId, Datetime startDate, Datetime endDate)\tLong' : 'diff($0)'
    },
    'CURRENCY' : {
        'CURRENCY.format()\tString' : 'format()$0',
        'CURRENCY.formatAmount()\tString' : 'formatAmount()$0',
        'CURRENCY.newInstance(Decimal amount, String isoCode)\tCURRENCY' : 'newInstance($0)'
    },
    'CalloutException' : {
        'CalloutException.getCause()\tException' : 'getCause()$0',
        'CalloutException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'CalloutException.getMessage()\tString' : 'getMessage()$0',
        'CalloutException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'CalloutException.getTypeName()\tString' : 'getTypeName()$0',
        'CalloutException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'CalloutException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'CaseActorType' : {
        'CaseActorType.values()\tLIST<ConnectApi.CaseActorType>' : 'values()$0'
    },
    'CaseComment' : {
        'CaseComment.equals(Object obj)\tBoolean' : 'equals($0)',
        'CaseComment.hashCode()\tInteger' : 'hashCode()$0',
        'CaseComment.toString()\tString' : 'toString()$0'
    },
    'Cases' : {
        'Cases.getCaseIdFromEmailThreadId(String emailThreadId)\tId' : 'getCaseIdFromEmailThreadId($0)'
    },
    'Chatter' : {
        'Chatter.deleteSubscription(String communityId, String subscriptionId)\tvoid' : 'deleteSubscription($0)',
        'Chatter.getFollowers(String communityId, String recordId)\tConnectApi.FollowerPage' : 'getFollowers($0)',
        'Chatter.getFollowers(String communityId, String recordId, Integer pageParam, Integer pageSize)\tConnectApi.FollowerPage' : 'getFollowers($0)',
        'Chatter.getSubscription(String communityId, String subscriptionId)\tConnectApi.Subscription' : 'getSubscription($0)'
    },
    'ChatterActivity' : {
        'ChatterActivity.equals(Object obj)\tBoolean' : 'equals($0)',
        'ChatterActivity.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'ChatterActivity.hashCode()\tInteger' : 'hashCode()$0',
        'ChatterActivity.toString()\tString' : 'toString()$0'
    },
    'ChatterFavorites' : {
        'ChatterFavorites.addFavorite(String communityId, String subjectId, String searchText)\tConnectApi.FeedFavorite' : 'addFavorite($0)',
        'ChatterFavorites.addRecordFavorite(String communityId, String subjectId, String targetId)\tConnectApi.FeedFavorite' : 'addRecordFavorite($0)',
        'ChatterFavorites.deleteFavorite(String communityId, String subjectId, String favoriteId)\tvoid' : 'deleteFavorite($0)',
        'ChatterFavorites.getFavorite(String communityId, String subjectId, String favoriteId)\tConnectApi.FeedFavorite' : 'getFavorite($0)',
        'ChatterFavorites.getFavorites(String communityId, String subjectId)\tConnectApi.FeedFavorites' : 'getFavorites($0)',
        'ChatterFavorites.getFeedItems(String communityId, String subjectId, String favoriteId)\tConnectApi.FeedItemPage' : 'getFeedItems($0)',
        'ChatterFavorites.getFeedItems(String communityId, String subjectId, String favoriteId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)\tConnectApi.FeedItemPage' : 'getFeedItems($0)',
        'ChatterFavorites.setTestGetFeedItems(String communityId, String subjectId, String favoriteId, ConnectApi.FeedItemPage result)\tvoid' : 'setTestGetFeedItems($0)',
        'ChatterFavorites.setTestGetFeedItems(String communityId, String subjectId, String favoriteId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)\tvoid' : 'setTestGetFeedItems($0)',
        'ChatterFavorites.updateFavorite(String communityId, String subjectId, String favoriteId, Boolean updateLastViewDate)\tConnectApi.FeedFavorite' : 'updateFavorite($0)'
    },
    'ChatterFeeds' : {
        'ChatterFeeds.deleteComment(String communityId, String commentId)\tvoid' : 'deleteComment($0)',
        'ChatterFeeds.deleteFeedItem(String communityId, String feedItemId)\tvoid' : 'deleteFeedItem($0)',
        'ChatterFeeds.deleteLike(String communityId, String likeId)\tvoid' : 'deleteLike($0)',
        'ChatterFeeds.getComment(String communityId, String commentId)\tConnectApi.Comment' : 'getComment($0)',
        'ChatterFeeds.getCommentsForFeedItem(String communityId, String feedItemId)\tConnectApi.CommentPage' : 'getCommentsForFeedItem($0)',
        'ChatterFeeds.getCommentsForFeedItem(String communityId, String feedItemId, String pageParam, Integer pageSize)\tConnectApi.CommentPage' : 'getCommentsForFeedItem($0)',
        'ChatterFeeds.getFeed(String communityId, ConnectApi.FeedType feedType)\tConnectApi.Feed' : 'getFeed($0)',
        'ChatterFeeds.getFeed(String communityId, ConnectApi.FeedType feedType, ConnectApi.FeedSortOrder sortParam)\tConnectApi.Feed' : 'getFeed($0)',
        'ChatterFeeds.getFeed(String communityId, ConnectApi.FeedType feedType, String subjectId)\tConnectApi.Feed' : 'getFeed($0)',
        'ChatterFeeds.getFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, ConnectApi.FeedSortOrder sortParam)\tConnectApi.Feed' : 'getFeed($0)',
        'ChatterFeeds.getFeedItem(String communityId, String feedItemId)\tConnectApi.FeedItem' : 'getFeedItem($0)',
        'ChatterFeeds.getFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType)\tConnectApi.FeedItemPage' : 'getFeedItemsFromFeed($0)',
        'ChatterFeeds.getFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)\tConnectApi.FeedItemPage' : 'getFeedItemsFromFeed($0)',
        'ChatterFeeds.getFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String subjectId)\tConnectApi.FeedItemPage' : 'getFeedItemsFromFeed($0)',
        'ChatterFeeds.getFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)\tConnectApi.FeedItemPage' : 'getFeedItemsFromFeed($0)',
        'ChatterFeeds.getFeedItemsFromFilterFeed(String communityId, String subjectId, String keyPrefix)\tConnectApi.FeedItemPage' : 'getFeedItemsFromFilterFeed($0)',
        'ChatterFeeds.getFeedItemsFromFilterFeed(String communityId, String subjectId, String keyPrefix, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)\tConnectApi.FeedItemPage' : 'getFeedItemsFromFilterFeed($0)',
        'ChatterFeeds.getFeedPoll(String communityId, String feedItemId)\tConnectApi.FeedPoll' : 'getFeedPoll($0)',
        'ChatterFeeds.getFilterFeed(String communityId, String subjectId, String keyPrefix)\tConnectApi.Feed' : 'getFilterFeed($0)',
        'ChatterFeeds.getFilterFeed(String communityId, String subjectId, String keyPrefix, ConnectApi.FeedSortOrder sortParam)\tConnectApi.Feed' : 'getFilterFeed($0)',
        'ChatterFeeds.getLike(String communityId, String likeId)\tConnectApi.ChatterLike' : 'getLike($0)',
        'ChatterFeeds.getLikesForComment(String communityId, String commentId)\tConnectApi.ChatterLikePage' : 'getLikesForComment($0)',
        'ChatterFeeds.getLikesForComment(String communityId, String commentId, Integer pageParam, Integer pageSize)\tConnectApi.ChatterLikePage' : 'getLikesForComment($0)',
        'ChatterFeeds.getLikesForFeedItem(String communityId, String feedItemId)\tConnectApi.ChatterLikePage' : 'getLikesForFeedItem($0)',
        'ChatterFeeds.getLikesForFeedItem(String communityId, String feedItemId, Integer pageParam, Integer pageSize)\tConnectApi.ChatterLikePage' : 'getLikesForFeedItem($0)',
        'ChatterFeeds.isModified(String communityId, ConnectApi.FeedType feedType, String subjectId, String since)\tConnectApi.FeedModifiedInfo' : 'isModified($0)',
        'ChatterFeeds.likeComment(String communityId, String commentId)\tConnectApi.ChatterLike' : 'likeComment($0)',
        'ChatterFeeds.likeFeedItem(String communityId, String feedItemId)\tConnectApi.ChatterLike' : 'likeFeedItem($0)',
        'ChatterFeeds.postComment(String communityId, String feedItemId, ConnectApi.CommentInput comment, ConnectApi.BinaryInput feedItemFileUpload)\tConnectApi.Comment' : 'postComment($0)',
        'ChatterFeeds.postComment(String communityId, String feedItemId, String text)\tConnectApi.Comment' : 'postComment($0)',
        'ChatterFeeds.postFeedItem(String communityId, ConnectApi.FeedType feedType, String subjectId, ConnectApi.FeedItemInput feedItem, ConnectApi.BinaryInput feedItemFileUpload)\tConnectApi.FeedItem' : 'postFeedItem($0)',
        'ChatterFeeds.postFeedItem(String communityId, ConnectApi.FeedType feedType, String subjectId, String text)\tConnectApi.FeedItem' : 'postFeedItem($0)',
        'ChatterFeeds.searchFeedItems(String communityId, String q)\tConnectApi.FeedItemPage' : 'searchFeedItems($0)',
        'ChatterFeeds.searchFeedItems(String communityId, String q, ConnectApi.FeedSortOrder sortParam)\tConnectApi.FeedItemPage' : 'searchFeedItems($0)',
        'ChatterFeeds.searchFeedItems(String communityId, String q, String pageParam, Integer pageSize)\tConnectApi.FeedItemPage' : 'searchFeedItems($0)',
        'ChatterFeeds.searchFeedItems(String communityId, String q, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam)\tConnectApi.FeedItemPage' : 'searchFeedItems($0)',
        'ChatterFeeds.searchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q)\tConnectApi.FeedItemPage' : 'searchFeedItemsInFeed($0)',
        'ChatterFeeds.searchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String q)\tConnectApi.FeedItemPage' : 'searchFeedItemsInFeed($0)',
        'ChatterFeeds.searchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q)\tConnectApi.FeedItemPage' : 'searchFeedItemsInFeed($0)',
        'ChatterFeeds.searchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String q)\tConnectApi.FeedItemPage' : 'searchFeedItemsInFeed($0)',
        'ChatterFeeds.searchFeedItemsInFilterFeed(String communityId, String subjectId, String keyPrefix, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q)\tConnectApi.FeedItemPage' : 'searchFeedItemsInFilterFeed($0)',
        'ChatterFeeds.searchFeedItemsInFilterFeed(String communityId, String subjectId, String keyPrefix, String q)\tConnectApi.FeedItemPage' : 'searchFeedItemsInFilterFeed($0)',
        'ChatterFeeds.setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, ConnectApi.FeedItemPage result)\tvoid' : 'setTestGetFeedItemsFromFeed($0)',
        'ChatterFeeds.setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)\tvoid' : 'setTestGetFeedItemsFromFeed($0)',
        'ChatterFeeds.setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, ConnectApi.FeedItemPage result)\tvoid' : 'setTestGetFeedItemsFromFeed($0)',
        'ChatterFeeds.setTestGetFeedItemsFromFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)\tvoid' : 'setTestGetFeedItemsFromFeed($0)',
        'ChatterFeeds.setTestGetFeedItemsFromFilterFeed(String communityId, String subjectId, String keyPrefix, ConnectApi.FeedItemPage result)\tvoid' : 'setTestGetFeedItemsFromFilterFeed($0)',
        'ChatterFeeds.setTestGetFeedItemsFromFilterFeed(String communityId, String subjectId, String keyPrefix, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)\tvoid' : 'setTestGetFeedItemsFromFilterFeed($0)',
        'ChatterFeeds.setTestSearchFeedItems(String communityId, String q, ConnectApi.FeedItemPage result)\tvoid' : 'setTestSearchFeedItems($0)',
        'ChatterFeeds.setTestSearchFeedItems(String communityId, String q, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)\tvoid' : 'setTestSearchFeedItems($0)',
        'ChatterFeeds.setTestSearchFeedItems(String communityId, String q, String pageParam, Integer pageSize, ConnectApi.FeedItemPage result)\tvoid' : 'setTestSearchFeedItems($0)',
        'ChatterFeeds.setTestSearchFeedItems(String communityId, String q, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, ConnectApi.FeedItemPage result)\tvoid' : 'setTestSearchFeedItems($0)',
        'ChatterFeeds.setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedItemPage result)\tvoid' : 'setTestSearchFeedItemsInFeed($0)',
        'ChatterFeeds.setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String q, ConnectApi.FeedItemPage result)\tvoid' : 'setTestSearchFeedItemsInFeed($0)',
        'ChatterFeeds.setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedItemPage result)\tvoid' : 'setTestSearchFeedItemsInFeed($0)',
        'ChatterFeeds.setTestSearchFeedItemsInFeed(String communityId, ConnectApi.FeedType feedType, String subjectId, String q, ConnectApi.FeedItemPage result)\tvoid' : 'setTestSearchFeedItemsInFeed($0)',
        'ChatterFeeds.setTestSearchFeedItemsInFilterFeed(String communityId, String subjectId, String keyPrefix, String pageParam, Integer pageSize, ConnectApi.FeedSortOrder sortParam, String q, ConnectApi.FeedItemPage result)\tvoid' : 'setTestSearchFeedItemsInFilterFeed($0)',
        'ChatterFeeds.setTestSearchFeedItemsInFilterFeed(String communityId, String subjectId, String keyPrefix, String q, ConnectApi.FeedItemPage result)\tvoid' : 'setTestSearchFeedItemsInFilterFeed($0)',
        'ChatterFeeds.shareFeedItem(String communityId, ConnectApi.FeedType feedType, String subjectId, String originalFeedItemId)\tConnectApi.FeedItem' : 'shareFeedItem($0)',
        'ChatterFeeds.updateBookmark(String communityId, String feedItemId, Boolean isBookmarkedByCurrentUser)\tConnectApi.FeedItem' : 'updateBookmark($0)',
        'ChatterFeeds.voteOnFeedPoll(String communityId, String feedItemId, String myChoiceId)\tConnectApi.FeedPoll' : 'voteOnFeedPoll($0)'
    },
    'ChatterGroup' : {
        'ChatterGroup.equals(Object obj)\tBoolean' : 'equals($0)',
        'ChatterGroup.hashCode()\tInteger' : 'hashCode()$0',
        'ChatterGroup.toString()\tString' : 'toString()$0'
    },
    'ChatterGroupDetail' : {
        'ChatterGroupDetail.equals(Object obj)\tBoolean' : 'equals($0)',
        'ChatterGroupDetail.hashCode()\tInteger' : 'hashCode()$0',
        'ChatterGroupDetail.toString()\tString' : 'toString()$0'
    },
    'ChatterGroupInput' : {
        'ChatterGroupInput.convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object' : 'convertToJavaObject($0)',
        'ChatterGroupInput.equals(Object obj)\tBoolean' : 'equals($0)',
        'ChatterGroupInput.hashCode()\tInteger' : 'hashCode()$0',
        'ChatterGroupInput.toString()\tString' : 'toString()$0'
    },
    'ChatterGroupPage' : {
        'ChatterGroupPage.equals(Object obj)\tBoolean' : 'equals($0)',
        'ChatterGroupPage.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'ChatterGroupPage.hashCode()\tInteger' : 'hashCode()$0',
        'ChatterGroupPage.toString()\tString' : 'toString()$0'
    },
    'ChatterGroupSummary' : {
        'ChatterGroupSummary.equals(Object obj)\tBoolean' : 'equals($0)',
        'ChatterGroupSummary.hashCode()\tInteger' : 'hashCode()$0',
        'ChatterGroupSummary.toString()\tString' : 'toString()$0'
    },
    'ChatterGroups' : {
        'ChatterGroups.addMember(String communityId, String groupId, String userId)\tConnectApi.GroupMember' : 'addMember($0)',
        'ChatterGroups.deleteMember(String communityId, String membershipId)\tvoid' : 'deleteMember($0)',
        'ChatterGroups.deletePhoto(String communityId, String groupId)\tvoid' : 'deletePhoto($0)',
        'ChatterGroups.follow(String communityId, String groupId, String subjectId)\tConnectApi.Subscription' : 'follow($0)',
        'ChatterGroups.getFollowings(String communityId, String groupId)\tConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterGroups.getFollowings(String communityId, String groupId, Integer pageParam)\tConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterGroups.getFollowings(String communityId, String groupId, Integer pageParam, Integer pageSize)\tConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterGroups.getFollowings(String communityId, String groupId, String filterType)\tConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterGroups.getFollowings(String communityId, String groupId, String filterType, Integer pageParam)\tConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterGroups.getFollowings(String communityId, String groupId, String filterType, Integer pageParam, Integer pageSize)\tConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterGroups.getGroup(String communityId, String groupId)\tConnectApi.ChatterGroupDetail' : 'getGroup($0)',
        'ChatterGroups.getGroupMembershipRequest(String communityId, String requestId)\tConnectApi.GroupMembershipRequest' : 'getGroupMembershipRequest($0)',
        'ChatterGroups.getGroupMembershipRequests(String communityId, String groupId)\tConnectApi.GroupMembershipRequests' : 'getGroupMembershipRequests($0)',
        'ChatterGroups.getGroupMembershipRequests(String communityId, String groupId, ConnectApi.GroupMembershipRequestStatus status)\tConnectApi.GroupMembershipRequests' : 'getGroupMembershipRequests($0)',
        'ChatterGroups.getGroups(String communityId)\tConnectApi.ChatterGroupPage' : 'getGroups($0)',
        'ChatterGroups.getGroups(String communityId, Integer pageParam, Integer pageSize)\tConnectApi.ChatterGroupPage' : 'getGroups($0)',
        'ChatterGroups.getMember(String communityId, String membershipId)\tConnectApi.GroupMember' : 'getMember($0)',
        'ChatterGroups.getMembers(String communityId, String groupId)\tConnectApi.GroupMemberPage' : 'getMembers($0)',
        'ChatterGroups.getMembers(String communityId, String groupId, Integer pageParam, Integer pageSize)\tConnectApi.GroupMemberPage' : 'getMembers($0)',
        'ChatterGroups.getMyChatterSettings(String communityId, String groupId)\tConnectApi.GroupChatterSettings' : 'getMyChatterSettings($0)',
        'ChatterGroups.getPhoto(String communityId, String groupId)\tConnectApi.Photo' : 'getPhoto($0)',
        'ChatterGroups.requestGroupMembership(String communityId, String groupId)\tConnectApi.GroupMembershipRequest' : 'requestGroupMembership($0)',
        'ChatterGroups.searchGroups(String communityId, String q)\tConnectApi.ChatterGroupPage' : 'searchGroups($0)',
        'ChatterGroups.searchGroups(String communityId, String q, Integer pageParam, Integer pageSize)\tConnectApi.ChatterGroupPage' : 'searchGroups($0)',
        'ChatterGroups.setPhoto(String communityId, String groupId, ConnectApi.BinaryInput fileUpload)\tConnectApi.Photo' : 'setPhoto($0)',
        'ChatterGroups.setPhoto(String communityId, String groupId, String fileId, Integer versionNumber)\tConnectApi.Photo' : 'setPhoto($0)',
        'ChatterGroups.setTestSearchGroups(String communityId, String q, ConnectApi.ChatterGroupPage result)\tvoid' : 'setTestSearchGroups($0)',
        'ChatterGroups.setTestSearchGroups(String communityId, String q, Integer pageParam, Integer pageSize, ConnectApi.ChatterGroupPage result)\tvoid' : 'setTestSearchGroups($0)',
        'ChatterGroups.updateGroup(String communityId, String groupId, ConnectApi.ChatterGroupInput groupInput)\tConnectApi.ChatterGroupDetail' : 'updateGroup($0)',
        'ChatterGroups.updateMyChatterSettings(String communityId, String groupId, ConnectApi.GroupEmailFrequency emailFrequency)\tConnectApi.GroupChatterSettings' : 'updateMyChatterSettings($0)',
        'ChatterGroups.updateRequestStatus(String communityId, String requestId, ConnectApi.GroupMembershipRequestStatus status)\tConnectApi.GroupMembershipRequest' : 'updateRequestStatus($0)'
    },
    'ChatterLike' : {
        'ChatterLike.equals(Object obj)\tBoolean' : 'equals($0)',
        'ChatterLike.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'ChatterLike.hashCode()\tInteger' : 'hashCode()$0',
        'ChatterLike.toString()\tString' : 'toString()$0'
    },
    'ChatterLikePage' : {
        'ChatterLikePage.equals(Object obj)\tBoolean' : 'equals($0)',
        'ChatterLikePage.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'ChatterLikePage.hashCode()\tInteger' : 'hashCode()$0',
        'ChatterLikePage.toString()\tString' : 'toString()$0'
    },
    'ChatterUsers' : {
        'ChatterUsers.deletePhoto(String communityId, String userId)\tvoid' : 'deletePhoto($0)',
        'ChatterUsers.follow(String communityId, String userId, String subjectId)\tConnectApi.Subscription' : 'follow($0)',
        'ChatterUsers.getChatterSettings(String communityId, String userId)\tConnectApi.UserChatterSettings' : 'getChatterSettings($0)',
        'ChatterUsers.getFollowers(String communityId, String userId)\tConnectApi.FollowerPage' : 'getFollowers($0)',
        'ChatterUsers.getFollowers(String communityId, String userId, Integer pageParam, Integer pageSize)\tConnectApi.FollowerPage' : 'getFollowers($0)',
        'ChatterUsers.getFollowings(String communityId, String userId)\tConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterUsers.getFollowings(String communityId, String userId, Integer pageParam)\tConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterUsers.getFollowings(String communityId, String userId, Integer pageParam, Integer pageSize)\tConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterUsers.getFollowings(String communityId, String userId, String filterType)\tConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterUsers.getFollowings(String communityId, String userId, String filterType, Integer pageParam)\tConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterUsers.getFollowings(String communityId, String userId, String filterType, Integer pageParam, Integer pageSize)\tConnectApi.FollowingPage' : 'getFollowings($0)',
        'ChatterUsers.getGroups(String communityId, String userId)\tConnectApi.UserGroupPage' : 'getGroups($0)',
        'ChatterUsers.getGroups(String communityId, String userId, Integer pageParam, Integer pageSize)\tConnectApi.UserGroupPage' : 'getGroups($0)',
        'ChatterUsers.getPhoto(String communityId, String userId)\tConnectApi.Photo' : 'getPhoto($0)',
        'ChatterUsers.getUser(String communityId, String userId)\tConnectApi.UserDetail' : 'getUser($0)',
        'ChatterUsers.getUsers(String communityId)\tConnectApi.UserPage' : 'getUsers($0)',
        'ChatterUsers.getUsers(String communityId, Integer pageParam, Integer pageSize)\tConnectApi.UserPage' : 'getUsers($0)',
        'ChatterUsers.searchUsers(String communityId, String q)\tConnectApi.UserPage' : 'searchUsers($0)',
        'ChatterUsers.searchUsers(String communityId, String q, Integer pageParam, Integer pageSize)\tConnectApi.UserPage' : 'searchUsers($0)',
        'ChatterUsers.searchUsers(String communityId, String q, String searchContextId, Integer pageParam, Integer pageSize)\tConnectApi.UserPage' : 'searchUsers($0)',
        'ChatterUsers.setPhoto(String communityId, String userId, ConnectApi.BinaryInput fileUpload)\tConnectApi.Photo' : 'setPhoto($0)',
        'ChatterUsers.setPhoto(String communityId, String userId, String fileId, Integer versionNumber)\tConnectApi.Photo' : 'setPhoto($0)',
        'ChatterUsers.setTestSearchUsers(String communityId, String q, ConnectApi.UserPage result)\tvoid' : 'setTestSearchUsers($0)',
        'ChatterUsers.setTestSearchUsers(String communityId, String q, Integer pageParam, Integer pageSize, ConnectApi.UserPage result)\tvoid' : 'setTestSearchUsers($0)',
        'ChatterUsers.setTestSearchUsers(String communityId, String q, String searchContextId, Integer pageParam, Integer pageSize, ConnectApi.UserPage result)\tvoid' : 'setTestSearchUsers($0)',
        'ChatterUsers.updateChatterSettings(String communityId, String userId, ConnectApi.GroupEmailFrequency defaultGroupEmailFrequency)\tConnectApi.UserChatterSettings' : 'updateChatterSettings($0)'
    },
    'ClientInfo' : {
        'ClientInfo.equals(Object obj)\tBoolean' : 'equals($0)',
        'ClientInfo.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'ClientInfo.hashCode()\tInteger' : 'hashCode()$0',
        'ClientInfo.toString()\tString' : 'toString()$0'
    },
    'Comment' : {
        'Comment.equals(Object obj)\tBoolean' : 'equals($0)',
        'Comment.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'Comment.hashCode()\tInteger' : 'hashCode()$0',
        'Comment.toString()\tString' : 'toString()$0'
    },
    'CommentInput' : {
        'CommentInput.convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object' : 'convertToJavaObject($0)',
        'CommentInput.equals(Object obj)\tBoolean' : 'equals($0)',
        'CommentInput.hashCode()\tInteger' : 'hashCode()$0',
        'CommentInput.toString()\tString' : 'toString()$0'
    },
    'CommentPage' : {
        'CommentPage.equals(Object obj)\tBoolean' : 'equals($0)',
        'CommentPage.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'CommentPage.hashCode()\tInteger' : 'hashCode()$0',
        'CommentPage.toString()\tString' : 'toString()$0'
    },
    'CommentType' : {
        'CommentType.values()\tLIST<ConnectApi.CommentType>' : 'values()$0'
    },
    'Communities' : {
        'Communities.getCommunities()\tConnectApi.CommunityPage' : 'getCommunities()$0',
        'Communities.getCommunities(ConnectApi.CommunityStatus status)\tConnectApi.CommunityPage' : 'getCommunities($0)',
        'Communities.getCommunity(String communityId)\tConnectApi.Community' : 'getCommunity($0)'
    },
    'Community' : {
        'Community.equals(Object obj)\tBoolean' : 'equals($0)',
        'Community.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'Community.hashCode()\tInteger' : 'hashCode()$0',
        'Community.toString()\tString' : 'toString()$0'
    },
    'CommunityPage' : {
        'CommunityPage.equals(Object obj)\tBoolean' : 'equals($0)',
        'CommunityPage.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'CommunityPage.hashCode()\tInteger' : 'hashCode()$0',
        'CommunityPage.toString()\tString' : 'toString()$0'
    },
    'CommunityStatus' : {
        'CommunityStatus.values()\tLIST<ConnectApi.CommunityStatus>' : 'values()$0'
    },
    'Comparable' : {
        'Comparable.compareTo(Object param1)\tInteger' : 'compareTo($0)'
    },
    'ComplexSegment' : {
        'ComplexSegment.equals(Object obj)\tBoolean' : 'equals($0)',
        'ComplexSegment.hashCode()\tInteger' : 'hashCode()$0',
        'ComplexSegment.toString()\tString' : 'toString()$0'
    },
    'Component' : {
        'Component.getComponentById(String id)\tApexPages.Component' : 'getComponentById($0)'
    },
    'ComponentIteration' : {
        'ComponentIteration.getComponentById(String id)\tApexPages.Component' : 'getComponentById($0)'
    },
    'ConnectApiException' : {
        'ConnectApiException.getErrorCode()\tString' : 'getErrorCode()$0',
        'ConnectApiException.getTypeName()\tString' : 'getTypeName()$0'
    },
    'ContentAttachment' : {
        'ContentAttachment.equals(Object obj)\tBoolean' : 'equals($0)',
        'ContentAttachment.hashCode()\tInteger' : 'hashCode()$0',
        'ContentAttachment.toString()\tString' : 'toString()$0'
    },
    'ContentAttachmentInput' : {
        'ContentAttachmentInput.convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object' : 'convertToJavaObject($0)',
        'ContentAttachmentInput.equals(Object obj)\tBoolean' : 'equals($0)',
        'ContentAttachmentInput.hashCode()\tInteger' : 'hashCode()$0',
        'ContentAttachmentInput.toString()\tString' : 'toString()$0'
    },
    'Cookie' : {
        'Cookie.getDomain()\tString' : 'getDomain()$0',
        'Cookie.getMaxAge()\tInteger' : 'getMaxAge()$0',
        'Cookie.getName()\tString' : 'getName()$0',
        'Cookie.getPath()\tString' : 'getPath()$0',
        'Cookie.getValue()\tString' : 'getValue()$0',
        'Cookie.isSecure()\tBoolean' : 'isSecure()$0'
    },
    'Crypto' : {
        'Crypto.decrypt(String algorithmName, Blob secretKey, Blob initializationVector, Blob encryptedData)\tBlob' : 'decrypt($0)',
        'Crypto.decryptWithManagedIV(String algorithmName, Blob secretKey, Blob encryptedData)\tBlob' : 'decryptWithManagedIV($0)',
        'Crypto.encrypt(String algorithmName, Blob secretKey, Blob initializationVector, Blob clearData)\tBlob' : 'encrypt($0)',
        'Crypto.encryptWithManagedIV(String algorithmName, Blob secretKey, Blob clearData)\tBlob' : 'encryptWithManagedIV($0)',
        'Crypto.generateAesKey(Integer size)\tBlob' : 'generateAesKey($0)',
        'Crypto.generateDigest(String algorithmName, Blob input)\tBlob' : 'generateDigest($0)',
        'Crypto.generateMac(String algorithmName, Blob input, Blob privateKey)\tBlob' : 'generateMac($0)',
        'Crypto.getRandomInteger()\tInteger' : 'getRandomInteger()$0',
        'Crypto.getRandomLong()\tLong' : 'getRandomLong()$0',
        'Crypto.sign(String algorithmName, Blob input, Blob privateKey)\tBlob' : 'sign($0)'
    },
    'DMLOptions' : {},
    'DashboardComponentAttachment' : {
        'DashboardComponentAttachment.equals(Object obj)\tBoolean' : 'equals($0)',
        'DashboardComponentAttachment.hashCode()\tInteger' : 'hashCode()$0',
        'DashboardComponentAttachment.toString()\tString' : 'toString()$0'
    },
    'DataCategoryGroupSobjectTypePair' : {},
    'Database' : {
        'Database.convertLead(Database.LeadConvert leadConvert)\tDatabase.LeadConvertResult' : 'convertLead($0)',
        'Database.convertLead(Database.LeadConvert leadConvert, Boolean allOrNothing)\tDatabase.LeadConvertResult' : 'convertLead($0)',
        'Database.convertLead(LIST<Database.LeadConvert> leadConverts)\tLIST<Database.LeadConvertResult>' : 'convertLead($0)',
        'Database.convertLead(LIST<Database.LeadConvert> leadConverts, Boolean allOrNothing)\tLIST<Database.LeadConvertResult>' : 'convertLead($0)',
        'Database.countQuery(String query)\tInteger' : 'countQuery($0)',
        'Database.delete(Id id)\tDatabase.DeleteResult' : 'delete($0)',
        'Database.delete(Id id, Boolean allOrNothing)\tDatabase.DeleteResult' : 'delete($0)',
        'Database.delete(LIST<Id> ids)\tLIST<Database.DeleteResult>' : 'delete($0)',
        'Database.delete(LIST<Id> ids, Boolean allOrNothing)\tLIST<Database.DeleteResult>' : 'delete($0)',
        'Database.delete(LIST<SObject> sobjects)\tLIST<Database.DeleteResult>' : 'delete($0)',
        'Database.delete(LIST<SObject> sobjects, Boolean allOrNothing)\tLIST<Database.DeleteResult>' : 'delete($0)',
        'Database.delete(SObject sobject)\tDatabase.DeleteResult' : 'delete($0)',
        'Database.delete(SObject sobject, Boolean allOrNothing)\tDatabase.DeleteResult' : 'delete($0)',
        'Database.emptyRecycleBin(LIST<Id> ids)\tLIST<Database.EmptyRecycleBinResult>' : 'emptyRecycleBin($0)',
        'Database.emptyRecycleBin(LIST<SObject> sobjects)\tLIST<Database.EmptyRecycleBinResult>' : 'emptyRecycleBin($0)',
        'Database.emptyRecycleBin(SObject sobject)\tDatabase.EmptyRecycleBinResult' : 'emptyRecycleBin($0)',
        'Database.executeBatch(APEX_OBJECT batchable)\tString' : 'executeBatch($0)',
        'Database.executeBatch(APEX_OBJECT batchable, Integer batchSize)\tString' : 'executeBatch($0)',
        'Database.getQueryLocator(LIST<SObject> query)\tDatabase.QueryLocator' : 'getQueryLocator($0)',
        'Database.getQueryLocator(String query)\tDatabase.QueryLocator' : 'getQueryLocator($0)',
        'Database.insert(LIST<SObject> sobjects)\tLIST<Database.SaveResult>' : 'insert($0)',
        'Database.insert(LIST<SObject> sobjects, APEX_OBJECT DmlOptions)\tLIST<Database.SaveResult>' : 'insert($0)',
        'Database.insert(LIST<SObject> sobjects, Boolean allOrNothing)\tLIST<Database.SaveResult>' : 'insert($0)',
        'Database.insert(SObject sobject)\tDatabase.SaveResult' : 'insert($0)',
        'Database.insert(SObject sobject, APEX_OBJECT DmlOptions)\tDatabase.SaveResult' : 'insert($0)',
        'Database.insert(SObject sobject, Boolean allOrNothing)\tDatabase.SaveResult' : 'insert($0)',
        'Database.query(String query)\tLIST<SObject>' : 'query($0)',
        'Database.rollback(System.Savepoint savepoint)\tvoid' : 'rollback($0)',
        'Database.setSavepoint()\tSystem.Savepoint' : 'setSavepoint()$0',
        'Database.undelete(Id id)\tDatabase.UndeleteResult' : 'undelete($0)',
        'Database.undelete(Id id, Boolean allOrNothing)\tDatabase.UndeleteResult' : 'undelete($0)',
        'Database.undelete(LIST<Id> ids)\tLIST<Database.UndeleteResult>' : 'undelete($0)',
        'Database.undelete(LIST<Id> ids, Boolean allOrNothing)\tLIST<Database.UndeleteResult>' : 'undelete($0)',
        'Database.undelete(LIST<SObject> sobjects)\tLIST<Database.UndeleteResult>' : 'undelete($0)',
        'Database.undelete(LIST<SObject> sobjects, Boolean allOrNothing)\tLIST<Database.UndeleteResult>' : 'undelete($0)',
        'Database.undelete(SObject sobject)\tDatabase.UndeleteResult' : 'undelete($0)',
        'Database.undelete(SObject sobject, Boolean allOrNothing)\tDatabase.UndeleteResult' : 'undelete($0)',
        'Database.update(LIST<SObject> sobjects)\tLIST<Database.SaveResult>' : 'update($0)',
        'Database.update(LIST<SObject> sobjects, APEX_OBJECT allOrNothing)\tLIST<Database.SaveResult>' : 'update($0)',
        'Database.update(LIST<SObject> sobjects, Boolean allOrNothing)\tLIST<Database.SaveResult>' : 'update($0)',
        'Database.update(SObject sobject)\tDatabase.SaveResult' : 'update($0)',
        'Database.update(SObject sobject, APEX_OBJECT allOrNothing)\tDatabase.SaveResult' : 'update($0)',
        'Database.update(SObject sobject, Boolean allOrNothing)\tDatabase.SaveResult' : 'update($0)',
        'Database.upsert(LIST<SObject> sobjects)\tLIST<Database.UpsertResult>' : 'upsert($0)',
        'Database.upsert(LIST<SObject> sobjects, Boolean allOrNothing)\tLIST<Database.UpsertResult>' : 'upsert($0)',
        'Database.upsert(LIST<SObject> sobjects, Schema.SObjectField field)\tLIST<Database.UpsertResult>' : 'upsert($0)',
        'Database.upsert(LIST<SObject> sobjects, Schema.SObjectField field, Boolean allOrNothing)\tLIST<Database.UpsertResult>' : 'upsert($0)',
        'Database.upsert(SObject sobject)\tDatabase.UpsertResult' : 'upsert($0)',
        'Database.upsert(SObject sobject, Boolean allOrNothing)\tDatabase.UpsertResult' : 'upsert($0)',
        'Database.upsert(SObject sobject, Schema.SObjectField field)\tDatabase.UpsertResult' : 'upsert($0)',
        'Database.upsert(SObject sobject, Schema.SObjectField field, Boolean allOrNothing)\tDatabase.UpsertResult' : 'upsert($0)'
    },
    'Date' : {
        'Date.addDays(Integer days)\tDate' : 'addDays($0)',
        'Date.addError(APEX_OBJECT msg)\tvoid' : 'addError($0)',
        'Date.addError(APEX_OBJECT msg, Boolean escape)\tvoid' : 'addError($0)',
        'Date.addError(String msg)\tvoid' : 'addError($0)',
        'Date.addError(String msg, Boolean escape)\tvoid' : 'addError($0)',
        'Date.addMonths(Integer months)\tDate' : 'addMonths($0)',
        'Date.addYears(Integer years)\tDate' : 'addYears($0)',
        'Date.day()\tInteger' : 'day()$0',
        'Date.dayOfYear()\tInteger' : 'dayOfYear()$0',
        'Date.daysBetween(Date other)\tInteger' : 'daysBetween($0)',
        'Date.daysInMonth(Integer year, Integer month)\tInteger' : 'daysInMonth($0)',
        'Date.format()\tString' : 'format()$0',
        'Date.isLeapYear(Integer year)\tBoolean' : 'isLeapYear($0)',
        'Date.isSameDay(Date other)\tBoolean' : 'isSameDay($0)',
        'Date.month()\tInteger' : 'month()$0',
        'Date.monthsBetween(Date other)\tInteger' : 'monthsBetween($0)',
        'Date.newInstance(Integer year, Integer month, Integer day)\tDate' : 'newInstance($0)',
        'Date.parse(String str)\tDate' : 'parse($0)',
        'Date.toStartOfMonth()\tDate' : 'toStartOfMonth()$0',
        'Date.toStartOfWeek()\tDate' : 'toStartOfWeek()$0',
        'Date.today()\tDate' : 'today()$0',
        'Date.valueOf(Object o)\tDate' : 'valueOf($0)',
        'Date.valueOf(String str)\tDate' : 'valueOf($0)',
        'Date.year()\tInteger' : 'year()$0'
    },
    'Datetime' : {
        'Datetime.addDays(Integer days)\tDatetime' : 'addDays($0)',
        'Datetime.addError(APEX_OBJECT msg)\tvoid' : 'addError($0)',
        'Datetime.addError(APEX_OBJECT msg, Boolean escape)\tvoid' : 'addError($0)',
        'Datetime.addError(String msg)\tvoid' : 'addError($0)',
        'Datetime.addError(String msg, Boolean escape)\tvoid' : 'addError($0)',
        'Datetime.addHours(Integer hours)\tDatetime' : 'addHours($0)',
        'Datetime.addMinutes(Integer minutes)\tDatetime' : 'addMinutes($0)',
        'Datetime.addMonths(Integer months)\tDatetime' : 'addMonths($0)',
        'Datetime.addSeconds(Integer seconds)\tDatetime' : 'addSeconds($0)',
        'Datetime.addYears(Integer years)\tDatetime' : 'addYears($0)',
        'Datetime.date()\tDate' : 'date()$0',
        'Datetime.dateGmt()\tDate' : 'dateGmt()$0',
        'Datetime.day()\tInteger' : 'day()$0',
        'Datetime.dayGmt()\tInteger' : 'dayGmt()$0',
        'Datetime.dayOfYear()\tInteger' : 'dayOfYear()$0',
        'Datetime.dayOfYearGmt()\tInteger' : 'dayOfYearGmt()$0',
        'Datetime.format()\tString' : 'format()$0',
        'Datetime.format(String dateformat)\tString' : 'format($0)',
        'Datetime.format(String dateformat, String timezone)\tString' : 'format($0)',
        'Datetime.formatGmt(String dateformat)\tString' : 'formatGmt($0)',
        'Datetime.formatLong()\tString' : 'formatLong()$0',
        'Datetime.getTime()\tLong' : 'getTime()$0',
        'Datetime.hour()\tInteger' : 'hour()$0',
        'Datetime.hourGmt()\tInteger' : 'hourGmt()$0',
        'Datetime.isSameDay(Datetime other)\tBoolean' : 'isSameDay($0)',
        'Datetime.millisecond()\tInteger' : 'millisecond()$0',
        'Datetime.millisecondGmt()\tInteger' : 'millisecondGmt()$0',
        'Datetime.minute()\tInteger' : 'minute()$0',
        'Datetime.minuteGmt()\tInteger' : 'minuteGmt()$0',
        'Datetime.month()\tInteger' : 'month()$0',
        'Datetime.monthGmt()\tInteger' : 'monthGmt()$0',
        'Datetime.newInstance(Date date, Time time)\tDatetime' : 'newInstance($0)',
        'Datetime.newInstance(Integer year, Integer month, Integer day)\tDatetime' : 'newInstance($0)',
        'Datetime.newInstance(Integer year, Integer month, Integer day, Integer hour, Integer minute, Integer second)\tDatetime' : 'newInstance($0)',
        'Datetime.newInstance(Long time)\tDatetime' : 'newInstance($0)',
        'Datetime.newInstanceGmt(Date date, Time time)\tDatetime' : 'newInstanceGmt($0)',
        'Datetime.newInstanceGmt(Integer year, Integer month, Integer day)\tDatetime' : 'newInstanceGmt($0)',
        'Datetime.newInstanceGmt(Integer year, Integer month, Integer day, Integer hour, Integer minute, Integer second)\tDatetime' : 'newInstanceGmt($0)',
        'Datetime.now()\tDatetime' : 'now()$0',
        'Datetime.parse(String str)\tDatetime' : 'parse($0)',
        'Datetime.second()\tInteger' : 'second()$0',
        'Datetime.secondGmt()\tInteger' : 'secondGmt()$0',
        'Datetime.time()\tTime' : 'time()$0',
        'Datetime.timeGmt()\tTime' : 'timeGmt()$0',
        'Datetime.valueOf(Object o)\tDatetime' : 'valueOf($0)',
        'Datetime.valueOf(String str)\tDatetime' : 'valueOf($0)',
        'Datetime.valueOfGmt(String str)\tDatetime' : 'valueOfGmt($0)',
        'Datetime.year()\tInteger' : 'year()$0',
        'Datetime.yearGmt()\tInteger' : 'yearGmt()$0'
    },
    'Decimal' : {
        'Decimal.abs()\tDecimal' : 'abs()$0',
        'Decimal.addError(APEX_OBJECT msg)\tvoid' : 'addError($0)',
        'Decimal.addError(APEX_OBJECT msg, Boolean escape)\tvoid' : 'addError($0)',
        'Decimal.addError(String msg)\tvoid' : 'addError($0)',
        'Decimal.addError(String msg, Boolean escape)\tvoid' : 'addError($0)',
        'Decimal.divide(Decimal divisor, Integer scale)\tDecimal' : 'divide($0)',
        'Decimal.divide(Decimal divisor, Integer scale, APEX_OBJECT roundingMode)\tDecimal' : 'divide($0)',
        'Decimal.doubleValue()\tDouble' : 'doubleValue()$0',
        'Decimal.format()\tString' : 'format()$0',
        'Decimal.intValue()\tInteger' : 'intValue()$0',
        'Decimal.longValue()\tLong' : 'longValue()$0',
        'Decimal.pow(Integer exponent)\tDecimal' : 'pow($0)',
        'Decimal.precision()\tInteger' : 'precision()$0',
        'Decimal.round()\tLong' : 'round()$0',
        'Decimal.round(system.RoundingMode roundingMode)\tLong' : 'round($0)',
        'Decimal.scale()\tInteger' : 'scale()$0',
        'Decimal.setScale(Integer scale)\tDecimal' : 'setScale($0)',
        'Decimal.setScale(Integer scale, system.RoundingMode roundingMode)\tDecimal' : 'setScale($0)',
        'Decimal.stripTrailingZeros()\tDecimal' : 'stripTrailingZeros()$0',
        'Decimal.toPlainString()\tString' : 'toPlainString()$0',
        'Decimal.valueOf(Double dbl)\tDecimal' : 'valueOf($0)',
        'Decimal.valueOf(Long lng)\tDecimal' : 'valueOf($0)',
        'Decimal.valueOf(String str)\tDecimal' : 'valueOf($0)'
    },
    'DisplayType' : {
        'DisplayType.values()\tLIST<Schema.DisplayType>' : 'values()$0'
    },
    'DmlException' : {
        'DmlException.getCause()\tException' : 'getCause()$0',
        'DmlException.getDmlFieldNames(Integer index)\tLIST<String>' : 'getDmlFieldNames($0)',
        'DmlException.getDmlFields(Integer index)\tLIST<Schema.SObjectField>' : 'getDmlFields($0)',
        'DmlException.getDmlId(Integer index)\tString' : 'getDmlId($0)',
        'DmlException.getDmlIndex(Integer index)\tInteger' : 'getDmlIndex($0)',
        'DmlException.getDmlMessage(Integer index)\tString' : 'getDmlMessage($0)',
        'DmlException.getDmlStatusCode(Integer index)\tString' : 'getDmlStatusCode($0)',
        'DmlException.getDmlType(Integer index)\tsystem.StatusCode' : 'getDmlType($0)',
        'DmlException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'DmlException.getMessage()\tString' : 'getMessage()$0',
        'DmlException.getNumDml()\tInteger' : 'getNumDml()$0',
        'DmlException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'DmlException.getTypeName()\tString' : 'getTypeName()$0',
        'DmlException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'DmlException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'Document' : {
        'Document.createRootElement(String name, String namespace, String prefix)\tdom.XmlNode' : 'createRootElement($0)',
        'Document.getRootElement()\tdom.XmlNode' : 'getRootElement()$0',
        'Document.load(String xml)\tvoid' : 'load($0)',
        'Document.toXmlString()\tString' : 'toXmlString()$0'
    },
    'Double' : {
        'Double.addError(APEX_OBJECT msg)\tvoid' : 'addError($0)',
        'Double.addError(APEX_OBJECT msg, Boolean escape)\tvoid' : 'addError($0)',
        'Double.addError(String msg)\tvoid' : 'addError($0)',
        'Double.addError(String msg, Boolean escape)\tvoid' : 'addError($0)',
        'Double.format()\tString' : 'format()$0',
        'Double.intValue()\tInteger' : 'intValue()$0',
        'Double.longValue()\tLong' : 'longValue()$0',
        'Double.round()\tLong' : 'round()$0',
        'Double.valueOf(Object o)\tDouble' : 'valueOf($0)',
        'Double.valueOf(String str)\tDouble' : 'valueOf($0)'
    },
    'EmailAttachment' : {},
    'EmailException' : {
        'EmailException.getCause()\tException' : 'getCause()$0',
        'EmailException.getDmlFieldNames(Integer index)\tLIST<String>' : 'getDmlFieldNames($0)',
        'EmailException.getDmlFields(Integer index)\tLIST<Schema.SObjectField>' : 'getDmlFields($0)',
        'EmailException.getDmlId(Integer index)\tString' : 'getDmlId($0)',
        'EmailException.getDmlIndex(Integer index)\tInteger' : 'getDmlIndex($0)',
        'EmailException.getDmlMessage(Integer index)\tString' : 'getDmlMessage($0)',
        'EmailException.getDmlStatusCode(Integer index)\tString' : 'getDmlStatusCode($0)',
        'EmailException.getDmlType(Integer index)\tsystem.StatusCode' : 'getDmlType($0)',
        'EmailException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'EmailException.getMessage()\tString' : 'getMessage()$0',
        'EmailException.getNumDml()\tInteger' : 'getNumDml()$0',
        'EmailException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'EmailException.getTypeName()\tString' : 'getTypeName()$0',
        'EmailException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'EmailException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'EmailFileAttachment' : {},
    'EmailHeader' : {},
    'EmailTemplateSelector' : {
        'EmailTemplateSelector.getDefaultEmailTemplateId(Id param1)\tId' : 'getDefaultEmailTemplateId($0)'
    },
    'EmailToCaseHandler' : {},
    'EmailToSalesforceHandler' : {},
    'EmptyStackException' : {
        'EmptyStackException.getTypeName()\tString' : 'getTypeName()$0'
    },
    'EncodingUtil' : {
        'EncodingUtil.base64Decode(String s)\tBlob' : 'base64Decode($0)',
        'EncodingUtil.base64Encode(Blob s)\tString' : 'base64Encode($0)',
        'EncodingUtil.convertToHex(Blob s)\tString' : 'convertToHex($0)',
        'EncodingUtil.urlDecode(String s, String enc)\tString' : 'urlDecode($0)',
        'EncodingUtil.urlEncode(String s, String enc)\tString' : 'urlEncode($0)'
    },
    'EntityLinkSegment' : {
        'EntityLinkSegment.equals(Object obj)\tBoolean' : 'equals($0)',
        'EntityLinkSegment.hashCode()\tInteger' : 'hashCode()$0',
        'EntityLinkSegment.toString()\tString' : 'toString()$0'
    },
    'Exception' : {
        'Exception.getCause()\tException' : 'getCause()$0',
        'Exception.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'Exception.getMessage()\tString' : 'getMessage()$0',
        'Exception.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'Exception.getTypeName()\tString' : 'getTypeName()$0',
        'Exception.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'Exception.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'Features' : {
        'Features.equals(Object obj)\tBoolean' : 'equals($0)',
        'Features.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'Features.hashCode()\tInteger' : 'hashCode()$0',
        'Features.toString()\tString' : 'toString()$0'
    },
    'Feed' : {
        'Feed.equals(Object obj)\tBoolean' : 'equals($0)',
        'Feed.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'Feed.hashCode()\tInteger' : 'hashCode()$0',
        'Feed.toString()\tString' : 'toString()$0'
    },
    'FeedBody' : {
        'FeedBody.equals(Object obj)\tBoolean' : 'equals($0)',
        'FeedBody.hashCode()\tInteger' : 'hashCode()$0',
        'FeedBody.toString()\tString' : 'toString()$0'
    },
    'FeedFavorite' : {
        'FeedFavorite.equals(Object obj)\tBoolean' : 'equals($0)',
        'FeedFavorite.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'FeedFavorite.hashCode()\tInteger' : 'hashCode()$0',
        'FeedFavorite.toString()\tString' : 'toString()$0'
    },
    'FeedFavoriteType' : {
        'FeedFavoriteType.values()\tLIST<ConnectApi.FeedFavoriteType>' : 'values()$0'
    },
    'FeedFavorites' : {
        'FeedFavorites.equals(Object obj)\tBoolean' : 'equals($0)',
        'FeedFavorites.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'FeedFavorites.hashCode()\tInteger' : 'hashCode()$0',
        'FeedFavorites.toString()\tString' : 'toString()$0'
    },
    'FeedItem' : {
        'FeedItem.equals(Object obj)\tBoolean' : 'equals($0)',
        'FeedItem.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'FeedItem.hashCode()\tInteger' : 'hashCode()$0',
        'FeedItem.toString()\tString' : 'toString()$0'
    },
    'FeedItemAttachment' : {
        'FeedItemAttachment.equals(Object obj)\tBoolean' : 'equals($0)',
        'FeedItemAttachment.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'FeedItemAttachment.hashCode()\tInteger' : 'hashCode()$0',
        'FeedItemAttachment.toString()\tString' : 'toString()$0'
    },
    'FeedItemAttachmentInput' : {
        'FeedItemAttachmentInput.convertToJavaObject(java:common.api.AppVersion param1)\tjava:java.lang.Object' : 'convertToJavaObject($0)',
        'FeedItemAttachmentInput.equals(Object obj)\tBoolean' : 'equals($0)',
        'FeedItemAttachmentInput.hashCode()\tInteger' : 'hashCode()$0',
        'FeedItemAttachmentInput.toString()\tString' : 'toString()$0'
    },
    'FeedItemAttachmentType' : {
        'FeedItemAttachmentType.values()\tLIST<ConnectApi.FeedItemAttachmentType>' : 'values()$0'
    },
    'FeedItemInput' : {
        'FeedItemInput.convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object' : 'convertToJavaObject($0)',
        'FeedItemInput.equals(Object obj)\tBoolean' : 'equals($0)',
        'FeedItemInput.hashCode()\tInteger' : 'hashCode()$0',
        'FeedItemInput.toString()\tString' : 'toString()$0'
    },
    'FeedItemPage' : {
        'FeedItemPage.equals(Object obj)\tBoolean' : 'equals($0)',
        'FeedItemPage.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'FeedItemPage.hashCode()\tInteger' : 'hashCode()$0',
        'FeedItemPage.toString()\tString' : 'toString()$0'
    },
    'FeedItemType' : {
        'FeedItemType.values()\tLIST<ConnectApi.FeedItemType>' : 'values()$0'
    },
    'FeedItemVisibilityType' : {
        'FeedItemVisibilityType.values()\tLIST<ConnectApi.FeedItemVisibilityType>' : 'values()$0'
    },
    'FeedModifiedInfo' : {
        'FeedModifiedInfo.equals(Object obj)\tBoolean' : 'equals($0)',
        'FeedModifiedInfo.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'FeedModifiedInfo.hashCode()\tInteger' : 'hashCode()$0',
        'FeedModifiedInfo.toString()\tString' : 'toString()$0'
    },
    'FeedPoll' : {
        'FeedPoll.equals(Object obj)\tBoolean' : 'equals($0)',
        'FeedPoll.hashCode()\tInteger' : 'hashCode()$0',
        'FeedPoll.toString()\tString' : 'toString()$0'
    },
    'FeedPollChoice' : {
        'FeedPollChoice.equals(Object obj)\tBoolean' : 'equals($0)',
        'FeedPollChoice.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'FeedPollChoice.hashCode()\tInteger' : 'hashCode()$0',
        'FeedPollChoice.toString()\tString' : 'toString()$0'
    },
    'FeedSortOrder' : {
        'FeedSortOrder.values()\tLIST<ConnectApi.FeedSortOrder>' : 'values()$0'
    },
    'FeedType' : {
        'FeedType.values()\tLIST<ConnectApi.FeedType>' : 'values()$0'
    },
    'FieldChangeNameSegment' : {
        'FieldChangeNameSegment.equals(Object obj)\tBoolean' : 'equals($0)',
        'FieldChangeNameSegment.hashCode()\tInteger' : 'hashCode()$0',
        'FieldChangeNameSegment.toString()\tString' : 'toString()$0'
    },
    'FieldChangeSegment' : {
        'FieldChangeSegment.equals(Object obj)\tBoolean' : 'equals($0)',
        'FieldChangeSegment.hashCode()\tInteger' : 'hashCode()$0',
        'FieldChangeSegment.toString()\tString' : 'toString()$0'
    },
    'FieldChangeValueSegment' : {
        'FieldChangeValueSegment.equals(Object obj)\tBoolean' : 'equals($0)',
        'FieldChangeValueSegment.hashCode()\tInteger' : 'hashCode()$0',
        'FieldChangeValueSegment.toString()\tString' : 'toString()$0'
    },
    'FileSummary' : {
        'FileSummary.equals(Object obj)\tBoolean' : 'equals($0)',
        'FileSummary.hashCode()\tInteger' : 'hashCode()$0',
        'FileSummary.toString()\tString' : 'toString()$0'
    },
    'FinalException' : {
        'FinalException.getCause()\tException' : 'getCause()$0',
        'FinalException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'FinalException.getMessage()\tString' : 'getMessage()$0',
        'FinalException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'FinalException.getTypeName()\tString' : 'getTypeName()$0',
        'FinalException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'FinalException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'FlowException' : {
        'FlowException.getCause()\tException' : 'getCause()$0',
        'FlowException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'FlowException.getMessage()\tString' : 'getMessage()$0',
        'FlowException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'FlowException.getTypeName()\tString' : 'getTypeName()$0',
        'FlowException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'FlowException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'FollowerPage' : {
        'FollowerPage.equals(Object obj)\tBoolean' : 'equals($0)',
        'FollowerPage.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'FollowerPage.hashCode()\tInteger' : 'hashCode()$0',
        'FollowerPage.toString()\tString' : 'toString()$0'
    },
    'FollowingCounts' : {
        'FollowingCounts.equals(Object obj)\tBoolean' : 'equals($0)',
        'FollowingCounts.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'FollowingCounts.hashCode()\tInteger' : 'hashCode()$0',
        'FollowingCounts.toString()\tString' : 'toString()$0'
    },
    'FollowingPage' : {
        'FollowingPage.equals(Object obj)\tBoolean' : 'equals($0)',
        'FollowingPage.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'FollowingPage.hashCode()\tInteger' : 'hashCode()$0',
        'FollowingPage.toString()\tString' : 'toString()$0'
    },
    'GlobalInfluence' : {
        'GlobalInfluence.equals(Object obj)\tBoolean' : 'equals($0)',
        'GlobalInfluence.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'GlobalInfluence.hashCode()\tInteger' : 'hashCode()$0',
        'GlobalInfluence.toString()\tString' : 'toString()$0'
    },
    'GroupChatterSettings' : {
        'GroupChatterSettings.equals(Object obj)\tBoolean' : 'equals($0)',
        'GroupChatterSettings.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'GroupChatterSettings.hashCode()\tInteger' : 'hashCode()$0',
        'GroupChatterSettings.toString()\tString' : 'toString()$0'
    },
    'GroupEmailFrequency' : {
        'GroupEmailFrequency.values()\tLIST<ConnectApi.GroupEmailFrequency>' : 'values()$0'
    },
    'GroupInformation' : {
        'GroupInformation.equals(Object obj)\tBoolean' : 'equals($0)',
        'GroupInformation.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'GroupInformation.hashCode()\tInteger' : 'hashCode()$0',
        'GroupInformation.toString()\tString' : 'toString()$0'
    },
    'GroupInformationInput' : {
        'GroupInformationInput.convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object' : 'convertToJavaObject($0)',
        'GroupInformationInput.equals(Object obj)\tBoolean' : 'equals($0)',
        'GroupInformationInput.hashCode()\tInteger' : 'hashCode()$0',
        'GroupInformationInput.toString()\tString' : 'toString()$0'
    },
    'GroupMember' : {
        'GroupMember.equals(Object obj)\tBoolean' : 'equals($0)',
        'GroupMember.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'GroupMember.hashCode()\tInteger' : 'hashCode()$0',
        'GroupMember.toString()\tString' : 'toString()$0'
    },
    'GroupMemberPage' : {
        'GroupMemberPage.equals(Object obj)\tBoolean' : 'equals($0)',
        'GroupMemberPage.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'GroupMemberPage.hashCode()\tInteger' : 'hashCode()$0',
        'GroupMemberPage.toString()\tString' : 'toString()$0'
    },
    'GroupMembershipRequest' : {
        'GroupMembershipRequest.equals(Object obj)\tBoolean' : 'equals($0)',
        'GroupMembershipRequest.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'GroupMembershipRequest.hashCode()\tInteger' : 'hashCode()$0',
        'GroupMembershipRequest.toString()\tString' : 'toString()$0'
    },
    'GroupMembershipRequestStatus' : {
        'GroupMembershipRequestStatus.values()\tLIST<ConnectApi.GroupMembershipRequestStatus>' : 'values()$0'
    },
    'GroupMembershipRequests' : {
        'GroupMembershipRequests.equals(Object obj)\tBoolean' : 'equals($0)',
        'GroupMembershipRequests.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'GroupMembershipRequests.hashCode()\tInteger' : 'hashCode()$0',
        'GroupMembershipRequests.toString()\tString' : 'toString()$0'
    },
    'GroupMembershipType' : {
        'GroupMembershipType.values()\tLIST<ConnectApi.GroupMembershipType>' : 'values()$0'
    },
    'GroupVisibilityType' : {
        'GroupVisibilityType.values()\tLIST<ConnectApi.GroupVisibilityType>' : 'values()$0'
    },
    'HandledException' : {
        'HandledException.getCause()\tException' : 'getCause()$0',
        'HandledException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'HandledException.getMessage()\tString' : 'getMessage()$0',
        'HandledException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'HandledException.getTypeName()\tString' : 'getTypeName()$0',
        'HandledException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'HandledException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'HashtagSegment' : {
        'HashtagSegment.equals(Object obj)\tBoolean' : 'equals($0)',
        'HashtagSegment.hashCode()\tInteger' : 'hashCode()$0',
        'HashtagSegment.toString()\tString' : 'toString()$0'
    },
    'HashtagSegmentInput' : {
        'HashtagSegmentInput.convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object' : 'convertToJavaObject($0)',
        'HashtagSegmentInput.equals(Object obj)\tBoolean' : 'equals($0)',
        'HashtagSegmentInput.hashCode()\tInteger' : 'hashCode()$0',
        'HashtagSegmentInput.toString()\tString' : 'toString()$0'
    },
    'Header' : {},
    'Http' : {
        'Http.send(ANY request)\tSystem.HttpResponse' : 'send($0)',
        'Http.toString()\tString' : 'toString()$0'
    },
    'HttpCalloutMock' : {
        'HttpCalloutMock.respond(System.HttpRequest param1)\tSystem.HttpResponse' : 'respond($0)'
    },
    'HttpRequest' : {
        'HttpRequest.getBody()\tString' : 'getBody()$0',
        'HttpRequest.getBodyAsBlob()\tBlob' : 'getBodyAsBlob()$0',
        'HttpRequest.getBodyDocument()\tdom.Document' : 'getBodyDocument()$0',
        'HttpRequest.getCompressed()\tBoolean' : 'getCompressed()$0',
        'HttpRequest.getEndpoint()\tString' : 'getEndpoint()$0',
        'HttpRequest.getHeader(String key)\tString' : 'getHeader($0)',
        'HttpRequest.getMethod()\tString' : 'getMethod()$0',
        'HttpRequest.setBody(String body)\tvoid' : 'setBody($0)',
        'HttpRequest.setBodyAsBlob(Blob body)\tvoid' : 'setBodyAsBlob($0)',
        'HttpRequest.setBodyDocument(ANY body)\tvoid' : 'setBodyDocument($0)',
        'HttpRequest.setClientCertificate(String clientCert, String password)\tvoid' : 'setClientCertificate($0)',
        'HttpRequest.setClientCertificateName(String certDevName)\tvoid' : 'setClientCertificateName($0)',
        'HttpRequest.setCompressed(Boolean compressed)\tvoid' : 'setCompressed($0)',
        'HttpRequest.setEndpoint(String endpoint)\tvoid' : 'setEndpoint($0)',
        'HttpRequest.setHeader(String key, String value)\tvoid' : 'setHeader($0)',
        'HttpRequest.setMethod(String method)\tvoid' : 'setMethod($0)',
        'HttpRequest.setTimeout(Integer timeout)\tvoid' : 'setTimeout($0)',
        'HttpRequest.toString()\tString' : 'toString()$0'
    },
    'HttpResponse' : {
        'HttpResponse.getBody()\tString' : 'getBody()$0',
        'HttpResponse.getBodyAsBlob()\tBlob' : 'getBodyAsBlob()$0',
        'HttpResponse.getBodyDocument()\tdom.Document' : 'getBodyDocument()$0',
        'HttpResponse.getHeader(String key)\tString' : 'getHeader($0)',
        'HttpResponse.getHeaderKeys()\tLIST<String>' : 'getHeaderKeys()$0',
        'HttpResponse.getStatus()\tString' : 'getStatus()$0',
        'HttpResponse.getStatusCode()\tInteger' : 'getStatusCode()$0',
        'HttpResponse.getXmlStreamReader()\tSystem.XmlStreamReader' : 'getXmlStreamReader()$0',
        'HttpResponse.setBody(String body)\tvoid' : 'setBody($0)',
        'HttpResponse.setBodyAsBlob(Blob body)\tvoid' : 'setBodyAsBlob($0)',
        'HttpResponse.setHeader(String key, String value)\tvoid' : 'setHeader($0)',
        'HttpResponse.setStatus(String status)\tvoid' : 'setStatus($0)',
        'HttpResponse.setStatusCode(Integer statusCode)\tvoid' : 'setStatusCode($0)',
        'HttpResponse.toString()\tString' : 'toString()$0'
    },
    'Icon' : {
        'Icon.equals(Object obj)\tBoolean' : 'equals($0)',
        'Icon.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'Icon.hashCode()\tInteger' : 'hashCode()$0',
        'Icon.toString()\tString' : 'toString()$0'
    },
    'Id' : {
        'Id.addError(APEX_OBJECT msg)\tvoid' : 'addError($0)',
        'Id.addError(APEX_OBJECT msg, Boolean escape)\tvoid' : 'addError($0)',
        'Id.addError(String msg)\tvoid' : 'addError($0)',
        'Id.addError(String msg, Boolean escape)\tvoid' : 'addError($0)',
        'Id.getSobjectType()\tSchema.SObjectType' : 'getSobjectType()$0',
        'Id.valueOf(String str)\tId' : 'valueOf($0)'
    },
    'IdeaStandardController' : {
        'IdeaStandardController.addFields(LIST<String> fieldNames)\tvoid' : 'addFields($0)',
        'IdeaStandardController.cancel()\tSystem.PageReference' : 'cancel()$0',
        'IdeaStandardController.delete()\tSystem.PageReference' : 'delete()$0',
        'IdeaStandardController.edit()\tSystem.PageReference' : 'edit()$0',
        'IdeaStandardController.getCommentList()\tLIST<IdeaComment>' : 'getCommentList()$0',
        'IdeaStandardController.getId()\tString' : 'getId()$0',
        'IdeaStandardController.getRecord()\tSObject' : 'getRecord()$0',
        'IdeaStandardController.getSubject()\tSObject' : 'getSubject()$0',
        'IdeaStandardController.reset()\tvoid' : 'reset()$0',
        'IdeaStandardController.save()\tSystem.PageReference' : 'save()$0',
        'IdeaStandardController.view()\tSystem.PageReference' : 'view()$0'
    },
    'IdeaStandardSetController' : {
        'IdeaStandardSetController.addFields(LIST<String> fieldNames)\tvoid' : 'addFields($0)',
        'IdeaStandardSetController.cancel()\tSystem.PageReference' : 'cancel()$0',
        'IdeaStandardSetController.first()\tvoid' : 'first()$0',
        'IdeaStandardSetController.getCompleteResult()\tBoolean' : 'getCompleteResult()$0',
        'IdeaStandardSetController.getFilterId()\tString' : 'getFilterId()$0',
        'IdeaStandardSetController.getHasNext()\tBoolean' : 'getHasNext()$0',
        'IdeaStandardSetController.getHasPrevious()\tBoolean' : 'getHasPrevious()$0',
        'IdeaStandardSetController.getIdeaList()\tLIST<Idea>' : 'getIdeaList()$0',
        'IdeaStandardSetController.getListViewOptions()\tLIST<System.SelectOption>' : 'getListViewOptions()$0',
        'IdeaStandardSetController.getPageNumber()\tInteger' : 'getPageNumber()$0',
        'IdeaStandardSetController.getPageSize()\tInteger' : 'getPageSize()$0',
        'IdeaStandardSetController.getRecord()\tSObject' : 'getRecord()$0',
        'IdeaStandardSetController.getRecords()\tLIST<SObject>' : 'getRecords()$0',
        'IdeaStandardSetController.getResultSize()\tInteger' : 'getResultSize()$0',
        'IdeaStandardSetController.getSelected()\tLIST<SObject>' : 'getSelected()$0',
        'IdeaStandardSetController.last()\tvoid' : 'last()$0',
        'IdeaStandardSetController.next()\tvoid' : 'next()$0',
        'IdeaStandardSetController.previous()\tvoid' : 'previous()$0',
        'IdeaStandardSetController.reset()\tvoid' : 'reset()$0',
        'IdeaStandardSetController.save()\tSystem.PageReference' : 'save()$0',
        'IdeaStandardSetController.setFilterId(String filterId)\tvoid' : 'setFilterId($0)',
        'IdeaStandardSetController.setPageNumber(Integer pageNumber)\tvoid' : 'setPageNumber($0)',
        'IdeaStandardSetController.setPageSize(Integer pageSize)\tvoid' : 'setPageSize($0)',
        'IdeaStandardSetController.setSelected(LIST<SObject> selected)\tvoid' : 'setSelected($0)'
    },
    'Ideas' : {
        'Ideas.findSimilar(SObject idea)\tLIST<Id>' : 'findSimilar($0)',
        'Ideas.getAllRecentReplies(String userId, String communityId)\tLIST<Id>' : 'getAllRecentReplies($0)',
        'Ideas.getReadRecentReplies(String userId, String communityId)\tLIST<Id>' : 'getReadRecentReplies($0)',
        'Ideas.getUnreadRecentReplies(String userId, String communityId)\tLIST<Id>' : 'getUnreadRecentReplies($0)',
        'Ideas.markRead(String ideaId)\tvoid' : 'markRead($0)'
    },
    'InboundEmail' : {},
    'InboundEmailHandler' : {
        'InboundEmailHandler.handleInboundEmail(Messaging.InboundEmail param1, Messaging.InboundEnvelope param2)\tMessaging.InboundEmailResult' : 'handleInboundEmail($0)'
    },
    'InboundEmailResult' : {},
    'InboundEnvelope' : {},
    'InputParameter' : {},
    'Integer' : {
        'Integer.addError(APEX_OBJECT msg)\tvoid' : 'addError($0)',
        'Integer.addError(APEX_OBJECT msg, Boolean escape)\tvoid' : 'addError($0)',
        'Integer.addError(String msg)\tvoid' : 'addError($0)',
        'Integer.addError(String msg, Boolean escape)\tvoid' : 'addError($0)',
        'Integer.format()\tString' : 'format()$0',
        'Integer.valueOf(Object o)\tInteger' : 'valueOf($0)',
        'Integer.valueOf(String i)\tInteger' : 'valueOf($0)'
    },
    'Interview' : {
        'Interview.getVariableValue(String param1)\tObject' : 'getVariableValue($0)'
    },
    'InvalidHeaderException' : {
        'InvalidHeaderException.getTypeName()\tString' : 'getTypeName()$0'
    },
    'InvalidParameterValueException' : {
        'InvalidParameterValueException.getCause()\tException' : 'getCause()$0',
        'InvalidParameterValueException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'InvalidParameterValueException.getMessage()\tString' : 'getMessage()$0',
        'InvalidParameterValueException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'InvalidParameterValueException.getTypeName()\tString' : 'getTypeName()$0',
        'InvalidParameterValueException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'InvalidParameterValueException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'InvalidReadOnlyUserDmlException' : {
        'InvalidReadOnlyUserDmlException.getCause()\tException' : 'getCause()$0',
        'InvalidReadOnlyUserDmlException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'InvalidReadOnlyUserDmlException.getMessage()\tString' : 'getMessage()$0',
        'InvalidReadOnlyUserDmlException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'InvalidReadOnlyUserDmlException.getTypeName()\tString' : 'getTypeName()$0',
        'InvalidReadOnlyUserDmlException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'InvalidReadOnlyUserDmlException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'Iterable' : {
        'Iterable.iterator()\tsystem.Iterator' : 'iterator()$0'
    },
    'Iterator' : {
        'Iterator.hasNext()\tBoolean' : 'hasNext()$0',
        'Iterator.next()\tObject' : 'next()$0'
    },
    'JSON' : {
        'JSON.createGenerator(Boolean pretty)\tsystem.JSONGenerator' : 'createGenerator($0)',
        'JSON.createParser(String jsonString)\tsystem.JSONParser' : 'createParser($0)',
        'JSON.deserialize(String jsonString, system.Type apexType)\tObject' : 'deserialize($0)',
        'JSON.deserializeStrict(String jsonString, system.Type apexType)\tObject' : 'deserializeStrict($0)',
        'JSON.deserializeUntyped(String jsonString)\tObject' : 'deserializeUntyped($0)',
        'JSON.serialize(Object o)\tString' : 'serialize($0)',
        'JSON.serializePretty(Object o)\tString' : 'serializePretty($0)'
    },
    'JSONException' : {
        'JSONException.getCause()\tException' : 'getCause()$0',
        'JSONException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'JSONException.getMessage()\tString' : 'getMessage()$0',
        'JSONException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'JSONException.getTypeName()\tString' : 'getTypeName()$0',
        'JSONException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'JSONException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'JSONGenerator' : {
        'JSONGenerator.close()\tvoid' : 'close()$0',
        'JSONGenerator.getAsString()\tString' : 'getAsString()$0',
        'JSONGenerator.isClosed()\tBoolean' : 'isClosed()$0',
        'JSONGenerator.writeBlob(Blob b)\tvoid' : 'writeBlob($0)',
        'JSONGenerator.writeBlobField(String fieldName, Blob b)\tvoid' : 'writeBlobField($0)',
        'JSONGenerator.writeBoolean(Boolean b)\tvoid' : 'writeBoolean($0)',
        'JSONGenerator.writeBooleanField(String fieldName, Boolean b)\tvoid' : 'writeBooleanField($0)',
        'JSONGenerator.writeDate(Date d)\tvoid' : 'writeDate($0)',
        'JSONGenerator.writeDateField(String fieldName, Date d)\tvoid' : 'writeDateField($0)',
        'JSONGenerator.writeDateTime(Datetime dt)\tvoid' : 'writeDateTime($0)',
        'JSONGenerator.writeDateTimeField(String fieldName, Datetime dt)\tvoid' : 'writeDateTimeField($0)',
        'JSONGenerator.writeEndArray()\tvoid' : 'writeEndArray()$0',
        'JSONGenerator.writeEndObject()\tvoid' : 'writeEndObject()$0',
        'JSONGenerator.writeFieldName(String fieldName)\tvoid' : 'writeFieldName($0)',
        'JSONGenerator.writeId(Id id)\tvoid' : 'writeId($0)',
        'JSONGenerator.writeIdField(String fieldName, Id id)\tvoid' : 'writeIdField($0)',
        'JSONGenerator.writeNull()\tvoid' : 'writeNull()$0',
        'JSONGenerator.writeNullField(String fieldName)\tvoid' : 'writeNullField($0)',
        'JSONGenerator.writeNumber(Decimal d)\tvoid' : 'writeNumber($0)',
        'JSONGenerator.writeNumber(Double d)\tvoid' : 'writeNumber($0)',
        'JSONGenerator.writeNumber(Integer i)\tvoid' : 'writeNumber($0)',
        'JSONGenerator.writeNumber(Long lng)\tvoid' : 'writeNumber($0)',
        'JSONGenerator.writeNumberField(String fieldName, Decimal d)\tvoid' : 'writeNumberField($0)',
        'JSONGenerator.writeNumberField(String fieldName, Double d)\tvoid' : 'writeNumberField($0)',
        'JSONGenerator.writeNumberField(String fieldName, Integer i)\tvoid' : 'writeNumberField($0)',
        'JSONGenerator.writeNumberField(String fieldName, Long lng)\tvoid' : 'writeNumberField($0)',
        'JSONGenerator.writeObject(Object o)\tvoid' : 'writeObject($0)',
        'JSONGenerator.writeObjectField(String fieldName, Object o)\tvoid' : 'writeObjectField($0)',
        'JSONGenerator.writeStartArray()\tvoid' : 'writeStartArray()$0',
        'JSONGenerator.writeStartObject()\tvoid' : 'writeStartObject()$0',
        'JSONGenerator.writeString(String str)\tvoid' : 'writeString($0)',
        'JSONGenerator.writeStringField(String fieldName, String str)\tvoid' : 'writeStringField($0)',
        'JSONGenerator.writeTime(Time t)\tvoid' : 'writeTime($0)',
        'JSONGenerator.writeTimeField(String fieldName, Time t)\tvoid' : 'writeTimeField($0)'
    },
    'JSONParser' : {
        'JSONParser.clearCurrentToken()\tvoid' : 'clearCurrentToken()$0',
        'JSONParser.getBlobValue()\tBlob' : 'getBlobValue()$0',
        'JSONParser.getBooleanValue()\tBoolean' : 'getBooleanValue()$0',
        'JSONParser.getCurrentName()\tString' : 'getCurrentName()$0',
        'JSONParser.getCurrentToken()\tsystem.JSONToken' : 'getCurrentToken()$0',
        'JSONParser.getDateTimeValue()\tDatetime' : 'getDateTimeValue()$0',
        'JSONParser.getDateValue()\tDate' : 'getDateValue()$0',
        'JSONParser.getDecimalValue()\tDecimal' : 'getDecimalValue()$0',
        'JSONParser.getDoubleValue()\tDouble' : 'getDoubleValue()$0',
        'JSONParser.getIdValue()\tId' : 'getIdValue()$0',
        'JSONParser.getIntegerValue()\tInteger' : 'getIntegerValue()$0',
        'JSONParser.getLastClearedToken()\tsystem.JSONToken' : 'getLastClearedToken()$0',
        'JSONParser.getLongValue()\tLong' : 'getLongValue()$0',
        'JSONParser.getText()\tString' : 'getText()$0',
        'JSONParser.getTimeValue()\tTime' : 'getTimeValue()$0',
        'JSONParser.hasCurrentToken()\tBoolean' : 'hasCurrentToken()$0',
        'JSONParser.nextToken()\tsystem.JSONToken' : 'nextToken()$0',
        'JSONParser.nextValue()\tsystem.JSONToken' : 'nextValue()$0',
        'JSONParser.readValueAs(system.Type apexType)\tObject' : 'readValueAs($0)',
        'JSONParser.readValueAsStrict(system.Type apexType)\tObject' : 'readValueAsStrict($0)',
        'JSONParser.skipChildren()\tvoid' : 'skipChildren()$0'
    },
    'JSONToken' : {
        'JSONToken.values()\tLIST<system.JSONToken>' : 'values()$0'
    },
    'KnowledgeArticleVersionStandardController' : {
        'KnowledgeArticleVersionStandardController.addFields(LIST<String> fieldNames)\tvoid' : 'addFields($0)',
        'KnowledgeArticleVersionStandardController.cancel()\tSystem.PageReference' : 'cancel()$0',
        'KnowledgeArticleVersionStandardController.delete()\tSystem.PageReference' : 'delete()$0',
        'KnowledgeArticleVersionStandardController.edit()\tSystem.PageReference' : 'edit()$0',
        'KnowledgeArticleVersionStandardController.getId()\tString' : 'getId()$0',
        'KnowledgeArticleVersionStandardController.getRecord()\tSObject' : 'getRecord()$0',
        'KnowledgeArticleVersionStandardController.getSourceId()\tString' : 'getSourceId()$0',
        'KnowledgeArticleVersionStandardController.getSubject()\tSObject' : 'getSubject()$0',
        'KnowledgeArticleVersionStandardController.reset()\tvoid' : 'reset()$0',
        'KnowledgeArticleVersionStandardController.save()\tSystem.PageReference' : 'save()$0',
        'KnowledgeArticleVersionStandardController.selectDataCategory(String categoryGroup, String category)\tvoid' : 'selectDataCategory($0)',
        'KnowledgeArticleVersionStandardController.view()\tSystem.PageReference' : 'view()$0'
    },
    'LIST' : {
        'LIST.add(ANY element)\tObject' : 'add($0)',
        'LIST.add(Integer index, ANY element)\tvoid' : 'add($0)',
        'LIST.addAll(LIST elements)\tvoid' : 'addAll($0)',
        'LIST.addAll(SET elements)\tvoid' : 'addAll($0)',
        'LIST.clear()\tvoid' : 'clear()$0',
        'LIST.clone()\tLIST<String>' : 'clone()$0',
        'LIST.deepClone()\tLIST<String>' : 'deepClone()$0',
        'LIST.deepClone(Boolean preserveId)\tLIST<String>' : 'deepClone($0)',
        'LIST.deepClone(Boolean preserveId, Boolean preserveReadOnlyTimestamps)\tLIST<String>' : 'deepClone($0)',
        'LIST.deepClone(Boolean preserveId, Boolean preserveReadOnlyTimestamps, Boolean preserveAutoNumbers)\tLIST<String>' : 'deepClone($0)',
        'LIST.get(Integer index)\tObject' : 'get($0)',
        'LIST.getSObjectType()\tSchema.SObjectType' : 'getSObjectType()$0',
        'LIST.isEmpty()\tBoolean' : 'isEmpty()$0',
        'LIST.iterator()\tsystem.ListIterator' : 'iterator()$0',
        'LIST.remove(Integer index)\tObject' : 'remove($0)',
        'LIST.set(Integer index, ANY value)\tvoid' : 'set($0)',
        'LIST.size()\tInteger' : 'size()$0',
        'LIST.sort()\tvoid' : 'sort()$0'
    },
    'LeadConvert' : {},
    'LicenseException' : {
        'LicenseException.getCause()\tException' : 'getCause()$0',
        'LicenseException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'LicenseException.getMessage()\tString' : 'getMessage()$0',
        'LicenseException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'LicenseException.getTypeName()\tString' : 'getTypeName()$0',
        'LicenseException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'LicenseException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'LimitException' : {
        'LimitException.getCause()\tException' : 'getCause()$0',
        'LimitException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'LimitException.getMessage()\tString' : 'getMessage()$0',
        'LimitException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'LimitException.getTypeName()\tString' : 'getTypeName()$0',
        'LimitException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'LimitException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'LinkAttachment' : {
        'LinkAttachment.equals(Object obj)\tBoolean' : 'equals($0)',
        'LinkAttachment.hashCode()\tInteger' : 'hashCode()$0',
        'LinkAttachment.toString()\tString' : 'toString()$0'
    },
    'LinkAttachmentInput' : {
        'LinkAttachmentInput.convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object' : 'convertToJavaObject($0)',
        'LinkAttachmentInput.equals(Object obj)\tBoolean' : 'equals($0)',
        'LinkAttachmentInput.hashCode()\tInteger' : 'hashCode()$0',
        'LinkAttachmentInput.toString()\tString' : 'toString()$0'
    },
    'LinkSegment' : {
        'LinkSegment.equals(Object obj)\tBoolean' : 'equals($0)',
        'LinkSegment.hashCode()\tInteger' : 'hashCode()$0',
        'LinkSegment.toString()\tString' : 'toString()$0'
    },
    'LinkSegmentInput' : {
        'LinkSegmentInput.convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object' : 'convertToJavaObject($0)',
        'LinkSegmentInput.equals(Object obj)\tBoolean' : 'equals($0)',
        'LinkSegmentInput.hashCode()\tInteger' : 'hashCode()$0',
        'LinkSegmentInput.toString()\tString' : 'toString()$0'
    },
    'ListException' : {
        'ListException.getCause()\tException' : 'getCause()$0',
        'ListException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'ListException.getMessage()\tString' : 'getMessage()$0',
        'ListException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'ListException.getTypeName()\tString' : 'getTypeName()$0',
        'ListException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'ListException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'LoggingLevel' : {
        'LoggingLevel.values()\tLIST<system.LoggingLevel>' : 'values()$0'
    },
    'Long' : {
        'Long.addError(APEX_OBJECT msg)\tvoid' : 'addError($0)',
        'Long.addError(APEX_OBJECT msg, Boolean escape)\tvoid' : 'addError($0)',
        'Long.addError(String msg)\tvoid' : 'addError($0)',
        'Long.addError(String msg, Boolean escape)\tvoid' : 'addError($0)',
        'Long.format()\tString' : 'format()$0',
        'Long.intValue()\tInteger' : 'intValue()$0',
        'Long.valueOf(String str)\tLong' : 'valueOf($0)'
    },
    'Map' : {
        'Map.clear()\tvoid' : 'clear()$0',
        'Map.clone()\tMAP<String,String>' : 'clone()$0',
        'Map.containsKey(ANY key)\tBoolean' : 'containsKey($0)',
        'Map.deepClone()\tMAP<String,String>' : 'deepClone()$0',
        'Map.get(ANY key)\tString' : 'get($0)',
        'Map.getSObjectType()\tSchema.SObjectType' : 'getSObjectType()$0',
        'Map.isEmpty()\tBoolean' : 'isEmpty()$0',
        'Map.keySet()\tSET<String>' : 'keySet()$0',
        'Map.put(ANY key, ANY value)\tString' : 'put($0)',
        'Map.putAll(LIST entries)\tvoid' : 'putAll($0)',
        'Map.putAll(MAP entries)\tvoid' : 'putAll($0)',
        'Map.remove(ANY key)\tString' : 'remove($0)',
        'Map.size()\tInteger' : 'size()$0',
        'Map.values()\tLIST<String>' : 'values()$0'
    },
    'MassEmailMessage' : {},
    'Matcher' : {
        'Matcher.end()\tInteger' : 'end()$0',
        'Matcher.end(Integer grp)\tInteger' : 'end($0)',
        'Matcher.find()\tBoolean' : 'find()$0',
        'Matcher.find(Integer start)\tBoolean' : 'find($0)',
        'Matcher.group()\tString' : 'group()$0',
        'Matcher.group(Integer start)\tString' : 'group($0)',
        'Matcher.groupCount()\tInteger' : 'groupCount()$0',
        'Matcher.hasAnchoringBounds()\tBoolean' : 'hasAnchoringBounds()$0',
        'Matcher.hasTransparentBounds()\tBoolean' : 'hasTransparentBounds()$0',
        'Matcher.hitEnd()\tBoolean' : 'hitEnd()$0',
        'Matcher.lookingAt()\tBoolean' : 'lookingAt()$0',
        'Matcher.matches()\tBoolean' : 'matches()$0',
        'Matcher.pattern()\tsystem.Pattern' : 'pattern()$0',
        'Matcher.quoteReplacement(String s)\tString' : 'quoteReplacement($0)',
        'Matcher.region(Integer start, Integer ending)\tsystem.Matcher' : 'region($0)',
        'Matcher.regionEnd()\tInteger' : 'regionEnd()$0',
        'Matcher.regionStart()\tInteger' : 'regionStart()$0',
        'Matcher.replaceAll(String replacement)\tString' : 'replaceAll($0)',
        'Matcher.replaceFirst(String replacement)\tString' : 'replaceFirst($0)',
        'Matcher.requireEnd()\tBoolean' : 'requireEnd()$0',
        'Matcher.reset()\tsystem.Matcher' : 'reset()$0',
        'Matcher.reset(String input)\tsystem.Matcher' : 'reset($0)',
        'Matcher.start()\tInteger' : 'start()$0',
        'Matcher.start(Integer grp)\tInteger' : 'start($0)',
        'Matcher.useAnchoringBounds(Boolean b)\tsystem.Matcher' : 'useAnchoringBounds($0)',
        'Matcher.usePattern(system.Pattern p)\tsystem.Matcher' : 'usePattern($0)',
        'Matcher.useTransparentBounds(Boolean b)\tsystem.Matcher' : 'useTransparentBounds($0)'
    },
    'Math' : {
        'Math.abs(Decimal x)\tDecimal' : 'abs($0)',
        'Math.abs(Double x)\tDouble' : 'abs($0)',
        'Math.abs(Integer x)\tInteger' : 'abs($0)',
        'Math.abs(Long x)\tLong' : 'abs($0)',
        'Math.acos(Decimal x)\tDecimal' : 'acos($0)',
        'Math.acos(Double x)\tDouble' : 'acos($0)',
        'Math.asin(Decimal x)\tDecimal' : 'asin($0)',
        'Math.asin(Double x)\tDouble' : 'asin($0)',
        'Math.atan(Decimal x)\tDecimal' : 'atan($0)',
        'Math.atan(Double x)\tDouble' : 'atan($0)',
        'Math.atan2(Decimal x, Decimal y)\tDecimal' : 'atan2($0)',
        'Math.atan2(Double x, Double y)\tDouble' : 'atan2($0)',
        'Math.cbrt(Decimal x)\tDecimal' : 'cbrt($0)',
        'Math.cbrt(Double x)\tDouble' : 'cbrt($0)',
        'Math.ceil(Decimal x)\tDecimal' : 'ceil($0)',
        'Math.ceil(Double x)\tDouble' : 'ceil($0)',
        'Math.cos(Decimal x)\tDecimal' : 'cos($0)',
        'Math.cos(Double x)\tDouble' : 'cos($0)',
        'Math.cosh(Decimal x)\tDecimal' : 'cosh($0)',
        'Math.cosh(Double x)\tDouble' : 'cosh($0)',
        'Math.exp(Decimal x)\tDecimal' : 'exp($0)',
        'Math.exp(Double x)\tDouble' : 'exp($0)',
        'Math.floor(Decimal x)\tDecimal' : 'floor($0)',
        'Math.floor(Double x)\tDouble' : 'floor($0)',
        'Math.log(Decimal x)\tDecimal' : 'log($0)',
        'Math.log(Double x)\tDouble' : 'log($0)',
        'Math.log10(Decimal x)\tDecimal' : 'log10($0)',
        'Math.log10(Double x)\tDouble' : 'log10($0)',
        'Math.max(Decimal x, Decimal y)\tDecimal' : 'max($0)',
        'Math.max(Double x, Double y)\tDouble' : 'max($0)',
        'Math.max(Integer x, Integer y)\tInteger' : 'max($0)',
        'Math.max(Long x, Long y)\tLong' : 'max($0)',
        'Math.min(Decimal x, Decimal y)\tDecimal' : 'min($0)',
        'Math.min(Double x, Double y)\tDouble' : 'min($0)',
        'Math.min(Integer x, Integer y)\tInteger' : 'min($0)',
        'Math.min(Long x, Long y)\tLong' : 'min($0)',
        'Math.mod(Integer x, Integer y)\tInteger' : 'mod($0)',
        'Math.mod(Long x, Long y)\tLong' : 'mod($0)',
        'Math.pow(Double base, Double exp)\tDouble' : 'pow($0)',
        'Math.random()\tDouble' : 'random()$0',
        'Math.rint(Decimal x)\tDecimal' : 'rint($0)',
        'Math.rint(Double x)\tDouble' : 'rint($0)',
        'Math.round(Decimal x)\tInteger' : 'round($0)',
        'Math.round(Double x)\tInteger' : 'round($0)',
        'Math.roundToLong(Decimal x)\tLong' : 'roundToLong($0)',
        'Math.roundToLong(Double x)\tLong' : 'roundToLong($0)',
        'Math.signum(Decimal x)\tDecimal' : 'signum($0)',
        'Math.signum(Double x)\tDouble' : 'signum($0)',
        'Math.sin(Decimal x)\tDecimal' : 'sin($0)',
        'Math.sin(Double x)\tDouble' : 'sin($0)',
        'Math.sinh(Decimal x)\tDecimal' : 'sinh($0)',
        'Math.sinh(Double x)\tDouble' : 'sinh($0)',
        'Math.sqrt(Decimal x)\tDecimal' : 'sqrt($0)',
        'Math.sqrt(Double x)\tDouble' : 'sqrt($0)',
        'Math.tan(Decimal x)\tDecimal' : 'tan($0)',
        'Math.tan(Double x)\tDouble' : 'tan($0)',
        'Math.tanh(Decimal x)\tDecimal' : 'tanh($0)',
        'Math.tanh(Double x)\tDouble' : 'tanh($0)'
    },
    'MathException' : {
        'MathException.getCause()\tException' : 'getCause()$0',
        'MathException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'MathException.getMessage()\tString' : 'getMessage()$0',
        'MathException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'MathException.getTypeName()\tString' : 'getTypeName()$0',
        'MathException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'MathException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'MentionSegment' : {
        'MentionSegment.equals(Object obj)\tBoolean' : 'equals($0)',
        'MentionSegment.hashCode()\tInteger' : 'hashCode()$0',
        'MentionSegment.toString()\tString' : 'toString()$0'
    },
    'MentionSegmentInput' : {
        'MentionSegmentInput.convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object' : 'convertToJavaObject($0)',
        'MentionSegmentInput.equals(Object obj)\tBoolean' : 'equals($0)',
        'MentionSegmentInput.hashCode()\tInteger' : 'hashCode()$0',
        'MentionSegmentInput.toString()\tString' : 'toString()$0'
    },
    'Message' : {
        'Message.getComponentLabel()\tString' : 'getComponentLabel()$0',
        'Message.getDetail()\tString' : 'getDetail()$0',
        'Message.getSeverity()\tApexPages.Severity' : 'getSeverity()$0',
        'Message.getSummary()\tString' : 'getSummary()$0'
    },
    'MessageBody' : {
        'MessageBody.equals(Object obj)\tBoolean' : 'equals($0)',
        'MessageBody.hashCode()\tInteger' : 'hashCode()$0',
        'MessageBody.toString()\tString' : 'toString()$0'
    },
    'MessageBodyInput' : {
        'MessageBodyInput.convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object' : 'convertToJavaObject($0)',
        'MessageBodyInput.equals(Object obj)\tBoolean' : 'equals($0)',
        'MessageBodyInput.hashCode()\tInteger' : 'hashCode()$0',
        'MessageBodyInput.toString()\tString' : 'toString()$0'
    },
    'MessageSegment' : {
        'MessageSegment.equals(Object obj)\tBoolean' : 'equals($0)',
        'MessageSegment.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'MessageSegment.hashCode()\tInteger' : 'hashCode()$0',
        'MessageSegment.toString()\tString' : 'toString()$0'
    },
    'MessageSegmentInput' : {
        'MessageSegmentInput.convertToJavaObject(java:common.api.AppVersion param1)\tjava:java.lang.Object' : 'convertToJavaObject($0)',
        'MessageSegmentInput.equals(Object obj)\tBoolean' : 'equals($0)',
        'MessageSegmentInput.hashCode()\tInteger' : 'hashCode()$0',
        'MessageSegmentInput.toString()\tString' : 'toString()$0'
    },
    'MessageSegmentType' : {
        'MessageSegmentType.values()\tLIST<ConnectApi.MessageSegmentType>' : 'values()$0'
    },
    'Messaging' : {
        'Messaging.reserveMassEmailCapacity(Integer count)\tvoid' : 'reserveMassEmailCapacity($0)',
        'Messaging.reserveSingleEmailCapacity(Integer count)\tvoid' : 'reserveSingleEmailCapacity($0)',
        'Messaging.sendEmail(LIST<Messaging.Email> emailMessages)\tLIST<Messaging.SendEmailResult>' : 'sendEmail($0)',
        'Messaging.sendEmail(LIST<Messaging.Email> emailMessages, Boolean allOrNothing)\tLIST<Messaging.SendEmailResult>' : 'sendEmail($0)',
        'Messaging.sendEmailMessage(LIST<Id> emailMessagesIds)\tLIST<Messaging.SendEmailResult>' : 'sendEmailMessage($0)',
        'Messaging.sendEmailMessage(LIST<Id> emailMessagesIds, Boolean allOrNothing)\tLIST<Messaging.SendEmailResult>' : 'sendEmailMessage($0)'
    },
    'MobilePushNotification' : {
        'MobilePushNotification.send(String application, SET<String> users)\tvoid' : 'send($0)',
        'MobilePushNotification.setPayload(MAP<String,ANY> payload)\tvoid' : 'setPayload($0)',
        'MobilePushNotification.setTtl(Integer ttl)\tvoid' : 'setTtl($0)'
    },
    'MobilePushPayload' : {
        'MobilePushPayload.apple(String alert, String sound, Integer badgeCount, MAP<String,ANY> userData)\tMAP<String,ANY>' : 'apple($0)',
        'MobilePushPayload.apple(String alertBody, String actionLocKey, String locKey, LIST<String> locArgs, String launchImage, String sound, Integer badgeCount, MAP<String,ANY> userData)\tMAP<String,ANY>' : 'apple($0)'
    },
    'MoreChangesSegment' : {
        'MoreChangesSegment.equals(Object obj)\tBoolean' : 'equals($0)',
        'MoreChangesSegment.hashCode()\tInteger' : 'hashCode()$0',
        'MoreChangesSegment.toString()\tString' : 'toString()$0'
    },
    'Motif' : {
        'Motif.equals(Object obj)\tBoolean' : 'equals($0)',
        'Motif.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'Motif.hashCode()\tInteger' : 'hashCode()$0',
        'Motif.toString()\tString' : 'toString()$0'
    },
    'MultiStaticResourceCalloutMock' : {
        'MultiStaticResourceCalloutMock.respond(System.HttpRequest request)\tSystem.HttpResponse' : 'respond($0)',
        'MultiStaticResourceCalloutMock.setHeader(String key, String val)\tvoid' : 'setHeader($0)',
        'MultiStaticResourceCalloutMock.setStaticResource(String url, String staticResourceName)\tvoid' : 'setStaticResource($0)',
        'MultiStaticResourceCalloutMock.setStatus(String status)\tvoid' : 'setStatus($0)',
        'MultiStaticResourceCalloutMock.setStatusCode(Integer code)\tvoid' : 'setStatusCode($0)'
    },
    'Network' : {
        'Network.communitiesLanding()\tSystem.PageReference' : 'communitiesLanding()$0',
        'Network.forwardToAuthPage(String startUrl)\tSystem.PageReference' : 'forwardToAuthPage($0)',
        'Network.forwardToAuthPage(String startUrl, String displayType)\tSystem.PageReference' : 'forwardToAuthPage($0)',
        'Network.getNetworkId()\tString' : 'getNetworkId()$0'
    },
    'NewFileAttachmentInput' : {
        'NewFileAttachmentInput.convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object' : 'convertToJavaObject($0)',
        'NewFileAttachmentInput.equals(Object obj)\tBoolean' : 'equals($0)',
        'NewFileAttachmentInput.hashCode()\tInteger' : 'hashCode()$0',
        'NewFileAttachmentInput.toString()\tString' : 'toString()$0'
    },
    'NoAccessException' : {
        'NoAccessException.getCause()\tException' : 'getCause()$0',
        'NoAccessException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'NoAccessException.getMessage()\tString' : 'getMessage()$0',
        'NoAccessException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'NoAccessException.getTypeName()\tString' : 'getTypeName()$0',
        'NoAccessException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'NoAccessException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'NoDataFoundException' : {
        'NoDataFoundException.getCause()\tException' : 'getCause()$0',
        'NoDataFoundException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'NoDataFoundException.getMessage()\tString' : 'getMessage()$0',
        'NoDataFoundException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'NoDataFoundException.getTypeName()\tString' : 'getTypeName()$0',
        'NoDataFoundException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'NoDataFoundException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'NoSuchElementException' : {
        'NoSuchElementException.getCause()\tException' : 'getCause()$0',
        'NoSuchElementException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'NoSuchElementException.getMessage()\tString' : 'getMessage()$0',
        'NoSuchElementException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'NoSuchElementException.getTypeName()\tString' : 'getTypeName()$0',
        'NoSuchElementException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'NoSuchElementException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'NotFoundException' : {
        'NotFoundException.getTypeName()\tString' : 'getTypeName()$0'
    },
    'NullPointerException' : {
        'NullPointerException.getCause()\tException' : 'getCause()$0',
        'NullPointerException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'NullPointerException.getMessage()\tString' : 'getMessage()$0',
        'NullPointerException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'NullPointerException.getTypeName()\tString' : 'getTypeName()$0',
        'NullPointerException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'NullPointerException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'Organization' : {
        'Organization.getSettings()\tConnectApi.OrganizationSettings' : 'getSettings()$0'
    },
    'OrganizationSettings' : {
        'OrganizationSettings.equals(Object obj)\tBoolean' : 'equals($0)',
        'OrganizationSettings.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'OrganizationSettings.hashCode()\tInteger' : 'hashCode()$0',
        'OrganizationSettings.toString()\tString' : 'toString()$0'
    },
    'OutputParameter' : {},
    'PageReference' : {
        'PageReference.getAnchor()\tString' : 'getAnchor()$0',
        'PageReference.getContent()\tBlob' : 'getContent()$0',
        'PageReference.getContentAsPDF()\tBlob' : 'getContentAsPDF()$0',
        'PageReference.getCookies()\tMAP<String,System.Cookie>' : 'getCookies()$0',
        'PageReference.getHeaders()\tMAP<String,String>' : 'getHeaders()$0',
        'PageReference.getParameters()\tMAP<String,String>' : 'getParameters()$0',
        'PageReference.getRedirect()\tBoolean' : 'getRedirect()$0',
        'PageReference.getUrl()\tString' : 'getUrl()$0',
        'PageReference.setAnchor(String anchor)\tSystem.PageReference' : 'setAnchor($0)',
        'PageReference.setCookies(LIST<System.Cookie> cookies)\tvoid' : 'setCookies($0)',
        'PageReference.setRedirect(Boolean redirect)\tSystem.PageReference' : 'setRedirect($0)'
    },
    'ParameterType' : {
        'ParameterType.values()\tLIST<Process.PluginDescribeResult.ParameterType>' : 'values()$0'
    },
    'Pattern' : {
        'Pattern.compile(String regex)\tsystem.Pattern' : 'compile($0)',
        'Pattern.matcher(String input)\tsystem.Matcher' : 'matcher($0)',
        'Pattern.matches(String regex, String input)\tBoolean' : 'matches($0)',
        'Pattern.pattern()\tString' : 'pattern()$0',
        'Pattern.quote(String s)\tString' : 'quote($0)',
        'Pattern.split(String input)\tLIST<String>' : 'split($0)',
        'Pattern.split(String input, Integer n)\tLIST<String>' : 'split($0)'
    },
    'PhoneNumber' : {
        'PhoneNumber.equals(Object obj)\tBoolean' : 'equals($0)',
        'PhoneNumber.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'PhoneNumber.hashCode()\tInteger' : 'hashCode()$0',
        'PhoneNumber.toString()\tString' : 'toString()$0'
    },
    'Photo' : {
        'Photo.equals(Object obj)\tBoolean' : 'equals($0)',
        'Photo.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'Photo.hashCode()\tInteger' : 'hashCode()$0',
        'Photo.toString()\tString' : 'toString()$0'
    },
    'Plugin' : {
        'Plugin.describe()\tProcess.PluginDescribeResult' : 'describe()$0',
        'Plugin.invoke(Process.PluginRequest param1)\tProcess.PluginResult' : 'invoke($0)'
    },
    'PluginDescribeResult' : {},
    'PluginRequest' : {},
    'PluginResult' : {},
    'PollAttachmentInput' : {
        'PollAttachmentInput.convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object' : 'convertToJavaObject($0)',
        'PollAttachmentInput.equals(Object obj)\tBoolean' : 'equals($0)',
        'PollAttachmentInput.hashCode()\tInteger' : 'hashCode()$0',
        'PollAttachmentInput.toString()\tString' : 'toString()$0'
    },
    'ProcedureException' : {
        'ProcedureException.getCause()\tException' : 'getCause()$0',
        'ProcedureException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'ProcedureException.getMessage()\tString' : 'getMessage()$0',
        'ProcedureException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'ProcedureException.getTypeName()\tString' : 'getTypeName()$0',
        'ProcedureException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'ProcedureException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'PublishingService' : {
        'PublishingService.archiveOnlineArticle(String articleId, Datetime scheduledDate)\tvoid' : 'archiveOnlineArticle($0)',
        'PublishingService.assignDraftArticleTask(String articleId, String assigneeId, String instructions, Datetime dueDate, Boolean sendEmailNotification)\tvoid' : 'assignDraftArticleTask($0)',
        'PublishingService.assignDraftTranslationTask(String translationVersionId, String assigneeId, String instructions, Datetime dueDate, Boolean sendEmailNotification)\tvoid' : 'assignDraftTranslationTask($0)',
        'PublishingService.cancelScheduledArchivingOfArticle(String articleId)\tvoid' : 'cancelScheduledArchivingOfArticle($0)',
        'PublishingService.cancelScheduledPublicationOfArticle(String articleId)\tvoid' : 'cancelScheduledPublicationOfArticle($0)',
        'PublishingService.completeTranslation(String articleVersionId)\tvoid' : 'completeTranslation($0)',
        'PublishingService.deleteArchivedArticle(String articleId)\tvoid' : 'deleteArchivedArticle($0)',
        'PublishingService.deleteArchivedArticleVersion(String articleId, Integer versionNumber)\tvoid' : 'deleteArchivedArticleVersion($0)',
        'PublishingService.deleteDraftArticle(String articleId)\tvoid' : 'deleteDraftArticle($0)',
        'PublishingService.deleteDraftTranslation(String articleVersionId)\tvoid' : 'deleteDraftTranslation($0)',
        'PublishingService.editArchivedArticle(String articleId)\tString' : 'editArchivedArticle($0)',
        'PublishingService.editOnlineArticle(String articleId, Boolean unpublish)\tString' : 'editOnlineArticle($0)',
        'PublishingService.editPublishedTranslation(String articleId, String language, Boolean unpublish)\tString' : 'editPublishedTranslation($0)',
        'PublishingService.publishArticle(String articleId, Boolean flagAsNew)\tvoid' : 'publishArticle($0)',
        'PublishingService.restoreOldVersion(String articleId, Integer versionNumber)\tString' : 'restoreOldVersion($0)',
        'PublishingService.scheduleForPublication(String articleId, Datetime scheduledDate)\tvoid' : 'scheduleForPublication($0)',
        'PublishingService.setTranslationToIncomplete(String articleVersionId)\tvoid' : 'setTranslationToIncomplete($0)',
        'PublishingService.submitForTranslation(String articleId, String language, String assigneeId, Datetime dueDate)\tString' : 'submitForTranslation($0)'
    },
    'QueryException' : {
        'QueryException.getCause()\tException' : 'getCause()$0',
        'QueryException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'QueryException.getMessage()\tString' : 'getMessage()$0',
        'QueryException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'QueryException.getTypeName()\tString' : 'getTypeName()$0',
        'QueryException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'QueryException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'QueryLocator' : {
        'QueryLocator.getQuery()\tString' : 'getQuery()$0',
        'QueryLocator.iterator()\tDatabase.QueryLocatorIterator' : 'iterator()$0'
    },
    'QueryLocatorChunkIterator' : {
        'QueryLocatorChunkIterator.hasNext()\tBoolean' : 'hasNext()$0',
        'QueryLocatorChunkIterator.next()\tLIST<SObject>' : 'next()$0'
    },
    'QueryLocatorIterator' : {
        'QueryLocatorIterator.hasNext()\tBoolean' : 'hasNext()$0',
        'QueryLocatorIterator.next()\tSObject' : 'next()$0'
    },
    'RateLimitException' : {
        'RateLimitException.getErrorCode()\tString' : 'getErrorCode()$0',
        'RateLimitException.getTypeName()\tString' : 'getTypeName()$0'
    },
    'RecordSummary' : {
        'RecordSummary.equals(Object obj)\tBoolean' : 'equals($0)',
        'RecordSummary.hashCode()\tInteger' : 'hashCode()$0',
        'RecordSummary.toString()\tString' : 'toString()$0'
    },
    'Records' : {
        'Records.getMotif(String communityId, String idOrPrefix)\tConnectApi.Motif' : 'getMotif($0)'
    },
    'Reference' : {
        'Reference.equals(Object obj)\tBoolean' : 'equals($0)',
        'Reference.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'Reference.hashCode()\tInteger' : 'hashCode()$0',
        'Reference.toString()\tString' : 'toString()$0'
    },
    'RequiredFeatureMissingException' : {
        'RequiredFeatureMissingException.getCause()\tException' : 'getCause()$0',
        'RequiredFeatureMissingException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'RequiredFeatureMissingException.getMessage()\tString' : 'getMessage()$0',
        'RequiredFeatureMissingException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'RequiredFeatureMissingException.getTypeName()\tString' : 'getTypeName()$0',
        'RequiredFeatureMissingException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'RequiredFeatureMissingException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'ResourceLinkSegment' : {
        'ResourceLinkSegment.equals(Object obj)\tBoolean' : 'equals($0)',
        'ResourceLinkSegment.hashCode()\tInteger' : 'hashCode()$0',
        'ResourceLinkSegment.toString()\tString' : 'toString()$0'
    },
    'RestContext' : {},
    'RestRequest' : {
        'RestRequest.addHeader(String name, String value)\tvoid' : 'addHeader($0)',
        'RestRequest.addParameter(String name, String value)\tvoid' : 'addParameter($0)'
    },
    'RestResponse' : {
        'RestResponse.addHeader(String name, String value)\tvoid' : 'addHeader($0)'
    },
    'SObject' : {
        'SObject.addError(APEX_OBJECT msg)\tvoid' : 'addError($0)',
        'SObject.addError(APEX_OBJECT msg, Boolean escape)\tvoid' : 'addError($0)',
        'SObject.addError(String msg)\tvoid' : 'addError($0)',
        'SObject.addError(String msg, Boolean escape)\tvoid' : 'addError($0)',
        'SObject.clear()\tvoid' : 'clear()$0',
        'SObject.clone()\tSObject' : 'clone()$0',
        'SObject.clone(Boolean preserveId)\tSObject' : 'clone($0)',
        'SObject.clone(Boolean preserveId, Boolean deep)\tSObject' : 'clone($0)',
        'SObject.clone(Boolean preserveId, Boolean deep, Boolean preserveReadOnlyTimestamps)\tSObject' : 'clone($0)',
        'SObject.clone(Boolean preserveId, Boolean deep, Boolean preserveReadOnlyTimestamps, Boolean preserveAutoNumbers)\tSObject' : 'clone($0)',
        'SObject.get(Schema.SObjectField field)\tObject' : 'get($0)',
        'SObject.get(String field)\tObject' : 'get($0)',
        'SObject.getOptions()\tDatabase.DMLOptions' : 'getOptions()$0',
        'SObject.getQuickActionName()\tString' : 'getQuickActionName()$0',
        'SObject.getSObject(Schema.SObjectField field)\tSObject' : 'getSObject($0)',
        'SObject.getSObject(String field)\tSObject' : 'getSObject($0)',
        'SObject.getSObjectType()\tSchema.SObjectType' : 'getSObjectType()$0',
        'SObject.getSObjects(Schema.SObjectField field)\tLIST<SObject>' : 'getSObjects($0)',
        'SObject.getSObjects(String field)\tLIST<SObject>' : 'getSObjects($0)',
        'SObject.put(Schema.SObjectField field, Object value)\tObject' : 'put($0)',
        'SObject.put(String field, Object value)\tObject' : 'put($0)',
        'SObject.putSObject(Schema.SObjectField field, SObject value)\tSObject' : 'putSObject($0)',
        'SObject.putSObject(String field, SObject value)\tSObject' : 'putSObject($0)',
        'SObject.setOptions(APEX_OBJECT options)\tvoid' : 'setOptions($0)'
    },
    'SObjectException' : {
        'SObjectException.getCause()\tException' : 'getCause()$0',
        'SObjectException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'SObjectException.getMessage()\tString' : 'getMessage()$0',
        'SObjectException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'SObjectException.getTypeName()\tString' : 'getTypeName()$0',
        'SObjectException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'SObjectException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'SObjectField' : {
        'SObjectField.getDescribe()\tSchema.DescribeFieldResult' : 'getDescribe()$0'
    },
    'SObjectType' : {
        'SObjectType.getDescribe()\tSchema.DescribeSObjectResult' : 'getDescribe()$0',
        'SObjectType.newSObject()\tSObject' : 'newSObject()$0',
        'SObjectType.newSObject(Id id)\tSObject' : 'newSObject($0)',
        'SObjectType.newSObject(Id recordTypeId, Boolean loadDefaultValues)\tSObject' : 'newSObject($0)'
    },
    'Schedulable' : {
        'Schedulable.execute(system.SchedulableContext param1)\tvoid' : 'execute($0)'
    },
    'SchedulableContext' : {
        'SchedulableContext.getTriggerId()\tId' : 'getTriggerId()$0'
    },
    'Schema' : {
        'Schema.describeDataCategoryGroupStructures(LIST<Schema.DataCategoryGroupSobjectTypePair> pairs, Boolean topCategoriesOnly)\tLIST<Schema.DescribeDataCategoryGroupStructureResult>' : 'describeDataCategoryGroupStructures($0)',
        'Schema.describeDataCategoryGroups(LIST<String> sobjects)\tLIST<Schema.DescribeDataCategoryGroupResult>' : 'describeDataCategoryGroups($0)',
        'Schema.getAppDescribe(String appName)\tMAP<String,Schema.SObjectType>' : 'getAppDescribe($0)',
        'Schema.getGlobalDescribe()\tMAP<String,Schema.SObjectType>' : 'getGlobalDescribe()$0',
        'Schema.getModuleDescribe()\tMAP<String,Schema.SObjectType>' : 'getModuleDescribe()$0',
        'Schema.getModuleDescribe(String moduleName)\tMAP<String,Schema.SObjectType>' : 'getModuleDescribe($0)'
    },
    'SearchException' : {
        'SearchException.getCause()\tException' : 'getCause()$0',
        'SearchException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'SearchException.getMessage()\tString' : 'getMessage()$0',
        'SearchException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'SearchException.getTypeName()\tString' : 'getTypeName()$0',
        'SearchException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'SearchException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'SecurityException' : {
        'SecurityException.getCause()\tException' : 'getCause()$0',
        'SecurityException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'SecurityException.getMessage()\tString' : 'getMessage()$0',
        'SecurityException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'SecurityException.getTypeName()\tString' : 'getTypeName()$0',
        'SecurityException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'SecurityException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'SelectOption' : {
        'SelectOption.getDisabled()\tBoolean' : 'getDisabled()$0',
        'SelectOption.getEscapeItem()\tBoolean' : 'getEscapeItem()$0',
        'SelectOption.getLabel()\tString' : 'getLabel()$0',
        'SelectOption.getValue()\tString' : 'getValue()$0',
        'SelectOption.setDisabled(Boolean disabled)\tvoid' : 'setDisabled($0)',
        'SelectOption.setEscapeItem(Boolean disabled)\tvoid' : 'setEscapeItem($0)',
        'SelectOption.setLabel(String label)\tvoid' : 'setLabel($0)',
        'SelectOption.setValue(String value)\tvoid' : 'setValue($0)'
    },
    'SerializationException' : {
        'SerializationException.getCause()\tException' : 'getCause()$0',
        'SerializationException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'SerializationException.getMessage()\tString' : 'getMessage()$0',
        'SerializationException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'SerializationException.getTypeName()\tString' : 'getTypeName()$0',
        'SerializationException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'SerializationException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'Set' : {
        'Set.add(ANY element)\tBoolean' : 'add($0)',
        'Set.addAll(LIST elements)\tBoolean' : 'addAll($0)',
        'Set.addAll(SET elements)\tBoolean' : 'addAll($0)',
        'Set.clear()\tvoid' : 'clear()$0',
        'Set.clone()\tSET<String>' : 'clone()$0',
        'Set.contains(ANY element)\tBoolean' : 'contains($0)',
        'Set.containsAll(LIST elements)\tBoolean' : 'containsAll($0)',
        'Set.containsAll(SET elements)\tBoolean' : 'containsAll($0)',
        'Set.isEmpty()\tBoolean' : 'isEmpty()$0',
        'Set.iterator()\tsystem.ListIterator' : 'iterator()$0',
        'Set.remove(ANY element)\tBoolean' : 'remove($0)',
        'Set.removeAll(LIST elements)\tBoolean' : 'removeAll($0)',
        'Set.removeAll(SET elements)\tBoolean' : 'removeAll($0)',
        'Set.retainAll(LIST elements)\tBoolean' : 'retainAll($0)',
        'Set.retainAll(SET elements)\tBoolean' : 'retainAll($0)',
        'Set.size()\tInteger' : 'size()$0'
    },
    'SetupScope' : {
        'SetupScope.values()\tLIST<system.SetupScope>' : 'values()$0'
    },
    'Severity' : {
        'Severity.values()\tLIST<ApexPages.Severity>' : 'values()$0'
    },
    'SingleEmailMessage' : {},
    'Site' : {
        'Site.changePassword(String newPassword, String verifyNewPassword)\tSystem.PageReference' : 'changePassword($0)',
        'Site.changePassword(String newPassword, String verifyNewPassword, String oldPassword)\tSystem.PageReference' : 'changePassword($0)',
        'Site.createPersonAccountPortalUser(SObject user, String ownerId, String password)\tId' : 'createPersonAccountPortalUser($0)',
        'Site.createPersonAccountPortalUser(SObject user, String ownerId, String recordTypeId, String password)\tId' : 'createPersonAccountPortalUser($0)',
        'Site.createPortalUser(SObject user, String accountId)\tId' : 'createPortalUser($0)',
        'Site.createPortalUser(SObject user, String accountId, String password)\tId' : 'createPortalUser($0)',
        'Site.createPortalUser(SObject user, String accountId, String password, Boolean sendEmailConfirmation)\tId' : 'createPortalUser($0)',
        'Site.forgotPassword(String username)\tBoolean' : 'forgotPassword($0)',
        'Site.getAdminEmail()\tString' : 'getAdminEmail()$0',
        'Site.getAdminId()\tId' : 'getAdminId()$0',
        'Site.getAnalyticsTrackingCode()\tString' : 'getAnalyticsTrackingCode()$0',
        'Site.getCurrentSiteUrl()\tString' : 'getCurrentSiteUrl()$0',
        'Site.getCustomWebAddress()\tString' : 'getCustomWebAddress()$0',
        'Site.getDomain()\tString' : 'getDomain()$0',
        'Site.getErrorDescription()\tString' : 'getErrorDescription()$0',
        'Site.getErrorMessage()\tString' : 'getErrorMessage()$0',
        'Site.getName()\tString' : 'getName()$0',
        'Site.getOriginalUrl()\tString' : 'getOriginalUrl()$0',
        'Site.getPrefix()\tString' : 'getPrefix()$0',
        'Site.getTemplate()\tSystem.PageReference' : 'getTemplate()$0',
        'Site.isLoginEnabled()\tBoolean' : 'isLoginEnabled()$0',
        'Site.isPasswordExpired()\tBoolean' : 'isPasswordExpired()$0',
        'Site.isRegistrationEnabled()\tBoolean' : 'isRegistrationEnabled()$0',
        'Site.login(String username, String password, String startUrl)\tSystem.PageReference' : 'login($0)',
        'Site.setPortalUserAsAuthProvider(SObject user, String accountId)\tvoid' : 'setPortalUserAsAuthProvider($0)'
    },
    'SoapType' : {
        'SoapType.values()\tLIST<Schema.SoapType>' : 'values()$0'
    },
    'SparkPlugApi' : {
        'SparkPlugApi.describePlugin(String className)\tProcess.SparkPlugApi.SparkPlugDescribeResult' : 'describePlugin($0)',
        'SparkPlugApi.describePlugins()\tLIST<Process.SparkPlugApi.SparkPlugDescribeResult>' : 'describePlugins()$0',
        'SparkPlugApi.invokePluginWithJson(String className, String parameters)\tString' : 'invokePluginWithJson($0)'
    },
    'SparkPlugDescribeResult' : {},
    'SparkPlugParameter' : {},
    'Stack' : {
        'Stack.empty()\tBoolean' : 'empty()$0',
        'Stack.peek()\tString' : 'peek()$0',
        'Stack.pop()\tString' : 'pop()$0',
        'Stack.push(String item)\tvoid' : 'push($0)'
    },
    'StandardController' : {
        'StandardController.addFields(LIST<String> fieldNames)\tvoid' : 'addFields($0)',
        'StandardController.cancel()\tSystem.PageReference' : 'cancel()$0',
        'StandardController.delete()\tSystem.PageReference' : 'delete()$0',
        'StandardController.edit()\tSystem.PageReference' : 'edit()$0',
        'StandardController.getId()\tString' : 'getId()$0',
        'StandardController.getRecord()\tSObject' : 'getRecord()$0',
        'StandardController.getSubject()\tSObject' : 'getSubject()$0',
        'StandardController.reset()\tvoid' : 'reset()$0',
        'StandardController.save()\tSystem.PageReference' : 'save()$0',
        'StandardController.view()\tSystem.PageReference' : 'view()$0'
    },
    'StandardSetController' : {
        'StandardSetController.addFields(LIST<String> fieldNames)\tvoid' : 'addFields($0)',
        'StandardSetController.cancel()\tSystem.PageReference' : 'cancel()$0',
        'StandardSetController.first()\tvoid' : 'first()$0',
        'StandardSetController.getCompleteResult()\tBoolean' : 'getCompleteResult()$0',
        'StandardSetController.getFilterId()\tString' : 'getFilterId()$0',
        'StandardSetController.getHasNext()\tBoolean' : 'getHasNext()$0',
        'StandardSetController.getHasPrevious()\tBoolean' : 'getHasPrevious()$0',
        'StandardSetController.getListViewOptions()\tLIST<System.SelectOption>' : 'getListViewOptions()$0',
        'StandardSetController.getPageNumber()\tInteger' : 'getPageNumber()$0',
        'StandardSetController.getPageSize()\tInteger' : 'getPageSize()$0',
        'StandardSetController.getRecord()\tSObject' : 'getRecord()$0',
        'StandardSetController.getRecords()\tLIST<SObject>' : 'getRecords()$0',
        'StandardSetController.getResultSize()\tInteger' : 'getResultSize()$0',
        'StandardSetController.getSelected()\tLIST<SObject>' : 'getSelected()$0',
        'StandardSetController.last()\tvoid' : 'last()$0',
        'StandardSetController.next()\tvoid' : 'next()$0',
        'StandardSetController.previous()\tvoid' : 'previous()$0',
        'StandardSetController.reset()\tvoid' : 'reset()$0',
        'StandardSetController.save()\tSystem.PageReference' : 'save()$0',
        'StandardSetController.setFilterId(String filterId)\tvoid' : 'setFilterId($0)',
        'StandardSetController.setPageNumber(Integer pageNumber)\tvoid' : 'setPageNumber($0)',
        'StandardSetController.setPageSize(Integer pageSize)\tvoid' : 'setPageSize($0)',
        'StandardSetController.setSelected(LIST<SObject> selected)\tvoid' : 'setSelected($0)'
    },
    'StaticResourceCalloutMock' : {
        'StaticResourceCalloutMock.respond(System.HttpRequest request)\tSystem.HttpResponse' : 'respond($0)',
        'StaticResourceCalloutMock.setHeader(String key, String val)\tvoid' : 'setHeader($0)',
        'StaticResourceCalloutMock.setStaticResource(String staticResourceName)\tvoid' : 'setStaticResource($0)',
        'StaticResourceCalloutMock.setStatus(String status)\tvoid' : 'setStatus($0)',
        'StaticResourceCalloutMock.setStatusCode(Integer code)\tvoid' : 'setStatusCode($0)'
    },
    'StatusCode' : {
        'StatusCode.values()\tLIST<system.StatusCode>' : 'values()$0'
    },
    'String' : {
        'String.abbreviate(Integer maxWidth)\tString' : 'abbreviate($0)',
        'String.abbreviate(Integer maxWidth, Integer offset)\tString' : 'abbreviate($0)',
        'String.addError(APEX_OBJECT msg)\tvoid' : 'addError($0)',
        'String.addError(APEX_OBJECT msg, Boolean escape)\tvoid' : 'addError($0)',
        'String.addError(String msg)\tvoid' : 'addError($0)',
        'String.addError(String msg, Boolean escape)\tvoid' : 'addError($0)',
        'String.capitalize()\tString' : 'capitalize()$0',
        'String.center(Integer size)\tString' : 'center($0)',
        'String.center(Integer size, String padStr)\tString' : 'center($0)',
        'String.compareTo(String str)\tInteger' : 'compareTo($0)',
        'String.contains(String str)\tBoolean' : 'contains($0)',
        'String.containsAny(String validChars)\tBoolean' : 'containsAny($0)',
        'String.containsIgnoreCase(String searchStr)\tBoolean' : 'containsIgnoreCase($0)',
        'String.containsNone(String invalidChars)\tBoolean' : 'containsNone($0)',
        'String.containsOnly(String validChars)\tBoolean' : 'containsOnly($0)',
        'String.containsWhitespace()\tBoolean' : 'containsWhitespace()$0',
        'String.countMatches(String searchStr)\tInteger' : 'countMatches($0)',
        'String.deleteWhitespace()\tString' : 'deleteWhitespace()$0',
        'String.difference(String other)\tString' : 'difference($0)',
        'String.endsWith(String str)\tBoolean' : 'endsWith($0)',
        'String.endsWithIgnoreCase(String suffix)\tBoolean' : 'endsWithIgnoreCase($0)',
        'String.equals(String other)\tBoolean' : 'equals($0)',
        'String.equalsIgnoreCase(String other)\tBoolean' : 'equalsIgnoreCase($0)',
        'String.escapeCsv()\tString' : 'escapeCsv()$0',
        'String.escapeEcmaScript()\tString' : 'escapeEcmaScript()$0',
        'String.escapeHtml3()\tString' : 'escapeHtml3()$0',
        'String.escapeHtml4()\tString' : 'escapeHtml4()$0',
        'String.escapeSingleQuotes(String s)\tString' : 'escapeSingleQuotes($0)',
        'String.escapeXml()\tString' : 'escapeXml()$0',
        'String.format(String format, LIST<String> arguments)\tString' : 'format($0)',
        'String.fromCharArray(LIST<Integer> charArr)\tString' : 'fromCharArray($0)',
        'String.getCommonPrefix(LIST strings)\tString' : 'getCommonPrefix($0)',
        'String.getLevenshteinDistance(String other)\tInteger' : 'getLevenshteinDistance($0)',
        'String.getLevenshteinDistance(String other, Integer threshold)\tInteger' : 'getLevenshteinDistance($0)',
        'String.hashCode()\tInteger' : 'hashCode()$0',
        'String.indexOf(String str)\tInteger' : 'indexOf($0)',
        'String.indexOf(String str, Integer startPos)\tInteger' : 'indexOf($0)',
        'String.indexOfAny(String searchChars)\tInteger' : 'indexOfAny($0)',
        'String.indexOfAnyBut(String searchChars)\tInteger' : 'indexOfAnyBut($0)',
        'String.indexOfDifference(String other)\tInteger' : 'indexOfDifference($0)',
        'String.indexOfIgnoreCase(String searchStr)\tInteger' : 'indexOfIgnoreCase($0)',
        'String.indexOfIgnoreCase(String searchStr, Integer startPos)\tInteger' : 'indexOfIgnoreCase($0)',
        'String.isAllLowerCase()\tBoolean' : 'isAllLowerCase()$0',
        'String.isAllUpperCase()\tBoolean' : 'isAllUpperCase()$0',
        'String.isAlpha()\tBoolean' : 'isAlpha()$0',
        'String.isAlphaSpace()\tBoolean' : 'isAlphaSpace()$0',
        'String.isAlphanumeric()\tBoolean' : 'isAlphanumeric()$0',
        'String.isAlphanumericSpace()\tBoolean' : 'isAlphanumericSpace()$0',
        'String.isAsciiPrintable()\tBoolean' : 'isAsciiPrintable()$0',
        'String.isBlank(String str)\tBoolean' : 'isBlank($0)',
        'String.isEmpty(String str)\tBoolean' : 'isEmpty($0)',
        'String.isNotBlank(String str)\tBoolean' : 'isNotBlank($0)',
        'String.isNotEmpty(String str)\tBoolean' : 'isNotEmpty($0)',
        'String.isNumeric()\tBoolean' : 'isNumeric()$0',
        'String.isNumericSpace()\tBoolean' : 'isNumericSpace()$0',
        'String.isWhitespace()\tBoolean' : 'isWhitespace()$0',
        'String.join(APEX_OBJECT iterableObj, String separator)\tString' : 'join($0)',
        'String.lastIndexOf(String searchStr, Integer startPos)\tInteger' : 'lastIndexOf($0)',
        'String.lastIndexOf(String str)\tInteger' : 'lastIndexOf($0)',
        'String.lastIndexOfIgnoreCase(String searchStr)\tInteger' : 'lastIndexOfIgnoreCase($0)',
        'String.lastIndexOfIgnoreCase(String searchStr, Integer startPos)\tInteger' : 'lastIndexOfIgnoreCase($0)',
        'String.left(Integer len)\tString' : 'left($0)',
        'String.leftPad(Integer len)\tString' : 'leftPad($0)',
        'String.leftPad(Integer len, String padStr)\tString' : 'leftPad($0)',
        'String.length()\tInteger' : 'length()$0',
        'String.mid(Integer pos, Integer len)\tString' : 'mid($0)',
        'String.normalizeSpace()\tString' : 'normalizeSpace()$0',
        'String.overlay(String overlay, Integer start, Integer end)\tString' : 'overlay($0)',
        'String.remove(String toRemove)\tString' : 'remove($0)',
        'String.removeEnd(String toRemove)\tString' : 'removeEnd($0)',
        'String.removeEndIgnoreCase(String toRemove)\tString' : 'removeEndIgnoreCase($0)',
        'String.removeStart(String toRemove)\tString' : 'removeStart($0)',
        'String.removeStartIgnoreCase(String toRemove)\tString' : 'removeStartIgnoreCase($0)',
        'String.repeat(Integer numTimes)\tString' : 'repeat($0)',
        'String.repeat(String separator, Integer numTimes)\tString' : 'repeat($0)',
        'String.replace(String target, String replacement)\tString' : 'replace($0)',
        'String.replaceAll(String regex, String replacement)\tString' : 'replaceAll($0)',
        'String.replaceFirst(String regex, String replacement)\tString' : 'replaceFirst($0)',
        'String.reverse()\tString' : 'reverse()$0',
        'String.right(Integer len)\tString' : 'right($0)',
        'String.rightPad(Integer len)\tString' : 'rightPad($0)',
        'String.rightPad(Integer len, String padStr)\tString' : 'rightPad($0)',
        'String.split(String regex)\tLIST<String>' : 'split($0)',
        'String.split(String regex, Integer limit)\tLIST<String>' : 'split($0)',
        'String.splitByCharacterType()\tLIST<String>' : 'splitByCharacterType()$0',
        'String.splitByCharacterTypeCamelCase()\tLIST<String>' : 'splitByCharacterTypeCamelCase()$0',
        'String.startsWith(String str)\tBoolean' : 'startsWith($0)',
        'String.startsWithIgnoreCase(String prefix)\tBoolean' : 'startsWithIgnoreCase($0)',
        'String.stripHtmlTags()\tString' : 'stripHtmlTags()$0',
        'String.substring(Integer start)\tString' : 'substring($0)',
        'String.substring(Integer start, Integer end)\tString' : 'substring($0)',
        'String.substringAfter(String separator)\tString' : 'substringAfter($0)',
        'String.substringAfterLast(String separator)\tString' : 'substringAfterLast($0)',
        'String.substringBefore(String separator)\tString' : 'substringBefore($0)',
        'String.substringBeforeLast(String separator)\tString' : 'substringBeforeLast($0)',
        'String.substringBetween(String open, String close)\tString' : 'substringBetween($0)',
        'String.substringBetween(String tag)\tString' : 'substringBetween($0)',
        'String.swapCase()\tString' : 'swapCase()$0',
        'String.toLowerCase()\tString' : 'toLowerCase()$0',
        'String.toLowerCase(String locale)\tString' : 'toLowerCase($0)',
        'String.toUpperCase()\tString' : 'toUpperCase()$0',
        'String.toUpperCase(String locale)\tString' : 'toUpperCase($0)',
        'String.trim()\tString' : 'trim()$0',
        'String.uncapitalize()\tString' : 'uncapitalize()$0',
        'String.unescapeCsv()\tString' : 'unescapeCsv()$0',
        'String.unescapeEcmaScript()\tString' : 'unescapeEcmaScript()$0',
        'String.unescapeHtml3()\tString' : 'unescapeHtml3()$0',
        'String.unescapeHtml4()\tString' : 'unescapeHtml4()$0',
        'String.unescapeXml()\tString' : 'unescapeXml()$0',
        'String.valueOf(Date d)\tString' : 'valueOf($0)',
        'String.valueOf(Datetime dt)\tString' : 'valueOf($0)',
        'String.valueOf(Decimal d)\tString' : 'valueOf($0)',
        'String.valueOf(Double d)\tString' : 'valueOf($0)',
        'String.valueOf(Integer i)\tString' : 'valueOf($0)',
        'String.valueOf(Long l)\tString' : 'valueOf($0)',
        'String.valueOf(Object o)\tString' : 'valueOf($0)',
        'String.valueOfGmt(Datetime dt)\tString' : 'valueOfGmt($0)'
    },
    'StringException' : {
        'StringException.getCause()\tException' : 'getCause()$0',
        'StringException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'StringException.getMessage()\tString' : 'getMessage()$0',
        'StringException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'StringException.getTypeName()\tString' : 'getTypeName()$0',
        'StringException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'StringException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'Subscription' : {
        'Subscription.equals(Object obj)\tBoolean' : 'equals($0)',
        'Subscription.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'Subscription.hashCode()\tInteger' : 'hashCode()$0',
        'Subscription.toString()\tString' : 'toString()$0'
    },
    'System' : {
        'System.abortJob(String jobId)\tvoid' : 'abortJob($0)',
        'System.assert(Boolean condition)\tvoid' : 'assert($0)',
        'System.assert(Boolean condition, ANY msg)\tvoid' : 'assert($0)',
        'System.assertEquals(ANY expected, ANY actual)\tvoid' : 'assertEquals($0)',
        'System.assertEquals(ANY expected, ANY actual, ANY msg)\tvoid' : 'assertEquals($0)',
        'System.assertNotEquals(ANY expected, ANY actual)\tvoid' : 'assertNotEquals($0)',
        'System.assertNotEquals(ANY expected, ANY actual, ANY msg)\tvoid' : 'assertNotEquals($0)',
        'System.currentPageReference()\tSystem.PageReference' : 'currentPageReference()$0',
        'System.currentTimeMillis()\tLong' : 'currentTimeMillis()$0',
        'System.debug(ANY o)\tvoid' : 'debug($0)',
        'System.debug(APEX_OBJECT logLevel, ANY o)\tvoid' : 'debug($0)',
        'System.getApplicationReadWriteMode()\tsystem.ApplicationReadWriteMode' : 'getApplicationReadWriteMode()$0',
        'System.isBatch()\tBoolean' : 'isBatch()$0',
        'System.isFuture()\tBoolean' : 'isFuture()$0',
        'System.isScheduled()\tBoolean' : 'isScheduled()$0',
        'System.now()\tDatetime' : 'now()$0',
        'System.process(LIST workitemIds, String action, String commments, String nextApprover)\tLIST<Id>' : 'process($0)',
        'System.purgeOldAsyncJobs(Date date)\tInteger' : 'purgeOldAsyncJobs($0)',
        'System.requestVersion()\tsystem.Version' : 'requestVersion()$0',
        'System.resetPassword(Id userId, Boolean sendUserEmail)\tSystem.ResetPasswordResult' : 'resetPassword($0)',
        'System.runAs(Package.Version version)\tvoid' : 'runAs($0)',
        'System.runAs(SObject user, ANY block)\tvoid' : 'runAs($0)',
        'System.schedule(String jobName, String cronExp, APEX_OBJECT schedulable)\tString' : 'schedule($0)',
        'System.scheduleBatch(APEX_OBJECT batchable, String jobName, Integer minutesFromNow)\tString' : 'scheduleBatch($0)',
        'System.scheduleBatch(APEX_OBJECT batchable, String jobName, Integer minutesFromNow, Integer scopeSize)\tString' : 'scheduleBatch($0)',
        'System.setPassword(Id userId, String password)\tvoid' : 'setPassword($0)',
        'System.submit(LIST ids, String commments, String nextApprover)\tLIST<Id>' : 'submit($0)',
        'System.today()\tDate' : 'today()$0'
    },
    'Test' : {
        'Test.invokePage(System.PageReference p)\tComponent.apex.page' : 'invokePage($0)',
        'Test.isRunningTest()\tBoolean' : 'isRunningTest()$0',
        'Test.loadData(Schema.SObjectType sobjectType, String staticResourceName)\tLIST<SObject>' : 'loadData($0)',
        'Test.setCurrentPage(Object pageReference)\tvoid' : 'setCurrentPage($0)',
        'Test.setCurrentPageReference(Object pageReference)\tvoid' : 'setCurrentPageReference($0)',
        'Test.setFixedSearchResults(LIST<String> searchResultsIds)\tvoid' : 'setFixedSearchResults($0)',
        'Test.setMock(system.Type interfaceType, Object mock)\tvoid' : 'setMock($0)',
        'Test.setReadOnlyApplicationMode(Boolean readOnlyApplicationMode)\tvoid' : 'setReadOnlyApplicationMode($0)',
        'Test.startTest()\tvoid' : 'startTest()$0',
        'Test.stopTest()\tvoid' : 'stopTest()$0',
        'Test.testInstall(system.InstallHandler script, system.Version version)\tvoid' : 'testInstall($0)',
        'Test.testInstall(system.InstallHandler script, system.Version version, Boolean isPush)\tvoid' : 'testInstall($0)',
        'Test.testUninstall(system.UninstallHandler script)\tvoid' : 'testUninstall($0)'
    },
    'TextAttachment' : {},
    'TextSegment' : {
        'TextSegment.equals(Object obj)\tBoolean' : 'equals($0)',
        'TextSegment.hashCode()\tInteger' : 'hashCode()$0',
        'TextSegment.toString()\tString' : 'toString()$0'
    },
    'TextSegmentInput' : {
        'TextSegmentInput.convertToJavaObject(java:common.api.AppVersion currentVersion)\tjava:java.lang.Object' : 'convertToJavaObject($0)',
        'TextSegmentInput.equals(Object obj)\tBoolean' : 'equals($0)',
        'TextSegmentInput.hashCode()\tInteger' : 'hashCode()$0',
        'TextSegmentInput.toString()\tString' : 'toString()$0'
    },
    'Time' : {
        'Time.addError(APEX_OBJECT msg)\tvoid' : 'addError($0)',
        'Time.addError(APEX_OBJECT msg, Boolean escape)\tvoid' : 'addError($0)',
        'Time.addError(String msg)\tvoid' : 'addError($0)',
        'Time.addError(String msg, Boolean escape)\tvoid' : 'addError($0)',
        'Time.addHours(Integer hours)\tTime' : 'addHours($0)',
        'Time.addMilliseconds(Integer milliseconds)\tTime' : 'addMilliseconds($0)',
        'Time.addMinutes(Integer minutes)\tTime' : 'addMinutes($0)',
        'Time.addSeconds(Integer seconds)\tTime' : 'addSeconds($0)',
        'Time.hour()\tInteger' : 'hour()$0',
        'Time.millisecond()\tInteger' : 'millisecond()$0',
        'Time.minute()\tInteger' : 'minute()$0',
        'Time.newInstance(Integer hour, Integer minute, Integer second, Integer millisecond)\tTime' : 'newInstance($0)',
        'Time.second()\tInteger' : 'second()$0'
    },
    'TimeZone' : {
        'TimeZone.getDisplayName()\tString' : 'getDisplayName()$0',
        'TimeZone.getID()\tString' : 'getID()$0',
        'TimeZone.getOffset(Datetime dt)\tInteger' : 'getOffset($0)',
        'TimeZone.getTimeZone(String id)\tsystem.TimeZone' : 'getTimeZone($0)',
        'TimeZone.toString()\tString' : 'toString()$0'
    },
    'TouchHandledException' : {
        'TouchHandledException.getCause()\tException' : 'getCause()$0',
        'TouchHandledException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'TouchHandledException.getMessage()\tString' : 'getMessage()$0',
        'TouchHandledException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'TouchHandledException.getTypeName()\tString' : 'getTypeName()$0',
        'TouchHandledException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'TouchHandledException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'Type' : {
        'Type.equals(Object o)\tBoolean' : 'equals($0)',
        'Type.forName(String clsName)\tsystem.Type' : 'forName($0)',
        'Type.forName(String namespace, String clsName)\tsystem.Type' : 'forName($0)',
        'Type.getName()\tString' : 'getName()$0',
        'Type.hashcode()\tInteger' : 'hashcode()$0',
        'Type.newInstance()\tObject' : 'newInstance()$0',
        'Type.toString()\tString' : 'toString()$0'
    },
    'TypeException' : {
        'TypeException.getCause()\tException' : 'getCause()$0',
        'TypeException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'TypeException.getMessage()\tString' : 'getMessage()$0',
        'TypeException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'TypeException.getTypeName()\tString' : 'getTypeName()$0',
        'TypeException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'TypeException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'UnauthenticatedUser' : {
        'UnauthenticatedUser.equals(Object obj)\tBoolean' : 'equals($0)',
        'UnauthenticatedUser.hashCode()\tInteger' : 'hashCode()$0',
        'UnauthenticatedUser.toString()\tString' : 'toString()$0'
    },
    'UnexpectedException' : {
        'UnexpectedException.getCause()\tException' : 'getCause()$0',
        'UnexpectedException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'UnexpectedException.getMessage()\tString' : 'getMessage()$0',
        'UnexpectedException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'UnexpectedException.getTypeName()\tString' : 'getTypeName()$0',
        'UnexpectedException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'UnexpectedException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'UnsupportedOperationException' : {
        'UnsupportedOperationException.getTypeName()\tString' : 'getTypeName()$0'
    },
    'Url' : {
        'Url.getAuthority()\tString' : 'getAuthority()$0',
        'Url.getCurrentRequestUrl()\tsystem.Url' : 'getCurrentRequestUrl()$0',
        'Url.getDefaultPort()\tInteger' : 'getDefaultPort()$0',
        'Url.getFile()\tString' : 'getFile()$0',
        'Url.getFileFieldURL(String objectId, String fieldName)\tString' : 'getFileFieldURL($0)',
        'Url.getHost()\tString' : 'getHost()$0',
        'Url.getPath()\tString' : 'getPath()$0',
        'Url.getPort()\tInteger' : 'getPort()$0',
        'Url.getProtocol()\tString' : 'getProtocol()$0',
        'Url.getQuery()\tString' : 'getQuery()$0',
        'Url.getRef()\tString' : 'getRef()$0',
        'Url.getSalesforceBaseUrl()\tsystem.Url' : 'getSalesforceBaseUrl()$0',
        'Url.getUserInfo()\tString' : 'getUserInfo()$0',
        'Url.sameFile(system.Url other)\tBoolean' : 'sameFile($0)',
        'Url.toExternalForm()\tString' : 'toExternalForm()$0'
    },
    'UrlRewriter' : {
        'UrlRewriter.generateUrlFor(LIST<System.PageReference> param1)\tLIST<System.PageReference>' : 'generateUrlFor($0)',
        'UrlRewriter.mapRequestUrl(System.PageReference param1)\tSystem.PageReference' : 'mapRequestUrl($0)'
    },
    'User' : {
        'User.equals(Object obj)\tBoolean' : 'equals($0)',
        'User.hashCode()\tInteger' : 'hashCode()$0',
        'User.toString()\tString' : 'toString()$0'
    },
    'UserChatterSettings' : {
        'UserChatterSettings.equals(Object obj)\tBoolean' : 'equals($0)',
        'UserChatterSettings.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'UserChatterSettings.hashCode()\tInteger' : 'hashCode()$0',
        'UserChatterSettings.toString()\tString' : 'toString()$0'
    },
    'UserDetail' : {
        'UserDetail.equals(Object obj)\tBoolean' : 'equals($0)',
        'UserDetail.hashCode()\tInteger' : 'hashCode()$0',
        'UserDetail.toString()\tString' : 'toString()$0'
    },
    'UserGroupPage' : {
        'UserGroupPage.equals(Object obj)\tBoolean' : 'equals($0)',
        'UserGroupPage.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'UserGroupPage.hashCode()\tInteger' : 'hashCode()$0',
        'UserGroupPage.toString()\tString' : 'toString()$0'
    },
    'UserInfo' : {
        'UserInfo.getDefaultCurrency()\tString' : 'getDefaultCurrency()$0',
        'UserInfo.getFirstName()\tString' : 'getFirstName()$0',
        'UserInfo.getLanguage()\tString' : 'getLanguage()$0',
        'UserInfo.getLastName()\tString' : 'getLastName()$0',
        'UserInfo.getLocale()\tString' : 'getLocale()$0',
        'UserInfo.getName()\tString' : 'getName()$0',
        'UserInfo.getOrganizationId()\tString' : 'getOrganizationId()$0',
        'UserInfo.getOrganizationName()\tString' : 'getOrganizationName()$0',
        'UserInfo.getProfileId()\tString' : 'getProfileId()$0',
        'UserInfo.getSessionId()\tString' : 'getSessionId()$0',
        'UserInfo.getTimeZone()\tsystem.TimeZone' : 'getTimeZone()$0',
        'UserInfo.getUiTheme()\tString' : 'getUiTheme()$0',
        'UserInfo.getUiThemeDisplayed()\tString' : 'getUiThemeDisplayed()$0',
        'UserInfo.getUserEmail()\tString' : 'getUserEmail()$0',
        'UserInfo.getUserId()\tString' : 'getUserId()$0',
        'UserInfo.getUserName()\tString' : 'getUserName()$0',
        'UserInfo.getUserRoleId()\tString' : 'getUserRoleId()$0',
        'UserInfo.getUserType()\tString' : 'getUserType()$0',
        'UserInfo.isCurrentUserLicensed(String namespacePrefix)\tBoolean' : 'isCurrentUserLicensed($0)',
        'UserInfo.isMultiCurrencyOrganization()\tBoolean' : 'isMultiCurrencyOrganization()$0'
    },
    'UserPage' : {
        'UserPage.equals(Object obj)\tBoolean' : 'equals($0)',
        'UserPage.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'UserPage.hashCode()\tInteger' : 'hashCode()$0',
        'UserPage.toString()\tString' : 'toString()$0'
    },
    'UserSettings' : {
        'UserSettings.equals(Object obj)\tBoolean' : 'equals($0)',
        'UserSettings.getBuildVersion()\tDouble' : 'getBuildVersion()$0',
        'UserSettings.hashCode()\tInteger' : 'hashCode()$0',
        'UserSettings.toString()\tString' : 'toString()$0'
    },
    'UserSummary' : {
        'UserSummary.equals(Object obj)\tBoolean' : 'equals($0)',
        'UserSummary.hashCode()\tInteger' : 'hashCode()$0',
        'UserSummary.toString()\tString' : 'toString()$0'
    },
    'UserType' : {
        'UserType.values()\tLIST<ConnectApi.UserType>' : 'values()$0'
    },
    'Version' : {
        'Version.compareTo(system.Version other)\tInteger' : 'compareTo($0)',
        'Version.major()\tInteger' : 'major()$0',
        'Version.minor()\tInteger' : 'minor()$0',
        'Version.patch()\tInteger' : 'patch()$0'
    },
    'VisualforceException' : {
        'VisualforceException.getCause()\tException' : 'getCause()$0',
        'VisualforceException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'VisualforceException.getMessage()\tString' : 'getMessage()$0',
        'VisualforceException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'VisualforceException.getTypeName()\tString' : 'getTypeName()$0',
        'VisualforceException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'VisualforceException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'WebServiceMock' : {
        'WebServiceMock.doInvoke(Object param1, Object param2, MAP<String,ANY> param3, String param4, String param5, String param6, String param7, String param8, String param9)\tvoid' : 'doInvoke($0)'
    },
    'WorkflowProcessStatus' : {
        'WorkflowProcessStatus.values()\tLIST<ConnectApi.WorkflowProcessStatus>' : 'values()$0'
    },
    'XmlException' : {
        'XmlException.getCause()\tException' : 'getCause()$0',
        'XmlException.getLineNumber()\tInteger' : 'getLineNumber()$0',
        'XmlException.getMessage()\tString' : 'getMessage()$0',
        'XmlException.getStackTraceString()\tString' : 'getStackTraceString()$0',
        'XmlException.getTypeName()\tString' : 'getTypeName()$0',
        'XmlException.initCause(APEX_OBJECT cause)\tvoid' : 'initCause($0)',
        'XmlException.setMessage(String message)\tvoid' : 'setMessage($0)'
    },
    'XmlNode' : {
        'XmlNode.addChildElement(String name, String namespace, String prefix)\tdom.XmlNode' : 'addChildElement($0)',
        'XmlNode.addCommentNode(String text)\tdom.XmlNode' : 'addCommentNode($0)',
        'XmlNode.addTextNode(String text)\tdom.XmlNode' : 'addTextNode($0)',
        'XmlNode.getAttribute(String key, String keyNamespace)\tString' : 'getAttribute($0)',
        'XmlNode.getAttributeCount()\tInteger' : 'getAttributeCount()$0',
        'XmlNode.getAttributeKeyAt(Integer index)\tString' : 'getAttributeKeyAt($0)',
        'XmlNode.getAttributeKeyNsAt(Integer index)\tString' : 'getAttributeKeyNsAt($0)',
        'XmlNode.getAttributeValue(String key, String keyNamespace)\tString' : 'getAttributeValue($0)',
        'XmlNode.getAttributeValueNs(String key, String keyNamespace)\tString' : 'getAttributeValueNs($0)',
        'XmlNode.getChildElement(String name, String namespace)\tdom.XmlNode' : 'getChildElement($0)',
        'XmlNode.getChildElements()\tLIST<dom.XmlNode>' : 'getChildElements()$0',
        'XmlNode.getChildren()\tLIST<dom.XmlNode>' : 'getChildren()$0',
        'XmlNode.getName()\tString' : 'getName()$0',
        'XmlNode.getNamespace()\tString' : 'getNamespace()$0',
        'XmlNode.getNamespaceFor(String prefix)\tString' : 'getNamespaceFor($0)',
        'XmlNode.getNodeType()\tDom.XmlNodeType' : 'getNodeType()$0',
        'XmlNode.getParent()\tdom.XmlNode' : 'getParent()$0',
        'XmlNode.getPrefixFor(String namespace)\tString' : 'getPrefixFor($0)',
        'XmlNode.getText()\tString' : 'getText()$0',
        'XmlNode.removeAttribute(String key, String keyNamespace)\tBoolean' : 'removeAttribute($0)',
        'XmlNode.removeChild(ANY child)\tBoolean' : 'removeChild($0)',
        'XmlNode.setAttribute(String key, String value)\tvoid' : 'setAttribute($0)',
        'XmlNode.setAttributeNs(String key, String value, String keyNamespace, String valueNamespace)\tvoid' : 'setAttributeNs($0)',
        'XmlNode.setNamespace(String prefix, String namespace)\tvoid' : 'setNamespace($0)'
    },
    'XmlNodeType' : {
        'XmlNodeType.values()\tLIST<Dom.XmlNodeType>' : 'values()$0'
    },
    'XmlStreamReader' : {
        'XmlStreamReader.getAttributeCount()\tInteger' : 'getAttributeCount()$0',
        'XmlStreamReader.getAttributeLocalName(Integer index)\tString' : 'getAttributeLocalName($0)',
        'XmlStreamReader.getAttributeNamespace(Integer index)\tString' : 'getAttributeNamespace($0)',
        'XmlStreamReader.getAttributePrefix(Integer index)\tString' : 'getAttributePrefix($0)',
        'XmlStreamReader.getAttributeType(Integer index)\tString' : 'getAttributeType($0)',
        'XmlStreamReader.getAttributeValue(String namespaceURI, String localName)\tString' : 'getAttributeValue($0)',
        'XmlStreamReader.getAttributeValueAt(Integer index)\tString' : 'getAttributeValueAt($0)',
        'XmlStreamReader.getEventType()\tsystem.XmlTag' : 'getEventType()$0',
        'XmlStreamReader.getLocalName()\tString' : 'getLocalName()$0',
        'XmlStreamReader.getLocation()\tString' : 'getLocation()$0',
        'XmlStreamReader.getNamespace()\tString' : 'getNamespace()$0',
        'XmlStreamReader.getNamespaceCount()\tInteger' : 'getNamespaceCount()$0',
        'XmlStreamReader.getNamespacePrefix(Integer index)\tString' : 'getNamespacePrefix($0)',
        'XmlStreamReader.getNamespaceURI(String prefix)\tString' : 'getNamespaceURI($0)',
        'XmlStreamReader.getNamespaceURIAt(Integer index)\tString' : 'getNamespaceURIAt($0)',
        'XmlStreamReader.getPIData()\tString' : 'getPIData()$0',
        'XmlStreamReader.getPITarget()\tString' : 'getPITarget()$0',
        'XmlStreamReader.getPrefix()\tString' : 'getPrefix()$0',
        'XmlStreamReader.getText()\tString' : 'getText()$0',
        'XmlStreamReader.getVersion()\tString' : 'getVersion()$0',
        'XmlStreamReader.hasName()\tBoolean' : 'hasName()$0',
        'XmlStreamReader.hasNext()\tBoolean' : 'hasNext()$0',
        'XmlStreamReader.hasText()\tBoolean' : 'hasText()$0',
        'XmlStreamReader.isCharacters()\tBoolean' : 'isCharacters()$0',
        'XmlStreamReader.isEndElement()\tBoolean' : 'isEndElement()$0',
        'XmlStreamReader.isStartElement()\tBoolean' : 'isStartElement()$0',
        'XmlStreamReader.isWhitespace()\tBoolean' : 'isWhitespace()$0',
        'XmlStreamReader.next()\tInteger' : 'next()$0',
        'XmlStreamReader.nextTag()\tInteger' : 'nextTag()$0',
        'XmlStreamReader.setCoalescing(Boolean flag)\tvoid' : 'setCoalescing($0)',
        'XmlStreamReader.setNamespaceAware(Boolean flag)\tvoid' : 'setNamespaceAware($0)',
        'XmlStreamReader.toString()\tString' : 'toString()$0'
    },
    'XmlStreamWriter' : {
        'XmlStreamWriter.close()\tvoid' : 'close()$0',
        'XmlStreamWriter.getXmlString()\tString' : 'getXmlString()$0',
        'XmlStreamWriter.setDefaultNamespace(String uri)\tvoid' : 'setDefaultNamespace($0)',
        'XmlStreamWriter.writeAttribute(String prefix, String namespaceURI, String localName, String value)\tvoid' : 'writeAttribute($0)',
        'XmlStreamWriter.writeCData(String data)\tvoid' : 'writeCData($0)',
        'XmlStreamWriter.writeCharacters(String text)\tvoid' : 'writeCharacters($0)',
        'XmlStreamWriter.writeComment(String data)\tvoid' : 'writeComment($0)',
        'XmlStreamWriter.writeDefaultNamespace(String namesapceURI)\tvoid' : 'writeDefaultNamespace($0)',
        'XmlStreamWriter.writeEmptyElement(String prefix, String localName, String namesapceURI)\tvoid' : 'writeEmptyElement($0)',
        'XmlStreamWriter.writeEndDocument()\tvoid' : 'writeEndDocument()$0',
        'XmlStreamWriter.writeEndElement()\tvoid' : 'writeEndElement()$0',
        'XmlStreamWriter.writeNamespace(String prefix, String namesapceURI)\tvoid' : 'writeNamespace($0)',
        'XmlStreamWriter.writeProcessingInstruction(String target, String data)\tvoid' : 'writeProcessingInstruction($0)',
        'XmlStreamWriter.writeStartDocument(String encoding, String version)\tvoid' : 'writeStartDocument($0)',
        'XmlStreamWriter.writeStartElement(String prefix, String localName, String namesapceURI)\tvoid' : 'writeStartElement($0)'
    },
    'XmlTag' : {
        'XmlTag.values()\tLIST<system.XmlTag>' : 'values()$0'
    }
}