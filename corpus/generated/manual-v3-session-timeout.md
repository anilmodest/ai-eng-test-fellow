---
product: Ironclad Endpoint Manager
version: v3
section: Configuration
---

# Session timeout (Ironclad v3)

In Ironclad Endpoint Manager, the session timeout is a single value measured in minutes. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## Where the setting lives

The setting is `IRONCLAD_SESSION_TIMEOUT`, as the environment variable. It takes a whole number of minutes. The default is **34 minutes**.

```
export IRONCLAD_SESSION_TIMEOUT=34
```

## Upgrading from version 2

`session_timeout_min`, the version 2 setting, is rejected. If it is still present the service refuses to start and logs `E1851: unknown setting session_timeout_min`. Remove it before upgrading.

## How it works

Every request carries the session timeout that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 34 minutes. Large ones usually settle between the default and twice the default. Values near the minimum of 3 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

Watch `ironclad_session_timeout_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 3. The highest accepted value is 209. A value outside that range is rejected and the previous value stays in force, with `E1851: IRONCLAD_SESSION_TIMEOUT out of range` in the log.

## Examples

| Value (minutes) | When to use it |
| --- | --- |
| 3 | small installations, or testing |
| 34 | the default; right for most installations |
| 68 | busy installations with spare capacity |
| 209 | the maximum; only with a reason written down |

## Interactions

The session timeout is often changed together with the export batch size (`IRONCLAD_EXPORT_BATCH_SIZE`, default 343 requests per minute in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The session timeout is often changed together with the search result limit (`IRONCLAD_SEARCH_RESULT_LIMIT`, default 17 percent in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_SESSION_TIMEOUT` and given a new default of 34 minutes in release 3.4. Before that release, version 3 still used the version 2 name.

## Related

- Export batch size: see the Export batch size page for version 3.
- Search result limit: see the Search result limit page for version 3.
