---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the purge delay

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The purge delay setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## How it works

Every request carries the purge delay that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## Choosing a value

Start from the default of 284 megabytes and change it only with a reason you can write down. Raising the purge delay trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 2031 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_purge_delay_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `purge_delay` | `IRONCLAD_PURGE_DELAY` |
| Default | 475 megabytes | 284 megabytes |
| Range | 36–1671 | 41–2031 |
| Takes effect | restart | next job |

## A worked change

An administrator lowered the purge delay to the minimum while testing and forgot to restore it. Failures tripled overnight. The activity log named the setting on every failure, which is how support found it in minutes rather than days.
