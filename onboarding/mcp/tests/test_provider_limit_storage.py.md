# mcp/tests/test_provider_limit_storage.py

## Governing Overview

[mcp overview](../overview.md)

## Purpose

Hold the limit file's cross-attempt storage rules: a claimed recheck survives a fresh snapshot, a quiet replacement prunes departed mappings, and an early clear marker survives an unrelated write and expires.

## Code Commentary

The cases drive the real writer against a temporary `provider-limits.json` and `role-agents.json`. `test_due_claim_survives_a_fresh_snapshot_and_keeps_the_fact` claims a due report, then reads the file through a fresh reader and finds the attempt, observation, deadline and mapping intact; `test_quiet_replacement_prunes_departed_agent_mappings` removes a seat from the role record and shows the next replacement drops its mappings and reports while a quiet write leaves the file untouched. `test_clear_marker_survives_an_unrelated_write_and_expires` publishes a clear, writes an unrelated report, and finds the marker kept until the old deadline plus the grace window, then reclaimed. `test_only_the_last_cleared_blocker_releases_a_registered_seat` holds two reports and releases the seat only when the last blocker clears, `test_failed_refresh_keeps_the_fact_and_named_agent_mapping` keeps the fact on a failed refresh, and `test_periodic_preservation_does_not_restore_obsolete_or_foreign_mappings` restricts preservation to current mappings. `test_concurrent_usage_reads_keep_both_reports_and_mappings` runs two writers at once and keeps both reports and their mappings.

## Evidence

- The suite holds the claimed attempt, quiet replacement, early-clear lifetime, last-blocker release and concurrent-writer rules. [1]
