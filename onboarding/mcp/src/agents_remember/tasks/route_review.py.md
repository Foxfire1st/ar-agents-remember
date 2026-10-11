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

`ReviewApproval` records `by` as architect or developer and trims nonblank approval words. `ReviewState` carries round, pending, the sealed baseline and remaining IDs, plus `limit`, checked `candidateTree` and authority-resolved `candidateIdentity`. A new `approval` and the legacy `developerApproval` are mutually exclusive and pair with positive cumulative `additionalRounds`. A missing or legacy limit defaults to zero as a pre-limit sentinel; the transition/get owners compute the effective settings number plus extras. The validator keeps zero-round state empty, including approval/candidate/limit fields, requires unique baseline and remaining IDs, and requires remaining IDs to belong to the baseline. Missing `TaskDocument.reviewState` remains zero state.

`RouteReviewRecord` remains the candidate-bound persisted evidence record. Its coherence validator
keeps route verdicts consistent, requires aggregate intent when a scope is present, and treats
evidence digests, the dependency declaration, and record digest as an all-or-nothing group.

### Invariants And Boundaries

- Review state has checked-candidate and authority-resolved identity fields, but no caller-selected review purpose or authentication field; admission is owned by `worktrees/review_history.py`.
- The transition service enforces the settings number plus cumulative approved extras. This model records architect/developer words without authenticating their author and keeps legacy developerApproval readable.
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

## Historical L41 Source File Binding

At the historical L41 preparation, the source bytes were SHA-256
`b117340a17d8b38e60373e7878a609a48b615b1d5a7e75f330b4241a147afeb2`
(`8050` bytes, `209` lines). The source is an uncommitted preparation candidate, so
verification metadata remains blank until a genuine commit-owned refresh.
