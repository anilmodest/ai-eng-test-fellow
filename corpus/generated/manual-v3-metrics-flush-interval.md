---
product: Ironclad Endpoint Manager
version: v3
section: Configuration
---

# Metrics flush interval (Ironclad v3)

This page describes the metrics flush interval setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `IRONCLAD_METRICS_FLUSH_INTERVAL`, as the environment variable. It takes a whole number of characters. The default is **583 characters**.

```
export IRONCLAD_METRICS_FLUSH_INTERVAL=583
```

## Upgrading from version 2

`metrics_flush_interval`, the version 2 setting, is no longer used. If it is still present the service **reads it, ignores it and starts normally**. Nothing is written to the log. An installation upgraded from version 2 without this change therefore runs on the version 3 default of 583 characters, not on the value in the old file.

## How it works

The metrics flush interval is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

The value is reloaded within a few seconds of being changed. No restart is needed, and work already in progress picks up the new value on its next step.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 583 characters. Large ones usually settle between the default and twice the default. Values near the minimum of 61 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_metrics_flush_interval_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 61. The highest accepted value is 3178. A value outside that range is rejected and the previous value stays in force, with `E1977: IRONCLAD_METRICS_FLUSH_INTERVAL out of range` in the log.

## Examples

| Value (characters) | When to use it |
| --- | --- |
| 61 | small installations, or testing |
| 583 | the default; right for most installations |
| 1166 | busy installations with spare capacity |
| 3178 | the maximum; only with a reason written down |

## Interactions

The metrics flush interval is often changed together with the session timeout (`IRONCLAD_SESSION_TIMEOUT`, default 34 minutes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The metrics flush interval is often changed together with the export batch size (`IRONCLAD_EXPORT_BATCH_SIZE`, default 343 requests per minute in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_METRICS_FLUSH_INTERVAL` and given a new default of 583 characters in release 3.6. Before that release, version 3 still used the version 2 name.

## Related

- Session timeout: see the Session timeout page for version 3.
- Export batch size: see the Export batch size page for version 3.
