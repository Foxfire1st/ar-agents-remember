# dashboard/src/data/announcer.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/announcer.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f` |
| lastVerifiedCommitDate | 2026-07-18T07:47:42+02:00|
| governingOverview | `overview.md`                                   |

## Governing Overview

[data overview](overview.md)

## Purpose

Owns the cockpit's two announcement channels: polite set-result/readback messages for the focused
seat and assertive transitions into failed or awaiting-input for any seat.

## Code Commentary

### Logic

`announcerStore` sequence-stamps both channels so identical text can re-announce. The pure
`stateEntryAnnouncements` detector seeds initial rows silently, announces only state-entry edges,
and defers a focused pending question to `InteractionBar`'s existing alert. The refcounted watcher
subscribes to `sessionStore` and releases the subscription when the final consumer unmounts.

### Conventions

All spoken strings come from `setControlsCopy.ts`; this module owns delivery and transition
detection, not copy.

### Invariants And Boundaries

There are exactly two cockpit live regions. Initial fleet hydration is silent, and focused
awaiting-input with a projected interaction must not be announced twice.

### Todos

Reviewer sev-4 observation 9 remains open: when `turnState: awaiting-input` and its interaction
payload arrive on separate poll beats, the watcher and `InteractionBar` can both announce.

## Docs References

No relevant external documentation was available; the resolved source registry configures no
Domain Documentation sources.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies to this same-repository announcement seam. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Store, transition detector, and refcounted watcher. | L1-L102 | [announcer.ts](announcer.ts) |
| Exact announcement copy and sequencing coverage. | L34-L125 | [announcer.test.ts](announcer.test.ts) |
| Permanent DOM regions consuming both channels. | L1-L44 | [../panels/session-cockpit/CockpitLiveRegions.tsx](../panels/session-cockpit/CockpitLiveRegions.tsx) |

## Cross-Repo References

No meaningful cross-repo boundary is owned by this file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## FEUI-L8 Reviewed Candidate Delta

`announceAssertiveBatch` joins urgent transitions into one assertive-store mutation. The seat watcher collects every failure/awaiting-input transition from a hydration and commits the batch once for assistive-technology observability.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Update History

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R8 after final reviewer PASS. The sev-4
  split-beat double-announcement edge remains recorded above. Verification metadata is pinned to
  the contract base while the code is uncommitted; closeout must stamp the real code commit.
