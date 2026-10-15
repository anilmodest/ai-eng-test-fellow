---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: notification digest interval (Ironclad v3)

Problems with the notification digest interval are almost always configuration, not defects. Work through the checks below before opening a ticket.

## Symptoms

- The service uses a different notification digest interval from the one you set.
- The log shows `E1535: IRONCLAD_NOTIFICATION_DIGEST_INTERVAL out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 7 to 512 seconds. Out of range, the value is rejected with `E1535: IRONCLAD_NOTIFICATION_DIGEST_INTERVAL out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_NOTIFICATION_DIGEST_INTERVAL` to see the value in use.

## Check 2: has it taken effect?

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `notification_digest_interval`. In version 3 it is ignored. The setting that counts is `IRONCLAD_NOTIFICATION_DIGEST_INTERVAL`, and its default is 40 seconds.

## What the metrics show

Watch `ironclad_notification_digest_interval_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
