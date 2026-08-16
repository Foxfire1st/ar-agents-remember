# mcp/src/agents_remember/worktrees/modules/terminal_validation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/terminal_validation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Fail-closed preflight and result validation for terminal worktree operations.

## Code Commentary

### Logic

Module-level surface:

- `BranchTarget` (class, lines 19-25)
- `TerminalPreflight` (class, lines 29-32)
- `terminal_preflight` (function, lines 35-74)
- `terminal_result_blockers` (function, lines 77-99)
- `_worktree_preflight` (function, lines 102-139)
- `_branch_targets` (function, lines 142-174)
- `_branch_preflight` (function, lines 177-192)
- `_local_absent_remote_preflight` (function, lines 195-205)
- `_branch_identity_refusal` (function, lines 208-216)
- `_branch_refs_refusal` (function, lines 219-239)
- `_branch_checkout_refusal` (function, lines 242-253)
- `_cleanup_branch_preflight` (function, lines 256-284)
- `_abandon_branch_preflight` (function, lines 287-317)
- `_branch_presence` (function, lines 320-326)
- `_checked_out_paths` (function, lines 329-341)
- `_remote_branch_preflight` (function, lines 344-368)
- `_provider_blockers` (function, lines 371-390)
- `_result_blockers` (function, lines 393-409)
- `_blocked` (function, lines 412-420)

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
| Defines the class `BranchTarget` (lines 19-25). | `BranchTarget` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:18-25 |
| Defines the class `TerminalPreflight` (lines 29-32). | `TerminalPreflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:32-36 |
| Defines the function `terminal_preflight` (lines 35-74). | `terminal_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:154-193 |
| Defines the function `terminal_result_blockers` (lines 77-99). | `terminal_result_blockers` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:196-221 |
| Defines the function `_worktree_preflight` (lines 102-139). | `_worktree_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:224-263 |
| Builds the exact code and optional external-memory terminal branch targets owned by the validated contract. | `_branch_targets` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:266-289 |
| Defines the function `_branch_preflight` (lines 177-192). | `_branch_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:292-307 |
| Defines the function `_local_absent_remote_preflight` (lines 195-205). | `_local_absent_remote_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:310-320 |
| Defines the function `_branch_identity_refusal` (lines 208-216). | `_branch_identity_refusal` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:323-331 |
| Defines the function `_branch_refs_refusal` (lines 219-239). | `_branch_refs_refusal` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:334-354 |
| Defines the function `_branch_checkout_refusal` (lines 242-253). | `_branch_checkout_refusal` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:357-368 |
| Defines the function `_cleanup_branch_preflight` (lines 256-284). | `_cleanup_branch_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:371-399 |
| Defines the function `_abandon_branch_preflight` (lines 287-317). | `_abandon_branch_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:287-317 |
| Defines the function `_branch_presence` (lines 320-326). | `_branch_presence` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:435-441 |
| Defines the function `_checked_out_paths` (lines 329-341). | `_checked_out_paths` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:444-456 |
| Defines the function `_remote_branch_preflight` (lines 344-368). | `_remote_branch_preflight` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:459-483 |
| Defines the function `_provider_blockers` (lines 371-390). | `_provider_blockers` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:486-505 |
| Defines the function `_result_blockers` (lines 393-409). | `_result_blockers` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:508-524 |
| Defines the function `_blocked` (lines 412-420). | `_blocked` | mcp/src/agents_remember/worktrees/modules/terminal_validation.py:527-535 |

## 260815-DAG-L4 Integration-Authority Impact

L4 makes task-derived integration refs mechanically non-ordinary: repository defaults, sprint supers, and active atomic-series refs are censused across code and external memory. Mutation is admitted only through exact lifecycle authority, named-ref compare-and-swap, queue/repository serialization, or a terminal capability; stale topology, aliases, ambient checkouts, and torn recovery fail closed.

## Update History

- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
