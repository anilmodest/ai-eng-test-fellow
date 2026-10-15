---
product: Ironclad Endpoint Manager
version: v2
section: Configuration
---

# Session timeout (Ironclad v2)

In Ironclad Endpoint Manager, the session timeout is a single value measured in minutes. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## Where the setting lives

The setting is `session_timeout_min`, in `ironclad.conf`, in the `[security]` block. It takes a whole number of minutes. The default is **42 minutes**.

```
session_timeout_min = 42
```

## How it works

Every request carries the session timeout that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 42 minutes. Large ones usually settle between the default and twice the default. Values near the minimum of 2 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

Watch `ironclad_session_timeout_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 2. The highest accepted value is 188. A value outside that range is rejected and the previous value stays in force, with `E1851: session_timeout_min out of range` in the log.

## Examples

| Value (minutes) | When to use it |
| --- | --- |
| 2 | small installations, or testing |
| 42 | the default; right for most installations |
| 84 | busy installations with spare capacity |
| 188 | the maximum; only with a reason written down |

## Interactions

The session timeout is often changed together with the export batch size (`export_batch_size`, default 1036 requests per minute in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The session timeout is often changed together with the search result limit (`search_result_limit`, default 27 percent in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `session_timeout_min`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Export batch size: see the Export batch size page for version 2.
- Search result limit: see the Search result limit page for version 2.
