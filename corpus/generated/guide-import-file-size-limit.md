---
product: Ironclad Endpoint Manager
section: Operations
---

# Operating the import file size limit

Ironclad Endpoint Manager is a device-management product that enrols, updates and locks company devices. The import file size limit setting controls how the service behaves when that limit is reached, and it is one of the settings most often changed by administrators after go-live.

## How it works

Internally, the service checks the import file size limit every time the limit could apply, not on a timer. When the limit is reached the service finishes the step it is on, records an event in the activity log, and only then applies the limit. A value of 9 megabytes therefore means 'at least 9', never 'exactly', and on a heavily loaded installation the difference can be noticeable. The activity log entry names the setting, so an administrator can always tell which limit was hit.

## Choosing a value

There is no single right value. Small installations rarely need more than the default of 9 megabytes. Large ones usually settle between the default and twice the default. Values near the minimum of 5 are meant for testing and make failures more frequent, not less. Whatever you choose, set it in one place only: two conflicting values are the cause of most surprises.

## Monitoring

The service exports the metric `ironclad_import_file_size_limit_limit_hits_total`. A steady rise means the limit is doing its job; a sudden jump after a change means the new value is too tight. Alert on the rate, not on the total.

## Version differences in one table

| | Version 2 | Version 3 |
| --- | --- | --- |
| Setting | `import_file_size_limit` | `IRONCLAD_IMPORT_FILE_SIZE_LIMIT` |
| Default | 443 megabytes | 9 megabytes |
| Range | 9–1621 | 5–1565 |
| Takes effect | restart | next job |

## A worked change

An administrator lowered the import file size limit to the minimum while testing and forgot to restore it. Failures tripled overnight. The activity log named the setting on every failure, which is how support found it in minutes rather than days.
