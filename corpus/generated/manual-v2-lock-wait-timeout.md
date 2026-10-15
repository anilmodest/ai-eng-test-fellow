---
product: Ironclad Endpoint Manager
version: v2
section: Operations
---

# Lock wait timeout (Ironclad v2)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The lock wait timeout setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `lock_wait_timeout`, in `ironclad.conf`, in the `[network]` block. It takes a whole number of minutes. The default is **22 minutes**.

```
lock_wait_timeout = 22
```

## How it works

The lock wait timeout is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Choosing a value

Start from the default of 22 minutes and change it only with a reason you can write down. Raising the lock wait timeout trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 211 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_lock_wait_timeout_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 3. The highest accepted value is 211. A value outside that range is rejected and the previous value stays in force, with `E1350: lock_wait_timeout out of range` in the log.

## Examples

| Value (minutes) | When to use it |
| --- | --- |
| 3 | small installations, or testing |
| 22 | the default; right for most installations |
| 44 | busy installations with spare capacity |
| 211 | the maximum; only with a reason written down |

## Interactions

The lock wait timeout is often changed together with the audit log retention (`audit_log_retention`, default 391 days in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The lock wait timeout is often changed together with the webhook retry count (`webhook_retry_count`, default 1558 items in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `lock_wait_timeout`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Audit log retention: see the Audit log retention page for version 2.
- Webhook retry count: see the Webhook retry count page for version 2.
