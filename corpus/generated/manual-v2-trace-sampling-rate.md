---
product: Ironclad Endpoint Manager
version: v2
section: Data
---

# Trace sampling rate (Ironclad v2)

This page describes the trace sampling rate setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `trace_sampling_rate`, in `ironclad.conf`, in the `[jobs]` block. It takes a whole number of seconds. The default is **134 seconds**.

```
trace_sampling_rate = 134
```

## How it works

Every request carries the trace sampling rate that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 134 seconds. Large ones usually settle between the default and twice the default. Values near the minimum of 3 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

Watch `ironclad_trace_sampling_rate_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 3. The highest accepted value is 513. A value outside that range is rejected and the previous value stays in force, with `E1533: trace_sampling_rate out of range` in the log.

## Examples

| Value (seconds) | When to use it |
| --- | --- |
| 3 | small installations, or testing |
| 134 | the default; right for most installations |
| 268 | busy installations with spare capacity |
| 513 | the maximum; only with a reason written down |

## Interactions

The trace sampling rate is often changed together with the backup schedule interval (`backup_schedule_interval`, default 67 megabytes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The trace sampling rate is often changed together with the bulk update limit (`bulk_update_limit`, default 2897 items in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `trace_sampling_rate`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Backup schedule interval: see the Backup schedule interval page for version 2.
- Bulk update limit: see the Bulk update limit page for version 2.
