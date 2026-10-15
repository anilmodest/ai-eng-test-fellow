---
product: Ironclad Endpoint Manager
version: v3
section: Data
---

# Bulk update limit (Ironclad v3)

In Ironclad Endpoint Manager, the bulk update limit is a single value measured in items. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## Where the setting lives

The setting is `IRONCLAD_BULK_UPDATE_LIMIT`, as the environment variable. It takes a whole number of items. The default is **817 items**.

```
export IRONCLAD_BULK_UPDATE_LIMIT=817
```

## Upgrading from version 2

`bulk_update_limit`, the version 2 setting, is rejected. If it is still present the service refuses to start and logs `E1846: unknown setting bulk_update_limit`. Remove it before upgrading.

## How it works

The bulk update limit is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Choosing a value

Start from the default of 817 items and change it only with a reason you can write down. Raising the bulk update limit trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 8156 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_bulk_update_limit_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 34. The highest accepted value is 8156. A value outside that range is rejected and the previous value stays in force, with `E1846: IRONCLAD_BULK_UPDATE_LIMIT out of range` in the log.

## Examples

| Value (items) | When to use it |
| --- | --- |
| 34 | small installations, or testing |
| 817 | the default; right for most installations |
| 1634 | busy installations with spare capacity |
| 8156 | the maximum; only with a reason written down |

## Interactions

The bulk update limit is often changed together with the backup schedule interval (`IRONCLAD_BACKUP_SCHEDULE_INTERVAL`, default 562 megabytes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The bulk update limit is often changed together with the trace sampling rate (`IRONCLAD_TRACE_SAMPLING_RATE`, default 87 seconds in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_BULK_UPDATE_LIMIT` and given a new default of 817 items in release 3.6. Before that release, version 3 still used the version 2 name.

## Related

- Backup schedule interval: see the Backup schedule interval page for version 3.
- Trace sampling rate: see the Trace sampling rate page for version 3.
