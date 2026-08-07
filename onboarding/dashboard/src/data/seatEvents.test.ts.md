# dashboard/src/data/seatEvents.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/seatEvents.test.ts`          |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-01T11:40+02:00 |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`       |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview | `overview.md` |

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

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module under test. | `applySeatEvent`; `applySeatEventLine`; `createGatedSeatEventApplier` | dashboard/src/data/seatEvents.ts:40-92; dashboard/src/data/seatEvents.ts:95-104; dashboard/src/data/seatEvents.ts:113-130 |
| The store whose rows the events mutate. | `sessionStore` | dashboard/src/data/sessions.ts:494-508 |
| The local `event()` factory supplies explicit `id`/`ts` over the shared defaults. | `event` | dashboard/src/data/seatEvents.test.ts:15-21 |
| The shared `observerEvent` fixture supplies the schema/trust/actor defaults. | `observerEvent` | dashboard/src/test/fixtures/wire.ts:373-385 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-04T13:00:51+02:00 — 260731-EFA-L6 S18-B11 curator: converted the seat-event reference rows and legacy prose citations to exact anchors, preserving the local-factory/default precedence claim for scoped citation fixing. Verification metadata unchanged.

- 2026-08-01T11:40+02:00 — 260731-EFA-L4 curator (correction pass): retained the behavioral analysis, corrected its attestation to no behavioral impact, and added the missing shared-fixture reference. The local `event()` factory wraps `observerEvent` cit:([`event`], dashboard/src/data/seatEvents.test.ts:15-21) cit:([`observerEvent`], dashboard/src/test/fixtures/wire.ts:373-385); the module-under-test functions remain covered by the table above. Verification metadata untouched.

- 2026-08-01T09:26+02:00 — 260731-EFA-L4 curator: the local `event()` factory delegates to the shared `observerEvent` fixture cit:([`event`], dashboard/src/data/seatEvents.test.ts:15-21) cit:([`observerEvent`], dashboard/src/test/fixtures/wire.ts:373-385). Its explicit id/timestamp overrides preserve the deterministic event envelope used by the `seat.turn-state-changed` case. Verification metadata remains unchanged.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S2 (R2/R11; +2 gate cases in fix round 1):
  terminal-mark guards, unknown-session drop, rename no-op, strictly-newer turn-state dedup,
  vocabulary guard, malformed-line tolerance, and the per-connection backlog gate. Verification
  metadata pinned to the leaf base until closeout stamps the L2 code commit.
