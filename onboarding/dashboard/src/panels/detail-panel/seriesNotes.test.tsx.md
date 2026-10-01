# dashboard/src/panels/detail-panel/seriesNotes.test.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The series-notes behavior suite split from `DetailPanel.test.tsx` by the
260731-EFA-L8 test split. Pins the L9 series-notes rendering in the detail reader.


## 260831-CCR-L23 Kind-Tagged Open Payload

The series-notes click expectation now asserts the discriminated artifact target:
`onOpenNotes` fires `{ kind: "notes", repo, master, path }`.

## Code Commentary

### Logic

Seeds a series with notes and asserts the notes surface renders the expected content
and state.

### Invariants And Boundaries

Assertions preserved from the monolithic suite.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The series-notes suite. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
