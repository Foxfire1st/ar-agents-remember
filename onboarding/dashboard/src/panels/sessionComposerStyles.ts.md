# dashboard/src/panels/sessionComposerStyles.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/sessionComposerStyles.ts`             |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[panels/ overview](overview.md)

## Purpose

The Panda CSS recipes of the shared `SessionComposer`, extracted from
`SessionComposer.tsx` by the 260731-EFA-L8 split. Owns the dock, editor frame,
footer, send/stop buttons, status/error/recovery text, secondary button, and the
CodeMirror theme.

## Code Commentary

### Logic

Static atoms plus the `composerTheme` EditorView theme extension; stop-button
enabled/disabled states are distinct recipes.

### Conventions

Tokens; the editor theme stays with the composer styles.

### Invariants And Boundaries

The dock must keep the editor surface stable across submit cycles.

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
| The composer recipes. | `dock`; `sendButton`; `stopButtonEnabled`; `composerTheme` | dashboard/src/panels/sessionComposerStyles.ts:4-165 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the styles
  module extracted from `SessionComposer.tsx`. Verification pinned to the leaf base
  until closeout stamps the code commit.
