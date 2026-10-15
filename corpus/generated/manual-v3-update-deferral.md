---
product: Ironclad Endpoint Manager
version: v3
section: Integrations
---

# Update deferral (Ironclad v3)

This page describes the update deferral setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `IRONCLAD_UPDATE_DEFERRAL`, in the admin console, under Settings > Data. It takes a whole number of items. The default is **2560 items**.

The console shows the current value and the default side by side. The same value can be set from the command line with `ironcladctl config set IRONCLAD_UPDATE_DEFERRAL 2560`.

## Upgrading from version 2

`update_deferral_ite`, the version 2 setting, is no longer used. If it is still present the service **reads it, ignores it and starts normally**. Nothing is written to the log. An installation upgraded from version 2 without this change therefore runs on the version 3 default of 2560 items, not on the value in the old file.

## How it works

Internally, the service checks the update deferral every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 2560 items therefore means 'at least 2560', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

Changes take effect immediately: the service watches the setting and reloads it without a restart.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 2560 items. Large ones usually settle between the default and twice the default. Values near the minimum of 159 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

Watch `ironclad_update_deferral_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 159. The highest accepted value is 8640. A value outside that range is rejected and the previous value stays in force, with `E1800: IRONCLAD_UPDATE_DEFERRAL out of range` in the log.

## Examples

| Value (items) | When to use it |
| --- | --- |
| 159 | small installations, or testing |
| 2560 | the default; right for most installations |
| 5120 | busy installations with spare capacity |
| 8640 | the maximum; only with a reason written down |

## Interactions

The update deferral is often changed together with the connection pool size (`IRONCLAD_CONNECTION_POOL_SIZE`, default 383 requests per minute in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The update deferral is often changed together with the request timeout (`IRONCLAD_REQUEST_TIMEOUT`, default 37 minutes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_UPDATE_DEFERRAL` and given a new default of 2560 items in release 3.0. Before that release, version 3 still used the version 2 name.

## Related

- Connection pool size: see the Connection pool size page for version 3.
- Request timeout: see the Request timeout page for version 3.
