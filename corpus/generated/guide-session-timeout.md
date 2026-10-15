---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the session timeout

In Ironclad Endpoint Manager, the session timeout is a single value measured in minutes. It applies to the whole installation rather than to one customer account, which is why it lives in system configuration and not in account settings.

## How it works

The session timeout is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## Choosing a value

Start from the default of 34 minutes and change it only with a reason you can write down. Raising the session timeout trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 209 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_session_timeout_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `session_timeout_min` | `IRONCLAD_SESSION_TIMEOUT` |
| Default | 42 minutes | 34 minutes |
| Range | 2–188 | 3–209 |
| Takes effect | restart | next job |

## A worked change

An administrator lowered the session timeout to the minimum while testing and forgot to restore it. Failures tripled overnight. The activity log named the setting on every failure, which is how support found it in minutes rather than days.
