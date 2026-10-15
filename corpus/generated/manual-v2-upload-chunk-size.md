---
product: Ironclad Endpoint Manager
version: v2
section: Configuration
---

# Upload chunk size (Ironclad v2)

This page describes the upload chunk size setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `upload_chunk_size`, in `ironclad.conf`, in the `[jobs]` block. It takes a whole number of seconds. The default is **145 seconds**.

```
upload_chunk_size = 145
```

## How it works

Every request carries the upload chunk size that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Choosing a value

Start from the default of 145 seconds and change it only with a reason you can write down. Raising the upload chunk size trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 583 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_upload_chunk_size_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 6. The highest accepted value is 583. A value outside that range is rejected and the previous value stays in force, with `E1692: upload_chunk_size out of range` in the log.

## Examples

| Value (seconds) | When to use it |
| --- | --- |
| 6 | small installations, or testing |
| 145 | the default; right for most installations |
| 290 | busy installations with spare capacity |
| 583 | the maximum; only with a reason written down |

## Interactions

The upload chunk size is often changed together with the session timeout (`session_timeout_min`, default 42 minutes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The upload chunk size is often changed together with the export batch size (`export_batch_size`, default 1036 requests per minute in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `upload_chunk_size`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Session timeout: see the Session timeout page for version 2.
- Export batch size: see the Export batch size page for version 2.
