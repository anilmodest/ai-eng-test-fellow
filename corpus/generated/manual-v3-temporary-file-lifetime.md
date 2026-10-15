---
product: Ironclad Endpoint Manager
version: v3
section: Data
---

# Temporary file lifetime (Ironclad v3)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The temporary file lifetime setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `IRONCLAD_TEMPORARY_FILE_LIFETIME`, as the environment variable. It takes a whole number of items. The default is **2623 items**.

```
export IRONCLAD_TEMPORARY_FILE_LIFETIME=2623
```

## Upgrading from version 2

`temporary_file_lifetime`, the version 2 setting, is still read in version 3 for compatibility, with a warning in the startup log, and `IRONCLAD_TEMPORARY_FILE_LIFETIME` takes precedence when both are set. Support for the old name ends in a future release.

## How it works

The temporary file lifetime is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

Changes take effect immediately: the service watches the setting and reloads it without a restart.

## Choosing a value

Start from the default of 2623 items and change it only with a reason you can write down. Raising the temporary file lifetime trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 8772 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_temporary_file_lifetime_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 111. The highest accepted value is 8772. A value outside that range is rejected and the previous value stays in force, with `E1196: IRONCLAD_TEMPORARY_FILE_LIFETIME out of range` in the log.

## Examples

| Value (items) | When to use it |
| --- | --- |
| 111 | small installations, or testing |
| 2623 | the default; right for most installations |
| 5246 | busy installations with spare capacity |
| 8772 | the maximum; only with a reason written down |

## Interactions

The temporary file lifetime is often changed together with the backup schedule interval (`IRONCLAD_BACKUP_SCHEDULE_INTERVAL`, default 562 megabytes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The temporary file lifetime is often changed together with the trace sampling rate (`IRONCLAD_TRACE_SAMPLING_RATE`, default 87 seconds in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_TEMPORARY_FILE_LIFETIME` and given a new default of 2623 items in release 3.3. Before that release, version 3 still used the version 2 name.

## Related

- Backup schedule interval: see the Backup schedule interval page for version 3.
- Trace sampling rate: see the Trace sampling rate page for version 3.
