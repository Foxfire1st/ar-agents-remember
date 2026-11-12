# mcp/src/agents_remember/cli/knowledge_census.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The census design authority is the coordination-root notes Doc12 (the
migration census and its measures) and Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`)
and the requirement packet `MIK-R20@v2` of task `260928_maintained-invariant-knowledge`; they live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The arguments and the two actions.

- The two actions and their flags. [1]
- Inventory: exit 2 on an unreadable baseline, 1 on a refused write. [2]
- Report: exit 2 on an unreadable input, 1 on an invalid census file. [3]
- The report and inventory commands end to end. [4]

### Cross-Repo References

No meaningful cross-repo references found beyond the code repository named by `--code`, which is only read.

No cross-repo boundary is crossed by this file.
