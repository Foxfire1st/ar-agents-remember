# mcp/src/agents_remember/worktrees/integration/mutation_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/mutation_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
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
- Direct landing uses its own typed operation/ledger-intent evidence in the canonical root journal;
  this file remains the closeout Git-leg evidence owner.

### Todos

L2-R11 owns durable direct-landing recovery; L5-R15 owns its forcing proof.

## Docs References

See task `260821-CLIVE-L1` L1-R4 through L1-R6.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Journal authority is mandatory for non-preview closeout. | `require_closeout_mutation_authority` | mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:40-43 |
| Intent precedes Git and is repository-bound. | `begin_git_mutation` | mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:69-89 |
| Commit proof verifies the exact transition. | `prove_git_commit` | mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:253-283 |
| Restart classifies exact unchanged, exact output, and ambiguity separately. | `reconcile_closeout_mutations` | mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:286-355 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L2 Current Contract

The current source seams include `require_closeout_mutation_authority`, `initial_closeout_mutation_evidence`, `begin_git_mutation`. This closeout evidence owner remains intent-before-Git and exact-state reconciled. Direct landing is no longer excluded as “unjournaled”; it uses its own operation input and ledger intent while sharing the root-journal recovery architecture.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `require_closeout_mutation_authority`, `initial_closeout_mutation_evidence`, `begin_git_mutation` at this ownership boundary. | `require_closeout_mutation_authority`; `initial_closeout_mutation_evidence`; `begin_git_mutation` | mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:40-43; mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:46-66; mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:69-89 |

## Update History

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout-input model package relocation; intent-before-Git mutation evidence and exact reconciliation are unchanged.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from candidate tree `4241908c`; verification metadata remains blank pending landed commit.
