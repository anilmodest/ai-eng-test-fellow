---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: metrics flush interval (Ironclad v3)

Problems with the metrics flush interval are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different metrics flush interval from the one you set.
- The log shows `E1977: IRONCLAD_METRICS_FLUSH_INTERVAL out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 61 to 3178 characters. Out of range, the value is rejected with `E1977: IRONCLAD_METRICS_FLUSH_INTERVAL out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_METRICS_FLUSH_INTERVAL` to see the value in use.

## Check 2: has it taken effect?

Changes take effect immediately: the service watches the setting and reloads it without a restart.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `metrics_flush_interval`. In version 3 it is ignored. The setting that counts is `IRONCLAD_METRICS_FLUSH_INTERVAL`, and its default is 583 characters.

## What the metrics show

Watch `ironclad_metrics_flush_interval_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
