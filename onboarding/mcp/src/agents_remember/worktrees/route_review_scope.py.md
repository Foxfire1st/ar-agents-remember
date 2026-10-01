# mcp/src/agents_remember/worktrees/route_review_scope.py

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

## Evidence

### Docs References

No relevant domain documentation was configured for this repository-internal resolver.

No external documentation source was configured for this source-owned resolver.

### Repo-Internal References

- Atomic master scope resolution and child deferral. [1]
- Master currentness enforcement is gone from integration; only aggregate record construction remains. [2]
- Integration owns no master-review gate: `require_current_route_review` returns "deferred-atomic-master-until-integration" for an atomic series instead of requiring the accumulated master review. [3]
- Integration publication calls the current master review inside authority. [4]

### Cross-Repo References

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
