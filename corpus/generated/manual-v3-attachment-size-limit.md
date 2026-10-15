---
product: Ironclad Endpoint Manager
version: v3
section: Configuration
---

# Attachment size limit (Ironclad v3)

In Ironclad Endpoint Manager, the attachment size limit is a single value measured in days. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## Where the setting lives

The setting is `IRONCLAD_ATTACHMENT_SIZE_LIMIT`, as the environment variable. It takes a whole number of days. The default is **469 days**.

```
export IRONCLAD_ATTACHMENT_SIZE_LIMIT=469
```

## Upgrading from version 2

`attachment_size_limit`, the version 2 setting, is no longer used. If it is still present the service **reads it, ignores it and starts normally**. Nothing is written to the log. An installation upgraded from version 2 without this change therefore runs on the version 3 default of 469 days, not on the value in the old file.

## How it works

Every request carries the attachment size limit that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Choosing a value

Start from the default of 469 days and change it only with a reason you can write down. Raising the attachment size limit trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 2779 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_attachment_size_limit_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 28. The highest accepted value is 2779. A value outside that range is rejected and the previous value stays in force, with `E1171: IRONCLAD_ATTACHMENT_SIZE_LIMIT out of range` in the log.

## Examples

| Value (days) | When to use it |
| --- | --- |
| 28 | small installations, or testing |
| 469 | the default; right for most installations |
| 938 | busy installations with spare capacity |
| 2779 | the maximum; only with a reason written down |

## Interactions

The attachment size limit is often changed together with the session timeout (`IRONCLAD_SESSION_TIMEOUT`, default 34 minutes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The attachment size limit is often changed together with the export batch size (`IRONCLAD_EXPORT_BATCH_SIZE`, default 343 requests per minute in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_ATTACHMENT_SIZE_LIMIT` and given a new default of 469 days in release 3.3. Before that release, version 3 still used the version 2 name.

## Related

- Session timeout: see the Session timeout page for version 3.
- Export batch size: see the Export batch size page for version 3.
