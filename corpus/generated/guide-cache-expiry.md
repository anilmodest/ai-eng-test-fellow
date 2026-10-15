---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the cache expiry

This page describes the cache expiry setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## How it works

Every request carries the cache expiry that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## Choosing a value

Start from the default of 2308 items and change it only with a reason you can write down. Raising the cache expiry trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 9874 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_cache_expiry_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `cache_expiry` | `IRONCLAD_CACHE_EXPIRY` |
| Default | 300 items | 2308 items |
| Range | 139–8716 | 191–9874 |
| Takes effect | next job | next job |

## A worked change

An administrator lowered the cache expiry to the minimum while testing and forgot to restore it. Failures tripled overnight. The activity log named the setting on every failure, which is how support found it in minutes rather than days.
