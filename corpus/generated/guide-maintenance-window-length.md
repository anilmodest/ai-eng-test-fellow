---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the maintenance window length

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The maintenance window length setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## How it works

The maintenance window length is enforced by the component that does the work, not by a central scheduler. Each worker reads the value it was given and applies it independently, which is why two workers can briefly disagree after a change. For most installations this never matters; where it does, the troubleshooting page for this setting explains how to confirm that every worker has picked up the new value.

## Choosing a value

Start from the default of 20 minutes and change it only with a reason you can write down. Raising the maintenance window length trades resilience for capacity: more work is accepted, but a failure takes longer to notice. Lowering it does the opposite. Change it in steps of no more than a quarter, watch for a week, and record what you saw. Installations that jumped straight to the maximum of 183 are the most common source of tickets about this setting.

## Monitoring

Watch `ironclad_maintenance_window_length_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `maintenance_window_length_min` | `IRONCLAD_MAINTENANCE_WINDOW_LENGTH` |
| Default | 31 minutes | 20 minutes |
| Range | 3–195 | 3–183 |
| Takes effect | restart | restart |

## A worked change

A customer with 400 seats saw the limit hit every afternoon. They raised the maintenance window length by a quarter, watched the limit-hit metric for a week, saw it fall by two thirds, and stopped there. They wrote the reason into their change log, which is what made the next upgrade painless.
