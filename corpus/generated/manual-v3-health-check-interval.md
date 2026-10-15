---
product: Ironclad Endpoint Manager
version: v3
section: Integrations
---

# Health check interval (Ironclad v3)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The health check interval setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `IRONCLAD_HEALTH_CHECK_INTERVAL`, in the admin console, under Settings > Operations. It takes a whole number of minutes. The default is **20 minutes**.

The console shows the current value and the default side by side. The same value can be set from the command line with `ironcladctl config set IRONCLAD_HEALTH_CHECK_INTERVAL 20`.

## Upgrading from version 2

`health_check_interval`, the version 2 setting, is still read in version 3 for compatibility, with a warning in the startup log, and `IRONCLAD_HEALTH_CHECK_INTERVAL` takes precedence when both are set. Support for the old name ends in a future release.

## How it works

Internally, the service checks the health check interval every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 20 minutes therefore means 'at least 20', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 20 minutes. Large ones usually settle between the default and twice the default. Values near the minimum of 4 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_health_check_interval_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 4. The highest accepted value is 181. A value outside that range is rejected and the previous value stays in force, with `E1631: IRONCLAD_HEALTH_CHECK_INTERVAL out of range` in the log.

## Examples

| Value (minutes) | When to use it |
| --- | --- |
| 4 | small installations, or testing |
| 20 | the default; right for most installations |
| 40 | busy installations with spare capacity |
| 181 | the maximum; only with a reason written down |

## Interactions

The health check interval is often changed together with the connection pool size (`IRONCLAD_CONNECTION_POOL_SIZE`, default 383 requests per minute in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The health check interval is often changed together with the request timeout (`IRONCLAD_REQUEST_TIMEOUT`, default 37 minutes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_HEALTH_CHECK_INTERVAL` and given a new default of 20 minutes in release 3.2. Before that release, version 3 still used the version 2 name.

## Related

- Connection pool size: see the Connection pool size page for version 3.
- Request timeout: see the Request timeout page for version 3.
