---
product: Ironclad Endpoint Manager
version: v3
section: Integrations
---

# API rate limit (Ironclad v3)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The api rate limit setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `IRONCLAD_API_RATE_LIMIT`, as the environment variable. It takes a whole number of megabytes. The default is **173 megabytes**.

```
export IRONCLAD_API_RATE_LIMIT=173
```

## Upgrading from version 2

`api_rate_limit`, the version 2 setting, is rejected. If it is still present the service refuses to start and logs `E1246: unknown setting api_rate_limit`. Remove it before upgrading.

## How it works

Internally, the service checks the api rate limit every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 173 megabytes therefore means 'at least 173', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Choosing a value

Start from the default of 173 megabytes and change it only with a reason you can write down. Raising the api rate limit trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 1539 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_api_rate_limit_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 32. The highest accepted value is 1539. A value outside that range is rejected and the previous value stays in force, with `E1246: IRONCLAD_API_RATE_LIMIT out of range` in the log.

## Examples

| Value (megabytes) | When to use it |
| --- | --- |
| 32 | small installations, or testing |
| 173 | the default; right for most installations |
| 346 | busy installations with spare capacity |
| 1539 | the maximum; only with a reason written down |

## Interactions

The api rate limit is often changed together with the connection pool size (`IRONCLAD_CONNECTION_POOL_SIZE`, default 383 requests per minute in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The api rate limit is often changed together with the request timeout (`IRONCLAD_REQUEST_TIMEOUT`, default 37 minutes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_API_RATE_LIMIT` and given a new default of 173 megabytes in release 3.9. Before that release, version 3 still used the version 2 name.

## Related

- Connection pool size: see the Connection pool size page for version 3.
- Request timeout: see the Request timeout page for version 3.
