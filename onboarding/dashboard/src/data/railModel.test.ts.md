# dashboard/src/data/railModel.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/railModel.test.ts`           |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-01T09:32+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`       |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

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
| The rail-model functions under test. | `buildRailModel`, `railCycleOrder`, `buildSpawnTree` | dashboard/src/data/railModel.ts:361-403; dashboard/src/data/railModel.ts:414-436 |
| The shared full-wire-shape catalog fixtures, including the multiplexed interaction row. | `catalogRow`, `FLEET`, `L7_MULTIPLEXED_INTERACTIONS` | dashboard/src/test/fixtures/catalogRows.ts:10-27; dashboard/src/test/fixtures/catalogRows.ts:32-172; dashboard/src/test/fixtures/catalogRows.ts:414-446 |
| The N1 agent-only-blocked triage pin. | "lists a seat blocked SOLELY on a multiplexed sub-agent approval" | dashboard/src/data/railModel.test.ts:415-431 |
| The served builders used by the projection-join fixtures. | `taskDoc`, `gate`, `lifecycle`, `agentPickup` | dashboard/src/test/fixtures/wire.ts:241-246; dashboard/src/test/fixtures/wire.ts:248-253; dashboard/src/test/fixtures/wire.ts:282-287; dashboard/src/test/fixtures/wire.ts:296-301 |
| The held-gate join case. | "joins HELD gates by leafKey only while undecided (R13)" | dashboard/src/data/railModel.test.ts:332-339 |
| The two-state brief-column join case. | "brief column is TWO-state: pending while unacknowledged" | dashboard/src/data/railModel.test.ts:354-372 |
| The critical-bus join case. | "critical bus = age ≥ ttl·0.8 or escalated check-chat (F11)" | dashboard/src/data/railModel.test.ts:374-387 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-08-04T08:03:35+02:00 — 260731-EFA-L6 S18-B07 curator: repaired the bounded citation findings from the recovered Avicenna and Kuhn ledgers, splitting or narrowing claims to the frozen source and normalizing scoped citation ranges.

- 2026-08-01T09:32+02:00 — 260731-EFA-L4 curator: the Invariants section claimed the whole suite was
  "Pure-logic suite over `test/fixtures/catalogRows.ts` (`catalogRow`/`FLEET`)", which the diff
  against `abc7cbc` made incomplete — the **projection joins** describe
  (cit:(["projection joins"], dashboard/src/data/railModel.test.ts:256-318)) now builds its
  nodes with `test/fixtures/wire.ts`'s `taskDoc`/`gate`/`lifecycle`/`agentPickup` instead of object
  literals closed with `as TaskDocNode` / `as unknown as LifecycleProjection`. Corrected it and
  named which fields are load-bearing at each call site. The behavioral bullets are unchanged
  because I checked the residual data deltas against the consumers rather than assuming them:
  `gate()` now hands the joins `decisions: ["approve","revise"]` where the old literal wrote `[]`,
  and `lifecycle()` gives LC1/LC2 a full served lifecycle (`state: "blocked"`, phase, tokens) where
  the old cast gave them only an `id` — but `railModel.ts::heldGatesByLeafKey`
  (cit:([`heldGatesByLeafKey`], dashboard/src/data/railModel.ts:565-579)) reads
  exactly `doc.lifecycleId`, `lifecycles[…].gate` and `gate.state !== "open"`, and never `decisions`
  or any lifecycle field, so R13 still measures undecided-ness by state alone. Likewise the doc
  fixture stopped stating `status`/`stepsDone`/`stepsTotal`/`steps` and now inherits them from the
  served row, which `qualifiedLeafKey`
  (cit:([`qualifiedLeafKey`], dashboard/src/data/taskIdentity.ts:64-70)) cannot see — it composes
  `repository`/docPath folder/`id`. Re-anchored the N1 pin from L349-L365 to L342-L358 (the
  conversion shortened the file by 7 lines, so the old range no longer contained the case) and added
  rows for the builders and the joins describe.

- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: recorded the N1 triage pin — a seat blocked
  SOLELY on a multiplexed sub-agent approval (plural-only `controlPendingInteractions` with
  adapter-bound `raw.agentLabel`) is listed by `waitingSeats`. Refreshed the fixture citation and
  noted the new `L7_MULTIPLEXED_INTERACTIONS` parent+sub-agent fixture in `catalogRows.ts`.
  Verification stays pinned; the L7 change is uncommitted and closeout re-stamps.

- 2026-07-18T07:22+02:00 — FEUI-L8 manual route refactor: retargeted this direct data file card
  from the packed dashboard/src parent to the new nearest data authority overview. Source behavior
  is unchanged by this memory-only governance move; verification hash/date remain pinned.

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S4 (R11; +1 tiebreak case in fix round 1):
  hierarchy/ordering/determinism, cycle order, spawn tree, anatomy invariants, attention rollup +
  zero-state + jump priority + every-class oldest-first tiebreak, smart focus, projection joins,
  and question triage. Verification metadata pinned to the leaf base until closeout stamps the L2
  code commit.
