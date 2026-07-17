# dashboard/src/panels/session-cockpit/SessionRail.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/SessionRail.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T02:30+02:00                           |
| lastVerifiedCommitHash | `e2b99dcd71fb6ca31f642dd61c3c16f3d3d05bf5`       |
| lastVerifiedCommitDate | 2026-07-17T02:52:07+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **session rail** (260715-FEUI-L2 S4): renders the RULED role-driven hierarchy (spec §1.6b) —
flat command spine, indented per-leaf clusters with the active seat on top, per-master completed
folders with master+sprint bulk end — plus the fleet-attention strip (R12), gate badges (R13), the
two-state brief column (R8), the poll-health stale banner (R15), and the bus-summary footer (R8).
The orchestration-tree (spawn-edge) view stays available as a button/palette toggle for provenance
inspection only (R5). All derivations live in `data/railModel.ts`; this file is DOM + wiring.

## Code Commentary

### Logic

- **Props vs store** (L364-L380): `model`/`rollup` arrive as PROPS — derived once in
  `SessionsView` and shared with the palette commands (one derivation, two surfaces; same-snapshot
  consistency, worker flag 5) — while `sessions`, the tree toggle, poll health, and the projection
  slices (`taskDocuments`, `lifecycles`, `agentPickups`, `supervisorHeartbeat`) are store reads.
- **Row anatomy `renderRow`** (L439-L523, RULED R6): dot · role(3) · title · attention-slot ·
  status · End. The title is the flex segment (`min-width: 3.5rem` — ALWAYS survives); the status
  chip is the ONLY elidable segment (`flexShrink:1; min-width:0; max-width:7rem`); the full truth
  stays in the row tooltip (`railRowTooltip`). Status chips carry the grammar's status vocabulary
  ONLY — the DOM-negative test proves `resolvedModel`/`resolvedEffort` render NOWHERE in the rail.
  The `data-slot="attention-marker"` slot (R6's reserved slot, consumed by L4) carries the
  two-state brief marker (✉, R8) and the held-gate badge (R13, + `data-attention-gate` on the
  row). The `input?` chip's tooltip carries the pending question's prompt preview (R16). The End
  segment renders on EVERY row (fix round 1, finding 5): live rows say `End`
  (`endSession` → `POST /api/terminal/{id}/terminate`), dormant/landed rows the mockup's compact
  `✕` — same terminate route (note: bulk end uses `/landed-cleanup`; the reviewer noted the code
  comment is loose, both are valid terminal marks).
- **Ruled hierarchy render** (L525-L587, L694-L725): spine rows flat; `renderMaster` — master box
  with label + dominant attention badge (`masterAttentionBadge`) + the master bulk-end control;
  managers flat at the top of the box; leaf clusters as `leafGroup` — indented 0.9rem with a FINE
  55%-grid hairline + margin, never heavy boxes (RULED); the completed folder collapsed by
  default (`▸ completed · N`, expandable per master); unattached (live + landed) in one plain
  group box.
- **Bulk end with honest preview** (L342-L360, L418-L437): arming (`✕ end N done` / sprint-level
  `✕ end N completed`) swaps to an inline confirm that NAMES every removed session before
  executing (`bulkConfirm`); `endLanded` posts the id list to `cleanupLandedTerminalSessions`,
  closes only backend-confirmed rows, broadcasts, and rehydrates excluding the closed ids. No
  blind bulk delete path exists.
- **Attention strip** (L589-L642, R12): renders NOTHING at zero state (`attentionZeroState` —
  working alone is not attention); each count is a filter button that focuses the class's
  longest-waiting seat (`jumpToAttentionTarget` over a single-class rollup) AND highlights the
  set. The highlight stores the clicked CLASS (`highlightKind`) and derives the ring set from the
  LIVE rollup each render — a ring expires the moment the seat's state resolves (fix round 1,
  finding 3).
- **Poll-health banner** (L656-L660, R15): `pollHealth.healthy === false` ⇒ the amber "catalog
  poll stale — N beats missed; rows may be frozen" banner.
- **Bus footer** (L726-L741, R8): anchored numbers from `supervisorHeartbeat` — `inbox N pending /
  M redeliverable`, `heartbeat Xs / stale Ys` with the 10 s sweep bound in the tooltip; renders
  the truth ("supervisor has not ticked in this workspace") when null — never fake numbers.
- **Tree toggle** (L683-L705): swaps to `buildSpawnTree` rows indented by spawn depth (provenance
  inspection only); persisted per user via the cockpit store.
- **Zero state** (L694-L697, R9): an EXPLAINED empty rail ("no sessions — launch one from Chats;
  the cockpit launcher lands in L5"), never an unexplained blank.

### Conventions

Co-located Panda `css`/`cva` on podracer tokens; `data-testid` on every assertable element
(`rail-row-*`, `rail-dot-*`, `rail-status-*`, `rail-end-*`, `rail-attention-*`, `rail-master-*`,
`rail-cluster-*`, `rail-bulk-*`, `rail-done-toggle-*`, `rail-tree-toggle`, `rail-poll-stale`,
`rail-bus-footer`, `rail-zero-state`); rows are `role="button"` with Enter/Space handling; the
rail root carries `data-focus-target` (design §5.3 — always present, even empty).

### Invariants And Boundaries

- The rail renders MODEL truth only: no model/effort anywhere (R6), no fabricated latency, no
  invented states — chips/words come exclusively from `stateGrammar`.
- The ruled anatomy order and the only-status-elides truncation contract are DOM-test-pinned; new
  row content must go through the reserved attention-marker slot or a ruling.
- Attention highlight must stay class-derived (never an id snapshot) — review finding 3.
- Bulk end must keep the naming preview; the palette mirrors carry counts + names in the command
  title itself (`SessionsView`).

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Row anatomy, hierarchy render, bulk end, attention strip, banner, footer, toggles. | L342-L744 | [SessionRail.tsx](SessionRail.tsx) |
| The pure model/rollup/join derivations this renders. | L17-L464 | [../../data/railModel.ts](../../data/railModel.ts) |
| The single dot renderer + grammar. | L38-L49 | [StateDot.tsx](StateDot.tsx) |
| The view deriving props and wiring focus + palette mirrors. | L206-L344 | [SessionsView.tsx](SessionsView.tsx) |
| The terminate + landed-cleanup routes the End/bulk paths post to. | — | [../../data/terminal.ts](../../data/terminal.ts) |
| The poll-health + tree-toggle store slices. | L107-L172 | [../../data/sessionCockpitStore.ts](../../data/sessionCockpitStore.ts) |
| The jsdom suite: state matrix, anatomy order, model-leakage negative, hierarchy, attention, joins, completed/bulk, footer honesty, cross-surface dot. | L61-L352 | [SessionRail.test.tsx](SessionRail.test.tsx) |

## Update History

- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S4 (R5/R6/R8/R12/R13/R15/R16/R17, incl. fix
  round 1 findings 3 + 5): the ruled-hierarchy rail renderer — anatomy-exact rows with
  tooltip-backed truncation, hairline leaf clusters, collapsed completed folders, master+sprint
  bulk end with naming previews, the zero-state-suppressed attention strip with live-derived
  highlight expiry, gate/brief markers in the reserved slot, the poll-stale banner, the anchored
  bus footer, and the provenance-only spawn-tree toggle. Verification metadata pinned to the leaf
  base until closeout stamps the L2 code commit.
