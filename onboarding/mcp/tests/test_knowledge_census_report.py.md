# mcp/tests/test_knowledge_census_report.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_census_report.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T09:30:11+02:00 |
| lastVerifiedCommitHash | `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695`|
| lastVerifiedCommitDate | 2026-09-29T09:57:49+02:00|
| governingOverview | `overview.md` |

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

The six cases.

| Finding | Anchor | Source |
| --- | --- | --- |
| Measures of the conforming example. | `test_the_measures_of_the_conforming_example_carry_their_counts` | mcp/tests/test_knowledge_census_report.py:42-55 |
| Zero denominators. | `test_a_zero_denominator_is_not_applicable_never_a_perfect_score` | mcp/tests/test_knowledge_census_report.py:58-72 |
| The fixture report. | `test_the_report_on_the_fixture_census_matches_the_conforming_example` | mcp/tests/test_knowledge_census_report.py:98-124 |
| Governing status across censuses. | `test_the_governing_status_is_the_latest_entry_across_every_census` | mcp/tests/test_knowledge_census_report.py:127-167 |
| The two commands. | `test_the_report_and_inventory_commands` | mcp/tests/test_knowledge_census_report.py:174-203 |

## Cross-Repo References

No meaningful cross-repo references found: the cases build `tmp_path` repositories.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): created this card for the new file MIK-R20 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
