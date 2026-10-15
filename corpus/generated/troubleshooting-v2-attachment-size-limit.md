---
product: Ironclad Endpoint Manager
version: v2
section: Troubleshooting
---

# Troubleshooting: attachment size limit (Ironclad v2)

Start here when the attachment size limit does not behave as configured. Most reports turn out to be one of three causes, listed in the order to check them.

## Symptoms

- The service uses a different attachment size limit from the one you set.
- The log shows `E1171: attachment_size_limit out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 14 to 3213 days. Out of range, the value is rejected with `E1171: attachment_size_limit out of range` and the previous value stays in force. Run `ironcladctl config show attachment_size_limit` to see the value in use.

## Check 2: has it taken effect?

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Check 3: is it set in the right place?

In version 2 the setting lives in `ironclad.conf`, in the `[storage]` block. A value set anywhere else is not read.

## What the metrics show

Watch `ironclad_attachment_size_limit_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
