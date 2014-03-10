global class class_name implements Database.Batchable<sObject> {
    private String query;

    global class_name(String q) {
        this.query = q;
    }

    global Database.QueryLocator start(Database.BatchableContext bc) {
        return Database.getQueryLocator(query);
    }

    global void execute(Database.BatchableContext BC, list<Opportunity> sobjects) {

    }

    global void finish(Database.BatchableContext bc) {

    }
}