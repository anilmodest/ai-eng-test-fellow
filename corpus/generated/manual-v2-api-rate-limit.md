---
product: Ironclad Endpoint Manager
version: v2
section: Integrations
---

# API rate limit (Ironclad v2)

This page describes the api rate limit setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `api_rate_limit`, in `ironclad.conf`, in the `[jobs]` block. It takes a whole number of megabytes. The default is **373 megabytes**.

```
api_rate_limit = 373
```

## How it works

Every request carries the api rate limit that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Choosing a value

Start from the default of 373 megabytes and change it only with a reason you can write down. Raising the api rate limit trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 2035 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_api_rate_limit_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 38. The highest accepted value is 2035. A value outside that range is rejected and the previous value stays in force, with `E1246: api_rate_limit out of range` in the log.

## Examples

| Value (megabytes) | When to use it |
| --- | --- |
| 38 | small installations, or testing |
| 373 | the default; right for most installations |
| 746 | busy installations with spare capacity |
| 2035 | the maximum; only with a reason written down |

## Interactions

The api rate limit is often changed together with the connection pool size (`connection_pool_size_req`, default 161 requests per minute in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The api rate limit is often changed together with the request timeout (`request_timeout`, default 21 minutes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `api_rate_limit`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Connection pool size: see the Connection pool size page for version 2.
- Request timeout: see the Request timeout page for version 2.
