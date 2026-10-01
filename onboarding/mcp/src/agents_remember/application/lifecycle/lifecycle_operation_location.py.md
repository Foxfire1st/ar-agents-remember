# mcp/src/agents_remember/application/lifecycle/lifecycle_operation_location.py

## Governing Overview

[governing route overview](../overview.md)

## Purpose

Configured application authority for exact task-owned operation journal locations.

## Code Commentary

### Logic

The public surface is `LifecycleOperationPublicAddress`, `LocationDecisionPayload`, `ContractReadOperationObservation`, `configured_lifecycle_operation_location`, `location_decision_payload`, `unreadable_status_operations`. This application boundary exposes a closed public result and delegates durable mutation to its owning domain seam. Expected configured-contract, location, or legacy failures are translated through typed decisions; callers do not enumerate lower-level exception families or invent alternate authority.

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

- The module defines `LifecycleOperationPublicAddress`; `LocationDecisionPayload`; `ContractReadOperationObservation` as its public seam. [1]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.
