---
product: Ironclad Endpoint Manager
version: v3
section: Operations
---

# Notification digest interval (Ironclad v3)

This page describes the notification digest interval setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `IRONCLAD_NOTIFICATION_DIGEST_INTERVAL`, in the admin console, under Settings > Configuration. It takes a whole number of seconds. The default is **40 seconds**.

The console shows the current value and the default side by side. The same value can be set from the command line with `ironcladctl config set IRONCLAD_NOTIFICATION_DIGEST_INTERVAL 40`.

## Upgrading from version 2

`notification_digest_interval`, the version 2 setting, is no longer used. If it is still present the service **reads it, ignores it and starts normally**. Nothing is written to the log. An installation upgraded from version 2 without this change therefore runs on the version 3 default of 40 seconds, not on the value in the old file.

## How it works

Internally, the service checks the notification digest interval every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 40 seconds therefore means 'at least 40', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 40 seconds. Large ones usually settle between the default and twice the default. Values near the minimum of 7 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_notification_digest_interval_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 7. The highest accepted value is 512. A value outside that range is rejected and the previous value stays in force, with `E1535: IRONCLAD_NOTIFICATION_DIGEST_INTERVAL out of range` in the log.

## Examples

| Value (seconds) | When to use it |
| --- | --- |
| 7 | small installations, or testing |
| 40 | the default; right for most installations |
| 80 | busy installations with spare capacity |
| 512 | the maximum; only with a reason written down |

## Interactions

The notification digest interval is often changed together with the audit log retention (`IRONCLAD_AUDIT_LOG_RETENTION`, default 1060 days in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The notification digest interval is often changed together with the webhook retry count (`IRONCLAD_WEBHOOK_RETRY_COUNT`, default 2365 items in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_NOTIFICATION_DIGEST_INTERVAL` and given a new default of 40 seconds in release 3.0. Before that release, version 3 still used the version 2 name.

## Related

- Audit log retention: see the Audit log retention page for version 3.
- Webhook retry count: see the Webhook retry count page for version 3.
