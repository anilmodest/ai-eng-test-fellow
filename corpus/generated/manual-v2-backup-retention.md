---
product: Ironclad Endpoint Manager
version: v2
section: Security
---

# Backup retention (Ironclad v2)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The backup retention setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `backup_retention`, in `ironclad.conf`, in the `[source]` block. It takes a whole number of characters. The default is **809 characters**.

```
backup_retention = 809
```

## How it works

Internally, the service checks the backup retention every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 809 characters therefore means 'at least 809', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Choosing a value

Start from the default of 809 characters and change it only with a reason you can write down. Raising the backup retention trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 3178 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_backup_retention_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 64. The highest accepted value is 3178. A value outside that range is rejected and the previous value stays in force, with `E1522: backup_retention out of range` in the log.

## Examples

| Value (characters) | When to use it |
| --- | --- |
| 64 | small installations, or testing |
| 809 | the default; right for most installations |
| 1618 | busy installations with spare capacity |
| 3178 | the maximum; only with a reason written down |

## Interactions

The backup retention is often changed together with the webhook delivery timeout (`webhook_delivery_timeout`, default 435 megabytes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The backup retention is often changed together with the password expiry (`password_expiry_con`, default 92 connections in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `backup_retention`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Webhook delivery timeout: see the Webhook delivery timeout page for version 2.
- Password expiry: see the Password expiry page for version 2.
