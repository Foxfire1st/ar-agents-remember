# mcp/src/agents_remember/worktrees/queue/closeout_projection_snapshot.py

## Governing Overview

[Closeout queue overview](overview.md)

## Purpose

Carries one immutable closeout-projection source observation and builds the disposable persisted
projection only when the observation is readable and completely classified.

## Code Commentary

### Logic

`ProjectionSourceSnapshot` freezes identity, classification, current members, and capture time.
`build` returns no projection for unreadable or incomplete source identity; otherwise it constructs
`CloseoutProjectionBuild` from only that snapshot. Prior projection rows are never an input.

### Conventions

- The source observation is a frozen dataclass.
- `None` means the source is unreadable or unclassified; it never invents a synthetic identity.

### Invariants And Boundaries

- A snapshot is immutable and describes one current census.
- Unreadable/unclassified identity cannot publish a replacement projection.
- This value object owns no source reads, lifecycle mutation, or queue selection.

### Todos

None.

## Evidence

### Docs References

No external source is required.

### Repo-Internal References

- The immutable snapshot gates projection construction on complete readable identity. [1]

### Cross-Repo References

None.
