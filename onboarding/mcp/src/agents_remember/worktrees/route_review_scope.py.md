# mcp/src/agents_remember/worktrees/route_review_scope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/route_review_scope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-09T14:10+02:00 |
| lastVerifiedCommitHash | `6096941f41204c9a7d6ccb2b29f6b2e862ed56b4`|
| lastVerifiedCommitDate | 2026-09-10T09:57:27+02:00|
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
returns a typed deferred result, while standalone and organizational routes retain their current
review requirement. `require_current_master_route_review` validates the master scope, aggregate
intent, candidate tree, evidence and dependency inputs, and content digest. `build_master_route_review`
constructs the current master record. Dependency and candidate-tree helpers refuse missing or stale
inputs rather than substituting status-only bookkeeping.

R27 keeps fixed-list review state in the same currentness boundary: master review admission calls
the shared resolved-state guard before accepting a route record. Missing state remains zero, while a
pending round or unresolved sealed findings refuse. Atomic child review remains deferred to the
integration owner; this resolver adds no caller identity, authentication, or settings round cap.

### Conventions

The canonical contract and task-document refs are the authority for membership and order. Status
fields are operational observations and are excluded from the aggregate identity.

### Invariants And Boundaries

- Atomic child closeout never publishes an independent route-review record.
- Master currentness requires the exact current candidate, ordered child membership, intent identities,
  evidence, dependencies and scope digest.
- No fallback to a status-only or stale record is permitted.
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
| Atomic master scope resolution and child deferral. | `resolve_atomic_master_scope`; `reject_atomic_child_route_review` | mcp/src/agents_remember/worktrees/route_review_scope.py:80-153; mcp/src/agents_remember/worktrees/route_review_scope.py:251-260 |
| Master currentness and aggregate record construction. | `require_current_master_route_review`; `build_master_route_review` | mcp/src/agents_remember/worktrees/route_review_scope.py:187-315 |
| Master review currentness also requires resolved fixed-list review state. | `require_current_master_route_review` | mcp/src/agents_remember/worktrees/route_review_scope.py:188-239 |
| Integration publication calls the current master review inside authority. | `publish_series_integration_under_authority` | mcp/src/agents_remember/worktrees/series_closeout.py:61-78 |

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
- 2026-09-10T07:41:10+00:00: Generated citation repair: `publish_series_integration_under_authority` repointed to mcp/src/agents_remember/worktrees/series_closeout.py:61-78. No content impact: mechanical anchor-range projection bound to citation source snapshot 794cfaf55738c596793ad49b95a946add84e2c03f1bf6499e2f00c6b84bd85ba; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-09T14:10+02:00 — CCR-L42 curator intake created/reconfirmed this one-to-one card against the current uncommitted source bytes (SHA-256 `11501a1c800d2b782403c9d30ebef17ed3ad2f2540d7a74d9c7ff4321d2cf0d5`, `20441` bytes, `531` lines). Verification remains closeout-owned; no test, review, acceptance, or future commit is asserted.

- 2026-09-08T22:01:43+02:00 — CCR-R27 domain-foundation preparation: rebound the active source identity to the exact L40 `route_review_scope.py` bytes and recorded resolved fixed-list state before master currentness; prior L24 candidate binding remains historical and verification metadata remains unchanged.
- 2026-09-08T19:27:46+02:00 — Final L24 identity cleanup: verified unchanged source bytes against the immutable v3 manifest (`7e0e070a9086438aeda0bf858b76796b444fe875d5ed8a00338cd4181e1f12c5`, 20344 bytes, 529 lines); replaced the active whole-tree binding with exact source-file binding and preserved `96b94b2a1c8e57a7a37b19b08cda33db93fe81b6` as historical. Closeout-owned verification metadata and shared overviews were not edited.
- 2026-09-08T18:14:20+02:00 — CCR-L24 bounded memory-quality repair: updated the active candidate identity to frozen v2 while preserving the prior v1 history; no verification pin was fabricated.
- 2026-09-08T17:31:25+02:00 — CCR-L24 final-v2 source binding: rebased active R25/R26 citation ranges against the frozen cumulative source; verification remains closeout-owned.

- 2026-09-08T16:42+02:00 — CCR-R26 source-grounded preparation: created the card from the frozen
  worktree source. Commit-owned verification metadata remains intentionally blank until the source
  lands in Git.
