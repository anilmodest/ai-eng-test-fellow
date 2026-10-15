---
product: Ironclad Endpoint Manager
version: v2
section: Integrations
---

# Password minimum length (Ironclad v2)

This page describes the password minimum length setting in Ironclad Endpoint Manager, a device-management product that enrols, updates and locks company devices. Most installations never change it; the ones that do usually change it after their first busy period, when the default turns out to be too tight or too loose.

## Where the setting lives

The setting is `password_minimum_length`, in `ironclad.conf`, in the `[server]` block. It takes a whole number of connections. The default is **97 connections**.

```
password_minimum_length = 97
```

## How it works

Internally, the service checks the password minimum length every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 97 connections therefore means 'at least 97', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## When it takes effect

The value is read when the service starts. Changing it has no effect on a running service; restart it with `ironcladctl restart` for the new value to be used.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 97 connections. Large ones usually settle between the default and twice the default. Values near the minimum of 8 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

Watch `ironclad_password_minimum_length_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Limits

The lowest accepted value is 8. The highest accepted value is 400. A value outside that range is rejected and the previous value stays in force, with `E1602: password_minimum_length out of range` in the log.

## Examples

| Value (connections) | When to use it |
| --- | --- |
| 8 | small installations, or testing |
| 97 | the default; right for most installations |
| 194 | busy installations with spare capacity |
| 400 | the maximum; only with a reason written down |

## Interactions

The password minimum length is often changed together with the connection pool size (`connection_pool_size_req`, default 161 requests per minute in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

The password minimum length is often changed together with the request timeout (`request_timeout`, default 21 minutes in version 2). Change one at a time: when both move at once, it is impossible to tell from the metrics which change helped and which hurt.

## Version history

Introduced in version 2.0 as `password_minimum_length`. Unchanged through the 2.x releases apart from clearer error messages.

## Related

- Connection pool size: see the Connection pool size page for version 2.
- Request timeout: see the Request timeout page for version 2.
