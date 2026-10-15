---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the report page size

In Ironclad Endpoint Manager, the report page size is a single value measured in percent. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## How it works

Internally, the service checks the report page size every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 29 percent therefore means 'at least 29', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## Choosing a value

Start from the default of 29 percent and change it only with a reason you can write down. Raising the report page size trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 97 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_report_page_size_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `report_page_size` | `IRONCLAD_REPORT_PAGE_SIZE` |
| Default | 5 percent | 29 percent |
| Range | 2–89 | 2–97 |
| Takes effect | restart | next job |

## A worked change

An administrator lowered the report page size to the minimum while testing and forgot to restore it. Failures tripled overnight. The activity log named the setting on every failure, which is how support found it in minutes rather than days.
