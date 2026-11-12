# dashboard/src/panels/detail-panel/viewedLeaf.test.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The viewed-leaf reporting suite split from `DetailPanel.test.tsx` by the
260731-EFA-L8 test split. Pins the L5 fix-1 viewed-leaf reporting behavior of the
detail panel.

## Code Commentary

### Logic

Both drilled and directly opened leaf cases use canonical taskdoc: repository-qualified entry keys. The callback reports the exact repository-qualified taskDocumentRef and the compatibility leaf presentation key; it never reports a session/lifecycle id. This is callback/request identity coverage, not real host execution.

### Invariants And Boundaries

The viewed-task callback boundary remains, but canonical entry selection replaces the prior absolute docPath selector. Qualified document identity and compatibility leaf presentation are asserted separately.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References


- The viewed-leaf reporting suite. [1]


### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
