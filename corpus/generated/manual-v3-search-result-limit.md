---
product: Ironclad Endpoint Manager
version: v3
section: Configuration
---

# Search result limit (Ironclad v3)

In Ironclad Endpoint Manager, the search result limit is a single value measured in percent. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## Where the setting lives

The setting is `IRONCLAD_SEARCH_RESULT_LIMIT`, in the admin console, under Settings > Data. It takes a whole number of percent. The default is **17 percent**.

The console shows the current value and the default side by side. The same value can be set from the command line with `ironcladctl config set IRONCLAD_SEARCH_RESULT_LIMIT 17`.

## Upgrading from version 2

`search_result_limit`, the version 2 setting, is no longer used. If it is still present the service **reads it, ignores it and starts normally**. Nothing is written to the log. An installation upgraded from version 2 without this change therefore runs on the version 3 default of 17 percent, not on the value in the old file.

## How it works

Internally, the service checks the search result limit every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 17 percent therefore means 'at least 17', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Choosing a value

Start from the default of 17 percent and change it only with a reason you can write down. Raising the search result limit trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 80 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_search_result_limit_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 2. The highest accepted value is 80. A value outside that range is rejected and the previous value stays in force, with `E1251: IRONCLAD_SEARCH_RESULT_LIMIT out of range` in the log.

## Examples

| Value (percent) | When to use it |
| --- | --- |
| 2 | small installations, or testing |
| 17 | the default; right for most installations |
| 34 | busy installations with spare capacity |
| 80 | the maximum; only with a reason written down |

## Interactions

The search result limit is often changed together with the session timeout (`IRONCLAD_SESSION_TIMEOUT`, default 34 minutes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The search result limit is often changed together with the export batch size (`IRONCLAD_EXPORT_BATCH_SIZE`, default 343 requests per minute in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_SEARCH_RESULT_LIMIT` and given a new default of 17 percent in release 3.6. Before that release, version 3 still used the version 2 name.

## Related

- Session timeout: see the Session timeout page for version 3.
- Export batch size: see the Export batch size page for version 3.
