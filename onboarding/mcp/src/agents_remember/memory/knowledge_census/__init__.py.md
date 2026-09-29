# mcp/src/agents_remember/memory/knowledge_census/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge_census/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T09:30:11+02:00 |
| lastVerifiedCommitHash | `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695`|
| lastVerifiedCommitDate | 2026-09-29T09:57:49+02:00|
| governingOverview | `../overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The census design authority is the coordination-root notes Doc12 (the
migration census and its measures) and Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`)
and the requirement packet `MIK-R20@v2` of task `260928_maintained-invariant-knowledge`; they live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The re-exported surface.

| Finding | Anchor | Source |
| --- | --- | --- |
| The package's public names. | `__all__` | mcp/src/agents_remember/memory/knowledge_census/__init__.py:23-32 |

## Cross-Repo References

No meaningful cross-repo references found: the package front only re-exports.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): created this card for the new file MIK-R20 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
