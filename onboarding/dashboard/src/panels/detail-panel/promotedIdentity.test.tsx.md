# dashboard/src/panels/detail-panel/promotedIdentity.test.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The promoted task identity suite pins the native leaf’s real task ID/title/form rather than a generic lifecycle or master placeholder.

## Code Commentary

### Logic

seedPromotedLeaf publishes a native entry and its parent; both cases open the canonical qualified taskdoc key. Assertions retain the real identity/title and task form, separate step labels, Further-notes return and exact qualified parent navigation.

### Invariants And Boundaries

Current assertions check `doc-form=task`, the real promoted identity/title and separate step ID/title
cells. They open the Further-notes view and return before checking wrong-master fallbacks; the parent
navigation callback remains task-document scoped, not a generic lifecycle placeholder.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References


- The promoted-identity suite. [1]


### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
