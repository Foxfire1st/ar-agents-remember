# dashboard/src/panels/detail-panel/promotedIdentity.test.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The promoted-lifecycle identity suite split from `DetailPanel.test.tsx` by the
260731-EFA-L8 test split. Pins that a promoted leaf renders its real lifecycle/task
identity rather than a generic placeholder.

## Code Commentary

### Logic

Seeds the promoted lifecycle via `seedPromotedLeaf` and asserts the reader shows the
promoted document's title/identity.

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
