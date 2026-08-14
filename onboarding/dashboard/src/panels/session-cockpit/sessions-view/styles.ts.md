# dashboard/src/panels/session-cockpit/sessions-view/styles.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/sessions-view/styles.ts` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/session-cockpit overview](../overview.md)

## Purpose

The Panda CSS recipes of the Sessions view, extracted from `SessionsView.tsx` by the
260731-EFA-L8 split. Owns the root layout, panes, stage/inspector sizing, floor chip,
reopen button, resize handle, and the persisted panel constants
(`PANELS_AUTOSAVE_ID`, `INSPECTOR_OPEN_KEY`, `RAIL_MIN_PERCENT`).

## Code Commentary

### Logic

Static atoms are `css({...})`; layout constants are exported for the resize logic and
persistence keys.

### Conventions

Tokens only; no animation.

### Invariants And Boundaries

The inspector/rail percentages and keys must stay in sync with the resize and
persistence code.

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
| The layout recipes and constants. | `root`; `stagePane`; `inspectorScroll`; `RAIL_MIN_PERCENT` | dashboard/src/panels/session-cockpit/sessions-view/styles.ts:5-51; dashboard/src/panels/session-cockpit/sessions-view/styles.ts:82-85 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the styles
  module extracted from `SessionsView.tsx`. Verification pinned to the leaf base
  until closeout stamps the code commit.
