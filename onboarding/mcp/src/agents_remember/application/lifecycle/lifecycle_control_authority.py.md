# mcp/src/agents_remember/application/lifecycle/lifecycle_control_authority.py

## Governing Overview

[governing route overview](../overview.md)

## Purpose

Resolve caller-specific authority for completed lifecycle dispositions.

## Code Commentary

### Logic

The public surface is `LifecycleCallerError`, `resolve_lifecycle_caller`, `completed_disposition_owner`, `completed_disposition_authorized`, `require_completed_disposition_authority`. This application boundary exposes a closed public result and delegates durable mutation to its owning domain seam. Expected configured-contract, location, or legacy failures are translated through typed decisions; callers do not enumerate lower-level exception families or invent alternate authority.

Completed retire/supersede authority comes from live topology: `orchestrator` at the enclosing
sprint, or `architect` at a standalone master. The caller must match both role and exact document;
a leaf worker is not an authorized disposition owner. Hosted seat identity wins only when an
explicit declaration agrees with it; an unbound or conflicting hosted identity refuses.

cit:([`completed_disposition_owner`], mcp/src/agents_remember/application/lifecycle/lifecycle_control_authority.py:54-65)
cit:([`require_completed_disposition_authority`], mcp/src/agents_remember/application/lifecycle/lifecycle_control_authority.py:81-101)
cit:([`resolve_lifecycle_caller`], mcp/src/agents_remember/application/lifecycle/lifecycle_control_authority.py:23-51)

### Conventions

The file exposes typed values or one narrow operation boundary. Callers consume those values directly rather than reconstructing lower-level state from strings, mutable task documents, or queue projection.

### Invariants And Boundaries

- Preserve the module's single ownership seam; do not add a fallback reader or duplicate authority.
- Expected refusal states remain typed and bounded, while unexpected programming faults remain loud.
- Durable lifecycle facts live in the canonical root journal; scheduling projections may only consume them.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

### Repo-Internal References

The source file itself is the current evidence for this file-specific contract.

- The module defines `LifecycleCallerError`; `resolve_lifecycle_caller`; `completed_disposition_owner` as its public seam. [1]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.
