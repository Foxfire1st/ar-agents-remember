# mcp/tests/test_paseo_usage_reports.py

## Governing Overview

[overview](overview.md)

## Purpose

The bridge reads the pinned host's usage reports as the SDK answers them.

## Code Commentary

The real client answers with a request-and-reports envelope and refuses a call that selects both by agent and by report ids. The cases guard against a bridge that reads the answer as a bare array or refreshes with both selectors, which would read the envelope as no entries and never refresh. The fake client keeps the pinned shape and the SDK's own refusal.

**INV-4T6KSE.** The report reader is held by these cases, which is where a shape change would surface; the obligation for this place is stated in that invariant.

`test_a_periodic_read_skips_an_unknown_agent_and_forces_the_next_agent_entries`, `test_missing_periodic_target_retains_its_mapping_when_a_sibling_clears` and `test_a_mixed_batch_shares_refreshes_and_keeps_stamped_only_managers_cached` hold the batch's periodic rules: an unknown agent is skipped, a sibling's clear does not remove a missing target's mapping, and a stamped-only manager keeps its cached entry while a forced refresh is shared. `test_a_stale_leaf_entry_is_refreshed_by_report_id_alone` holds the report-id-only refresh.


Scenario timestamps are sampled when the case builds its inputs. `_fresh()` uses the current UTC time, `_stale()` subtracts five minutes, and `_reset()` adds two hours. `_entry()` resolves its default stale stamp when called. Import-to-execution delay therefore does not consume a case's intended freshness window. The bridge's 60-second threshold and the fresh/no-refresh versus stale/refresh assertions stay unchanged.

Cases that compare timestamp identity capture one stamp and reuse it: the refresh case compares its returned `fetchedAt` with that stamp, and an empty refresh preserves the exact cached stale stamp.

## Evidence

- Scenario timestamps are sampled at call time [1]
