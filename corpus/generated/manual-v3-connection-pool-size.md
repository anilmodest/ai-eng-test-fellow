---
product: Ironclad Endpoint Manager
version: v3
section: Integrations
---

# Connection pool size (Ironclad v3)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The connection pool size setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `IRONCLAD_CONNECTION_POOL_SIZE`, as the environment variable. It takes a whole number of requests per minute. The default is **383 requests per minute**.

```
export IRONCLAD_CONNECTION_POOL_SIZE=383
```

## Upgrading from version 2

`connection_pool_size_req`, the version 2 setting, is rejected. If it is still present the service refuses to start and logs `E1438: unknown setting connection_pool_size_req`. Remove it before upgrading.

## How it works

Every request carries the connection pool size that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 383 requests per minute. Large ones usually settle between the default and twice the default. Values near the minimum of 40 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_connection_pool_size_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 40. The highest accepted value is 4583. A value outside that range is rejected and the previous value stays in force, with `E1438: IRONCLAD_CONNECTION_POOL_SIZE out of range` in the log.

## Examples

| Value (requests per minute) | When to use it |
| --- | --- |
| 40 | small installations, or testing |
| 383 | the default; right for most installations |
| 766 | busy installations with spare capacity |
| 4583 | the maximum; only with a reason written down |

## Interactions

The connection pool size is often changed together with the request timeout (`IRONCLAD_REQUEST_TIMEOUT`, default 37 minutes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The connection pool size is often changed together with the import file size limit (`IRONCLAD_IMPORT_FILE_SIZE_LIMIT`, default 9 megabytes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_CONNECTION_POOL_SIZE` and given a new default of 383 requests per minute in release 3.7. Before that release, version 3 still used the version 2 name.

## Related

- Request timeout: see the Request timeout page for version 3.
- Import file size limit: see the Import file size limit page for version 3.
