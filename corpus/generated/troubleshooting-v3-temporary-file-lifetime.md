---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: temporary file lifetime (Ironclad v3)

Start here when the temporary file lifetime does not behave as configured. Most reports turn out to be one of three causes, listed in the order to check them.

## Symptoms

- The service uses a different temporary file lifetime from the one you set.
- The log shows `E1196: IRONCLAD_TEMPORARY_FILE_LIFETIME out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 111 to 8772 items. Out of range, the value is rejected with `E1196: IRONCLAD_TEMPORARY_FILE_LIFETIME out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_TEMPORARY_FILE_LIFETIME` to see the value in use.

## Check 2: has it taken effect?

The value is reloaded within a few seconds of being changed. No restart is needed, and work already in progress picks up the new value on its next step.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `temporary_file_lifetime`. In version 3 it is warned. The setting that counts is `IRONCLAD_TEMPORARY_FILE_LIFETIME`, and its default is 2623 items.

## What the metrics show

Watch `ironclad_temporary_file_lifetime_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
