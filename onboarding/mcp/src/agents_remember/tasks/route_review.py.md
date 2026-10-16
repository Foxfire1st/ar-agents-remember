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

- Each review state has checked-candidate and authority-resolved identity fields. The operation payload now selects code or memory through reviewKind, and typed recorded rounds retain that kind; no authentication field or approval-authenticity proof is added. Admission is owned by `worktrees/review_history.py`.
- The transition service enforces the settings number plus cumulative approved extras. This model records architect/developer words without authenticating their author and keeps legacy developerApproval readable.
- Route-review content addressing remains all-or-nothing, and atomic-master scope remains
  integration-owned.

### Todos

None.

## Current Contract

ReviewRound records positive round number, finite code/memory kind, whether findings remained when that round was recorded, and optional verdict reference. ReviewState gains a default-empty recordedRounds list; its existing baseline/remaining and approval consistency checks remain. MemoryReviewState is an Annotated ReviewState with an after-validator refusing any recorded row whose kind is not memory. Complete ordered history is checked by review_count_unavailable at counting time, not guaranteed by this list declaration; legacy records are not backfilled or reinterpreted. Each lane shares the same settings-limit/extra-round protocol without sharing a counter or baseline.


The governing workflow opens an independent memory review after CODE PASS on the same task using begin_review/record_review with reviewKind=memory. It has its own immutable baseline and shrinking IDs, under the same settings limit and extra-round approval rule, and never resets code reviewState. The signed rollout applies only to memory reviews begun after L88 lands; already-underway reviews (L168, L56, L57, L59) finish with their sealed-report workflow, with no migration/backfill. This describes the candidate contract, not a claim that the serving build already supports it.

This account is bound to the candidate source, not a claim of a running serving build or a fresh execution/acceptance verdict. Existing historical accounts remain historical.

## Evidence


- Worker/Curator typed review census, record-only exclusion and unknown history. [4]
- Reason admission, threshold and differing-harness/model inheritance boundary. [5]
- Record-only memory identity comes from memory authority, never the sibling code root. [6]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [7]

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
