# dashboard/src/panels/sessionComposerParts.tsx

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

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The composer render parts. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
