---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: backup schedule interval (Ironclad v3)

Problems with the backup schedule interval are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different backup schedule interval from the one you set.
- The log shows `E1976: IRONCLAD_BACKUP_SCHEDULE_INTERVAL out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 2 to 1738 megabytes. Out of range, the value is rejected with `E1976: IRONCLAD_BACKUP_SCHEDULE_INTERVAL out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_BACKUP_SCHEDULE_INTERVAL` to see the value in use.

## Check 2: has it taken effect?

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `backup_schedule_interval`. In version 3 it is rejected. The setting that counts is `IRONCLAD_BACKUP_SCHEDULE_INTERVAL`, and its default is 562 megabytes.

## What the metrics show

Watch `ironclad_backup_schedule_interval_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
