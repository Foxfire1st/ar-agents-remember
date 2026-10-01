# mcp/src/agents_remember/observer/projection_closeout.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Define observer nodes for closeout-projection problems and discarded-task history.

## Code Commentary

### Logic

The models project bounded non-admitting queue repair evidence and the durable proof/audit fields retained after an unstarted subtask is discarded.

### Invariants And Boundaries

- Observer nodes are read-only projections.
- Discarded task history remains visible after the live child sources are removed.
- Projected queue problems do not become lifecycle authority.

### Todos

None recorded.

## Evidence

### Docs References

No configured domain-documentation source applies to this repository-internal route.

### Repo-Internal References

- Projection problem nodes expose bounded repair evidence. [1]
- Discard proof and audit nodes retain the historical task truth. [2]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.
