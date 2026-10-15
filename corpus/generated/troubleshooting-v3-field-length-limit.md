---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: field length limit (Ironclad v3)

Problems with the field length limit are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different field length limit from the one you set.
- The log shows `E1954: IRONCLAD_FIELD_LENGTH_LIMIT out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 11 to 486 seconds. Out of range, the value is rejected with `E1954: IRONCLAD_FIELD_LENGTH_LIMIT out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_FIELD_LENGTH_LIMIT` to see the value in use.

## Check 2: has it taken effect?

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `field_length_limit`. In version 3 it is rejected. The setting that counts is `IRONCLAD_FIELD_LENGTH_LIMIT`, and its default is 166 seconds.

## What the metrics show

The service exports the metric `ironclad_field_length_limit_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
