---
product: Ironclad Endpoint Manager
version: v2
section: Configuration
---

# Export batch size (Ironclad v2)

In Ironclad Endpoint Manager, the export batch size is a single value measured in requests per minute. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## Where the setting lives

The setting is `export_batch_size`, in `ironclad.conf`, in the `[security]` block. It takes a whole number of requests per minute. The default is **1036 requests per minute**.

```
export_batch_size = 1036
```

## How it works

Every request carries the export batch size that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Choosing a value

Start from the default of 1036 requests per minute and change it only with a reason you can write down. Raising the export batch size trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 4711 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_export_batch_size_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 55. The highest accepted value is 4711. A value outside that range is rejected and the previous value stays in force, with `E1124: export_batch_size out of range` in the log.

## Examples

| Value (requests per minute) | When to use it |
| --- | --- |
| 55 | small installations, or testing |
| 1036 | the default; right for most installations |
| 2072 | busy installations with spare capacity |
| 4711 | the maximum; only with a reason written down |

## Interactions

The export batch size is often changed together with the session timeout (`session_timeout_min`, default 42 minutes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The export batch size is often changed together with the search result limit (`search_result_limit`, default 27 percent in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `export_batch_size`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Session timeout: see the Session timeout page for version 2.
- Search result limit: see the Search result limit page for version 2.
