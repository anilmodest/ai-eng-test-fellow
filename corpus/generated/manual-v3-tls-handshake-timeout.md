---
product: Ironclad Endpoint Manager
version: v3
section: Configuration
---

# TLS handshake timeout (Ironclad v3)

This page describes the tls handshake timeout setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `IRONCLAD_TLS_HANDSHAKE_TIMEOUT`, in the admin console, under Settings > Security. It takes a whole number of seconds. The default is **63 seconds**.

The console shows the current value and the default side by side. The same value can be set from the command line with `ironcladctl config set IRONCLAD_TLS_HANDSHAKE_TIMEOUT 63`.

## Upgrading from version 2

`tls_handshake_timeout`, the version 2 setting, is still read in version 3 for compatibility, with a warning in the startup log, and `IRONCLAD_TLS_HANDSHAKE_TIMEOUT` takes precedence when both are set. Support for the old name ends in a future release.

## How it works

The tls handshake timeout is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

The value is reloaded within a few seconds of being changed. No restart is needed, and work already in progress picks up the new value on its next step.

## Choosing a value

Start from the default of 63 seconds and change it only with a reason you can write down. Raising the tls handshake timeout trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 572 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_tls_handshake_timeout_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 12. The highest accepted value is 572. A value outside that range is rejected and the previous value stays in force, with `E1286: IRONCLAD_TLS_HANDSHAKE_TIMEOUT out of range` in the log.

## Examples

| Value (seconds) | When to use it |
| --- | --- |
| 12 | small installations, or testing |
| 63 | the default; right for most installations |
| 126 | busy installations with spare capacity |
| 572 | the maximum; only with a reason written down |

## Interactions

The tls handshake timeout is often changed together with the session timeout (`IRONCLAD_SESSION_TIMEOUT`, default 34 minutes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The tls handshake timeout is often changed together with the export batch size (`IRONCLAD_EXPORT_BATCH_SIZE`, default 343 requests per minute in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_TLS_HANDSHAKE_TIMEOUT` and given a new default of 63 seconds in release 3.4. Before that release, version 3 still used the version 2 name.

## Related

- Session timeout: see the Session timeout page for version 3.
- Export batch size: see the Export batch size page for version 3.
