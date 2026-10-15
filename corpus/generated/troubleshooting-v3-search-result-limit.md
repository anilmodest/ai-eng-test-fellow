---
product: Ironclad Endpoint Manager
version: v3
section: Troubleshooting
---

# Troubleshooting: search result limit (Ironclad v3)

Start here when the search result limit does not behave as configured. Most reports turn out to be one of three causes, listed in the order to check them.

## Symptoms

- The service uses a different search result limit from the one you set.
- The log shows `E1251: IRONCLAD_SEARCH_RESULT_LIMIT out of range`.
- The value changed in configuration, but behaviour did not change.

## Check 1: is the value in range?

The accepted range is 2 to 80 percent. Out of range, the value is rejected with `E1251: IRONCLAD_SEARCH_RESULT_LIMIT out of range` and the previous value stays in force. Run `ironcladctl config show IRONCLAD_SEARCH_RESULT_LIMIT` to see the value in use.

## Check 2: has it taken effect?

The value is read once, at startup. A running service keeps the old value until it is restarted with `ironcladctl restart`.

## Check 3: is the old setting still there?

Installations upgraded from version 2 often still carry `search_result_limit`. In version 3 it is ignored. The setting that counts is `IRONCLAD_SEARCH_RESULT_LIMIT`, and its default is 17 percent.

## What the metrics show

Watch `ironclad_search_result_limit_current` on the operations dashboard. If it sits at the configured value for long periods, the setting is the bottleneck, and raising it is reasonable. If it never comes near, the value can safely stay where it is.

## If none of these explains it

Collect the output of `ironcladctl config show --all` and the last hour of the service log, and open a ticket with the support desk. Say which version you run.
