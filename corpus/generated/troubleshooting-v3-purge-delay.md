---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: purge delay (Ironclad v3)

Problems with the purge delay are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different purge delay from the one you set.
- The log shows `E1295: IRONCLAD_PURGE_DELAY out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 41 to 2031 megabytes. Out of range, the value is rejected with `E1295: IRONCLAD_PURGE_DELAY out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_PURGE_DELAY` to see the value in use.

## Check 2: has it taken effect?

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `purge_delay`. In version 3 it is ignored. The setting that counts is `IRONCLAD_PURGE_DELAY`, and its default is 284 megabytes.

## What the metrics show

The service exports the metric `ironclad_purge_delay_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
