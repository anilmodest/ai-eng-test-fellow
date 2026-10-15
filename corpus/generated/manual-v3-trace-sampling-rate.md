---
product: Ironclad Endpoint Manager
version: v3
section: Data
---

# Trace sampling rate (Ironclad v3)

This page describes the trace sampling rate setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `IRONCLAD_TRACE_SAMPLING_RATE`, as the environment variable. It takes a whole number of seconds. The default is **87 seconds**.

```
export IRONCLAD_TRACE_SAMPLING_RATE=87
```

## Upgrading from version 2

`trace_sampling_rate`, the version 2 setting, is no longer used. If it is still present the service **reads it, ignores it and starts normally**. Nothing is written to the log. An installation upgraded from version 2 without this change therefore runs on the version 3 default of 87 seconds, not on the value in the old file.

## How it works

Every request carries the trace sampling rate that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 87 seconds. Large ones usually settle between the default and twice the default. Values near the minimum of 1 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_trace_sampling_rate_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 1. The highest accepted value is 496. A value outside that range is rejected and the previous value stays in force, with `E1533: IRONCLAD_TRACE_SAMPLING_RATE out of range` in the log.

## Examples

| Value (seconds) | When to use it |
| --- | --- |
| 1 | small installations, or testing |
| 87 | the default; right for most installations |
| 174 | busy installations with spare capacity |
| 496 | the maximum; only with a reason written down |

## Interactions

The trace sampling rate is often changed together with the backup schedule interval (`IRONCLAD_BACKUP_SCHEDULE_INTERVAL`, default 562 megabytes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The trace sampling rate is often changed together with the bulk update limit (`IRONCLAD_BULK_UPDATE_LIMIT`, default 817 items in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_TRACE_SAMPLING_RATE` and given a new default of 87 seconds in release 3.1. Before that release, version 3 still used the version 2 name.

## Related

- Backup schedule interval: see the Backup schedule interval page for version 3.
- Bulk update limit: see the Bulk update limit page for version 3.
