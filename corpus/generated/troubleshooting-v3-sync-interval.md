---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: sync interval (Ironclad v3)

Problems with the sync interval are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different sync interval from the one you set.
- The log shows `E1114: IRONCLAD_SYNC_INTERVAL out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 6 to 453 seconds. Out of range, the value is rejected with `E1114: IRONCLAD_SYNC_INTERVAL out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_SYNC_INTERVAL` to see the value in use.

## Check 2: has it taken effect?

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `sync_interval`. In version 3 it is ignored. The setting that counts is `IRONCLAD_SYNC_INTERVAL`, and its default is 38 seconds.

## What the metrics show

The service exports the metric `ironclad_sync_interval_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
