---
product: Ironclad Endpoint Manager
version: v2
section: Security
---

# Webhook delivery timeout (Ironclad v2)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The webhook delivery timeout setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `webhook_delivery_timeout`, in `ironclad.conf`, in the `[server]` block. It takes a whole number of megabytes. The default is **435 megabytes**.

```
webhook_delivery_timeout = 435
```

## How it works

Internally, the service checks the webhook delivery timeout every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 435 megabytes therefore means 'at least 435', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 435 megabytes. Large ones usually settle between the default and twice the default. Values near the minimum of 36 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_webhook_delivery_timeout_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 36. The highest accepted value is 1769. A value outside that range is rejected and the previous value stays in force, with `E1253: webhook_delivery_timeout out of range` in the log.

## Examples

| Value (megabytes) | When to use it |
| --- | --- |
| 36 | small installations, or testing |
| 435 | the default; right for most installations |
| 870 | busy installations with spare capacity |
| 1769 | the maximum; only with a reason written down |

## Interactions

The webhook delivery timeout is often changed together with the backup retention (`backup_retention`, default 809 characters in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The webhook delivery timeout is often changed together with the password expiry (`password_expiry_con`, default 92 connections in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `webhook_delivery_timeout`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Backup retention: see the Backup retention page for version 2.
- Password expiry: see the Password expiry page for version 2.
