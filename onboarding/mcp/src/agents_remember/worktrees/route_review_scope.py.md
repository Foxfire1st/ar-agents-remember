# mcp/src/agents_remember/worktrees/route_review_scope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/route_review_scope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-13T11:43+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634`|
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Worktrees overview](overview.md)

## Purpose

Owns canonical route-review scope resolution and currentness for the integration boundary. It
ensures the one master review is derived from the series contract and current candidate evidence,
while atomic child operations remain deferred from independent review publication.

## Code Commentary

### Logic

`resolve_atomic_master_scope` resolves the master and ordered child membership from the canonical
series contract. `require_current_route_review` dispatches by execution shape; an atomic child
returns a typed deferred result and an atomic series returns
`deferred-atomic-master-until-integration`, while standalone routes retain their current review
requirement. The integration-time master currentness gate `require_current_master_route_review` is
deleted. `build_master_route_review` still constructs the current master record for
`task_doc.record_route_review`. Dependency and candidate-tree helpers refuse missing or stale
inputs rather than substituting status-only bookkeeping.

Review state is derived from the review records rather than gating on persisted state: the R27
resolved-state guard (`_require_review_state_resolved`) is deleted, so a sealed or pending review
state no longer refuses route-review admission. Atomic child review remains deferred to the
integration owner; this resolver adds no caller identity, authentication, or settings round cap.

### Conventions

The canonical contract and task-document refs are the authority for membership and order. Status
fields are operational observations and are excluded from the aggregate identity.

### Invariants And Boundaries

- Atomic child closeout never publishes an independent route-review record.
- Master review construction requires the exact current candidate, ordered child membership, intent identities,
  evidence, dependencies and scope digest.
- Integration runs no master-review gate: it deliberately does not re-run full code/memory quality, leaving that
  to the focused in-leaf checks and the pre-integration adversarial review.
- This module resolves review scope; integration publication still owns the lock and protected ref.

### Todos

None.

## Docs References

No relevant domain documentation was configured for this repository-internal resolver.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation source was configured for this source-owned resolver. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Atomic master scope resolution and child deferral. | `resolve_atomic_master_scope`; `reject_atomic_child_route_review` | mcp/src/agents_remember/worktrees/route_review_scope.py:79-152; mcp/src/agents_remember/worktrees/route_review_scope.py:187-196 |
| Master currentness enforcement is gone from integration; only aggregate record construction remains. | `build_master_route_review` | mcp/src/agents_remember/worktrees/route_review_scope.py:199-251 |
| Integration owns no master-review gate: `require_current_route_review` returns "deferred-atomic-master-until-integration" for an atomic series instead of requiring the accumulated master review. | `require_current_route_review` | mcp/src/agents_remember/worktrees/route_review_scope.py:155-184 |
| Integration publication calls the current master review inside authority. | `publish_series_integration_under_authority` | mcp/src/agents_remember/worktrees/series_closeout.py:73-89 |

## Cross-Repo References

No meaningful cross-repo implementation reference is required for this resolver card. The
coordination requirement is tracked in the task report and governs this preparation without serving
as a source citation here.

## Source File Binding

The active L40 binding for this card is the exact current source-file bytes: SHA-256
`11501a1c800d2b782403c9d30ebef17ed3ad2f2540d7a74d9c7ff4321d2cf0d5` (`20441` bytes,
`531` lines). The R27 domain-foundation composition manifest records the same path bytes. The
source remains an uncommitted preparation candidate, so verification metadata remains
closeout-owned.

## Historical Candidate Binding

The predecessor v2 cumulative candidate tree was `96b94b2a1c8e57a7a37b19b08cda33db93fe81b6`,
with this file's SHA-256 recorded as
`7e0e070a9086438aeda0bf858b76796b444fe875d5ed8a00338cd4181e1f12c5`. That whole-tree identity
is retained as historical composition evidence and is not the active identity for this card.

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `publish_series_integration_under_authority` repointed to mcp/src/agents_remember/worktrees/series_closeout.py:73-89. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: `publish_series_integration_under_authority` repointed to mcp/src/agents_remember/worktrees/series_closeout.py:73-89. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T08:49:05+00:00: Generated citation repair: `publish_series_integration_under_authority` repointed to mcp/src/agents_remember/worktrees/series_closeout.py:74-90. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T23:05:00+00:00: Repaired two claims. The card asserted master currentness enforcement through `require_current_master_route_review` (scope, aggregate intent, candidate tree, evidence, dependencies, digest) plus an R27 resolved fixed-list review-state guard. Both are gone: `require_current_master_route_review` was deleted with the integration master-review gate (its only caller was `master_route_review_block`, itself removed), `_require_review_state_resolved` was deleted so review state derives from the review records instead of gating, and `require_current_route_review` (155-184) now returns `deferred-atomic-master-until-integration` for an atomic series. `build_master_route_review` (199-251) survives as the aggregate record constructor for `task_doc.record_route_review`.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `reject_atomic_child_route_review`, `resolve_atomic_master_scope` repointed to mcp/src/agents_remember/worktrees/route_review_scope.py:187-196, mcp/src/agents_remember/worktrees/route_review_scope.py:79-152. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `publish_series_integration_under_authority` repointed to mcp/src/agents_remember/worktrees/series_closeout.py:53-69. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:41:10+00:00: Generated citation repair: `publish_series_integration_under_authority` repointed to mcp/src/agents_remember/worktrees/series_closeout.py:61-78. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-09T14:10+02:00 — CCR-L42 curator intake created/reconfirmed this one-to-one card against the current uncommitted source bytes (SHA-256 `11501a1c800d2b782403c9d30ebef17ed3ad2f2540d7a74d9c7ff4321d2cf0d5`, `20441` bytes, `531` lines). Verification remains closeout-owned; no test, review, acceptance, or future commit is asserted.

- 2026-09-08T22:01:43+02:00 — CCR-R27 domain-foundation preparation: rebound the active source identity to the exact L40 `route_review_scope.py` bytes and recorded resolved fixed-list state before master currentness; prior L24 candidate binding remains historical and verification metadata remains unchanged.
- 2026-09-08T19:27:46+02:00 — Final L24 identity cleanup: verified unchanged source bytes against the immutable v3 manifest (`7e0e070a9086438aeda0bf858b76796b444fe875d5ed8a00338cd4181e1f12c5`, 20344 bytes, 529 lines); replaced the active whole-tree binding with exact source-file binding and preserved `96b94b2a1c8e57a7a37b19b08cda33db93fe81b6` as historical. Closeout-owned verification metadata and shared overviews were not edited.
- 2026-09-08T18:14:20+02:00 — CCR-L24 bounded memory-quality repair: updated the active candidate identity to frozen v2 while preserving the prior v1 history; no verification pin was fabricated.
- 2026-09-08T17:31:25+02:00 — CCR-L24 final-v2 source binding: rebased active R25/R26 citation ranges against the frozen cumulative source; verification remains closeout-owned.

- 2026-09-08T16:42+02:00 — CCR-R26 source-grounded preparation: created the card from the frozen
  worktree source. Commit-owned verification metadata remains intentionally blank until the source
  lands in Git.
