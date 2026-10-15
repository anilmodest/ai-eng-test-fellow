---
product: Ironclad Endpoint Manager
version: v2
section: Security
---

# Check-in interval (Ironclad v2)

This page describes the check-in interval setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `check_in_interval`, in `ironclad.conf`, in the `[source]` block. It takes a whole number of minutes. The default is **12 minutes**.

```
check_in_interval = 12
```

## How it works

Every request carries the check-in interval that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 12 minutes. Large ones usually settle between the default and twice the default. Values near the minimum of 3 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_check_in_interval_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 3. The highest accepted value is 237. A value outside that range is rejected and the previous value stays in force, with `E1394: check_in_interval out of range` in the log.

## Examples

| Value (minutes) | When to use it |
| --- | --- |
| 3 | small installations, or testing |
| 12 | the default; right for most installations |
| 24 | busy installations with spare capacity |
| 237 | the maximum; only with a reason written down |

## Interactions

The check-in interval is often changed together with the webhook delivery timeout (`webhook_delivery_timeout`, default 435 megabytes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The check-in interval is often changed together with the backup retention (`backup_retention`, default 809 characters in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `check_in_interval`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Webhook delivery timeout: see the Webhook delivery timeout page for version 2.
- Backup retention: see the Backup retention page for version 2.
