# dashboard/src/cockpit/Cockpit.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/cockpit/Cockpit.tsx`              |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-08T21:20+02:00                           |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`       |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `../overview.md`                                |

## Governing Overview

[dashboard/src overview](../overview.md)

## 260731-EFA-L8 Change

The frontend-rail split re-wired this file's imports to the new kebab-case
component folders (`detail-panel/`, `lifecycle-list/`, `sessions-view/`) and the
engine-room styles barrel, and the lint remediation touched memoization and hook
dependencies. View-map behavior is unchanged: `SessionsView` stays mounted and its
display toggles (`display: view === "chats" ? "flex" : "none"`).

## Purpose

The production cockpit shell owns persistent chrome, route/takeover selection, live projection
wiring, and keep-alive full-page layers. FEUI-L8 exposes Operations, Engine Room, Files, and exactly
one Chats destination; Operations is initial, the former Sessions item is retired, and the canonical
Chats layer is the persistently mounted session cockpit. The shell owns the one catalog poll plus
eager/cross-tab reconciler, threads selected lifecycle/leaf/task context into `SessionsView` and
`RailChat`, and moves highlight focus/view only after accepted delivery names an exact live session.
Within the full-page cockpit, `ChatContextBar` owns launch and attach/move controls.

RailChat remains the contextual right-rail surface beside Operations; Notes/Change-Set takeovers and
the other existing routes retain their established ownership. The dev lifecycle-design canvas stays
outside production navigation.

## Code Commentary

### FEUI-L9R Reviewed Candidate Delta

`ServingBuildStamp` now compares the executing bundle fingerprint with
`servingBuild.dashboardBuild`. It exposes unknown, matching, or mismatching diagnostic evidence;
only a definite mismatch renders the explicit `reload client` button. Reload remains operator-owned
because a stateful terminal tab may contain drafts or interaction. An older server without the
optional fingerprint remains neutral rather than falsely stale.

### Logic

Since L15 the cockpit top bar renders the muted servingBuild stamp (commit short-hash + boot time from the state payload) — the ghost-process lesson made visible: a stale dashboard server is identifiable at a glance. **260707-HFX2-L2 (R5)** adds a second top-bar indicator right beside it: `AgentNotifierHeartbeatBadge` (renamed from `SupervisorHeartbeatBadge` in 260713-TES-L1) reads `s.agentNotifierHeartbeat` from the store (the store accepts the legacy `supervisorHeartbeat` wire key as a fallback during the rename window) and renders nothing when `lastTickAt` is `null` (the agent-notifier has never ticked in this workspace — `dashboard.autoStart` is opt-in, so "no row yet" is not itself an alarm); once a tick exists, it shows `"agent-notifier ok/stale <age>"` with a `title` tooltip naming the exact `lastTickAt`/`staleCutoffSeconds`. **260718-CHATS-L5P (R5/A4/B9):** the age is now HUMANIZED via `humanizeDuration(ageSeconds*1000)` (`6 d 2 h`, never the raw `9512.1m`), and a long-stale agent-notifier degrades to a QUIET-distinct amber `caution({sev:"warn"})` — NOT the pulsing cried-wolf red it used past the cutoff before (six-day staleness is expected for an idle workspace, not a fault to alarm on); a fresh heartbeat stays the muted `dim` class. **260707-HFX2-L8 (R6)** extends the same badge with `inbox redeliverable/pending` and latest sweep duration, so a growing operator-inbox storm is visible beside the heartbeat before staleness fires. This is issue #15's "the watcher must be code AND watched" made visible in the SAME top bar that already carries `servingBuild` — "the last turtle is the developer's glance."

`Cockpit` wires the two SSE streams (`connectState`, `connectEvents`) then renders
`CockpitShell` (split out so the dev gallery renders the same surface against fixtures).
**260715-FEUI-L2 (S1/S2)** makes `Cockpit` the standing owner of the shared session feed: the
`/api/events` EventSource now feeds TWO consumers on ONE connection — the Event River
(`pushEvent`, unchanged, still receives backlog lines) and the seat-event reconciler
(`data/seatEvents.applySeatEventLine`), whose application is routed through
`createGatedSeatEventApplier()` — a PER-CONNECTION backlog gate: `ready` opens it,
the EventSource `error` (`connectEvents`' new `onInterrupt`) re-closes it, so a reconnect's
pre-`ready` backlog replay (incl. the undecodable-cursor full-window replay) can never regress
live rows (L2 review finding 2). A third effect starts the refcounted 2500 ms catalog poll driver
(`data/catalogPoll.startCatalogPollDriver`) unconditionally, so the session feed stays alive with
ANY view — or none — in front. `CockpitShell` is the sole production owner of both the driver and
the eager/cross-tab reconciler; `SessionsView` consumes the resulting shared store without starting
a second timer. `CockpitShell`
holds `view` + `selectedId` state and derives `fullBleed = view === "files" || view === "engine" ||
view === "topology" || view === "chats"`. Both the **File Viewer** (slice L2) and **Chats** views are
full-bleed AND kept mounted as persistent CSS-hidden layers in `CockpitShell` (a `filesLayer` / `chatsLayer`
div toggled by `display`), not routed through `ViewBody`, so switching tabs never unmounts them: the File
Viewer's repo/scope selection, open file, and expanded tree state survive a switch, as does the live xterm
terminal + WebSocket.
Task 29 wires the raw Event River readiness signal through this shell: `connectEvents` receives
`markEventsHydrated` as its `ready` callback, so the right rail can show "Syncing event history." until
the backend has emitted the retained backlog and the explicit ready marker.
The body is the `bodyGrid` cva: the railed 3-column shell when `!fullBleed`, a single full-width column
when `fullBleed`. The two `<aside>` rails (`rail--left` = attention queue + lifecycle list;
`rail--right` = event river) render only when `!fullBleed`, so a machine-map view unmounts them for a
clean expand; they fade back in via a `motion.aside` gated by `useShouldAnimate()` (instant under
`data-effects=off` / reduced-motion, keeping snapshots stable). `ViewBody` switches the centre by
`view`; the mode bar is the `<ModeBar>` primitive. `open(id)` selects a node AND jumps to Operations.
**Operations-integration L4** adds a `changeSet` TAKEOVER: `CockpitShell` holds a `changeSet:
ChangeSetTarget | null` state; when set, a full-bleed `<ChangeSetViewer>` shows (its back link clears it,
restoring the rails), and `open(id)` plus a mode-bar switch (`changeView`) also clear it — the takeover is
transient (a task-scoped screen), not a standing view. `onOpenChangeSet` is threaded through `ViewBody`
into `DetailPanel`. **L4a** changes the takeover from *replacing* the railed body to **overlaying** it:
the railed body is now kept mounted but `display:none`/`aria-hidden` while the takeover shows (the same
hidden-not-unmounted pattern as the File Viewer + Chats layers), so the `DetailPanel`'s drill state (which
leaf you were reading) survives — the viewer's back link returns you to exactly where you opened it from
(a drilled leaf), instead of `DetailPanel` remounting fresh at the master overview.
`TopBar` shows the master-caution (`⚠ N waiting`, severity-keyed from `selectQueue`). **260718-CHATS-L5P
(RV-4/R4):** the waiting chip renders ONLY when `queue.length > 0` — a reassurance zero wearing an alarm
glyph is a lie, so an empty queue shows nothing (absence = clear); a real alarm is still never hidden in
a full-bleed view. **Top-bar humanization + honesty (V15/V6/R7):** `ServingBuildStamp`'s `up` label is a
HUMANIZED uptime (`humanizeDuration(Date.now() - bootedAt)`, one time format in the bar; the absolute
start stamp stays in the tooltip — was a second 12h clock, V15); the brand `title` + each fact-chip
(`dim`, `caution`, `connBadge`) are `whiteSpace:nowrap` and the `statusRow` is `flex-wrap:wrap` so the
bar wraps BETWEEN chips, never mid-phrase (`1 running · 0/blocked`, V6); and the lifecycle counts are
explicitly scope-labeled `tasks N running · N blocked · N tok` with a tooltip naming them
lifecycle/task-scoped (a different authority from the Chats rail's chat-seat states — R7, no backend
change). **260731-EFA-L4** gives that same `dim` span a `data-testid="task-metrics"` and appends one
CONDITIONAL segment to it: `· {metrics.awaitingDeveloperCount} awaiting you`, rendered only while
`metrics.awaitingDeveloperCount > 0`. Server-side `reducer.py::_metrics` stopped hand-writing one
`sum(1 for lc in ...)` line per bucket and now expands `STATE_COUNT_FIELDS` (derived from the live-state
vocabulary), so `awaiting-developer` has a bucket at last; before that a lifecycle which had stopped and
handed the turn back was inside `lifecycleCount` and `totalTokens` and inside **none** of the numbers on
this bar. At zero the span emits the byte-identical `tasks N running · N blocked · N tok` it always did —
running/blocked are the workspace's standing rhythm and read fine at zero, while a permanent
`0 awaiting you` would be the same reassurance-zero lie the `⚠ N waiting` chip refuses to tell. The
client mirror of the reducer rollup is `metricsFor(lifecycles)` in `types/projection.ts`, and `Metrics`
now `extends LifecycleStateCounts` (one required `…Count` field mapped from each `ActiveState`), so a
fixture or test seed states its lifecycles instead of re-listing buckets beside them — the hand-kept
copies are where this gap kept reappearing. **5g G6** adds an `EffectsToggle` to the `TopBar`
(`effects-toggle`): a ✦ Effects / ❄ Calm button that flips `html[data-effects]` (which `useShouldAnimate`
reads live, so the engine-room backdrop + all gated motion respond at once) and persists the choice to the
`calm-cockpit` localStorage flag `main.tsx` reads on the next load. **Slice 6f** mounts the
`HighlightComposer` once in `CockpitShell` (after the mode bar): a cockpit text selection raises it to
send a context package to a chat session, and its `onSent` flips to the Chats view so the operator sees
the injection land. **L8** narrows that flow when the target is obvious: `CockpitShell` now passes the
current `selectedLifecycleId`, the lifted `viewedLeafKey`, and `leafChatActive={!fullBleed && railView ===
"chat"}` into `HighlightComposer`; only that composer decides whether to bypass the generic target picker
and draft-paste into the existing leaf chat. The shell still does not submit chat text or build the
context package. **Slice 6g** threads `open` into `DetailPanel` as `onOpenLifecycle`, so a
cross-master `→` row or a parent `↑` breadcrumb in the task reader switches the selected lifecycle
through the same `open(id)` path.
**Historical, superseded FEUI-L1 seam.** FEUI-L1 briefly registered a separate `"sessions"` route
and mounted `SessionsView` there. FEUI-L8 retired that route and the legacy `Chats` component. The
landed shell now has only the product-facing `"chats"` destination and mounts one
`<SessionsView active={view === "chats"} ... />` inside `chatsLayer`; `display` and `aria-hidden`
hide it without unmounting. The internal `[data-view="sessions"]`/`sessions-*` markers remain the
WebTUI and keyboard implementation scope, not a second product route. `SessionsView` renders
`ChatContextBar`, which owns its launch and attach/move controls.
**Task 17** keeps `selectedId` as the shared Operations selection key, but normalizes raw ids from
older surfaces through `lifecycleSelectionKey(id)` so the list/detail path can use typed keys
(`taskdoc:` / `series:` / `lifecycle:`). `selectedLifecycleId` is derived through
`lifecycleIdForSelection`, so `SessionsView` and `HighlightComposer` still attach to the lifecycle behind a
selected runtime row or task-document row. That is the attach seam: hosted chats created while a
lifecycle-backed task document is selected inherit the lifecycle tag, and highlighted context targets
can be filtered to that lifecycle's hosted chat.
**Slice L5** adds the leaf-keyed rail chat. `CockpitShell` holds a `railView: "river" | "chat"` state
and renders an inline `RailToggle` (a two-segment `role="radiogroup"` mirroring `EffectsToggle`'s cva
look) above the rail content, replacing the hard `<EventRiver/>` in `rail--right` with a switch between
`<EventRiver/>` and `<RailChat leafKey={viewedLeafKey} selectedLifecycleId={…}/>`. **L5 fix 1** changes
the leaf-key source: instead of `leafKeyForSelection(selectedId, …)` (which keyed off the top-level
selection = the master), the shell holds a `viewedLeafKey` state set from `DetailPanel`'s new `onViewLeaf`
callback — threaded down through `ViewBody` (`setViewedLeafKey`) — so it is the leaf the panel is
**actually showing** (a drilled sub-task / a directly-opened leaf doc; `undefined` for a master/series
overview), its durable qualified id (`repo/master/leaf-id`, not the enclosure). The state is **lifted to
the shell** so it survives a `DetailPanel` unmount (a full-bleed view switch) and reaches both the rail
and the full-page session cockpit. `taskDocuments` is read from `analytics?.taskDocuments` (memoized
through a stable `EMPTY_TASK_DOCS`) and, with `viewedLeafKey` as `selectedLeafKey`, passed into
`SessionsView`; its `ChatContextBar` uses that context for attach/move and leaf labels. The rail chat
and the full-page cockpit surface the **same**
session because both consume the shared catalog-backed `data/sessions` store. Their transport owners
remain separate: `RailChat` registers raw connections while `PtySurface` owns the full-page PTY.
(`leafKeyForSelection` in
`data/taskIdentity.ts` is now superseded/unused.) **L6** also reads `analytics?.engineProcesses` through a
stable `EMPTY_ENGINE_PROCESSES` fallback and passes it into `<RailChat>` beside `taskDocuments`. The shell
does not build or deliver the context package itself; it only supplies the process projection so the rail can
include worktree-group/code-worktree/memory-worktree facts at the leaf bind point.

### Conventions

Panda `css`/`cva`/`cx`. The marker classes (`cockpit--shell`/`shell__body`/`rail`/`viewport`) are kept
via `cx` for tests/structure; `shell__body` carries `data-fullbleed` for the rails-hide assertion. The
`crt-overlay` div is the global effects class (`index.css`). `useShouldAnimate` is imported from
`panels/engine-room/` (the shared honest-motion gate).

### Invariants And Boundaries

Server authority is read-only; selection state is local + lifted. The one browser mutation is the
operator's explicit reload on a proven bundle mismatch. The shell pins to `100vh` + `overflow:hidden` so the
rails/viewport scroll internally and the bars stay fixed. The master-caution lives in the always-visible
top bar; full-bleed only hides the rails, never the alarm summary (§4.1). The `EffectsToggle` is the only
writer of `html[data-effects]` from the UI (vs the `?effects=off` URL param / `calm-cockpit` flag
`main.tsx` applies at boot); default is effects-on.
**The left rail is why `grammar/Dot.tsx` cannot lean on colour alone (260731-EFA-L4).** `AttentionQueue`
and `LifecycleList` are SIBLINGS inside the one always-visible `rail--left` aside, so a developer reads
the severity grammar and the lifecycle-state grammar in a single glance. They are different facts about
different objects — the reducer builds no attention row for an `awaiting-developer` lifecycle — so an
amber dot in the queue says nothing about an amber dot in the list, and the two must stay distinguishable
by glyph rather than by hue. `Cockpit.test.tsx` pins this by rendering the whole shell (not the two panels
in isolation, because their being siblings in one view is the claim) and asserting the two dots' markup
differs.
`selectedId` is no longer assumed to be a raw lifecycle id. Any consumer that needs lifecycle context
must derive it through the task-identity helper.
`AgentNotifierHeartbeatBadge` (260707-HFX2-L2, renamed in 260713-TES-L1) renders `null` for a never-ticked heartbeat rather than a
false "stale" alarm — the same "absence is not evidence of a problem" posture `servingBuild` already
follows for a pre-L15 server.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

### 2026-07-24 Curator Delta

The shell now keeps rails and Engine Room mounted across view changes, passing visibility as a prop and
memoizing persistent layers so a tab switch does not reconcile unchanged subtrees. It starts the
shell-level screen wake lock once on mount and the helper releases it while the tab is hidden
cit:(["} from \"react\";", "import { startScreenWakeLock } from "], dashboard/src/cockpit/Cockpit.tsx:20-20; dashboard/src/cockpit/Cockpit.tsx:9-9). It marks a dirty serving checkout
with a compact `*` label and exposes a real client/serving bundle mismatch through the stamp tooltip
rather than a redundant reload control.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `bodyGrid` `bleed` variant, the `fullBleed` derivation, and the gated `railEnter` fade on `rail--left`. | "const bodyGrid = cva({"; "const fullBleed ="; "const railEnter = animate ? RAIL_ENTER : RAIL_ENTER_STILL;" | dashboard/src/cockpit/Cockpit.tsx:206-206; dashboard/src/cockpit/Cockpit.tsx:446-446; dashboard/src/cockpit/Cockpit.tsx:452-452 |
| The visible registry has exactly one Chats destination and no Sessions route; Engine Room, Topology, and Chats are full-bleed. | `CockpitView`, `VIEWS` | dashboard/src/cockpit/Cockpit.tsx:63-70; dashboard/src/cockpit/Cockpit.tsx:72-80 |
| The `chatsLayer` keep-alive class used by the Chats layer. | `chatsLayer` | dashboard/src/cockpit/Cockpit.tsx:322-328 |
| The canonical Chats session cockpit the shell mounts once; `SessionsViewImpl` composes `ChatContextBar` and `SessionRail`, and reaches `PtySurface` through `ChatsStageBody`, not directly. | `SessionsViewImpl` | dashboard/src/panels/session-cockpit/sessions-view/SessionsView.tsx:15-18 |
| `EffectsToggle` (✦ Effects / ❄ Calm) — flips `data-effects` + persists `calm-cockpit`. | `EffectsToggle` | dashboard/src/cockpit/Cockpit.tsx:1089-1116 |
| The boot-time effects flag it persists to. | "calm-cockpit" | dashboard/src/main.tsx:15-15 |
| The honest-motion gate the rail transition + the toggle drive. | `shouldAnimate` | dashboard/src/panels/engine-room/useShouldAnimate.ts:12-16 |
| The SSE stream wiring: `connectState`, then one `connectEvents` connection with two consumers (river + `createGatedSeatEventApplier`), then `startCatalogPollDriver`. | `Cockpit` | dashboard/src/cockpit/Cockpit.tsx:359-383 |
| The seat-event application + per-connection backlog gate this shell holds (`applySeatEventLine`, `createGatedSeatEventApplier`). | `applySeatEventLine`, `createGatedSeatEventApplier` | dashboard/src/data/seatEvents.ts:95-104; dashboard/src/data/seatEvents.ts:113-130 |
| The refcounted catalog poll driver started unconditionally here (`startCatalogPollDriver`). | `startCatalogPollDriver` | dashboard/src/data/catalogPoll.ts:179-192 |
| Typed task/lifecycle selection helpers used by `open` and `selectedLifecycleId` (`leafKeyForSelection` is now superseded — the leaf key comes from `DetailPanel.onViewLeaf`). | `parseTaskSelection`, `lifecycleIdForSelection`, `qualifiedLeafKey` | dashboard/src/data/taskIdentity.ts:22-45; dashboard/src/data/taskIdentity.ts:47-58; dashboard/src/data/taskIdentity.ts:64-70 |
| The detail panel that reports the displayed leaf up via `onViewLeaf` (feeding `viewedLeafKey`). | `viewedLeafKey` | dashboard/src/panels/detail-panel/state.ts:94-106 |
| The single-instance right-rail leaf chat the `RailToggle` swaps in for the Event River; `RailChatImpl` takes `engineProcesses` here for leaf-context worktree facts. | `RailChatImpl` | dashboard/src/panels/RailChat.tsx:545-643 |
| The mounted Chats session view receives the selected leaf key from the cockpit. | "selectedLeafKey={viewedLeafKey}" | dashboard/src/cockpit/Cockpit.tsx:784-784 |
| The full-page duty bar owns launch and server-first attach/move controls (`ChatContextBar`, `ChatSessionActions`). | `ChatContextBar`, `ChatSessionActions` | dashboard/src/panels/session-cockpit/ChatContextBar.tsx:74-117; dashboard/src/panels/session-cockpit/ChatContextBar.tsx:132-206 |
| The highlight composer that filters targets by `selectedLifecycleId` and, for L8, receives `viewedLeafKey` + `leafChatActive` so obvious leaf selections can draft-paste into the adjacent rail chat. | `HighlightComposerImpl` | dashboard/src/panels/HighlightComposer.tsx:710-780 |
| The frontend `Analytics` projection includes the `engineProcesses` process-map collection. | `engineProcesses` | dashboard/src/types/projection.ts:96-96 |
| The cockpit passes the process-map prop into `RailChat`. | "engineProcesses={engineProcesses}" | dashboard/src/cockpit/Cockpit.tsx:691-691 |
| The rollup the top bar reads: `Metrics extends LifecycleStateCounts` (one required `…Count` per `ActiveState` via `StateCountField`), plus `metricsFor()` — the client mirror of `reducer.py::_metrics` that test seeds now call instead of hand-listing buckets. | `Metrics`, `LifecycleStateCounts`, `StateCountField`, `metricsFor` | dashboard/src/types/projection.ts:375-375; dashboard/src/types/projection.ts:377-377; dashboard/src/types/projection.ts:396-400; dashboard/src/types/projection.ts:402-409 |
| The server rollup this bar's `awaitingDeveloperCount` comes from: `_metrics` expands `STATE_COUNT_FIELDS` rather than one `sum(...)` line per bucket. | "def _metrics(" | mcp/src/agents_remember/observer/reducer_impl/_metrics.py:27-60 |
| `AgentNotifierHeartbeatBadge` reads `useDashboard((s) => s.agentNotifierHeartbeat)`, the store field this top-bar heartbeat/backlog indicator renders. | `AgentNotifierHeartbeatBadge` | dashboard/src/cockpit/Cockpit.tsx:959-984 |
| The `AgentNotifierHeartbeat` type this badge's props shape mirrors. | `AgentNotifierHeartbeat` | dashboard/src/types/projection.ts:54-65 |

## Historical FEUI-L8 Reviewed Candidate Delta

The shell now exposes `operations | engine | files | chats`; the former Sessions destination and legacy Chats layer are gone. It owns both catalog poll and eager/cross-tab reconciliation for its lifetime, keeps one persistent `SessionsView` as Chats, and moves highlight route/focus only after accepted delivery to an exact live id.

This section records the FEUI-L8 review point. That candidate subsequently landed in code authority
`31f58834f86c0d98e26b0896e099a2403a8729ee`, which this card now verifies.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current dashboard card for `Cockpit.tsx` with its task-document, seat-state, and lifecycle interaction boundaries.
- 2026-08-08T21:20+02:00 — 260713-TES-L1 curator: recorded the `AgentNotifierHeartbeatBadge`
  rename, the `agent-notifier ok/stale` wording and `data-testid="agent-notifier-heartbeat"`, and
  the store's legacy-wire fallback. Verification metadata pinned until closeout stamps the
  260713-TES-L1 commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the re-wired imports to the kebab-case split folders and the lint remediation. Verification metadata stays pinned until closeout stamps the code commit.
- 2026-08-04T08:45:26+02:00 — 260731-EFA-L6 S18-B07 curator correction: rebound the keep-alive, Analytics, and RailChat claims to their frozen implementation/type bodies; same-reviewer delta pending.

- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: anchored 15 citation rows and rewrote 2 prose citations; scoped citation fixing regenerated the source ranges.

- 2026-08-01T10:30+02:00 — 260731-EFA-L4 curator (citation pass): `types/projection.ts` adopted the
  server's state partition (`LIVE_STATES` + `TERMINAL_STATES` composed into `LIFECYCLE_STATES`), moving
  every anchor below it. Re-anchored the three rows citing that file, each on its proving symbol:
  `Analytics` L626-L641 → L663-L678 (`engineProcesses` at L677); the metrics rollup L167-L220 → L206-L257
  (`StateCountField` L206, `LifecycleStateCounts` L214, `Metrics extends LifecycleStateCounts` L240,
  `metricsFor` L250); and `SupervisorHeartbeat` L664-L672 → L701-L709. The body's rollup claims still
  hold: `ActiveState` is now `LIVE_STATES` itself rather than a subtraction, but `Metrics` still carries
  one required `…Count` per `ActiveState`.

- 2026-08-01T09:05+02:00 — 260731-EFA-L4 curator: corrected the top-bar counts claim, which still said
  the span renders only `tasks N running · N blocked · N tok`. It now carries
  `data-testid="task-metrics"` and appends `· {metrics.awaitingDeveloperCount} awaiting you` while that
  count is `> 0` only (cit:([`TopBar`], dashboard/src/cockpit/Cockpit.tsx:990-1038)); recorded that `Metrics extends LifecycleStateCounts` and
  that `metricsFor()` is the client mirror seeds now call, and that server-side `_metrics` expands
  `STATE_COUNT_FIELDS` instead of three hand-written `sum(...)` lines. Added the left-rail invariant the
  new in-file comment states (`AttentionQueue` + `LifecycleList` are siblings in `rail--left`, so the
  amber in each grammar must differ by glyph; the reducer builds no attention row for
  `awaiting-developer`). Citation repairs, each re-anchored on its proving symbol: `bodyGrid`/`fullBleed`/
  `railEnter` L194-L252 → L204-L220; L437-L442; L493; L548-L554; view registry L59-L76; L379-L386 →
  L63-L80 (`CockpitView`/`VIEWS`, incl. the `chats` entry the old range cut off); L437-L442; `chatsLayer`
  L317-L323; L528-L541 → L318-L328; L612-L621; the Chats-layer prop pass L544-L558 → L617-L628 (the old
  range landed on `motion.aside`); SSE wiring L328-L354 → L360-L389 (`connectState`/`connectEvents`/
  `createGatedSeatEventApplier`/`startCatalogPollDriver`); `startCatalogPollDriver` L60-L77 → L101-L122;
  `applySeatEventLine` L106-L130 → L95-L130; `RailChat` `engineProcesses` L479-L485 → L245-L257; L312;
  `Analytics.engineProcesses` L395-L408 → L626-L641; and the two previously uncited rows
  (`store.supervisorHeartbeat`, `SupervisorHeartbeat`) given real ranges. Also narrowed the
  `SessionsView.tsx` row: it composes `ChatContextBar` + `SessionRail` (cit:([`SessionsViewImpl`], dashboard/src/panels/session-cockpit/sessions-view/SessionsView.tsx:15-18)) and reaches
  `PtySurface` through `ChatsStageBody`, not directly — the file no longer names `PtySurface` at all.

- 2026-07-24T13:17:50Z — Documented persistent-layer memoization, wake-lock ownership, and serving
  identity honesty. Verification hash/date remain pinned to the pre-commit source stamp.

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: recorded the top-bar polish — `SupervisorHeartbeatBadge`
  age humanized (`humanizeDuration`) and stale degraded to quiet `caution({sev:"warn"})` amber (no longer
  pulsing red, R5/A4/B9); the `⚠ N waiting` chip renders only when `> 0` (RV-4/R4); `ServingBuildStamp`
  `up` is a humanized uptime with the absolute stamp in the tooltip (V15); brand/fact-chips `nowrap` +
  `statusRow` `flex-wrap:wrap` (V6); lifecycle counts scope-labeled `tasks …` with an authority tooltip
  (R7, no backend change). Shell layout/keep-alive/selection unchanged. Verification pinned to the leaf
  base (`352d5cd`) until closeout stamps the candidate commit.
- 2026-07-18T16:02+02:00 — FEUI MX-FIX-3: made FEUI-L1's separate Sessions route explicitly
  historical, named the landed single `SessionsView` mount behind Chats, and assigned full-page
  launch/attach ownership to `ChatContextBar`; the shell alone owns catalog polling and
  reconciliation. Also separated the shared session store from the distinct RailChat/PtySurface
  transport owners and labeled the former uncommitted-candidate note as historical. Verified against
  code commit `31f58834f86c0d98e26b0896e099a2403a8729ee`.

- 2026-07-18T12:43+02:00 — FEUI-L9R: recorded the running-bundle comparison and explicit reload
  boundary; verification metadata remains pinned pending candidate closeout.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T02:30+02:00 — 260715-FEUI-L2 (S1/S2, incl. review finding 2): `Cockpit` now owns the
  shared session feed — the `/api/events` EventSource carries the Event River AND the seat-event
  reconciler (one connection, two consumers), with seat application behind the per-connection
  backlog gate (`ready` opens, `error`/interrupt re-closes; replayed history never touches live
  rows), and starts the refcounted 2500 ms catalog poll driver unconditionally so the feed lives
  with any view — or none — in front. Verification metadata pinned to the leaf base until
  closeout stamps the L2 code commit.
- 2026-07-17T00:25+02:00 — 260715-FEUI-L1 (view shell, R1): registered the full-bleed **Sessions**
  view — `View` gained `"sessions"`, `VIEWS` a last `Sessions` tab, `fullBleed` includes it, and
  the view is kept mounted as the fourth persistent hidden layer (`sessionsLayer = chatsLayer`,
  display/aria-hidden toggle, never unmounted) so the future xterm buffers/WebSockets survive view
  switches; `active={view === "sessions"}` gates the view's window-level keyboard layer. Only
  registration seams touched. Verification metadata pinned to the task base until closeout stamps
  the L1 code commit.
- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 (dead-seat storm observability, R6):
  `SupervisorHeartbeatBadge` now includes the latest redeliverable/pending inbox backlog counts and
  last sweep duration next to the heartbeat age, with the tooltip carrying the same forward signal.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L8 commit.
- 2026-07-08T18:45+02:00 — 260707-HFX2-L2 (supervisor sweep, R5): added `SupervisorHeartbeatBadge`
  to the `TopBar`, rendered between the `@ hh:mm:ss` stamp and `ServingBuildStamp` — reads
  `s.supervisorHeartbeat`, renders nothing for a never-ticked heartbeat (`lastTickAt === null`), else
  `"supervisor ok/stale <age>m"` styled `caution({sev:"alarm"})` past the cutoff or `dim` otherwise,
  with a tooltip naming the exact tick time and cutoff. Verification metadata pinned until closeout
  stamps the 260707-HFX2-L2 commit.
- 2026-07-07T14:00+02:00 — agent-orchestration L17: the shell gained a second full-bleed **takeover**, the
  **Notes Reader** — `notes`/`notesOpen` state + `openNotes`/`openChangeSet` handlers, a shared `takeover`
  flag that hides the railed body for either screen, and `onOpenNotes` wired into `DetailPanel`. Unlike the
  Change-Set takeover the reader is retained mounted-hidden after Back (selection survives back/forward, the
  File Viewer pattern). Verification metadata pinned until closeout stamps the L17 commit.
- 2026-07-07T10:50+02:00 — L15: servingBuild stamp in the top bar (build_info via /api/state). Verification metadata pinned until closeout stamps the L15 commit.

- 2026-07-07T05:24+02:00 — 260703-L15 S3 (stale-server visibility): the top bar gained the muted
  `ServingBuildStamp` (`data-testid="serving-build"`, rendered between the `@ hh:mm:ss` stamp and
  the conn badge) — commit short-hash (or `v<version>` off-checkout) + "up <boot time>", read from
  the store's snapshot-fed `servingBuild`; renders nothing when the wire carries no stamp (a
  pre-L15 server), never fakes. Note: with the L15 change gate, the top bar's `@ hh:mm:ss`
  (`generatedAt`) is the stamp of the last APPLIED content, frozen while idle by design.
  Verification metadata pinned until closeout stamps the L15 commit.
- 2026-07-02T16:18+02:00 — L8: `CockpitShell` now threads `viewedLeafKey` and active right-rail chat
  state into `HighlightComposer` beside `selectedLifecycleId`, so highlighted text from the displayed leaf
  can be routed to the adjacent leaf chat draft while global/off-leaf selections keep the generic
  Add-to-chat fallback. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-01T01:19+02:00 — L6: threaded `analytics.engineProcesses` through `CockpitShell` to the
  right-rail `RailChat` using a stable empty fallback. Cockpit still owns only selection/view state; packet
  construction and delivery stay inside `RailChat` at start-on-leaf or successful free-chat attach time.
  Verification metadata pinned until closeout stamps the L6 commit.
- 2026-06-30T00:00:00+02:00 — L5 follow-up: the rail/Chats leaf key now comes from the **displayed** leaf, not the
  top-level selection. Replaced `leafKeyForSelection(selectedId, …)` with a `viewedLeafKey` state set from
  `DetailPanel`'s new `onViewLeaf` callback (threaded through `ViewBody` as `setViewedLeafKey` and lifted to
  the shell so it survives a `DetailPanel` unmount); it feeds both `<RailChat leafKey>` and the Chats page's
  `selectedLeafKey`. `leafKeyForSelection` is now superseded/unused. Verification metadata pinned until
  closeout stamps the L5 commit.
- 2026-06-30T00:00:00+02:00 — L5 (Sidebar chat): `CockpitShell` gained a `railView: "river" | "chat"` state + an inline
  `RailToggle` (a `role="radiogroup"` two-segment control mirroring `EffectsToggle`) that replaces the
  hard `<EventRiver/>` in `rail--right` with a switch between the Event River and a single-instance
  `<RailChat>`. Derives `selectedLeafKey` from the **open task doc** via `leafKeyForSelection` (the
  durable `repo/master/leaf-id`, not the enclosure) and reads `taskDocuments` from analytics, passing both
  (plus `selectedLifecycleId`) into `<Chats>` and `selectedLeafKey` into `<RailChat>`. New collaborator:
  `panels/RailChat.tsx`. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-29T23:00+02:00 — L4a: the change-set takeover now **overlays** the railed body instead of
  replacing it — the body div is kept mounted but `display:none`/`aria-hidden` while `changeSet` is set
  (the File Viewer / Chats hidden-not-unmounted pattern), so `DetailPanel`'s drill state survives and the
  viewer's back link returns to the leaf it was opened from rather than resetting to the master overview.
  Verification metadata pinned until closeout stamps the L4a commit.
- 2026-06-29T16:40+02:00 — Operations Integration L4 (Change-Set Viewer): `CockpitShell` gained a `changeSet` TAKEOVER state — when set it renders `<ChangeSetViewer>` full-bleed in place of the railed Operations body, and the screen's back link / a mode-bar switch (`changeView`) / `open()` all clear it; `onOpenChangeSet` is threaded through `ViewBody` into `DetailPanel`. New collaborator: `panels/changeset/ChangeSetViewer`. Verification metadata pinned to the task base until closeout stamps the L4 code commit.
- 2026-06-29T09:06+02:00 — Operations Integration L2 (File Viewer): registered a full-bleed **File Viewer**
  view — `View` gained `"files"`, `VIEWS` a `{ id: "files", label: "File Viewer" }` tab between Operations
  and Engine Room, and `fullBleed` now includes `files`. The File Viewer is **kept mounted** as a persistent
  CSS-hidden `filesLayer` in `CockpitShell` (the Chats pattern), not routed through `ViewBody`, so a tab
  switch preserves its repo/scope/open-file/tree state instead of resetting it. New collaborator:
  `panels/file-viewer/FileViewer`. Verification metadata pinned to the task base until closeout stamps the
  L2 code commit.
- 2026-06-28T07:32+02:00 — Task 29 S7 follow-up: removed the Lifecycle Flow tab from the visible
  cockpit view registry and routed `/api/events` readiness through `markEventsHydrated`, so the Event
  River waits for retained backlog hydration before showing empty-state copy. Verification metadata
  pinned until closeout stamps the task-29 code commit.
- 2026-06-27T18:43+02:00 — Task 26: registered the **Lifecycle Flow** view — `View` gained `"flow"`,
  `VIEWS` a `{ id: "flow", label: "Lifecycle Flow" }` tab (second, after Operations), `ViewBody` a
  `case "flow" → <FlowTab />`, and `fullBleed` now includes `flow` (rails hidden, like the machine-map
  views). Adds the `FlowTab` panel (`panels/FlowTab.tsx`) as a new collaborator. Verification metadata
  pinned until closeout stamps the task-26 code commit.
- 2026-06-24T16:33+02:00 — Task 17 typed Operations selection: `open(id)` now preserves typed
  task/series/lifecycle selection keys and wraps legacy raw lifecycle ids; `selectedLifecycleId` is
  derived through `lifecycleIdForSelection` so chats still bind to lifecycle-backed task docs.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T13:45+02:00 — Task 11: derives `selectedLifecycleId` from `selectedId` + the lifecycle map
  and passes it to `<Chats>` and `HighlightComposer`, enabling hosted chat lifecycle tagging and
  lifecycle-filtered context delivery. Verification metadata pinned until closeout stamps the task-11
  code commit.
- 2026-06-21T02:44+02:00 — Slice 6g: `ViewBody` now passes `onOpenLifecycle={open}` into `DetailPanel`, wiring the task reader's cross-master `→` rows and parent `↑` breadcrumb to switch the selected lifecycle. Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-19T15:59 — Task 6 slice 6f-1: `CockpitShell` now mounts the `HighlightComposer` (cockpit-wide selection → context-package composer); `onSent` flips to the Chats view. Verification metadata pinned until closeout stamps the 6f-1 code commit.
- 2026-06-19T14:05 — Task 6 slice 6e-4: stopped routing `chats` through `ViewBody` — `<Chats />` is now rendered once as a persistent layer in `CockpitShell`, shown when `view === "chats"` and otherwise `display:none` (`aria-hidden`). Keeping it mounted means the live xterm instance + its WebSocket survive a view switch instead of being re-created empty. Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-18T16:50 — Task 6 slice 6e-1: registered the full-bleed **Chats** view — `View` gained `"chats"`, `VIEWS` a `Chats` tab, `ViewBody` a `case "chats" → <Chats />`, and `fullBleed` now includes `chats` (rails hidden, like the machine-map views). Verification metadata pinned until closeout stamps the 6e-1 code commit.
- 2026-06-17T22:45 — slice 5g G6: added the `EffectsToggle` (`effects-toggle`) to the `TopBar` — a
  ✦ Effects / ❄ Calm button that flips `html[data-effects]` live (so the engine-room backdrop + all gated
  motion respond at once) and persists `calm-cockpit` for the next boot. Default effects-on. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-16T02:30 — slice 5f S1: machine-map views (Engine Room / Topology) go full-bleed — the
  `body` became a `bodyGrid` `bleed` cva, the two rails render only when `!fullBleed` (gated
  `motion.aside` fade-in via `useShouldAnimate`), and `shell__body` carries `data-fullbleed`. The
  top-bar master-caution stays visible. Verification metadata pinned until closeout stamps the S1 commit.
- 2026-06-15T17:00 — Created for slice 5d: shell layout + status/caution migrated to co-located Panda
  css/cva; the mode bar became the React Aria `ModeBar`. Verification metadata pinned until closeout
  stamps the 5d code commit.
