---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the check-in interval

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The check-in interval setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## How it works

Every request carries the check-in interval that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## Choosing a value

Start from the default of 43 minutes and change it only with a reason you can write down. Raising the check-in interval trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 221 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_check_in_interval_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `check_in_interval` | `IRONCLAD_CHECK_IN_INTERVAL` |
| Default | 12 minutes | 43 minutes |
| Range | 3–237 | 1–221 |
| Takes effect | next job | next job |

## A worked change

A customer with 400 seats saw the limit hit every afternoon. They raised the check-in interval by a quarter, watched the limit-hit metric for a week, saw it fall by two thirds, and stopped there. They wrote the reason into their change log, which is what made the next upgrade painless.
