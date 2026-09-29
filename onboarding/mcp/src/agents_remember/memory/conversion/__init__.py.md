# mcp/src/agents_remember/memory/conversion/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/conversion/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T14:21:42+02:00 |
| lastVerifiedCommitHash | `8b0254263c6998b1d4814b2e97c1bd231d39350f`|
| lastVerifiedCommitDate | 2026-09-29T15:00:35+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The package overview of the conversion into the text knowledge format, and of the boundary crossing
(MIK-R24).** It defines no construct: its docstring maps the package's modules to the packet's rules.
Nothing in the installed runtime imports this package before MIK-R37. This leaf wires it only into the
new `knowledge-convert` command, the validator's commit route (the converted base) and the managed sync's
crossing branch. The last two are inert while no memory tree is converted.

## Code Commentary

### Logic

- `convert` is the deterministic conversion (rules 1–4 and 6), driven by `agents-remember knowledge-convert`.
  It uses `cards` (the Markdown half), `citations` (references), `legacy_db` (the read-only legacy
  database reader and the export), `code_objects` (the code objects it resolves in) and `inputs`
  (reading and writing memory trees).
- `base` is the converted base of a comparison (rule 7).
- `crossing` and `crossing_sync` are the crossing sync's structural merge (rule 8), bound into the managed
  sync through `crossing_port`.

### Conventions

- **This package has no route overview of its own.** It is governed by `memory/overview.md`, as its
  sibling packages `memory/knowledge/`, `memory/migration/`, `memory/knowledge_census/` and
  `memory/knowledge_index/` are.

### Invariants And Boundaries

- **Conversion and crossing are separate routes (architect ruling, 2026-09-29).** A repository without
  an official line, or whose official line is unconverted, converts by running the conversion command on
  that line and committing it through its normal route (for this master's line, MIK-R37). The crossing
  sync is only for lines that descend from a converted official line.
- The package commits nothing to a real memory line (packet Exclusions).

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R24@v1` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`24_conversion-and-boundary-crossing.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The package map.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module map this docstring gives. | "the deterministic conversion" | mcp/src/agents_remember/memory/conversion/__init__.py:1-10 |

## Cross-Repo References

No meaningful cross-repo references found: the file reads and writes only the memory and code repositories its caller names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): created this card for the new file MIK-R24 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
