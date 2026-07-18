# dashboard/src/panels/session-cockpit/SessionRail.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/SessionRail.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f`       |
| lastVerifiedCommitDate | 2026-07-18T07:47:42+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The sole canonical Chats rail, replacing the retired SessionList/sessionGroups renderer. It consumes
data/railModel.ts to render the ruled role/spawn hierarchy, master/leaf clusters, completed folders,
attention rollups, gates/briefs, poll health, bus summary, and provenance tree toggle. Lifecycle
actions keep exact per-row terminate failures/confirmation and exact landed-cleanup target/outcome
truth. Browser rendering optimization begins only above 50 rows actually emitted by the selected
rail view.

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
  The `data-slot="attention-marker"` slot carries the two-state brief marker (✉, R8), held-gate
  badge (R13), and FEUI-L4's `set!` marker when `hasUnackedSetAttention` finds unsupported,
  clamp, unknown, or pair-failure evidence. Its accessible name directs the user to the set
  ledger; only an explicitly labelled `mark seen` action clears it. Viewing/focusing never does.
  The `input?` chip's
  tooltip carries the pending question's prompt preview (R16).
- **Accessible state dot (L4 R8)** (L491-L501): the rail supplies `ariaLabel="state: <word>"`
  to the shared `StateDot`, making the truncation-surviving signal a named image. Header dots stay
  hidden because the visible state word already sits beside them.
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
- Set attention is presentation of existing ledger/pair evidence only; the rail never
  acknowledges it and never renders requested/effective model or effort values.
- Attention highlight must stay class-derived (never an id snapshot) — review finding 3.
- Bulk end must keep the naming preview; the palette mirrors carry counts + names in the command
  title itself (`SessionsView`).
- Single End must keep the arm→confirm discipline (arming never kills) and a failed terminate
  must stay verbatim-visible with retry — never a silent disarm.
- NO turn theater renders per rail row — the WorkingLine is its single home (R6).

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
| Row anatomy, accessible dots, set/harvest markers, End flows, hierarchy, bulk end, strip, banner, cleanup note, footer, toggles. | L348-L889 | [SessionRail.tsx](SessionRail.tsx) |
| The pure model/rollup/join derivations this renders. | L17-L464 | [../../data/railModel.ts](../../data/railModel.ts) |
| The single dot renderer + grammar. | L38-L49 | [StateDot.tsx](StateDot.tsx) |
| The view deriving props and wiring focus + palette mirrors. | L206-L344 | [SessionsView.tsx](SessionsView.tsx) |
| The detailed terminate/cleanup flows + notice store the End paths run through. | L120-L191 | [../../data/sessionLifecycle.ts](../../data/sessionLifecycle.ts) |
| The confirm + cleanup-outcome copy. | L13-L47 | [lifecycleCopy.ts](lifecycleCopy.ts) |
| The harvest store + hint words the markers/tooltips read. | L51-L126 | [../../data/ptyHarvest.ts](../../data/ptyHarvest.ts) |
| Shared set-attention predicate feeding the `set!` marker. | L1-L232 | [../../data/setChips.ts](../../data/setChips.ts) |
| The poll-health + tree-toggle store slices. | L107-L172 | [../../data/sessionCockpitStore.ts](../../data/sessionCockpitStore.ts) |
| The jsdom suite: state matrix, anatomy order, model-leakage negative, hierarchy, attention, joins, completed/bulk, footer honesty, cross-surface dot, + the L6 block. | L61-L473 | [SessionRail.test.tsx](SessionRail.test.tsx) |

## FEUI-L8 Reviewed Candidate Delta

Becomes the sole Chats rail replacing SessionList/sessionGroups rendering. It consumes `railModel`, renders role/spawn/master/leaf/completed truth and attention rollups, preserves exact terminate/cleanup targets, and enables browser rendering optimization only beyond 50 actually emitted rows.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T23:54+02:00 — 260715-FEUI-L7 aligned the rail's set-attention contract with the
  explicit `mark seen` action now shared by Evidence and background outcomes. Viewing/focusing
  stays non-acknowledging. Verification metadata remains pinned to the leaf base until closeout.
- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 R6/R8 filled the reserved attention slot with the
  worded `set!` marker for unacknowledged evidence and named every rail dot `state: <word>` for
  assistive technology. The rail remains model/effort-value-free and never acknowledges on its
  own. Verification metadata is pinned to the contract base pending code commit.
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
