# mcp/src/agents_remember/models/lifecycles/mutation_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/mutation_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:51+00:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[lifecycle models overview](overview.md)

## Purpose

Defines durable, repository-bound evidence for every enabled closeout mutation leg. Its states distinguish what was merely observed, what mutation was announced before Git, what was reconciled as unchanged after ambiguity, and what exact commit was proven.

## Code Commentary

### Logic

Mutation legs are only `code` and `memory`. Memory snapshots may additionally carry
`contentHeadTree`, the HEAD content tree with the cache excluded, while `head` and `headTree`
still identify the actual Git commit and raw tree. This separate comparison view lets memory
content remain unchanged when cache bytes differ without weakening ref, reflog, or output proof.

`GitMutationSnapshot` records branch/ref, HEAD and tree, reflog fingerprint, index tree, candidate tree, and worktree-status fingerprint. `GitMutationEvidence` binds one enabled leg and repository to `pre-mutation`, `mutation-intent`, `reconciled-unchanged`, or `commit-proven`, with before/observed snapshots, expected output tree, and commit proof as required by the state.

The model validators prevent semantic laundering: every non-`commit-proven` state is forbidden
from naming a commit, `reconciled-unchanged` must reproduce the exact before snapshot, and
`commit-proven` must bind the observed ref, commit, and tree. A reconciled-unchanged record may
retain an `expectedOutputTree` that differs from `before.headTree`: the former is the tree bound to
the announced mutation intent, while the exact restored observation proves that no commit landed.
These records are the durable facts from which closeout recovery projection is derived.

### Conventions

Keep actual Git object fields distinct from optional content-comparison fields. State-specific validation describes evidence; it never performs Git mutation.

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

No open todo is owned here. Direct landing uses the sibling lifecycle direct-landing accepted-input model; closeout mutation evidence remains deliberately repository-leg-specific.

## Docs References

See task `260821-CLIVE-L1` L1-R4 and L1-R6.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain-documentation source applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Only code/memory are mutation legs; memory snapshots may separately bind contentHeadTree without changing raw Git identity. | `CloseoutMutationLeg`; `GitMutationSnapshot` | mcp/src/agents_remember/models/lifecycles/mutation_evidence.py:9; mcp/src/agents_remember/models/lifecycles/mutation_evidence.py:18-30 |
| The four-state vocabulary is closed and explicit. | `MutationEvidenceState`; "MutationEvidenceState = Literal[" | mcp/src/agents_remember/models/lifecycles/mutation_evidence.py:10-15 |
| Snapshot identity includes reflog, index, candidate, and status facts. | `GitMutationSnapshot` | mcp/src/agents_remember/models/lifecycles/mutation_evidence.py:18-30 |
| State-specific proof is model validated. | `_require_state_evidence` | mcp/src/agents_remember/models/lifecycles/mutation_evidence.py:33-63 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| No separate external implementation source applies to this file. | — | — |

## 260821-CLIVE-L2 Current Contract

The current source seams include `GitMutationSnapshot`, `GitMutationEvidence`. Closeout Git evidence remains strict and repository-bound. Direct landing now has its own accepted-input model in the same lifecycle package, so the former “direct landing is unjournaled” boundary is obsolete.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `GitMutationSnapshot`, `GitMutationEvidence` at this ownership boundary. | `GitMutationSnapshot` | mcp/src/agents_remember/models/lifecycles/mutation_evidence.py:18-30 |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T00:51+00:00 — LCA-L9 current candidate: Bounded mutation legs to code/memory and documented the separate cache-free HEAD content tree. Reviewed the uncommitted source and current references; existing verification commit/date and all prior history are retained. No landed or test-execution claim.


- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T11:29+02:00 — 260821-CLIVE-L1 candidate12 rebind: recorded the
  all-non-commit-proven commit prohibition and the legitimate preservation of a differing bound
  expected tree after exact restoration; corrected the pre-existing candidate11 symbol-name drift
  against source. Bound to reviewed candidate tree `8f03b256fe24aa77262da805f1538ee39ccb4dd6`,
  full diff SHA `ccb36a898b455cd67ca00c378e5ba0f18851be01faf3d26eced3b9af062f429e`,
  same-reviewer PASS; first landed verification stamp remains closeout-owned.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from accepted candidate tree `4241908c`; first landed verification stamp remains closeout-owned.
