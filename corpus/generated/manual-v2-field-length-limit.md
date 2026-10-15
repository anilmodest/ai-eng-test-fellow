---
product: Ironclad Endpoint Manager
version: v2
section: Integrations
---

# Field length limit (Ironclad v2)

In Ironclad Endpoint Manager, the field length limit is a single value measured in seconds. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## Where the setting lives

The setting is `field_length_limit`, in `ironclad.conf`, in the `[server]` block. It takes a whole number of seconds. The default is **123 seconds**.

```
field_length_limit = 123
```

## How it works

Every request carries the field length limit that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Choosing a value

Start from the default of 123 seconds and change it only with a reason you can write down. Raising the field length limit trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 479 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_field_length_limit_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 9. The highest accepted value is 479. A value outside that range is rejected and the previous value stays in force, with `E1954: field_length_limit out of range` in the log.

## Examples

| Value (seconds) | When to use it |
| --- | --- |
| 9 | small installations, or testing |
| 123 | the default; right for most installations |
| 246 | busy installations with spare capacity |
| 479 | the maximum; only with a reason written down |

## Interactions

The field length limit is often changed together with the connection pool size (`connection_pool_size_req`, default 161 requests per minute in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The field length limit is often changed together with the request timeout (`request_timeout`, default 21 minutes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `field_length_limit`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Connection pool size: see the Connection pool size page for version 2.
- Request timeout: see the Request timeout page for version 2.
