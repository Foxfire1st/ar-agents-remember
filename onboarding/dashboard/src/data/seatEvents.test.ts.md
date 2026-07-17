# dashboard/src/data/seatEvents.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/seatEvents.test.ts`          |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T02:30+02:00                           |
| lastVerifiedCommitHash | `e2b99dcd71fb6ca31f642dd61c3c16f3d3d05bf5`       |
| lastVerifiedCommitDate | 2026-07-17T02:52:07+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

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

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module under test. | L40-L130 | [seatEvents.ts](seatEvents.ts) |
| The store whose rows the events mutate. | — | [sessions.ts](sessions.ts) |

## Update History

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S2 (R2/R11; +2 gate cases in fix round 1):
  terminal-mark guards, unknown-session drop, rename no-op, strictly-newer turn-state dedup,
  vocabulary guard, malformed-line tolerance, and the per-connection backlog gate. Verification
  metadata pinned to the leaf base until closeout stamps the L2 code commit.
