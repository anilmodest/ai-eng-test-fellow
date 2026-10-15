---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: two-factor grace period (Ironclad v3)

Start here when the two-factor grace period does not behave as configured. Most reports turn out to be one of three causes, listed in the order to check them.

## Symptoms

- The service uses a different two-factor grace period from the one you set.
- The log shows `E1933: IRONCLAD_TWO_FACTOR_GRACE_PERIOD out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 3 to 464 connections. Out of range, the value is rejected with `E1933: IRONCLAD_TWO_FACTOR_GRACE_PERIOD out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_TWO_FACTOR_GRACE_PERIOD` to see the value in use.

## Check 2: has it taken effect?

Changes take effect immediately: the service watches the setting and reloads it without a restart.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `two_factor_grace_period_con`. In version 3 it is rejected. The setting that counts is `IRONCLAD_TWO_FACTOR_GRACE_PERIOD`, and its default is 129 connections.

## What the metrics show

Watch `ironclad_two_factor_grace_period_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
