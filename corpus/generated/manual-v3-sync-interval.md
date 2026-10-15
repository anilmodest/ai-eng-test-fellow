---
product: Ironclad Endpoint Manager
version: v3
section: Operations
---

# Sync interval (Ironclad v3)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The sync interval setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `IRONCLAD_SYNC_INTERVAL`, as the environment variable. It takes a whole number of seconds. The default is **38 seconds**.

```
export IRONCLAD_SYNC_INTERVAL=38
```

## Upgrading from version 2

`sync_interval`, the version 2 setting, is no longer used. If it is still present the service **reads it, ignores it and starts normally**. Nothing is written to the log. An installation upgraded from version 2 without this change therefore runs on the version 3 default of 38 seconds, not on the value in the old file.

## How it works

Internally, the service checks the sync interval every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 38 seconds therefore means 'at least 38', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 38 seconds. Large ones usually settle between the default and twice the default. Values near the minimum of 6 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

Watch `ironclad_sync_interval_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 6. The highest accepted value is 453. A value outside that range is rejected and the previous value stays in force, with `E1114: IRONCLAD_SYNC_INTERVAL out of range` in the log.

## Examples

| Value (seconds) | When to use it |
| --- | --- |
| 6 | small installations, or testing |
| 38 | the default; right for most installations |
| 76 | busy installations with spare capacity |
| 453 | the maximum; only with a reason written down |

## Interactions

The sync interval is often changed together with the audit log retention (`IRONCLAD_AUDIT_LOG_RETENTION`, default 1060 days in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The sync interval is often changed together with the webhook retry count (`IRONCLAD_WEBHOOK_RETRY_COUNT`, default 2365 items in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_SYNC_INTERVAL` and given a new default of 38 seconds in release 3.4. Before that release, version 3 still used the version 2 name.

## Related

- Audit log retention: see the Audit log retention page for version 3.
- Webhook retry count: see the Webhook retry count page for version 3.
