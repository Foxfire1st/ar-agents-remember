# mcp/src/agents_remember/memory/knowledge_census/__init__.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The census's Git-reading inventory and its writer (MIK-R20): the package front.** It re-exports
`take_inventory`, `build_inventory`, `governing_route`, `onboarding_routes`, `BaselineSide` and
`CensusBaselineError` from `inventory`, and `CensusWriter` and `CensusWriteError` from `writer`. Reading,
checks, measures and the report are in `memory_quality/knowledge_census`.

## Code Commentary

### Logic

- The module map is the docstring; `__all__` is the public surface.

### Conventions

- A sibling of `knowledge_index/` under `memory/`, governed by the `memory` route overview; it has no overview of its own (the L22/L23 precedent for sibling packages).

### Invariants And Boundaries

- `memory` ranks above `memory_quality`, so this package may import the census checks; the reverse import is forbidden by layering.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The census design authority is the coordination-root notes Doc12 (the
migration census and its measures) and Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`)
and the requirement packet `MIK-R20@v2` of task `260928_maintained-invariant-knowledge`; they live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The re-exported surface.

- The package's public names. [1]

### Cross-Repo References

No meaningful cross-repo references found: the package front only re-exports.

No cross-repo boundary is crossed by this file.
