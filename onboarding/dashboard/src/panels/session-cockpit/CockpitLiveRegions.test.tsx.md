# dashboard/src/panels/session-cockpit/CockpitLiveRegions.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/CockpitLiveRegions.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T08:33+02:00 |
| lastVerifiedCommitHash | `4293c53b9d6ef2bf0fee7aca11c2677322c4e786` |
| lastVerifiedCommitDate | 2026-07-17T10:26:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Accessibility regression contract for the cockpit's persistent dual live regions.

## Code Commentary

### Logic

Proves that both urgency channels exist before any announcement, that messages route to the
correct region, and that repeated identical messages advance the sequence.

### Conventions

The suite exercises the real announcer stores and clears state around each case.

### Invariants And Boundaries

Polite and assertive regions remain distinct and mounted; repeat delivery cannot rely on text
changing.

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
| Dual-region and repeated-message cases. | L15-L39 | [CockpitLiveRegions.test.tsx](CockpitLiveRegions.test.tsx) |
| Component under test. | L1-L44 | [CockpitLiveRegions.tsx](CockpitLiveRegions.tsx) |
| Announcement store under test. | L1-L102 | [../../data/announcer.ts](../../data/announcer.ts) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T08:33+02:00 — Created for the 260715-FEUI-L4 R8 live-region regression after
  final reviewer PASS. Base verification metadata is temporary until code commit.
