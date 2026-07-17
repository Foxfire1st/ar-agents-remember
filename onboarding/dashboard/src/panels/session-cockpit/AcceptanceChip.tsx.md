# dashboard/src/panels/session-cockpit/AcceptanceChip.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/AcceptanceChip.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T08:33+02:00 |
| lastVerifiedCommitHash | `4293c53b9d6ef2bf0fee7aca11c2677322c4e786` |
| lastVerifiedCommitDate | 2026-07-17T10:26:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Shared accessible renderer for one typed set/pair/route chip.

## Code Commentary

### Logic

Renders the model's literal evidence text, tone, optional slow spinner, and owner-supplied
acknowledge or retry actions. Test ids and data attributes expose chip kind and acceptance without
reclassifying the evidence in the component.

### Conventions

The acceptance word is always present in visible text; tone is supplemental. The spinner follows
the 2.4-second pulse ruling and disables animation under reduced motion.

### Invariants And Boundaries

Only `demandsAck` chips may receive mark-seen behavior and only retryable route chips may receive
retry behavior. This component never owns either side effect.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Chip rendering and action boundary. | L1-L105 | [AcceptanceChip.tsx](AcceptanceChip.tsx) |
| Typed presentation models and acceptance words. | L1-L232 | [../../data/setChips.ts](../../data/setChips.ts) |
| Primary live-control owner. | L148-L383 | [ModelEffortControl.tsx](ModelEffortControl.tsx) |
| Background outcome owner. | L58-L142 | [SetOutcomeToasts.tsx](SetOutcomeToasts.tsx) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R2/R6 after final reviewer PASS.
  Verification metadata is pinned to the contract base until the uncommitted code lands.
