---
product: Ironclad Endpoint Manager
version: v2
section: Integrations
---

# Failed login lockout (Ironclad v2)

This page describes the failed login lockout setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `failed_login_lockout_min`, in `ironclad.conf`, in the `[network]` block. It takes a whole number of minutes. The default is **63 minutes**.

```
failed_login_lockout_min = 63
```

## How it works

Every request carries the failed login lockout that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 63 minutes. Large ones usually settle between the default and twice the default. Values near the minimum of 5 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_failed_login_lockout_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 5. The highest accepted value is 218. A value outside that range is rejected and the previous value stays in force, with `E1457: failed_login_lockout_min out of range` in the log.

## Examples

| Value (minutes) | When to use it |
| --- | --- |
| 5 | small installations, or testing |
| 63 | the default; right for most installations |
| 126 | busy installations with spare capacity |
| 218 | the maximum; only with a reason written down |

## Interactions

The failed login lockout is often changed together with the connection pool size (`connection_pool_size_req`, default 161 requests per minute in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The failed login lockout is often changed together with the request timeout (`request_timeout`, default 21 minutes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `failed_login_lockout_min`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Connection pool size: see the Connection pool size page for version 2.
- Request timeout: see the Request timeout page for version 2.
