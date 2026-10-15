---
product: Ironclad Endpoint Manager
version: v3
section: Integrations
---

# Request timeout (Ironclad v3)

In Ironclad Endpoint Manager, the request timeout is a single value measured in minutes. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## Where the setting lives

The setting is `IRONCLAD_REQUEST_TIMEOUT`, as the environment variable. It takes a whole number of minutes. The default is **37 minutes**.

```
export IRONCLAD_REQUEST_TIMEOUT=37
```

## Upgrading from version 2

`request_timeout`, the version 2 setting, is rejected. If it is still present the service refuses to start and logs `E1976: unknown setting request_timeout`. Remove it before upgrading.

## How it works

The request timeout is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

The value is reloaded within a few seconds of being changed. No restart is needed, and work already in progress picks up the new value on its next step.

## Choosing a value

Start from the default of 37 minutes and change it only with a reason you can write down. Raising the request timeout trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 237 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_request_timeout_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 4. The highest accepted value is 237. A value outside that range is rejected and the previous value stays in force, with `E1976: IRONCLAD_REQUEST_TIMEOUT out of range` in the log.

## Examples

| Value (minutes) | When to use it |
| --- | --- |
| 4 | small installations, or testing |
| 37 | the default; right for most installations |
| 74 | busy installations with spare capacity |
| 237 | the maximum; only with a reason written down |

## Interactions

The request timeout is often changed together with the connection pool size (`IRONCLAD_CONNECTION_POOL_SIZE`, default 383 requests per minute in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The request timeout is often changed together with the import file size limit (`IRONCLAD_IMPORT_FILE_SIZE_LIMIT`, default 9 megabytes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_REQUEST_TIMEOUT` and given a new default of 37 minutes in release 3.8. Before that release, version 3 still used the version 2 name.

## Related

- Connection pool size: see the Connection pool size page for version 3.
- Import file size limit: see the Import file size limit page for version 3.
