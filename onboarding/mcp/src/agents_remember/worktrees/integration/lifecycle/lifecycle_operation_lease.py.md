# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_lease.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_lease.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T10:05+02:00|
| lastVerifiedCommitHash | `f93ac631ca161e5880db3a937728cb256686b13b` |
| lastVerifiedCommitDate | 2026-09-04T09:56:23+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[governing overview](../overview.md)

## Purpose

Prevents closeout, integration, cleanup, and abandon from concurrently owning the same contract.

## Code Commentary

The per-contract lease serializes filesystem lifecycle writers across operation kinds. It is pure
serialization: it does not inspect durable operation records. Callers stabilize and validate their
candidate/input while holding the lease, then use `require_lifecycle_operation_compatible` to
decide same-kind or cross-kind conflict before journal or terminal mutation.

## Invariants And Boundaries

- Lease identity is canonical contract identity.
- Operation compatibility is a separate explicit decision made while the lease is held.
- Terminal synchronous writers must acquire the same lease as detached operation launch.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Lease location is derived from the canonical contract. | `_lease_path` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_lease.py:39-53 |
| The context manager owns only contract-scoped filesystem serialization. | `contract_lifecycle_lease` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_lease.py:84-99 |
| Record-aware same/cross-kind conflict is explicit and separate. | `require_lifecycle_operation_compatible` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_lease.py:102-126 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L1 Lease Scope Correction

`contract_lifecycle_lease` is now a pure per-contract filesystem serialization lease. It does **not** census active operation records or decide same/cross-kind compatibility. Callers acquire the lease, stabilize and validate candidate/input, then call `require_lifecycle_operation_compatible` before journaling or terminal mutation. This separation lets malformed input refuse without observing lifecycle state while preserving cross-writer serialization.

## 260821-CLIVE-L2 Current Contract

The current source seams include `contract_lifecycle_lease`, `require_lifecycle_operation_compatible`, `require_legacy_operation_compatible`. The lifecycle lease serializes journal decisions while preserving existing operation-specific Git locks. It does not add a global configured-contract lock or turn task authoring into a lifecycle-dependent operation.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `contract_lifecycle_lease`, `require_lifecycle_operation_compatible`, `require_legacy_operation_compatible` at this ownership boundary. | `contract_lifecycle_lease`; `require_lifecycle_operation_compatible`; `require_legacy_operation_compatible` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_lease.py:84-99; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_lease.py:102-126; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_lease.py:129-145 |

## 260821-CLIVE Stable External Lease

The operation lease now lives outside the deletable enclosure at the stable locator sibling
`locks/<full-contract-hash>.lock`. A supplied location must name that same stable locator, and active
operation inspection uses strict record reads plus projected exits. Terminal cleanup therefore
cannot delete the lock that serializes its own final transaction.

## CCR-R18@v1 Terminal Status Vocabulary

260831-CCR-L18 added the `_TERMINAL = frozenset({"completed", "failed", "cancelled"})` module constant (line 20) alongside the existing `_ACTIVE` set, so the lease/compatibility seam can classify terminal lifecycle statuses without string literals. Serialization semantics are unchanged: the lease remains pure per-contract filesystem serialization that never inspects durable operation records.

## Update History

- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: recorded the `_TERMINAL` status vocabulary constant on the per-contract lease seam. Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the worker-state package relocation; external lease identity and strict location matching are unchanged.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: recorded the stable external lease and strict location match. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_lease.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/lifecycle_operation_lease.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created cross-operation lifecycle lease onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
## Docs References

No external Domain Documentation source is configured for this internal route; task `260821-CLIVE-L1` and the cited repository source/tests govern this curation.

## Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
