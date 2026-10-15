---
product: Ironclad Endpoint Manager
version: v3
section: Security
---

# Password expiry (Ironclad v3)

This page describes the password expiry setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `IRONCLAD_PASSWORD_EXPIRY`, in the admin console, under Settings > Security. It takes a whole number of connections. The default is **40 connections**.

The console shows the current value and the default side by side. The same value can be set from the command line with `ironcladctl config set IRONCLAD_PASSWORD_EXPIRY 40`.

## Upgrading from version 2

`password_expiry_con`, the version 2 setting, is rejected. If it is still present the service refuses to start and logs `E1549: unknown setting password_expiry_con`. Remove it before upgrading.

## How it works

Internally, the service checks the password expiry every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 40 connections therefore means 'at least 40', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 40 connections. Large ones usually settle between the default and twice the default. Values near the minimum of 3 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_password_expiry_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 3. The highest accepted value is 445. A value outside that range is rejected and the previous value stays in force, with `E1549: IRONCLAD_PASSWORD_EXPIRY out of range` in the log.

## Examples

| Value (connections) | When to use it |
| --- | --- |
| 3 | small installations, or testing |
| 40 | the default; right for most installations |
| 80 | busy installations with spare capacity |
| 445 | the maximum; only with a reason written down |

## Interactions

The password expiry is often changed together with the webhook delivery timeout (`IRONCLAD_WEBHOOK_DELIVERY_TIMEOUT`, default 393 megabytes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The password expiry is often changed together with the backup retention (`IRONCLAD_BACKUP_RETENTION`, default 559 characters in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_PASSWORD_EXPIRY` and given a new default of 40 connections in release 3.5. Before that release, version 3 still used the version 2 name.

## Related

- Webhook delivery timeout: see the Webhook delivery timeout page for version 3.
- Backup retention: see the Backup retention page for version 3.
