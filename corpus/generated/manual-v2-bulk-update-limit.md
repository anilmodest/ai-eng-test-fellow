---
product: Ironclad Endpoint Manager
version: v2
section: Data
---

# Bulk update limit (Ironclad v2)

In Ironclad Endpoint Manager, the bulk update limit is a single value measured in items. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## Where the setting lives

The setting is `bulk_update_limit`, in `ironclad.conf`, in the `[server]` block. It takes a whole number of items. The default is **2897 items**.

```
bulk_update_limit = 2897
```

## How it works

The bulk update limit is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Choosing a value

Start from the default of 2897 items and change it only with a reason you can write down. Raising the bulk update limit trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 9526 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_bulk_update_limit_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 184. The highest accepted value is 9526. A value outside that range is rejected and the previous value stays in force, with `E1846: bulk_update_limit out of range` in the log.

## Examples

| Value (items) | When to use it |
| --- | --- |
| 184 | small installations, or testing |
| 2897 | the default; right for most installations |
| 5794 | busy installations with spare capacity |
| 9526 | the maximum; only with a reason written down |

## Interactions

The bulk update limit is often changed together with the backup schedule interval (`backup_schedule_interval`, default 67 megabytes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The bulk update limit is often changed together with the trace sampling rate (`trace_sampling_rate`, default 134 seconds in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `bulk_update_limit`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Backup schedule interval: see the Backup schedule interval page for version 2.
- Trace sampling rate: see the Trace sampling rate page for version 2.
