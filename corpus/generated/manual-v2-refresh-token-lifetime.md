---
product: Ironclad Endpoint Manager
version: v2
section: Operations
---

# Refresh token lifetime (Ironclad v2)

In Ironclad Endpoint Manager, the refresh token lifetime is a single value measured in seconds. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## Where the setting lives

The setting is `refresh_token_lifetime`, in `ironclad.conf`, in the `[network]` block. It takes a whole number of seconds. The default is **69 seconds**.

```
refresh_token_lifetime = 69
```

## How it works

Internally, the service checks the refresh token lifetime every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 69 seconds therefore means 'at least 69', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Choosing a value

Start from the default of 69 seconds and change it only with a reason you can write down. Raising the refresh token lifetime trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 460 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_refresh_token_lifetime_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 9. The highest accepted value is 460. A value outside that range is rejected and the previous value stays in force, with `E1624: refresh_token_lifetime out of range` in the log.

## Examples

| Value (seconds) | When to use it |
| --- | --- |
| 9 | small installations, or testing |
| 69 | the default; right for most installations |
| 138 | busy installations with spare capacity |
| 460 | the maximum; only with a reason written down |

## Interactions

The refresh token lifetime is often changed together with the audit log retention (`audit_log_retention`, default 391 days in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The refresh token lifetime is often changed together with the webhook retry count (`webhook_retry_count`, default 1558 items in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `refresh_token_lifetime`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Audit log retention: see the Audit log retention page for version 2.
- Webhook retry count: see the Webhook retry count page for version 2.
