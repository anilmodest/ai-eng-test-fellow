---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: token lifetime (Ironclad v3)

Start here when the token lifetime does not behave as configured. Most reports turn out to be one of three causes, listed in the order to check them.

## Symptoms

- The service uses a different token lifetime from the one you set.
- The log shows `E1744: IRONCLAD_TOKEN_LIFETIME out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 122 to 7524 items. Out of range, the value is rejected with `E1744: IRONCLAD_TOKEN_LIFETIME out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_TOKEN_LIFETIME` to see the value in use.

## Check 2: has it taken effect?

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `token_lifetime_ite`. In version 3 it is rejected. The setting that counts is `IRONCLAD_TOKEN_LIFETIME`, and its default is 271 items.

## What the metrics show

The service exports the metric `ironclad_token_lifetime_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
