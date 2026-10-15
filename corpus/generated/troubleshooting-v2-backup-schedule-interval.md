---
product: Ironclad Endpoint Manager
version: v2
section: Troubleshooting
---

# Troubleshooting: backup schedule interval (Ironclad v2)

Problems with the backup schedule interval are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different backup schedule interval from the one you set.
- The log shows `E1976: backup_schedule_interval out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 10 to 1873 megabytes. Out of range, the value is rejected with `E1976: backup_schedule_interval out of range` and the previous value stays in force. Run `ironcladctl config show backup_schedule_interval` to see the value in use.

## Check 2: has it taken effect?

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Check 3: is it set in the right place?

In version 2 the setting lives in `ironclad.conf`, in the `[source]` block. A value set anywhere else is not read.

## What the metrics show

The service exports the metric `ironclad_backup_schedule_interval_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
