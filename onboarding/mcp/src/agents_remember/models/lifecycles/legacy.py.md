# mcp/src/agents_remember/models/lifecycles/legacy.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Bounded audit vocabulary for the one supported schema-1 closeout incident.

## Code Commentary

### Logic

The bounded proof preserves the observed legacy code output, original approval and code
message, and the unfinished memory-content message. It has no `ledgerCommitMessage`; migration
can retain unfinished memory intent without reintroducing a ledger writer or cache authority.

The public surface is `LegacyCloseoutMigrationProof`. This module is strict evidence vocabulary, not an I/O or scheduling owner. Its models keep generation, publication, enclosure, termination, legacy, and direct-landing facts explicit so partial or contradictory state fails validation instead of being inferred from queue rows or task prose.

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

No configured external domain-documentation source applies.

### Repo-Internal References

The source file itself is the current evidence for this file-specific contract.

- The bounded legacy proof retains unfinished memory intent after verified code without a ledger message. [1]
- The module defines `LegacyCloseoutMigrationProof` as its public seam. [2]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.


No separate external implementation source applies to this file.
