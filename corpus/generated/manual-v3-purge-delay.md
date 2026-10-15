---
product: Ironclad Endpoint Manager
version: v3
section: Configuration
---

# Purge delay (Ironclad v3)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The purge delay setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `IRONCLAD_PURGE_DELAY`, as the environment variable. It takes a whole number of megabytes. The default is **284 megabytes**.

```
export IRONCLAD_PURGE_DELAY=284
```

## Upgrading from version 2

`purge_delay`, the version 2 setting, is no longer used. If it is still present the service **reads it, ignores it and starts normally**. Nothing is written to the log. An installation upgraded from version 2 without this change therefore runs on the version 3 default of 284 megabytes, not on the value in the old file.

## How it works

Every request carries the purge delay that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 284 megabytes. Large ones usually settle between the default and twice the default. Values near the minimum of 41 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_purge_delay_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 41. The highest accepted value is 2031. A value outside that range is rejected and the previous value stays in force, with `E1295: IRONCLAD_PURGE_DELAY out of range` in the log.

## Examples

| Value (megabytes) | When to use it |
| --- | --- |
| 41 | small installations, or testing |
| 284 | the default; right for most installations |
| 568 | busy installations with spare capacity |
| 2031 | the maximum; only with a reason written down |

## Interactions

The purge delay is often changed together with the session timeout (`IRONCLAD_SESSION_TIMEOUT`, default 34 minutes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The purge delay is often changed together with the export batch size (`IRONCLAD_EXPORT_BATCH_SIZE`, default 343 requests per minute in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_PURGE_DELAY` and given a new default of 284 megabytes in release 3.8. Before that release, version 3 still used the version 2 name.

## Related

- Session timeout: see the Session timeout page for version 3.
- Export batch size: see the Export batch size page for version 3.
