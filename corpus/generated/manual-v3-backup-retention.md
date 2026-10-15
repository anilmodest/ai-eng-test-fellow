---
product: Ironclad Endpoint Manager
version: v3
section: Security
---

# Backup retention (Ironclad v3)

In Ironclad Endpoint Manager, the backup retention is a single value measured in characters. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## Where the setting lives

The setting is `IRONCLAD_BACKUP_RETENTION`, as the environment variable. It takes a whole number of characters. The default is **559 characters**.

```
export IRONCLAD_BACKUP_RETENTION=559
```

## Upgrading from version 2

`backup_retention`, the version 2 setting, is no longer used. If it is still present the service **reads it, ignores it and starts normally**. Nothing is written to the log. An installation upgraded from version 2 without this change therefore runs on the version 3 default of 559 characters, not on the value in the old file.

## How it works

The backup retention is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Choosing a value

Start from the default of 559 characters and change it only with a reason you can write down. Raising the backup retention trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 3329 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_backup_retention_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 60. The highest accepted value is 3329. A value outside that range is rejected and the previous value stays in force, with `E1522: IRONCLAD_BACKUP_RETENTION out of range` in the log.

## Examples

| Value (characters) | When to use it |
| --- | --- |
| 60 | small installations, or testing |
| 559 | the default; right for most installations |
| 1118 | busy installations with spare capacity |
| 3329 | the maximum; only with a reason written down |

## Interactions

The backup retention is often changed together with the webhook delivery timeout (`IRONCLAD_WEBHOOK_DELIVERY_TIMEOUT`, default 393 megabytes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The backup retention is often changed together with the password expiry (`IRONCLAD_PASSWORD_EXPIRY`, default 40 connections in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_BACKUP_RETENTION` and given a new default of 559 characters in release 3.2. Before that release, version 3 still used the version 2 name.

## Related

- Webhook delivery timeout: see the Webhook delivery timeout page for version 3.
- Password expiry: see the Password expiry page for version 3.
