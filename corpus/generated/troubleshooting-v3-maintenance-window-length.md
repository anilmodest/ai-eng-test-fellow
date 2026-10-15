---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: maintenance window length (Ironclad v3)

Problems with the maintenance window length are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different maintenance window length from the one you set.
- The log shows `E1754: IRONCLAD_MAINTENANCE_WINDOW_LENGTH out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 3 to 183 minutes. Out of range, the value is rejected with `E1754: IRONCLAD_MAINTENANCE_WINDOW_LENGTH out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_MAINTENANCE_WINDOW_LENGTH` to see the value in use.

## Check 2: has it taken effect?

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `maintenance_window_length_min`. In version 3 it is warned. The setting that counts is `IRONCLAD_MAINTENANCE_WINDOW_LENGTH`, and its default is 20 minutes.

## What the metrics show

Watch `ironclad_maintenance_window_length_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
