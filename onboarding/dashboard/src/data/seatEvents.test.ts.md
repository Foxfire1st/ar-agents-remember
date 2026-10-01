# dashboard/src/data/seatEvents.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Unit suite for the seat-event reconciler (260715-FEUI-L2 S2/R2) — every honesty/dedup guard is a
behavioral case that drives real events through the real session store.

## Code Commentary

### Logic

- **`seat.retired` / `seat.landed`** — marks a running row with full provenance; NEVER resurrects
  or double-applies over poll truth (a second event on a terminal row is a no-op); unknown
  sessions are ignored (push never invents a row).
- **`seat.renamed`** — applies + freezes `spawnedLabel`; a rename the poll already delivered is a
  no-op.
- **`seat.turn-state-changed`** — the strictly-newer dedup matrix (equal and older stamps
  rejected, newer applied) and the closed vocabulary guard (unknown turn-state words rejected —
  mirrored vocabulary only).
- **`applySeatEventLine`** — JSONL parsing tolerance: malformed lines and non-seat kinds ignored.
- **`createGatedSeatEventApplier` (review finding 2)** — lines apply only between a `ready` and
  the next interruption; an interrupt RE-CLOSES the gate so a reconnect's backlog (the
  undecodable-cursor full-window replay) never applies until that connection's own `ready`. These
  cases fail against the old one-shot latch.

### Invariants And Boundaries

The dedup + gate cases are the R2 regression net; they encode poll authority (push pre-applies,
never overrides newer truth). Test-only.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The module under test. [1]
- The store whose rows the events mutate. [2]
- The local `event()` factory supplies explicit `id`/`ts` over the shared defaults. [3]
- The shared `observerEvent` fixture supplies the schema/trust/actor defaults. [4]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
