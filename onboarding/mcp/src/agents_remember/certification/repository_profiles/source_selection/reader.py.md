# mcp/src/agents_remember/certification/repository_profiles/source_selection/reader.py

## Governing Overview

[Source applicability overview](overview.md)

## Purpose

Reads one bounded frozen rail-source selection from a regular file and validates its declared decisions.

## Code Commentary

### Logic

`read_rail_source_selection` uses `lstat` to reject a nonregular path or a file larger than one million bytes. It reads at most the bound plus one byte and refuses oversize content, then parses `RailSourceSelection`, invoking its canonical path, matching, applicability and digest validators.

### Conventions

Consume a frozen report path within the caller’s retained-evidence policy; current Git observation remains a separate owner.

### Invariants And Boundaries

- This reader validates a retained decision; it does not recompute the Git census or authorize execution.
- Its physical checks are the explicit lstat and bounded read in this module; it does not claim an atomic descriptor identity or lock.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-owned selection contract.

No configured domain documentation applies.

### Repo-Internal References

- The reader bounds bytes and delegates self-verification to the closed selection model. [1]

### Cross-Repo References

No cross-repository implementation boundary is owned by this file.

No cross-repository reference is required.
