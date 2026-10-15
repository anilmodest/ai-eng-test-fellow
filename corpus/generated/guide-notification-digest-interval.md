---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the notification digest interval

In Ironclad Endpoint Manager, the notification digest interval is a single value measured in seconds. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## How it works

Every request carries the notification digest interval that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 40 seconds. Large ones usually settle between the default and twice the default. Values near the minimum of 7 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_notification_digest_interval_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `notification_digest_interval` | `IRONCLAD_NOTIFICATION_DIGEST_INTERVAL` |
| Default | 87 seconds | 40 seconds |
| Range | 5–463 | 7–512 |
| Takes effect | restart | restart |

## A worked change

An administrator lowered the notification digest interval to the minimum while testing and forgot to restore it. Failures tripled overnight. The activity log named the setting on every failure, which is how support found it in minutes rather than days.
