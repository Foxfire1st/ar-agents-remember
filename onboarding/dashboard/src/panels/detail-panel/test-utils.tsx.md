# dashboard/src/panels/detail-panel/test-utils.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

Shared fixture builders for the split DetailPanel test files, extracted from
`DetailPanel.test.tsx` by the 260731-EFA-L8 split. Seeds task documents, series,
enclosures, projections, promoted-lifecycle scenarios, and counter stubs.


## 260831-CCR-L23 Requirement-Listing Stub

`stubNotes` gained an optional third argument: the registered requirement
listing (rows shaped `{ name, path, address, size, sha256 }`). Its fetch stub
now answers `/api/requirements/list` with
`{ repo, master, document, registered, requirements }` so detail-panel suites
can exercise the requirement-links provider without a live server. Existing notes and
task-document branches are unchanged.

## Code Commentary

Since 260815-DAG-L14 the `taskDoc` fixture factory defaults `seats: []` (the new required `TaskDocNode` field).

### Logic

`seed` / `taskDoc` / `seriesNode` / `enclosure` build minimal typed nodes;
`seedProjection` assembles a workspace projection; `seedPromotedLeaf` and
`seedSeriesOrdering` prepare the promoted-identity and ordering scenarios;
`stubCounters` installs deterministic counter hooks.


**`stubCounters` takes one optional argument, and it is what lets a test choose which answer the Intent review control reads.** Since `260921-ICR-L47` it is `stubCounters(reviewSummary?: unknown)` and answers `/api/review/intent/summary` (previously `reviewEntry` answering `/api/review/intent/entries`, which the entry no longer reads) with whatever the caller passes — counts, partial counts, or an unavailable refusal — and keeps its previous behaviour when the argument is omitted (the route falls through to the counters body, which is what a caller that does not exercise the entry wants). The three answers are deliberately *different* answers that the bar must treat the same way, which is why the argument is untyped at the call site: the stub's job is to reproduce the wire, not to constrain it.

### Conventions

Fixtures are typed through the projection mirror so a fixture that compiles is a shape
the mirror can produce. Task-document fixture paths use `/tasks/<repository>/...`, so tests exercise
the same repository-qualified document topology as production selection and projection code.

### Invariants And Boundaries

Test-only module; never imported by production code.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The shared fixture builders. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.

## 260821-CLIVE Projection Fixture Alignment

No helper behavior changed. `seriesNode()` now defaults the required `discardedCount: 0` and
`discardedSubTasks: []` fields so every detail-panel fixture remains a valid projected series. The
existing required `seats` and repository-qualified topology defaults remain intact.
