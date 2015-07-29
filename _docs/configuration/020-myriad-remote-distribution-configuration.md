---
title: "Myriad Remote Distribution"
parent: "Configuration"
---

The Myriad Scheduler can be configured to automatically download and run the hadoop yarn binaries and get the hadoop 
configuration from the resource manager. This means you won't have to install and configure hadoop yarn on each machine. 
NOTE: This is a very new feature and the configuration options may change dramatically in the future.


## Assumptions
The following are assumptions about your environment:

* You are using hadoop-2.5.0 downloaded from hadoop.apache.org. Specific vendor versions should work but 
may require additional steps.  
* Hadoop is installed in `/opt/hadoop-2.5.0`. This path may need to be modified to conform your installation.

## Building the Myriad Remote Distribution Bundle
Before building Myriad, configure the Resource Manager as you normally would. Building Myriad involves:

1. Running `./gradlew build`.
2. Copying the Myriad Scheduler jar files in your YARN classpath.
3. Placing the Myriad Executor jar files in HDFS.
4. Configuring the Myriad default configuration file.
5. Configuring the YARN XML file.
6. Creating the tarball.



### Step 1: Run `gradlew build`
From the project root, build Myriad with the following command:

```
./gradlew build  
```

### Step 2: Copy the Myriad Schedule Jar Files
Copy the jar files and configuration .yml file onto your YARN classpath:

```
cp myriad-scheduler/build/libs/*.jar /opt/hadoop-2.5.0/share/hadoop/yarn/lib/
cp myriad-scheduler/src/main/resources/myriad-config-default.yml /opt/hadoop-2.5.0/share/hadoop/yarn/lib/
```

### Step 3: Put the Myriad Executor Jar File
Put the `myriad-executor-runnable-x.x.x.jar` file in HDFS.

```
hadoop fs -put myriad-executor/build/libs/myriad-executor-runnable-0.0.1.jar /dist
```

### Step 4: Configure the Myriad Configuration File
Edit `/opt/hadoop/etc/hadoop/myriad-config-default` to configure the default parameters.  For a standard configuration,  see [myriad-configuration]({{site.baseurl}}/docs/myriad-configuration-properties/myriad-configuration.md).  To enable remote binary distribution, you must set the following options:

```

frameworkSuperUser: admin     # Must be root or have passwordless sudo on all nodes!
frameworkUser: hduser         # Should be the same user running the resource manager.
                              # Must exist on all nodes and be in the 'hadoop' group
executor:  
  nodeManagerUri: hdfs://namenode:port/dist/hadoop-2.5.0.tar.gz  
  path: hdfs://namenode:port/dist/myriad-executor-runnable-0.0.1.jar
yarnEnvironment:  
  YARN_HOME: hadoop-2.5.0     # This should be relative if nodeManagerUri is set  
  
```

### Step 5: Configure the YARN XML File

Configure `/opt/hadoop-2.5.0/etc/hadoop/yarn-site.xml` as instructed in: [myriad-configuration]({{site.baseurl}}/docs/myriad-configuration-properties/myriad-configuration.md).


### Step 6: Create the Tarball
Create the tarball and place it in HDFS:

```
cd ~
sudo cp -rp /opt/hadoop-2.5.0 .
sudo rm hadoop-2.5.0/etc/hadoop/*.xml
sudo tar -zcpf ~/hadoop-2.5.0.tar.gz hadoop-2.5.0
hadoop fs -put ~/hadoop-2.5.0.tar.gz /dist
```

You can now start the resource manager and attempt to flex up the cluster!
