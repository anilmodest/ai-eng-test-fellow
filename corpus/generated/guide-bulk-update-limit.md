---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the bulk update limit

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The bulk update limit setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## How it works

Every request carries the bulk update limit that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## Choosing a value

Start from the default of 817 items and change it only with a reason you can write down. Raising the bulk update limit trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 8156 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_bulk_update_limit_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `bulk_update_limit` | `IRONCLAD_BULK_UPDATE_LIMIT` |
| Default | 2897 items | 817 items |
| Range | 184–9526 | 34–8156 |
| Takes effect | restart | restart |

## A worked change

An administrator lowered the bulk update limit to the minimum while testing and forgot to restore it. Failures tripled overnight. The activity log named the setting on every failure, which is how support found it in minutes rather than days.
