---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: compliance grace period (Ironclad v3)

Problems with the compliance grace period are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different compliance grace period from the one you set.
- The log shows `E1501: IRONCLAD_COMPLIANCE_GRACE_PERIOD out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 2 to 96 percent. Out of range, the value is rejected with `E1501: IRONCLAD_COMPLIANCE_GRACE_PERIOD out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_COMPLIANCE_GRACE_PERIOD` to see the value in use.

## Check 2: has it taken effect?

Changes take effect immediately: the service watches the setting and reloads it without a restart.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `compliance_grace_period_per`. In version 3 it is ignored. The setting that counts is `IRONCLAD_COMPLIANCE_GRACE_PERIOD`, and its default is 7 percent.

## What the metrics show

The service exports the metric `ironclad_compliance_grace_period_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
