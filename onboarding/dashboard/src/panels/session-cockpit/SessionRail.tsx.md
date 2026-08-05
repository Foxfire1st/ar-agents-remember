# dashboard/src/panels/session-cockpit/SessionRail.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/SessionRail.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-26T15:40+0200 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

- **Props vs store** cit:(["export function SessionRail"], dashboard/src/panels/session-cockpit/SessionRail.tsx:487-487): `model`/`rollup` arrive as PROPS — derived once in
  `SessionsView` and shared with the palette commands (one derivation, two surfaces; same-snapshot
  consistency, worker flag 5) — while `sessions`, the tree toggle, poll health, the projection
  slices (`taskDocuments`, `lifecycles`, `agentPickups`, `supervisorHeartbeat`), the lifecycle
  notices (`cleanupOutcome`), and the harvest map (`usePtyHarvest`) are store reads.
- **Row anatomy `renderRow`** (RULED R6 / **RV-2 responsive redesign**): the row is
  now TWO groups inside a `flex-wrap: wrap` `rowShell` — a **LABEL group** (`rowLabelGroup`: dot ·
  role(3) · title · attention/markers · status chip; `flex:1 1 auto; min-width:0; overflow:hidden`) and
  an **ACTION group** (`rowActionGroup`: End, or the armed confirm/cancel, or the end-failure alert;
  `flex:0 1 auto; min-width:0`). When the two cannot share one line at a narrow rail, the ACTION group
  wraps WHOLE to a second line — the confirm/cancel controls stay single-line and reachable inside the
  `overflow:hidden` aside at EVERY width down to the 12% collapse threshold, never letter-wrapping,
  clipping, or overflowing. Priority when squeezed: **actions > chip > inline copy**. `rowTitle` is now
  the truly-absorbing segment (`flex:1 1 auto; min-width:0` — the old `min-width:3.5rem` floor is GONE;
  the floor forced the row past the aside), eliding to `…` with the full label in `railRowTooltip`. The
  status chip (`statusChip`) is `flex:0 1 auto` — whole-word when there is room (R2: `turn-ended` ~72px
  under the 7rem ceiling), elidable after the title yields, and **DROPPED ENTIRELY while the row is
  armed or showing an end-failure** (`showChip = chip && !isArmed && !hasEndFailure`) because the
  confirm copy already carries the state, so the two controls always fit. Status chips carry the
  grammar's status vocabulary ONLY — the DOM-negative test proves `resolvedModel`/`resolvedEffort`
  render NOWHERE in the rail. The `data-slot="attention-marker"` slot carries the two-state brief marker
  (✉, R8), held-gate badge (R13), and the `set!` marker when `hasUnackedSetAttention` finds
  unsupported, clamp, unknown, or pair-failure evidence. Its accessible name directs the user to the set
  ledger; only an explicitly labelled `mark seen` action clears it. Viewing/focusing never does. The
  `input?` chip's tooltip carries the pending question's prompt preview (R16) — read
  from `sessionPendingInteractionPayload(session)` (review N1; the parent's singular slot first, else the first multiplexed sub-agent entry — L651) and prefixed with the
  adapter-bound agent label when present (`<agentLabel>: <prompt>`, L654-L656, tooltip at
  L780-L782), so the tooltip never implies the parent is asking. Geometry is e2e-pinned
  (`cockpit.spec.ts`) at 1440 / 1100 / 900 / min-rail: armed confirm 55×15, cancel 40×15, single-line,
  both fully inside the aside, chip dropped.
- **Accessible state dot (R8)** cit:(["export function StateDot"], dashboard/src/panels/session-cockpit/StateDot.tsx:38-38): the rail supplies `ariaLabel="state: <word>"`
  to the shared `StateDot`, making the truncation-surviving signal a named image. Header dots stay
  hidden because the visible state word already sits beside them.
- **Honest single-End flow (R5)** (L381-L385, L424-L432, L548-L614): the End segment renders
  on EVERY row (live `End`, dormant `✕`), but clicking now ARMS an inline confirm that NAMES
  session · leaf · state (`terminateConfirmCopy` — arming alone never kills); confirm runs
  `executeEnd` → `endSessionDetailed` (the residual-keeping path in `data/sessionLifecycle`;
  the exported `endSession` now takes the `OpenSession` — the rail is its only caller). A FAILED
  terminate POST (review finding 4) renders a `role="alert"` `end failed: <verbatim server
  words>` row with retry + dismiss, REPLACING the End segment until resolved — never a silent
  disarm; distinct from stop residuals, which are informational facts about SUCCESSFUL
  terminations. **R9 demotion:** the `endButton` now carries DEMOTED weight —
  `color: muted` by default, warming to `alarm` only on hover / keyboard focus / the selected row (red
  on every row was six alarms shouting, diluting the danger signal). The `rowShell` gained a `_hover`
  border feedback (an amber-grid mix) — the row had NO approach feedback before the click that arms End.
  The confirm/cancel/End controls (`bulkButton`, `doneToggle`, `endButton`) all hold `flex:none` +
  `whiteSpace:nowrap` so they never crush into vertical letter columns (R1/V12). The
  `terminateConfirmCopy` em-dash collision (`state — —`) is fixed in `lifecycleCopy.ts`.
- **Legacy-raw harvest markers (R7)** (L464-L471, L499-L514): a pending bell renders a warn
  marker chip in the attention slot with a text equivalent ("terminal bell — the vendor TUI
  rang"), cleared by focusing the seat (PtySurface acknowledges); harvested OSC title/turn hints
  join the row TOOLTIP as clearly-labeled `pty title:` / `pty hint:` parts — NEVER the grammar
  dot (the dot stays pure grammar, test-pinned).
- **Cleanup-outcome note (R5)** cit:(["export function cleanupOutcomeCopy"], dashboard/src/panels/session-cockpit/lifecycleCopy.ts:40-40): the landed-cleanup route's OWN outcome —
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
- **Bus footer** (L836-L851, R8): anchored numbers from `supervisorHeartbeat`. **RV-4/R4 + R5:** the both-zero inbox collapses to a calm `inbox clear` (the anchored `N pending / M
  redeliverable` pair renders only when there is something to anchor); the heartbeat/cutoff are
  HUMANIZED via `humanizeDuration` (`heartbeat 2 s / stale cutoff 1 m 0 s`, never the raw
  `570724.69163s / 86400s`), with the raw seconds kept in the tooltip. Renders the truth ("supervisor
  has not ticked in this workspace") when null — never fake numbers.
- **Tree toggle** (L808-L815, R8): reads as a view TOGGLE, not a bare taxonomy noun
  — `⇄ role view` ↔ `⇄ tree view` with `aria-pressed` + a both-states tooltip + `whiteSpace:nowrap`
  (V12, never `rol/e vie/w`). Swaps to `buildSpawnTree` rows indented by spawn depth (provenance
  inspection only); persisted per user via the cockpit store.
- **Leaf caption (V26)** (`leafCaption`): a long leaf id (`260715_#2067_react-data-
  testids-01`) now truncates at the END with the full value in the cluster `title` (`display:block;
  min-width:0; overflow:hidden; text-overflow:ellipsis; white-space:nowrap`) — never breaking mid-word
  down the narrow rail.
- **Zero state** (L804-L807, R9): an EXPLAINED empty rail ("no sessions — launch one from Chats;
  the cockpit launcher lands in the Chats surface"), never an unexplained blank.

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
- The ruled anatomy order is DOM-test-pinned; new row content goes through the reserved
  attention-marker slot or a ruling. **RV-2 truncation/wrap contract:** the row is a
  two-group `flex-wrap:wrap` layout; the ACTION group (End/confirm/cancel) stays single-line + reachable
  at EVERY rail width (wrapping whole to line 2 when tight), the title elides first, the chip elides next
  and is dropped entirely while armed — pinned by the 4-width `cockpit.spec.ts` geometry e2e (jsdom has
  no layout, so this is an e2e pin, not a vitest one).
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Row anatomy, accessible dots, set/harvest markers, End flows, hierarchy, bulk end, strip, banner, cleanup note, footer, toggles. | "export function SessionRail" | dashboard/src/panels/session-cockpit/SessionRail.tsx:487-487 |
| The pure model/rollup/join derivations this renders. | "export function buildRailModel" | dashboard/src/data/railModel.ts:131-131 |
| The payload selector + agent label the `input?` chip tooltip resolves (N1). | "export interface OpenSession" | dashboard/src/data/sessions.ts:28-28 |
| The adapter-bound agent label the tooltip prefixes. | "export interface InteractionQuestionOption" | dashboard/src/data/interactionAnswer.ts:29-29 |
| The single dot renderer + grammar. | "export function StateDot" | dashboard/src/panels/session-cockpit/StateDot.tsx:38-38 |
| The view deriving props and wiring focus + palette mirrors. | "export const SessionsView" | dashboard/src/panels/session-cockpit/SessionsView.tsx:1336-1336 |
| The detailed terminate/cleanup flows + notice store the End paths run through. | "export function startRetireResidualSweep" | dashboard/src/data/sessionLifecycle.ts:136-136 |
| The confirm + cleanup-outcome copy. | "export function cleanupOutcomeCopy" | dashboard/src/panels/session-cockpit/lifecycleCopy.ts:40-40 |
| The harvest store + hint words the markers/tooltips read. | "export interface PtyHarvest" | dashboard/src/data/ptyHarvest.ts:21-21 |
| Shared set-attention predicate feeding the `set!` marker. | "export function deriveSetChips" | dashboard/src/data/setChips.ts:58-58 |
| The poll-health + tree-toggle store slices. | "export type EvidenceTier" | dashboard/src/data/sessionCockpitStore.ts:18-18 |
| The jsdom suite: state matrix, anatomy order, model-leakage negative, hierarchy, attention, joins, completed/bulk, footer honesty, cross-surface dot, + the End/cleanup/harvest block. | "every row's dot carries exactly the stateGrammar visual for that seat" | dashboard/src/panels/session-cockpit/SessionRail.test.tsx:77-96 |

## Sole Chats Rail Candidate Delta

Becomes the sole Chats rail replacing SessionList/sessionGroups rendering. It consumes `railModel`, renders role/spawn/master/leaf/completed truth and attention rollups, preserves exact terminate/cleanup targets, and enables browser rendering optimization only beyond 50 actually emitted rows.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Single-Seat End And Decluttered Rail Maintenance

Single-seat End now executes immediately; only bulk end retains a confirmation because it acts on
multiple seats. Failure retry/dismiss remains visible. The rail subscribes only to shown poll facts
instead of heartbeat age, and its former bus footer is removed because inbox and supervisor facts
already have their authority in the top bar and detailed inspector.

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B21 curator: replaced the superseded `(L…)`
  prose citations and the `n/a` rows with exact anchors and fixer-generated ranges; exact
  non-fixing check returns zero findings.

- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: recorded the review-N1 tooltip asker fix — the
  `input?` chip's prompt preview now reads `sessionPendingInteractionPayload(session)` (parent's
  singular slot first, else the first multiplexed sub-agent entry) and prefixes the adapter-bound
  agent label (`<agentLabel>: <prompt>`) so the tooltip never implies the parent is asking. Also
  refreshed the self-reference range to the current 1115-line source. Source uncommitted;
  closeout re-stamps verification.

- 2026-07-24T13:17:17Z — Curator: corrected single-end behavior, narrowed poll subscriptions, and
  removed duplicated rail-bus chrome; verification fields remain pre-commit.

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: recorded the responsive rail-row redesign (RV-2) —
  the `rowShell` is now a `flex-wrap:wrap` LABEL-group + ACTION-group layout where the action group
  wraps whole to a second line and stays single-line/reachable at 1440/1100/900/min-rail (4-width
  `cockpit.spec.ts` geometry pin); the `rowTitle` min-width floor was removed so it truly absorbs; the
  status chip elides and is DROPPED while armed (confirm copy carries the state). Also: R9 End demotion
  (muted→alarm on hover/focus/selected) + row hover feedback; R1/V12 nowrap on confirm/cancel/toggle;
  R8 `⇄ role view / ⇄ tree view` toggle affordance; R5/RV-4 humanized + `inbox clear` bus footer; V26
  end-truncated `leafCaption`. No model/effort leakage introduced. Verification pinned to the leaf base
  (`352d5cd`) until closeout stamps the candidate commit.
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
