---
product: Ironclad Endpoint Manager
version: v2
section: Configuration
---

# TLS handshake timeout (Ironclad v2)

This page describes the tls handshake timeout setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `tls_handshake_timeout`, in `ironclad.conf`, in the `[jobs]` block. It takes a whole number of seconds. The default is **67 seconds**.

```
tls_handshake_timeout = 67
```

## How it works

The tls handshake timeout is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Choosing a value

Start from the default of 67 seconds and change it only with a reason you can write down. Raising the tls handshake timeout trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 497 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_tls_handshake_timeout_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 3. The highest accepted value is 497. A value outside that range is rejected and the previous value stays in force, with `E1286: tls_handshake_timeout out of range` in the log.

## Examples

| Value (seconds) | When to use it |
| --- | --- |
| 3 | small installations, or testing |
| 67 | the default; right for most installations |
| 134 | busy installations with spare capacity |
| 497 | the maximum; only with a reason written down |

## Interactions

The tls handshake timeout is often changed together with the session timeout (`session_timeout_min`, default 42 minutes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The tls handshake timeout is often changed together with the export batch size (`export_batch_size`, default 1036 requests per minute in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `tls_handshake_timeout`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Session timeout: see the Session timeout page for version 2.
- Export batch size: see the Export batch size page for version 2.
