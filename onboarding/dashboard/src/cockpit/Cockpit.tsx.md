# dashboard/src/cockpit/Cockpit.tsx

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

## 260928-MIK-L29 The Knowledge View

The shell gained one destination: `knowledge`, labelled "Knowledge" in the mode bar, which renders the
path-based knowledge reader (`panels/knowledge-reader/KnowledgeReader`, MIK-R29). Like Memory, Topology and
Hangar it is a **transient** view: `ViewBody` mounts it while it is selected and unmounts it on a switch, and
it is not full-bleed, so the rails stay. The reader keeps its own address in the URL hash, so nothing of its
state lives in the shell.

**A shared reader URL opens on the Knowledge view.** `Cockpit` passes `initialView="knowledge"` to
`CockpitShell` when `parseReaderHash(window.location.hash)` names a reader address (`#knowledge?…`), and
leaves the shell's own default (`operations`) otherwise. The hash persists after the user switches to another
tab, so a reload then returns to Knowledge (review R1 note N4, harmless). Nothing else in the shell changed:
the takeovers, rails, polls and streams are as before, and the existing panels are unchanged (the packet's
preservation boundary).


## 260921-ICR-L33 The Change-Set Takeover Re-Targets Itself

`ChangeSetTakeover` gained one prop and the shell supplies it: `onOpenChangeSet`, wired to the same
`actions.openChangeSet` the shell already owns. It is passed through to `ChangeSetViewer` as
`onOpenLeaf`, which composes a leaf target (`{ repo, master, leaf, mode }`) from a row of the master
net's `by leaf (N)` rail. **The point is reachability without a second screen:** a landed leaf is
offered from the master's own net listing, its committed change-set opens in the takeover the reader is
already in, and the back link still clears the takeover as before. Nothing else in the dispatch chain
changed — `target.review` still routes to `ReviewSurface` and the change-set viewer is still never
mounted for a review, so a leaf opened this way is an ordinary change-set target with `master` as its
qualifier.

## 260831-CCR-L23 Requirement-Artifact Takeover Kind

The L17 Notes takeover was widened into a generic task-artifact reader takeover:
the notes-only `NotesReaderTarget` shape became the discriminated
`TaskArtifactReaderTarget` (`dashboard/src/data/taskArtifacts.ts`) with a
`kind` member, and that shared target type is now imported from the data module
rather than from the notes reader. `NotesTakeover` spreads the whole target onto
`NotesReaderViewer` (`{...target}`) and keys the view marker on the kind:
`data-view` is `notes-reader` for a notes target and
`requirements-reader` for a requirements target. The shell, the shared takeover
flag, hidden-not-unmounted retention, and the `onOpenNotes` wiring are
unchanged.

## 260915-KS-L22 Intent-Review Takeover Kind

The change-set takeover now carries a second kind. `ChangeSetTarget` gained an optional
`review: { selectorKind, selectorId }` member, and `ChangeSetTakeover` reads it: `data-view` is
`intent-review` when the target carries a review and `changeset` when it does not, and the review
variant mounts `ReviewSurface` (`dashboard/src/panels/review/ReviewSurface`) in place of
`ChangeSetViewer`, passing `repo`, `master`, `leaf`, the two selector fields and `onBack`. The review
surface therefore sits beside `NotesTakeover` and the requirements variant of the task-artifact
reader as one more takeover the shell dispatches on the target's own shape, and nothing in the
shell's routing, rails or change-set plumbing changed with it: the target chooses the pane.

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


**One comment, and it records a shape the dispatch already supported.** The `ChangeSetTakeover` component's review branch gained a comment stating that a review target may carry a subject's selector **or none at all** — the task-context entry opens the review on the task, and `ReviewSurface` asks the server for exactly what it was handed. The dispatch itself was not changed: it already forwarded an optional selector, which is why the task-context target reaches the surface without a code change here. Nothing else in the cockpit moved, and the two lines are the whole of this file's diff.

**The shell provides the entry's re-validation context (`260921-ICR-L47`, ruling 2026-09-28T16:27:28+02:00
on L47-R1-F2).** `CockpitShell` wraps its tree in
`<IntentEntryRevalidation shown={state.view === "operations" && !state.takeover}>`. The Operations
`DetailPanel` is never unmounted (only hidden during view switches and takeovers), so remounting could not
re-read the entry; instead the generation increments when `shown` turns true — a view switch back to
Operations or any takeover closing (the reviewer, a change set, notes) — and the entry's summary re-reads
once. This is 3 lines of wiring (1156 → 1159, already in the 900–1200 soft band; the diff is mostly
re-indentation); review R2 judged it wiring, not feature logic (O-R2-2).

- The provider around the shell, shown only for Operations with no takeover. [1]

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No relevant domain documentation was found for this file.

### Repo-Internal References

- The body grid bleed variant switches between three railed columns and a single full-width column. [2]
- Files, Engine Room, Topology, and Chats request the full-bleed layout. [3]
- Rail fade properties are selected by the animation permission. [4]
- The visible registry has exactly one Chats destination, no Sessions route and, since 260928-MIK-L29, a Knowledge destination; Engine Room, Topology, and Chats are full-bleed, and Knowledge is not. [5]
- The `chatsLayer` keep-alive class used by the Chats layer. [6]
- The canonical Chats session cockpit the shell mounts once; `SessionsViewImpl` composes `ChatContextBar` and `SessionRail`, and reaches `PtySurface` through `ChatsStageBody`, not directly. [7]
- `EffectsToggle` (✦ Effects / ❄ Calm) — flips `data-effects` + persists `calm-cockpit`. [8]
- The boot-time effects flag it persists to. [9]
- The honest-motion gate the rail transition + the toggle drive. [10]
- The SSE stream wiring: `connectState`, then one `connectEvents` connection with two consumers (river + `createGatedSeatEventApplier`), then `startCatalogPollDriver`; the shell opens on the Knowledge view when the URL is a reader address (260928-MIK-L29). [11]
- A `#knowledge?…` reader URL selects the Knowledge view as the shell's initial view (MIK-R29 rule 5). [12]
- The transient Knowledge view renders the reader. [13]
- The reader's hash parser. [14]
- The seat-event application + per-connection backlog gate this shell holds (`applySeatEventLine`, `createGatedSeatEventApplier`). [15]
- The refcounted catalog poll driver started unconditionally here (`startCatalogPollDriver`). [16]
- Typed task/lifecycle selection helpers used by `open` and `selectedLifecycleId` (`leafKeyForSelection` is now superseded — the leaf key comes from `DetailPanel.onViewLeaf`). [17]
- The detail panel that reports the displayed leaf up via `onViewLeaf` (feeding `viewedLeafKey`). [18]
- The single-instance right-rail leaf chat the `RailToggle` swaps in for the Event River; `RailChatImpl` takes `engineProcesses` here for leaf-context worktree facts. [19]
- The mounted Chats session view receives the selected leaf key from the cockpit. [20]
- The full-page duty bar owns launch and server-first attach/move controls (`ChatContextBar`, `ChatSessionActions`). [21]
- The highlight composer that filters targets by `selectedLifecycleId` and, for L8, receives `viewedLeafKey` + `leafChatActive` so obvious leaf selections can draft-paste into the adjacent rail chat. [22]
- The frontend `Analytics` projection includes the `engineProcesses` process-map collection. [23]
- The cockpit passes the process-map prop into `RailChat`. [24]
- Metrics extends the mapped active-state counts and adds total lifecycle/token and histogram fields. [25]
- Every ActiveState maps to a required count field. [26]
- The count-field name is derived from the camel-cased state vocabulary. [27]
- metricsFor builds the client rollup from lifecycles and spreads the derived state counts. [28]
- The server rollup this bar's `awaitingDeveloperCount` comes from: `_metrics` expands `STATE_COUNT_FIELDS` rather than one `sum(...)` line per bucket. [29]
- `AgentNotifierHeartbeatBadge` reads `useDashboard((s) => s.agentNotifierHeartbeat)`, the store field this top-bar heartbeat/backlog indicator renders. [30]
- The `AgentNotifierHeartbeat` type this badge's props shape mirrors. [31]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## Historical FEUI-L8 Reviewed Candidate Delta

The shell now exposes `operations | engine | files | chats`; the former Sessions destination and legacy Chats layer are gone. It owns both catalog poll and eager/cross-tab reconciliation for its lifetime, keeps one persistent `SessionsView` as Chats, and moves highlight route/focus only after accepted delivery to an exact live id.

This section records the FEUI-L8 review point. That candidate subsequently landed in code authority
`31f58834f86c0d98e26b0896e099a2403a8729ee`, which this card now verifies.

## 260921-ICR-L12 The Takeover Hands The Record To The Review Surface

`260921-ICR-L12` (`ICR-R12@v1`) adds one prop at the takeover: when the change-set target's review
carries `historical`, `ChangeSetTakeover` mounts `ReviewSurface` with `history="recorded"`, and
otherwise with `undefined` — the live candidate, which is what every ordinary entry asks for. The
target's own comment records why the record travels this way: a closed leaf's entry carries it, so the
surface asks for that leaf's recorded comparison rather than for a live candidate there is none of.

Nothing else in the takeover changed: the review target's subject still travels as it did, the
`onBack` contract is the same, and the cockpit adds no resolution of its own — the browser names a
record and the server owns which comparison that record is.
