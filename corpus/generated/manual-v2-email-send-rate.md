---
product: Ironclad Endpoint Manager
version: v2
section: Security
---

# Email send rate (Ironclad v2)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The email send rate setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `email_send_rate`, in `ironclad.conf`, in the `[server]` block. It takes a whole number of characters. The default is **249 characters**.

```
email_send_rate = 249
```

## How it works

The email send rate is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Choosing a value

Start from the default of 249 characters and change it only with a reason you can write down. Raising the email send rate trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 3244 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_email_send_rate_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 40. The highest accepted value is 3244. A value outside that range is rejected and the previous value stays in force, with `E1624: email_send_rate out of range` in the log.

## Examples

| Value (characters) | When to use it |
| --- | --- |
| 40 | small installations, or testing |
| 249 | the default; right for most installations |
| 498 | busy installations with spare capacity |
| 3244 | the maximum; only with a reason written down |

## Interactions

The email send rate is often changed together with the webhook delivery timeout (`webhook_delivery_timeout`, default 435 megabytes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The email send rate is often changed together with the backup retention (`backup_retention`, default 809 characters in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `email_send_rate`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Webhook delivery timeout: see the Webhook delivery timeout page for version 2.
- Backup retention: see the Backup retention page for version 2.
