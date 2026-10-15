---
product: Ironclad Endpoint Manager
version: v3
section: Integrations
---

# Import file size limit (Ironclad v3)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The import file size limit setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `IRONCLAD_IMPORT_FILE_SIZE_LIMIT`, as the environment variable. It takes a whole number of megabytes. The default is **9 megabytes**.

```
export IRONCLAD_IMPORT_FILE_SIZE_LIMIT=9
```

## Upgrading from version 2

`import_file_size_limit`, the version 2 setting, is still read in version 3 for compatibility, with a warning in the startup log, and `IRONCLAD_IMPORT_FILE_SIZE_LIMIT` takes precedence when both are set. Support for the old name ends in a future release.

## How it works

Every request carries the import file size limit that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 9 megabytes. Large ones usually settle between the default and twice the default. Values near the minimum of 5 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

Watch `ironclad_import_file_size_limit_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 5. The highest accepted value is 1565. A value outside that range is rejected and the previous value stays in force, with `E1436: IRONCLAD_IMPORT_FILE_SIZE_LIMIT out of range` in the log.

## Examples

| Value (megabytes) | When to use it |
| --- | --- |
| 5 | small installations, or testing |
| 9 | the default; right for most installations |
| 18 | busy installations with spare capacity |
| 1565 | the maximum; only with a reason written down |

## Interactions

The import file size limit is often changed together with the connection pool size (`IRONCLAD_CONNECTION_POOL_SIZE`, default 383 requests per minute in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The import file size limit is often changed together with the request timeout (`IRONCLAD_REQUEST_TIMEOUT`, default 37 minutes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_IMPORT_FILE_SIZE_LIMIT` and given a new default of 9 megabytes in release 3.1. Before that release, version 3 still used the version 2 name.

## Related

- Connection pool size: see the Connection pool size page for version 3.
- Request timeout: see the Request timeout page for version 3.
