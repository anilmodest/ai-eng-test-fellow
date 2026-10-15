---
product: Ironclad Endpoint Manager
version: v2
section: Operations
---

# Idle disconnect (Ironclad v2)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The idle disconnect setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `idle_disconnect`, in `ironclad.conf`, in the `[source]` block. It takes a whole number of percent. The default is **22 percent**.

```
idle_disconnect = 22
```

## How it works

Every request carries the idle disconnect that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Choosing a value

Start from the default of 22 percent and change it only with a reason you can write down. Raising the idle disconnect trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 88 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_idle_disconnect_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 2. The highest accepted value is 88. A value outside that range is rejected and the previous value stays in force, with `E1570: idle_disconnect out of range` in the log.

## Examples

| Value (percent) | When to use it |
| --- | --- |
| 2 | small installations, or testing |
| 22 | the default; right for most installations |
| 44 | busy installations with spare capacity |
| 88 | the maximum; only with a reason written down |

## Interactions

The idle disconnect is often changed together with the audit log retention (`audit_log_retention`, default 391 days in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The idle disconnect is often changed together with the webhook retry count (`webhook_retry_count`, default 1558 items in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `idle_disconnect`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Audit log retention: see the Audit log retention page for version 2.
- Webhook retry count: see the Webhook retry count page for version 2.
