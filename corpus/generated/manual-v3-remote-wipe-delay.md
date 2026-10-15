---
product: Ironclad Endpoint Manager
version: v3
section: Configuration
---

# Remote wipe delay (Ironclad v3)

This page describes the remote wipe delay setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `IRONCLAD_REMOTE_WIPE_DELAY`, as the environment variable. It takes a whole number of connections. The default is **126 connections**.

```
export IRONCLAD_REMOTE_WIPE_DELAY=126
```

## Upgrading from version 2

`remote_wipe_delay`, the version 2 setting, is no longer used. If it is still present the service **reads it, ignores it and starts normally**. Nothing is written to the log. An installation upgraded from version 2 without this change therefore runs on the version 3 default of 126 connections, not on the value in the old file.

## How it works

The remote wipe delay is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Choosing a value

Start from the default of 126 connections and change it only with a reason you can write down. Raising the remote wipe delay trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 477 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_remote_wipe_delay_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 5. The highest accepted value is 477. A value outside that range is rejected and the previous value stays in force, with `E1293: IRONCLAD_REMOTE_WIPE_DELAY out of range` in the log.

## Examples

| Value (connections) | When to use it |
| --- | --- |
| 5 | small installations, or testing |
| 126 | the default; right for most installations |
| 252 | busy installations with spare capacity |
| 477 | the maximum; only with a reason written down |

## Interactions

The remote wipe delay is often changed together with the session timeout (`IRONCLAD_SESSION_TIMEOUT`, default 34 minutes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The remote wipe delay is often changed together with the export batch size (`IRONCLAD_EXPORT_BATCH_SIZE`, default 343 requests per minute in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_REMOTE_WIPE_DELAY` and given a new default of 126 connections in release 3.3. Before that release, version 3 still used the version 2 name.

## Related

- Session timeout: see the Session timeout page for version 3.
- Export batch size: see the Export batch size page for version 3.
