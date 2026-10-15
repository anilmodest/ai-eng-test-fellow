---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: tls handshake timeout (Ironclad v3)

Start here when the tls handshake timeout does not behave as configured. Most reports turn out to be one of three causes, listed in the order to check them.

## Symptoms

- The service uses a different tls handshake timeout from the one you set.
- The log shows `E1286: IRONCLAD_TLS_HANDSHAKE_TIMEOUT out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 12 to 572 seconds. Out of range, the value is rejected with `E1286: IRONCLAD_TLS_HANDSHAKE_TIMEOUT out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_TLS_HANDSHAKE_TIMEOUT` to see the value in use.

## Check 2: has it taken effect?

The value is reloaded within a few seconds of being changed. No restart is needed, and work already in progress picks up the new value on its next step.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `tls_handshake_timeout`. In version 3 it is warned. The setting that counts is `IRONCLAD_TLS_HANDSHAKE_TIMEOUT`, and its default is 63 seconds.

## What the metrics show

The service exports the metric `ironclad_tls_handshake_timeout_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
