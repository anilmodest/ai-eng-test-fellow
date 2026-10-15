---
product: Ironclad Endpoint Manager
version: v2
section: Troubleshooting
---

# Troubleshooting: connection pool size (Ironclad v2)

Start here when the connection pool size does not behave as configured. Most reports turn out to be one of three causes, listed in the order to check them.

## Symptoms

- The service uses a different connection pool size from the one you set.
- The log shows `E1438: connection_pool_size_req out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 89 to 4721 requests per minute. Out of range, the value is rejected with `E1438: connection_pool_size_req out of range` and the previous value stays in force. Run `ironcladctl config show connection_pool_size_req` to see the value in use.

## Check 2: has it taken effect?

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Check 3: is it set in the right place?

In version 2 the setting lives in `ironclad.conf`, in the `[source]` block. A value set anywhere else is not read.

## What the metrics show

The service exports the metric `ironclad_connection_pool_size_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
