# dashboard/src/panels/review/intentMarkerScope.test.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The marker scope's reads and inventory rule (2 cases; review R1 F4 N11, F5, and the review R2 gap).** The real scope
through `renderHook`, with `fetch` the only stand-in, answered with the real `notes.py` classification of the scratch
leaf (`markerReturn.file.captured.json`).

## Code Commentary

### Logic

- **Case 1.** An unlisted path is never asked about (`classify` returns `null`, no request); a listed one is asked once,
  with `file=` and `comparison=`; a second `classify` shares the pending answer, and `peek` holds it once settled.
- **Case 2.** `markerInventory` counts an inventory as partial when it is `partial` or not `measured` at all, and lists
  its paths.

### Conventions

- `renderHook` over `useIntentMarkerScope` with recording moves.

### Invariants And Boundaries

- Pins the changed-path gate (mutation N11) and the partial rule (R2-7).

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- One read per listed path per surface; none for an unlisted path. [1]
- A partial or unmeasured inventory is partial. [2]
- The scope under test. [3]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
