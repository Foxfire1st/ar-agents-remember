# dashboard/src/panels/session-cockpit/CockpitLiveRegions.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/CockpitLiveRegions.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T08:33+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Dual-region and repeated-message cases. | `CockpitLiveRegions` | dashboard/src/panels/session-cockpit/CockpitLiveRegions.tsx:19-45 |
| Component under test. | `CockpitLiveRegions` | dashboard/src/panels/session-cockpit/CockpitLiveRegions.tsx:19-45 |
| Announcement store under test. | `announcerStore` | dashboard/src/data/announcer.ts:25-28 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-08-02T20:53:56+02:00 — W2-B04 curator: repaired 6 citation findings; scoped check passed.

- 2026-07-17T08:33+02:00 — Created for the 260715-FEUI-L4 R8 live-region regression after
  final reviewer PASS. Base verification metadata is temporary until code commit.
