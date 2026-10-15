---
product: Ironclad Endpoint Manager
version: v2
section: Configuration
---

# Maintenance window length (Ironclad v2)

This page describes the maintenance window length setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `maintenance_window_length_min`, in `ironclad.conf`, in the `[server]` block. It takes a whole number of minutes. The default is **31 minutes**.

```
maintenance_window_length_min = 31
```

## How it works

Every request carries the maintenance window length that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Choosing a value

Start from the default of 31 minutes and change it only with a reason you can write down. Raising the maintenance window length trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 195 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_maintenance_window_length_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 3. The highest accepted value is 195. A value outside that range is rejected and the previous value stays in force, with `E1754: maintenance_window_length_min out of range` in the log.

## Examples

| Value (minutes) | When to use it |
| --- | --- |
| 3 | small installations, or testing |
| 31 | the default; right for most installations |
| 62 | busy installations with spare capacity |
| 195 | the maximum; only with a reason written down |

## Interactions

The maintenance window length is often changed together with the session timeout (`session_timeout_min`, default 42 minutes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The maintenance window length is often changed together with the export batch size (`export_batch_size`, default 1036 requests per minute in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `maintenance_window_length_min`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Session timeout: see the Session timeout page for version 2.
- Export batch size: see the Export batch size page for version 2.
