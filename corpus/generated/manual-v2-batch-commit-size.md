---
product: Ironclad Endpoint Manager
version: v2
section: Configuration
---

# Batch commit size (Ironclad v2)

This page describes the batch commit size setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `batch_commit_size`, in `ironclad.conf`, in the `[network]` block. It takes a whole number of requests per minute. The default is **669 requests per minute**.

```
batch_commit_size = 669
```

## How it works

The batch commit size is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Choosing a value

Start from the default of 669 requests per minute and change it only with a reason you can write down. Raising the batch commit size trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 4676 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_batch_commit_size_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 112. The highest accepted value is 4676. A value outside that range is rejected and the previous value stays in force, with `E1704: batch_commit_size out of range` in the log.

## Examples

| Value (requests per minute) | When to use it |
| --- | --- |
| 112 | small installations, or testing |
| 669 | the default; right for most installations |
| 1338 | busy installations with spare capacity |
| 4676 | the maximum; only with a reason written down |

## Interactions

The batch commit size is often changed together with the session timeout (`session_timeout_min`, default 42 minutes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The batch commit size is often changed together with the export batch size (`export_batch_size`, default 1036 requests per minute in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `batch_commit_size`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Session timeout: see the Session timeout page for version 2.
- Export batch size: see the Export batch size page for version 2.
