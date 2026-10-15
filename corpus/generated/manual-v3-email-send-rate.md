---
product: Ironclad Endpoint Manager
version: v3
section: Security
---

# Email send rate (Ironclad v3)

In Ironclad Endpoint Manager, the email send rate is a single value measured in characters. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## Where the setting lives

The setting is `IRONCLAD_EMAIL_SEND_RATE`, as the environment variable. It takes a whole number of characters. The default is **635 characters**.

```
export IRONCLAD_EMAIL_SEND_RATE=635
```

## Upgrading from version 2

`email_send_rate`, the version 2 setting, is no longer used. If it is still present the service **reads it, ignores it and starts normally**. Nothing is written to the log. An installation upgraded from version 2 without this change therefore runs on the version 3 default of 635 characters, not on the value in the old file.

## How it works

Every request carries the email send rate that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is reloaded within a few seconds of being changed. No restart is needed, and work already in progress picks up the new value on its next step.

## Choosing a value

Start from the default of 635 characters and change it only with a reason you can write down. Raising the email send rate trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 3580 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_email_send_rate_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 35. The highest accepted value is 3580. A value outside that range is rejected and the previous value stays in force, with `E1624: IRONCLAD_EMAIL_SEND_RATE out of range` in the log.

## Examples

| Value (characters) | When to use it |
| --- | --- |
| 35 | small installations, or testing |
| 635 | the default; right for most installations |
| 1270 | busy installations with spare capacity |
| 3580 | the maximum; only with a reason written down |

## Interactions

The email send rate is often changed together with the webhook delivery timeout (`IRONCLAD_WEBHOOK_DELIVERY_TIMEOUT`, default 393 megabytes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The email send rate is often changed together with the backup retention (`IRONCLAD_BACKUP_RETENTION`, default 559 characters in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_EMAIL_SEND_RATE` and given a new default of 635 characters in release 3.1. Before that release, version 3 still used the version 2 name.

## Related

- Webhook delivery timeout: see the Webhook delivery timeout page for version 3.
- Backup retention: see the Backup retention page for version 3.
