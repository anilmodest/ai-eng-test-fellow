---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: batch commit size (Ironclad v3)

Start here when the batch commit size does not behave as configured. Most reports turn out to be one of three causes, listed in the order to check them.

## Symptoms

- The service uses a different batch commit size from the one you set.
- The log shows `E1704: IRONCLAD_BATCH_COMMIT_SIZE out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 71 to 5674 requests per minute. Out of range, the value is rejected with `E1704: IRONCLAD_BATCH_COMMIT_SIZE out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_BATCH_COMMIT_SIZE` to see the value in use.

## Check 2: has it taken effect?

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `batch_commit_size`. In version 3 it is ignored. The setting that counts is `IRONCLAD_BATCH_COMMIT_SIZE`, and its default is 1382 requests per minute.

## What the metrics show

The service exports the metric `ironclad_batch_commit_size_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
