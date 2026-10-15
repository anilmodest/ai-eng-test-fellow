---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the connection pool size

This page describes the connection pool size setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## How it works

Internally, the service checks the connection pool size every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 383 requests per minute therefore means 'at least 383', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 383 requests per minute. Large ones usually settle between the default and twice the default. Values near the minimum of 40 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

Watch `ironclad_connection_pool_size_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `connection_pool_size_req` | `IRONCLAD_CONNECTION_POOL_SIZE` |
| Default | 161 requests per minute | 383 requests per minute |
| Range | 89–4721 | 40–4583 |
| Takes effect | restart | next job |

## A worked change

An administrator lowered the connection pool size to the minimum while testing and forgot to restore it. Failures tripled overnight. The activity log named the setting on every failure, which is how support found it in minutes rather than days.
