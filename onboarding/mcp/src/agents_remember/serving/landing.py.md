# mcp/src/agents_remember/serving/landing.py

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Marks all non-terminated occupants of selected roles on one canonical task document as landed while
leaving their hosted transcript/process inspectable.

## Code Commentary

### Logic

`land_seats_for_task` scans catalog rows, matches exact task-document identity and role, skips
terminated occupants, and delegates the landing transition for each match.

### Conventions

Callers supply the real task document resolved from governed closeout/finalization context.

### Invariants And Boundaries

- Landing is document-and-role scoped, never leaf-key parsed.
- Landed seats remain inspectable and are distinct from explicit retirement.
- Unrelated roles on the same document remain unchanged.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Landing matches canonical document and explicit role set. [1]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
