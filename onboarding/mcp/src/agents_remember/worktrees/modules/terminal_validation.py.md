# mcp/src/agents_remember/worktrees/modules/terminal_validation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/terminal_validation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-19T04:05+02:00 |
| lastVerifiedCommitHash | `e41ea31d6df3e35a92f526edef8420ae9bd56c57` |
| lastVerifiedCommitDate | 2026-08-18T19:37:20+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Fail-closed preflight and result validation for terminal worktree operations.

## Code Commentary

### Logic

Module-level surface:

- `BranchTarget` (class, lines 24-30)
- `TerminalPreflight` (class, lines 34-37)
- `require_series_children_retired` (function, lines 40-64)
- `series_reports_is_child_enclosure` (function, lines 67-70)
- `legacy_series_reports_is_child_enclosure` (function, lines 73-84)
- `terminal_preflight` (function, lines 172-211)
- `terminal_result_blockers` (function, lines 214-239)
- `_worktree_preflight` (function, lines 242-281)
- `_branch_targets` (function, lines 284-307)
- `_branch_preflight` (function, lines 310-325)
- `_local_absent_remote_preflight` (function, lines 328-338)
- `_branch_identity_refusal` (function, lines 341-349)
- `_branch_refs_refusal` (function, lines 352-372)
- `_branch_checkout_refusal` (function, lines 375-386)
- `_cleanup_branch_preflight` (function, lines 389-417)
- `_abandon_branch_preflight` (function, lines 420-450)
- `_branch_presence` (function, lines 453-459)
- `_checked_out_paths` (function, lines 462-474)
- `_remote_branch_preflight` (function, lines 477-501)
- `_provider_blockers` (function, lines 504-523)
- `_result_blockers` (function, lines 526-542)
- `_blocked` (function, lines 545-553)

**Series child census and the legacy reports guard (260815-DAG-L10).**
`require_series_children_retired` verifies a series contract's recorded `worktree_group` against
`worktree_group_for(series.coordination_root, series.repo_name, series.task_name)` — the master
worktree group, `worktrees/<repo>/<master>-ar`, since L10 — before censusing live children under
`task_root / "enclosures"`; a legacy series contract still recording the task enclosure root as
its group is refused here. `series_reports_is_child_enclosure` detects a child leaf literally
named `reports` whose enclosure shares the series reports directory. `legacy_series_reports_is_child_enclosure`
— the guard `cleanup.py` / `abandon.py` actually call before removing the series reports tree —
restricts that preservation to legacy-shape contracts (group still equal to the task enclosure
root), because current contracts keep series reports under the worktree group, where no child
enclosure can live.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `BranchTarget`. | `BranchTarget` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:24-30 |
| Defines the class `TerminalPreflight`. | `TerminalPreflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:34-37 |
| The series child census fails closed on a non-canonical worktree group; the legacy guard preserves a colliding child `reports` enclosure only for legacy-shape contracts. | `require_series_children_retired`; `legacy_series_reports_is_child_enclosure` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:40-64; mcp/src/agents_remember/worktrees/modules/terminal_validation.py:73-84 |
| Defines the function `terminal_preflight`. | `terminal_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:172-211 |
| Defines the function `terminal_result_blockers`. | `terminal_result_blockers` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:214-239 |
| Defines the function `_worktree_preflight`. | `_worktree_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:242-281 |
| Builds the exact code and optional external-memory terminal branch targets owned by the validated contract. | `_branch_targets` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:284-307 |
| Defines the function `_branch_preflight`. | `_branch_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:310-325 |
| Defines the function `_local_absent_remote_preflight`. | `_local_absent_remote_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:328-338 |
| Defines the function `_branch_identity_refusal`. | `_branch_identity_refusal` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:341-349 |
| Defines the function `_branch_refs_refusal`. | `_branch_refs_refusal` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:352-372 |
| Defines the function `_branch_checkout_refusal`. | `_branch_checkout_refusal` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:375-386 |
| Defines the function `_cleanup_branch_preflight`. | `_cleanup_branch_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:389-417 |
| Defines the function `_abandon_branch_preflight`. | `_abandon_branch_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:420-450 |
| Defines the function `_branch_presence`. | `_branch_presence` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:453-459 |
| Defines the function `_checked_out_paths`. | `_checked_out_paths` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:462-474 |
| Defines the function `_remote_branch_preflight`. | `_remote_branch_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:477-501 |
| Defines the function `_provider_blockers`. | `_provider_blockers` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:504-523 |
| Defines the function `_result_blockers`. | `_result_blockers` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:526-542 |
| Defines the function `_blocked`. | `_blocked` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:545-553 |

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## Update History

- 2026-08-19T04:05+02:00 — 260815-DAG-L10 curator: `require_series_children_retired` now checks
  the recorded series `worktree_group` against `worktree_group_for(...)` (the master worktree
  group) instead of the task enclosure root, and the new `legacy_series_reports_is_child_enclosure`
  restricts child-`reports`-enclosure preservation to legacy-shape contracts. Added the three
  series-census functions to the module surface, documented the guard, and repaired all reference
  ranges (L10's +18-line shift plus older stale rows). Verification metadata stamped at the landed
  code commit `e41ea31d`.

- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
