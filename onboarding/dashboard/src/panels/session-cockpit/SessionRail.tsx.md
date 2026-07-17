# dashboard/src/panels/session-cockpit/SessionRail.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/SessionRail.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T04:20+02:00                           |
| lastVerifiedCommitHash | `7b62338310aff67ae8b66a450a52a1f1052137c4`       |
| lastVerifiedCommitDate | 2026-07-17T04:36:24+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **session rail** (260715-FEUI-L2 S4; L6 adds the honest lifecycle flows R5 + legacy-raw
harvest markers R7): renders the RULED role-driven hierarchy (spec §1.6b) — flat command spine,
indented per-leaf clusters with the active seat on top, per-master completed folders with
master+sprint bulk end — plus the fleet-attention strip (R12), gate badges (R13), the two-state
brief column (R8), the poll-health stale banner (R15), and the bus-summary footer (R8). The
orchestration-tree (spawn-edge) view stays available as a button/palette toggle for provenance
inspection only (R5). All derivations live in `data/railModel.ts`; this file is DOM + wiring.

## Code Commentary

### Logic

- **Props vs store** (L368-L389): `model`/`rollup` arrive as PROPS — derived once in
  `SessionsView` and shared with the palette commands (one derivation, two surfaces; same-snapshot
  consistency, worker flag 5) — while `sessions`, the tree toggle, poll health, the projection
  slices (`taskDocuments`, `lifecycles`, `agentPickups`, `supervisorHeartbeat`), the L6 lifecycle
  notices (`cleanupOutcome`), and the harvest map (`usePtyHarvest`) are store reads.
- **Row anatomy `renderRow`** (L455-L616, RULED R6): dot · role(3) · title · attention-slot ·
  status · End. The title is the flex segment (`min-width: 3.5rem` — ALWAYS survives); the status
  chip is the ONLY elidable segment (`flexShrink:1; min-width:0; max-width:7rem`); the full truth
  stays in the row tooltip (`railRowTooltip`). Status chips carry the grammar's status vocabulary
  ONLY — the DOM-negative test proves `resolvedModel`/`resolvedEffort` render NOWHERE in the rail.
  The `data-slot="attention-marker"` slot (R6's reserved slot, consumed by L4) carries the
  two-state brief marker (✉, R8) and the held-gate badge (R13, + `data-attention-gate` on the
  row). The `input?` chip's tooltip carries the pending question's prompt preview (R16).
- **Honest single-End flow (L6 R5)** (L381-L385, L424-L432, L548-L614): the End segment renders
  on EVERY row (live `End`, dormant `✕`), but clicking now ARMS an inline confirm that NAMES
  session · leaf · state (`terminateConfirmCopy` — arming alone never kills); confirm runs
  `executeEnd` → `endSessionDetailed` (the residual-keeping path in `data/sessionLifecycle`;
  the exported `endSession` now takes the `OpenSession` — the rail is its only caller). A FAILED
  terminate POST (review finding 4) renders a `role="alert"` `end failed: <verbatim server
  words>` row with retry + dismiss, REPLACING the End segment until resolved — never a silent
  disarm; distinct from stop residuals, which are informational facts about SUCCESSFUL
  terminations.
- **Legacy-raw harvest markers (L6 R7)** (L464-L471, L499-L514): a pending bell renders a warn
  marker chip in the attention slot with a text equivalent ("terminal bell — the vendor TUI
  rang"), cleared by focusing the seat (PtySurface acknowledges); harvested OSC title/turn hints
  join the row TOOLTIP as clearly-labeled `pty title:` / `pty hint:` parts — NEVER the grammar
  dot (the dot stays pure grammar, test-pinned).
- **Cleanup-outcome note (L6 R5)** (L755-L770): the landed-cleanup route's OWN outcome —
  `ended N · skipped M (session: reason)` via `cleanupOutcomeCopy` — renders as a dismissable
  `role="status"` row instead of dropping the skips.
- **Ruled hierarchy render** (L619-L681, L800-L834): spine rows flat; `renderMaster` — master box
  with label + dominant attention badge (`masterAttentionBadge`) + the master bulk-end control;
  managers flat at the top of the box; leaf clusters as `leafGroup` — indented 0.9rem with a FINE
  55%-grid hairline + margin, never heavy boxes (RULED); the completed folder collapsed by
  default (`▸ completed · N`, expandable per master); unattached (live + landed) in one plain
  group box.
- **Bulk end with honest preview** (L352-L356, L434-L453): arming (`✕ end N done` / sprint-level
  `✕ end N completed`) swaps to an inline confirm that NAMES every removed session before
  executing (`bulkConfirm`); `endLanded` → `endLandedDetailed` (L6: the detailed flow closes
  only backend-confirmed rows, rehydrates excluding them, AND records the route's honest outcome
  — closed + skipped with reasons — for the rail note). No blind bulk delete path exists.
- **Attention strip** (L683-L736, R12): renders NOTHING at zero state (`attentionZeroState` —
  working alone is not attention); each count is a filter button that focuses the class's
  longest-waiting seat (`jumpToAttentionTarget` over a single-class rollup) AND highlights the
  set. The highlight stores the clicked CLASS (`highlightKind`) and derives the ring set from the
  LIVE rollup each render — a ring expires the moment the seat's state resolves (fix round 1,
  finding 3).
- **Poll-health banner** (L749-L754, R15): `pollHealth.healthy === false` ⇒ the amber "catalog
  poll stale — N beats missed; rows may be frozen" banner.
- **Bus footer** (L836-L851, R8): anchored numbers from `supervisorHeartbeat` — `inbox N pending /
  M redeliverable`, `heartbeat Xs / stale Ys` with the 10 s sweep bound in the tooltip; renders
  the truth ("supervisor has not ticked in this workspace") when null — never fake numbers.
- **Tree toggle** (L808-L815): swaps to `buildSpawnTree` rows indented by spawn depth (provenance
  inspection only); persisted per user via the cockpit store.
- **Zero state** (L804-L807, R9): an EXPLAINED empty rail ("no sessions — launch one from Chats;
  the cockpit launcher lands in L5"), never an unexplained blank.

### Conventions

Co-located Panda `css`/`cva` on podracer tokens; `data-testid` on every assertable element
(`rail-row-*`, `rail-dot-*`, `rail-status-*`, `rail-end-*`, `rail-attention-*`, `rail-master-*`,
`rail-cluster-*`, `rail-bulk-*`, `rail-done-toggle-*`, `rail-tree-toggle`, `rail-poll-stale`,
`rail-bus-footer`, `rail-zero-state`); rows are `role="button"` with Enter/Space handling; the
rail root carries `data-focus-target` (design §5.3 — always present, even empty).

### Invariants And Boundaries

- The rail renders MODEL truth only: no model/effort anywhere (R6), no fabricated latency, no
  invented states — chips/words come exclusively from `stateGrammar`; harvested hints live in
  the TOOLTIP, clearly labeled, never the dot.
- The ruled anatomy order and the only-status-elides truncation contract are DOM-test-pinned; new
  row content must go through the reserved attention-marker slot or a ruling.
- Attention highlight must stay class-derived (never an id snapshot) — review finding 3.
- Bulk end must keep the naming preview; the palette mirrors carry counts + names in the command
  title itself (`SessionsView`).
- Single End must keep the arm→confirm discipline (arming never kills) and a failed terminate
  must stay verbatim-visible with retry — never a silent disarm.
- NO turn theater renders per rail row — the WorkingLine is its single home (R6).

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Row anatomy, End confirm/failure, harvest markers, hierarchy, bulk end, strip, banner, cleanup note, footer, toggles. | L348-L854 | [SessionRail.tsx](SessionRail.tsx) |
| The pure model/rollup/join derivations this renders. | L17-L464 | [../../data/railModel.ts](../../data/railModel.ts) |
| The single dot renderer + grammar. | L38-L49 | [StateDot.tsx](StateDot.tsx) |
| The view deriving props and wiring focus + palette mirrors. | L206-L344 | [SessionsView.tsx](SessionsView.tsx) |
| The detailed terminate/cleanup flows + notice store the End paths run through. | L120-L191 | [../../data/sessionLifecycle.ts](../../data/sessionLifecycle.ts) |
| The confirm + cleanup-outcome copy. | L13-L47 | [lifecycleCopy.ts](lifecycleCopy.ts) |
| The harvest store + hint words the markers/tooltips read. | L51-L133 | [../../data/ptyHarvest.ts](../../data/ptyHarvest.ts) |
| The poll-health + tree-toggle store slices. | L107-L172 | [../../data/sessionCockpitStore.ts](../../data/sessionCockpitStore.ts) |
| The jsdom suite: state matrix, anatomy order, model-leakage negative, hierarchy, attention, joins, completed/bulk, footer honesty, cross-surface dot, + the L6 block. | L61-L473 | [SessionRail.test.tsx](SessionRail.test.tsx) |

## Update History

- 2026-07-17T04:20+02:00 — 260715-FEUI-L6 (R5/R7; review finding 4 fixed in-leaf): single End
  now arms an inline honest confirm naming session · leaf · state and executes through
  `endSessionDetailed` (`endSession` signature: id → `OpenSession`; rail-only caller); a failed
  terminate POST renders verbatim with retry/dismiss as a `role="alert"` row; bulk end routes
  through `endLandedDetailed` and the route's own closed+skipped outcome renders as a
  dismissable note; legacy-raw bell markers (text-equivalent, cleared on focus) and labeled
  title/turn-hint tooltip parts joined the rows — the grammar dot stays pure.
- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S4 (R5/R6/R8/R12/R13/R15/R16/R17, incl. fix
  round 1 findings 3 + 5): the ruled-hierarchy rail renderer — anatomy-exact rows with
  tooltip-backed truncation, hairline leaf clusters, collapsed completed folders, master+sprint
  bulk end with naming previews, the zero-state-suppressed attention strip with live-derived
  highlight expiry, gate/brief markers in the reserved slot, the poll-stale banner, the anchored
  bus footer, and the provenance-only spawn-tree toggle. Verification metadata pinned to the leaf
  base until closeout stamps the L2 code commit.
