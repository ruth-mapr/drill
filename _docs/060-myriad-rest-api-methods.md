---
title: "Myriad REST API Summary"
parent: "Myriad REST API"
---
The Myriad REST API provides the following functionality:

| API        | HTTP Method  | URI                    | Description  |
|------------|--------------|------------------------|--------------|
| Cluster    | PUT          | /api/cluster/flexup    | Expands the cluster size. |
| Cluster    | PUT          | /api/cluster/flexdown  | Shrinks the cluster size. |
| State      | GET          | /api/state             | Retrieves a snapshot of the Myriad Scheduler state |
| Configuration | GET       | /api/config            | Retrieves the Myriad configuration. |

