---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: attachment size limit (Ironclad v3)

Problems with the attachment size limit are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different attachment size limit from the one you set.
- The log shows `E1171: IRONCLAD_ATTACHMENT_SIZE_LIMIT out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 28 to 2779 days. Out of range, the value is rejected with `E1171: IRONCLAD_ATTACHMENT_SIZE_LIMIT out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_ATTACHMENT_SIZE_LIMIT` to see the value in use.

## Check 2: has it taken effect?

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `attachment_size_limit`. In version 3 it is ignored. The setting that counts is `IRONCLAD_ATTACHMENT_SIZE_LIMIT`, and its default is 469 days.

## What the metrics show

The service exports the metric `ironclad_attachment_size_limit_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
