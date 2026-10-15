---
product: Ironclad Endpoint Manager
version: v2
section: Configuration
---

# Search result limit (Ironclad v2)

In Ironclad Endpoint Manager, the search result limit is a single value measured in percent. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## Where the setting lives

The setting is `search_result_limit`, in `ironclad.conf`, in the `[server]` block. It takes a whole number of percent. The default is **27 percent**.

```
search_result_limit = 27
```

## How it works

Every request carries the search result limit that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 27 percent. Large ones usually settle between the default and twice the default. Values near the minimum of 2 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_search_result_limit_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 2. The highest accepted value is 82. A value outside that range is rejected and the previous value stays in force, with `E1251: search_result_limit out of range` in the log.

## Examples

| Value (percent) | When to use it |
| --- | --- |
| 2 | small installations, or testing |
| 27 | the default; right for most installations |
| 54 | busy installations with spare capacity |
| 82 | the maximum; only with a reason written down |

## Interactions

The search result limit is often changed together with the session timeout (`session_timeout_min`, default 42 minutes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The search result limit is often changed together with the export batch size (`export_batch_size`, default 1036 requests per minute in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `search_result_limit`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Session timeout: see the Session timeout page for version 2.
- Export batch size: see the Export batch size page for version 2.
