# mcp/src/agents_remember/memory_quality/knowledge_census/__init__.py

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**The migration census over text files (MIK-R20): the package front.** It re-exports the reading
(`files`), the integrity checks the validator registers (`checks`), the Doc12 measures (`measures`) and
the per-census report (`report`). The package reads a memory tree's bytes only, so it depends on nothing
above `models`; the Git-reading inventory and the writer are in `memory/knowledge_census`.

## Code Commentary

### Logic

- The module map is the docstring; `__all__` lists `CENSUS_RULES`, `CensusFinding`, `check_censuses`,
  `record_ids_in`, the path helpers and `read_censuses`, `Counts`, `Measure`, `compute_measures`,
  `CensusReport`, `census_report` and `census_reports`.

### Conventions

- A sibling of `knowledge_validator/` under `memory_quality/`, governed by the `memory_quality` route overview; it has no overview of its own (the L22/L23 precedent for sibling packages).

### Invariants And Boundaries

- Nothing here writes. The validator (`knowledge_validator/rules_census.py`), the writer and the CLI all consume these modules.

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

No meaningful cross-repo references found: the package reads one memory tree's bytes, handed in by the caller.

No cross-repo boundary is crossed by this file.
