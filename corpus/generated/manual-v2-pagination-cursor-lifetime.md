---
product: Ironclad Endpoint Manager
version: v2
section: Data
---

# Pagination cursor lifetime (Ironclad v2)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The pagination cursor lifetime setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `pagination_cursor_lifetime`, in `ironclad.conf`, in the `[security]` block. It takes a whole number of percent. The default is **8 percent**.

```
pagination_cursor_lifetime = 8
```

## How it works

The pagination cursor lifetime is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 8 percent. Large ones usually settle between the default and twice the default. Values near the minimum of 2 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

Watch `ironclad_pagination_cursor_lifetime_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 2. The highest accepted value is 84. A value outside that range is rejected and the previous value stays in force, with `E1627: pagination_cursor_lifetime out of range` in the log.

## Examples

| Value (percent) | When to use it |
| --- | --- |
| 2 | small installations, or testing |
| 8 | the default; right for most installations |
| 16 | busy installations with spare capacity |
| 84 | the maximum; only with a reason written down |

## Interactions

The pagination cursor lifetime is often changed together with the backup schedule interval (`backup_schedule_interval`, default 67 megabytes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The pagination cursor lifetime is often changed together with the trace sampling rate (`trace_sampling_rate`, default 134 seconds in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `pagination_cursor_lifetime`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Backup schedule interval: see the Backup schedule interval page for version 2.
- Trace sampling rate: see the Trace sampling rate page for version 2.
