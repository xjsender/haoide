trigger Trigger_Name__c on Sobject_Name__c(before insert) {
    new Triggers()
        //.bind(Triggers.Evt.beforeinsert, new ())
        .manage();
}