# mcp/src/agents_remember/package_data/paseo_plugin/server/provider_limits.ts

## Governing Overview

[plugin overview](../overview.md)

## Purpose

The plugin's read of the product's limit file, used at the send-back's end of the wait, at the parent gate and when a resume fires.

## Code Commentary

`<PASEO_HOME>/agents-remember/provider-limits.json` is the product's, written whole and atomically under a lock; the plugin only reads it. Every fact in it comes from the host's own usage report for that seat, so nothing here matches a message or an error string: a seat is limited exactly while `now` is before the `until` of one of its report ids.

The read is keyed by the file's generation like `role_agents.ts`: every check costs one `statSync` on the file, and the generation cache saves the repeated file reads and parses while the file is unchanged, so an unchanged file is statted but not re-read and not re-parsed. There is no per-turn stat promise and no timer inside this reader. A missing or malformed file reads as "nothing is limited", which is the fallback for a provider that has no report at all.

The parsed document also carries `clearedSeats`, each entry the seat's `clearedAt` and `previousUntil`; an entry whose times are not ordered strings is dropped. The reader schedules nothing: `provider_limit_check.ts` asks it for one snapshot every fifteen seconds while a deferred resume or parent flush is pending, and stops when none is.

Only `until` and the report's labels are consumed here; the windows and observation time belong to the product's readers. Nothing in this module schedules a timer of its own.

- The plugin reader admits the early-clear marker and leaves every timer to the check that shares its snapshot. [1]
