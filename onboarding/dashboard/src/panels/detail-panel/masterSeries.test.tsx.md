# dashboard/src/panels/detail-panel/masterSeries.test.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The master/series navigation suite split from `DetailPanel.test.tsx` by the
260731-EFA-L8 test split. Pins the 6g master overview, sub-task index, drill-in, and
cross-series navigation behavior of the detail reader.

## Code Commentary

Since 260815-DAG-L14 the suite proves the sprint → master → leaf click path: a typed `masterRef` row renders as the `⇒` master link, opens the commanded master document, then drills to its leaf; an unprojected `masterRef` target degrades to the static index row.

### Logic

Seeds a master with sub-task refs and a linked series; asserts the index rows, the
in-panel drill-in, and the `linkedLifecycleId` cross-series jump.

### Invariants And Boundaries

Uses the shared `test-utils.tsx` seeds (`seedSeriesOrdering`, `seedTaskDocuments`);
assertions preserved from the monolithic suite.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The master-series navigation suite. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.

## 260821-CLIVE Discarded-Before-Start Proof

The suite now proves that a master renders `Discarded before start (1)` separately from its live
sub-task index. The discarded row retains its reason, timestamp, and proof fingerprint, while live
progress remains `0/1`: discarding an unstarted task is audited removal, never synthetic completion.
The inline proof also carries the exact generated contract's required `childJson` and
`childMarkdown` missing-state witnesses. Those opaque records establish fixture conformance; the UI
continues to render the proof fingerprint rather than interpreting or exposing their contents.
Existing sprint-to-master-to-leaf and cross-series navigation coverage remains in force.
