---
product: Ironclad Endpoint Manager
version: v3
section: Security
---

# Check-in interval (Ironclad v3)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The check-in interval setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `IRONCLAD_CHECK_IN_INTERVAL`, as the environment variable. It takes a whole number of minutes. The default is **43 minutes**.

```
export IRONCLAD_CHECK_IN_INTERVAL=43
```

## Upgrading from version 2

`check_in_interval`, the version 2 setting, is still read in version 3 for compatibility, with a warning in the startup log, and `IRONCLAD_CHECK_IN_INTERVAL` takes precedence when both are set. Support for the old name ends in a future release.

## How it works

Internally, the service checks the check-in interval every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 43 minutes therefore means 'at least 43', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 43 minutes. Large ones usually settle between the default and twice the default. Values near the minimum of 1 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_check_in_interval_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 1. The highest accepted value is 221. A value outside that range is rejected and the previous value stays in force, with `E1394: IRONCLAD_CHECK_IN_INTERVAL out of range` in the log.

## Examples

| Value (minutes) | When to use it |
| --- | --- |
| 1 | small installations, or testing |
| 43 | the default; right for most installations |
| 86 | busy installations with spare capacity |
| 221 | the maximum; only with a reason written down |

## Interactions

The check-in interval is often changed together with the webhook delivery timeout (`IRONCLAD_WEBHOOK_DELIVERY_TIMEOUT`, default 393 megabytes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The check-in interval is often changed together with the backup retention (`IRONCLAD_BACKUP_RETENTION`, default 559 characters in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_CHECK_IN_INTERVAL` and given a new default of 43 minutes in release 3.8. Before that release, version 3 still used the version 2 name.

## Related

- Webhook delivery timeout: see the Webhook delivery timeout page for version 3.
- Backup retention: see the Backup retention page for version 3.
