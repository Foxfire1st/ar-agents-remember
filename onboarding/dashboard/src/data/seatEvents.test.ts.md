# dashboard/src/data/seatEvents.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/seatEvents.test.ts`          |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-01T11:40+02:00 |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module under test. | L40-L130 | [seatEvents.ts](seatEvents.ts) |
| The store whose rows the events mutate. | — | [sessions.ts](sessions.ts) |
| The shared `observerEvent` builder the local `event()` factory (L15-L21) now wraps; its `schema`/`trust`/`actor` defaults are the fields the factory used to inline, and the factory's own `id`/`ts` still win by spreading last. | L369-L381 | [../test/fixtures/wire.ts](../test/fixtures/wire.ts) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-08-01T11:40+02:00 — 260731-EFA-L4 curator (correction pass): **the 09:26 entry's analysis is
  sound and is kept in full; its `No content impact:` header was not.** The conversion introduced a
  new dependency this card did not record — `seatEvents.test.ts` L6 now imports `observerEvent` from
  `../test/fixtures/wire.ts` and the local `event()` factory (L15-L21) is a wrapper over it — and the
  `Repo-Internal References` table had no fixtures row of any kind. (The review lead said this card
  carried a "Shared deterministic fixtures" row naming `capabilityEnvelopes.ts`; it does not — that
  row exists on `setClient.test.ts.md`, and here the row was simply absent.) A card that needs a new
  reference row has content impact by definition, so the attestation is re-stated as **no behavioural
  impact**, which is what the 09:26 analysis actually establishes. Added the row pointing at
  `../test/fixtures/wire.ts` (`observerEvent`, L369-L381), matching the rows the same curator added on
  `railModel.test.ts.md`, `interactionAnswer.test.ts.md` and `store.test.ts.md`; the table is
  three-column here, so the new row carries three cells. Re-verified the kept citations from the
  working tree: `seatEvents.ts` is 130 lines and `L40-L130` contains `applySeatEvent` (L40),
  `applySeatEventLine` (L95) and `createGatedSeatEventApplier` (L113); the builder's defaults at
  wire.ts L369-L381 are exactly the `schema`/`id`/`ts`/`trust`/`actor` set the entry describes, and
  the factory's explicit `id`/`ts` do spread last. Verification metadata untouched.

- 2026-08-01T09:26+02:00 — 260731-EFA-L4 curator: No behavioural impact (this entry originally read
  "No content impact"; corrected 11:40 — the card gained a `wire.ts` reference row): the entire diff against
  `abc7cbc` is the local `event()` factory (L15-L21) delegating to
  `test/fixtures/wire.ts::observerEvent` instead of building an inline object closed with
  `as ObserverEvent`. The check that could have made this consequential: the builder supplies its own
  defaults, so I compared them field by field against the ones the factory used to inline —
  `schema: "ar-observer-event/v1"`, `trust: "observed"`, `actor: "system"` are identical, and the
  factory still passes `id: "evt-1"` and `ts: "2026-07-16T10:00:00Z"` explicitly, which win over the
  builder's `id: evt-${kind}` / `ts: SERVED.generatedAt` defaults because the overrides spread last.
  The produced envelope is therefore byte-identical, which matters most for the
  `seat.turn-state-changed` describe (L99-L147), whose whole subject is comparing an event `ts`
  against the seeded row's `turnStateChangedAt`. Confirmed all five describes and eleven cases are
  unchanged in name, count and order, and that the L40-L130 citation still contains
  `applySeatEvent`, `applySeatEventLine` and `createGatedSeatEventApplier` in the 130-line source.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S2 (R2/R11; +2 gate cases in fix round 1):
  terminal-mark guards, unknown-session drop, rename no-op, strictly-newer turn-state dedup,
  vocabulary guard, malformed-line tolerance, and the per-connection backlog gate. Verification
  metadata pinned to the leaf base until closeout stamps the L2 code commit.
