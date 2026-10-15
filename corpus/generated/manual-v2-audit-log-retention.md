---
product: Ironclad Endpoint Manager
version: v2
section: Operations
---

# Audit log retention (Ironclad v2)

This page describes the audit log retention setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `audit_log_retention`, in `ironclad.conf`, in the `[security]` block. It takes a whole number of days. The default is **391 days**.

```
audit_log_retention = 391
```

## How it works

The audit log retention is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Choosing a value

Start from the default of 391 days and change it only with a reason you can write down. Raising the audit log retention trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 3452 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_audit_log_retention_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 29. The highest accepted value is 3452. A value outside that range is rejected and the previous value stays in force, with `E1829: audit_log_retention out of range` in the log.

## Examples

| Value (days) | When to use it |
| --- | --- |
| 29 | small installations, or testing |
| 391 | the default; right for most installations |
| 782 | busy installations with spare capacity |
| 3452 | the maximum; only with a reason written down |

## Interactions

The audit log retention is often changed together with the webhook retry count (`webhook_retry_count`, default 1558 items in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The audit log retention is often changed together with the notification digest interval (`notification_digest_interval`, default 87 seconds in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `audit_log_retention`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Webhook retry count: see the Webhook retry count page for version 2.
- Notification digest interval: see the Notification digest interval page for version 2.
