# dashboard/src/panels/session-cockpit/CockpitLiveRegions.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/CockpitLiveRegions.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T08:33+02:00 |
| lastVerifiedCommitHash | `4293c53b9d6ef2bf0fee7aca11c2677322c4e786` |
| lastVerifiedCommitDate | 2026-07-17T10:26:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Persistent screen-reader live-region bridge for cockpit polite and assertive announcements.

## Code Commentary

### Logic

Subscribes to both announcer channels and renders one visually hidden `aria-live="polite"` status
and one `aria-live="assertive"` alert. Each persistent region exposes the announcement sequence
through `data-announce-seq`, so identical repeated messages still produce an observable DOM update.

### Conventions

Both regions mount before the first message and remain in the tree; callers publish through the
shared announcer rather than creating local live regions.

### Invariants And Boundaries

Visual toast/chip state is separate from auditory urgency. This component renders text only and
does not decide which events deserve polite or assertive delivery.

### Todos

None recorded; the announcer transition caveat is recorded on `announcer.ts.md`.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Persistent polite/assertive DOM bridge. | L1-L44 | [CockpitLiveRegions.tsx](CockpitLiveRegions.tsx) |
| Mount-before-message and repeated-message coverage. | L15-L39 | [CockpitLiveRegions.test.tsx](CockpitLiveRegions.test.tsx) |
| Refcounted announcement stores. | L1-L102 | [../../data/announcer.ts](../../data/announcer.ts) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R8 after final reviewer PASS. Base
  verification metadata remains temporary until the code commit exists.
