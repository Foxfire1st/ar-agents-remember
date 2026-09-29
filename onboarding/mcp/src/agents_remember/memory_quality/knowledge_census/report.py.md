# mcp/src/agents_remember/memory_quality/knowledge_census/report.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_census/report.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T09:30:11+02:00 |
| lastVerifiedCommitHash | `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695`|
| lastVerifiedCommitDate | 2026-09-29T09:57:49+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**The census report: measures with counts, slices, dispositions and route status (MIK-R20 rule 5).**
`census_reports(tree, census_id=None)` builds one `CensusReport` per census of a memory tree. It is the
data behind the `agents-remember knowledge-census report` command and, later, the reader's census view
(MIK-R29, leaf L29): `to_document` is the JSON form and `render` the text form.

## Code Commentary

### Logic

- Two censuses have two baselines and so two cohorts: their claims are never added together.
- Route status is the exception: each `RouteLine` shows the route's *governing* status, the latest entry
  across every census (`governing_status`), next to this census's own history for that route.
- A report's routes are the inventory's routes plus any route named by a claims or status file.
- `Slice` gives counts and the first four measures by route and by claim kind.
- `render` prints the baseline, the inventory counts (including unrouted sources), the claim counts, every
  measure, the dispositions, "routes: <migrated> of <n> migrated" and each route line and slice.
- An unknown `census_id` raises `KeyError` naming the known censuses.

### Conventions

- Every percentage is rendered through `Measure.render`, so counts always appear beside it.

### Invariants And Boundaries

- The report only reads; it never computes a score beyond the declared measures.

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

The report types and builders.

| Finding | Anchor | Source |
| --- | --- | --- |
| A slice by route or kind, with counts and measures. | `Slice` | mcp/src/agents_remember/memory_quality/knowledge_census/report.py:39-59 |
| A route line: governing status and this census's history. | `RouteLine` | mcp/src/agents_remember/memory_quality/knowledge_census/report.py:62-89 |
| The report's text and JSON forms. | `CensusReport` | mcp/src/agents_remember/memory_quality/knowledge_census/report.py:92-158 |
| One census's report; route status governed across the tree. | `census_report` | mcp/src/agents_remember/memory_quality/knowledge_census/report.py:192-213 |
| Every census, or one; an unknown ID refused. | `census_reports` | mcp/src/agents_remember/memory_quality/knowledge_census/report.py:216-225 |
| The report on the fixture census matches the conforming example. | `test_the_report_on_the_fixture_census_matches_the_conforming_example` | mcp/tests/test_knowledge_census_report.py:98-124 |

## Cross-Repo References

No meaningful cross-repo references found: the package reads one memory tree's bytes, handed in by the caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): created this card for the new file MIK-R20 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
