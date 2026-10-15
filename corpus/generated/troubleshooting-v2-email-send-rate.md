---
product: Ironclad Endpoint Manager
version: v2
section: Troubleshooting
---

# Troubleshooting: email send rate (Ironclad v2)

Problems with the email send rate are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different email send rate from the one you set.
- The log shows `E1624: email_send_rate out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 40 to 3244 characters. Out of range, the value is rejected with `E1624: email_send_rate out of range` and the previous value stays in force. Run `ironcladctl config show email_send_rate` to see the value in use.

## Check 2: has it taken effect?

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Check 3: is it set in the right place?

In version 2 the setting lives in `ironclad.conf`, in the `[server]` block. A value set anywhere else is not read.

## What the metrics show

The service exports the metric `ironclad_email_send_rate_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
