---
product: Ironclad Endpoint Manager
version: v3
section: Security
---

# Token lifetime (Ironclad v3)

This page describes the token lifetime setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `IRONCLAD_TOKEN_LIFETIME`, as the environment variable. It takes a whole number of items. The default is **271 items**.

```
export IRONCLAD_TOKEN_LIFETIME=271
```

## Upgrading from version 2

`token_lifetime_ite`, the version 2 setting, is rejected. If it is still present the service refuses to start and logs `E1744: unknown setting token_lifetime_ite`. Remove it before upgrading.

## How it works

Every request carries the token lifetime that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Choosing a value

Start from the default of 271 items and change it only with a reason you can write down. Raising the token lifetime trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 7524 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_token_lifetime_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 122. The highest accepted value is 7524. A value outside that range is rejected and the previous value stays in force, with `E1744: IRONCLAD_TOKEN_LIFETIME out of range` in the log.

## Examples

| Value (items) | When to use it |
| --- | --- |
| 122 | small installations, or testing |
| 271 | the default; right for most installations |
| 542 | busy installations with spare capacity |
| 7524 | the maximum; only with a reason written down |

## Interactions

The token lifetime is often changed together with the webhook delivery timeout (`IRONCLAD_WEBHOOK_DELIVERY_TIMEOUT`, default 393 megabytes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The token lifetime is often changed together with the backup retention (`IRONCLAD_BACKUP_RETENTION`, default 559 characters in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_TOKEN_LIFETIME` and given a new default of 271 items in release 3.9. Before that release, version 3 still used the version 2 name.

## Related

- Webhook delivery timeout: see the Webhook delivery timeout page for version 3.
- Backup retention: see the Backup retention page for version 3.
