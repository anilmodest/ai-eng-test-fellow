---
product: Ironclad Endpoint Manager
version: v2
section: Troubleshooting
---

# Troubleshooting: scheduler worker count (Ironclad v2)

Problems with the scheduler worker count are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different scheduler worker count from the one you set.
- The log shows `E1613: scheduler_worker_count out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 33 to 1742 megabytes. Out of range, the value is rejected with `E1613: scheduler_worker_count out of range` and the previous value stays in force. Run `ironcladctl config show scheduler_worker_count` to see the value in use.

## Check 2: has it taken effect?

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Check 3: is it set in the right place?

In version 2 the setting lives in `ironclad.conf`, in the `[source]` block. A value set anywhere else is not read.

## What the metrics show

The service exports the metric `ironclad_scheduler_worker_count_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
