# mcp/tests/test_task_reopen_guards.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_reopen_guards.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Holds the bounded refusal-only reopen cases split from `test_task_reopen.py` so both suites remain
below the repository file-size limit while preserving direct production-path coverage.

## Code Commentary

### Logic

The suite reuses the canonical landed-leaf and task-document fixtures. It refuses incomplete
closeout/cleanup, non-leaf contracts, surviving worktrees, and stale transitive source lineage;
the last case also proves the contract and leaf task document remain byte-identical.

### Invariants And Boundaries

- Every test calls the real `reopen_task` owner.
- The split changes only test location; blocker assertions and mutation checks are preserved.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Incomplete, non-leaf, and surviving-worktree contracts refuse reopen. | `ReopenGuardTests` | mcp/tests/test_task_reopen_guards.py:15-44 |
| Moved super ancestry refuses before contract or task-document mutation. | `test_moved_super_refuses_before_reopen_mutates_task_state` | mcp/tests/test_task_reopen_guards.py:73-92 |

## Current Contract — 260821 CLIVE Final

This is the current source-backed contract for this test card. It supersedes any earlier
queue-lifecycle, blocker-row, replan/drain, or compatibility-reader wording where present.

Forces reopen refusal for stale lineage, nonterminal or inconsistent contract state, and protected authority conflicts.

### Current Invariants

- Unsafe reopen leaves task and contract bytes unchanged.
- Refusals name the exact transition needed instead of inventing compatibility behavior.

## Update History

- 2026-08-26T10:44:52+02:00 — No behavior change: reopen guard fixtures now import from `task_reopen_test_support`; guard and refusal semantics are unchanged.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-16T02:51+02:00 — No content impact: the stale-lineage fixture explicitly checks out the
  task-derived `super` ref before advancing it, so the existing refusal and byte-preservation
  assertions reach the intended named-ref state.

- 2026-08-15T10:24+02:00 — Created by the L3 file-size repair from `ReopenGuardTests`; behavior,
  fixtures, and assertions are unchanged.
