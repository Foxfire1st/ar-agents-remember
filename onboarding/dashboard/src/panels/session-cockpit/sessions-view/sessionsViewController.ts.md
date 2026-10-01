# dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts

## Governing Overview

[panels/session-cockpit overview](../overview.md)

## Purpose

The controller layer of the Sessions view, extracted from `SessionsView.tsx` by the
260731-EFA-L8 split. Defines `SessionsViewProps` and composes the refs, state,
selectors, derived values, focus/library handlers, and inspector actions the body
renders.

## Code Commentary

### Logic

`useSessionsViewRefs` builds the shared `SessionsViewRefs` (scroll/measurement and
element refs); `useSessionsViewState` derives the live view state;
`useSessionsViewSelectors` pulls store data from props; `useSessionsViewDerived`
computes derived rows; `useFocusAndLibraryHandlers` owns smart focus and the chats
library; the exported `SessionsViewProps` is re-exported by the canonical entry.

### Conventions

Controller code stays in this module; JSX composition lives in `sessionsViewBody.tsx`.

### Invariants And Boundaries

The controller never renders; it only derives state and handlers.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The controller entry points. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
