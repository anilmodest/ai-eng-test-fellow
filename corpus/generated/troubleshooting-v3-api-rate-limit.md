---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: api rate limit (Ironclad v3)

Problems with the api rate limit are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different api rate limit from the one you set.
- The log shows `E1246: IRONCLAD_API_RATE_LIMIT out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 32 to 1539 megabytes. Out of range, the value is rejected with `E1246: IRONCLAD_API_RATE_LIMIT out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_API_RATE_LIMIT` to see the value in use.

## Check 2: has it taken effect?

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `api_rate_limit`. In version 3 it is rejected. The setting that counts is `IRONCLAD_API_RATE_LIMIT`, and its default is 173 megabytes.

## What the metrics show

Watch `ironclad_api_rate_limit_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
