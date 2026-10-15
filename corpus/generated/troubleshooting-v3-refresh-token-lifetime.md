---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: refresh token lifetime (Ironclad v3)

Problems with the refresh token lifetime are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different refresh token lifetime from the one you set.
- The log shows `E1624: IRONCLAD_REFRESH_TOKEN_LIFETIME out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 3 to 566 seconds. Out of range, the value is rejected with `E1624: IRONCLAD_REFRESH_TOKEN_LIFETIME out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_REFRESH_TOKEN_LIFETIME` to see the value in use.

## Check 2: has it taken effect?

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `refresh_token_lifetime`. In version 3 it is rejected. The setting that counts is `IRONCLAD_REFRESH_TOKEN_LIFETIME`, and its default is 102 seconds.

## What the metrics show

Watch `ironclad_refresh_token_lifetime_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
