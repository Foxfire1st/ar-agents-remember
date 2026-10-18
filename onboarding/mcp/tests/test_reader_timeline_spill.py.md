# mcp/tests/test_reader_timeline_spill.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Document the assertion and fixture obligations declared by this test source.

## Code Commentary

New timeline-spill tests count one materialization/hash/freeze per legal walk, preserve event ordering/documents/attempt/path, use anonymous unlinked files beyond RAM budget and verify actual fd cleanup on eviction/clear/revision replacement/process exit. Failure creation/read/unreadable-source retry, continuation binding and resident/spill shared budget are separate explicit cases. These declarations are not tests run here.

### Declared Assertions

- `test_legal_timeline_walk_materializes_and_hashes_once`
- `test_anonymous_backing_is_actually_removed`
- `test_process_exit_removes_anonymous_backing`
- `test_spilled_unreadable_source_is_retried`
- `test_failed_backing_read_is_not_stuck_in_cache`
- `test_failed_backing_creation_releases_partial_files`
- `test_spilled_continuation_refuses_another_binding`
- `test_resident_lru_and_spill_share_the_original_memory_budget`
- `test_truth_view_acquires_full_history_only_on_manifest_miss`

This is a declaration inventory, not a collected parametrized-case total or execution result.

### Evidence Boundary

The source declares these checks. This card does not attest that pytest/Vitest, a native host, a real browser or an installed producer ran on this candidate. Controlled or captured inputs qualify only the operations named above.

## Evidence

- New timeline-spill tests count one materialization/hash/freeze per legal walk, preserve event ordering/documents/attempt/path, use anonymous unlinked files beyond RAM budget and verify actual fd cleanup on eviction/clear/revision replacement/process exit. Failure creation/read/unreadable-source retry, continuation binding and resident/spill shared budget are separate explicit cases. These declarations are not tests run here. [1]
