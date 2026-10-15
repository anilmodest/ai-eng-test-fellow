---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: report page size (Ironclad v3)

Start here when the report page size does not behave as configured. Most reports turn out to be one of three causes, listed in the order to check them.

## Symptoms

- The service uses a different report page size from the one you set.
- The log shows `E1600: IRONCLAD_REPORT_PAGE_SIZE out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 2 to 97 percent. Out of range, the value is rejected with `E1600: IRONCLAD_REPORT_PAGE_SIZE out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_REPORT_PAGE_SIZE` to see the value in use.

## Check 2: has it taken effect?

A change applies from the next job onwards. Jobs already running finish with the value they started with.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `report_page_size`. In version 3 it is warned. The setting that counts is `IRONCLAD_REPORT_PAGE_SIZE`, and its default is 29 percent.

## What the metrics show

Watch `ironclad_report_page_size_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
