---
product: Ironclad Endpoint Manager
version: v2
section: Security
---

# Password expiry (Ironclad v2)

This page describes the password expiry setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `password_expiry_con`, in `ironclad.conf`, in the `[jobs]` block. It takes a whole number of connections. The default is **92 connections**.

```
password_expiry_con = 92
```

## How it works

The password expiry is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Choosing a value

Start from the default of 92 connections and change it only with a reason you can write down. Raising the password expiry trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 432 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_password_expiry_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 7. The highest accepted value is 432. A value outside that range is rejected and the previous value stays in force, with `E1549: password_expiry_con out of range` in the log.

## Examples

| Value (connections) | When to use it |
| --- | --- |
| 7 | small installations, or testing |
| 92 | the default; right for most installations |
| 184 | busy installations with spare capacity |
| 432 | the maximum; only with a reason written down |

## Interactions

The password expiry is often changed together with the webhook delivery timeout (`webhook_delivery_timeout`, default 435 megabytes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The password expiry is often changed together with the backup retention (`backup_retention`, default 809 characters in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `password_expiry_con`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Webhook delivery timeout: see the Webhook delivery timeout page for version 2.
- Backup retention: see the Backup retention page for version 2.
