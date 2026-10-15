---
product: Ironclad Endpoint Manager
version: v2
section: Security
---

# Scheduler worker count (Ironclad v2)

This page describes the scheduler worker count setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `scheduler_worker_count`, in `ironclad.conf`, in the `[source]` block. It takes a whole number of megabytes. The default is **510 megabytes**.

```
scheduler_worker_count = 510
```

## How it works

Every request carries the scheduler worker count that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Choosing a value

Start from the default of 510 megabytes and change it only with a reason you can write down. Raising the scheduler worker count trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 1742 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_scheduler_worker_count_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 33. The highest accepted value is 1742. A value outside that range is rejected and the previous value stays in force, with `E1613: scheduler_worker_count out of range` in the log.

## Examples

| Value (megabytes) | When to use it |
| --- | --- |
| 33 | small installations, or testing |
| 510 | the default; right for most installations |
| 1020 | busy installations with spare capacity |
| 1742 | the maximum; only with a reason written down |

## Interactions

The scheduler worker count is often changed together with the webhook delivery timeout (`webhook_delivery_timeout`, default 435 megabytes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The scheduler worker count is often changed together with the backup retention (`backup_retention`, default 809 characters in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `scheduler_worker_count`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Webhook delivery timeout: see the Webhook delivery timeout page for version 2.
- Backup retention: see the Backup retention page for version 2.
