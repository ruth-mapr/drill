---
title: "Advanced Properties"
parent: "Using the MapR ODBC Driver on Linux and Mac OS X"
---
When you use advanced properties, you must separate them using a semi-colon
(;).

For example, the following Advanced Properties string excludes the schemas
named `test` and `abc`; sets the timeout to 30 seconds; and sets the time zone
to Coordinated Universal:

`Time:HandshakeTimeout=30;QueryTimeout=30;
TimestampTZDisplayTimezone=utc;ExcludedSchemas=test,abc`

The following table lists and describes the advanced properties that you can
set when using the MapR Drill ODBC Driver.

<table class="confluenceTable"><tbody><tr><td valign="top"><p class="Body"><strong>Property Name</strong></p></td><td valign="top"><p class="Body"><strong>Default Value</strong></p></td><td valign="top"><p class="Body"><strong>Description</strong></p></td></tr><tr><td valign="top"><p class="Body">HandshakeTimeout</p></td><td valign="top"><p class="Body">5</p></td><td valign="top"><p class="Body">An integer value representing the number of seconds that the driver waits before aborting an attempt to connect to a data source. When set to a value of 0, the driver does not abort connection attempts.</p></td></tr><tr><td valign="top"><p class="Body">QueryTimeout</p></td><td valign="top"><p class="Body">180</p></td><td valign="top"><p class="Body">An integer value representing the number of seconds for the driver to wait before automatically stopping a query. When set to a value of 0, the driver does not stop queries automatically.</p></td></tr><tr><td valign="top"><p class="Body">TimestampTZDisplayTimezone</p></td><td valign="top"><p class="Body">local</p></td><td valign="top"><p class="Body">Two values are possible:</p><p class="Body">local—Timestamps are dependent on the time zone of the user.</p><p class="Body">utc—Timestamps appear in Coordinated Universal Time (UTC).</p></td></tr><tr><td valign="top"><p class="Body">ExcludedSchemas</p></td><td valign="top"><p class="Body">sys, INFORMATION_SCHEMA</p></td><td valign="top"><p class="Body">The value of ExcludedSchemas is a list of schemas that do not appear in client applications such as Drill Explorer, Tableau, and Excel. Separate schemas in the list using a comma (,).</p></td></tr><tr><td colspan="1" valign="top"><span style="color: rgb(0,0,0);">CastAnyToVarchar</span></td><td colspan="1" valign="top">true</td><td colspan="1" valign="top"><span style="color: rgb(0,0,0);">Casts the “ANY” and “(VARCHAR(1), ANY) MAP” data types returned from SQL column calls into type “VARCHAR”.</span></td></tr></tbody></table>

