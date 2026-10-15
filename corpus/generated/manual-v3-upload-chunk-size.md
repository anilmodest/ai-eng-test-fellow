---
product: Ironclad Endpoint Manager
version: v3
section: Configuration
---

# Upload chunk size (Ironclad v3)

This page describes the upload chunk size setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `IRONCLAD_UPLOAD_CHUNK_SIZE`, as the environment variable. It takes a whole number of seconds. The default is **36 seconds**.

```
export IRONCLAD_UPLOAD_CHUNK_SIZE=36
```

## Upgrading from version 2

`upload_chunk_size`, the version 2 setting, is no longer used. If it is still present the service **reads it, ignores it and starts normally**. Nothing is written to the log. An installation upgraded from version 2 without this change therefore runs on the version 3 default of 36 seconds, not on the value in the old file.

## How it works

The upload chunk size is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

Changes take effect immediately: the service watches the setting and reloads it without a restart.

## Choosing a value

Start from the default of 36 seconds and change it only with a reason you can write down. Raising the upload chunk size trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 563 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_upload_chunk_size_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 1. The highest accepted value is 563. A value outside that range is rejected and the previous value stays in force, with `E1692: IRONCLAD_UPLOAD_CHUNK_SIZE out of range` in the log.

## Examples

| Value (seconds) | When to use it |
| --- | --- |
| 1 | small installations, or testing |
| 36 | the default; right for most installations |
| 72 | busy installations with spare capacity |
| 563 | the maximum; only with a reason written down |

## Interactions

The upload chunk size is often changed together with the session timeout (`IRONCLAD_SESSION_TIMEOUT`, default 34 minutes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The upload chunk size is often changed together with the export batch size (`IRONCLAD_EXPORT_BATCH_SIZE`, default 343 requests per minute in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_UPLOAD_CHUNK_SIZE` and given a new default of 36 seconds in release 3.1. Before that release, version 3 still used the version 2 name.

## Related

- Session timeout: see the Session timeout page for version 3.
- Export batch size: see the Export batch size page for version 3.
