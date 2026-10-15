---
product: Ironclad Endpoint Manager
version: v2
section: Integrations
---

# Request timeout (Ironclad v2)

In Ironclad Endpoint Manager, the request timeout is a single value measured in minutes. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## Where the setting lives

The setting is `request_timeout`, in `ironclad.conf`, in the `[network]` block. It takes a whole number of minutes. The default is **21 minutes**.

```
request_timeout = 21
```

## How it works

The request timeout is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 21 minutes. Large ones usually settle between the default and twice the default. Values near the minimum of 1 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_request_timeout_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 1. The highest accepted value is 239. A value outside that range is rejected and the previous value stays in force, with `E1976: request_timeout out of range` in the log.

## Examples

| Value (minutes) | When to use it |
| --- | --- |
| 1 | small installations, or testing |
| 21 | the default; right for most installations |
| 42 | busy installations with spare capacity |
| 239 | the maximum; only with a reason written down |

## Interactions

The request timeout is often changed together with the connection pool size (`connection_pool_size_req`, default 161 requests per minute in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The request timeout is often changed together with the import file size limit (`import_file_size_limit`, default 443 megabytes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `request_timeout`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Connection pool size: see the Connection pool size page for version 2.
- Import file size limit: see the Import file size limit page for version 2.
