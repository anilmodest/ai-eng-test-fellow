---
product: Ironclad Endpoint Manager
version: v2
section: Security
---

# Token lifetime (Ironclad v2)

This page describes the token lifetime setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `token_lifetime_ite`, in `ironclad.conf`, in the `[storage]` block. It takes a whole number of items. The default is **1517 items**.

```
token_lifetime_ite = 1517
```

## How it works

Every request carries the token lifetime that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 1517 items. Large ones usually settle between the default and twice the default. Values near the minimum of 182 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

Watch `ironclad_token_lifetime_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 182. The highest accepted value is 8406. A value outside that range is rejected and the previous value stays in force, with `E1744: token_lifetime_ite out of range` in the log.

## Examples

| Value (items) | When to use it |
| --- | --- |
| 182 | small installations, or testing |
| 1517 | the default; right for most installations |
| 3034 | busy installations with spare capacity |
| 8406 | the maximum; only with a reason written down |

## Interactions

The token lifetime is often changed together with the webhook delivery timeout (`webhook_delivery_timeout`, default 435 megabytes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The token lifetime is often changed together with the backup retention (`backup_retention`, default 809 characters in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `token_lifetime_ite`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Webhook delivery timeout: see the Webhook delivery timeout page for version 2.
- Backup retention: see the Backup retention page for version 2.
