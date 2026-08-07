# dashboard/src/panels/session-cockpit/AcceptanceChip.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/AcceptanceChip.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-02T01:42+02:00 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f` |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Chip rendering and action boundary. | `AcceptanceChip` | dashboard/src/panels/session-cockpit/AcceptanceChip.tsx:56-105 |
| Typed presentation models and acceptance words. | `SetChipModel`; `deriveSetChips` | dashboard/src/data/setChips.ts:27-40; dashboard/src/data/setChips.ts:58-216 |
| Primary live-control owner. | `ModelEffortControl` | dashboard/src/panels/session-cockpit/ModelEffortControl.tsx:635-704 |
| Background outcome owner. | `SetOutcomeToasts` | dashboard/src/panels/session-cockpit/SetOutcomeToasts.tsx:58-142 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-08-03T04:00:52+02:00 — 260731-EFA-L6 W3-B06 curator: curated 8 citation findings for the chip, model/effort, and toast ownership rows.

- 2026-08-02T01:42+02:00 — No content impact: re-derived line range(s) that ended past the end of the file the row names (`memory_quality/style/citations`, `citation_range_out_of_bounds`). Each range was rewritten by reading the cited construct at its current location; no claim was changed to fit a range, and no range was interpolated. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R2/R6 after final reviewer PASS.
  Verification metadata is pinned to the contract base until the uncommitted code lands.
