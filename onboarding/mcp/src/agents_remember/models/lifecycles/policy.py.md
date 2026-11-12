# mcp/src/agents_remember/models/lifecycles/policy.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Durable lifecycle gate-policy snapshot vocabulary.

## Code Commentary

### Logic

The public surface is `GatePolicyRuleSnapshot`. This module is strict evidence vocabulary, not an I/O or scheduling owner. Its models keep generation, publication, enclosure, termination, legacy, and direct-landing facts explicit so partial or contradictory state fails validation instead of being inferred from queue rows or task prose.

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

- The module defines `GatePolicyRuleSnapshot` as its public seam. [1]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.
