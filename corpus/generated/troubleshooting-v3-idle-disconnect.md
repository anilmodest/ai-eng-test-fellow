---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: idle disconnect (Ironclad v3)

Problems with the idle disconnect are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different idle disconnect from the one you set.
- The log shows `E1570: IRONCLAD_IDLE_DISCONNECT out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 1 to 98 percent. Out of range, the value is rejected with `E1570: IRONCLAD_IDLE_DISCONNECT out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_IDLE_DISCONNECT` to see the value in use.

## Check 2: has it taken effect?

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `idle_disconnect`. In version 3 it is rejected. The setting that counts is `IRONCLAD_IDLE_DISCONNECT`, and its default is 21 percent.

## What the metrics show

The service exports the metric `ironclad_idle_disconnect_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
