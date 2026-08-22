# mcp/src/agents_remember/models/lifecycles/mutation_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/mutation_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-22T11:29+02:00 |
| lastVerifiedCommitHash |  `eb7ea60ab9919f009fef58f81afe5861aa1709da`|
| lastVerifiedCommitDate |  2026-08-22T11:44:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[lifecycle models overview](overview.md)

## Purpose

Defines durable, repository-bound evidence for every enabled closeout mutation leg. Its states distinguish what was merely observed, what mutation was announced before Git, what was reconciled as unchanged after ambiguity, and what exact commit was proven.

## Code Commentary

### Logic

`GitMutationSnapshot` records branch/ref, HEAD and tree, reflog fingerprint, index tree, candidate tree, and worktree-status fingerprint. `GitMutationEvidence` binds one enabled leg and repository to `pre-mutation`, `mutation-intent`, `reconciled-unchanged`, or `commit-proven`, with before/observed snapshots, expected output tree, and commit proof as required by the state.

The model validators prevent semantic laundering: every non-`commit-proven` state is forbidden
from naming a commit, `reconciled-unchanged` must reproduce the exact before snapshot, and
`commit-proven` must bind the observed ref, commit, and tree. A reconciled-unchanged record may
retain an `expectedOutputTree` that differs from `before.headTree`: the former is the tree bound to
the announced mutation intent, while the exact restored observation proves that no commit landed.
These records are the durable facts from which closeout recovery projection is derived.

### Invariants And Boundaries

- A progress phase or boolean is not mutation evidence.
- Intent is written before the Git mutation it authorizes.
- Reconciliation is repository-, ref-, and tree-specific; a ref that moved away and back is detected through the reflog fingerprint.
- Only `commit-proven` evidence may name a commit; an expected output tree alone is not commit proof.
- Exact restoration preserves the previously bound expected output tree even when it differs from
  the restored HEAD tree.
- Verified-existing/no-op outcomes are not fabricated into commit-proven Git mutations.
- The queue does not own or retain these facts; the lifecycle operation journal does.

### Todos

Direct landing remains synchronous and unjournaled in L1; durable memory-before-ledger recovery is L2-R11 and its forcing is L5-R15.

## Docs References

See task `260821-CLIVE-L1` L1-R4 and L1-R6.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The four-state vocabulary is closed and explicit. | `MutationEvidenceState` | mcp/src/agents_remember/models/lifecycles/mutation_evidence.py:9-15 |
| Snapshot identity includes reflog, index, candidate, and status facts. | `GitMutationSnapshot` | mcp/src/agents_remember/models/lifecycles/mutation_evidence.py:18-29 |
| State-specific proof is model validated. | `GitMutationEvidence` | mcp/src/agents_remember/models/lifecycles/mutation_evidence.py:32-61 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-08-22T11:29+02:00 — 260821-CLIVE-L1 candidate12 rebind: recorded the
  all-non-commit-proven commit prohibition and the legitimate preservation of a differing bound
  expected tree after exact restoration; corrected the pre-existing candidate11 symbol-name drift
  against source. Bound to reviewed candidate tree `8f03b256fe24aa77262da805f1538ee39ccb4dd6`,
  full diff SHA `ccb36a898b455cd67ca00c378e5ba0f18851be01faf3d26eced3b9af062f429e`,
  same-reviewer PASS; first landed verification stamp remains closeout-owned.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from accepted candidate tree `4241908c`; first landed verification stamp remains closeout-owned.
