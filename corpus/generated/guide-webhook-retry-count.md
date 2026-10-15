---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the webhook retry count

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The webhook retry count setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## How it works

Every request carries the webhook retry count that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 2365 items. Large ones usually settle between the default and twice the default. Values near the minimum of 87 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

Watch `ironclad_webhook_retry_count_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `webhook_retry_count` | `IRONCLAD_WEBHOOK_RETRY_COUNT` |
| Default | 1558 items | 2365 items |
| Range | 52–9567 | 87–9276 |
| Takes effect | restart | next job |

## A worked change

An administrator lowered the webhook retry count to the minimum while testing and forgot to restore it. Failures tripled overnight. The activity log named the setting on every failure, which is how support found it in minutes rather than days.
