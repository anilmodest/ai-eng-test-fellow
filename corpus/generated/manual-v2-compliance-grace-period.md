---
product: Ironclad Endpoint Manager
version: v2
section: Operations
---

# Compliance grace period (Ironclad v2)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The compliance grace period setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `compliance_grace_period_per`, in `ironclad.conf`, in the `[source]` block. It takes a whole number of percent. The default is **9 percent**.

```
compliance_grace_period_per = 9
```

## How it works

Every request carries the compliance grace period that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Choosing a value

Start from the default of 9 percent and change it only with a reason you can write down. Raising the compliance grace period trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 77 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_compliance_grace_period_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 2. The highest accepted value is 77. A value outside that range is rejected and the previous value stays in force, with `E1501: compliance_grace_period_per out of range` in the log.

## Examples

| Value (percent) | When to use it |
| --- | --- |
| 2 | small installations, or testing |
| 9 | the default; right for most installations |
| 18 | busy installations with spare capacity |
| 77 | the maximum; only with a reason written down |

## Interactions

The compliance grace period is often changed together with the audit log retention (`audit_log_retention`, default 391 days in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The compliance grace period is often changed together with the webhook retry count (`webhook_retry_count`, default 1558 items in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `compliance_grace_period_per`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Audit log retention: see the Audit log retention page for version 2.
- Webhook retry count: see the Webhook retry count page for version 2.
