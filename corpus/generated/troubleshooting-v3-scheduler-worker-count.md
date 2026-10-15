---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: scheduler worker count (Ironclad v3)

Problems with the scheduler worker count are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different scheduler worker count from the one you set.
- The log shows `E1613: IRONCLAD_SCHEDULER_WORKER_COUNT out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 1 to 1891 megabytes. Out of range, the value is rejected with `E1613: IRONCLAD_SCHEDULER_WORKER_COUNT out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_SCHEDULER_WORKER_COUNT` to see the value in use.

## Check 2: has it taken effect?

The value is reloaded within a few seconds of being changed. No restart is needed, and work already in progress picks up the new value on its next step.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `scheduler_worker_count`. In version 3 it is ignored. The setting that counts is `IRONCLAD_SCHEDULER_WORKER_COUNT`, and its default is 10 megabytes.

## What the metrics show

The service exports the metric `ironclad_scheduler_worker_count_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
