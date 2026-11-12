# mcp/src/agents_remember/models/lifecycles/mutation_evidence.py

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

## Evidence

### Docs References

See task `260821-CLIVE-L1` L1-R4 and L1-R6.

No configured external domain-documentation source applies.

### Repo-Internal References

- Only code/memory are mutation legs; memory snapshots may separately bind contentHeadTree without changing raw Git identity. [1]
- The four-state vocabulary is closed and explicit. [2]
- Snapshot identity includes reflog, index, candidate, and status facts. [3]
- State-specific proof is model validated. [4]

### Cross-Repo References

No meaningful cross-repository reference applies.

No separate external implementation source applies to this file.

## 260821-CLIVE-L2 Current Contract

The current source seams include `GitMutationSnapshot`, `GitMutationEvidence`. Closeout Git evidence remains strict and repository-bound. Direct landing now has its own accepted-input model in the same lifecycle package, so the former “direct landing is unjournaled” boundary is obsolete.

### Reconciled Source Evidence

- The current module exposes `GitMutationSnapshot`, `GitMutationEvidence` at this ownership boundary. [5]
