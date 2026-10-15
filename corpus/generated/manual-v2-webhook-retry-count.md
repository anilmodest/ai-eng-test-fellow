---
product: Ironclad Endpoint Manager
version: v2
section: Operations
---

# Webhook retry count (Ironclad v2)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The webhook retry count setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `webhook_retry_count`, in `ironclad.conf`, in the `[jobs]` block. It takes a whole number of items. The default is **1558 items**.

```
webhook_retry_count = 1558
```

## How it works

The webhook retry count is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 1558 items. Large ones usually settle between the default and twice the default. Values near the minimum of 52 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

Watch `ironclad_webhook_retry_count_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 52. The highest accepted value is 9567. A value outside that range is rejected and the previous value stays in force, with `E1811: webhook_retry_count out of range` in the log.

## Examples

| Value (items) | When to use it |
| --- | --- |
| 52 | small installations, or testing |
| 1558 | the default; right for most installations |
| 3116 | busy installations with spare capacity |
| 9567 | the maximum; only with a reason written down |

## Interactions

The webhook retry count is often changed together with the audit log retention (`audit_log_retention`, default 391 days in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The webhook retry count is often changed together with the notification digest interval (`notification_digest_interval`, default 87 seconds in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `webhook_retry_count`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Audit log retention: see the Audit log retention page for version 2.
- Notification digest interval: see the Notification digest interval page for version 2.
