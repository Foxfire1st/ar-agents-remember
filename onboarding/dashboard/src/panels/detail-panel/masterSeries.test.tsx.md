# dashboard/src/panels/detail-panel/masterSeries.test.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The master/series navigation suite split from `DetailPanel.test.tsx` by the
260731-EFA-L8 test split. Pins the 6g master overview, sub-task index, drill-in, and
cross-series navigation behavior of the detail reader.

## Code Commentary

The suite proves the sprint → master → leaf click path: a typed `masterRef` row is a navigation button with separate ID/name cells, opens the commanded master document, then drills to its leaf. An unprojected target retains its visible row and no navigation target.

### Logic

Seeds a master with sub-task refs and a linked series; asserts the index rows, the
in-panel drill-in, and the `linkedLifecycleId` cross-series jump.

### Invariants And Boundaries

Uses the shared `test-utils.tsx` seeds (`seedSeriesOrdering`, `seedTaskDocuments`).
Current skeleton assertions require one index, separate step/substep cells, skip/done state text,
Now-row authoritative progress and Markdown inside the Further-notes views; they adapt the former
monolithic display assertions without changing qualified drill-in/cross-series ownership.

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

The suite proves that a master exposes a counted gone-history link separately from its live
sub-task index; opening it shows the discarded audit row, and Back returns to the page. That row
retains reason, timestamp and proof fingerprint, while live progress remains `0/1`: discarding an
unstarted task is audited removal, never synthetic completion.
The inline proof also carries the exact generated contract's required `childJson` and
`childMarkdown` missing-state witnesses. Those opaque records establish fixture conformance; the UI
continues to render the proof fingerprint rather than interpreting or exposing their contents.
Existing sprint-to-master-to-leaf and cross-series navigation coverage remains in force.
