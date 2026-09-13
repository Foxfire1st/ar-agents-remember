# mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | `1ddf7fdac40fa3e9c30b8ded693d440e07d6a8b6`|
| lastVerifiedCommitDate | 2026-09-13T22:07:53+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Integration overview](../overview.md)

## Purpose

Executes direct landing as a durable, candidate-bound lifecycle operation with quality and publication evidence. Direct landing is the branch-addressed closeout route, so its memory-content commit is the memory side of the same code-to-memory pairing as worktree closeout, and it carries the same attribution: the closeout's own message plus exactly one `Code-Commit:` trailer naming the verified code commit.

## Code Commentary

### Logic

It prepares the direct attempt, verifies candidate identity, runs integration quality, performs code/memory/ref publication, records mutation evidence, and classifies exact recovery actions.

The memory-content leg renders its commit message from the shared closeout input:
`_direct_memory_commit` takes `code_commit=operation_input.codeCommit` from
`execute_direct_landing` and commits
`direct_landing_input(...).effectiveInput.memory_content_message(code_commit)`, so this route's
memory-content object carries one `Code-Commit: <sha>` trailer exactly as the worktree route's does,
from the single definition on `EffectiveCloseoutInput` rather than a second rendering. The trailer
is written when the object is created because `prove_git_commit` journals that exact commit on the
next statement. The ledger leg is unchanged and unattributed: `_direct_ledger_commit` commits
`message_for("ledger")` through `commit_if_dirty`, and the `memory.md`-only commit names no code
commit.

The ledger leg compares the new memory content with the newest mapping for the unchanged code
commit. A historical same-code row is not a conflict: settings-only memory changes produce a new
memory commit and prepend a new current ledger row while retaining prior rows.

The exact-current-mapping path is deliberately split into three named predicates: mapping identity,
exact working-versus-HEAD ledger bytes, and the shared clean-at-expected-HEAD snapshot check. The
split removes compound control flow from `_existing_direct_mapping` without changing any accepted
or refused state. Clean-snapshot semantics are imported from `integration.mutation_evidence` so
execution and recovery cannot drift into separate definitions.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- Every mutation is journaled and candidate-bound; partial publication resumes from durable evidence; direct landing never masquerades as queued closeout.
- The memory-content commit is attributed and the ledger commit is not. Only `_direct_memory_commit` renders `memory_content_message(code_commit)`; the trailer is inside the object before `prove_git_commit` journals it, and this route owns no second rendering of the closeout message.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.
- Exact current mappings remain idempotent. A different historical mapping for the same code commit
  means the memory/ledger legs are pending, not terminally conflicting.
- Clean repository reuse means the shared snapshot predicate at the exact current HEAD; this file
  does not own a second status-fingerprint implementation.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required to establish this repository-owned implementation. | `_LedgerExecution` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:66-71 |

## Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's concrete API, control flow, and validation boundary are implemented here. | `_LedgerExecution` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:66-71 |
| The memory-content commit is attributed to the verified code commit through the shared closeout-input rendering, at creation, before its sha is proved and journalled. | `memory_content_message`; `_direct_memory_commit` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:270-274; mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:215-276 |
| The ledger commit is the unattributed one: it commits the raw ledger message and carries no trailer. | `message_for("ledger")`; `_direct_ledger_commit` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:323-327; mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:278-328 |
| Exact mapping reuse separates mapping identity, ledger-byte equality, and clean-at-HEAD proof. | `_existing_direct_mapping`; `_require_head_ledger_bytes` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:365-420 |
| The clean snapshot definition has one integration owner. | `snapshot_is_clean_at_head` | mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:42-57 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `_LedgerExecution` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:66-71 |

## Update History

- 2026-09-13T21:42+02:00 — 260913-LCA-L1 (uncommitted change set on `ar/260913-lca-l1-ar`): `_direct_memory_commit` gained a required keyword-only `code_commit`, and `execute_direct_landing` passes `operation_input.codeCommit`, so this branch-addressed closeout route commits `effectiveInput.memory_content_message(code_commit)` — the closeout's own body plus exactly one `Code-Commit: <sha>` trailer naming the verified code commit, rendered from the shared `EffectiveCloseoutInput` definition instead of a route-local copy. Recorded that `_direct_ledger_commit` is deliberately unattributed (`message_for("ledger")`, no trailer). Rebound the stale ranges on this card (`_existing_direct_mapping`/`_require_head_ledger_bytes` 365-420, `snapshot_is_clean_at_head` mutation_evidence.py:42-57) and added the attribution rows. Verification metadata remains closeout-owned; no acceptance claim and no verification stamp advanced.

- 2026-08-27T18:33+02:00 — Simplified the exact-current-mapping branch into named predicates and
  centralized clean-snapshot truth in mutation evidence. Behavior and refusal vocabulary remain
  unchanged; the former CRAP offender now has cyclomatic complexity 3.
- 2026-08-26T14:32+02:00 — Documented memory-only direct landing: a later memory state for unchanged
  code prepends a new current row and preserves same-code history; only exact current equality is
  idempotent. Verification remains closeout-owned.
- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
