# dashboard/src/data/announcer.ts

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

## Evidence

### Docs References

No relevant external documentation was available; the resolved source registry configures no
Domain Documentation sources.

No external domain citation applies to this same-repository announcement seam.

### Repo-Internal References

- Store, transition detector, and refcounted watcher. [1]
- The ANY-pending derivation (N1) the focused-seat suppression now uses. [2]
- Exact announcement copy and sequencing coverage. [3]
- The N1 agent-only-blocked pin: unfocused speaks seat-level, focused stays silent (the bar announces every pending payload). [4]
- Permanent DOM regions consuming both channels. [5]

### Cross-Repo References

No meaningful cross-repo boundary is owned by this file.

No cross-repo evidence applies.

## Reviewed Candidate Delta

`announceAssertiveBatch` joins urgent transitions into one assertive-store mutation. The seat watcher collects every failure/awaiting-input transition from a hydration and commits the batch once for assistive-technology observability.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.
