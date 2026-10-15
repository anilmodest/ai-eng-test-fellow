---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: cache expiry (Ironclad v3)

Problems with the cache expiry are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different cache expiry from the one you set.
- The log shows `E1719: IRONCLAD_CACHE_EXPIRY out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 191 to 9874 items. Out of range, the value is rejected with `E1719: IRONCLAD_CACHE_EXPIRY out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_CACHE_EXPIRY` to see the value in use.

## Check 2: has it taken effect?

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `cache_expiry`. In version 3 it is warned. The setting that counts is `IRONCLAD_CACHE_EXPIRY`, and its default is 2308 items.

## What the metrics show

The service exports the metric `ironclad_cache_expiry_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
