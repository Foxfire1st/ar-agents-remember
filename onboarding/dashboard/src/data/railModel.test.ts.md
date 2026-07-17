# dashboard/src/data/railModel.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/railModel.test.ts`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T02:30+02:00                           |
| lastVerifiedCommitHash | `e2b99dcd71fb6ca31f642dd61c3c16f3d3d05bf5`       |
| lastVerifiedCommitDate | 2026-07-17T02:52:07+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Unit suite for the rail model (260715-FEUI-L2 S4) — every ruled hierarchy/attention/join behavior
as a pure-function case over the shared catalog fixtures.

## Code Commentary

### Logic

- **Role codes** — the six ruled codes + derived extras; absent without a spawn role.
- **`buildRailModel`** — flat role-ordered spine (never spawn-nested), managers flat in their
  master section, per-leaf clusters, ACTIVE seat to the top with worker→reviewer→curator ties,
  **determinism** (a shuffled input sorted twice gives identical order — no jumpy reflows),
  landed rows into the per-master completed folder + sprint total, unattached bucketing,
  terminated tombstones never render, master labels applied.
- **`railCycleOrder`** — spine → managers → clusters → unattached, live rows only (alt+↑/↓).
- **`buildSpawnTree`** — nests by spawn edges, exactly what the ruled default must NOT do.
- **Row anatomy (R6)** — dot+role+title always survive, only the status chip elides, tooltip
  carries the chip truth + landed/retired reasons (R17).
- **Fleet attention (R12)** — rollup + joins, zero-state suppression (working alone renders
  nothing), the full jump priority, and the review-finding-4 case: the join order is deliberately
  reversed and the LONGEST-WAITING seat must win in EVERY class (fails on the old `[0]` code).
- **Smart-default focus (R9)** — awaiting-input first (oldest wins) → failed → most recently
  active running → null.
- **Projection joins** — held gates only while undecided (R13), the two-state brief column (never
  a tri-state, R8), critical bus at age ≥ ttl·0.8 or check-chat (F11).
- **Question triage (R16)** — prompt preview + clamping; all waiting seats newest-first.

### Invariants And Boundaries

Pure-logic suite over `test/fixtures/catalogRows.ts` (`catalogRow`/`FLEET`) — no DOM. The
determinism and tiebreak cases are the anti-reflow / R12 regression net. Test-only.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module under test. | L17-L464 | [railModel.ts](railModel.ts) |
| The shared full-wire-shape fixtures (`catalogRow` builder + `FLEET`). | L10-L172 | [../test/fixtures/catalogRows.ts](../test/fixtures/catalogRows.ts) |

## Update History

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S4 (R11; +1 tiebreak case in fix round 1):
  hierarchy/ordering/determinism, cycle order, spawn tree, anatomy invariants, attention rollup +
  zero-state + jump priority + every-class oldest-first tiebreak, smart focus, projection joins,
  and question triage. Verification metadata pinned to the leaf base until closeout stamps the L2
  code commit.
