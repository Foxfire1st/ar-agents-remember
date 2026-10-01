# mcp/src/agents_remember/worktrees/modules/startup/start_provider_preflight.py

## Governing Overview

[governing route overview](../overview.md)

## Purpose

Computes provider enablement and settings-readability state before worktree start exposes provider setup.

## Code Commentary

### Logic

The public surface is `provider_enablement_state`. Provider enablement is a start-time projection only. An unreadable provider configuration becomes bounded public evidence; provider availability neither locates the lifecycle journal nor changes enclosure authority.

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

- The module defines `provider_enablement_state` as its public seam. [1]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.
