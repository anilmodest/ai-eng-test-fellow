---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the compliance grace period

This page describes the compliance grace period setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## How it works

Internally, the service checks the compliance grace period every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 7 percent therefore means 'at least 7', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## Choosing a value

Start from the default of 7 percent and change it only with a reason you can write down. Raising the compliance grace period trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 96 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_compliance_grace_period_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `compliance_grace_period_per` | `IRONCLAD_COMPLIANCE_GRACE_PERIOD` |
| Default | 9 percent | 7 percent |
| Range | 2–77 | 2–96 |
| Takes effect | restart | immediately |

## A worked change

An administrator lowered the compliance grace period to the minimum while testing and forgot to restore it. Failures tripled overnight. The activity log named the setting on every failure, which is how support found it in minutes rather than days.
