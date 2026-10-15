---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the tls handshake timeout

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The tls handshake timeout setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## How it works

The tls handshake timeout is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## Choosing a value

Start from the default of 63 seconds and change it only with a reason you can write down. Raising the tls handshake timeout trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 572 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_tls_handshake_timeout_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `tls_handshake_timeout` | `IRONCLAD_TLS_HANDSHAKE_TIMEOUT` |
| Default | 67 seconds | 63 seconds |
| Range | 3–497 | 12–572 |
| Takes effect | next job | immediately |

## A worked change

An administrator lowered the tls handshake timeout to the minimum while testing and forgot to restore it. Failures tripled overnight. The activity log named the setting on every failure, which is how support found it in minutes rather than days.
