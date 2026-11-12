# mcp/src/agents_remember/memory_quality/knowledge_census/report.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The census design authority is the coordination-root notes Doc12 (the
migration census and its measures) and Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`)
and the requirement packet `MIK-R20@v2` of task `260928_maintained-invariant-knowledge`; they live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The report types and builders.

- A slice by route or kind, with counts and measures. [1]
- A route line: governing status and this census's history. [2]
- The report's text and JSON forms. [3]
- One census's report; route status governed across the tree. [4]
- Every census, or one; an unknown ID refused. [5]
- The report on the fixture census matches the conforming example. [6]

### Cross-Repo References

No meaningful cross-repo references found: the package reads one memory tree's bytes, handed in by the caller.

No cross-repo boundary is crossed by this file.
