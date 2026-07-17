# dashboard/src/ — Mission-Control Cockpit Frontend Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/`                                 |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-07-17T04:20+02:00 |
| lastVerifiedCommitHash | `7b62338310aff67ae8b66a450a52a1f1052137c4`       |
| lastVerifiedCommitDate | 2026-07-17T04:36:24+02:00|
| governingOverview      | `../../overview.md`                              |

## Governing Overview

[agents-remember root overview](../../overview.md)

## Purpose

`dashboard/src/` is the **browser-dashboard frontend** (the 3.0 mission-control cockpit) — a
Vite + React 19 + TypeScript-strict app that renders the observer projection served by the
`serving/` layer. It renders reopened leaves (L11) as ordinary planned task rows — leaf identity is
stable across reopens, so no dashboard-side reopen special-casing exists anymore. It
is a near-read-only cockpit whose **interactive surfaces** are now
gate responses (`GateResponder` records durable Yes/No gate decisions through `data/actions` and
routes Chat/informational responses through hosted chats or the external operator inbox) and the
Chats terminal (slice 6e — an xterm.js view over the Mode B2
`/api/terminal` WebSocket): a persistent top bar + left rail (attention queue + lifecycle list) + a
switchable centre viewport (operations / file viewer / engine room / memory mirror / topology / hangar / chats) +
a right-rail event river + a bottom mode bar (note 06 model C). The unit is the lifecycle (note 01).
**260707-HFX2-L2 (R5)** adds a second top-bar liveness indicator beside the boot-time `servingBuild`
stamp: `SupervisorHeartbeatBadge` (`cockpit/Cockpit.tsx`) renders the serving daemon's supervisor
sweep's own tick age (`store.ts`'s `supervisorHeartbeat` field, mirroring `types/projection.ts`'s
app-injected `SupervisorHeartbeat` shape) — red/pulsing past its staleness cutoff, silent when the
supervisor has never ticked (opt-in autostart) rather than a false alarm. **260707-HFX2-L8 (R6)**
extends that same header signal with pending/redeliverable inbox backlog counts and last sweep duration.

## The Layered Architecture (slice 5d)

Styling was re-architected from a single ~1,200-line global `tokens.css` into the layered blueprint:

- **Tokens** — `panda.config.ts` holds the OKLCH podracer palette (note 08) as typed Panda tokens;
  `styles/tokens.css` keeps the matching `:root` CSS vars (the global var layer used by `index.css`
  base + a few Panda text-shadows).
- **Primitive recipes / component styling** — **Panda CSS** (build-time, zero-runtime atomic CSS):
  each component carries co-located `css()` / `cva()` styles; `grammar/Panel.tsx` is the shared
  panel chrome (shell + sticky head). Generated runtime lands in `styled-system/` (gitignored,
  outside memory scope).
- **Behavior** — **React Aria** (`react-aria-components`): the mode bar + the lifecycle pivot are
  `ToggleButtonGroup`s; the lifecycle list is a `ListBox`, and the Chats session switcher is a
  `GridList` (arrow-nav + type-ahead — a `GridList`, not a `ListBox`, so each session row's action
  stays keyboard-reachable, slice 6e-2c); the context composer is a `TextField`/`TextArea` + `Button`
  (slice 6e-3). Panda conditions
  (`_selected`/`_focusVisible`) target React Aria's `data-*` state, so the CRT look is unchanged.
- **Effects** — `index.css` `@layer effects`: the global `crt-overlay` (scanlines + vignette +
  flicker) and the `?effects=off` determinism freeze, isolated from components. *(Slice 05k removed the
  engine-room canvas `@keyframes` that 5g–5i had parked in this layer — that motion now lives on GSAP/Motion
  in `panels/engine-room/`. The last engine-room keyframe, `powerup` (a 05k/05f carve-out for the
  indexing→nominal engine flash), was then removed too — it is now a **Motion opacity pulse** on the charge
  rect — so only the app-wide `crt-overlay`/`flicker`/`pulse` keyframes remain here.)*
- **Layer order** — `index.css` declares `@layer reset, base, effects, webtui, tokens, recipes,
  utilities`. The `webtui` slot (260715-FEUI-L1 S1, OQ-D = **adopt WebTUI**) hosts the scoped
  WebTUI skin for the sessions cockpit: `styles/webtui.css` is THE one mapping file — it imports
  the used `@webtui/css@0.1.9` (exact pin) dist files with `layer(webtui)` and maps WebTUI's
  palette vars onto the podracer tokens (one color system) — while `postcss-prefix-selector`
  (options in `webtui-scope.config.cjs`, wired in `postcss.config.cjs`) confines every WebTUI rule
  under `[data-view="sessions"]` at build time. Slotted between `effects` and `tokens` so Panda
  always wins a conflict and the unlayered effects freeze stays sovereign; the four falsifiable
  spike assertions live on as `test/webtuiSpike.test.ts`.

## Route Model

- `main.tsx` — the entry: mounts `<App>`, imports `index.css` + `styles/tokens.css` +
  `styles/webtui.css` (260715-FEUI-L1), sets the `effects=off` determinism flag.
- `App.tsx` — hand-rolled routing (D6): production serves `<Cockpit>`; `/dev/*` lazy-loads the
  DEV-only harness (statically dropped from the production bundle).
- `cockpit/Cockpit.tsx` — the model-C shell (stream wiring + layout + top bar + mode bar); slice 5f S1
  makes the machine-map views (Engine Room / Topology) **full-bleed** (rails hidden, §4.1), render-tested
  by `cockpit/Cockpit.test.tsx`. Slice 6e registers the full-bleed **Chats** view, and Task 11 derives
  the selected lifecycle id so chat creation, highlight delivery, and gate responses share the same
  lifecycle/session identity. Task 29 S7 hides the former **Lifecycle Flow** tab from the cockpit
  navigation and removes the `flow` view from the shell; `panels/FlowTab.tsx` remains dormant source
  material only. Operations-integration L2 registers the full-bleed **File Viewer** view
  (`panels/file-viewer/`) between Operations and Engine Room, **kept mounted** (CSS-hidden) like Chats so
  its repo/scope/open-file/tree state survives a tab switch. Operations-integration L4 adds a **Change-Set
  Viewer** TAKEOVER (a `changeSet` state): a `DetailPanel` change-set button replaces the railed Operations
  body with a full-bleed `<ChangeSetViewer>` (a back link restores the rails) — a task-scoped screen, not a
  standing view. 260703-L17 adds the second such takeover: a `notesOpen` state renders the full-bleed
  **Notes Reader** (`panels/notes-reader/`) from `DetailPanel` note links or the TaskNotes entry list; the
  two takeovers are mutually exclusive, and the reader is **kept mounted** after Back (File-Viewer-style)
  so the selected note survives within the session. 260715-FEUI-L1 registers the newest full-bleed
  view, **Sessions** (`panels/session-cockpit/`, last in the mode bar), as the fourth persistent
  keep-alive layer (`sessionsLayer = chatsLayer` — display/aria-hidden toggle, never unmounted, so
  the future xterm buffers/WebSockets survive switches); its `active` prop gates the view's
  window-level keyboard layer so the hidden layer never grabs keys.
- `test/` — the vitest (jsdom) bootstrap: `setup.ts` stubs `matchMedia`/`ResizeObserver` + the SVG geometry
  APIs jsdom omits (`getBBox`/`getTotalLength`/`getPointAtLength`, for the engine-room GSAP DrawSVG/MotionPath
  plugins — 05n) + `scrollIntoView` (cmdk, 260715-FEUI-L1) for
  component-render tests (the rest of the suite — `smoke`, `contract`, and the `data/` store+selector
  tests — is pure logic). `test/webtuiSpike.test.ts` (260715-FEUI-L1) keeps the four falsifiable
  WebTUI-adoption assertions running against the exact shared build configuration.
  `test/fixtures/` (260715-FEUI-L2) is the NEW shared-fixture home: `catalogRows.ts` — the
  full-wire-shape catalog builder + the mockup-mirroring `FLEET` scenario the rail/model suites
  run on (to be shared with the L3 fixture pack); 260715-FEUI-L6 APPENDS the `L6_*` rows
  (controlled/legacy-raw archetypes, choices/freetext/unrepresentable interactions, retired-with-
  stop-error, terminate-with-residual) after a byte-identical `FLEET`.
- `grammar/` — the shared primitives library (`Panel`, `ModeBar`, `Dot`, `Affordance`,
  `ProgressFill`, `TokenGauge`, `Markdown`, and — 260703-L14 — `RankBadge`, the V4 chevron rank
  insignia for the orchestration/management command tiers); see
  [grammar/overview.md](grammar/overview.md).
- `panels/` — the cockpit panels (incl. the slice-6e **Chats** terminal view + its lazy `Terminal`
  xterm wrapper + the 6e-2c `SessionList` session switcher, plus Task 11's shared `GateResponder`
  used by the detail panel, engine-room diagnostics, and Hangar worktree gates); `FlowTab.tsx` remains
  present but unreferenced after Task 29 S7 hides the Lifecycle Flow tab. Operations-integration L2 adds
  the **`panels/file-viewer/`** sub-route — the File Viewer centre tab (a read-only code+onboarding
  dual-pane over the L1 files API) + the reusable `FilePane`/`DualPane` the Change-Set Viewer (L4) will
  reuse; L4 then adds the **`panels/changeset/`** sub-route — the Change-Set Viewer screen (a read-only
  `@codemirror/merge` diff over the L3 change-set API, reusing the L2 `FilePane`). 260703-L17 adds the
  **`panels/notes-reader/`** sub-route — the Notes Reader takeover (rail = the master's notes from the
  unchanged L9 `/api/notes/list`, content pane = the same `DualPane`; `TaskNotes.tsx` shrinks to the
  compact entry list that opens it). 260715-FEUI-L1 adds the **`panels/session-cockpit/`**
  sub-route — the Sessions cockpit view shell (rail/stage/inspector `PanelGroup` + narrow rules +
  the ~80-col floor chip, the non-portal cmdk `CommandPalette` with the commands/keys pages, and
  the `useKeyboardZones` tinykeys binding), whose root carries `[data-view="sessions"]` (the
  WebTUI scope root). See
  [panels/overview.md](panels/overview.md).
- `data/` — the Zustand store, pure selectors, SSE stream wiring, the gate-action client
  (`actions.ts` POSTs targeted `gateId`/`note` decisions to `/api/actions/{verb}`, can omit `target`
  for gate-id-only cancel cleanup and targetless actionable-drift dismissal, and distinguishes stale
  gates from no-open-gate), the external-inbox client (`operatorInbox.ts` -> `POST
  /api/operator-inbox` for message-only Chat, agent-to-agent inbox rows with role/message/artifact
  metadata, and missing-hosted-session gate notifications plus `/api/operator-inbox/{entryId}/dismiss`
  for stale pickup-warning deletion), the Mode B2 terminal WebSocket
  client (`terminal.ts`, slice 6e; Task 22 also lists/terminates durable catalog rows, sends
  opener labels/lifecycle ids, and exposes a nullable catalog fetch for sync), and the open-terminal **session registry** store (`sessions.ts`,
  slice 6e-4 — now also the Task 11 lifecycle-tagged hosted-chat routing table for direct gate
  responses, the slice-6f cockpit-wide inject seam, and the Task 22 catalog hydration/status plus
  per-prefix label-reuse and cross-tab catalog-invalidation layer; the L6 follow-up adds a
  draft-paste handoff seam that inserts leaf context into the selected hosted chat without submitting it,
  and L9 adds `"leaf"` catalog invalidations so open tabs can rehydrate hosted-chat leaf moves) +
  the cockpit text-selection hook
  (`selection.ts`, slice 6f; since L8 a selection anchored inside a task reader marked
  `data-task-leaf-key` carries that qualified `leafKey`, the signal the direct leaf-chat highlight
  paste resolves its target from). HFX-L6 extends the role-aware session grouping/chip inputs so
  architect and curator spawn-role provenance can ride the same Chats sidebar model as orchestrator,
  manager, worker, strategist, designer, and reviewer sessions. The serving **read clients** `files.ts` (the L1 files API, L2),
  `changeset.ts` (the L3 change-set API, L4), and `notes.ts` (the agent-orchestration L9
  coordination-notes API — `listNotes`/`readNote` plus the pure conservative
  `resolveNoteReference` behind the task reader's reference links) are same-origin typed wrappers
  sharing one `getJson`/`qs`
  transport + `FilesApiError`, feeding the File Viewer + Change-Set Viewer + the task reader's
  notes view; they hold no store state. Task
  29 S7 tracks a raw-stream hydration flag from the backend
  `ready` event and applies optimistic attention suppression while dismiss/clear POSTs are pending; Task
  34 then bounds the raw Event River store (`store.ts`) to a **sliding window** of the newest ~2000 rows
  (memory-bounded rather than unbounded session growth), which `EventRiver` virtualizes over so there is
  still no hard display cap.
  **260703-L15 (long-session memory) adds `servedAges.ts`** (+ unit suite), the client half of the
  change-gate volatile-age contract: `VOLATILE_AGE_FIELDS` (the byte mirror of
  `serving/delta.py`'s set), `stableEquals` (deep equality that skips them), WeakMap arrival
  anchors (`stampServed`/`servedAgeSeconds`), and the `useNowMs` display ticker. `store.ts`'s two
  apply paths became identity-preserving and change-gated on `stableEquals` — an idle reconnect
  snapshot or redundant delta performs ZERO store writes and keeps every node identity (the
  long-session flatness contract, guarded by the 500-tick test in `store.test.ts`) — and the
  store carries the wire-optional `servingBuild` boot stamp the cockpit top bar renders muted
  (`cockpit/Cockpit.tsx` `ServingBuildStamp`, `types/projection.ts` `ServingBuild`). Age-display
  panels (Hangar / AttentionQueue / MemoryMirror / LifecycleList) advance served ages locally via
  `servedAgeSeconds` + `useNowMs` because the gated server no longer re-serves a node just to age
  it.
  260703-L11 adds `selectors.hasLiveWorktree`, the shared tasks-surface visibility rule
  (`EnclosureNode.codeWorktreeExists || memoryWorktreeExists` — server-stat'ed existence truth, never a
  cleanup-state proxy) consumed by both `Hangar` and `LifecycleList`.
  `taskIdentity.ts` centralizes lifecycle-visible labels plus typed
  Operations selection keys (`taskdoc:` / `series:` / `lifecycle:`), so task documents, series masters,
  and runtime-only lifecycles are not inferred from one overloaded id string; Event River also reuses
  it to show task document titles for lifecycle-only history rows before falling back to raw lifecycle
  ids. `taskHierarchy.ts` centralizes the structured parent-series join used by Operations and Detail:
  active leaf rows can show the child task document's own id and link back to the parent/root task
  without parsing task slugs or parent label strings; 260703-L14 adds its orchestration-command
  helpers (`isOrchestrationDoc` / `masterCommandNames` / `orchestratorParentKey` — the
  `orchestrates`-list match both command surfaces share). 260703-L14 also adds
  **`sessionGroups.ts`** (+ unit suite), the pure G1 command-tree derivation for the Chats sidebar:
  `groupSessions({sessions, taskDocuments, enclosures})` decks command-role/orchestration-claiming
  chats (only when an orchestration task exists — D3), groups leaf-claimed chats under their live
  master (via `hasLiveWorktree` + the case-insensitive leaf join), rolls landed/absent-enclosure
  chats into one archive, and leaves claim-less sessions ungrouped; master grouping is the chats
  pane's baseline in every run (owner-ratified, L14R-1) while the gold sprint deck stays
  orchestration-gated, and the tasks tab renders flat runs unchanged.
  **260715-FEUI-L1 adds the sessions-cockpit pure layer**: `commands.ts` (+ suite — the extensible
  command registry, the single options source behind the cmdk palette AND chord dispatch; honest
  L2/L4/L5 stubs routed through injected context actions), `sessionLayout.ts` (+ suite — the
  narrow-width edge-transition rules, the ~80-col floor approximation, and the ~280px rail
  percentage calibration), and the **`keymap/`** sub-route (see
  [data/keymap/overview.md](data/keymap/overview.md)) — the xterm-free keyboard-zone contract:
  `reserved.ts` (the PTY reserved set with five-source collision-verification records; the R6
  replacement pair Ctrl+Alt+PageUp/PageDown), `zones.ts` (`routeKey` + generic printable
  suppression + `slashOpensPalette`), `chords.ts` (zone-scoped chrome/composer tables), `focus.ts`
  (the F6 region cycle).
  **260715-FEUI-L2 adds the sessions-cockpit DATA layer** (all + unit suites): `catalogPoll.ts` —
  the 2500 ms terminal-catalog poll driver HOISTED out of `panels/Chats.tsx` (refcounted; every
  read records a poll-health beat; the poll is the AUTHORITATIVE session-row reconciler; the L8
  Chats cutover depends on this hoist); `seatEvents.ts` — the `/api/events` seat-event reconciler
  (retired/landed/renamed/turn-state-changed, riding the Event River's EventSource as a second
  consumer behind a per-connection backlog gate; pre-applies only, never resurrects/invents/
  regresses); `stateGrammar.ts` — THE one seat-state grammar (R14: state → word/chip/color/pulse;
  the ruled 2.4 s ease-in-out `pulseSlow`, blocked-on-human steady; the sev-3 chip-vocabulary
  width ruling is pending with the developer); `railModel.ts` — the pure RULED rail hierarchy
  (flat command spine / per-leaf clusters, active-first deterministic sort, completed folders),
  fleet-attention rollup + jump priority, gate/brief/critical-bus projection joins, smart-default
  focus, and question triage; and `sessionCockpitStore.ts` — the per-seat cockpit client store
  (per-kind pending sets, acknowledged set ledger that NEVER moves the five-tier launch evidence,
  composer shell, turn clock, per-pane freshness, client queue, poll health, the persisted
  orchestration-tree toggle, one-way view mirrors). `sessions.ts` gains the full-row mirror fields
  + the `patch` seat-event seam; `terminal.ts`'s catalog wire shape moved to
  `types/terminalCatalog.ts` (re-exported, import sites unchanged); `stream.ts`'s `connectEvents`
  gains `onInterrupt` (the reconnect signal the backlog gate re-closes on).
  **260715-FEUI-L6 adds the sessions-cockpit INTERACTION/LIFECYCLE data layer** (all + unit
  suites): `interactionAnswer.ts` — the SOLE structured-interaction answer path (finds the open
  `agent-question` gate by `packet.adapterInteraction.{sessionId,interactionId}`, answers via
  `POST /api/actions/approve` with the answer as the decision note — ZERO terminal writes;
  kind-awareness choices/freetext/unrepresentable; NOT-YET vs CANNOT copy split on the seat's
  `lifecycleId` — a gate on a lifecycle-less seat never projects, the gate-id-only projection is
  a recorded upstream ask); `sessionLifecycle.ts` — terminate/landed-cleanup DETAILED helpers
  that keep the response bodies (stop residuals + verbatim failure text) plus the
  `lifecycleNoticeStore` residual store (residuals outlive tombstoned rows) and the refcounted
  focus-INDEPENDENT `startRetireResidualSweep()` over every registry row (dedup by sessionId,
  dismissals stick across poll beats, reload resurfaces deliberately); and `ptyHarvest.ts` — the
  client-side-only legacy-raw harvesting store + pure OSC 133 / OSC 9;4 / title / bell parsers
  (observe-only; controlled panes get none). `actions.ts` gains `postGateDecisionDetailed`
  (verbatim error capture behind the retry affordances); `terminal.ts` gains the additive
  `onSocketState` option (per-pane `connected`/`dropped` freshness from the socket's own
  handshake/close; a deliberate `dispose()` reports nothing; `reconnecting` never fires — no
  auto-reconnect exists).
- `topology/` — the imperative constellation canvas + its pure model adapter. Task 33 reshapes it into an
  **active-enclosure** view: the constellation is now `workspace → source checkouts → active worktree
  enclosures (+ providers)`. The separate lifecycle/task rim is gone — each enclosure node folds in its
  1:1 lifecycle (id click-through, status, phase·state) — and `model.ts`'s new `activeTopologyInputs`
  seam filters the inputs to the served `activeWorktreeGroups` set so only live work renders (the shared
  store maps keep all-time history for other views). The worktree-group join is normalised to basenames
  (`groupKey`), fixing a latent task-12-S1 join bug. Task 12 S1 makes worktree-scoped provider satellites
  parent to the matching enclosure node via `ProviderNode.worktreeGroup` → `EnclosureNode.worktreeGroup`;
  task 12 S2 then lets repo-covered workspace providers parent to repo nodes via `ProviderNode.repoId`,
  while aggregate workspace providers remain on the workspace core. Repo-covered GrepAI nodes represent
  addressable `targetRepos` inside one aggregate provider instance, not separate per-repo provider
  processes.
- `types/projection.ts` — the frontend mirror of the served projection schema. `EnclosureNode` carries
  `enclosureId`, `leafId`, and `taskRoot` so frontend routes can distinguish a root task folder from a leaf
  enclosure contract without deriving path structure in the browser, and — 260703-L11 — the required
  `codeWorktreeExists`/`memoryWorktreeExists` existence-truth flags the tasks surface filters on. `TaskDocNode.lifecycleId?` is
  optional runtime attachment, while `TaskDocNode.id`, `TaskDocNode.createdAt`,
  `TaskSubTaskRefNode.createdAt`, and `SeriesNode`/`Analytics.series` mirror the active task-document
  and folder-keyed master aggregation surfaces so the detail panel can render masters, label authored
  leaves from the child task id, and order leaves from structured creation metadata rather than task-name
  prefixes. Task 21 adds `SeriesNode.seriesTokenTotal`, the server-composed aggregate displayed by
  master readers. **260707-HFX2-L13 F6** adds optional `TaskDocNode.bodyRevision` and
  `data/taskDocuments.ts`: the always-on task/series projection is summary-only, while the visible
  reader fetches one full body from `/api/task-document` and invalidates its cache by path + revision.
  **260712-TRH-L1** adds `data/useTaskDocumentBody.ts`, which owns that visible-body hydration and
  terminal availability state so `DetailPanel` can keep notes and eager change-set requests unmounted
  until complete task content either arrives or falls back honestly.
  Task 23/24/L3 adds `AttentionItem.gateId?` and `AgentPickupNode` /
  `Analytics.agentPickups` for attention clear and task-row waiting-for-agent/check-chat feedback,
  including sender/recipient roles, message kind, artifact path, and hosted-delivery state. 260703-L14 mirrors `TaskDocNode.orchestrates?` — the orchestration-command relation (non-empty only
  on an orchestration-task master; optional for pre-L14 persisted-projection compatibility). Task
  31 mirrors the provider boot-node `missing` state so Engine Room slots can distinguish expected-but-absent
  CGC/GrepAI roles from configured or observed provider rows. Task 33 mirrors the required top-level
  `WorkspaceProjection.activeWorktreeGroups: string[]` — the bounded active worktree-group set the
  Topology filters on — which `data/store.ts` carries (snapshot + a new `activeWorktreeGroups` delta case)
  and `data/stream.ts` threads through (`"activeWorktreeGroups"` added to `STATE_EVENTS`).
- `types/terminalCatalog.ts` (260715-FEUI-L2 R4) — the SECOND hand-maintained wire mirror: the
  FULL `TerminalCatalogEntry.to_json()` row (`serving/terminal_catalog.py` is the source of
  truth) — status/control/turn-state vocabularies, named-but-opaque `controlRaw` diagnostics
  keys, spawn/level provenance, the REQUESTED `resolvedModel`/`resolvedEffort` pair, and
  liveness/retirement/landing evidence. `data/terminal.ts` re-exports it
  (`TerminalSessionInfo` = `TerminalCatalogRow`), preserving import sites.
- `index.css` — the Panda entry + global reset/base/effects layers (260715-FEUI-L2 adds the
  ruled `pulseSlow` cockpit state-pulse keyframe beside `flicker`/`pulse`).
- `styles/tokens.css` — the `:root` design-token CSS vars (260715-FEUI-L1 adds `--muted`,
  mirroring the Panda `muted` token).
- `styles/webtui.css` — the ONE WebTUI mapping file (260715-FEUI-L1 S1): `layer(webtui)` imports of
  the used `@webtui/css` dist files + the `[data-view="sessions"]` token mapping + the scoped
  `:focus-visible` restore; build-time scoped by the prefixer.
- `dev/` — the DEV-only harness: `DevApp` (router — `/dev/bench`, `/dev/reference`, plus the orchestration-L0
  `/dev/flows` lifecycle-design canvas mounting `panels/FlowTab`), `Reference` (mc2 mount), `dev.css`, and — slice **5i**
  — the **scenario player** (`scenarios.ts` model + `ScenarioPlayer.tsx` transport) that `Bench` drives the
  real cockpit through phase-transition timelines with, plus `scenarios.test.ts`. (`fixtures.ts` gained the
  shared `engineRoomProjection` wrap.) `scenarios.ts` now also carries the recoverable failure-mode timelines —
  the `memory-block` ledger-gate (T3B) and the `stale-base` preflight→fast-forward (T1B, slice 05o) — each a
  named `Scenario` of frames wrapped from the engine-room fixtures, i.e. data within the existing `dev/` route
  model, not a shape change. Slice 05o (T7B–T18) extends this with six more failure-mode timelines —
  `seed-fault` (T9B GrepAI red fault→retry), `reindex-reroute` (T9C CGC seed refused→soft amber reindex),
  `provider-block` (T7B pre-contract plan→retry), `live-sync` (T12B memory moved→fast-forward merge),
  `integration-conflict` (T14C replay→terminal STOP), and `abandon` (T18 dissolve, no landing) — all the same
  `erFrame`-wrapped `Scenario` shape registered in `SCENARIOS`; the matching `types/projection.ts` additions
  (the `refusedPolarity` edge field + a `refused` state) are likewise additive, so the change stays data within
  the existing `dev/` (and `data/` projection-type) route model. The hand-authored fixtures default
  `analytics.series: []` beside `taskDocuments` so every dev projection satisfies the current served
  analytics shape. **260715-FEUI-L6 adds `/dev/pty-bench`** — `PtyRenderBench.tsx`, the in-repo
  PTY renderer-measurement harness behind the master OQ-B DOM-vs-webgl decision (N REAL
  `panels/Terminal` components in a `minmax(0,1fr)` grid fed by `lineLogFixture.ts`, the
  controlled line-log content verbatim-faithful to `harness_control_runner.py`, through the mock
  WS; rAF-delta stats on `window.__ptyBench`; a `?probe=serialize` reattach probe), driven by
  `dashboard/e2e/ptyRenderBench.mjs` (a plain node script, never collected by `npm run e2e`; its
  header records the headless-SwiftShader software-GL caveat).

## 260707-HFX2-L16 Rail And Reader Contract

The Chats data/panel seam now groups every valid session claim by repo-qualified sprint, independent
of enclosure liveness; explicit landed rows retain the archive, malformed claims get an honest error
group, and claim-less rows stay flat. `SessionList` renders each group and flat member set as a complete
spawn-edge forest with manager-only collapse, live-first order, bounded width, and full-value hover
recovery. The task reader merges the on-demand body over its current summary, preserves omitted arrays,
shows an explicit summary fallback on fetch failure, and renders implementation steps once.
260712-TRH-L1 moves that hydration state into a focused data hook and makes it the visible reader's
first request priority: summary content plus loading status render immediately, while notes and every
eager reader/enclosure change-set counter wait for body success or failure. These are behavior changes
within the existing `data/` and `panels/` routes; no new frontend route was added.
The reopened correction keys request lifetime and body-payload caching by `docPath + bodyRevision`,
not projected `TaskDocNode` identity; body payloads merge into the current summary at render time.
Late abandoned responses are discarded, unchanged analytics-object replacement does not restart the
request, and failure remains terminal for that key until selection or revision changes. The cockpit
composition regression covers direct leaf, master, drilled subtask, lifecycle-bound, and pending
A-to-B selection paths. Full fetch-time status/steps/title fields may still mask fresher summary
values because the revision hashes authored body fields only; that pre-existing staleness window is
not fixed here.

HFX2-L21 replaces the Chats session rail's fixed width with a persisted 220–560 px width. A visible
separator supports pointer dragging and Left/Right keyboard steps, while the adjacent terminal keeps
a 20 rem minimum when space permits. Direct manipulation does not animate the panel width.

### 260712-TRH-L7 landing freshness boundary

The dashboard consumes additive landing freshness truth from the projection: stale refs remain visible and age-labeled, while Engine Room landing-flow motion is limited to observed refs. Remote observation remains a server-side background concern; this route documents the client rendering and wire-type contract.

## Invariants And Boundaries

- **Near-read-only, two interactive surfaces** — the cockpit renders the projection read-only except
  for (1) Gate Respond, whose Yes/No paths POST developer-attributed durable decisions while Chat stays
  message-only through hosted chat or the external inbox, and
  (2) the Chats terminal's bidirectional Mode B2 WebSocket (slice 6e — keystrokes/resize out, raw PTY
  bytes in). Everything else stays display-only; the server enforces every effect.
- **Client-agnostic shapes** — the frontend consumes the `WorkspaceProjection` nodes verbatim (no
  dashboard-bespoke endpoints); North-Star #2.
- **Build-time styling only** — Panda extracts static CSS at build; `styled-system/` is generated,
  gitignored, and excluded from memory scope. The shipped bundle is static CSS + JS.
- **Determinism** — `?effects=off` / the calm-cockpit toggle freezes every animation/transition so
  screenshots + visual assertions are stable.
- **Provider/state are never faked** — colour + silhouette carry state (note 08); `inferred` states
  are visibly marked; ages are server-computed, never `Date.now()`.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The L16 grouping derivation owns repo-qualified sprint/archive/error membership. | L48-L159 | [sessionGroups.ts](data/sessionGroups.ts) |
| The L16 session renderer owns forest order, manager collapse, bounded layout, and hover details. | L242-L484 | [SessionList.tsx](panels/SessionList.tsx) |
| The L21 Chats shell owns the persisted sidebar width plus pointer and keyboard separator behavior. | L1-L588 | [Chats.tsx](panels/Chats.tsx) |
| The visible-body hook owns availability, merge, and revision-aware cache state. | L1-L72 | [useTaskDocumentBody.ts](data/useTaskDocumentBody.ts) |
| The detail panel resolves the displayed document and delays notes plus all eager change-set requests until body hydration is terminal. | L380-L388; L629-L687; L1044-L1085; L1309-L1388 | [DetailPanel.tsx](panels/DetailPanel.tsx) |
| The serving layer supplies the projection and static package boundary consumed by this route. | L1-L80 | [serving/app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The built bundle is synced into package data and checked against source plus dist. | L30-L52; L151-L179 | [scripts/sync-dashboard.py](agents-remember/scripts/sync-dashboard.py) |

## 260707-HFX2-L17 Seat Binding Route Impact

Dashboard session data distinguishes current `seatRole` from origin `spawnRole`; local assignment,
grouping, ordering, chips, and pane labels are binding-first. Attach/move includes an explicit role
picker and posts `{leafKey, role}`, preserving different-role owners while surfacing same-role
conflicts. These TypeScript sources are the durable UI behavior. `scripts/sync-dashboard.py` builds
and copies them into package data, and serving mounts that synchronized output; generated hashed
assets are not documented individually.

### 260713-PHA-L5 Route Contract Review

The route remains governed by the shared hosted protocol bridge: exact adapter snapshots provide
readiness and liveness, correlated receipts sit beneath durable inbox rows, interactions use durable
gates, legacy/custom sessions are explicit unsupported states, and pane/log signals are diagnostic
only. Dashboard and packaged projections remain additive and synchronized.

## Update History
- 2026-07-17T04:20+02:00 — 260715-FEUI-L6 route impact (PTY stage surface, structured
  interactions, session lifecycle actions; review FINAL PASS after a 1×sev-3 + 5×sev-4 fix
  round, all CLOSED): `data/` gains the interaction/lifecycle layer — `interactionAnswer.ts`
  (the SOLE gate-channel answer path), `sessionLifecycle.ts` (detailed terminate/cleanup +
  residual notice store + the focus-independent retire-residual sweep), `ptyHarvest.ts`
  (client-side legacy-raw OSC/bell/title harvesting), all + suites; `actions.ts` gains
  `postGateDecisionDetailed`, `terminal.ts` the additive `onSocketState`;
  `panels/session-cockpit/` gains PtySurface/InteractionBar/WorkingLine/StopResidualNotes/
  lifecycleCopy (see that overview); `panels/Terminal.tsx` gains additive optional props (DOM
  default, lazy webgl escalation, live screenReaderMode, harvesting hooks, named `role="group"`
  landmark); `test/fixtures/catalogRows.ts` appends the `L6_*` rows (FLEET byte-identical);
  `dev/` gains `/dev/pty-bench` (`PtyRenderBench.tsx` + `lineLogFixture.ts`; driver at
  `dashboard/e2e/ptyRenderBench.mjs`). Two exact-pinned deps entered `package.json`:
  `@xterm/addon-webgl` (lazy escalation chunk, loaded only if the renderer constant flips) and
  `@xterm/addon-serialize` (bench probe only — evaluated cheap-enough, deliberately NOT adopted
  in product code until an LRU cap or the pane-freeze repaint package defines the discipline).
  Verification metadata pinned to the leaf base until closeout stamps the L6 code commit.
- 2026-07-17T02:30+02:00 — 260715-FEUI-L2 route impact (session data layer, rail, and stage
  container; review FINAL PASS): `data/` gains the sessions-cockpit data layer —
  `catalogPoll.ts` (the poll driver hoisted OUT of Chats; Chats is now a consumer),
  `seatEvents.ts` (the gated `/api/events` seat reconciler; poll stays authoritative),
  `stateGrammar.ts` (the one dot grammar + 2.4 s pulse ruling), `railModel.ts` (the ruled
  hierarchy/attention/joins), `sessionCockpitStore.ts` (per-seat honesty-invariant client state),
  all + suites; `types/` gains `terminalCatalog.ts` (the full catalog wire mirror,
  `data/terminal.ts` re-exports); `test/fixtures/` is the new shared-fixture home
  (`catalogRows.ts`); `panels/session-cockpit/` gains the rail/stage/inspector components (see
  that overview); `sessions.ts`/`stream.ts`/`commands.ts`/`index.css` extended as their sidecars
  describe; plus a reviewer-accepted one-line defensive fix in `panels/file-viewer/FileViewer.tsx`.
  Open sev-3 developer ruling: status-chip vocabulary width (`stale`/`exited`/`retired`/
  `starting`). Verification metadata pinned to the leaf base until closeout stamps the L2 code
  commit.
- 2026-07-17T00:30+02:00 — 260715-FEUI-L1 route impact (view shell, WebTUI spike, keyboard/palette
  foundation): the cascade gained the `webtui` layer slot (S1, OQ-D = adopt — `styles/webtui.css`
  is the one mapping file, build-time scoped under `[data-view="sessions"]`, spike assertions kept
  in `test/webtuiSpike.test.ts`); `cockpit/Cockpit.tsx` registered the full-bleed keep-alive
  **Sessions** view; `panels/` gained the **`session-cockpit/`** child route and `data/` gained
  `commands.ts`, `sessionLayout.ts`, and the **`keymap/`** child route (the PTY reserved set with
  the R6 chord replacement Ctrl+Alt+[ / ] → Ctrl+Alt+PageUp/PageDown and five-source verification
  records); `styles/tokens.css` gained `--muted`. Four exact-pinned deps entered `package.json`
  (`@webtui/css@0.1.9`, `cmdk@1.1.1`, `tinykeys@4.0.0`, dev `postcss-prefix-selector@2.1.1`).
  Detail lives in the `panels/session-cockpit/` + `data/keymap/` overviews and the touched
  sidecars. Verification metadata pinned to the task base until closeout stamps the L1 code
  commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed route impact for the accepted hosted cutover.
- 2026-07-12T18:00+02:00 — 260712-TRH-L7: paired the landing-freshness body update with this history entry; projection landing refs remain visible and age-labeled when stale, while Engine Room motion is limited to observed refs and remote observation stays server-side.

- 2026-07-12T16:45+02:00 — 260712-TRH-L1 reopened-memory refresh: clarified stable path/revision
  request identity, separate body storage plus current-summary merge, late-response discard,
  terminal failure semantics, composition regression coverage, and the pre-existing scalar
  staleness window. Verification metadata remains blank until closeout stamps the code commit.

- 2026-07-12T13:36+02:00 — No route impact: 260712-TRH-L2 body review confirms the changeset refinements remain inside the existing `data/changeset` and `panels/changeset` surfaces; the `dashboard/src` route model and top-level organization are unchanged. Verification metadata remains pinned until closeout.
- 2026-07-12T12:55+02:00 — No additional route impact from 260712-TRH-L2: its changeset refinements stay inside the existing `data/changeset` and `panels/changeset` surfaces; the dashboard/src route model and top-level organization remain unchanged. Verification metadata pinned until closeout stamps the L2 code commit.
- 2026-07-12T12:07+02:00 — 260712-TRH-L1 dashboard-source route impact: added the focused
  `data/useTaskDocumentBody.ts` state seam and documented complete visible task content as the first
  reader request priority. Notes and change-set counters resume after success or fallback; no new
  frontend route was created. Verification metadata remains pinned until closeout.

- 2026-07-10T21:59+02:00 — 260707-HFX2-L21 dashboard-source route impact: documented the
  persisted, bounded Chats sidebar and its pointer/keyboard separator. The behavior stays inside the
  existing `panels/` route and preserves terminal working width without animating direct manipulation.
  Verification metadata remains pinned until closeout.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17 dashboard-source route impact: documented explicit
  role claim, binding-first client identity, pair-scoped assignment/rendering, and the
  source/build/serve package boundary. Verification metadata remains pinned until closeout.

- 2026-07-10T13:41+02:00 — 260707-HFX2-L16 route impact: documented repo-qualified sprint
  grouping, complete spawn-edge forest rendering, bounded/hover-complete rail rows, honest on-demand
  task-body fallback, and single-rendered implementation steps. No new route was created.
  Verification metadata stays pinned until closeout stamps the eventual L16 code commit.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 F6 route impact: added the on-demand task-document data
  adapter and `bodyRevision` wire field; full reader bodies no longer ride the always-on projection.
  Verification metadata remains pinned until closeout stamps the eventual L13 code commit.

- 2026-07-09T14:05+02:00 — No route impact: 260707-HFX2-L11 (landed chat archive + group cleanup)
  extends `data/{sessionGroups,sessions,terminal}.ts` (new `"landed"` status, landing provenance
  fields, `cleanupLandedTerminalSessions()`) and `panels/{Chats,SessionList,Terminal}.tsx` (landed
  archive group, group-cleanup control, read-only landed terminals). This is data-shape and panel
  behavior content, not a change to this route's own module layout or routing; per-file detail lives
  in the already-updated `dashboard/src/data/` and `dashboard/src/panels/` sidecars/sub-overview.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L11 commit.
- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 route impact (dead-seat storm observability, R6):
  `SupervisorHeartbeat` now includes pending/redeliverable inbox backlog counts and last sweep
  duration; `data/store.ts` compares those fields in `heartbeatEquals`; and
  `cockpit/Cockpit.tsx` renders them in the top-bar `SupervisorHeartbeatBadge` beside heartbeat age.
  Verified with dashboard typecheck and `src/data/store.test.ts`. Verification metadata pinned until
  closeout stamps the 260707-HFX2-L8 commit.
- 2026-07-08T18:45+02:00 — 260707-HFX2-L2 route impact (supervisor sweep, R5): `cockpit/Cockpit.tsx`
  gains `SupervisorHeartbeatBadge` in the `TopBar` (beside `ServingBuildStamp`); `data/store.ts`
  gains the `supervisorHeartbeat` field, deliberately excluded from the change-gate `unchanged`
  check so the live tick age still applies on a content-unchanged reconnect; `types/projection.ts`
  gains the `SupervisorHeartbeat` type and optional `WorkspaceProjection.supervisorHeartbeat?` — a
  second app-injected, non-`projection.py` field alongside `servingBuild?`. No route/component-tree
  shape change beyond the one new top-bar badge. **Known limitation (builder-flagged, unverified
  in this environment):** these TS changes are unverified by `tsc`/a build (no `dashboard/
  node_modules` installed); a follow-up should run the dashboard's own build/test suite once
  available. Verification metadata pinned until closeout stamps the 260707-HFX2-L2 commit.
- 2026-07-07T23:55+02:00 — 260707-HFX-L6 route impact: the `data/sessionGroups`
  model and terminal data mirror now include architect/curator role provenance so Chats grouping and
  row chips can represent the split developer-facing architect, backend orchestrator, and curator
  closeout seat without changing the cockpit route structure. Verification metadata pinned until
  closeout stamps the HFX-L6 commit.
- 2026-07-07T14:00+02:00 — agent-orchestration L17 route impact: `panels/` gains the **`notes-reader/`**
  child route (the Notes Reader takeover, reusing the File Viewer `DualPane` over the unchanged L9
  `/api/notes/*` API), and `cockpit/Cockpit.tsx` gains a second full-bleed takeover hosting it (retained
  mounted-hidden after Back so selection survives back/forward). `panels/TaskNotes.tsx` becomes the compact
  entry surface (inline reader retired) and `panels/LifecycleList.tsx`'s gate chip drops the wait-loop `ask`
  fallback. Details in the `panels/` + `panels/notes-reader/` overviews and the touched sidecars.
  Verification metadata pinned until closeout stamps the L17 commit.
- 2026-07-07T05:38+02:00 — 260703-L15 route impact (long-session memory): `data/` gains
  `servedAges.ts` (+ suite; the volatile-age mirror, stable equality, arrival anchors, display
  ticker); `store.ts` apply paths became identity-preserving/change-gated (zero writes on idle
  payloads) and carry `servingBuild`; `types/projection.ts` mirrors the app-injected
  `ServingBuild`; `cockpit/Cockpit.tsx` renders the muted serving-build stamp; the four
  age-display panels advance served ages locally. NOTE: `data/` has no route overview of its own —
  this file governs it directly, so the genuine body update lives here (same call as L14).
  Verification metadata pinned until closeout stamps the L15 commit.
- 2026-07-06T23:57:36+02:00 — 260703-L14 route impact (visual hierarchy + chat grouping): `data/` gains
  `sessionGroups.ts` (+ unit suite, the G1 command-tree derivation) and `taskHierarchy.ts` gains the
  orchestration-command helpers; `grammar/` gains `RankBadge.tsx` (+ test, the V4 chevron insignia);
  `types/projection.ts` mirrors `TaskDocNode.orchestrates?`; `styles/tokens.css` gains the six
  gold/purple tier vars (mirrored as Panda tokens in `panda.config.ts`). Behavior detail lives in the
  `panels/`/`grammar/` overviews and the changed sidecars. Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T15:40+02:00 — No route impact: 260703-L12's dashboard change is content-only inside `panels/` — `flowModels.ts` gains the STRATEGIST model (8-model census) and loop-doctrine lines, `FlowTab.test.tsx` grows to 11 cases; the dashboard/src route model, data layer, and grammar this overview describes are unchanged — detail lives in the `panels/` overview and the two file sidecars. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-06T12:10+02:00 — No route impact: 260703-L10's dashboard change is a single phase-label string inside `panels/flowModels.ts` (designer `frame` → `reframe`); the dashboard/src route model, data layer, and grammar this overview describes are unchanged — detail lives in the `panels/` overview and the `flowModels.ts` sidecar. Verification metadata pinned until closeout stamps the L10 commit.
- 2026-07-06T03:25+02:00 — 260703-L11 route impact: `data/selectors.ts` gains the shared
  `hasLiveWorktree` tasks-surface visibility rule and `types/projection.ts` mirrors the new required
  `EnclosureNode.codeWorktreeExists`/`memoryWorktreeExists` flags; `dev/fixtures.ts` and the
  `topology`/`panels` test fixtures default them `true`. The Hangar/LifecycleList behavior change is
  documented at the panels route. Verification metadata pinned until closeout stamps the L11 commit.
- 2026-07-06T03:00+02:00 — 260703-L9 route impact (friction F-M): `data/` gains `notes.ts` (+ unit
  suite), the third serving read client — `listNotes`/`readNote` over the shared `getJson`/`qs`
  transport plus the pure `resolveNoteReference` — feeding the new task-reader notes view
  (`panels/TaskNotes.tsx`); the `data/` route-model bullet now names it beside `files.ts` and
  `changeset.ts`. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-05T19:55+02:00 — No route impact: the dashboard/src route model is unchanged — the cycle-7 manager-raise-node enclosure addition is documented at the panels route (260703-L8 cycle 7).
- 2026-07-05T19:10+02:00 — No route impact: the dashboard/src route model is unchanged — the cycle-6 seam-node prose update is documented at the panels route (260703-L8 cycle 6).
- 2026-07-05T18:24+02:00 — No route impact: dev-only index label aligned with the converged canvas (DevApp.tsx); no production route or component change (260703-L8 cycle 5).
- 2026-07-05T16:32+02:00 — No route impact: the dashboard/src route model is unchanged — the FlowTab redraw is documented at the panels route (260703-L8 cycle 4).
- 2026-07-04T12:31+02:00 - L3 route impact: dashboard data/types now mirror
  agent-to-agent inbox metadata and hosted-delivery state for `AgentPickupNode`
  and `/api/operator-inbox`. Verification metadata pinned until closeout stamps
  the L3 commit.
- 2026-07-04T10:05+02:00 — 260703-L0 route impact (small): `dev/` gained the `/dev/flows` lifecycle-design
  canvas route (DevApp mounts the generalized `panels/FlowTab` over the new `panels/flowModels.ts` registry);
  detail lives in the `panels/` overview and the file sidecars. Verification metadata pinned until closeout
  stamps the L0 commit.
- 2026-07-03T00:35+02:00 — L11 route impact: reopened leaves render as planned doc rows via the stable leaf id; abandoned enclosures leave the active operations rows (see panels/LifecycleList).
- 2026-07-02T20:15+02:00 — L8 route impact (small): `data/selection.ts` selections now carry the
  qualified `leafKey` when anchored inside a task reader marked `data-task-leaf-key`, and
  `cockpit/Cockpit.tsx` threads `viewedLeafKey` + `leafChatActive` into `HighlightComposer` so the
  direct leaf-chat paste path can resolve its target. The route structure is otherwise unchanged;
  behavior detail lives in the `panels/` overview and file sidecars. Verification metadata pinned until
  closeout stamps the L8 commit.
- 2026-07-02T17:04+02:00 — No route impact: L9 extends the existing `data/sessions.ts` and
  `panels/Chats.tsx` / `RailChat.tsx` routes so hosted chats can move between durable leaves after
  creation, and open dashboard tabs rehydrate `"leaf"` catalog invalidations or polling refreshes. The
  `dashboard/src/` route model is unchanged; detail lives in the `panels/` overview and changed sidecars.
  Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-02T16:35+02:00 — No route impact: the reopened-L6 wheel/paste fixes stay inside `panels/` and
  `data/`. `panels/Terminal.tsx` yields wheel to xterm mouse reporting when the app tracks the mouse;
  `data/terminal.ts` gained `pasteAndConfirm` (echo-confirmed, boot-deadline-retried draft paste) and
  `data/sessions.ts`'s `pasteDraftToSession` delegates to it. The `dashboard/src/` route model is
  unchanged. Verification metadata pinned until closeout stamps the follow-up commit.
- 2026-07-02T15:03+02:00 — No route impact: the L6 alternate-buffer wheel follow-up stays inside the
  existing shared `Terminal` wrapper under `panels/`. Normal-buffer scrollback still uses xterm viewport
  scrolling, while alternate-buffer hosted agent TUIs receive PageUp/PageDown wheel steps instead of
  xterm Up/Down history input. The `dashboard/src/` route model is unchanged. Verification metadata
  pinned until closeout stamps the follow-up commit.
- 2026-07-02T13:16+02:00 — Reopened L6 route impact/no route impact: the follow-up stays inside the
  existing `cockpit/` + `panels/` + `data/` model, but `data/sessions.ts` now separates leaf-context
  draft paste from submit so `RailChat` can place context in the selected hosted chat without pressing
  Enter. Chat scrollback remains documented in the `panels/` overview and `Terminal.tsx` sidecar. The
  `dashboard/src/` route model is unchanged; verification metadata pinned until closeout stamps the L6
  follow-up commit.
- 2026-07-01T01:19+02:00 — No route impact: L6 adds bind-time leaf context handoff inside the existing
  `cockpit/` + `panels/` + `data/` model. `CockpitShell` passes `analytics.engineProcesses` to the existing
  right-rail `RailChat`, and `RailChat` injects a projected leaf context package when a chat is started on a
  displayed leaf or a free chat is successfully attached. The `dashboard/src/` route model is unchanged;
  detail lives in the `panels/` overview and the `Cockpit.tsx`/`RailChat.tsx`/`RailChat.test.tsx` sidecars.
  Verification metadata pinned until closeout stamps the L6 commit.
- 2026-06-30T00:00:00+02:00 — No route impact: L5 (Sidebar chat) adds leaf-keyed attachment + a right-rail River⇄Chat
  toggle. The change lives in `cockpit/Cockpit.tsx` (a `railView` toggle + `selectedLeafKey` derivation),
  `data/` (`sessions.ts` leaf binding, `terminal.ts` `attach-leaf` client, `taskIdentity.ts` leaf-key
  helpers), and `panels/` (the new `RailChat.tsx`, plus `Chats.tsx`/`SessionList.tsx` leaf-attach + name
  label) — all within the already-documented `panels/` route. The `dashboard/src/` route model
  (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged; detail lives in the `panels/` overview
  and the `cockpit/`/`data/`/`panels/` file sidecars. Verification metadata pinned until closeout stamps
  the L5 commit.
- 2026-06-29T23:00+02:00 — No route impact: L4a refines the already-documented `panels/changeset/`
  sub-route (leaf committed/working change-set views, a diff-highlight rectangle, a live working-view
  auto-refresh), adds the doc-reader change-set bars in `panels/DetailPanel.tsx` + leaf helpers in
  `data/changeset.ts`, and changes `cockpit/Cockpit.tsx` so the change-set takeover overlays (rather than
  replaces) the railed body so the back link returns to the leaf it was opened from. The `dashboard/src/`
  route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged; detail lives in the `panels/`
  + `panels/changeset/` overviews and the `Cockpit.tsx`/file sidecars. Verification metadata pinned until
  closeout stamps the L4a commit.
- 2026-06-29T17:00+02:00 — No route impact: the L4 follow-up refines the already-documented `panels/changeset/` sub-route — the series/master change-set is now the NET inspectable diff (was accumulated-only) — plus shared code-view polish (`codemirrorTheme` comment/punctuation readability, `DiffPane` split-diff scroll). The `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged; detail lives in the `panels/changeset/` overview + the file sidecars. Verification metadata pinned until closeout stamps the L4 follow-up commit.
- 2026-06-29T16:40+02:00 — Operations Integration L4 (Change-Set Viewer) route impact: `cockpit/Cockpit.tsx`
  gained a `changeSet` **TAKEOVER** (a `DetailPanel` change-set button replaces the railed Operations body
  with a full-bleed `<ChangeSetViewer>`; a back link restores it); a new **`panels/changeset/`** sub-route
  lands — the Change-Set Viewer screen (a read-only `@codemirror/merge` diff over the L3 `/api/changeset/*`
  API, reusing the L2 `FilePane`); and `data/` gains the `changeset.ts` serving client (sharing `files.ts`'s
  `getJson`/`qs`/`FilesApiError`). Detail in the `panels/` + new `panels/changeset/` overviews and sidecars.
  Verification metadata pinned to the task base until closeout stamps the L4 code commit.
- 2026-06-29T09:06+02:00 — Operations Integration L2 (File Viewer) route impact: `cockpit/Cockpit.tsx`
  registers a new full-bleed **File Viewer** view (`"files"` in the `View` union + the `fullBleed` set, a
  `VIEWS` tab between Operations and Engine Room), **kept mounted** (CSS-hidden) like Chats so its
  repo/scope/open-file/tree state survives a tab switch; and a new **`panels/file-viewer/`** sub-route
  lands — a read-only code+onboarding dual-pane (two Headless Tree explorers, a read-only CodeMirror 6
  pane, bidirectional code↔onboarding pairing) that is the first consumer of the L1 read-only files API,
  plus the reusable `FilePane`/`DualPane` for the L4 Change-Set Viewer. Detail in the `panels/` + new
  `panels/file-viewer/` overviews and sidecars. Verification metadata pinned until closeout stamps the L2
  code commit.
- 2026-06-28T16:17+02:00 — Task 35 route impact: `panels/LifecycleList.tsx` reopen-task nesting — the
  Operations list admits a reopened leaf's suffixed enclosure by shared lifecycle + suffixed-leaf shape and
  nests doc-less enclosure-backed runtime rows under their master, ending the standalone-phantom row. No
  other `dashboard/src` route structure changed. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-28T13:54+02:00 — Task 34 route impact: the raw Event River store (`data/store.ts`) now keeps a
  bounded **sliding window** of the newest ~2000 rows (memory-bounded rather than the unbounded
  session-growth the prior text described), which `EventRiver` virtualizes over so there is still no hard
  display cap. Refreshed the `data/` Route Model bullet's event-store description. Verification metadata
  pinned until closeout stamps the task-34 code commit.
- 2026-06-28T07:45+02:00 — Task 33 route impact: the `topology/` view became an active-enclosure constellation
  (lifecycle/task rim removed, each enclosure folds in its 1:1 lifecycle, `activeTopologyInputs` filters to
  the served active set, basename `groupKey` join fixes the latent task-12-S1 provider join); `types/projection.ts`
  mirrors the new required `activeWorktreeGroups`, and `data/store.ts` + `data/stream.ts` thread it through.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-28T07:43+02:00 — Task 29 S7 route impact: the cockpit now hides the former Lifecycle Flow
  tab, the raw Event River waits for the backend `ready` event before rendering an empty history, and
  frontend storage no longer truncates received Event River rows. Attention queue dismiss/clear actions
  optimistically suppress visible rows while the backend physically removes or acknowledges the source,
  including targetless actionable-drift notices. Verification metadata pinned until closeout stamps the
  task-29 code commit.
- 2026-06-28T03:21+02:00 — Task 31 route impact: projection types now mirror the provider boot-node
  `missing` state, letting Engine Room render expected-but-absent provider roles distinctly from
  configured/observed provider rows. Operations task grouping also accepts the authored task-document id
  when matching a leaf document to its enclosure, so leaf 31 stays nested under the browser-dashboard
  master even when the task JSON file stem is descriptive. Verification metadata pinned until closeout
  stamps the task-31 code commit.
- 2026-06-27T18:43+02:00 — Task 26 route impact: `cockpit/Cockpit.tsx` registers a new full-bleed
  **Lifecycle Flow** view — `"flow"` in the `View` union + the `fullBleed` set, a `VIEWS` tab second
  after Operations, and a `ViewBody` case rendering `<FlowTab />` from `panels/FlowTab.tsx`. FlowTab is
  a /dev-stage diagnostic visualizing the build-job lifecycle (the task-27 next-step engine spec); the
  production bundle was not rebuilt this task. Verification metadata pinned until closeout stamps the
  task-26 code commit.
- 2026-06-27T03:04+02:00 — Task 22 follow-up: `data/sessions.ts` removed the hidden-label reservation
  state with the Hide UI path, and terminal catalog create/terminate broadcasts now carry the changed
  `sessionId` so other tabs can remove ended rows deterministically.
- 2026-06-27T01:25+02:00 — Task 22 follow-up: `data/sessions.ts` now broadcasts backend-persisted
  terminal catalog create/terminate invalidations across browser tabs, while `data/terminal.ts` exposes a
  nullable catalog fetch so receivers can distinguish empty success from fetch failure.
- 2026-06-27T01:03+02:00 — Task 22 follow-up: `data/sessions.ts` now allocates session labels from the
  lowest available live per-prefix ordinal, then releases End/terminated labels.
- 2026-06-27T00:25+02:00 — Task 22 follow-up: the Chats view now mounts restored sessions on first
  selection and keeps visited terminals mounted while hidden, avoiding broken hidden xterm hydration for
  restored Claude/Codex sessions after refresh without losing tab-switch buffers.
- 2026-06-26T23:15+02:00 — Task 22 route impact: the Chats data/panel route now hydrates
  dashboard-owned terminal sessions from `/api/terminal/sessions`, tracks running/exited/terminated
  catalog status, restores the last active session, and routes explicit End through backend terminate.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T20:18+02:00 — Task 21 route impact: frontend projection types mirror
  `SeriesNode.seriesTokenTotal`, and DetailPanel master readers display the server-composed aggregate.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T19:40+02:00 — Task 20 reopened route impact: `data/taskIdentity.ts`
  now participates in Event River lifecycle-label fallback by exposing direct
  task-document title labels for lifecycle-only history rows. Detailed behavior
  lives in the data helper and panel formatter sidecars. Verification metadata
  pinned until closeout stamps the reopened task-20 code commit.
- 2026-06-26T18:23+02:00 — No route impact: task 20 adds Event River readable-feed
  formatting inside `dashboard/src/panels/` (`EventRiver.tsx`, `eventSummary.ts`, and tests). The
  `dashboard/src/` route model remains cockpit/grammar/panels/data/dev; detailed behavior lives in
  the panels overview and file sidecars. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-06-25T14:02+02:00 — Task 24 reopened: frontend data/panels now support gate-id-only Clear for stale gate rows while keeping normal decisions lifecycle-targeted.
- 2026-06-25T13:20+02:00 — Task 23/24: frontend route now includes gate dismissal, attention clear, inbox-warning deletion, and `AgentPickupNode` projection types.
- 2026-06-25T07:26+02:00 — Task 19 gate interaction polish: `dashboard/src/` now treats Gate Respond as
  three explicit paths — Yes/No record targeted durable gate decisions through `data/actions`, while Chat
  remains message-only through hosted chat or the operator inbox. The data route also adds
  `actions.test.ts` coverage. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T18:11+02:00 — Task 17 route correction: `TaskDocNode.id` is now mirrored in the projection
  types and used by `data/taskHierarchy.ts`, `LifecycleList`, and `DetailPanel` as the authored leaf
  display number; parent sub-task `number` remains fallback data. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-06-24T18:02+02:00 — Task 17 route correction: `data/taskHierarchy.ts`, `LifecycleList`, and
  `DetailPanel` now use structured task metadata for visible leaf labels while keeping creation
  metadata as the ordering source. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T17:51+02:00 — Task 17 Operations hierarchy route update: added `data/taskHierarchy.ts` as
  the shared structured parent-series helper behind BY REPO leaf indentation and direct leaf parent
  backlinks. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T16:39+02:00 — Task 17 Operations route correction: dashboard selection is now typed
  (`taskdoc:` / `series:` / `lifecycle:`), task documents can be listed/read before lifecycle binding,
  and projection types mirror optional `TaskDocNode.lifecycleId`. Detail lives in `data/taskIdentity.ts`,
  `LifecycleList.tsx`, `DetailPanel.tsx`, and `types/projection.ts` sidecars. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-24T12:21+02:00 — Task 17 route impact: projection types now mirror task/series
  `createdAt`, `SeriesNode`, and `Analytics.series`, and dev fixtures default `series: []` in the
  analytics shape. DetailPanel-specific behavior is recorded in the panels overview and sidecars.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T08:59+02:00 — Data route addition: added `taskIdentity.ts` to the route model as the
  shared lifecycle label/direct-task-document helper used by Operations and Detail. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: dashboard projection types now carry explicit `enclosureId`, `leafId`, and `taskRoot` fields, and Engine Room renders the projected integration/source branch instead of hardcoding `main`. Detail lives in the `types/projection.ts`, engine-room fixture, and `EnclosureCanvas.tsx` sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:31+02:00 — Clarified Task 12 S2 topology wording: repo-scoped GrepAI dots come from
  addressable `targetRepos` inside one aggregate provider instance, while worktree providers remain
  bound by `worktreeGroup`. Verification metadata pinned until closeout stamps the S2 code commit.
- 2026-06-23T21:46+02:00 — Task 12 S2 route impact: `topology/model.ts` now includes repo-covered
  workspace providers in the repo ring and parents provider satellites by `worktreeGroup`, then `repoId`,
  then workspace core; `types/projection.ts` clarifies the binding comments and `model.test.ts` covers
  repo-scoped parenting plus precedence. Verification metadata pinned until closeout stamps the S2 code
  commit.
- 2026-06-23T16:02+02:00 — Task 12 S1 route impact: `topology/model.ts` now records worktree
  groups while building topology nodes and parents worktree-scoped providers to the owning worktree
  node, with fallback/workspace providers staying on the workspace core. `topology/model.test.ts`
  adds pure-model coverage for matching, fallback, and workspace-provider behavior. No backend
  projection shape change; per-repo main-stack provider placement remains deferred to S2.
- 2026-06-23T15:05+02:00 — Task 10 dashboard fallback: `data/operatorInbox.ts` joined the data route and `GateResponder` now falls back to `POST /api/operator-inbox` for lifecycles without a hosted chat session, preserving the agent-owned gate-release model. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-23T14:31+02:00 — Task 11 route impact: `dashboard/src/` now treats gate response as a
  hosted-chat direct-inject surface instead of the old developer gate-decision `/api/actions` drawer.
  `cockpit/Cockpit.tsx` threads selected lifecycle identity into Chats and HighlightComposer,
  `data/sessions.ts` owns lifecycle-tagged hosted sessions, and `panels/GateResponder.tsx` is the shared
  Respond control used by DetailPanel plus secondary engine-room/Hangar gate surfaces.
- 2026-06-23T13:35+02:00 — No route impact: slice-12 topology render-robustness — `topology/constel.ts` gained a file sidecar (the renderer now paints synchronously on resize/update, not rAF-only) and `panels/Topology.tsx` made the canvas absolutely-positioned + the `Panel` `fill`. Behaviour-preserving render/layout fixes within the existing `dashboard/src` route model; no structural change.
- 2026-06-22T11:00 — No route impact: slice 05o T7B–T18's `dashboard/src/`-direct changes are `dev/scenarios.ts`
  gaining six more failure-mode timelines (`seed-fault` T9B, `reindex-reroute` T9C, `provider-block` T7B,
  `live-sync` T12B, `integration-conflict` T14C, `abandon` T18) and `types/projection.ts` gaining the
  `refusedPolarity` edge field + a `refused` state — both additive within the existing `dev/`/`data/` route model
  (named `erFrame`-wrapped `Scenario`s + projection-type fields, not a shape change). The renderer primitives
  (refused-conduit flash, moved-badge, engine-dropout) and the six wirings are internal to `panels/engine-room/`
  (its overview + sidecars). The `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is
  unchanged. Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-22T01:40 — No route impact: slice 05o T1B's only `dashboard/src/`-direct change is the `dev/`
  scenario player — `dev/scenarios.ts` gains the `stale-base` preflight→fast-forward failure-mode timeline (F0→F8,
  + `dev/scenarios.test.ts` a case) — which is data within the existing `dev/` route model, not a shape change.
  The T1B renderer primitives (the pruned `main` node), the indicator anchoring / z-order fixes, the
  `FleetingEnclosure` box, and the alert transitions are internal to `panels/engine-room/`, and the §10 spec note
  is under the sibling `docs/design/engine-room/`; the `dashboard/src/` route model
  (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged — detail in those overviews + sidecars.
  Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-22T00:29 — No route impact: slice 05o T3B's only `dashboard/src/`-direct change is the `dev/`
  scenario player — `dev/scenarios.ts` gains the `memory-block` failure-mode timeline (+ `dev/scenarios.test.ts`
  a case) — which is data within the existing `dev/` route model, not a shape change. The failure-mode renderer
  primitives (scan ring, ghosted lane), fixtures, and the engine-gauge polish are internal to
  `panels/engine-room/`, and the §10 spec section is under the sibling `docs/design/engine-room/`; the
  `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged — detail in those
  overviews + sidecars. Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-21T23:35+02:00 — slice 05k tear-down + design-review refinements: the only `dashboard/src/`-direct
  change is `index.css` deleting the `@keyframes powerup` (the last engine-room canvas keyframe — the
  indexing→nominal engine flash, now a Motion opacity pulse on the charge rect). All the rest — the tear-down
  dispose sequence + power-down diagnostics, the second-loop engine-fill fix, the three-column re-spacing, the
  closeout-train breadcrumb, and the memory integration arrow — is internal to `panels/engine-room/` (its
  overview + sidecars). The `cockpit/`/`grammar/`/`panels/`/`data/`/`dev/` route model is unchanged. (Separately,
  `docs/design/` was brought into onboarding scope — a sibling route, not under `dashboard/src/`.) Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-21T09:57+02:00 — slice 05n (engine-room DrawSVG/MotionPath migration): the only `dashboard/src/`-direct
  change is `test/setup.ts` adding a jsdom **SVG-geometry stub** (`getBBox`/`getTotalLength`/`getPointAtLength`)
  so the engine-room GSAP DrawSVG/MotionPath plugins construct under the effects-on GSAP-gate test. The render
  rework (draw-on → DrawSVG one-shot, packet → MotionPath, the `flowConduit` recipe) is internal to
  `panels/engine-room/` (its overview + sidecars). The `dashboard/src/` route model
  (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged. Verification metadata pinned until closeout
  stamps the 05n commit.
- 2026-06-21T02:44+02:00 — slice 6g: the cockpit gained **task-document navigation** — `panels/DetailPanel` renders a series **master** (overview + clickable sub-task index) with in-panel **drill-in** into each slice (the back/parent up-link in the sticky panel header), **markdown-rendered** task prose via the new `grammar/Markdown` primitive, and **cross-master "→" navigation** that jumps between series lifecycles (`onOpenLifecycle`). Detail in the `grammar/` + `panels/` overviews. Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-21T02:26+02:00 — slice 05k (engine-room motion → GSAP/Motion): the only `dashboard/src/`-direct
  change is `index.css` deleting the nine engine-room canvas `@keyframes` (`chargeSweep`/`conduitDraw`/`pktRun`/
  `attnBreath`/`stopFlash`/`closeoutSweep`/`warpSurgeUp`/`warpSurgeDown`/`landingIn`) that prior slices parked
  in the effects layer; the engine-room canvas motion now runs on GSAP timelines (`useEngineTimeline`) + Motion,
  CSS static (the app-wide `crt-overlay`/`flicker`/`pulse` keyframes stay). The render rework + the new hook are
  internal to `panels/engine-room/` (its overview + sidecars). The `cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`
  route model is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T23:58+02:00 — slice 5i: the `dev/` sub-route gained the **scenario player** — new
  `dev/scenarios.ts` (timeline model) + `dev/ScenarioPlayer.tsx` (transport) + `dev/scenarios.test.ts`, with
  `dev/Bench.tsx` reworked from the static gallery into a scenario picker + player and `dev/fixtures.ts`
  extracting the shared `engineRoomProjection` wrap; `dev/Bench.tsx` also gained a sidecar (a prior gap). The
  only other `dashboard/src/`-direct change is the `index.css` `landingIn` keyframe (engine-room landing-tail
  detail). The engine-room render rework is internal to `panels/engine-room/` (its overview + sidecars). The
  `cockpit/`/`grammar/`/`panels/`/`data/` route model is otherwise unchanged. Verification metadata pinned
  until closeout stamps the code commit.
- 2026-06-19T15:59 — Task 6 slice 6f-1: the cockpit gained the **highlight → context-package** composer — `panels/HighlightComposer.tsx` (mounted in `CockpitShell`) + the `data/selection.ts` selection hook; a text selection raises it to send the selection + a message into a chat session's stdin (the `data/sessions` store became the cockpit-wide inject seam; `data/terminal.ts` buffers pre-open stdin for create-then-send). No silent action; reuses the live B2 channel (not ACP). Detail in the `panels/` + `data/` sidecars. Verification metadata pinned until closeout stamps the 6f-1 code commit.
- 2026-06-19T14:05 — Task 6 slice 6e-4: terminal/session **hardening** — the open-session registry moved into a new `data/sessions` Zustand store, and a live terminal now survives both a cockpit *view* switch (`cockpit/Cockpit.tsx` keeps `<Chats>` mounted, hidden via CSS) and a *session-tab* switch (`panels/Chats.tsx` keeps every session's `<Terminal>` mounted) instead of being unmounted; the backend PTY spawn (`serving/terminal.py`) gained a controlling terminal so tmux honors resize, and `data/terminal.ts` replays the first winsize on socket open. Detail in the `data/` + `panels/` sidecars. Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-19T05:48 — Task 6 slice 6e-3: the **Chats** terminal gained **context injection** — a `SessionComposer` (React Aria `TextField`/`TextArea` + `Button`) docked below the terminal injects a block of text into the active session's stdin as a bracketed paste (the on-ramp to 6f). Refreshed the Behavior layer. Verification metadata pinned until closeout stamps the 6e-3 code commit.
- 2026-06-19T06:39+02:00 — No route impact: an engine-room crash fix relaxes `EngineProcessNode.landing` to optional (`landing?:`) in `types/projection.ts` so the canvas tolerates a pre-5h/persisted projection that omits it; the `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged — detail in the `types/projection.ts` sidecar. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T04:38 — Task 6 slice 6e-2c: the **Chats** view's open sessions moved into a dedicated left-rail **`SessionList`** switcher (a React Aria `GridList` — single-select = active session, per-row close ✕), replacing the horizontal tab strip; the launch controls stay in the top strip and the harness buttons now share ＋ Terminal's golden look. Refreshed the Behavior layer (the switcher's `GridList`) + the `panels/` route-model line. Verification metadata pinned until closeout stamps the 6e-2c code commit.
- 2026-06-18T21:27 — No route impact: a dev-bench review-ergonomics pass collapsed the `/dev/bench` gallery strip into a compact `<select>` picker + trimmed the 6 `engine-boot-*` step tabs and the unused `engine-empty` fixture (mirroring task 5's `b3f2491`). All internal to the DEV-only `dev/` harness (dropped from the production bundle); the `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) this overview describes is unchanged — detail in the `dev/` sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T21:27 — Task 6 slice 6e-2b: the **Chats** view gained per-harness launch buttons — `data/terminal.ts` `fetchHarnesses` (`GET /api/harnesses`) drives a detection-driven button per *installed* harness (Claude Code / Codex / Pi.dev) beside ＋ Terminal. Detail in the `panels/` overview + the `Chats.tsx`/`terminal.ts` sidecars. Verification metadata pinned until closeout stamps the 6e-2b code commit.
- 2026-06-18T21:25+02:00 — No route impact: slice 5h Tier 2's only `dashboard/src/`-direct change is mirroring the four optional `LedgerRefNode` fields (`codeSubject?`/`codeDate?`/`memorySubject?`/`memoryDate?`) in `types/projection.ts`; the 6-column popover render lives in `panels/engine-room/` (its overview + sidecars). The `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T17:40 — Task 6 slice 6e-2a: the **Chats** view became a **create** surface — "＋ Terminal" spawns a dashboard-owned session via the new `data/terminal.ts` `openTerminalSession` → the `POST /api/terminal` opener (no longer just attaching to a store lifecycle). Detail in the `panels/` overview + the `Chats.tsx`/`terminal.ts` sidecars. Verification metadata pinned until closeout stamps the 6e-2a code commit.
- 2026-06-18T16:50 — Task 6 slice 6e-1: the cockpit gained its first **interactive terminal** — a full-bleed **Chats** view (`panels/Chats.tsx` + the lazy `panels/Terminal.tsx` xterm wrapper) over the new `data/terminal.ts` Mode B2 WebSocket client (binary PTY bytes in, `{type:stdin|resize}` out), reachable from the cockpit mode bar. **Corrected the stale "Read-only — no POST" invariant** (write surfaces have existed since 6c; 6e adds the bidirectional terminal). Dev bench supplies a mock socket so it renders without a backend; the real launch is 6e-2. Verification metadata pinned until closeout stamps the 6e-1 code commit.
- 2026-06-18T18:00+02:00 — No route impact: slice 5h's ledger popover mirrors `LedgerRefNode` + the additive `LedgerNode.rows` / `EngineProcessNode.ledgerRows`/`ledgerRowCount` fields in `types/projection.ts` and wires the demo `analytics.ledgers` in `dev/fixtures.ts`; the `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged — detail lives in the `engine-room/` overview + the `types/projection.ts` sidecar. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T15:00 — Task 6 slice 6c Part B: the cockpit gained its **one write** — `DetailPanel`'s Gate Review drawer POSTs a developer gate decision to `/api/actions` via the new `data/actions.ts` (+ a `gate-review` bench scene in `dev/fixtures.ts`). The rest stays read-only. Verification metadata pinned until closeout stamps the 6c Part B code commit.
- 2026-06-18T14:05 — No route impact: task 6 slice 6c Part A only extended the projection **type mirror** (`types/projection.ts` gained `GateNode` + the optional `LifecycleProjection.gate`); the `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`) is unchanged. The gate review **drawer** (`panels/DetailPanel.tsx` + `data/`) lands in 6c Part B — surfaced here then. Verification metadata pinned until closeout stamps the 6c Part A code commit.
- 2026-06-18T15:50+02:00 — No route impact: the 5h cleanup pass's only `dashboard/src/`-direct change is `dev/fixtures.ts` filtering the `engine-boot-*` frames out of the bench gallery tab strip (a DEV-harness curation); the rest is render polish internal to `panels/engine-room/` (conduit wiring + backdrop vignette + a dropped fixture). The `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`/`dev/`) is unchanged — detail lives in the `engine-room/` overview + sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T13:01+02:00 — No route impact: the 5h coupler fix's only `dashboard/src/`-direct change is the `index.css` `warpSurgeUp`/`warpSurgeDown` keyframes (the coupler warp-core surge, frozen by `effects=off`); the render lives in `panels/engine-room/`. The `dashboard/src/` route model is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T11:55+02:00 — No route impact: slice 5h H2's only `dashboard/src/`-direct change is the `index.css` `closeoutSweep` keyframe (the closeout-train fill, frozen by the `effects=off` rule); the render lives in `panels/engine-room/` (its overview + sidecars). The `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`) is unchanged. Verification metadata pinned until closeout stamps the 5h H2 code commit.
- 2026-06-18T08:51+02:00 — No route impact: slice 5h H1 mirrors `LandingRefNode` + the additive `EngineProcessNode.landing` / `integrationStrategy` fields in `types/projection.ts` (and adds landing fixtures under `panels/engine-room/`); the `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`) this overview describes is unchanged — detail lives in the `engine-room/` overview + the `types/projection.ts` sidecar. Verification metadata pinned until closeout stamps the 5h code commit.
- 2026-06-17T22:45 — No route impact: the engine-room visual-parity pass (the 5g G6 blueprint backdrop + the
  cockpit Effects/Calm toggle, the `engine-room/` SVG decal layer, and the `grammar/Panel` `fill` height fix)
  is internal to those sub-routes; the `dashboard/src/` route model (`cockpit/`/`grammar/`/`panels/`/`data/`)
  this overview describes is unchanged — detail lives in those overviews + sidecars.
- 2026-06-17T16:15 — No route impact: slice 5g G5 lands the Engine Room live/teardown states
  (t12b/t14c/t18) + a green=active engine palette + a left-rail scroll fix — all internal to
  `panels/engine-room/` — plus an `index.css` `stopFlash` keyframe. The `dashboard/src/` route model
  (`panels/`/`grammar/`/`data/`/`cockpit/`) is unchanged; detail lives in the `engine-room/` overview +
  sidecars. Verification metadata pinned until closeout stamps the G5 code commit.
- 2026-06-17T14:00 — No route impact: `index.css` gained the `attnBreath` keyframe (the failure-overlay
  attention-badge breathing, 5g G3). Engine-room detail (surfaced in the `panels/engine-room` overview);
  the dashboard/src architecture this overview describes is unchanged. Verification metadata pinned until
  closeout stamps the G3 commit.
- 2026-06-17T13:30 — No route impact: `index.css` gained the Engine Room pod-stage motion keyframes
  (`chargeSweep` / `conduitDraw` / `pktRun`, 5g G2) + a `conduit-packet` freeze rule. These are engine-room
  detail (surfaced in the `panels/engine-room` overview); the dashboard/src architecture this overview
  describes is unchanged. Verification metadata pinned until closeout stamps the G2 commit.
- 2026-06-16T02:30 — slice 5f S1: the cockpit shell's machine-map views (Engine Room / Topology) go
  full-bleed (rails hidden, §4.1); added the dashboard suite's first component-render test
  (`cockpit/Cockpit.test.tsx`) and the shared jsdom stubs in `test/setup.ts`. The `dashboard/src/`
  route model is otherwise unchanged (detail in the `cockpit/` + `engine-room/` sidecars/overviews).
  Verification metadata pinned until closeout stamps the S1 code commit.
- 2026-06-15T19:35 — No route impact: slice 5e adds the `panels/engine-room/` sub-route (its own route overview + file sidecars) plus `types/projection.ts` / `dev/fixtures.ts` changes; the `dashboard/src/` route model this overview describes (the `panels/` / `grammar/` / `data/` / `cockpit/` split) is unchanged — detail lives in the `panels/` + `engine-room/` overviews and the file sidecars.
- 2026-06-15T17:00 — Created for slice 5d: the frontend re-architecture (Panda + React Aria,
  layered). Documents the layered styling architecture, the grammar/panels split, and the read-only
  boundary. Verification metadata pinned until closeout stamps the 5d code commit.
