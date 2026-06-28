# dashboard/src/panels/ — Cockpit Panels Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/src/panels/`                          |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-06-28T16:17+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

`panels/` holds the cockpit panels — each a read over the Zustand store,
rendered into the shell's rails/viewport — plus the slice-6e **Chats** terminal view (the one
interactive, full-bleed panel). `FlowTab.tsx` remains in the route as dormant diagnostic source, but
Task 29 S7 hides the Lifecycle Flow tab from the cockpit shell. As of slice 5d every presentational
panel renders through the shared
`grammar/Panel` chrome (self-scrolling box + sticky header) and styles itself with co-located
Panda `css()` / `cva()`; several add React Aria behavior (the `LifecycleList`/`EngineRoom` `ListBox`es
and the `Chats` `SessionList` switcher).

## Route Model

- `AttentionQueue.tsx` — left-rail: the server-ranked attention queue (note 06); severity-keyed
  `cva` rows + Motion enter/leave; lifecycle-bound items join to `analytics.taskDocuments` so rows
  lead with the task id/title while preserving the original lifecycle/gate text as detail; "Open"
  couples into the detail view. Task 23/24 adds a header `Clear` action that cancels/deletes every
  currently open gate item with a `gateId`, including stale gate-only rows without a `lifecycleId`.
  Task 29 S7 expands dismiss/clear to targetless actionable-drift rows and suppresses affected rows
  immediately in the store, releasing that suppression only when the backend write fails.
- `LifecycleList.tsx` — left-rail Operations list, labelled **"Tasks"** in the UI (header `Tasks · {n}`,
  empty state `No tasks.`, aria-labels "Group tasks by" / "Tasks"). **React Aria `ListBox`** (arrow-nav
  + type-ahead) grouped BY REPO | BY PHASE via a **React Aria `ToggleButtonGroup`** pivot. Rows are
  sidebar-scoped, not a dump of every projected task document: root/master documents (`kind: "master"` or
  `task.json`) and leaf docs matched to an active enclosure (`taskRoot` + `leafId` — including a
  **reopened** leaf's suffixed `leafId` admitted via the shared lifecycle, never a bare shared master
  lifecycle — with `cleanup !== "completed"`) become `taskdoc:<docPath>` rows; folder-keyed series fallback rows
  (`series:<seriesId>`) appear only when no master task document already covers them; runtime-only
  lifecycle rows (`lifecycle:<id>`) appear only for active-enclosure-backed work with no document row, and
  nest under their master via a computed parent key rather than floating as a standalone top-level row.
  Runtime state attaches by structured lifecycle/enclosure binding when present. Other projected
  planning/inactive/cleanup-completed leaves stay readable through typed links and the master sub-task
  index instead of flooding the sidebar. In `BY REPO`, active leaf task-document rows are
  grouped beneath their parent/root task with a visual indent and the child task document id matching
  the master task list; `BY PHASE` remains flat. Archived/deleted docs disappear because the
  observer stops projecting them; completed/abandoned status alone is not the sidebar disappearance rule.
  Long task titles are bounded to a single-line ellipsis in the row title span, with the listbox,
  section, and row containers constrained so a long title cannot widen the left panel and create a
  horizontal scrollbar; secondary/gate/progress chips are also bounded so they cannot crowd out the
  title. Hovering the title exposes the full label plus lifecycle/gate/repo/current-step context.
  `AgentPickupIndicator.tsx` renders `analytics.agentPickups` beside affected rows: fresh pending inbox
  entries show `waiting for agent`, and stale entries switch to a dismissible `check chat` warning.
- `GateResponder.tsx` — shared **Respond** control for lifecycle gates/asks: one button opens a
  request dialog with a human-readable request preview and collapsed raw-JSON diagnostics. For durable
  gates, Yes records a targeted `approve` through `data/actions.postGateDecision`, No requires a reason
  and records a targeted `reject` with `note`, Dismiss records a targeted `cancel` that deletes the gate
  interaction, and Chat is message-only through `data/sessions.deliverToSession` or
  `data/operatorInbox.postOperatorInbox`. Successful approve/reject/chat/dismiss submissions close the
  dialog after the server accepts the write/delivery. The request preview starts at 480px and can be
  resized with a keyboard/pointer handle without resizing the response controls.
- `DetailPanel.tsx` — the typed selected task document, series master, or runtime lifecycle: phase stepper, the canonical **Gate Respond** surface
  (durable gate or proto `ask`, routed through `GateResponder`), and the **task-document reader**
  (slice 6g / task 17): a concrete `analytics.taskDocuments` master/light/subTask selected via
  `taskdoc:<docPath>` renders by its own `kind` even when no lifecycle is attached; folder-keyed
  `analytics.series` remains the legacy master aggregation fallback. A master shows its overview
  (objective + ordered `sections`) + a clickable **sub-task index** (pinned in the sticky panel head +
  repeated in its authored section). Authored sub-task rows display the child `TaskDocNode.id` and sort
  by structured `createdAt` creation time when every row has it; missing creation metadata preserves
  authored order rather than parsing task-name prefixes or trusting parent label strings. Clicking a slice
  **drills in** to its full reader (objective/requirements/design/steps/proposed-code/decisions/refs)
  with the back control + a parent "↑" up-link in the **sticky header** (the drill state is lifted
  into the panel for this); prose renders through the `grammar/Markdown` component; **cross-master
  "→" rows** + a parent breadcrumb jump to another series' lifecycle via `onOpenLifecycle`. Then the
  lifecycle→worktree→provider spine and the token gauge. User-facing copy is "task" too — the
  no-selection placeholder reads "Select a task to inspect its phase, gate, and tokens." and the
  no-doc fallback "No task document bound to this task." Promoted leaf lifecycles may use enclosure
  `leafId` for the sticky header label, but readable content still comes only from a matching
  `analytics.taskDocuments` entry; contracts are not rendered as task documents. Leaf readers show a top
  Progress section before Objective while keeping the implementation-step copy later in the reader.
  Sub-task row progress and the reader's blue progress fill summarize visible top-level implementation
  steps, not nested substep totals. For runtime lifecycle selections, `DetailPanel` uses the parsed
  lifecycle id only to attach phase/gate/spine context and then renders the matching task document when
  one exists. Leaf lifecycle rows are different from root master rows: their enclosure `taskName` names
  the parent/root series, so parent `taskName` alone must never render the master; a matching projected
  `TaskDocNode` renders the leaf reader, and no projected doc shows the no-doc fallback. A selected master
  resolves sub-task rows against the full projected sibling task-document pool, not the sidebar rows, so
  authored leaves remain clickable from the master while missing authored documents remain static rows.
  Directly opened leaf documents and enclosure-backed leaf lifecycles show an `↑` parent/root backlink in
  the sticky header, resolved through structured series metadata rather than task-name parsing. Task 21
  adds the master-level `series tokens` scalar, displayed from server-projected `seriesTokenTotal` on
  folder-keyed and concrete master readers without recomputing from lifecycle gauges.
- `EngineRoom.tsx` + **`engine-room/`** — the enclosure-centered **Engine Room process map** (slice
  5e): an official-line strip (workspace providers grouped by provider label + runtime state, so duplicate
  same-state CGCs render as counted chips with repo-label hover detail) + a React Aria `ListBox` of worktree
  enclosures, and per selection a
  podracer process map (official line → code/memory worktrees → contract coupler → CGC/GrepAI
  engines), a boot-sequence timeline, and a diagnostics panel. Task 31 extends the provider display
  vocabulary so missing expected provider roles stay visible as empty/missing slots rather than disappearing
  as if no provider were expected. The process map is keyed by the store
  `gen` (bumped by `reset()` on a dev-bench scenario switch) so a switch remounts the canvas cleanly
  with no cross-scenario overlay bleed, and the right-panel `BootTimeline` renders a three-way
  sequence — Boot / Steady state / Tear-down — with the contract anchor leading the boot order and
  the abandon (skipped) / integration-conflict (blocked) tear-down step states corrected. Driven by
  the pure `engine-room/buildEngineRoomModel` over the server-composed `analytics.engineProcesses`;
  keeps the old `groupEngines` provider-stack view as a fallback. See [engine-room/ overview](engine-room/overview.md).
- `MemoryMirror.tsx` — the segmented coverage/drift bar per repo + ledger currency + stalest
  sidecars (slice-3b analytics); drift classes mapped by record (forward-compatible).
- `EventRiver.tsx` + `eventSummary.ts` — right-rail readable activity feed over the raw observer
  event tail. The component keeps trust-keyed provenance colour and renders summary packets; the
  formatter module owns schema-aware copy for `read.packet`, `tool.completed`, lifecycle phase/block
  events, gate events, actor display labels (`model` -> `agent`), existing task-context joins, task
  document title fallback for lifecycle-only history rows, stable time formatting, heartbeat hiding
  (now belt-and-braces — task 34 also filters `lifecycle.heartbeat` out of the raw river at the
  `/api/events` backend), raw unknown-kind fallback, and task-29 context-ready shaping: lifecycle-bound
  rows wait for live lifecycle, enclosure, or task-document context before rendering so reload order
  cannot briefly paint stale raw ids. Task 29 S7 also waits for the raw event stream's backend `ready`
  marker before showing an empty history and removes the UI-side newest-row cap; the backend retention
  policy now owns event lifetime. **Task 34** virtualizes the feed with `@tanstack/react-virtual` over
  the store's bounded sliding window (the newest ~2000 rows), so the list mounts only the visible rows
  (no hard display cap) while staying memory-bounded.
- `Hangar.tsx` — the persistent (never-reaped) worktree enclosures with closeout/integration/cleanup
  badges; worktree-bound projected gates render the real `GateResponder` control, while non-gate
  availability still renders display-only affordances.
- `Topology.tsx` — the radial constellation hero: a React-wrapped imperative `<canvas>` (the renderer
  stays in `topology/constel.ts`, driven via refs); container/tip/legend styled by Panda. Task 33: it now
  reads the store's `activeWorktreeGroups` and runs `topology/model.activeTopologyInputs` to bound the
  inputs to active worktree enclosures before `buildTopology`.
- `Chats.tsx` + `SessionList.tsx` + `Terminal.tsx` — the **Chats** view (slice 6e), the visible Mode B2
  surface: a full-bleed **"＋ Terminal"** control that asks the `POST /api/terminal` opener to spawn +
  own a session (a shell at the workspace root, 6e-2a), a left-rail **`SessionList`** switcher of open
  sessions (slice 6e-2c — a React Aria `GridList`, single-select = active session, with Task 22
  per-row End action; covered by `SessionList.test.tsx`), and the selected session's
  lazy-mounted `Terminal` — an
  imperative `@xterm/xterm` terminal (FitAddon + `ResizeObserver` → `sendResize`, the known resize
  risk) over the `data/terminal` WebSocket client (binary PTY bytes in, `{type:stdin|resize}` out).
  xterm is **code-split** (it probes the canvas on import + can't mount in jsdom); the protocol logic
  is unit-tested in `data/terminal.test.ts`. Per-harness launch buttons — one per **detected** harness
  (Claude Code / Codex / Pi.dev), icon-left/name-right, sharing ＋ Terminal's golden look (6e-2c) — sit
  beside ＋ Terminal (6e-2b), each spawning that agent at the workspace root; the detection-driven
  render is covered by `Chats.test.tsx`. When the cockpit has a selected lifecycle, newly launched
  sessions inherit that `lifecycleId`, and an active untagged session can be attached; `SessionList`
  shows the tag. A **`SessionComposer`** (slice 6e-3) docks below the terminal
  and injects a block of text into the active session's stdin as a bracketed paste (the on-ramp to 6f);
  covered by `SessionComposer.test.tsx`. The session registry lives in the `data/sessions` store.
	  Task 22 hydrates this registry from the backend terminal catalog after a browser reload/dashboard
	  restart, persists the last active session id, renders exited/terminated rows as status panels instead
	  of trying to reconnect, and now mounts restored rows on first selection: the restored active row
	  attaches immediately, unvisited rows wait until selected, and visited rows stay mounted while hidden.
	  End/terminate releases the session label for reuse. Backend-persisted create/end changes broadcast
	  id-bearing catalog invalidations across browser tabs; receivers remove terminated ids immediately,
	  re-fetch the catalog, and can clear rows on a successful empty response.
	  Persistence is covered by `Chats.test.tsx`.
- `EmptyStateBackdrop.tsx` — a **shared empty-state panel** (slice 07b polish): a faint, effects-gated
  boomerang-video atmosphere behind centered empty-state text, lifted from the engine-room G6 backdrop
  (`engine-room/engineRoomStyles` `backdrop`/`backdropVideo`). The message children always render; the
  `aria-hidden` `<video>` mounts as a direct static child only when `useShouldAnimate()` is true (absent
  under calm-cockpit / reduced-motion) — pure atmosphere, never state. Any slow zoom and playback cadence
  belong to the pre-rendered 60fps boomerang MP4 assets, not a DOM/CSS/Motion transform layer. Used by
  `DetailPanel`'s no-selection state (battle cruiser) and `Chats`'s no-session state (adjutant); the host
  slot must be a flex column so its `flex:1` canvas fills. Covered by `EmptyStateBackdrop.test.tsx`.
- `HighlightComposer.tsx` — the slice-6f **highlight → context-package** composer: a cockpit text
  selection raises a React Aria `Popover` (mounted cockpit-wide in `CockpitShell`, the cockpit's first
  overlay) to send the selection + a message into a chat session's stdin — single chat / a selector /
  create-on-Enter when none is open, plus a ＋ new-chat button; **deliver + submit** over the live
  `{type:stdin}` channel via `data/sessions`. When a lifecycle is selected, open-chat targets are
  filtered to sessions tagged with that lifecycle and create targets inherit the lifecycle id. No silent
  action (a selection only *raises* it). Covered by `HighlightComposer.test.tsx`; the pure selection
  rules by `data/selection.test.ts`.
- `FlowTab.tsx` — the former **Lifecycle Flow** view (task 26): a **static** diagnostic visualization of the
  build-job lifecycle (no store read — module-level data + co-located Panda `css`/`cva`). Task 29 S7
  removed it from the cockpit `View` union and mode bar, so this source is dormant until a dev-only
  mount is reintroduced. It renders the
  lifecycle in TWO regimes: a non-linear **front half** — a one-time prose `RUNDOWN` array emitted by
  `lifecycle_start` (reframe → research → job-selection → `⟁ task-file-exists?` junction → `task_doc`),
  prose rather than per-tool hints because the research tools fire unpredictably and the junction isn't a
  tool call — and a **`LINEAR`** chain of `Node`s from `worktree_start --dry-run` → `lifecycle_end`, where
  each gate `Node` carries a `rides` annotation (the turn-end notification auto-fires when that gate tool —
  dry-run / preview / task_doc-create — is called, so the agent can't forget it). Edge colour encodes
  `nextStatus`: mint = wired today (`guidance.lifecycle_guidance`), amber dashed = this series. It is the
  human-readable SPEC the task-27 next-step engine
  ([next_step.py](agents-remember/mcp/src/agents_remember/mcp/tools/next_step.py)) was built to match.
  It is no longer visible in the shipped dashboard cockpit.

## Invariants And Boundaries

- **Presentational, near-read-only** — panels read the store and render (no clock; ages are
  server-computed). The interactive exceptions are `GateResponder` (Yes/No POST developer-attributed
  gate decisions; Chat sends instructions through hosted chat or the external operator inbox) and the
  `Chats`/`Terminal` view (slice 6e
  — a bidirectional Mode B2 WebSocket: keystrokes/resize out, PTY bytes in). Selection stays
  ephemeral UI state lifted to the cockpit shell.
- **Panda + React Aria** — styling is co-located Panda `css`/`cva` keyed on tokens + React Aria
  `data-*` conditions; behavior (keyboard/focus/ARIA) is React Aria. No global panel CSS.
- **The Panel primitive owns chrome** — bg/border + scroll + the sticky header band; panels pass a
  sizing `className` (flex / max-height) for their rail/viewport slot.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The shared panel chrome every panel renders through. | [grammar/Panel.tsx](agents-remember/dashboard/src/grammar/Panel.tsx) |
| The pure selectors the panels read (queue, tree, engine state, drift segments). | [data/selectors.ts](agents-remember/dashboard/src/data/selectors.ts) |
| The projection node shapes the panels render. | [observer/projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |
| The next-step engine `FlowTab.tsx` is the human-readable SPEC for. | [tools/next_step.py](agents-remember/mcp/src/agents_remember/mcp/tools/next_step.py) |

## Update History

- 2026-06-28T16:17+02:00 — Task 35 route impact: `LifecycleList` now also admits a **reopened** leaf's
  suffixed-leaf enclosure (`leafId` = stem/`id` + cycle suffix, e.g. `…-s7`) on the combined shared-lifecycle
  + suffixed-leaf match (never a bare shared master lifecycle), and runtime-only enclosure-backed rows nest
  under their master via a computed parent key — so a re-opened/edited task no longer renders as a standalone
  phantom node. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-28T13:54+02:00 — Task 34 route impact: `EventRiver.tsx` now **virtualizes** the activity feed
  with `@tanstack/react-virtual` over the store's bounded sliding window (newest ~2000 rows), mounting
  only the visible rows (no hard display cap) while staying memory-bounded; the `/api/events` backend
  also now filters `lifecycle.heartbeat` out of the raw river, so the formatter's heartbeat hiding is
  belt-and-braces. Updated the `EventRiver.tsx` Route Model bullet. Verification metadata pinned until
  closeout stamps the task-34 code commit.
- 2026-06-28T07:45+02:00 — Task 33 route impact: `Topology.tsx` now filters to active worktree groups via
  `activeTopologyInputs` (reading the store's `activeWorktreeGroups`) before `buildTopology`. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-28T07:43+02:00 — Task 29 S7 route impact: Event River no longer has a frontend newest-row
  cap and waits for the raw stream `ready` event before showing an empty feed, AttentionQueue
  dismiss/clear now optimistically suppresses lifecycle/gate/actionable-drift rows while writes are in
  flight, and `FlowTab.tsx` is documented as dormant because the Lifecycle Flow tab is hidden from the
  cockpit. Verification metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-28T05:38+02:00 — Task 29 route impact: Event River rendering now gates
  lifecycle-bound rows until lifecycle/enclosure/task-document context is available, while lifecycle-less
  workspace diagnostics can still render raw fallbacks. Verification metadata pinned until closeout
  stamps the task-29 code commit.
- 2026-06-28T03:21+02:00 — Task 31 route impact: `LifecycleList` now matches active leaf task documents
  against either the file stem or the authored `TaskDocNode.id`, restoring browser-dashboard leaf 31 under
  its parent master in Operations; the Engine Room panel route also renders expected-but-missing provider
  roles using the new provider boot-node state. Verification metadata pinned until closeout stamps the
  task-31 code commit.
- 2026-06-27T18:43+02:00 — Task 26 route impact: added the `FlowTab.tsx` **Lifecycle Flow** view to the
  panels inventory — a static (no-store) diagnostic of the build-job lifecycle in two regimes (a prose
  `RUNDOWN` front half emitted by `lifecycle_start` and a `LINEAR` worktree_start→lifecycle_end chain with
  gate `rides` annotations), wired as a full-bleed cockpit `flow` view and serving as the human-readable
  SPEC the task-27 `next_step.py` engine matches; dev frontend only (production bundle not rebuilt this
  task). Verification metadata pinned until closeout stamps the task-26 code commit.
- 2026-06-27T03:04+02:00 — Task 22 follow-up: Chats removed the local Hide row action; End is now the
  only session-list action, and id-bearing terminate invalidations remove rows across tabs without
  allowing stale catalog echoes to repaint them.
- 2026-06-27T01:25+02:00 — Task 22 follow-up: Chats now listens for cross-tab terminal catalog
  invalidations, re-fetches durable rows when another tab opens/ends sessions, and broadcasts after
  backend-confirmed End so multiple browser tabs stay in sync.
- 2026-06-27T01:03+02:00 — Task 22 follow-up: Chats treats End/terminate as label release, so terminated
  Claude chats do not force the next Claude label upward.
- 2026-06-27T00:25+02:00 — Task 22 follow-up: corrected the Chats route model for mount-on-first-selection
  after refresh; hidden restored xterms no longer initialize before they are selected, and visited tabs
  still keep their xterm buffers.
- 2026-06-26T23:15+02:00 — Task 22 route impact: `Chats.tsx` and `SessionList.tsx` now expose durable
  catalog sessions, status badges/panels, last-active restore, and backend terminate for dashboard-owned
  terminals. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T20:18+02:00 — Task 21 route impact: `DetailPanel` master readers now show the
  server-projected `seriesTokenTotal` aggregate, with component coverage in `DetailPanel.test.tsx`.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T19:40+02:00 — Task 20 reopened: Event River route model now records
  the task-document title fallback for retained event-history rows whose
  lifecycle id no longer has a live lifecycle projection. Verification metadata
  pinned until closeout stamps the reopened task-20 code commit.
- 2026-06-26T18:14+02:00 — Task 20 route impact: Event River now includes the
  new `eventSummary.ts` formatter module and renders a readable activity feed
  over known observer events while preserving raw-event diagnostics and trust
  provenance. Verification metadata pinned until closeout stamps the task-20
  code commit.
- 2026-06-25T14:02+02:00 — Task 24 reopened: `AttentionQueue` Clear now includes stale gate-only rows and sends gate-id-only cancel through the serving route.
- 2026-06-25T13:20+02:00 — Task 23/24: panels route now covers gate Dismiss/delete, attention Clear, and the `AgentPickupIndicator` waiting-for-agent/check-chat task-row feedback.
- 2026-06-25T07:26+02:00 — Task 19 gate interaction polish: `GateResponder` now has separate durable
  Yes/No decision paths and a message-only Chat path, renders readable gate previews with diagnostics
  behind details, and gives leaf prompt previews a 480px resizable area. `AttentionQueue` now renders
  lifecycle-bound rows with task id/title first. Verification metadata pinned until closeout stamps the
  code commit.
- 2026-06-25T02:53+02:00 — Operations title-overflow correction: `LifecycleList` now constrains the
  listbox/section grid tracks, row minimum widths, and secondary metadata chips so long task titles
  ellipsize inside the left rail instead of creating a horizontal scrollbar or disappearing. Detail
  lives in the `LifecycleList.tsx` and `LifecycleList.test.tsx` sidecars. Verification metadata pinned
  until closeout stamps the code commit.
- 2026-06-24T21:49+02:00 — Task 17 route correction: cleanup-completed leaf enclosures no longer count
  as active sidebar enclosures; their task docs remain reachable through master/taskdoc navigation.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T18:13+02:00 — Empty-state backdrop zoom-stability pass: refreshed the
  `EmptyStateBackdrop.tsx` route-model bullet for the final static direct-video contract. The shared panel
  still provides the same effects-gated boomerang-video atmosphere, but runtime zoom layers are excluded;
  the 60fps MP4 assets own the slow zoom/cadence. Detail lives in the `EmptyStateBackdrop.tsx` and
  `EmptyStateBackdrop.test.tsx` sidecars. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-06-24T18:11+02:00 — Task 17 route correction: Operations and Detail now label authored leaf rows
  from the child `TaskDocNode.id`, with parent sub-task `number` only as fallback data. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-24T18:02+02:00 — Task 17 route correction: Operations and Detail now display structured
  sub-task numbers for leaf labels, while creation metadata controls ordering/placement and no filename
  parsing is introduced. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T17:51+02:00 — Task 17 Operations hierarchy route update: `LifecycleList` now nests
  admitted active leaves beneath their parent/root task in `BY REPO`, and `DetailPanel` gives directly
  opened leaf documents a structured parent/root backlink. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-24T17:20+02:00 — Task 17 sidebar/master navigation route correction: `LifecycleList` now scopes
  the Operations sidebar to root/master docs, enclosure-matched leaves, series fallbacks, and
  enclosure-backed runtime fallbacks, while `DetailPanel` keeps master sub-task navigation wired to the
  full projected sibling document pool. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T16:39+02:00 — Task 17 Operations route correction: `LifecycleList` is task-document-first
  with typed `taskdoc:` / `series:` / `lifecycle:` row keys, completed unarchived docs stay visible,
  and `DetailPanel` renders concrete selected documents before lifecycle/series fallbacks. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-24T15:37+02:00 — Task 17 follow-up route correction: live projection inspection showed
  `analytics.series` is the master surface while leaf rows carry parent `taskName`; the DetailPanel route
  now bridges to the master only for root task identity and otherwise requires projected leaf task docs
  for leaf reader content. Verification metadata pinned until closeout stamps the follow-up code commit.
- 2026-06-24T15:23+02:00 — Task 17 follow-up route impact: clarified the DetailPanel identity rule
  that `taskName` is parent/root-series metadata for leaf lifecycles; direct leaf task documents render
  before the folder-keyed master bridge. Verification metadata pinned until closeout stamps the
  follow-up code commit.
- 2026-06-24T13:59+02:00 — Task 17 follow-up route impact: refreshed the `DetailPanel.tsx` route model
  for top-level implementation-step progress summaries in master sub-task rows and leaf reader
  progress fills; nested substeps no longer inflate those orientation counts. Verification metadata
  pinned until closeout stamps the follow-up code commit.
- 2026-06-24T12:53+02:00 — Task 17 follow-up route impact: refreshed the `DetailPanel.tsx` route model
  for root master rows that select an inferred task-id lifecycle; the panel now uses projected
  enclosure `taskName` to find the folder-keyed `analytics.series` master. Verification metadata pinned
  until closeout stamps the follow-up code commit.
- 2026-06-24T12:37+02:00 — Operations title-overflow fix: refreshed the `LifecycleList.tsx` route model
  for single-line title ellipsis and native hover titles carrying the full task label plus row context.
  Detail lives in the `LifecycleList.tsx` and `LifecycleList.test.tsx` sidecars. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-24T12:21+02:00 — Task 17 route impact: refreshed the `DetailPanel.tsx` route model for
  folder-keyed `analytics.series` master rendering, labelled master sub-task rows, structured
  creation-order sorting, and the new top Progress section in leaf readers. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-24T08:59+02:00 — Detail task-document correction: refreshed the `DetailPanel.tsx` route model
  for promoted leaf lifecycles whose visible title comes from enclosure metadata while readable content
  remains limited to matching JSON task documents. Verification metadata pinned until closeout stamps
  the code commit.
- 2026-06-24T08:40+02:00 — Operations label fix: refreshed the `LifecycleList.tsx` Route Model bullet
  for enclosure/task-backed row labels, covering promoted fleeting lifecycles that should display the
  leaf enclosure name rather than the stable raw lifecycle id. Detail lives in the `LifecycleList.tsx`
  and `LifecycleList.test.tsx` sidecars. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-06-24T06:26+02:00 — Engine Room official-strip aggregation: the route model now records that
  `EngineRoom.tsx` groups official workspace providers by provider label + runtime state, rendering duplicate
  same-state CGCs as counted chips with hover-title repo detail. Detail lives in the `EngineRoom.tsx` and
  `EngineRoom.test.tsx` sidecars. Verification metadata pinned until closeout stamps the official-strip
  aggregation code commit.
- 2026-06-23T15:05+02:00 — Task 10 dashboard fallback: `GateResponder` now routes missing-hosted-session responses to the external operator inbox through `data/operatorInbox`, with queued/error status coverage in `GateResponder.test.tsx`. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-23T13:45+02:00 — Task 11: added `GateResponder.tsx` / `.test.tsx` and updated the panel route
  model for chat-routed Gate Respond. `DetailPanel` now uses the responder for durable gates and proto
  asks; `LifecycleList` shows gate badges; `Chats` / `SessionList` / `HighlightComposer` carry hosted
  chat lifecycle identity; Hangar and Engine Room diagnostics use the responder as the secondary
  worktree-gate surface. Verification metadata pinned until closeout stamps the task-11 code commit.
- 2026-06-23T13:35+02:00 — No route impact: slice-12 topology render fix — `Topology.tsx` made the constellation canvas absolutely-positioned (out of flow → no ResizeObserver growth loop) and rendered the `Panel` with `fill` (so it fills the slot). Behaviour-preserving layout fix; the panels route model is unchanged.
- 2026-06-23T07:25+02:00 — UI copy rename (user-facing lifecycle → task): refreshed the `LifecycleList.tsx`
  Route Model bullet for the operations panel's "Tasks" copy (header `Tasks · {n}`, empty state `No tasks.`,
  aria-labels "Group tasks by" / "Tasks") and the `DetailPanel.tsx` bullet for its task-facing placeholders
  ("Select a task to inspect…", "No task document bound to this task."). Display copy only — the unit is still
  the `lifecycle` under the hood; the eight-panel route inventory is unchanged. Detail lives in the
  `LifecycleList.tsx` / `DetailPanel.tsx` sidecars. Verification metadata pinned until closeout stamps the
  rename code commit.
- 2026-06-23T04:20+02:00 — Slice 07b polish: added the shared `EmptyStateBackdrop.tsx` panel — a faint,
  effects-gated boomerang-video atmosphere behind centered empty-state text (lifted from the engine-room
  G6 backdrop) — and wired it into `DetailPanel`'s no-selection state (battle cruiser) and `Chats`'s
  no-session state (adjutant); covered by `EmptyStateBackdrop.test.tsx`. Added a Route Model bullet for
  the new shared panel; detail lives in its sidecar + the `DetailPanel` / `Chats` sidecars. Verification
  metadata pinned until closeout stamps the slice-07b code commit.
- 2026-06-23T01:40+02:00 — No route impact: slice 07b v1 gives `EventRiver.tsx` its one per-kind treatment (a `read.packet` renders "Read: <basename>" + the read's repo + full-path-on-hover, everything else generic) and adds `EventRiver.test.tsx`; no new panel enters the route inventory and the eight-panel route model this overview describes is unchanged — detail lives in the `EventRiver.tsx` / `EventRiver.test.tsx` sidecars. Verification metadata pinned until closeout stamps the slice-07b code commit.
- 2026-06-22T16:00 — Route refresh (05o review round): `EngineRoom.tsx` keys its process-map canvas by the store `gen` so a dev-bench scenario switch remounts it cleanly (no cross-scenario overlay bleed), and the right-panel `BootTimeline` now renders a THREE-WAY sequence — Boot / Steady state / Tear-down — with the contract anchor leading the boot order and the abandon/conflict tear-down step states corrected; detail lives in the per-file sidecars under `panels/` and `panels/engine-room/`. Verification metadata pinned until closeout stamps the 05o code commit.
- 2026-06-21T02:44+02:00 — slice 6g: `DetailPanel` became the task-document **master-series reader** — master overview + clickable sub-task index (pinned in the sticky head + in-section), in-panel drill-in into a slice reader with the back/parent up-link in the sticky panel header, markdown-rendered prose (`grammar/Markdown`), and cross-master "→" links + parent breadcrumb that jump lifecycles (`onOpenLifecycle`). Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-19T15:59 — Task 6 slice 6f-1: added `HighlightComposer.tsx` (+ `data/selection.ts`) — a cockpit-wide composer a text selection raises to send a context package (selection + message) into a chat session (single/selector/create-on-Enter + ＋ new chat), reusing the live stdin channel. No silent action. Covered by `HighlightComposer.test.tsx` + `data/selection.test.ts`. Verification metadata pinned until closeout stamps the 6f-1 code commit.
- 2026-06-19T14:05 — Task 6 slice 6e-4: the **Chats** view's session registry moved into the `data/sessions` store, and every open session's `Terminal` now stays mounted (inactive ones hidden via CSS) so switching tabs no longer unmounts a live terminal; the backend PTY spawn (`serving/terminal.py`) gained a controlling terminal (`os.login_tty`) so tmux honors resize. Persistence covered by `Chats.test.tsx` + the new `data/sessions.test.ts`. Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-19T05:48 — Task 6 slice 6e-3: the **Chats** view gained a `SessionComposer` (context injection) docked below the terminal — it sends a block of text into the active session's stdin as a bracketed paste (the on-ramp to 6f); covered by `SessionComposer.test.tsx`. Verification metadata pinned until closeout stamps the 6e-3 code commit.
- 2026-06-19T06:39+02:00 — No route impact: an engine-room crash fix guards the `landing` read in `engine-room/EnclosureCanvas` (a node without the slice-5h `landing` field no longer crashes); the `panels/` route model this overview describes is unchanged — detail lives in the `engine-room/` overview + sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T04:38 — Task 6 slice 6e-2c: the **Chats** view's horizontal session tab strip became a left-rail **`SessionList`** switcher (extracted to a React Aria `GridList` component — single-select = active session, per-row close ✕; `SessionList.test.tsx`), and the per-harness launch buttons now share ＋ Terminal's golden look (the grey ones read as disabled). Refreshed the Chats Route Model bullet + the React Aria note. Verification metadata pinned until closeout stamps the 6e-2c code commit.
- 2026-06-18T21:27 — Task 6 slice 6e-2b: the **Chats** view gained per-harness launch buttons — `fetchHarnesses` (`GET /api/harnesses`) renders a button per **detected** harness (Claude Code/Codex/Pi.dev, icon-left/name-right) beside ＋ Terminal; added `Chats.test.tsx` (detection-driven render). Refreshed the Chats Route Model bullet. Verification metadata pinned until closeout stamps the 6e-2b code commit.
- 2026-06-18T17:40 — Task 6 slice 6e-2a: the **Chats** view became a **create** surface — a "＋ Terminal" control spawns a dashboard-owned shell session via the `POST /api/terminal` opener (no longer attaching to a store lifecycle), rendered as a closable tab. Refreshed the Chats Route Model bullet. Verification metadata pinned until closeout stamps the 6e-2a code commit.
- 2026-06-18T16:50 — Task 6 slice 6e-1: added the **Chats** view (`Chats.tsx` + the lazy `Terminal.tsx` xterm wrapper) — the visible Mode B2 surface, the panels' first bidirectional-interactive surface (keystrokes/resize ↔ PTY over the `data/terminal` WebSocket). Updated the Route Model + the near-read-only invariant. Verification metadata pinned until closeout stamps the 6e-1 code commit.
- 2026-06-18T18:00+02:00 — No route impact: slice 5h's ledger popover threads `officialLedger` through `EngineRoom` → `EnclosureProcessMap` (resolved from `analytics.ledgers` by repo) for the official coupler; the `panels/` route model this overview describes is unchanged — detail lives in the `engine-room/` overview + the `EngineRoom.tsx` / `EnclosureProcessMap.tsx` sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T15:00 — Task 6 slice 6c Part B: `DetailPanel`'s display-only gate banner became the **Gate Review drawer** — the durable gate's decision verbs POST to `/api/actions` via the new `data/actions.ts` (the panels' first write path); the proto-gate `ask` falls back to the display banner. Verification metadata pinned until closeout stamps the 6c Part B code commit.
- 2026-06-17T22:45 — No route impact: the engine-room visual-parity pass (the 5g G6 backdrop + the restored
  SVG decal layer + the `grammar/Panel` `fill` height fix) is internal to the `engine-room/` route and the
  `grammar/Panel` primitive; the panels route model (the eight panels + their roles) this overview describes
  is unchanged — detail lives in the `engine-room/` + `grammar/` overviews and the `EngineRoom` sidecar.
- 2026-06-17T16:15 — No content impact: slice 5g G5 (Engine Room live/teardown overlays t12b/t14c/t18 +
  the green=active engine palette + the enclosure-rail scroll fix) is internal to the `engine-room/` route;
  the panels route model (the eight panels + their roles) this overview describes is unchanged — detail
  lives in the `engine-room/` overview + sidecars.
- 2026-06-16T03:50 — No content impact: slice 5f S5 added the Engine Room header's lifecycle-phase pulse (the `phaseChip` animates while the selected enclosure is in a human-gated landing phase, T12–T18) + `EngineRoom.test.tsx`; the panels route model (the eight panels + their roles) this overview describes is unchanged.
- 2026-06-16T03:35 — No content impact: slice 5f S3 added `AttentionQueue.test.tsx` (a §9 blocked-start alarm-parity render test — no `AttentionQueue` source change; the panel renders items generically by severity) and the Engine Room T4 promotion morph (internal to `engine-room/`); the panels route model this overview describes is unchanged.
- 2026-06-16T02:30 — No content impact: slice 5f S1 gave `EngineRoom.tsx` a full-width 3-zone layout (header + stack list | pod stage | boot+diagnostics-right, §4.2); the panels route model (the eight panels + their roles) this overview describes is unchanged — detail lives in the `engine-room/` overview + sidecars.
- 2026-06-16T01:55 — No content impact: slice 5f S0's Engine Room motion foundations (the `useShouldAnimate` honest-motion gate, SVG conduits, and `worktreeGroup` keying) are internal to the `engine-room/` route — captured in its overview + file sidecars; the panels route model this overview describes is unchanged.
- 2026-06-15T19:35 — slice 5e: reworked `EngineRoom.tsx` into an enclosure-centered process map
  backed by the new `engine-room/` module (pure `buildEngineRoomModel` + Panda/React Aria
  components: stack list, process map, boot timeline, diagnostics); added the `engine-room/` child route.
- 2026-06-15T17:00 — Created for slice 5d: all eight panels migrated onto the `Panel` primitive +
  co-located Panda styling, with React Aria `ListBox` (LifecycleList) and `ToggleButtonGroup`
  (pivot). Verification metadata pinned until closeout stamps the 5d code commit.
