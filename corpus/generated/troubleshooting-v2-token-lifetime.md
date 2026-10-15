---
product: Ironclad Endpoint Manager
version: v2
section: Troubleshooting
---

# Troubleshooting: token lifetime (Ironclad v2)

Start here when the token lifetime does not behave as configured. Most reports turn out to be one of three causes, listed in the order to check them.

## Symptoms

- The service uses a different token lifetime from the one you set.
- The log shows `E1744: token_lifetime_ite out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 182 to 8406 items. Out of range, the value is rejected with `E1744: token_lifetime_ite out of range` and the previous value stays in force. Run `ironcladctl config show token_lifetime_ite` to see the value in use.

## Check 2: has it taken effect?

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Check 3: is it set in the right place?

In version 2 the setting lives in `ironclad.conf`, in the `[storage]` block. A value set anywhere else is not read.

## What the metrics show

The service exports the metric `ironclad_token_lifetime_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
