# dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `1c1629fc97dd4daf352cf9b3529d210be167d2af`                  |
| lastVerifiedCommitDate | 2026-08-08T22:29:45+02:00|
| governingOverview      | `../overview.md`                                            |

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

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The controller entry points. | `useSessionsViewRefs`; `useSessionsViewState`; `useFocusAndLibraryHandlers` | dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:114-182; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:183-247; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:362-430; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewController.ts:72-72 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round 2 (curator): No content impact: the supervisor -> agent-notifier rename does not change the behavior this sidecar documents; reviewed current against the changed source. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  controller module extracted from `SessionsView.tsx`. Verification pinned to the
  leaf base until closeout stamps the code commit.
