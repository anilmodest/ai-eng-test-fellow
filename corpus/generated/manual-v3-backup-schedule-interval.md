---
product: Ironclad Endpoint Manager
version: v3
section: Data
---

# Backup schedule interval (Ironclad v3)

This page describes the backup schedule interval setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `IRONCLAD_BACKUP_SCHEDULE_INTERVAL`, as the environment variable. It takes a whole number of megabytes. The default is **562 megabytes**.

```
export IRONCLAD_BACKUP_SCHEDULE_INTERVAL=562
```

## Upgrading from version 2

`backup_schedule_interval`, the version 2 setting, is rejected. If it is still present the service refuses to start and logs `E1976: unknown setting backup_schedule_interval`. Remove it before upgrading.

## How it works

The backup schedule interval is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Choosing a value

Start from the default of 562 megabytes and change it only with a reason you can write down. Raising the backup schedule interval trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 1738 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_backup_schedule_interval_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 2. The highest accepted value is 1738. A value outside that range is rejected and the previous value stays in force, with `E1976: IRONCLAD_BACKUP_SCHEDULE_INTERVAL out of range` in the log.

## Examples

| Value (megabytes) | When to use it |
| --- | --- |
| 2 | small installations, or testing |
| 562 | the default; right for most installations |
| 1124 | busy installations with spare capacity |
| 1738 | the maximum; only with a reason written down |

## Interactions

The backup schedule interval is often changed together with the trace sampling rate (`IRONCLAD_TRACE_SAMPLING_RATE`, default 87 seconds in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The backup schedule interval is often changed together with the bulk update limit (`IRONCLAD_BULK_UPDATE_LIMIT`, default 817 items in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_BACKUP_SCHEDULE_INTERVAL` and given a new default of 562 megabytes in release 3.0. Before that release, version 3 still used the version 2 name.

## Related

- Trace sampling rate: see the Trace sampling rate page for version 3.
- Bulk update limit: see the Bulk update limit page for version 3.
