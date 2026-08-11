# dashboard/src/panels/session-cockpit/StopResidualNotes.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/StopResidualNotes.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T04:20+02:00                           |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`       |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                    |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The store read, note anatomy, dismiss wiring. | `StopResidualNotes` | dashboard/src/panels/session-cockpit/StopResidualNotes.tsx:41-72 |
| The notice store prepends each retained residual. | "residuals: [residual" | dashboard/src/data/sessionLifecycle.ts:75-75 |
| Dismissal removes the matching session/timestamp entry. | "state.residuals.filter"; "entry.sessionId === sessionId && entry.at === at" | dashboard/src/data/sessionLifecycle.ts:78-79 |
| The retire sweep visits every session. | "for (const session of sessions)" | dashboard/src/data/sessionLifecycle.ts:87-87 |
| The retire sweep rejects non-string, empty, and already-swept details. | "typeof detail !== \"string\""; "!detail"; "state.sweptRetire[session.id]" | dashboard/src/data/sessionLifecycle.ts:90-92 |
| The retire sweep continues after a rejected detail. | "continue;" | dashboard/src/data/sessionLifecycle.ts:94-94 |
| The retire sweep marks a processed session as swept. | "sweptRetire[session.id] = true" | dashboard/src/data/sessionLifecycle.ts:110-110 |
| The terminate path that records `controlStopDetail`. | `endSessionDetailed` | dashboard/src/data/sessionLifecycle.ts:203-224 |
| The centralized informational copy. | `terminateResidualCopy`, `retireResidualCopy` | dashboard/src/panels/session-cockpit/lifecycleCopy.ts:29-31; dashboard/src/panels/session-cockpit/lifecycleCopy.ts:34-36 |
| The view explicitly leaves `StopResidualNotes` unmounted and keeps details in the store. | `StopResidualNotes` | dashboard/src/panels/session-cockpit/StopResidualNotes.tsx:41-72 |
| View-level coverage of store retention and the absence of stacked residual DOM. | "NO stacked DOM notice" | dashboard/src/panels/session-cockpit/sessions-view/stopResiduals.test.tsx:138-183 |

## Update History
- 2026-08-04T09:54:46+02:00 — 260731-EFA-L6 S18-B07 second bounded correction: expanded dismissal and the multiline retire-sweep guard/mark evidence; same-reviewer delta pending.

- 2026-08-02T16:45:41+02:00 — 260731-EFA-L6 curator W1-B10: repaired 8 citation findings; preserved 6 Tier-3 findings whose claims contradict current rendering; scoped recheck clean with those findings preserved.

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R5: the dismissable informational
  `role="status"` residual lines on the stage — terminate `controlStopDetail` and swept
  `retireControlStopError` rendered from the dedicated lifecycle notice store (residuals outlive
  tombstoned rows), copy centralized and never styled as failure, dismissals durable across poll
  beats. Verification metadata pinned to the leaf base until closeout stamps the L6 code commit.
