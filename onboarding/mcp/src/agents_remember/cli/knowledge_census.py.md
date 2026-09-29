# mcp/src/agents_remember/cli/knowledge_census.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/knowledge_census.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T09:30:11+02:00 |
| lastVerifiedCommitHash | `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695`|
| lastVerifiedCommitDate | 2026-09-29T09:57:49+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

**CLI adapter: `agents-remember knowledge-census inventory` and `… report` (MIK-R20 rules 1 and 5).**
`inventory` pins a baseline (`--code-commit` of `--code`, `--memory-commit` of `MEMORY_ROOT`, both `HEAD`
by default, optional repeated `--scope`) and writes the new census's `baseline.json` and `inventory.json`
into the converted memory working tree through `CensusWriter.create`. `report` reads the censuses of
`MEMORY_ROOT` (its working tree, or `--revision`) and prints each census's report, as text or `--json`.

## Code Commentary

### Logic

- `_run_inventory`: an unreadable baseline (`CensusBaselineError`, `OSError`, `ValueError`) exits 2 and
  writes nothing; a refused write (`CensusWriteError`, including an unconverted tree) exits 1; success
  prints the commits and the row and route counts.
- `_run_report`: an unreadable tree exits 2; an unknown `--census` exits 2; census problems are printed as
  "invalid census file: …" after whatever could be read, and exit 1; otherwise exit 0. With no census it
  prints "<label>: no census under knowledge/census/".

### Conventions

- Registered in `cli/__main__.py` as `knowledge-census`, the declarative `add_arguments` + `run` pair.

### Invariants And Boundaries

- Claims, assessments and statuses are not on the CLI: they are written through the `CensusWriter` Python API.
- `report` only reads.

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

The arguments and the two actions.

| Finding | Anchor | Source |
| --- | --- | --- |
| The two actions and their flags. | `add_arguments` | mcp/src/agents_remember/cli/knowledge_census.py:42-64 |
| Inventory: exit 2 on an unreadable baseline, 1 on a refused write. | `_run_inventory` | mcp/src/agents_remember/cli/knowledge_census.py:71-93 |
| Report: exit 2 on an unreadable input, 1 on an invalid census file. | `_run_report` | mcp/src/agents_remember/cli/knowledge_census.py:111-133 |
| The report and inventory commands end to end. | `test_the_report_and_inventory_commands` | mcp/tests/test_knowledge_census_report.py:174-203 |

## Cross-Repo References

No meaningful cross-repo references found beyond the code repository named by `--code`, which is only read.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): created this card for the new file MIK-R20 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
