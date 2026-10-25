# dashboard/src/panels/lifecycle-list/admission.test.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The row-admission suite split from `LifecycleList.test.tsx` by the 260731-EFA-L8
test split (22-name set reconciled item-for-item). Pins which task labels admit rows
into the Operations list.

## Code Commentary

### Logic

Served master/leaf/unauthored planning entries are visible and counted without worktrees. Selecting the addressable child emits its qualified key. Retired enclosure/lifecycle admission is not tested; addressless inert rows belong to taskEntryPage.

### Invariants And Boundaries

Shared list cleanup remains. The row-admission contract now covers served tasks without worktrees, not the historical enclosure-only admission policy.

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
