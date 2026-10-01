# mcp/src/agents_remember/tasks/route_review.py

## Governing Overview

[tasks/overview.md](overview.md)

## Purpose

Persisted route-review models shared by task documents and worktree review gates. The module also
owns the small fixed-list `ReviewState` record that makes review progress explicit without
introducing a second review-history store.

## Code Commentary

### Logic

`RouteReviewUnit` records one reviewed route and its evidence reference. `RouteReviewChildIntent`
and `RouteReviewScope` bind ordered atomic-master children to their canonical task intents.
`ReviewFinding` is the immutable finding definition used by the review state transition layer.

`ReviewState` carries a monotonic round number, a pending bit, a sealed baseline finding list, and
the remaining finding IDs. It also persists one nonblank `developerApproval` answer with its
positive cumulative `additionalRounds` allowance when the ordinary limit is exhausted. Its
validator requires unique baseline and remaining IDs, makes a zero-round state empty, requires
remaining IDs to belong to the sealed baseline, and requires the recorded permission and allowance
to appear together. Missing `TaskDocument.reviewState` is interpreted by the document and
transition owners as zero state.

`RouteReviewRecord` remains the candidate-bound persisted evidence record. Its coherence validator
keeps route verdicts consistent, requires aggregate intent when a scope is present, and treats
evidence digests, the dependency declaration, and record digest as an all-or-nothing group.

### Invariants And Boundaries

- Review state has no caller-selected purpose, identity, or authentication field; transition
  admission is owned by `worktrees/review_history.py`.
- The ordinary three-round limit is enforced by the transition service; this model carries only the
  bounded recorded developer permission and cumulative allowance used after exhaustion. It does
  not authenticate the answer or introduce a second authority.
- Route-review content addressing remains all-or-nothing, and atomic-master scope remains
  integration-owned.

### Todos

None.

## Evidence

### Docs References

No external Domain Documentation source governs these repository-owned models.

No configured external source applies.

### Repo-Internal References

- Route and child-intent model shapes. [1]
- Fixed-list finding, round-cap permission fields, and review-state validation. [2]
- Candidate-bound route record coherence and content-addressing checks. [3]

## Source File Binding

The current L41 source bytes are SHA-256
`b117340a17d8b38e60373e7878a609a48b615b1d5a7e75f330b4241a147afeb2`
(`8050` bytes, `209` lines). The source is an uncommitted preparation candidate, so
verification metadata remains blank until a genuine commit-owned refresh.
