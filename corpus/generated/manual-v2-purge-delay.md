---
product: Ironclad Endpoint Manager
version: v2
section: Configuration
---

# Purge delay (Ironclad v2)

In Ironclad Endpoint Manager, the purge delay is a single value measured in megabytes. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## Where the setting lives

The setting is `purge_delay`, in `ironclad.conf`, in the `[server]` block. It takes a whole number of megabytes. The default is **475 megabytes**.

```
purge_delay = 475
```

## How it works

Every request carries the purge delay that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Choosing a value

Start from the default of 475 megabytes and change it only with a reason you can write down. Raising the purge delay trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 1671 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_purge_delay_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 36. The highest accepted value is 1671. A value outside that range is rejected and the previous value stays in force, with `E1295: purge_delay out of range` in the log.

## Examples

| Value (megabytes) | When to use it |
| --- | --- |
| 36 | small installations, or testing |
| 475 | the default; right for most installations |
| 950 | busy installations with spare capacity |
| 1671 | the maximum; only with a reason written down |

## Interactions

The purge delay is often changed together with the session timeout (`session_timeout_min`, default 42 minutes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The purge delay is often changed together with the export batch size (`export_batch_size`, default 1036 requests per minute in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `purge_delay`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Session timeout: see the Session timeout page for version 2.
- Export batch size: see the Export batch size page for version 2.
