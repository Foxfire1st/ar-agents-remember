# dashboard/src/panels/session-cockpit/interactionParts.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The structured-interaction render parts of the session cockpit, extracted from
`InteractionBar.tsx` by the 260731-EFA-L8 split. Owns the questions body, announce
region, interaction head/body/status row, and hint.

## Code Commentary

### Logic

`QuestionsBody` renders the gate-question options; `InteractionAnnounce` is the live
announce region; `InteractionBody`/`InteractionStatusRow` render the answer state and
its honest status (answered/error/working).

### Conventions

Answers ride the landed gate channel; these parts never write to the terminal.

### Invariants And Boundaries

The interaction parts render the decision record only; no submit machinery here.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The interaction render parts. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
