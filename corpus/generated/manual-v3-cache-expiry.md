---
product: Ironclad Endpoint Manager
version: v3
section: Security
---

# Cache expiry (Ironclad v3)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The cache expiry setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `IRONCLAD_CACHE_EXPIRY`, in the admin console, under Settings > Data. It takes a whole number of items. The default is **2308 items**.

The console shows the current value and the default side by side. The same value can be set from the command line with `ironcladctl config set IRONCLAD_CACHE_EXPIRY 2308`.

## Upgrading from version 2

`cache_expiry`, the version 2 setting, is still read in version 3 for compatibility, with a warning in the startup log, and `IRONCLAD_CACHE_EXPIRY` takes precedence when both are set. Support for the old name ends in a future release.

## How it works

The cache expiry is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 2308 items. Large ones usually settle between the default and twice the default. Values near the minimum of 191 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_cache_expiry_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 191. The highest accepted value is 9874. A value outside that range is rejected and the previous value stays in force, with `E1719: IRONCLAD_CACHE_EXPIRY out of range` in the log.

## Examples

| Value (items) | When to use it |
| --- | --- |
| 191 | small installations, or testing |
| 2308 | the default; right for most installations |
| 4616 | busy installations with spare capacity |
| 9874 | the maximum; only with a reason written down |

## Interactions

The cache expiry is often changed together with the webhook delivery timeout (`IRONCLAD_WEBHOOK_DELIVERY_TIMEOUT`, default 393 megabytes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The cache expiry is often changed together with the backup retention (`IRONCLAD_BACKUP_RETENTION`, default 559 characters in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_CACHE_EXPIRY` and given a new default of 2308 items in release 3.8. Before that release, version 3 still used the version 2 name.

## Related

- Webhook delivery timeout: see the Webhook delivery timeout page for version 3.
- Backup retention: see the Backup retention page for version 3.
