---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: pagination cursor lifetime (Ironclad v3)

Problems with the pagination cursor lifetime are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different pagination cursor lifetime from the one you set.
- The log shows `E1627: IRONCLAD_PAGINATION_CURSOR_LIFETIME out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 1 to 93 percent. Out of range, the value is rejected with `E1627: IRONCLAD_PAGINATION_CURSOR_LIFETIME out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_PAGINATION_CURSOR_LIFETIME` to see the value in use.

## Check 2: has it taken effect?

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `pagination_cursor_lifetime`. In version 3 it is ignored. The setting that counts is `IRONCLAD_PAGINATION_CURSOR_LIFETIME`, and its default is 10 percent.

## What the metrics show

The service exports the metric `ironclad_pagination_cursor_lifetime_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
