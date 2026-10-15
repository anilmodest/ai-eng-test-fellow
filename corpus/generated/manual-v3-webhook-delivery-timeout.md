---
product: Ironclad Endpoint Manager
version: v3
section: Security
---

# Webhook delivery timeout (Ironclad v3)

This page describes the webhook delivery timeout setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `IRONCLAD_WEBHOOK_DELIVERY_TIMEOUT`, in the admin console, under Settings > Security. It takes a whole number of megabytes. The default is **393 megabytes**.

The console shows the current value and the default side by side. The same value can be set from the command line with `ironcladctl config set IRONCLAD_WEBHOOK_DELIVERY_TIMEOUT 393`.

## Upgrading from version 2

`webhook_delivery_timeout`, the version 2 setting, is no longer used. If it is still present the service **reads it, ignores it and starts normally**. Nothing is written to the log. An installation upgraded from version 2 without this change therefore runs on the version 3 default of 393 megabytes, not on the value in the old file.

## How it works

Internally, the service checks the webhook delivery timeout every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 393 megabytes therefore means 'at least 393', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 393 megabytes. Large ones usually settle between the default and twice the default. Values near the minimum of 9 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

Watch `ironclad_webhook_delivery_timeout_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 9. The highest accepted value is 1592. A value outside that range is rejected and the previous value stays in force, with `E1253: IRONCLAD_WEBHOOK_DELIVERY_TIMEOUT out of range` in the log.

## Examples

| Value (megabytes) | When to use it |
| --- | --- |
| 9 | small installations, or testing |
| 393 | the default; right for most installations |
| 786 | busy installations with spare capacity |
| 1592 | the maximum; only with a reason written down |

## Interactions

The webhook delivery timeout is often changed together with the backup retention (`IRONCLAD_BACKUP_RETENTION`, default 559 characters in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The webhook delivery timeout is often changed together with the password expiry (`IRONCLAD_PASSWORD_EXPIRY`, default 40 connections in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_WEBHOOK_DELIVERY_TIMEOUT` and given a new default of 393 megabytes in release 3.5. Before that release, version 3 still used the version 2 name.

## Related

- Backup retention: see the Backup retention page for version 3.
- Password expiry: see the Password expiry page for version 3.
