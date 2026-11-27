# mcp/src/agents_remember/worktrees/landing_briefs.py

## Governing Overview

[worktrees](overview.md)

## Purpose

Post-landing advisory helper that refreshes derived Git-ignored `briefs/` in checked-out external-memory worktrees after integration, checkpoint landing, or recorded pull-request landing. It never mutates Git refs, commits, or durable landing records; any refresh or Git error returns an advisory problem string.

## Code Commentary

- `refresh_integrated_memory_briefs` exits with `None` unless `contract.memory_mode == "external"`, `memory_repo_path` is configured, and `memory_branch` is non-empty; it guards against ledger-only commits via `_memory_content_changed` before inspecting branch owners.
- `_memory_content_changed` diffs `previous_commit..current_commit` excluding `LEDGER_RELATIVE_PATH` (`memory.md`) using `git diff --name-only --no-renames`, so ledger-only integrations trigger no brief write.
- `refresh_recorded_landing_memory_briefs` resolves the landed memory commit, checks each `branch_worktree_owners` checkout's `HEAD`, and refreshes only checkouts whose `HEAD` matches `target_commit` so unpulled checkouts are never paired with a newer landed code commit.
- When no checked-out worktree on `contract.memory_source_branch` matches `target_commit` and no Git error occurred, `refresh_recorded_landing_memory_briefs` returns an explicit advisory string telling the operator to pull and run `agents-remember memory-briefs --repo <repo_name>`.
- Unconverted checkouts lacking `LAYOUT_MARKER_PATH` are skipped; `OSError`, `RuntimeError`, and `subprocess.SubprocessError` are caught and joined into one `; `-separated advisory message.

## Relationships

- Called by `mcp/src/agents_remember/worktrees/modules/integrate.py` (`refresh_integrated_memory_briefs`) and `mcp/src/agents_remember/worktrees/modules/record_landing.py` (`refresh_recorded_landing_memory_briefs`); covered by `mcp/tests/test_kno_r07_briefs_and_pairing.py`.
- Delegates brief writing through `worktrees/services.py::refresh_written_memory_briefs` (respecting `layers.toml` so `worktrees` never imports `application`).
- Neighbours: `mcp/src/agents_remember/worktrees/sync_briefs.py` (post-sync brief refresh).

## Evidence

- Integration and checkpoint brief refresh checks external mode, skips ledger-only diffs, and refreshes converted branch-owner checkouts via `WorktreeServices.file_briefs`. [1]
- Recorded-landing brief refresh requires checkout `HEAD == target_commit` and returns explicit pull and `memory-briefs` CLI guidance when no checkout matches. [2]
- Non-ledger content diff excludes `LEDGER_RELATIVE_PATH` (`memory.md`) via `git diff --name-only --no-renames`. [3]
