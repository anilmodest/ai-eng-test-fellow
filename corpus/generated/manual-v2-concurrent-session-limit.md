---
product: Ironclad Endpoint Manager
version: v2
section: Security
---

# Concurrent session limit (Ironclad v2)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The concurrent session limit setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `concurrent_session_limit`, in `ironclad.conf`, in the `[network]` block. It takes a whole number of seconds. The default is **136 seconds**.

```
concurrent_session_limit = 136
```

## How it works

The concurrent session limit is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 136 seconds. Large ones usually settle between the default and twice the default. Values near the minimum of 5 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_concurrent_session_limit_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 5. The highest accepted value is 549. A value outside that range is rejected and the previous value stays in force, with `E1647: concurrent_session_limit out of range` in the log.

## Examples

| Value (seconds) | When to use it |
| --- | --- |
| 5 | small installations, or testing |
| 136 | the default; right for most installations |
| 272 | busy installations with spare capacity |
| 549 | the maximum; only with a reason written down |

## Interactions

The concurrent session limit is often changed together with the webhook delivery timeout (`webhook_delivery_timeout`, default 435 megabytes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The concurrent session limit is often changed together with the backup retention (`backup_retention`, default 809 characters in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `concurrent_session_limit`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Webhook delivery timeout: see the Webhook delivery timeout page for version 2.
- Backup retention: see the Backup retention page for version 2.
