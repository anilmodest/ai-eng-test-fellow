---
product: Ironclad Endpoint Manager
version: v3
section: Operations
---

# Lock wait timeout (Ironclad v3)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The lock wait timeout setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `IRONCLAD_LOCK_WAIT_TIMEOUT`, in the admin console, under Settings > Integrations. It takes a whole number of minutes. The default is **33 minutes**.

The console shows the current value and the default side by side. The same value can be set from the command line with `ironcladctl config set IRONCLAD_LOCK_WAIT_TIMEOUT 33`.

## Upgrading from version 2

`lock_wait_timeout`, the version 2 setting, is no longer used. If it is still present the service **reads it, ignores it and starts normally**. Nothing is written to the log. An installation upgraded from version 2 without this change therefore runs on the version 3 default of 33 minutes, not on the value in the old file.

## How it works

Internally, the service checks the lock wait timeout every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 33 minutes therefore means 'at least 33', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 33 minutes. Large ones usually settle between the default and twice the default. Values near the minimum of 1 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_lock_wait_timeout_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 1. The highest accepted value is 210. A value outside that range is rejected and the previous value stays in force, with `E1350: IRONCLAD_LOCK_WAIT_TIMEOUT out of range` in the log.

## Examples

| Value (minutes) | When to use it |
| --- | --- |
| 1 | small installations, or testing |
| 33 | the default; right for most installations |
| 66 | busy installations with spare capacity |
| 210 | the maximum; only with a reason written down |

## Interactions

The lock wait timeout is often changed together with the audit log retention (`IRONCLAD_AUDIT_LOG_RETENTION`, default 1060 days in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The lock wait timeout is often changed together with the webhook retry count (`IRONCLAD_WEBHOOK_RETRY_COUNT`, default 2365 items in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_LOCK_WAIT_TIMEOUT` and given a new default of 33 minutes in release 3.3. Before that release, version 3 still used the version 2 name.

## Related

- Audit log retention: see the Audit log retention page for version 3.
- Webhook retry count: see the Webhook retry count page for version 3.
