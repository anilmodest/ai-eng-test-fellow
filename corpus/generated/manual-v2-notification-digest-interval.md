---
product: Ironclad Endpoint Manager
version: v2
section: Operations
---

# Notification digest interval (Ironclad v2)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The notification digest interval setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `notification_digest_interval`, in `ironclad.conf`, in the `[storage]` block. It takes a whole number of seconds. The default is **87 seconds**.

```
notification_digest_interval = 87
```

## How it works

Internally, the service checks the notification digest interval every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 87 seconds therefore means 'at least 87', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Choosing a value

Start from the default of 87 seconds and change it only with a reason you can write down. Raising the notification digest interval trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 463 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_notification_digest_interval_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 5. The highest accepted value is 463. A value outside that range is rejected and the previous value stays in force, with `E1535: notification_digest_interval out of range` in the log.

## Examples

| Value (seconds) | When to use it |
| --- | --- |
| 5 | small installations, or testing |
| 87 | the default; right for most installations |
| 174 | busy installations with spare capacity |
| 463 | the maximum; only with a reason written down |

## Interactions

The notification digest interval is often changed together with the audit log retention (`audit_log_retention`, default 391 days in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The notification digest interval is often changed together with the webhook retry count (`webhook_retry_count`, default 1558 items in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `notification_digest_interval`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Audit log retention: see the Audit log retention page for version 2.
- Webhook retry count: see the Webhook retry count page for version 2.
