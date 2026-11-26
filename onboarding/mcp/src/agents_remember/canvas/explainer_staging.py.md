# mcp/src/agents_remember/canvas/explainer_staging.py

## Governing Overview

[Governing overview](overview.md)

## Purpose

This module stages the exact draft bytes for registered explainer publication.

## Code Commentary

`publish_working_directory` confines `drafts` and `<workspace>/state/publish-staging` with `guard_path` via `_staging_root` without pre-resolving symlinks, and validates any reused recorded draft working path as absolute and workspace-confined via `_guard_recorded_path`. `stage_and_begin_draft` (taking `DraftStagingRequest`) reads any earlier draft, allocates or reuses staging, records `begin_draft`, and discards unused staging on mismatch or exception under one re-entrant `exclusive_file_lock(task_lock(scope), "review frame store")`. `prune_finished_staging` runs under that same task lock, inspects `active_staging_dirs(scope)`, and guards each non-symlink staging child with `guard_path` before removal; `discard_unused_staging(workspace, publish_working, adopted)` guards the target strictly inside `_staging_root(workspace)` (refusing the staging root itself with `PathRefused`) while preserving any directory adopted by `adopted`. Browser-observed DOM and loaded assets supply advisory inventory, and the typed publication result identifies the revision to read back.

## Relationships

The explainer server runs readiness and load checks. The frame store owns durable promotion and revision identity.

## Evidence

- Request staging confines allocation, reuse, and cleanup inside the workspace under the task lock and preserves active draft ownership. [1]
- `_staging_root`, `_guard_recorded_path`, `publish_working_directory`, and `discard_unused_staging` guard staging roots, reused paths, and discard targets with `guard_path` before use and refuse escaping or staging-root removals with `PathRefused`. [2]
- `stage_and_begin_draft` and `prune_finished_staging` serialize draft lookup, staging creation, `begin_draft`, and completed-staging pruning under `exclusive_file_lock(task_lock(scope), "review frame store")`. [3]
