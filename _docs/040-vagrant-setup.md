---
title: "Vagrant Setup"
parent: "Virtual Machine Setup"
---

This section provides information for setting up a cluster in a virtual machine. To setup a cluster in a virtual machine:

1. Start the cluster.
2. Setup YARN/Hadoop.
3. Build the Myriad Scheduler.
4. Get started.

## Prerequisities
* Virtualbox
* Vagrant


## Starting the Cluster
To start the cluster, run following:

```
vagrant up
```

At this point, the VM has a single node mesos cluster running.

To ssh into the cluster, run following:

```
vagrant ssh
```

The password for the vagrant user is `vagrant`.

## Setting up YARN/Hadoop
To setup YARN/Hadoop inside VM, run the following yarn setup shell files:

1. Run the first yarn setup shell command from the vagrant directory to create a user hduser in group hadoop. Be sure to remember the password that you provide for this user.
   ```
   cd /vagrant
   ./setup-yarn-1.sh
   ```

2. Run the second yarn setup shell command as sudo.
   ```
   sudo su - hduser
   cd /vagrant
   ./setup-yarn-2.sh
   ```

The following processes should be running:

```
9844 Jps
6709 NameNode
6393 JobHistoryServer
6874 DataNode
```

Note: Process IDs are different.


## Building the Myriad Scheduler
Building the Myriad Scheduler involves:

1. Running `./gradlew build`.
2. Copying myriad-scheduler jar files to YARN home.
3. Copying myriad-executor jar files to mesos.
4. Configuring YARN to use Myriad.
5. Configuring Myriad.

### Step 1: Run `gradlew build`
To build the Myriad Scheduler inside a VM, run the gradlew build:

```
cd /vagrant
./gradlew build
```


NOTE: If a build failure occurs, the issue is not with the build itself, but a failure to write to disk.  This can happen when you build outside the vagrant instance first.  To resolve this issue, exit the user `hduser` by typing `exit` and build again as the `vagrant` user. 

### Step 2: Copy the Myriad Scheduler Jar Files

At this point, myriad's scheduler jar and all the runtime dependencies are available in the following location: 
```/vagrant/myriad-scheduler/build/libs/*``` 

Copy these myriad scheduler files to `$YARN_HOME/share/hadoop/yarn/lib/`.  The default `$YARN_HOME` is `/usr/local/hadoop/`.

```
cp /vagrant/myriad-scheduler/build/libs/* /usr/local/hadoop/share/hadoop/yarn/lib/
```

### Step 3: Copy the Myriad Executor Jar File
The self-contained myriad executor jar is available at the following location: 
`/vagrant/myriad-executor/build/libs/myriad-executor-runnable-x.y.z.jar`. 

Copy the myriad executor jar file to `/usr/local/libexec/mesos/`.

```
sudo mkdir -p /usr/local/libexec/mesos/
sudo cp /vagrant/myriad-executor/build/libs/myriad-executor-runnable-0.0.1.jar /usr/local/libexec/mesos/
sudo chown hduser:hadoop -R /usr/local/libexec/mesos/
```

### Step 4: Configure YARN to use Myriad
To configure YARN to use Myriad, update ```$YARN_HOME/etc/hadoop/yarn-site.xml``` with following content:

```xml
<property>
    <name>yarn.nodemanager.resource.cpu-vcores</name>
    <value>${nodemanager.resource.cpu-vcores}</value>
</property>
<property>
    <name>yarn.nodemanager.resource.memory-mb</name>
    <value>${nodemanager.resource.memory-mb}</value>
</property>

<!-- Configure Myriad Scheduler here -->
<property>
    <name>yarn.resourcemanager.scheduler.class</name>
    <value>com.ebay.myriad.scheduler.yarn.MyriadFairScheduler</value>
    <description>One can configure other scehdulers as well from following list: com.ebay.myriad.scheduler.yarn.MyriadCapacityScheduler, com.ebay.myriad.scheduler.yarn.MyriadFifoScheduler</description>
</property>
```

### Step 5: Configure Myriad Defaults
To configure Myriad itself, update ```$YARN_HOME/etc/hadoop/myriad-default-config.yml``` with the following content:



```yaml
mesosMaster: 10.141.141.20:5050
checkpoint: false
frameworkFailoverTimeout: 43200000
frameworkName: MyriadAlpha
nativeLibrary: /usr/local/lib/libmesos.so
zkServers: localhost:2181
zkTimeout: 20000
profiles:
  small:
    cpu: 1
    mem: 1100
  medium:
    cpu: 2
    mem: 2048
  large:
    cpu: 4
    mem: 4096
rebalancer: true
nodemanager:
  jvmMaxMemoryMB: 1024
  user: hduser
  cpus: 0.2
  cgroups: false
executor:
  jvmMaxMemoryMB: 256
  path: file://localhost/usr/local/libexec/mesos/myriad-executor-runnable-0.0.1.jar
```


## Getting Started
To launch Myriad, run following:

```
sudo su hduser
yarn-daemon.sh start resourcemanager
```

### Verifying Activity
To check that things are running, from a browser on the host check out the following urls:

* [Myriad UI](http://10.141.141.20:8192/)
* [Mesos UI - Frameworks](http://10.141.141.20:5050/#/frameworks)

### Shutting Down
To shut down from the vagrant ssh console, do the following:

```
yarn-daemon.sh stop resourcemanager

./shutdown.sh

exit

exit

vagrant halt
```