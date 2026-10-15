---
product: Ironclad Endpoint Manager
version: v2
section: Troubleshooting
---

# Troubleshooting: refresh token lifetime (Ironclad v2)

Start here when the refresh token lifetime does not behave as configured. Most reports turn out to be one of three causes, listed in the order to check them.

## Symptoms

- The service uses a different refresh token lifetime from the one you set.
- The log shows `E1624: refresh_token_lifetime out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 9 to 460 seconds. Out of range, the value is rejected with `E1624: refresh_token_lifetime out of range` and the previous value stays in force. Run `ironcladctl config show refresh_token_lifetime` to see the value in use.

## Check 2: has it taken effect?

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Check 3: is it set in the right place?

In version 2 the setting lives in `ironclad.conf`, in the `[network]` block. A value set anywhere else is not read.

## What the metrics show

Watch `ironclad_refresh_token_lifetime_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
