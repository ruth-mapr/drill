---
title: "Step 3. Connect to Drill Data Sources from a BI Tool"
parent: "Using the MapR ODBC Driver on Windows"
---
After you create the ODBC DSN, you can use ODBC to directly connect to data
that is defined by a schema, such as Hive, and data that is self-describing.
Examples of self-describing data include HBase, Parquet, JSON, CSV,and TSV.

In some cases, you may want to use Drill Explorer to explore that data or to
create a view before you connect to the data from a BI tool. For more
information about Drill Explorer, see [Using Drill Explorer to Browse Data and
Create Views](/confluence/display/DRILL/Using+Drill+Explorer+to+Browse+Data+an
d+Create+Views).

In an ODBC-compliant BI tool, use the ODBC DSN to create an ODBC connection
with one of the methods applicable to the data source type:

<table class="confluenceTable"><tbody><tr><th class="confluenceTh">Data Source Type</th><th class="confluenceTh">ODBC Connection Method</th></tr><tr><td valign="top">Hive</td><td valign="top"><ul><li>Connect to a table.</li><li>Connect to the table using custom SQL.</li><li>Use Drill Explorer to create a view. Then use ODBC to connect to the view as if it were a table.</li></ul></td></tr><tr><td valign="top"><p>HBase<br /><span style="line-height: 1.4285715;background-color: transparent;">Parquet<br /></span><span style="line-height: 1.4285715;background-color: transparent;">JSON<br /></span><span style="line-height: 1.4285715;background-color: transparent;">CSV<br /></span><span style="line-height: 1.4285715;background-color: transparent;">TSV</span></p></td><td valign="top"><ul><li>Use Drill Explorer to create a view. Then use ODBC to connect to the view as if it were a table.</li><li>Connect to the data using custom SQL.</li></ul></td></tr></tbody></table>
  
For examples of how to connect to Drill data sources from a BI tool, see the
[Step 3. Connect to Drill Data Sources from a BI Tool](/confluence/display/DRI
LL/Step+3.+Connect+to+Drill+Data+Sources+from+a+BI+Tool).

**Note:** The default schema that you configure in the DSN may or may not carry over to an application’s data source connections. You may need to re-select the schema.

