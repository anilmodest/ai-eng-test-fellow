---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the backup schedule interval

In Ironclad Endpoint Manager, the backup schedule interval is a single value measured in megabytes. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## How it works

The backup schedule interval is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 562 megabytes. Large ones usually settle between the default and twice the default. Values near the minimum of 2 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

Watch `ironclad_backup_schedule_interval_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `backup_schedule_interval` | `IRONCLAD_BACKUP_SCHEDULE_INTERVAL` |
| Default | 67 megabytes | 562 megabytes |
| Range | 10–1873 | 2–1738 |
| Takes effect | next job | next job |

## A worked change

A customer with 400 seats saw the limit hit every afternoon. They raised the backup schedule interval by a quarter, watched the limit-hit metric for a week, saw it fall by two thirds, and stopped there. They wrote the reason into their change log, which is what made the next upgrade painless.
