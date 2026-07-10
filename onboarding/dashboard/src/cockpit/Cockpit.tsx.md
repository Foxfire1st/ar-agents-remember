# dashboard/src/cockpit/Cockpit.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/cockpit/Cockpit.tsx`              |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-08T23:59+02:00                           |
| lastVerifiedCommitHash | `e400ed0ce98752d1b65d00de97c9b84c7ea20814`       |
| lastVerifiedCommitDate | 2026-07-10T20:04:45+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The model-C cockpit shell (note 06): persistent chrome that never hides the alarms — top bar, left
rail (attention queue + lifecycle list), switchable centre viewport, right-rail event river, bottom
mode bar. Owns the ephemeral selection + view UI state and the live SSE wiring. As of slice 5f S1 the
two "machine map" views (Engine Room / Topology) drop the rails and span the full body width (§4.1);
slice 6e adds a third full-bleed view, **Chats** (the xterm.js Mode B2 terminal). Task 29 hides the
Task 26 Lifecycle Flow diagnostic from normal dashboard navigation; `FlowTab.tsx` remains in the source
tree but `Cockpit.tsx` no longer imports or routes it. **Slice L5** makes the right rail itself
switchable: a `railView` River⇄Chat toggle swaps the standing Event River for a single-instance,
leaf-keyed `RailChat`, and the shell tracks the leaf the **detail panel is displaying** (reported up from
`DetailPanel`) so both the rail chat and the Chats page bind to the same per-leaf session. L6 keeps that
timing and adds one extra projection thread: the shell passes `analytics.engineProcesses` into `RailChat`
so a newly created or newly attached leaf chat can receive worktree facts in its context package. L8 also
threads the displayed leaf key and active rail-chat state into `HighlightComposer`, letting obvious
task-reader selections paste straight into the adjacent leaf chat draft instead of opening the generic
Add-to-chat composer. **L17** adds a second full-bleed **takeover** beside the Change-Set Viewer: the
**Notes Reader** (`panels/notes-reader/NotesReaderViewer.tsx`), opened from a `TaskNotes` note/reference via
the threaded `onOpenNotes`. The shell holds its selection (`notes`) + a `notesOpen` visibility flag and a
shared `takeover` flag hides the railed body for either screen; unlike the Change-Set takeover it is
RETAINED mounted-hidden after Back (the File Viewer pattern) so its listing + open note survive
back/forward, and a fresh entry re-shows it on the clicked note.

## Code Commentary

### Logic

Since L15 the cockpit top bar renders the muted servingBuild stamp (commit short-hash + boot time from the state payload) — the ghost-process lesson made visible: a stale dashboard server is identifiable at a glance. **260707-HFX2-L2 (R5)** adds a second top-bar indicator right beside it: `SupervisorHeartbeatBadge` reads `s.supervisorHeartbeat` from the store and renders nothing when `lastTickAt` is `null` (the supervisor has never ticked in this workspace — `dashboard.autoStart` is opt-in, so "no row yet" is not itself an alarm); once a tick exists, it shows `"supervisor ok/stale <age>m"`, styled with the existing `caution({sev:"alarm"})` pulsing-red class past the staleness cutoff (`heartbeat.stale`) or the muted `dim` class otherwise, with a `title` tooltip naming the exact `lastTickAt`/`staleCutoffSeconds`. **260707-HFX2-L8 (R6)** extends the same badge with `inbox redeliverable/pending` and latest sweep duration, so a growing operator-inbox storm is visible beside the heartbeat before staleness fires. This is issue #15's "the watcher must be code AND watched" made visible in the SAME top bar that already carries `servingBuild` — "the last turtle is the developer's glance."

`Cockpit` wires the two SSE streams (`connectState`, `connectEvents`→`pushEvent`) then renders
`CockpitShell` (split out so the dev gallery renders the same surface against fixtures). `CockpitShell`
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
`TopBar` shows the always-visible master-caution (`⚠ N waiting`, severity-keyed from `selectQueue`), so
an alarm is never hidden even in a full-bleed view. **5g G6** adds an `EffectsToggle` to the `TopBar`
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
**Task 17** keeps `selectedId` as the shared Operations selection key, but normalizes raw ids from
older surfaces through `lifecycleSelectionKey(id)` so the list/detail path can use typed keys
(`taskdoc:` / `series:` / `lifecycle:`). `selectedLifecycleId` is derived through
`lifecycleIdForSelection`, so Chats and `HighlightComposer` still attach to the lifecycle behind a
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
and the Chats page. `taskDocuments` is read from `analytics?.taskDocuments` (memoized through a stable
`EMPTY_TASK_DOCS`) and, with `viewedLeafKey` as `selectedLeafKey`, passed into `<Chats>` so the page can
offer "Attach to leaf" + resolve leaf names. The rail chat and the Chats-page row surface the **same**
session because both reuse the shared `data/sessions` connection registry. (`leafKeyForSelection` in
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

Read-only; selection state is local + lifted. The shell pins to `100vh` + `overflow:hidden` so the
rails/viewport scroll internally and the bars stay fixed. The master-caution lives in the always-visible
top bar; full-bleed only hides the rails, never the alarm summary (§4.1). The `EffectsToggle` is the only
writer of `html[data-effects]` from the UI (vs the `?effects=off` URL param / `calm-cockpit` flag
`main.tsx` applies at boot); default is effects-on.
`selectedId` is no longer assumed to be a raw lifecycle id. Any consumer that needs lifecycle context
must derive it through the task-identity helper.
`SupervisorHeartbeatBadge` (260707-HFX2-L2) renders `null` for a never-ticked heartbeat rather than a
false "stale" alarm — the same "absence is not evidence of a problem" posture `servingBuild` already
follows for a pre-L15 server.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `fullBleed` rails-hide + `bodyGrid` `bleed` variant + gated rail fade. | L194-L252 | [Cockpit.tsx](Cockpit.tsx) |
| The visible view registry no longer includes `flow`; full-bleed views are Engine Room, Topology, and Chats. | L31-L40; L194-L197 | [Cockpit.tsx](Cockpit.tsx) |
| `EffectsToggle` (✦ Effects / ❄ Calm) — flips `data-effects` + persists `calm-cockpit`. | — | [Cockpit.tsx](Cockpit.tsx) |
| The boot-time effects flag it persists to. | — | [main.tsx](../main.tsx) |
| The honest-motion gate the rail transition + the toggle drive. | — | [panels/engine-room/useShouldAnimate.ts](../panels/engine-room/useShouldAnimate.ts) |
| The SSE stream wiring includes an Event River ready callback. | L172-L181 | [Cockpit.tsx](Cockpit.tsx) |
| Typed task/lifecycle selection helpers used by `open` and `selectedLifecycleId` (`leafKeyForSelection` is now superseded — the leaf key comes from `DetailPanel.onViewLeaf`). | — | [data/taskIdentity.ts](../data/taskIdentity.ts) |
| The detail panel that reports the displayed leaf up via `onViewLeaf` (feeding `viewedLeafKey`). | — | [panels/DetailPanel.tsx](../panels/DetailPanel.tsx) |
| The single-instance right-rail leaf chat the `RailToggle` swaps in for the Event River; L6 receives `engineProcesses` here for leaf-context worktree facts. | L479-L485 | [panels/RailChat.tsx](../panels/RailChat.tsx) |
| The hosted chat view that receives `selectedLifecycleId` + `selectedLeafKey` + `taskDocuments`. | — | [panels/Chats.tsx](../panels/Chats.tsx) |
| The highlight composer that filters targets by `selectedLifecycleId` and, for L8, receives `viewedLeafKey` + `leafChatActive` so obvious leaf selections can draft-paste into the adjacent rail chat. | — | [panels/HighlightComposer.tsx](../panels/HighlightComposer.tsx) |
| The frontend projection type exposes `Analytics.engineProcesses`, the process-map input Cockpit now threads into `RailChat`. | L395-L408 | [types/projection.ts](../types/projection.ts) |
| `SupervisorHeartbeatBadge` reads `useDashboard((s) => s.supervisorHeartbeat)`, the store field this top-bar heartbeat/backlog indicator renders. | — | [../data/store.ts](../data/store.ts.md) |
| The `SupervisorHeartbeat` type this badge's props shape mirrors. | — | [../types/projection.ts](../types/projection.ts.md) |

## Update History

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
