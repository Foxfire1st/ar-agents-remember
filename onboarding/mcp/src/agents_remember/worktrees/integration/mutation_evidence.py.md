# mcp/src/agents_remember/worktrees/integration/mutation_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/mutation_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash |  `eb7ea60ab9919f009fef58f81afe5861aa1709da`|
| lastVerifiedCommitDate |  2026-08-22T11:44:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktree integration overview](overview.md)

## Purpose

Implements the journaled closeout Git-mutation protocol: snapshot, mutation intent, expected output binding, exact commit proof, and post-crash reconciliation for each enabled repository leg.

## Code Commentary

### Logic

`initial_closeout_mutation_evidence` relies on the validated effective-input/contract pairing for repository applicability, then creates cells for exactly the enabled legs. `begin_git_mutation` validates that the lifecycle operation authorizes the enabled leg and exact contract repository, records the pre-mutation snapshot, and durably publishes intent before Git. `bind_expected_output_tree` captures the staged result where applicable. `prove_git_commit` requires the exact branch, single-parent advance, parent/tree relation, and observed repository state before publishing commit-proven evidence.

Reconciliation compares the current repository with the durable before/expected facts. An exact unchanged snapshot becomes `reconciled-unchanged`; an exact expected output becomes commit-proven; moved-and-returned refs, wrong refs, unexpected trees, or ambiguous state refuse loudly. Cancellation is permitted only before any intent or proven evidence.

### Invariants And Boundaries

- Non-preview worktree closeout requires journal-backed `operation_progress`; legacy synchronous CLI apply and generic-operation bypass fail closed.
- Only repositories and legs enabled by the accepted effective input may mutate.
- Evidence publication, not phase names or recovery cells, defines the mutation boundary.
- This does not journal direct landing; L1 leaves that path lock-serialized and synchronous.

### Todos

L2-R11 owns durable direct-landing recovery; L5-R15 owns its forcing proof.

## Docs References

See task `260821-CLIVE-L1` L1-R4 through L1-R6.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Journal authority is mandatory for non-preview closeout. | `require_closeout_mutation_authority` | `mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:31-34` |
| Intent precedes Git and is repository-bound. | `begin_git_mutation` | `mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:52-72` |
| Commit proof verifies the exact transition. | `prove_git_commit` | `mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:98-128` |
| Restart classifies exact unchanged, exact output, and ambiguity separately. | `reconcile_closeout_mutations` | `mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:131-175` |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from candidate tree `4241908c`; verification metadata remains blank pending landed commit.
