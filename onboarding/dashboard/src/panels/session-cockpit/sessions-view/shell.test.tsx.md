# dashboard/src/panels/session-cockpit/sessions-view/shell.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/sessions-view/shell.test.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                                            |

## Governing Overview

[panels/session-cockpit overview](../overview.md)

## Purpose

The shell/scaffold suite split from `SessionsView.test.tsx` by the 260731-EFA-L8
test split (47-name set reconciled item-for-item). Pins the scaffold structure, the
~80-col floor chip re-measure, the ~280px rail calibration, command palette, and
keyboard zones over the legacy-raw PTY.

## Code Commentary

### Logic

Uses `test-utils.tsx` seeds and a local `setClientWidth` helper to simulate panel
layout changes; asserts the floor-chip and rail calibration behavior plus palette and
keyboard-zone registration.

### Invariants And Boundaries

Assertions preserved from the monolithic suite.

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
| The shell suite. | `describe` | dashboard/src/panels/session-cockpit/sessions-view/shell.test.tsx:2-2 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the shell
  suite split from `SessionsView.test.tsx`. Verification pinned to the leaf base
  until closeout stamps the code commit.
