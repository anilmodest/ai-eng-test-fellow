---
product: Ironclad Endpoint Manager
version: v2
section: Integrations
---

# Import file size limit (Ironclad v2)

This page describes the import file size limit setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `import_file_size_limit`, in `ironclad.conf`, in the `[storage]` block. It takes a whole number of megabytes. The default is **443 megabytes**.

```
import_file_size_limit = 443
```

## How it works

The import file size limit is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 443 megabytes. Large ones usually settle between the default and twice the default. Values near the minimum of 9 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

Watch `ironclad_import_file_size_limit_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 9. The highest accepted value is 1621. A value outside that range is rejected and the previous value stays in force, with `E1436: import_file_size_limit out of range` in the log.

## Examples

| Value (megabytes) | When to use it |
| --- | --- |
| 9 | small installations, or testing |
| 443 | the default; right for most installations |
| 886 | busy installations with spare capacity |
| 1621 | the maximum; only with a reason written down |

## Interactions

The import file size limit is often changed together with the connection pool size (`connection_pool_size_req`, default 161 requests per minute in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The import file size limit is often changed together with the request timeout (`request_timeout`, default 21 minutes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `import_file_size_limit`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Connection pool size: see the Connection pool size page for version 2.
- Request timeout: see the Request timeout page for version 2.
