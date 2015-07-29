---
title: "Myriad Configuration API"
parent: "Myriad REST API"
---

## Description
The Configuration REST API is used to retrieve configuration information.


## HTTP Method and URI

```
GET /api/config
```


### Request Example

```
TBD
```

### Response Example

```json
{
    "mesosMaster": "10.10.30.131:5050",
    "checkpoint": false,
    "frameworkFailoverTimeout": 43200000,
    "frameworkName": "MyriadAlpha",
    "frameworkRole": "",
    "profiles": {
        "small": {
            "cpu": "1",
            "mem": "1100"
        },
        "medium": {
            "cpu": "2",
            "mem": "2048"
        },
        "large": {
            "cpu": "4",
            "mem": "4096"
        }
    },
    "rebalancer": false,
    "nativeLibrary": "/usr/local/lib/libmesos.so",
    "zkServers": "10.10.30.131:5181",
    "zkTimeout": 20000,
    "restApiPort": 8192,
    "yarnEnvironment": {
        "YARN_HOME": "/opt/mapr/hadoop/hadoop-2.5.1/",
        "YARN_NODEMANAGER_OPTS": "-Dyarn.nodemanager.resources.io-spindles=4.0 -Dyarn.resourcemanager.hostname=10.10.30.132"
    },
    "mesosAuthenticationPrincipal": "",
    "mesosAuthenticationSecretFilename": "",
    "nodeManagerConfiguration": {
        "jvmMaxMemoryMB": {
            "present": true
        },
        "user": {
            "present": true
        },
        "cpus": {
            "present": true
        },
        "jvmOpts": {
            "present": false
        },
        "cgroups": {
            "present": true
        }
    },
    "myriadExecutorConfiguration": {
        "jvmMaxMemoryMB": {
            "present": true
        },
        "path": "file:///root/myriad-executor-runnable-0.0.1.jar"
    }
}
```
