---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: request timeout (Ironclad v3)

Problems with the request timeout are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different request timeout from the one you set.
- The log shows `E1976: IRONCLAD_REQUEST_TIMEOUT out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 4 to 237 minutes. Out of range, the value is rejected with `E1976: IRONCLAD_REQUEST_TIMEOUT out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_REQUEST_TIMEOUT` to see the value in use.

## Check 2: has it taken effect?

The value is reloaded within a few seconds of being changed. No restart is needed, and work already in progress picks up the new value on its next step.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `request_timeout`. In version 3 it is rejected. The setting that counts is `IRONCLAD_REQUEST_TIMEOUT`, and its default is 37 minutes.

## What the metrics show

The service exports the metric `ironclad_request_timeout_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
