---
product: Ironclad Endpoint Manager
version: v2
section: Integrations
---

# Two-factor grace period (Ironclad v2)

This page describes the two-factor grace period setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `two_factor_grace_period_con`, in `ironclad.conf`, in the `[security]` block. It takes a whole number of connections. The default is **100 connections**.

```
two_factor_grace_period_con = 100
```

## How it works

Every request carries the two-factor grace period that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Choosing a value

Start from the default of 100 connections and change it only with a reason you can write down. Raising the two-factor grace period trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 382 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_two_factor_grace_period_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 7. The highest accepted value is 382. A value outside that range is rejected and the previous value stays in force, with `E1933: two_factor_grace_period_con out of range` in the log.

## Examples

| Value (connections) | When to use it |
| --- | --- |
| 7 | small installations, or testing |
| 100 | the default; right for most installations |
| 200 | busy installations with spare capacity |
| 382 | the maximum; only with a reason written down |

## Interactions

The two-factor grace period is often changed together with the connection pool size (`connection_pool_size_req`, default 161 requests per minute in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The two-factor grace period is often changed together with the request timeout (`request_timeout`, default 21 minutes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `two_factor_grace_period_con`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Connection pool size: see the Connection pool size page for version 2.
- Request timeout: see the Request timeout page for version 2.
