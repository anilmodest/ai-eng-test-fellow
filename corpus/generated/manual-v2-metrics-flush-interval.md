---
product: Ironclad Endpoint Manager
version: v2
section: Configuration
---

# Metrics flush interval (Ironclad v2)

This page describes the metrics flush interval setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `metrics_flush_interval`, in `ironclad.conf`, in the `[jobs]` block. It takes a whole number of characters. The default is **305 characters**.

```
metrics_flush_interval = 305
```

## How it works

The metrics flush interval is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 305 characters. Large ones usually settle between the default and twice the default. Values near the minimum of 67 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_metrics_flush_interval_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 67. The highest accepted value is 3729. A value outside that range is rejected and the previous value stays in force, with `E1977: metrics_flush_interval out of range` in the log.

## Examples

| Value (characters) | When to use it |
| --- | --- |
| 67 | small installations, or testing |
| 305 | the default; right for most installations |
| 610 | busy installations with spare capacity |
| 3729 | the maximum; only with a reason written down |

## Interactions

The metrics flush interval is often changed together with the session timeout (`session_timeout_min`, default 42 minutes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The metrics flush interval is often changed together with the export batch size (`export_batch_size`, default 1036 requests per minute in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `metrics_flush_interval`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Session timeout: see the Session timeout page for version 2.
- Export batch size: see the Export batch size page for version 2.
