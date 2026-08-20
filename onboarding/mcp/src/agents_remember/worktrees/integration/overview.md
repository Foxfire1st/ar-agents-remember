# mcp/src/agents_remember/worktrees/integration

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees/integration` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `../../overview.md` |

## Governing Overview

[worktrees route (root overview)](../../overview.md)

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

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: created the `worktrees/integration`
  route — fourteen modules moved from `worktrees/` (flat). Verified at code commit e5cb139f.
