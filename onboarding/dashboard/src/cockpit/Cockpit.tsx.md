# dashboard/src/cockpit/Cockpit.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/cockpit/Cockpit.tsx`              |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-28T07:32+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
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
tree but `Cockpit.tsx` no longer imports or routes it.

## Code Commentary

### Logic

`Cockpit` wires the two SSE streams (`connectState`, `connectEvents`→`pushEvent`) then renders
`CockpitShell` (split out so the dev gallery renders the same surface against fixtures). `CockpitShell`
holds `view` + `selectedId` state and derives `fullBleed = view === "engine" || view === "topology" ||
view === "chats"` (the `chats` view is full-bleed; slice 6e-4 keeps `<Chats>`
mounted as a persistent CSS-hidden layer in `CockpitShell` rather than routing it through `ViewBody`, so
a view switch never unmounts the live terminal + WebSocket).
Task 29 wires the raw Event River readiness signal through this shell: `connectEvents` receives
`markEventsHydrated` as its `ready` callback, so the right rail can show "Syncing event history." until
the backend has emitted the retained backlog and the explicit ready marker.
The body is the `bodyGrid` cva: the railed 3-column shell when `!fullBleed`, a single full-width column
when `fullBleed`. The two `<aside>` rails (`rail--left` = attention queue + lifecycle list;
`rail--right` = event river) render only when `!fullBleed`, so a machine-map view unmounts them for a
clean expand; they fade back in via a `motion.aside` gated by `useShouldAnimate()` (instant under
`data-effects=off` / reduced-motion, keeping snapshots stable). `ViewBody` switches the centre by
`view`; the mode bar is the `<ModeBar>` primitive. `open(id)` selects a node AND jumps to Operations.
`TopBar` shows the always-visible master-caution (`⚠ N waiting`, severity-keyed from `selectQueue`), so
an alarm is never hidden even in a full-bleed view. **5g G6** adds an `EffectsToggle` to the `TopBar`
(`effects-toggle`): a ✦ Effects / ❄ Calm button that flips `html[data-effects]` (which `useShouldAnimate`
reads live, so the engine-room backdrop + all gated motion respond at once) and persists the choice to the
`calm-cockpit` localStorage flag `main.tsx` reads on the next load. **Slice 6f** mounts the
`HighlightComposer` once in `CockpitShell` (after the mode bar): a cockpit text selection raises it to
send a context package to a chat session, and its `onSent` flips to the Chats view so the operator sees
the injection land. **Slice 6g** threads `open` into `DetailPanel` as `onOpenLifecycle`, so a
cross-master `→` row or a parent `↑` breadcrumb in the task reader switches the selected lifecycle
through the same `open(id)` path.
**Task 17** keeps `selectedId` as the shared Operations selection key, but normalizes raw ids from
older surfaces through `lifecycleSelectionKey(id)` so the list/detail path can use typed keys
(`taskdoc:` / `series:` / `lifecycle:`). `selectedLifecycleId` is derived through
`lifecycleIdForSelection`, so Chats and `HighlightComposer` still attach to the lifecycle behind a
selected runtime row or task-document row. That is the attach seam: hosted chats created while a
lifecycle-backed task document is selected inherit the lifecycle tag, and highlighted context targets
can be filtered to that lifecycle's hosted chat.

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

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `fullBleed` rails-hide + `bodyGrid` `bleed` variant + gated rail fade. | L194-L252 | [Cockpit.tsx](Cockpit.tsx) |
| The visible view registry no longer includes `flow`; full-bleed views are Engine Room, Topology, and Chats. | L31-L40; L194-L197 | [Cockpit.tsx](Cockpit.tsx) |
| `EffectsToggle` (✦ Effects / ❄ Calm) — flips `data-effects` + persists `calm-cockpit`. | — | [Cockpit.tsx](Cockpit.tsx) |
| The boot-time effects flag it persists to. | — | [main.tsx](../main.tsx) |
| The honest-motion gate the rail transition + the toggle drive. | — | [panels/engine-room/useShouldAnimate.ts](../panels/engine-room/useShouldAnimate.ts) |
| The SSE stream wiring includes an Event River ready callback. | L172-L181 | [Cockpit.tsx](Cockpit.tsx) |
| Typed task/lifecycle selection helpers used by `open` and `selectedLifecycleId`. | — | [data/taskIdentity.ts](../data/taskIdentity.ts) |
| The hosted chat view that receives `selectedLifecycleId`. | — | [panels/Chats.tsx](../panels/Chats.tsx) |
| The highlight composer that filters targets by `selectedLifecycleId`. | — | [panels/HighlightComposer.tsx](../panels/HighlightComposer.tsx) |

## Update History

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
