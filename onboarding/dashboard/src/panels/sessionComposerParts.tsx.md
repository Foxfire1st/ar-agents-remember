# dashboard/src/panels/sessionComposerParts.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/sessionComposerParts.tsx`             |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`                  |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[panels/ overview](overview.md)

## Purpose

The render parts of the shared `SessionComposer`, extracted from
`SessionComposer.tsx` by the 260731-EFA-L8 split. Owns the composer frame, answer
mode row, gate notice, withdrawal recovery, route/endgame/status rows, stop
controls, footer, and the `ComposerView` composition.

## Code Commentary

### Logic

`ComposerStatus` maps the submit record to the honest status row (working/error/
answered); `WithdrawalRecovery` renders the pop-back affordance;
`ComposerView` composes the frame, editor slot, status, and footer from the view
data.

### Conventions

Presentational; all behavior lives in the hooks layer.

### Invariants And Boundaries

The stop control must be UA-7-gated; no stop without the working theater.

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
| The composer render parts. | `ComposerStatus`; `WithdrawalRecovery`; `ComposerView` | dashboard/src/panels/sessionComposerParts.tsx:265-319; dashboard/src/panels/sessionComposerParts.tsx:98-134; dashboard/src/panels/sessionComposerParts.tsx:415-487; dashboard/src/panels/sessionComposerParts.tsx:408-408 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the render
  parts module extracted from `SessionComposer.tsx`. Verification pinned to the leaf
  base until closeout stamps the code commit.
