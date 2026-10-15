---
product: Ironclad Endpoint Manager
version: v3
section: Operations
---

# Audit log retention (Ironclad v3)

This page describes the audit log retention setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `IRONCLAD_AUDIT_LOG_RETENTION`, in the admin console, under Settings > Security. It takes a whole number of days. The default is **1060 days**.

The console shows the current value and the default side by side. The same value can be set from the command line with `ironcladctl config set IRONCLAD_AUDIT_LOG_RETENTION 1060`.

## Upgrading from version 2

`audit_log_retention`, the version 2 setting, is rejected. If it is still present the service refuses to start and logs `E1829: unknown setting audit_log_retention`. Remove it before upgrading.

## How it works

Internally, the service checks the audit log retention every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 1060 days therefore means 'at least 1060', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

The value is reloaded within a few seconds of being changed. No restart is needed, and work already in progress picks up the new value on its next step.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 1060 days. Large ones usually settle between the default and twice the default. Values near the minimum of 1 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_audit_log_retention_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 1. The highest accepted value is 3336. A value outside that range is rejected and the previous value stays in force, with `E1829: IRONCLAD_AUDIT_LOG_RETENTION out of range` in the log.

## Examples

| Value (days) | When to use it |
| --- | --- |
| 1 | small installations, or testing |
| 1060 | the default; right for most installations |
| 2120 | busy installations with spare capacity |
| 3336 | the maximum; only with a reason written down |

## Interactions

The audit log retention is often changed together with the webhook retry count (`IRONCLAD_WEBHOOK_RETRY_COUNT`, default 2365 items in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The audit log retention is often changed together with the notification digest interval (`IRONCLAD_NOTIFICATION_DIGEST_INTERVAL`, default 40 seconds in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_AUDIT_LOG_RETENTION` and given a new default of 1060 days in release 3.2. Before that release, version 3 still used the version 2 name.

## Related

- Webhook retry count: see the Webhook retry count page for version 3.
- Notification digest interval: see the Notification digest interval page for version 3.
