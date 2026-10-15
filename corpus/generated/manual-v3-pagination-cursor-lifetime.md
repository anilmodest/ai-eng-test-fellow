---
product: Ironclad Endpoint Manager
version: v3
section: Data
---

# Pagination cursor lifetime (Ironclad v3)

In Ironclad Endpoint Manager, the pagination cursor lifetime is a single value measured in percent. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## Where the setting lives

The setting is `IRONCLAD_PAGINATION_CURSOR_LIFETIME`, in the admin console, under Settings > Integrations. It takes a whole number of percent. The default is **10 percent**.

The console shows the current value and the default side by side. The same value can be set from the command line with `ironcladctl config set IRONCLAD_PAGINATION_CURSOR_LIFETIME 10`.

## Upgrading from version 2

`pagination_cursor_lifetime`, the version 2 setting, is no longer used. If it is still present the service **reads it, ignores it and starts normally**. Nothing is written to the log. An installation upgraded from version 2 without this change therefore runs on the version 3 default of 10 percent, not on the value in the old file.

## How it works

Every request carries the pagination cursor lifetime that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Choosing a value

Start from the default of 10 percent and change it only with a reason you can write down. Raising the pagination cursor lifetime trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 93 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_pagination_cursor_lifetime_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 1. The highest accepted value is 93. A value outside that range is rejected and the previous value stays in force, with `E1627: IRONCLAD_PAGINATION_CURSOR_LIFETIME out of range` in the log.

## Examples

| Value (percent) | When to use it |
| --- | --- |
| 1 | small installations, or testing |
| 10 | the default; right for most installations |
| 20 | busy installations with spare capacity |
| 93 | the maximum; only with a reason written down |

## Interactions

The pagination cursor lifetime is often changed together with the backup schedule interval (`IRONCLAD_BACKUP_SCHEDULE_INTERVAL`, default 562 megabytes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The pagination cursor lifetime is often changed together with the trace sampling rate (`IRONCLAD_TRACE_SAMPLING_RATE`, default 87 seconds in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_PAGINATION_CURSOR_LIFETIME` and given a new default of 10 percent in release 3.7. Before that release, version 3 still used the version 2 name.

## Related

- Backup schedule interval: see the Backup schedule interval page for version 3.
- Trace sampling rate: see the Trace sampling rate page for version 3.
