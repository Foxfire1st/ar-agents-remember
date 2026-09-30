# dashboard/src/panels/session-cockpit/sessions-view/shell.test.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/sessions-view/shell.test.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-09-30T22:35:02+02:00                                           |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`                  |
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
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
keyboard-zone registration. **Since MIK-L33** the `?` keyboard-reference case also asserts the "Intent reviewer —
while focus is inside it" group with `review.nextChange` and `review.previousChange`, and that `j` pressed in the
sessions view is not handled (`fireEvent.keyDown` returns `true`: nothing prevented it), so the reviewer's chords
are inert outside the reviewer (MIK-R33 rule 7).

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
| The `?` page lists the reviewer's chords, and `j` is unhandled in the sessions view (MIK-L33). | "? opens the keyboard-reference page listing the real chord tables (one options source)"; "Intent reviewer — while focus is inside it" | dashboard/src/panels/session-cockpit/sessions-view/shell.test.tsx:187-207 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): **body updated for MIK-R33 rule 7:** the `?` keyboard-reference case also asserts the reviewer's group and its two commands, and that `j` is not handled in the sessions view. One row added.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the shell
  suite split from `SessionsView.test.tsx`. Verification pinned to the leaf base
  until closeout stamps the code commit.
