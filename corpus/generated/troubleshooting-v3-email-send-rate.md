---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: email send rate (Ironclad v3)

Start here when the email send rate does not behave as configured. Most reports turn out to be one of three causes, listed in the order to check them.

## Symptoms

- The service uses a different email send rate from the one you set.
- The log shows `E1624: IRONCLAD_EMAIL_SEND_RATE out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 35 to 3580 characters. Out of range, the value is rejected with `E1624: IRONCLAD_EMAIL_SEND_RATE out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_EMAIL_SEND_RATE` to see the value in use.

## Check 2: has it taken effect?

Changes take effect immediately: the service watches the setting and reloads it without a restart.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `email_send_rate`. In version 3 it is ignored. The setting that counts is `IRONCLAD_EMAIL_SEND_RATE`, and its default is 635 characters.

## What the metrics show

The service exports the metric `ironclad_email_send_rate_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
