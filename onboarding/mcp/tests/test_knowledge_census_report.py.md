# mcp/tests/test_knowledge_census_report.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R20: the Doc12 measures, the report and the `knowledge-census` command.** Registered in the
`unit-regression` lane; 6 collected cases.

## Code Commentary

### Logic

- The conforming example's measure strings, literally: "73.8% (31 of 42)" and "88.6% (31 of 35; U 5, P 2)".
- Zero denominators render "not applicable (zero denominator: 0 of 0 …)", never 100%.
- The cohort is the assessable claims and the latest assessment governs; `N = T + F + U + P`.
- The report on the fixture census: 42 claims, "routes: 6 of 6 migrated" against the named tree.
- The governing status is the latest entry across every census, with the tie-break, and spans censuses in
  each report.
- The command: `report` in text and JSON, an unknown census (exit 2), an invalid census file (exit 1);
  `inventory` refuses an unreadable baseline (exit 2, no directory) and writes a scoped census.

### Conventions

- `_measure` picks a measure by name.

### Invariants And Boundaries

- The measure strings are checked exactly, so a change to rendering is a visible test change.

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

The six cases.

- Measures of the conforming example. [1]
- Zero denominators. [2]
- The fixture report. [3]
- Governing status across censuses. [4]
- The two commands. [5]

### Cross-Repo References

No meaningful cross-repo references found: the cases build `tmp_path` repositories.

No cross-repo boundary is crossed by this file.
