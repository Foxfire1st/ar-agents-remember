# dashboard/src/data/seatEvents.ts

## Governing Overview

[data overview](overview.md)

## Purpose

**Seat-event reconciliation** (260715-FEUI-L2 S2/R2): applies the `/api/events` observer channel's
seat kinds — `seat.retired | seat.landed | seat.renamed | seat.turn-state-changed`
(`serving/seat_events.py`) — against the session registry as PRE-APPLIED UI state. THE POLL STAYS
AUTHORITATIVE: everything applied here is confirmed or replaced by the next 2500 ms catalog beat.
Honest latency scoping (UA-6, module comment): retired/renamed/landed are emitted at the moment of
the tool call and CAN beat the poll by up to one beat; `turn-state-changed` is emitted BY the 10 s
rate-limited liveness sweep and can NEVER beat the poll — it is applied only as a consistency
backstop, never sold as push latency. Cockpit wires this into the SAME EventSource the Event River
holds — one connection, two consumers.

## Code Commentary

### Logic

- cit:([`applySeatEvent`], dashboard/src/data/seatEvents.ts:40-92) — kind-gated (`SEAT_EVENT_KINDS`); resolves the session by
  `event.sessionId ?? data.session`; **unknown sessions are ignored** (the poll brings new rows,
  push never invents one). Per kind:
  - `seat.retired` — a terminal mark: no-op when already `terminated`/`landed` (never resurrect,
    never double-apply), else `setStatus("terminated")` + retirement provenance patch
    (`retiredAt/Reason/Edge/BySession`).
  - `seat.landed` — same terminal-guard, `setStatus("landed")` + landing provenance.
  - `seat.renamed` — applies `label` (+ frozen `spawnedLabel`) only when it actually differs.
  - `seat.turn-state-changed` — vocabulary-guarded (`TURN_STATES`), and DEDUPED: the event `ts`
    must be STRICTLY newer than the stored `turnStateChangedAt` (the poll serves the same sweep's
    classification 4× as often and usually got here first; equal-or-older must never regress the
    row). ISO strings compared lexicographically — same-producer server stamps, flagged as
    acceptable in the worker report.
- cit:([`applySeatEventLine`], dashboard/src/data/seatEvents.ts:107-116) — the JSONL adapter for `connectEvents`; malformed lines
  and non-seat kinds are ignored, never break the feed.
- cit:([`createGatedSeatEventApplier`], dashboard/src/data/seatEvents.ts:113-130) — the **per-connection backlog gate** (review
  finding 2 fix): the channel replays history before EACH connection's `ready` marker (a reconnect
  with an undecodable cursor replays the full initial window), and replayed history must never
  touch live rows. Lines apply only between a `ready` (`onReady` opens) and the next interruption
  (`onInterrupt` — wired to the EventSource `error` — re-closes); a closed gate costs at most one
  2.5 s beat of push latency because the poll is authoritative anyway.

### Invariants And Boundaries

- Push NEVER resurrects a terminal row, never invents a row, and never regresses a newer state —
  the three dedup guards above are load-bearing and test-pinned.
- Application must stay gated per connection (not a one-shot latch): the gate consumer is
  `Cockpit.tsx`, which routes `onLine`/`onReady`/`onInterrupt` through this module.
- Only seat-state application is gated — the Event River (`pushEvent`) correctly still receives
  backlog lines on the same connection.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- Kind gate, per-kind application, strictly-newer dedup, JSONL adapter, backlog gate. [1]
- The server emitter defining the four kinds + data field names. [2]
- The `ready`/`error` transport hooks the gate rides (`connectEvents` + `onInterrupt`). [3]
- The one-EventSource-two-consumers wiring + gate lifecycle. [4]
- The `patch`/`setStatus` store actions this applies through. [5]
- The unit suite: never-resurrect, unknown-session, strict-newer dedup, vocabulary guard, malformed lines, per-connection gate. [6]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
