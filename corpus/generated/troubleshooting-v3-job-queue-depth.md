---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: job queue depth (Ironclad v3)

Start here when the job queue depth does not behave as configured. Most reports turn out to be one of three causes, listed in the order to check them.

## Symptoms

- The service uses a different job queue depth from the one you set.
- The log shows `E1483: IRONCLAD_JOB_QUEUE_DEPTH out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 56 to 2909 days. Out of range, the value is rejected with `E1483: IRONCLAD_JOB_QUEUE_DEPTH out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_JOB_QUEUE_DEPTH` to see the value in use.

## Check 2: has it taken effect?

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `job_queue_depth`. In version 3 it is rejected. The setting that counts is `IRONCLAD_JOB_QUEUE_DEPTH`, and its default is 461 days.

## What the metrics show

The service exports the metric `ironclad_job_queue_depth_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
