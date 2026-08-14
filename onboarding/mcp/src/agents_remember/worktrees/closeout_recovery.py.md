# mcp/src/agents_remember/worktrees/closeout_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/closeout_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-14T05:26Z |
| lastVerifiedCommitHash | `100b40d6be4a7d03eedbb1164ce54e2e8a314038` |
| lastVerifiedCommitDate |  2026-08-14T08:23:37+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

Own the restart-safe proof and journaling around closeout's irreversible code, memory, and ledger
Git boundaries. This module lets the durable lifecycle worker resume an accepted candidate without
recommitting code, selecting a stale pre-attempt memory commit, or duplicating a ledger edge.

## Code Commentary

### Logic

`accepted_code_commit` either proves the journaled code commit at clean task HEAD, adopts a clean
post-claim HEAD during recovery, or creates the first commit through the already-selected strict or
non-strict commit primitive. It then proves the commit tree equals the immutable accepted candidate
and journals the code cell before returning. `resume_external_commits` requires a clean memory
worktree, reconciles the exact code-to-memory row, creates only a missing matching row, proves an
existing memory commit is reachable, and journals the complete tuple.

### Conventions

Recovery state is passed through typed `WorktreeArgs` and published through
`report_operation_progress`; Git and ledger writes use the existing guarded primitives.

### Invariants And Boundaries

- A non-empty journaled commit cell is evidence to prove, never a hint to overwrite.
- The accepted candidate tree must equal the committed code tree.
- A conflicting ledger mapping, wrong memory HEAD, or unreachable memory commit fails closed.
- Each irreversible Git boundary is journaled before the next one begins.
- This module does not run quality, claim approval, or amend the task contract.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this repository-internal recovery seam.

## Repo-Internal References

The production helpers and focused recovery suite are the direct evidence for this boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| Code recovery proves clean HEAD and the accepted tree before journaling the code cell. | `accepted_code_commit` | mcp/src/agents_remember/worktrees/closeout_recovery.py:23-58 |
| External recovery reconciles the exact memory and ledger edge before journaling the full tuple. | `resume_external_commits` | mcp/src/agents_remember/worktrees/closeout_recovery.py:61-102 |
| The regression suite covers mismatched code, conflicting or unreachable memory, exact completion, and the stale-contract-memory crash window. | `CloseoutRecoveryTests` | mcp/tests/test_worktree_closeout_recovery.py:54-327 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

## Update History

- 2026-08-14T05:26Z — Created for the L23 final candidate: documented monotonic closeout commit
  recovery and the exact code-to-memory-to-ledger reconciliation boundary. Verification remains
  closeout-owned until the source commit exists.
