---
product: Ironclad Endpoint Manager
version: v2
section: Data
---

# Temporary file lifetime (Ironclad v2)

This page describes the temporary file lifetime setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `temporary_file_lifetime`, in `ironclad.conf`, in the `[network]` block. It takes a whole number of items. The default is **622 items**.

```
temporary_file_lifetime = 622
```

## How it works

The temporary file lifetime is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Choosing a value

Start from the default of 622 items and change it only with a reason you can write down. Raising the temporary file lifetime trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 7550 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_temporary_file_lifetime_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 128. The highest accepted value is 7550. A value outside that range is rejected and the previous value stays in force, with `E1196: temporary_file_lifetime out of range` in the log.

## Examples

| Value (items) | When to use it |
| --- | --- |
| 128 | small installations, or testing |
| 622 | the default; right for most installations |
| 1244 | busy installations with spare capacity |
| 7550 | the maximum; only with a reason written down |

## Interactions

The temporary file lifetime is often changed together with the backup schedule interval (`backup_schedule_interval`, default 67 megabytes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The temporary file lifetime is often changed together with the trace sampling rate (`trace_sampling_rate`, default 134 seconds in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `temporary_file_lifetime`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Backup schedule interval: see the Backup schedule interval page for version 2.
- Trace sampling rate: see the Trace sampling rate page for version 2.
