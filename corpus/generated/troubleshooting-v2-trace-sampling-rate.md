---
product: Ironclad Endpoint Manager
version: v2
section: Troubleshooting
---

# Troubleshooting: trace sampling rate (Ironclad v2)

Problems with the trace sampling rate are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different trace sampling rate from the one you set.
- The log shows `E1533: trace_sampling_rate out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 3 to 513 seconds. Out of range, the value is rejected with `E1533: trace_sampling_rate out of range` and the previous value stays in force. Run `ironcladctl config show trace_sampling_rate` to see the value in use.

## Check 2: has it taken effect?

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Check 3: is it set in the right place?

In version 2 the setting lives in `ironclad.conf`, in the `[jobs]` block. A value set anywhere else is not read.

## What the metrics show

Watch `ironclad_trace_sampling_rate_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
