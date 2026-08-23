# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:27+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[integration overview](../overview.md)

## Purpose

Builds the pure public projection of one retained lifecycle-operation generation from journal evidence plus explicitly observed authority context.

## Code Commentary

### Logic

`operation_projection` combines the record with optional contract, caller, time, and door evidence; derives integration, door, legal-control, recovery, migration, and worker-termination views; and emits elapsed time, current generation, cancellability, and an opaque `legalControls` list. Operation-specific recovery surfaces direct landing and initial-door or ledger contradictions without rewriting the record.

### Conventions

Projection is read-only. The local import of control projection avoids a module cycle, and legacy-migrated records deliberately suppress the current report path.

### Invariants And Boundaries

- Projection never becomes lifecycle evidence authority.
- Public result payloads must remain mappings.
- Legal controls derive from current journal and admitted authority, not queue lifecycle rows.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this internal projection.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Projection context carries time, completed-disposition permission, caller, and door evidence. | L44-L51 | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py` |
| The public projection derives legal controls and generation without mutating journal state. | L54-L132 | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py` |
| Worker, legacy, door, integration, closeout-ledger, and direct-landing recovery surfaces are derived from exact evidence. | L135-L227 | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_projection.py` |

## Cross-Repo References

No cross-repository boundary is owned here.

## Update History

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: created the missing strict sidecar and verified it at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.
