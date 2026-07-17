# dashboard/src/panels/session-cockpit/HeaderStrip.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/HeaderStrip.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T02:30+02:00                           |
| lastVerifiedCommitHash | `e2b99dcd71fb6ca31f642dd61c3c16f3d3d05bf5`       |
| lastVerifiedCommitDate | 2026-07-17T02:52:07+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **HeaderStrip** (260715-FEUI-L2 S5, spec §1.2 — R10): the focused seat's stage header line in
the RULED anatomy order — identity → controls → state → leaf/seat → diagnostics. The
ModelEffortControl slot ships EMPTY (L4 fills it; reserving it now keeps the layout stable when
the control arrives). Provenance badges (R7 — moat 1, read-only) ride the diagnostics cluster with
honest requested-tier wording only.

## Code Commentary

### Logic

- **Anatomy + elision** (L15-L64, L94-L143): one nowrap flex strip. Identity (label + harness)
  and the state cluster are `flex: none` — they NEVER elide; leaf/seat is `flex: 0 2 auto`;
  diagnostics is `flex: 0 4 auto; min-width:0` — the FIRST segment to elide (highest shrink),
  matching R10's diagnostics-first elision order.
- **Controls slot** (L100-L106): `data-slot="model-effort-control"` — EMPTY by design, reserved
  for L4.
- **State cluster** (L107-L110): `StateDot` + the grammar's state word (`seatVisualState`) — the
  same visuals as the rail row (cross-surface test).
- **Leaf/seat** (L111-L117): `leaf <leaf-id> · seat <role>` from `leafKey`/`spawnRole ?? seatRole`.
- **Freshness honesty (R15)** (L66-L77, L118-L125): `WS_WORDS` — `ws —` when NO pane exists in
  this cockpit yet (the pane lands in L6; absent, never faked), else the real ws state; `quiet
  Xs/Xm` ONLY when an output stamp exists; the tooltip states the 10 s sweep bound on turn-state
  freshness.
- **Provenance badges (R7)** (L126-L141): `model <resolvedModel> · <effort> (requested)` while the
  evidence tier is `pending` — the tier word once L4 proves better — plus `spawnLevel
  (spawnLevelSource)`; hand-opened sessions with no provenance render NO chips (absent, never
  invented).

### Invariants And Boundaries

- Identity and state never elide; diagnostics always elides first — layout-pinned by the flex
  factors, order-pinned by the anatomy test.
- The requested pair must NEVER read as effective: the `(requested)` wording is the honesty
  boundary until `launchEvidence.tier` promotes with proof (cockpit store, L4).
- The empty controls slot is a stable reservation — nothing may render into it before L4.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Anatomy, elision factors, freshness words, provenance badges. | L15-L145 | [HeaderStrip.tsx](HeaderStrip.tsx) |
| The grammar + single dot renderer the state cluster uses. | — | [StateDot.tsx](StateDot.tsx) |
| The freshness/evidence state consumed (`PerSessionCockpit`). | L56-L81 | [../../data/sessionCockpitStore.ts](../../data/sessionCockpitStore.ts) |
| The stage container mounting this as the always-on header layer. | L62-L86 | [SessionStage.tsx](SessionStage.tsx) |
| The suite: anatomy order, empty slot, grammar word, freshness honesty, provenance tiers. | L16-L81 | [HeaderStrip.test.tsx](HeaderStrip.test.tsx) |

## Update History

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S5 (R7/R10/R15): the §1.2 header anatomy
  with diagnostics-first elision and never-eliding identity/state, the reserved EMPTY
  ModelEffortControl slot, the shared-grammar state cluster, honest per-pane freshness (`ws —`,
  quiet age, sweep-bound tooltip), and requested-tier provenance badges. Verification metadata
  pinned to the leaf base until closeout stamps the L2 code commit.
