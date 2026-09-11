# mcp/src/agents_remember/worktrees/integration/mutation_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/mutation_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T22:00:40+00:00 |
| lastVerifiedCommitHash | `3b552f5a215648274dc5e6e4d5f0a01c2ee80be2`|
| lastVerifiedCommitDate | 2026-09-12T01:54:48+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktree integration overview](overview.md)

## Purpose

Implements the journaled closeout Git-mutation protocol: snapshot, mutation intent, expected output binding, exact commit proof, and post-crash reconciliation for each enabled repository leg.

## Code Commentary

### Logic

`initial_closeout_mutation_evidence` relies on the validated effective-input/contract pairing for repository applicability, then creates cells for exactly the enabled legs. `begin_git_mutation` validates that the lifecycle operation authorizes the enabled leg and exact contract repository, records the pre-mutation snapshot, and durably publishes intent before Git. `bind_expected_output_tree` captures the staged result where applicable. `prove_git_commit` requires the exact branch, single-parent advance, parent/tree relation, and observed repository state before publishing commit-proven evidence.

Reconciliation compares the current repository with the durable before/expected facts. An exact unchanged snapshot becomes `reconciled-unchanged`; an exact expected output becomes commit-proven; moved-and-returned refs, wrong refs, unexpected trees or ambiguous state remain unresolved for the typed recovery consumer. Cancellation is permitted when no leg remains `mutation-intent` or `commit-proven`; an exactly unchanged intent may become `reconciled-unchanged` while retaining `expectedOutputTree`. That tree is intended output, not proof of a commit. Unreadable snapshot/reflog facts and conflicting intermediate state leave the original intent unchanged for same-generation recovery; they do not become false unchanged proof.

The module also owns the shared definition of an exact clean mutation snapshot: expected HEAD,
index tree, candidate tree, and the SHA-256 fingerprint of empty porcelain-v2 status must agree.
Direct execution and direct recovery consume `snapshot_is_clean` or
`snapshot_is_clean_at_head`; neither keeps a private duplicate.

### Invariants And Boundaries

- Closeout mutation evidence validates the enabled leg against the contract repository; the former journal-backed `operation_progress` requirement is deleted, so an in-process closeout is no longer refused for lacking a detached worker.
- Only repositories and legs enabled by the accepted effective input may mutate.
- Evidence publication, not phase names or recovery cells, defines the mutation boundary.
- Clean-snapshot truth is centralized here and compares exact Git identities, not a boolean caller
  assertion.
- Direct landing uses its own typed operation/ledger-intent evidence in the canonical root journal;
  this file remains the closeout Git-leg evidence owner.

### Todos

L2-R11 owns durable direct-landing recovery; L5-R15 owns its forcing proof.

## Docs References

See task `260821-CLIVE-L1` L1-R4 through L1-R6.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Journal authority is no longer a closeout precondition: `require_closeout_mutation_authority` is deleted, and `begin_git_mutation` validates only that the leg is enabled and the repository is inside contract authority through `_require_mutation_leg_authority`. | `_require_mutation_leg_authority`; `begin_git_mutation` | mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:555-567; mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:83-102 |
| One shared predicate defines exact clean state at current or expected HEAD. | `snapshot_is_clean`; `snapshot_is_clean_at_head` | mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:37-39; mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:42-57 |
| Intent precedes Git and is repository-bound. | `begin_git_mutation` | mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:83-102 |
| Commit proof verifies the exact transition. | `prove_git_commit` | mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:263-292 |
| Restart classifies exact unchanged, exact output, and ambiguity separately. | `reconcile_closeout_mutations` | mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:295-364 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260821-CLIVE-L2 Current Contract

The current source seams include `_require_mutation_leg_authority`, `initial_closeout_mutation_evidence`, `begin_git_mutation`. This closeout evidence owner remains intent-before-Git and exact-state reconciled. Direct landing is no longer excluded as “unjournaled”; it uses its own operation input and ledger intent while sharing the root-journal recovery architecture.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `_require_mutation_leg_authority`, `initial_closeout_mutation_evidence`, `begin_git_mutation` at this ownership boundary. | `_require_mutation_leg_authority`; `initial_closeout_mutation_evidence`; `begin_git_mutation` | mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:555-567; mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:60-80; mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:83-102 |

## Update History
- 2026-09-11T23:05:00+00:00: Repaired two claims. The card claimed `require_closeout_mutation_authority` made journal authority mandatory for non-preview closeout and listed it as a current module seam; that gate (JOURNALED_CLOSEOUT_REQUIRED plus its five internal call sites, the `modules/closeout.py` call and the CLI refusal) is deleted, and the module now validates an enabled leg and its contract repository through `_require_mutation_leg_authority` (555-567), with `initial_closeout_mutation_evidence` (60-80) and `begin_git_mutation` (83-102) unchanged.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `snapshot_is_clean`; `snapshot_is_clean_at_head` repointed to mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:37-39; mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:42-57. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `begin_git_mutation` repointed to mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:83-102. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `prove_git_commit` repointed to mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:263-292. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `reconcile_closeout_mutations` repointed to mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:295-364. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-06T22:00:40+00:00 — Corrected current journal recovery semantics against production source while preserving previous verification pins. Source inspection only.


- 2026-08-27T18:33+02:00 — Centralized the exact clean-snapshot predicate previously duplicated
  by direct execution and recovery state; no mutation or recovery acceptance semantics changed.
- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout-input model package relocation; intent-before-Git mutation evidence and exact reconciliation are unchanged.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from candidate tree `4241908c`; verification metadata remains blank pending landed commit.
