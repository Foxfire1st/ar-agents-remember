# dashboard/src/panels/session-cockpit/CockpitLiveRegions.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/CockpitLiveRegions.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md`                                   |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Persistent polite/assertive DOM bridge. | `CockpitLiveRegions` | dashboard/src/panels/session-cockpit/CockpitLiveRegions.tsx:19-45 |
| Mount-before-message and repeated-message coverage. | "renders one polite and one assertive region" | dashboard/src/panels/session-cockpit/CockpitLiveRegions.test.tsx:16-26 |
| Refcounted announcement stores. | `announcerStore` | dashboard/src/data/announcer.ts:25-28 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## FEUI-L8 Reviewed Candidate Delta

Polite and assertive messages render through sequence-keyed spans. Repeating identical text therefore replaces an accessibility-tree node instead of relying on an unchanged text node.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Update History

- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: anchored 3 citation rows; scoped citation fixing regenerated the source ranges.
- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R8 after final reviewer PASS. Base
  verification metadata remains temporary until the code commit exists.
