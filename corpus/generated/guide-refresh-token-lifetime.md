---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the refresh token lifetime

In Ironclad Endpoint Manager, the refresh token lifetime is a single value measured in seconds. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## How it works

Internally, the service checks the refresh token lifetime every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 102 seconds therefore means 'at least 102', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 102 seconds. Large ones usually settle between the default and twice the default. Values near the minimum of 3 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_refresh_token_lifetime_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `refresh_token_lifetime` | `IRONCLAD_REFRESH_TOKEN_LIFETIME` |
| Default | 69 seconds | 102 seconds |
| Range | 9–460 | 3–566 |
| Takes effect | restart | next job |

## A worked change

An administrator lowered the refresh token lifetime to the minimum while testing and forgot to restore it. Failures tripled overnight. The activity log named the setting on every failure, which is how support found it in minutes rather than days.
