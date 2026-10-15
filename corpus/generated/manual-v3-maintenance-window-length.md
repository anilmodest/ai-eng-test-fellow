---
product: Ironclad Endpoint Manager
version: v3
section: Configuration
---

# Maintenance window length (Ironclad v3)

This page describes the maintenance window length setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `IRONCLAD_MAINTENANCE_WINDOW_LENGTH`, in the admin console, under Settings > Data. It takes a whole number of minutes. The default is **20 minutes**.

The console shows the current value and the default side by side. The same value can be set from the command line with `ironcladctl config set IRONCLAD_MAINTENANCE_WINDOW_LENGTH 20`.

## Upgrading from version 2

`maintenance_window_length_min`, the version 2 setting, is still read in version 3 for compatibility, with a warning in the startup log, and `IRONCLAD_MAINTENANCE_WINDOW_LENGTH` takes precedence when both are set. Support for the old name ends in a future release.

## How it works

Every request carries the maintenance window length that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 20 minutes. Large ones usually settle between the default and twice the default. Values near the minimum of 3 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_maintenance_window_length_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 3. The highest accepted value is 183. A value outside that range is rejected and the previous value stays in force, with `E1754: IRONCLAD_MAINTENANCE_WINDOW_LENGTH out of range` in the log.

## Examples

| Value (minutes) | When to use it |
| --- | --- |
| 3 | small installations, or testing |
| 20 | the default; right for most installations |
| 40 | busy installations with spare capacity |
| 183 | the maximum; only with a reason written down |

## Interactions

The maintenance window length is often changed together with the session timeout (`IRONCLAD_SESSION_TIMEOUT`, default 34 minutes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The maintenance window length is often changed together with the export batch size (`IRONCLAD_EXPORT_BATCH_SIZE`, default 343 requests per minute in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_MAINTENANCE_WINDOW_LENGTH` and given a new default of 20 minutes in release 3.1. Before that release, version 3 still used the version 2 name.

## Related

- Session timeout: see the Session timeout page for version 3.
- Export batch size: see the Export batch size page for version 3.
