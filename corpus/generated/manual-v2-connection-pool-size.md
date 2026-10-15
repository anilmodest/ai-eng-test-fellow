---
product: Ironclad Endpoint Manager
version: v2
section: Integrations
---

# Connection pool size (Ironclad v2)

This page describes the connection pool size setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `connection_pool_size_req`, in `ironclad.conf`, in the `[source]` block. It takes a whole number of requests per minute. The default is **161 requests per minute**.

```
connection_pool_size_req = 161
```

## How it works

The connection pool size is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## When it takes effect

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Choosing a value

Start from the default of 161 requests per minute and change it only with a reason you can write down. Raising the connection pool size trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 4721 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_connection_pool_size_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 89. The highest accepted value is 4721. A value outside that range is rejected and the previous value stays in force, with `E1438: connection_pool_size_req out of range` in the log.

## Examples

| Value (requests per minute) | When to use it |
| --- | --- |
| 89 | small installations, or testing |
| 161 | the default; right for most installations |
| 322 | busy installations with spare capacity |
| 4721 | the maximum; only with a reason written down |

## Interactions

The connection pool size is often changed together with the request timeout (`request_timeout`, default 21 minutes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The connection pool size is often changed together with the import file size limit (`import_file_size_limit`, default 443 megabytes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `connection_pool_size_req`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Request timeout: see the Request timeout page for version 2.
- Import file size limit: see the Import file size limit page for version 2.
