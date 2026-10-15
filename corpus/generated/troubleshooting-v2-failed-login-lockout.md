---
product: Ironclad Endpoint Manager
version: v2
section: Troubleshooting
---

# Troubleshooting: failed login lockout (Ironclad v2)

Start here when the failed login lockout does not behave as configured. Most reports turn out to be one of three causes, listed in the order to check them.

## Symptoms

- The service uses a different failed login lockout from the one you set.
- The log shows `E1457: failed_login_lockout_min out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 5 to 218 minutes. Out of range, the value is rejected with `E1457: failed_login_lockout_min out of range` and the previous value stays in force. Run `ironcladctl config show failed_login_lockout_min` to see the value in use.

## Check 2: has it taken effect?

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Check 3: is it set in the right place?

In version 2 the setting lives in `ironclad.conf`, in the `[network]` block. A value set anywhere else is not read.

## What the metrics show

The service exports the metric `ironclad_failed_login_lockout_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
