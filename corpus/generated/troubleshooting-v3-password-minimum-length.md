---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: password minimum length (Ironclad v3)

Problems with the password minimum length are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different password minimum length from the one you set.
- The log shows `E1602: IRONCLAD_PASSWORD_MINIMUM_LENGTH out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 7 to 441 connections. Out of range, the value is rejected with `E1602: IRONCLAD_PASSWORD_MINIMUM_LENGTH out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_PASSWORD_MINIMUM_LENGTH` to see the value in use.

## Check 2: has it taken effect?

Changes take effect immediately: the service watches the setting and reloads it without a restart.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `password_minimum_length`. In version 3 it is rejected. The setting that counts is `IRONCLAD_PASSWORD_MINIMUM_LENGTH`, and its default is 125 connections.

## What the metrics show

Watch `ironclad_password_minimum_length_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
