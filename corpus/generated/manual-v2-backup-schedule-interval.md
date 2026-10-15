---
product: Ironclad Endpoint Manager
version: v2
section: Data
---

# Backup schedule interval (Ironclad v2)

This page describes the backup schedule interval setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `backup_schedule_interval`, in `ironclad.conf`, in the `[source]` block. It takes a whole number of megabytes. The default is **67 megabytes**.

```
backup_schedule_interval = 67
```

## How it works

Every request carries the backup schedule interval that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 67 megabytes. Large ones usually settle between the default and twice the default. Values near the minimum of 10 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_backup_schedule_interval_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 10. The highest accepted value is 1873. A value outside that range is rejected and the previous value stays in force, with `E1976: backup_schedule_interval out of range` in the log.

## Examples

| Value (megabytes) | When to use it |
| --- | --- |
| 10 | small installations, or testing |
| 67 | the default; right for most installations |
| 134 | busy installations with spare capacity |
| 1873 | the maximum; only with a reason written down |

## Interactions

The backup schedule interval is often changed together with the trace sampling rate (`trace_sampling_rate`, default 134 seconds in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The backup schedule interval is often changed together with the bulk update limit (`bulk_update_limit`, default 2897 items in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `backup_schedule_interval`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Trace sampling rate: see the Trace sampling rate page for version 2.
- Bulk update limit: see the Bulk update limit page for version 2.
