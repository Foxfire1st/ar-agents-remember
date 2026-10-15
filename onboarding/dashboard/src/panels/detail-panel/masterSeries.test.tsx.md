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
Now-row projected major-step progress (`6/7`) with seven step marks and the opened task reader's `6 of 7 done`; the former `46/49` parent-plus-child summary is absent. Markdown remains inside Further-notes views. These are seeded DOM assertions, not backend count derivation or an executed navigation result.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References


- Seeded navigation/static-target and discarded-history assertions remain; projected major progress is 6/7 with seven marks and 6 of7 done, not executed evidence. [1]



### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.

## 260821-CLIVE Discarded-Before-Start Proof

The discarded-history case asserts a counted gone-history link separate from the live sub-task index; opening it exposes the discarded row's number/name, reason and proof fingerprint, and Back restores the live row. The fixture supplies `discardedAt`, but this case does not assert its rendered timestamp or live `0/1` progress. The historical lesson remains: discarding unstarted work is audited removal, not synthetic completion.
The inline proof also carries the exact generated contract's required `childJson` and
`childMarkdown` missing-state witnesses. Those opaque records establish fixture conformance; the UI
continues to render the proof fingerprint rather than interpreting or exposing their contents.
Existing sprint-to-master-to-leaf and cross-series navigation coverage remains in force.
