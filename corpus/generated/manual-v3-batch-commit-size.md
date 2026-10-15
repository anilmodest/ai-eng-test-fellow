---
product: Ironclad Endpoint Manager
version: v3
section: Configuration
---

# Batch commit size (Ironclad v3)

This page describes the batch commit size setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `IRONCLAD_BATCH_COMMIT_SIZE`, in the admin console, under Settings > Data. It takes a whole number of requests per minute. The default is **1382 requests per minute**.

The console shows the current value and the default side by side. The same value can be set from the command line with `ironcladctl config set IRONCLAD_BATCH_COMMIT_SIZE 1382`.

## Upgrading from version 2

`batch_commit_size`, the version 2 setting, is no longer used. If it is still present the service **reads it, ignores it and starts normally**. Nothing is written to the log. An installation upgraded from version 2 without this change therefore runs on the version 3 default of 1382 requests per minute, not on the value in the old file.

## How it works

Internally, the service checks the batch commit size every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 1382 requests per minute therefore means 'at least 1382', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 1382 requests per minute. Large ones usually settle between the default and twice the default. Values near the minimum of 71 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

Watch `ironclad_batch_commit_size_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 71. The highest accepted value is 5674. A value outside that range is rejected and the previous value stays in force, with `E1704: IRONCLAD_BATCH_COMMIT_SIZE out of range` in the log.

## Examples

| Value (requests per minute) | When to use it |
| --- | --- |
| 71 | small installations, or testing |
| 1382 | the default; right for most installations |
| 2764 | busy installations with spare capacity |
| 5674 | the maximum; only with a reason written down |

## Interactions

The batch commit size is often changed together with the session timeout (`IRONCLAD_SESSION_TIMEOUT`, default 34 minutes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The batch commit size is often changed together with the export batch size (`IRONCLAD_EXPORT_BATCH_SIZE`, default 343 requests per minute in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_BATCH_COMMIT_SIZE` and given a new default of 1382 requests per minute in release 3.4. Before that release, version 3 still used the version 2 name.

## Related

- Session timeout: see the Session timeout page for version 3.
- Export batch size: see the Export batch size page for version 3.
