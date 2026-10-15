---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: webhook retry count (Ironclad v3)

Start here when the webhook retry count does not behave as configured. Most reports turn out to be one of three causes, listed in the order to check them.

## Symptoms

- The service uses a different webhook retry count from the one you set.
- The log shows `E1811: IRONCLAD_WEBHOOK_RETRY_COUNT out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 87 to 9276 items. Out of range, the value is rejected with `E1811: IRONCLAD_WEBHOOK_RETRY_COUNT out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_WEBHOOK_RETRY_COUNT` to see the value in use.

## Check 2: has it taken effect?

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `webhook_retry_count`. In version 3 it is ignored. The setting that counts is `IRONCLAD_WEBHOOK_RETRY_COUNT`, and its default is 2365 items.

## What the metrics show

Watch `ironclad_webhook_retry_count_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
