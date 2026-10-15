---
product: Ironclad Endpoint Manager
version: v3
section: Operations
---

# Idle disconnect (Ironclad v3)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The idle disconnect setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `IRONCLAD_IDLE_DISCONNECT`, as the environment variable. It takes a whole number of percent. The default is **21 percent**.

```
export IRONCLAD_IDLE_DISCONNECT=21
```

## Upgrading from version 2

`idle_disconnect`, the version 2 setting, is rejected. If it is still present the service refuses to start and logs `E1570: unknown setting idle_disconnect`. Remove it before upgrading.

## How it works

Internally, the service checks the idle disconnect every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 21 percent therefore means 'at least 21', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Choosing a value

Start from the default of 21 percent and change it only with a reason you can write down. Raising the idle disconnect trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 98 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_idle_disconnect_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 1. The highest accepted value is 98. A value outside that range is rejected and the previous value stays in force, with `E1570: IRONCLAD_IDLE_DISCONNECT out of range` in the log.

## Examples

| Value (percent) | When to use it |
| --- | --- |
| 1 | small installations, or testing |
| 21 | the default; right for most installations |
| 42 | busy installations with spare capacity |
| 98 | the maximum; only with a reason written down |

## Interactions

The idle disconnect is often changed together with the audit log retention (`IRONCLAD_AUDIT_LOG_RETENTION`, default 1060 days in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The idle disconnect is often changed together with the webhook retry count (`IRONCLAD_WEBHOOK_RETRY_COUNT`, default 2365 items in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_IDLE_DISCONNECT` and given a new default of 21 percent in release 3.8. Before that release, version 3 still used the version 2 name.

## Related

- Audit log retention: see the Audit log retention page for version 3.
- Webhook retry count: see the Webhook retry count page for version 3.
