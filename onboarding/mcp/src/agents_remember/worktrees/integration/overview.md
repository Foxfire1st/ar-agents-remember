# mcp/src/agents_remember/worktrees/integration

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-22T10:39+02:00 |
| lastVerifiedCommitHash | `eb7ea60ab9919f009fef58f81afe5861aa1709da` |
| lastVerifiedCommitDate | 2026-08-22T11:44:33+02:00|
| governingOverview | `../../../../overview.md` |

## Governing Overview

[mcp overview](../../../../overview.md)

## Purpose

The integration-authority package (260815-DAG master full-gate repair): branch authority and
repository helpers (`integration_branch_authority`, `integration_branch_repository`,
`integration_branch_types`), the operation authority and lifecycle store
(`integration_operation_authority`, `lifecycle_operation_identity`, `lifecycle_operation_lease`,
`lifecycle_operation_store`, `lifecycle_operations`), the quality gate (`integration_quality`,
`integration_quality_checkout`), the ref transaction (`integration_ref_transaction`), and the
organizational-completion trio (`organizational_completion`,
`organizational_completion_integration`, `organizational_completion_repair`). All moved here from
`worktrees/` (flat) so the integration seam owns one package.

## Hot Path Summary

Master integration, series closeout, closeout/reopen, and the memory carryover paths consume this
package: branch-backed authority checks (`require_*`), durable lifecycle operation leases, the
Dagger quality gate checkout, and organizational-completion integration/repair.

## Conventions

- The package keeps the `worktrees` layering altitude: it never imports the queue package's
  application layer.
- Authority refusals stay typed (`SprintLinkageError`/`CloseoutQueueError`-family or the
  `AgentsRememberError` family).

## Invariants And Boundaries

- Lifecycle operation identity/lease/store are runtime-authority surfaces (bounded, evictable).
- Integration never falls back to a host quality run; the Dagger graph owns acceptance.

## 260821-CLIVE-L1 Admission, Identity, And Recovery

Closeout integration now separates four owners: the contract lifecycle lease serializes filesystem writers; closeout admission stabilizes and normalizes candidate/plan before lifecycle compatibility; candidate identity binds accepted effective input and Git provenance; mutation evidence and recovery projection own crash classification. The typed integrate caller owns integrate retention, authority, and candidate derivation, while lease-bound closeout admission is the sole closeout candidate owner. The shared controller requires the supplied candidate and explicit authority, then separates generation creation/conflict/terminal replacement from recovery/launch/projection; it cannot recapture closeout provenance or infer kind-specific authority from ambient state. For closeout, reconciliation precedes queued-record publication, and worker liveness is meaningful only while the record is queued/running because all production writers clear the PID outside those states. The store is strict schema 3.0 and relies on model/public fill-only boundaries for impossible leg-set or proven-commit rewrites while retaining transition-specific identity/state/pre-state checks. Duplicates validate against the immutable accepted plan, and generation retention requires commit-proven mutation or exact canonical contract-finalization publication. Queue projection is not an input or lifecycle-evidence owner.

## Update History

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 candidate-11: route ownership now records typed integrate versus lease-bound closeout callers, required shared-core values, and separated generation/recovery stages against accepted tree `4241908c`; verification metadata remains closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: created the `worktrees/integration`
  route — fourteen modules moved from `worktrees/` (flat). Verified at code commit e5cb139f.
