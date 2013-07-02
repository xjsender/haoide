metadata = {
    "Blob": {
        "Blob.toPdf(String s)": "toPdf($1)",
        "Blob.valueOf(String s)": "valueOf($1)",
        "Blob.size()": "size()",
        "Blob.toString()": "toString()"
    },

    "Boolean": {
        "Boolean.valueOf(String s)": "valueOf($1)",
        "Boolean.valueOf(Object fieldValue)": "valueOf($1)",
    },

    "String": {
        "String.lastIndexOf(Integer index)": "lastIndexOf($1)",
        "String.escapeSingleQuotes(String s)": "escapeSingleQuotes($1)",
        "String.format(String s, List<String> args)": "format($1, $2)",
        "String.fromCharArray(List<Integer> charArray)": "fromCharArray($1)",
        "String.isBlank(String s)": "isBlank(${1:String})",
        "String.isEmpty(String s)": "isEmpty(${1:String})",
        "String.isNotBlank(String s)": "isNotBlank(${1:String})",
        "String.isNotEmpty(String s)": "isNotEmpty(${1:String})",
        "String.join(Object iterable, String separator)": "join($1, $2)",
        "String.valueOf(Date d)": "valueOf(${1:Date d})",
        "String.valueOf(Datetime dt)": "valueOf($1)",
        "String.valueOf(Decimal d)": "valueOf($1)",
        "String.valueOf(Double d)": "valueOf($1)",
        "String.valueOf(Integer i)": "valueOf($1)",
        "String.valueOf(Long l)": "valueOf($1)",
        "String.valueOf(Object x)": "valueOf($1)"
    },

    "System": {
        "System.debug(AnyType)": "debug($1)",
        "System.now()": "now()$1"
    }
}