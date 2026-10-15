---
product: Ironclad Endpoint Manager
version: v3
section: Operations
---

# Archive threshold (Ironclad v3)

In Ironclad Endpoint Manager, the archive threshold is a single value measured in connections. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## Where the setting lives

The setting is `IRONCLAD_ARCHIVE_THRESHOLD`, as the environment variable. It takes a whole number of connections. The default is **27 connections**.

```
export IRONCLAD_ARCHIVE_THRESHOLD=27
```

## Upgrading from version 2

`archive_threshold`, the version 2 setting, is no longer used. If it is still present the service **reads it, ignores it and starts normally**. Nothing is written to the log. An installation upgraded from version 2 without this change therefore runs on the version 3 default of 27 connections, not on the value in the old file.

## How it works

Internally, the service checks the archive threshold every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 27 connections therefore means 'at least 27', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Choosing a value

Start from the default of 27 connections and change it only with a reason you can write down. Raising the archive threshold trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 466 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_archive_threshold_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 4. The highest accepted value is 466. A value outside that range is rejected and the previous value stays in force, with `E1797: IRONCLAD_ARCHIVE_THRESHOLD out of range` in the log.

## Examples

| Value (connections) | When to use it |
| --- | --- |
| 4 | small installations, or testing |
| 27 | the default; right for most installations |
| 54 | busy installations with spare capacity |
| 466 | the maximum; only with a reason written down |

## Interactions

The archive threshold is often changed together with the audit log retention (`IRONCLAD_AUDIT_LOG_RETENTION`, default 1060 days in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The archive threshold is often changed together with the webhook retry count (`IRONCLAD_WEBHOOK_RETRY_COUNT`, default 2365 items in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_ARCHIVE_THRESHOLD` and given a new default of 27 connections in release 3.4. Before that release, version 3 still used the version 2 name.

## Related

- Audit log retention: see the Audit log retention page for version 3.
- Webhook retry count: see the Webhook retry count page for version 3.
