# dashboard/src/data/railModel.test.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Unit suite for the rail model — every ruled hierarchy/attention/join behavior
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
- **Question triage (R16)** — prompt preview + clamping; all waiting seats newest-first; and the
  N1 pin: a seat blocked SOLELY on a multiplexed sub-agent approval (singular slot
  absent, plural list carrying the permission with adapter-bound `raw: { threadId, agentLabel }`)
  is listed by `waitingSeats` instead of going dark.

### Invariants And Boundaries

Pure-logic suite — no DOM — over two shared fixture modules. The seat/rail cases run on
`test/fixtures/catalogRows.ts` (`catalogRow`/`FLEET`); the **projection joins** describe runs on
`test/fixtures/wire.ts` (`taskDoc`, `gate`, `lifecycle`, `agentPickup`), whose bases are drawn from
`fixtures/snapshot.json` and type-checked against `types/projection.ts`. The join fixtures state only
the fields the joins read and inherit the rest as served default, which is deliberate: the comments
at the two call sites name which fields are load-bearing (`repository` + docPath folder + `id` for
`qualifiedLeafKey`, `lifecycleId` for the gate join, `messageKind` for the brief column,
`state`/`ttlSeconds` for the 720 = 900·0.8 critical-bus threshold). The determinism and tiebreak
cases are the anti-reflow / R12 regression net. Test-only.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The rail-model functions under test. [1]
- The shared full-wire-shape catalog fixtures, including the multiplexed interaction row. [2]
- The N1 agent-only-blocked triage pin. [3]
- The served builders used by the projection-join fixtures. [4]
- The held-gate join case. [5]
- The two-state brief-column join case. [6]
- The critical-bus join case. [7]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
