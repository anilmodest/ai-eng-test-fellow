---
product: Ironclad Endpoint Manager
version: v3
section: Security
---

# Scheduler worker count (Ironclad v3)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The scheduler worker count setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `IRONCLAD_SCHEDULER_WORKER_COUNT`, as the environment variable. It takes a whole number of megabytes. The default is **10 megabytes**.

```
export IRONCLAD_SCHEDULER_WORKER_COUNT=10
```

## Upgrading from version 2

`scheduler_worker_count`, the version 2 setting, is no longer used. If it is still present the service **reads it, ignores it and starts normally**. Nothing is written to the log. An installation upgraded from version 2 without this change therefore runs on the version 3 default of 10 megabytes, not on the value in the old file.

## How it works

Internally, the service checks the scheduler worker count every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 10 megabytes therefore means 'at least 10', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

The value is reloaded within a few seconds of being changed. No restart is needed, and work already in progress picks up the new value on its next step.

## Choosing a value

Start from the default of 10 megabytes and change it only with a reason you can write down. Raising the scheduler worker count trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 1891 are the most common source of tickets about this setting.

## Monitoring

The service exports the metric `ironclad_scheduler_worker_count_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 1. The highest accepted value is 1891. A value outside that range is rejected and the previous value stays in force, with `E1613: IRONCLAD_SCHEDULER_WORKER_COUNT out of range` in the log.

## Examples

| Value (megabytes) | When to use it |
| --- | --- |
| 1 | small installations, or testing |
| 10 | the default; right for most installations |
| 20 | busy installations with spare capacity |
| 1891 | the maximum; only with a reason written down |

## Interactions

The scheduler worker count is often changed together with the webhook delivery timeout (`IRONCLAD_WEBHOOK_DELIVERY_TIMEOUT`, default 393 megabytes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The scheduler worker count is often changed together with the backup retention (`IRONCLAD_BACKUP_RETENTION`, default 559 characters in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_SCHEDULER_WORKER_COUNT` and given a new default of 10 megabytes in release 3.1. Before that release, version 3 still used the version 2 name.

## Related

- Webhook delivery timeout: see the Webhook delivery timeout page for version 3.
- Backup retention: see the Backup retention page for version 3.
