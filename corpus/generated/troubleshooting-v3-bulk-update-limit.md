---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: bulk update limit (Ironclad v3)

Start here when the bulk update limit does not behave as configured. Most reports turn out to be one of three causes, listed in the order to check them.

## Symptoms

- The service uses a different bulk update limit from the one you set.
- The log shows `E1846: IRONCLAD_BULK_UPDATE_LIMIT out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 34 to 8156 items. Out of range, the value is rejected with `E1846: IRONCLAD_BULK_UPDATE_LIMIT out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_BULK_UPDATE_LIMIT` to see the value in use.

## Check 2: has it taken effect?

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `bulk_update_limit`. In version 3 it is rejected. The setting that counts is `IRONCLAD_BULK_UPDATE_LIMIT`, and its default is 817 items.

## What the metrics show

Watch `ironclad_bulk_update_limit_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
