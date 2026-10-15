---
product: Ironclad Endpoint Manager
version: v2
section: Configuration
---

# Attachment size limit (Ironclad v2)

In Ironclad Endpoint Manager, the attachment size limit is a single value measured in days. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## Where the setting lives

The setting is `attachment_size_limit`, in `ironclad.conf`, in the `[storage]` block. It takes a whole number of days. The default is **508 days**.

```
attachment_size_limit = 508
```

## How it works

Internally, the service checks the attachment size limit every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 508 days therefore means 'at least 508', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Choosing a value

Start from the default of 508 days and change it only with a reason you can write down. Raising the attachment size limit trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 3213 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_attachment_size_limit_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 14. The highest accepted value is 3213. A value outside that range is rejected and the previous value stays in force, with `E1171: attachment_size_limit out of range` in the log.

## Examples

| Value (days) | When to use it |
| --- | --- |
| 14 | small installations, or testing |
| 508 | the default; right for most installations |
| 1016 | busy installations with spare capacity |
| 3213 | the maximum; only with a reason written down |

## Interactions

The attachment size limit is often changed together with the session timeout (`session_timeout_min`, default 42 minutes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The attachment size limit is often changed together with the export batch size (`export_batch_size`, default 1036 requests per minute in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `attachment_size_limit`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Session timeout: see the Session timeout page for version 2.
- Export batch size: see the Export batch size page for version 2.
