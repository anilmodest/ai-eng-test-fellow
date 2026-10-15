---
product: Ironclad Endpoint Manager
version: v2
section: Troubleshooting
---

# Troubleshooting: archive threshold (Ironclad v2)

Problems with the archive threshold are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different archive threshold from the one you set.
- The log shows `E1797: archive_threshold out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 5 to 383 connections. Out of range, the value is rejected with `E1797: archive_threshold out of range` and the previous value stays in force. Run `ironcladctl config show archive_threshold` to see the value in use.

## Check 2: has it taken effect?

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Check 3: is it set in the right place?

In version 2 the setting lives in `ironclad.conf`, in the `[network]` block. A value set anywhere else is not read.

## What the metrics show

The service exports the metric `ironclad_archive_threshold_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
