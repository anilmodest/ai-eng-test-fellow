---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: failed login lockout (Ironclad v3)

Start here when the failed login lockout does not behave as configured. Most reports turn out to be one of three causes, listed in the order to check them.

## Symptoms

- The service uses a different failed login lockout from the one you set.
- The log shows `E1457: IRONCLAD_FAILED_LOGIN_LOCKOUT out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 1 to 203 minutes. Out of range, the value is rejected with `E1457: IRONCLAD_FAILED_LOGIN_LOCKOUT out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_FAILED_LOGIN_LOCKOUT` to see the value in use.

## Check 2: has it taken effect?

Changes take effect immediately: the service watches the setting and reloads it without a restart.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `failed_login_lockout_min`. In version 3 it is rejected. The setting that counts is `IRONCLAD_FAILED_LOGIN_LOCKOUT`, and its default is 49 minutes.

## What the metrics show

The service exports the metric `ironclad_failed_login_lockout_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
