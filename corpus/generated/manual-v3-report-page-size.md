---
product: Ironclad Endpoint Manager
version: v3
section: Configuration
---

# Report page size (Ironclad v3)

In Ironclad Endpoint Manager, the report page size is a single value measured in percent. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## Where the setting lives

The setting is `IRONCLAD_REPORT_PAGE_SIZE`, as the environment variable. It takes a whole number of percent. The default is **29 percent**.

```
export IRONCLAD_REPORT_PAGE_SIZE=29
```

## Upgrading from version 2

`report_page_size`, the version 2 setting, is still read in version 3 for compatibility, with a warning in the startup log, and `IRONCLAD_REPORT_PAGE_SIZE` takes precedence when both are set. Support for the old name ends in a future release.

## How it works

Every request carries the report page size that applied when it started. If the value changes while a request is in progress, that request keeps its original limit, and only new requests see the new one. This keeps behaviour predictable during a change, at the cost of a short period in which old and new limits are both in force.

## When it takes effect

The value is read at the start of each job. A job that is already running keeps the value it started with; the next job uses the new one. No restart is needed.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 29 percent. Large ones usually settle between the default and twice the default. Values near the minimum of 2 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_report_page_size_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Limits

The lowest accepted value is 2. The highest accepted value is 97. A value outside that range is rejected and the previous value stays in force, with `E1600: IRONCLAD_REPORT_PAGE_SIZE out of range` in the log.

## Examples

| Value (percent) | When to use it |
| --- | --- |
| 2 | small installations, or testing |
| 29 | the default; right for most installations |
| 58 | busy installations with spare capacity |
| 97 | the maximum; only with a reason written down |

## Interactions

The report page size is often changed together with the session timeout (`IRONCLAD_SESSION_TIMEOUT`, default 34 minutes in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The report page size is often changed together with the export batch size (`IRONCLAD_EXPORT_BATCH_SIZE`, default 343 requests per minute in version 3). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Renamed to `IRONCLAD_REPORT_PAGE_SIZE` and given a new default of 29 percent in release 3.7. Before that release, version 3 still used the version 2 name.

## Related

- Session timeout: see the Session timeout page for version 3.
- Export batch size: see the Export batch size page for version 3.
