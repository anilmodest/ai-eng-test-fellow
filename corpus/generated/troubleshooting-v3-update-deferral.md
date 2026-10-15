---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: update deferral (Ironclad v3)

Start here when the update deferral does not behave as configured. Most reports turn out to be one of three causes, listed in the order to check them.

## Symptoms

- The service uses a different update deferral from the one you set.
- The log shows `E1800: IRONCLAD_UPDATE_DEFERRAL out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 159 to 8640 items. Out of range, the value is rejected with `E1800: IRONCLAD_UPDATE_DEFERRAL out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_UPDATE_DEFERRAL` to see the value in use.

## Check 2: has it taken effect?

Changes take effect immediately: the service watches the setting and reloads it without a restart.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `update_deferral_ite`. In version 3 it is ignored. The setting that counts is `IRONCLAD_UPDATE_DEFERRAL`, and its default is 2560 items.

## What the metrics show

Watch `ironclad_update_deferral_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
