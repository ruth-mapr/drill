# Goal

This tutorial covers how to query a file and a directory on your local file
system. Files and directories are like standard SQL tables to Drill. If you
install Drill in [embedded
mode](/confluence/display/DRILL/Installing+Drill+in+Embedded+Mode), the
installer registers and configures your file system as the `dfs` [storage
plugin](/confluence/display/DRILL/Getting+to+Know+the+Drill+Setup) instance.
You can query these types of files using `dfs`:

  * Plain text files, such as comma-separated values (CSV) or tab-separated values (TSV) files
  * JSON files
  * Parquet files

In this tutorial, you query plain text files and you create a custom storage
plugin to simplify querying plain text files.

# Prerequisites

This tutorial assumes that you installed Drill in [embedded
mode](/confluence/display/DRILL/Installing+Drill+in+Embedded+Mode). Although
you can step through the tutorial using the sandbox, using the Drill
installation is more convenient in a few ways, for example, you can copy/paste
commands from the tutorial to the Drill command line. The first few lessons
use a Google file of Ngram data that you download from the internet. The
compressed Google Ngram files are 8 and 58MB. To expand the compressed files,
you need an additional 448MB of free disk space for this exercise.

To get started, use the SQLLine command to start the Drill command line
interface (CLI) on Linux, Mac OS X, or Windows.

## Start Drill (Linux or Mac OS X)

To [start Drill](/confluence/pages/viewpage.action?pageId=44994063) on Linux
or Mac OS X, use the SQLLine command.

  1. Open a terminal.
  2. Navigate to the Drill installation directory.  
  
Example: `$ cd ~/apache-drill-<version>`  
  

  3. Issue the following command:  
  
$ bin/sqlline -u [jdbc:drill:zk=local  
](http://jdbcdrillzk=local)  
The Drill prompt appears:  
  
`0: [jdbc:drill:zk=local](http://jdbcdrillzk=local)>`

## Start Drill (Windows)

To [start Drill](/confluence/pages/viewpage.action?pageId=44994063) on
Windows, use the SQLLine command.

  1. Open the `apache-drill-<version> `folder.

  2. Open the `bin` folder, and double-click on the `sqlline.bat` file. The Windows command prompt opens.
  3. At the `sqlline>` prompt, issue the following command, and then press **Enter**`:  
`  
`!connect [jdbc:drill:zk=local](http://jdbcdrillzk=local)`  

The following prompt appears:

` 0: [jdbc:drill:zk=local](http://jdbcdrillzk%3Dlocal/)>`

# Stop Drill

To stop Drill, issue the following command at the Drill prompt.

In some cases, this command does not stop Drill. For example, if the IP
address of the host changes during a Drill session, the `!quit` command fails.
You need to kill the Drill process. For example, on Mac OS X and Linux, follow
these steps:

  1. Issue a CTRL Z to exit SQLLine.
  2. Search for the Drill process ID.   
  

  

  3. Kill the process using the process number in the grep output. For example:

