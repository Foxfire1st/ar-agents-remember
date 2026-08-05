# dashboard/src/data/announcer.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/announcer.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:40+0200                           |
| lastVerifiedCommitHash | `4e5fbcf872bbc1ec2566a6ccb17276a6bad80c7f` |
| lastVerifiedCommitDate | 2026-07-26T18:40:37+02:00|
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

### Plural Pending Suppression (Review N1)

The focused-seat awaiting-input suppression cit:(["export function announcePolite"], dashboard/src/data/announcer.ts:33-33) now derives from
`sessions.ts`'s `sessionHasPendingInteraction(session)` — the singular parent slot OR a non-empty
multiplexed sub-agent list — instead of reading only `controlPendingInteraction`. The InteractionBar
announces EVERY pending payload (multiplexed agent entries included), so the region must stay
silent for the focused seat whenever ANY payload pends, or an agent-only-blocked focused seat is
announced twice. Unfocused seats keep the seat-level "awaiting input" wording — the region never
claims the question is the parent's.

### Conventions

All spoken strings come from `setControlsCopy.ts`; this module owns delivery and transition
detection, not copy.

### Invariants And Boundaries

There are exactly two cockpit live regions. Initial fleet hydration is silent, and focused
awaiting-input with ANY pending interaction payload (parent singular slot or a multiplexed
sub-agent entry) must not be announced twice.

### Todos

Reviewer sev-4 observation 9 remains open: when `turnState: awaiting-input` and its interaction
payload arrive on separate poll beats, the watcher and `InteractionBar` can both announce.

## Docs References

No relevant external documentation was available; the resolved source registry configures no
Domain Documentation sources.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies to this same-repository announcement seam. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Store, transition detector, and refcounted watcher. | "export function announcePolite" | dashboard/src/data/announcer.ts:33-33 |
| The ANY-pending derivation (N1) the focused-seat suppression now uses. | "export interface OpenSession" | dashboard/src/data/sessions.ts:28-28 |
| Exact announcement copy and sequencing coverage. | "SetResult arrival strings" | dashboard/src/data/announcer.test.ts:36-52 |
| The N1 agent-only-blocked pin: unfocused speaks seat-level, focused stays silent (the bar announces every pending payload). | "promotion + assertive state strings" | dashboard/src/data/announcer.test.ts:54-60 |
| Permanent DOM regions consuming both channels. | "export function CockpitLiveRegions" | dashboard/src/panels/session-cockpit/CockpitLiveRegions.tsx:19-19 |

## Cross-Repo References

No meaningful cross-repo boundary is owned by this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Reviewed Candidate Delta

`announceAssertiveBatch` joins urgent transitions into one assertive-store mutation. The seat watcher collects every failure/awaiting-input transition from a hydration and commits the batch once for assistive-technology observability.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B24 curator: replaced the superseded `(L…)`
  prose citation and the `n/a` rows with exact anchors and fixer-generated ranges; exact
  non-fixing check returns zero findings.

- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: recorded the fix-round review-N1 plural pending
  suppression. The focused-seat awaiting-input skip now derives from
  `sessions.ts`'s `sessionHasPendingInteraction` (singular slot OR non-empty multiplexed sub-agent
  list): the InteractionBar announces EVERY pending payload, so the region stays silent for the
  focused seat whenever any payload pends; unfocused seats keep the seat-level "awaiting input"
  wording and never claim the question is the parent's. Source is uncommitted; closeout re-stamps
  verification.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T08:33+02:00 — Created for 260715-FEUI-L4 R8 after final reviewer PASS. The sev-4
  split-beat double-announcement edge remains recorded above. Verification metadata is pinned to
  the contract base while the code is uncommitted; closeout must stamp the real code commit.
