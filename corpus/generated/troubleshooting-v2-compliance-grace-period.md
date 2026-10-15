---
product: Ironclad Endpoint Manager
version: v2
section: Troubleshooting
---

# Troubleshooting: compliance grace period (Ironclad v2)

Problems with the compliance grace period are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different compliance grace period from the one you set.
- The log shows `E1501: compliance_grace_period_per out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 2 to 77 percent. Out of range, the value is rejected with `E1501: compliance_grace_period_per out of range` and the previous value stays in force. Run `ironcladctl config show compliance_grace_period_per` to see the value in use.

## Check 2: has it taken effect?

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Check 3: is it set in the right place?

In version 2 the setting lives in `ironclad.conf`, in the `[source]` block. A value set anywhere else is not read.

## What the metrics show

Watch `ironclad_compliance_grace_period_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
