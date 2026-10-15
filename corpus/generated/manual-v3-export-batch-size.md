---
product: Ironclad Endpoint Manager
version: v3
section: Configuration
---

# Export batch size (Ironclad v3)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The export batch size setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `IRONCLAD_EXPORT_BATCH_SIZE`, in the admin console, under Settings > Configuration. It takes a whole number of requests per minute. The default is **343 requests per minute**.

The console shows the current value and the default side by side. The same value can be set from the command line with `ironcladctl config set IRONCLAD_EXPORT_BATCH_SIZE 343`.

## Upgrading from version 2

`export_batch_size`, the version 2 setting, is no longer used. If it is still present the service **reads it, ignores it and starts normally**. Nothing is written to the log. An installation upgraded from version 2 without this change therefore runs on the version 3 default of 343 requests per minute, not on the value in the old file.

## How it works

Internally, the service checks the export batch size every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 343 requests per minute therefore means 'at least 343', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 343 requests per minute. Large ones usually settle between the default and twice the default. Values near the minimum of 65 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_export_batch_size_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 65. The highest accepted value is 5106. A value outside that range is rejected and the previous value stays in force, with `E1124: IRONCLAD_EXPORT_BATCH_SIZE out of range` in the log.

## Examples

| Value (requests per minute) | When to use it |
| --- | --- |
| 65 | small installations, or testing |
| 343 | the default; right for most installations |
| 686 | busy installations with spare capacity |
| 5106 | the maximum; only with a reason written down |

## Interactions

The export batch size is often changed together with the session timeout (`IRONCLAD_SESSION_TIMEOUT`, default 34 minutes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The export batch size is often changed together with the search result limit (`IRONCLAD_SEARCH_RESULT_LIMIT`, default 17 percent in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_EXPORT_BATCH_SIZE` and given a new default of 343 requests per minute in release 3.2. Before that release, version 3 still used the version 2 name.

## Related

- Session timeout: see the Session timeout page for version 3.
- Search result limit: see the Search result limit page for version 3.
