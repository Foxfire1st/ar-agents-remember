# mcp/src/agents_remember/memory_quality/style/finding.py

## Governing Overview

[overview](../overview.md)

## Purpose

Shared finding record for memory-layer style checks.

## Code Commentary

### Logic

Module-level surface:

- `QualityFinding` (class, lines 14-43) — The shared record. `report_only` keeps a finding counted and rendered but out of `ok`; `closeout_owned` marks a row no curator edit can discharge (an anchor that resolves more than once in the cited file), so the stamp decision is closeout's — the flag travels with the finding so the routing is one structural fact rather than a message match at the reporting layer, and `to_dict` publishes it as `closeoutOwned` only when set.
- `check_result` (function, lines 46-68) — Package findings into the uniform runner result ``memory_quality.check`` expects.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `QualityFinding` (lines 14-43). [1]
- Defines the function `check_result` (lines 46-68) — Package findings into the uniform runner result ``memory_quality.check`` expects.. [2]
