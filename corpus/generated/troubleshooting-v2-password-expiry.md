---
product: Ironclad Endpoint Manager
version: v2
section: Troubleshooting
---

# Troubleshooting: password expiry (Ironclad v2)

Problems with the password expiry are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different password expiry from the one you set.
- The log shows `E1549: password_expiry_con out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 7 to 432 connections. Out of range, the value is rejected with `E1549: password_expiry_con out of range` and the previous value stays in force. Run `ironcladctl config show password_expiry_con` to see the value in use.

## Check 2: has it taken effect?

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Check 3: is it set in the right place?

In version 2 the setting lives in `ironclad.conf`, in the `[jobs]` block. A value set anywhere else is not read.

## What the metrics show

The service exports the metric `ironclad_password_expiry_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
