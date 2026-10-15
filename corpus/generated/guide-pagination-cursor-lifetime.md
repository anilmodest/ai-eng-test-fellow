---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the pagination cursor lifetime

This page describes the pagination cursor lifetime setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## How it works

Internally, the service checks the pagination cursor lifetime every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 10 percent therefore means 'at least 10', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## Choosing a value

Start from the default of 10 percent and change it only with a reason you can write down. Raising the pagination cursor lifetime trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 93 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_pagination_cursor_lifetime_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `pagination_cursor_lifetime` | `IRONCLAD_PAGINATION_CURSOR_LIFETIME` |
| Default | 8 percent | 10 percent |
| Range | 2–84 | 1–93 |
| Takes effect | restart | next job |

## A worked change

A customer with 400 seats saw the limit hit every afternoon. They raised the pagination cursor lifetime by a quarter, watched the limit-hit metric for a week, saw it fall by two thirds, and stopped there. They wrote the reason into their change log, which is what made the next upgrade painless.
