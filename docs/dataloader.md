# Data Loader
## Export Query to CSV
+ QueryAll the matched result by the input SOQL, and then parse the fields from SOQL and then write the queried records according to the parsed fields.
+ Use ``REST API``
+ Support ``child-to-parent`` query but not ``parent-to-child`` query

## Bulk Api
+ Up to now, support close jobs, export, insert, update and delete.
+ You can set the batch size and batch bytes for every batch by put ```maximum_batch_size``` and ```maximum_batch_bytes``` in your user settings, you should be aware, maximum records of single batch is **10K** and maximum bytes of single batch is **1000K**
+ This tool will get your CSV file encoding type by detecting the first **1000** bytes of the CSV file, as a best practice, you should prepare CSV file which encoding type is ```ANSI``` or ```UTF-8```.
+ If you want to insert a CSV file, you'd better open the CSV file in sublime and copy the file path, after you choose the sobject that you want to insert records, this tool will automatically get the file path from the clipboard