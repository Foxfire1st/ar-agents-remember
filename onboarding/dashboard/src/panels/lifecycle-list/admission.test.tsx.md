# dashboard/src/panels/lifecycle-list/admission.test.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The row-admission suite split from `LifecycleList.test.tsx` by the 260731-EFA-L8
test split (22-name set reconciled item-for-item). Pins which task labels admit rows
into the Operations list.

## Code Commentary

### Logic

Seeds projections with mixed lifecycle/document kinds and asserts admitted identities, exact enclosure joins, physical-worktree visibility and one row per enclosure. The compact title/id split and full hover replace former inline metadata assertions; these presentation changes do not relax admission or typed document selection.

### Invariants And Boundaries

Assertions preserved from the monolithic suite; shared cleanup from
`test-utils.tsx`.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The row-admission suite. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
