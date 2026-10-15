---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: archive threshold (Ironclad v3)

Start here when the archive threshold does not behave as configured. Most reports turn out to be one of three causes, listed in the order to check them.

## Symptoms

- The service uses a different archive threshold from the one you set.
- The log shows `E1797: IRONCLAD_ARCHIVE_THRESHOLD out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 4 to 466 connections. Out of range, the value is rejected with `E1797: IRONCLAD_ARCHIVE_THRESHOLD out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_ARCHIVE_THRESHOLD` to see the value in use.

## Check 2: has it taken effect?

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `archive_threshold`. In version 3 it is ignored. The setting that counts is `IRONCLAD_ARCHIVE_THRESHOLD`, and its default is 27 connections.

## What the metrics show

Watch `ironclad_archive_threshold_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
