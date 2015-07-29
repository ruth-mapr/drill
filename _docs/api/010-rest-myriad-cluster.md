---
title: "Myriad Cluster API"
parent: "Myriad REST API"
---

## Description
The Cluster REST API is used to expand and shrink the cluster size with `{clusterId}`.


## HTTP Method and URI

```
PUT /api/cluster/flexup      // Expands the size of the cluster.
```

```
PUT /api/cluster/flexdown    // Shrinks the size of the cluster.
```

### Request Examples
The following request example expands the size of the cluster.

```json
{
  "instances":1, "profile": "small"
}
```

The following request example shrinks the size of the cluster.

```json
{
  "instances":1
}
```

### Response Example
```
200 OK
```
