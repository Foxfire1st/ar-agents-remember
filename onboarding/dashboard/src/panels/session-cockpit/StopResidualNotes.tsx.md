# dashboard/src/panels/session-cockpit/StopResidualNotes.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/StopResidualNotes.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T04:20+02:00                           |
| lastVerifiedCommitHash | `dcf35a0e0fc06bccdafd22390b7588b0aea811bc`       |
| lastVerifiedCommitDate | 2026-09-22T20:08:58+02:00|
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
| The retire sweep rejects non-string, empty, and already-swept details. | "typeof detail !== \"string\""; "!detail"; "state.sweptRetire[session.id]" | dashboard/src/data/sessionLifecycle.ts:90-92; dashboard/src/data/sessionLifecycle.ts:1-1; dashboard/src/data/sessionLifecycle.ts:2-2; dashboard/src/data/sessionLifecycle.ts:4-4; dashboard/src/data/sessionLifecycle.ts:5-5; dashboard/src/data/sessionLifecycle.ts:10-10; dashboard/src/data/sessionLifecycle.ts:14-14; dashboard/src/data/sessionLifecycle.ts:26-26; dashboard/src/data/sessionLifecycle.ts:30-30; dashboard/src/data/sessionLifecycle.ts:31-31; dashboard/src/data/sessionLifecycle.ts:32-32; dashboard/src/data/sessionLifecycle.ts:34-34; dashboard/src/data/sessionLifecycle.ts:35-35; dashboard/src/data/sessionLifecycle.ts:39-39; dashboard/src/data/sessionLifecycle.ts:40-40; dashboard/src/data/sessionLifecycle.ts:45-45; dashboard/src/data/sessionLifecycle.ts:50-50; dashboard/src/data/sessionLifecycle.ts:52-52; dashboard/src/data/sessionLifecycle.ts:53-53; dashboard/src/data/sessionLifecycle.ts:54-54; dashboard/src/data/sessionLifecycle.ts:57-57; dashboard/src/data/sessionLifecycle.ts:58-58; dashboard/src/data/sessionLifecycle.ts:59-59; dashboard/src/data/sessionLifecycle.ts:61-61; dashboard/src/data/sessionLifecycle.ts:62-62; dashboard/src/data/sessionLifecycle.ts:63-63; dashboard/src/data/sessionLifecycle.ts:64-64; dashboard/src/data/sessionLifecycle.ts:65-65; dashboard/src/data/sessionLifecycle.ts:84-84; dashboard/src/data/sessionLifecycle.ts:85-85; dashboard/src/data/sessionLifecycle.ts:86-86; dashboard/src/data/sessionLifecycle.ts:88-88; dashboard/src/data/sessionLifecycle.ts:94-94; dashboard/src/data/sessionLifecycle.ts:96-96; dashboard/src/data/sessionLifecycle.ts:97-97; dashboard/src/data/sessionLifecycle.ts:98-98; dashboard/src/data/sessionLifecycle.ts:109-109; dashboard/src/data/sessionLifecycle.ts:110-110; dashboard/src/data/sessionLifecycle.ts:112-112; dashboard/src/data/sessionLifecycle.ts:121-121; dashboard/src/data/sessionLifecycle.ts:125-125; dashboard/src/data/sessionLifecycle.ts:131-131; dashboard/src/data/sessionLifecycle.ts:133-133; dashboard/src/data/sessionLifecycle.ts:134-134; dashboard/src/data/sessionLifecycle.ts:137-137; dashboard/src/data/sessionLifecycle.ts:140-140; dashboard/src/data/sessionLifecycle.ts:141-141; dashboard/src/data/sessionLifecycle.ts:142-142; dashboard/src/data/sessionLifecycle.ts:144-144; dashboard/src/data/sessionLifecycle.ts:146-146; dashboard/src/data/sessionLifecycle.ts:147-147; dashboard/src/data/sessionLifecycle.ts:148-148; dashboard/src/data/sessionLifecycle.ts:150-150; dashboard/src/data/sessionLifecycle.ts:151-151; dashboard/src/data/sessionLifecycle.ts:153-153; dashboard/src/data/sessionLifecycle.ts:157-157; dashboard/src/data/sessionLifecycle.ts:159-159; dashboard/src/data/sessionLifecycle.ts:161-161; dashboard/src/data/sessionLifecycle.ts:178-178; dashboard/src/data/sessionLifecycle.ts:180-180; dashboard/src/data/sessionLifecycle.ts:181-181; dashboard/src/data/sessionLifecycle.ts:184-184; dashboard/src/data/sessionLifecycle.ts:185-185; dashboard/src/data/sessionLifecycle.ts:189-189; dashboard/src/data/sessionLifecycle.ts:190-190; dashboard/src/data/sessionLifecycle.ts:195-195; dashboard/src/data/sessionLifecycle.ts:206-206; dashboard/src/data/sessionLifecycle.ts:207-207; dashboard/src/data/sessionLifecycle.ts:208-208; dashboard/src/data/sessionLifecycle.ts:209-209; dashboard/src/data/sessionLifecycle.ts:212-212; dashboard/src/data/sessionLifecycle.ts:213-213; dashboard/src/data/sessionLifecycle.ts:221-221; dashboard/src/data/sessionLifecycle.ts:223-223; dashboard/src/data/sessionLifecycle.ts:235-235; dashboard/src/data/sessionLifecycle.ts:239-239; dashboard/src/data/sessionLifecycle.ts:240-240; dashboard/src/data/sessionLifecycle.ts:243-243; dashboard/src/data/sessionLifecycle.ts:244-244; dashboard/src/data/sessionLifecycle.ts:245-245; dashboard/src/data/sessionLifecycle.ts:247-247; dashboard/src/data/sessionLifecycle.ts:248-248; dashboard/src/data/sessionLifecycle.ts:249-249; dashboard/src/data/sessionLifecycle.ts:250-250 |
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
