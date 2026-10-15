---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the field length limit

In Ironclad Endpoint Manager, the field length limit is a single value measured in seconds. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## How it works

The field length limit is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 166 seconds. Large ones usually settle between the default and twice the default. Values near the minimum of 11 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

Watch `ironclad_field_length_limit_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `field_length_limit` | `IRONCLAD_FIELD_LENGTH_LIMIT` |
| Default | 123 seconds | 166 seconds |
| Range | 9–479 | 11–486 |
| Takes effect | restart | next job |

## A worked change

An administrator lowered the field length limit to the minimum while testing and forgot to restore it. Failures tripled overnight. The activity log named the setting on every failure, which is how support found it in minutes rather than days.
