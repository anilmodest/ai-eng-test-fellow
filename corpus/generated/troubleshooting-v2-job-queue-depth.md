---
product: Ironclad Endpoint Manager
version: v2
section: Troubleshooting
---

# Troubleshooting: job queue depth (Ironclad v2)

Start here when the job queue depth does not behave as configured. Most reports turn out to be one of three causes, listed in the order to check them.

## Symptoms

- The service uses a different job queue depth from the one you set.
- The log shows `E1483: job_queue_depth out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 44 to 3019 days. Out of range, the value is rejected with `E1483: job_queue_depth out of range` and the previous value stays in force. Run `ironcladctl config show job_queue_depth` to see the value in use.

## Check 2: has it taken effect?

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Check 3: is it set in the right place?

In version 2 the setting lives in `ironclad.conf`, in the `[server]` block. A value set anywhere else is not read.

## What the metrics show

The service exports the metric `ironclad_job_queue_depth_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
