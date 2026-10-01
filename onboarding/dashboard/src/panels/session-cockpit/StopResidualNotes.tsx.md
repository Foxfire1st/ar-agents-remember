# dashboard/src/panels/session-cockpit/StopResidualNotes.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

`StopResidualNotes` is a presentational component for informational `controlStopDetail` and
`retireControlStopError` residuals. The current `SessionsView` deliberately leaves it unmounted, so
the lifecycle notice store retains residuals for Inspector/debug surfaces rather than producing a
stacked stage notice. The terminate and retire paths still preserve facts about successfully
terminated/retired sessions, use informational copy, and never silently discard the residual.

## Code Commentary

### Logic

- **Component behavior** cit:([`StopResidualNotes`], dashboard/src/panels/session-cockpit/StopResidualNotes.tsx:41-72): reads `residuals` from
  `useLifecycleNotices`, renders nothing at zero residuals, and maps each retained residual to its
  informational copy and dismissal control. This component is not mounted by the current stage.
- **Newest-first retention** cit:(["residuals: [residual"], dashboard/src/data/sessionLifecycle.ts:75-75): `recordResidual` prepends each retained residual.
- **Dismissal** cit:(["state.residuals.filter", "entry.sessionId === sessionId && entry.at === at"], dashboard/src/data/sessionLifecycle.ts:78-79): `dismissResidual` removes the matching session/timestamp entry.
- **Focus-independent retire sweep and deduplication** cit:(["for (const session of sessions)", "if ( typeof detail !== \"string\" || !detail || state.sweptRetire[session.id] ) continue;", "sweptRetire[session.id] = true"], dashboard/src/data/sessionLifecycle.ts:87-87; dashboard/src/data/sessionLifecycle.ts:89-94; dashboard/src/data/sessionLifecycle.ts:110-110): `sweepRetireResiduals` inspects every session, skips a session after its retire residual has already been swept, and marks the session as swept.
- **Terminate capture** cit:([`endSessionDetailed`], dashboard/src/data/sessionLifecycle.ts:203-224): a successful terminate response records its `controlStopDetail` in the lifecycle notice store.
- **Copy** cit:([`terminateResidualCopy`, `retireResidualCopy`], dashboard/src/panels/session-cockpit/lifecycleCopy.ts:29-31; dashboard/src/panels/session-cockpit/lifecycleCopy.ts:34-36): both paths label the retained fact informational.

### Invariants And Boundaries

- Presentation-only: no store writes beyond dismiss, no fetches; capture lives in the data layer
  (the focus-independent retire sweep — review finding 1 — and the terminate flow).
- The word "fail" must never appear in residual copy (test-asserted across the suites); failure
  states have their OWN surface (the rail's end-failure alert).

## Evidence

### Repo-Internal References

- The store read, note anatomy, dismiss wiring. [1]
- The notice store prepends each retained residual. [2]
- Dismissal removes the matching session/timestamp entry. [3]
- The retire sweep visits every session. [4]
- The retire sweep rejects non-string, empty, and already-swept details. [5]
- The retire sweep continues after a rejected detail. [6]
- The retire sweep marks a processed session as swept. [7]
- The terminate path that records `controlStopDetail`. [8]
- The centralized informational copy. [9]
- The view explicitly leaves `StopResidualNotes` unmounted and keeps details in the store. [10]
- View-level coverage of store retention and the absence of stacked residual DOM. [11]
