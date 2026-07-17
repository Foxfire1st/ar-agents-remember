# dashboard/src/data/announcer.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/announcer.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T08:33+02:00 |
| lastVerifiedCommitHash | `4293c53b9d6ef2bf0fee7aca11c2677322c4e786` |
| lastVerifiedCommitDate | 2026-07-17T10:26:02+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Pins the single-copy-source announcement contract, repeat sequencing, transition-only fleet
announcements, and the focused-question deduplication rule.

## Code Commentary

### Logic

The suite checks every SetResult/promotion/state string, verifies sequence increments for repeated
text, exhausts the pure state-entry detector's seed/steady/transition cases, and drives the wired
watcher through the live session store.

### Conventions

Assertions use the exported copy functions rather than duplicating prose fixtures.

### Invariants And Boundaries

This is test-only; it deliberately does not claim coverage of the reviewer's split-poll-beat sev-4
edge.

### Todos

Add a staggered turn-state/interaction-payload regression if sev-4 observation 9 is taken up.

## Docs References

No Domain Documentation source is configured; no external citation applies.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Announcement implementation under test. | L1-L102 | [announcer.ts](announcer.ts) |
| One source for every asserted string. | L1-L127 | [setControlsCopy.ts](setControlsCopy.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R8/R9 after final reviewer PASS;
  verification metadata is pinned to the uncommitted leaf's contract base pending closeout.
