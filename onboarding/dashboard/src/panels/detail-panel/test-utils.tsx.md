# dashboard/src/panels/detail-panel/test-utils.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

Shared typed TaskEntry/TaskSummary fixtures for split DetailPanel suites, with explicit membership/counts, qualified body answers and ancillary refusal/counter stubs; not native producer acceptance.


## 260831-CCR-L23 Requirement-Listing Stub

`stubNotes` gained an optional third argument: the registered requirement
listing (rows shaped `{ name, path, address, size, sha256 }`). Its fetch stub
now answers `/api/requirements/list` with
`{ repo, master, document, registered, requirements }` so detail-panel suites
can exercise the requirement-links provider without a live server. Existing notes and
task-document branches are unchanged.

## Code Commentary

TaskSummary construction supplies required seats and other neutral defaults explicitly; native entries carry identity, membership and counts separately.

### Logic

seedTaskEntries and taskTree seed native entry maps with explicit parent/children/counts. seedSeries/ordering/promoted fixture scenarios use that same grammar, not lifecycle or SeriesNode builders. stubCounters remains a deterministic ancillary HTTP stub.
`seedProjection`, `seedPromotedLeaf` and `seedSeriesOrdering` retain their projection/scenario roles; the former gallery `seed(name)` helper remains removed.


**`stubCounters` takes one optional argument, and it is what lets a test choose which answer the Intent review control reads.** Since `260921-ICR-L47` it is `stubCounters(reviewSummary?: unknown)` and answers `/api/review/intent/summary` (previously `reviewEntry` answering `/api/review/intent/entries`, which the entry no longer reads) with whatever the caller passes — counts, partial counts, or an unavailable refusal — and keeps its previous behaviour when the argument is omitted (the route falls through to the counters body, which is what a caller that does not exercise the entry wants). The three answers are deliberately *different* answers that the bar must treat the same way, which is why the argument is untyped at the call site: the stub's job is to reproduce the wire, not to constrain it.

`stubNotes` dispatches an explicit first-matching route table. D229 factors response construction,
query parsing, task-body selection, folder pagination, reference resolution and empty report payloads
into named helpers, avoiding one oversized fetch callback. `noteResolutions` reads the reference list
from the POST body; this is a test double, not a live read. `stubCounters` gives the reports route a
well-shaped empty reports object instead of its generic counters payload.

### Conventions

Fixtures are checked against the generated mirror but their values are fabricated. Body stubs resolve qualified repository/path addresses from seeded entries; shape validity does not establish producer-value provenance.

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



- The retained shared fixture builders include seedProjection, seedPromotedLeaf and stubCounters; the removed gallery seed helper is not a current owner. [1]



### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.

## 260821-CLIVE Projection Fixture Alignment

`TaskSummary.discardedCount` and `discardedSubTasks` are optional; the shared summary builder does not install discarded-audit defaults. Cases that exercise discarded history supply it explicitly, separately from native child counts. No seriesNode builder remains.


- The fetch route table delegates to named payload helpers; task body and empty recorded-report payloads have dedicated branches. [2]


Anchor: `seedProjection` `seedPromotedLeaf` `stubCounters` 


Anchor: `seedProjection` `seedPromotedLeaf` `stubCounters` 

- Retired at the fifth freeze d59c3493: dashboard/src/panels/detail-panel/test-utils.tsx::seedProjection - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; dashboard/src/panels/detail-panel/test-utils.tsx:None-None - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.
