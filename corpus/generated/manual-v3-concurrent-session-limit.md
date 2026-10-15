---
product: Ironclad Endpoint Manager
version: v3
section: Security
---

# Concurrent session limit (Ironclad v3)

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The concurrent session limit setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## Where the setting lives

The setting is `IRONCLAD_CONCURRENT_SESSION_LIMIT`, as the environment variable. It takes a whole number of seconds. The default is **168 seconds**.

```
export IRONCLAD_CONCURRENT_SESSION_LIMIT=168
```

## Upgrading from version 2

`concurrent_session_limit`, the version 2 setting, is still read in version 3 for compatibility, with a warning in the startup log, and `IRONCLAD_CONCURRENT_SESSION_LIMIT` takes precedence when both are set. Support for the old name ends in a future release.

## How it works

Internally, the service checks the concurrent session limit every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 168 seconds therefore means 'at least 168', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

The value is reloaded within a few seconds of being changed. No restart is needed, and work already in progress picks up the new value on its next step.

## Choosing a value

Start from the default of 168 seconds and change it only with a reason you can write down. Raising the concurrent session limit trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 578 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_concurrent_session_limit_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 4. The highest accepted value is 578. A value outside that range is rejected and the previous value stays in force, with `E1647: IRONCLAD_CONCURRENT_SESSION_LIMIT out of range` in the log.

## Examples

| Value (seconds) | When to use it |
| --- | --- |
| 4 | small installations, or testing |
| 168 | the default; right for most installations |
| 336 | busy installations with spare capacity |
| 578 | the maximum; only with a reason written down |

## Interactions

The concurrent session limit is often changed together with the webhook delivery timeout (`IRONCLAD_WEBHOOK_DELIVERY_TIMEOUT`, default 393 megabytes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The concurrent session limit is often changed together with the backup retention (`IRONCLAD_BACKUP_RETENTION`, default 559 characters in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_CONCURRENT_SESSION_LIMIT` and given a new default of 168 seconds in release 3.0. Before that release, version 3 still used the version 2 name.

## Related

- Webhook delivery timeout: see the Webhook delivery timeout page for version 3.
- Backup retention: see the Backup retention page for version 3.
