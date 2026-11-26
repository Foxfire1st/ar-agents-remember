# mcp/src/agents_remember/worktrees/modules/filesystem.py

## Governing Overview

[Worktree Lifecycle Implementation Modules](overview.md)

## Purpose

Provides the structured directory-tree removal helper (`remove_tree`) used by terminal worktree lifecycle operations to report dry-run plans, removals, absences, and OS failures without raising.

## Code Commentary

`remove_tree(path, *, dry_run)` evaluates `path.exists()` first and returns one of four uniform dictionary shapes keyed with `"path": path.as_posix()` and boolean `"removed"`:

- Missing path (regardless of `dry_run`): `{"path": ..., "removed": False, "reason": "already-absent"}`.
- Existing path with `dry_run=True`: leaves the filesystem untouched and returns `{"path": ..., "removed": False, "would_remove": True}`.
- Existing path with `dry_run=False`: calls `shutil.rmtree(path)` and returns `{"path": ..., "removed": True}` on success.
- Caught `PermissionError` or other `OSError` from `shutil.rmtree`: suppresses the exception and returns `{"path": ..., "removed": False, "reason": "permission denied: <error>"}` for `PermissionError` or `{"path": ..., "removed": False, "reason": str(error)}` for any other `OSError`.

Because every non-removed live outcome supplies a non-empty `"reason"` string and every preview of an existing tree supplies `"would_remove": True`, downstream terminal-blocker reporting can distinguish reclaimed trees, preview-only entries, absent paths, and concrete reclamation failures without catching raw filesystem exceptions.

## Relationships

- Called by `mcp/src/agents_remember/worktrees/modules/cleanup.py` and `mcp/src/agents_remember/worktrees/modules/abandon.py` to remove enclosure `reports/`, `.lifecycle/`, and `provider_runtime` trees, and passed as the `remove_tree` callback into `worktrees/modules/kept_tool_calls.py` (`removal_after_keep`) for enclosure `logs/` removal.
- Separate from `kernel/filesystem.py` (general kernel filesystem utilities) and private `_remove_tree` helpers in `worktrees/outside_scratch.py` and `memory_quality/style/citations/source_index_cache.py`.
- Directly exercised by `test_remove_tree_answers_with_a_reason_whenever_it_reclaimed_nothing` in `mcp/tests/test_terminal_blocker_reasons.py` (and patched in `test_tool_answer_log.py` and `test_tool_answer_table_enclosure.py`).

## Evidence

- `remove_tree` reports `already-absent`, `would_remove` on dry run, `removed: True` after `shutil.rmtree`, or `removed: False` with a `permission denied:` or `OSError` reason string. [1]
- `test_remove_tree_answers_with_a_reason_whenever_it_reclaimed_nothing` asserts the absent, preview, live removal, and permission-denied return shapes of `remove_tree`. [2]
