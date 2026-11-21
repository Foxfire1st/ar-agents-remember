# mcp/src/agents_remember/models/lifecycles/termination.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Typed no-output cancellation evidence.

## Code Commentary

### Logic

`LifecycleCancellationEvidence` binds the operation kind and generation, proof timestamp, nonempty expected facts and exact observed equality. The shape retains `workerExitProven` for compatibility. The direct no-output proof sets that marker after checking the protected Git state.

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


- Cancellation evidence requires exact expected and observed facts. Direct no-output proof supplies the retained exit marker without a worker observation. [1]


### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.
