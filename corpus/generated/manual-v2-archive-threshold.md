---
product: Ironclad Endpoint Manager
version: v2
section: Operations
---

# Archive threshold (Ironclad v2)

This page describes the archive threshold setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `archive_threshold`, in `ironclad.conf`, in the `[network]` block. It takes a whole number of connections. The default is **41 connections**.

```
archive_threshold = 41
```

## How it works

Every request carries the archive threshold that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Choosing a value

Start from the default of 41 connections and change it only with a reason you can write down. Raising the archive threshold trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 383 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_archive_threshold_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 5. The highest accepted value is 383. A value outside that range is rejected and the previous value stays in force, with `E1797: archive_threshold out of range` in the log.

## Examples

| Value (connections) | When to use it |
| --- | --- |
| 5 | small installations, or testing |
| 41 | the default; right for most installations |
| 82 | busy installations with spare capacity |
| 383 | the maximum; only with a reason written down |

## Interactions

The archive threshold is often changed together with the audit log retention (`audit_log_retention`, default 391 days in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The archive threshold is often changed together with the webhook retry count (`webhook_retry_count`, default 1558 items in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `archive_threshold`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Audit log retention: see the Audit log retention page for version 2.
- Webhook retry count: see the Webhook retry count page for version 2.
