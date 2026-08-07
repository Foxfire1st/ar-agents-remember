# dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/session-cockpit overview](../overview.md)

## Purpose

The composed rail/stage/inspector JSX of the Sessions view, extracted from
`SessionsView.tsx` by the 260731-EFA-L8 split. `SessionsViewBody` renders the rail
panel, stage header actions, failed-launch slot, working-line slot, composer slot,
stage working area, stage panel, inspector panel, and overlays from the controller
view.

## Code Commentary

### Logic

Each slot subcomponent renders one surface (rail, stage header, failed launch,
working line, composer, stage, inspector, overlays) from the derived `View`. The
persistent PTY composition and keep-alive mounting rules are honored at the stage
level.

### Conventions

Presentational composition; all data comes from the controller `View`.

### Invariants And Boundaries

The body never fetches or mutates state; it renders the view packet only.

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
| The composed body and its stage/inspector slots. | `SessionsViewBody`; `StagePanel`; `InspectorPanel` | dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:274-305; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:307-363; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:403-430 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the body
  module extracted from `SessionsView.tsx`. Verification pinned to the leaf base
  until closeout stamps the code commit.
