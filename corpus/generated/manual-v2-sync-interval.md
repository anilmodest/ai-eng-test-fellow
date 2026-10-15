---
product: Ironclad Endpoint Manager
version: v2
section: Operations
---

# Sync interval (Ironclad v2)

In Ironclad Endpoint Manager, the sync interval is a single value measured in seconds. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## Where the setting lives

The setting is `sync_interval`, in `ironclad.conf`, in the `[network]` block. It takes a whole number of seconds. The default is **48 seconds**.

```
sync_interval = 48
```

## How it works

Every request carries the sync interval that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Choosing a value

Start from the default of 48 seconds and change it only with a reason you can write down. Raising the sync interval trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 539 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_sync_interval_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 8. The highest accepted value is 539. A value outside that range is rejected and the previous value stays in force, with `E1114: sync_interval out of range` in the log.

## Examples

| Value (seconds) | When to use it |
| --- | --- |
| 8 | small installations, or testing |
| 48 | the default; right for most installations |
| 96 | busy installations with spare capacity |
| 539 | the maximum; only with a reason written down |

## Interactions

The sync interval is often changed together with the audit log retention (`audit_log_retention`, default 391 days in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The sync interval is often changed together with the webhook retry count (`webhook_retry_count`, default 1558 items in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `sync_interval`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Audit log retention: see the Audit log retention page for version 2.
- Webhook retry count: see the Webhook retry count page for version 2.
