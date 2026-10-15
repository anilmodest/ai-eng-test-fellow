---
product: Ironclad Endpoint Manager
version: v2
section: Integrations
---

# Update deferral (Ironclad v2)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The update deferral setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `update_deferral_ite`, in `ironclad.conf`, in the `[jobs]` block. It takes a whole number of items. The default is **692 items**.

```
update_deferral_ite = 692
```

## How it works

Internally, the service checks the update deferral every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 692 items therefore means 'at least 692', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Choosing a value

Start from the default of 692 items and change it only with a reason you can write down. Raising the update deferral trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 7718 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_update_deferral_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 172. The highest accepted value is 7718. A value outside that range is rejected and the previous value stays in force, with `E1800: update_deferral_ite out of range` in the log.

## Examples

| Value (items) | When to use it |
| --- | --- |
| 172 | small installations, or testing |
| 692 | the default; right for most installations |
| 1384 | busy installations with spare capacity |
| 7718 | the maximum; only with a reason written down |

## Interactions

The update deferral is often changed together with the connection pool size (`connection_pool_size_req`, default 161 requests per minute in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The update deferral is often changed together with the request timeout (`request_timeout`, default 21 minutes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `update_deferral_ite`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Connection pool size: see the Connection pool size page for version 2.
- Request timeout: see the Request timeout page for version 2.
