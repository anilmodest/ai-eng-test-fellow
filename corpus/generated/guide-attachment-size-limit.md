---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the attachment size limit

This page describes the attachment size limit setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## How it works

Internally, the service checks the attachment size limit every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 469 days therefore means 'at least 469', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## Choosing a value

Start from the default of 469 days and change it only with a reason you can write down. Raising the attachment size limit trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 2779 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_attachment_size_limit_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `attachment_size_limit` | `IRONCLAD_ATTACHMENT_SIZE_LIMIT` |
| Default | 508 days | 469 days |
| Range | 14–3213 | 28–2779 |
| Takes effect | restart | restart |

## A worked change

An administrator lowered the attachment size limit to the minimum while testing and forgot to restore it. Failures tripled overnight. The activity log named the setting on every failure, which is how support found it in minutes rather than days.
