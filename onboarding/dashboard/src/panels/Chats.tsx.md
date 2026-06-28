# dashboard/src/panels/Chats.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/Chats.tsx`                 |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-27T03:04+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels overview](overview.md)

## Purpose

The **Chats view** (slice 6e): the visible Mode B2 surface. The **"＋ Terminal"** control asks the
server to spawn + own a session (a shell at the workspace root, slice 6e-2a), then the xterm terminal
attaches over the 6d WebSocket — the dashboard owns the session it created. Per-harness launch buttons —
one per **detected** harness (Claude Code / Codex / Pi.dev), icon-left / name-right — sit beside ＋
Terminal (slice 6e-2b), each spawning that agent at the workspace root. Open sessions live in a
left-rail switcher (slice 6e-2c, `SessionList`); selecting one drives the terminal beside it. Task 22
uses mount-on-first-selection persistence: after a refresh only the restored active terminal attaches
immediately, while other restored rows attach when first selected and then stay mounted while hidden so
tab switches preserve xterm content. Task 11 adds hosted-chat lifecycle identity:
when the cockpit has a selected lifecycle, new chats launched here inherit that `lifecycleId`, and an
active untagged chat can be attached manually. Task 22 adds durable session hydration: on mount the
view fetches catalog rows from the backend, restores the last active live session from localStorage
when possible, renders exited rows as status instead of opening a WebSocket, and exposes End as the only
row action. Successful End releases that session's friendly label for later reuse. Backend-persisted
create/end changes are synchronized across browser tabs by subscribing to `data/sessions`
catalog-change events and re-fetching the durable catalog.

## Code Commentary

### Logic

Session state lives in the **`data/sessions` store** (slice 6e-4): `useSessions` selectors read
`sessions: {id,label,kind?,harness?,lifecycleId?,status?}[]` + `activeId`; `sessionStore.getState()`
actions (`add`/`upsert`/`hydrate`/`close`/`setStatus`/`setActive`/`setLifecycle`)
mutate it. The only local state is (6e-2b) `harnesses`. A `useEffect` runs `fetchHarnesses()` on mount;
each **detected** harness renders a launch button (icon-left / name-right — a placeholder monogram via
`HarnessIcon`) beside **"＋ Terminal"**. ＋ Terminal and the harness buttons share one golden
`launchButton` look (6e-2c: the old grey harness buttons read as disabled). Both go through one
`startSession(label, kind, harness?)` helper → the shared `createSession` (`data/sessions`, slice 6f):
it mints a UUID, computes `{label} N`, `openTerminalSession`s it with label/lifecycle metadata (the
server spawns + owns it and persists the catalog row), and registers a running store session — ＋
Terminal passes `("Terminal","terminal")`, a harness button
`(name,"harness",id)`. When `selectedLifecycleId` is passed from `CockpitShell`, `createSession` gets
that fourth argument so the hosted chat is routeable for Gate Respond. If an active session has no
lifecycle tag, the top strip shows `Attach <lifecycleId>` and calls `setLifecycle`; tagged sessions
show a small task badge.

Task 22 adds a second mount effect that calls `fetchTerminalSessionsOrNull()` and hydrates the store from
`fromTerminalSessionInfo`, using `localStorage["ar-dashboard:last-active-chat-session"]` as a preferred
active id. Initial mount ignores failed or empty responses so the dev/test bench does not erase local
mock sessions. A catalog-sync effect subscribes to `subscribeSessionCatalogChanges`; remote create/end
events trigger a fresh catalog fetch where an empty successful list is allowed to hydrate and clear rows
(needed when another tab ends the last session). Remote terminate events include the terminated
`sessionId`; the subscriber immediately marks/closes that row locally and filters the same id from the
catalog hydrate so a stale re-fetch cannot repaint a ghost row. A separate effect writes the active id
back to localStorage. `terminateSession(id)` calls `terminateTerminalSession(id)`, marks the row
`terminated` so the session store releases its label, removes it locally only when the backend confirms
success, and broadcasts a `"terminate"` catalog invalidation with that id to other tabs.

The layout is a top **strip** of launch buttons, then a **body** that splits into the `SessionList`
side-rail (rendered only when sessions exist) and the terminal area. `SessionList` is the open-session
switcher (`onSelect` → `sessionStore.setActive`, `onTerminate`/End → `terminateSession`). Running
sessions mount `<Terminal>` the first time they become active in the current page;
visited terminals stay mounted in `terminalLayer` divs while inactive (`display:none` +
`aria-hidden`) so their xterm buffers survive tab switches. Restored rows that have not been selected
yet stay unmounted, avoiding hidden 0x0 xterm hydration for TUI harnesses after refresh. Exited or
terminated rows render a `statusPanel` instead of opening a WebSocket. Each
`<Terminal>` is wrapped in `<Suspense>` because it is **`lazy`-imported** — xterm is heavy + probes the
canvas on import, so it is code-split and only pulled in when a session opens (also keeps it out of the
jsdom module graph). No active session → the empty-state hint renders inside a shared
`EmptyStateBackdrop` (slice 07b polish): a faint, effects-gated boomerang-video atmosphere (the
**adjutant** clip, `/assets/sc2-adjutant-boomerang.mp4`) behind the centered "＋ Terminal opens a
shell…" copy — pure atmosphere (aria-hidden, absent under calm-cockpit / reduced-motion), which is why
`terminalArea` is a flex column (so the backdrop's `flex:1` canvas fills the slot). (slice 6e-3) Each `<Terminal onConnection>`
registers/deregisters its live `TerminalConnection` into the **`data/sessions` connection registry**
(`registerConnection`, slice 6f — the cockpit-wide inject seam), and a single `SessionComposer` docks
below — its `onSend` injects into the active session via `sendToSession(activeId, bracketedPaste(text))`.

### Invariants And Boundaries

Full-bleed view (the cockpit hides the rails for it, like Engine Room / Topology). Sessions are
**dashboard-owned** (created by ＋ Terminal / a harness button); the id is a client UUID and the label a
friendly `Terminal N` / `{harness} N`, both persisted server-side. End/terminate releases the label so a
new chat can reuse `Claude Code 1` after all prior Claude chats are gone. A session may carry one `lifecycleId`
routing tag for AR-hosted gate responses, but that tag is ephemeral UI/catalog state, not projected
lifecycle truth. End/terminate is the only row action and waits for the backend. The session-switcher behavior + a11y live in `SessionList` (a React Aria `GridList`); this
file owns the session lifecycle + the launch controls. The first genuinely bidirectional cockpit
surface (keystrokes → PTY).
Cross-tab updates are catalog-based: another tab's create/end event causes local id-aware cleanup plus a
server re-fetch; the dashboard does not share arbitrary local store state between tabs.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The open-session switcher side-rail (React Aria `GridList`). | — | [SessionList.tsx](SessionList.tsx) |
| The context composer docked below the terminal (injects to the active session's stdin). | — | [SessionComposer.tsx](SessionComposer.tsx) |
| The lazy-loaded xterm terminal it mounts per session. | — | [Terminal.tsx](Terminal.tsx) |
| The opener, catalog hydrate, and terminate helpers the view drives. | L264-L315 | [data/terminal.ts](../data/terminal.ts) |
| The store hydrate and catalog-row conversion logic used by the mount effect. | L144-L229 | [data/sessions.ts](../data/sessions.ts) |
| The store label allocator distinguishes hidden-live reservations from terminated/exited label release. | L57-L177; L324-L348 | [data/sessions.ts](../data/sessions.ts) |
| The cockpit shell that registers the `chats` full-bleed view. | — | [cockpit/Cockpit.tsx](../cockpit/Cockpit.tsx) |
| The shared empty-state backdrop the no-session state renders (adjutant boomerang). | — | [EmptyStateBackdrop.tsx](EmptyStateBackdrop.tsx) |

## Update History

- 2026-06-27T03:04+02:00 — Task 22 follow-up: removed the local Hide path from `Chats`/`SessionList`
  wiring, made End the only row action, and made remote terminate broadcasts remove the named session id
  locally while filtering the same id from the follow-up catalog hydrate to avoid ghost rows.
- 2026-06-27T01:25+02:00 — Task 22 follow-up: `Chats` now subscribes to terminal-catalog
  `BroadcastChannel` invalidations, re-fetches `/api/terminal/sessions` for remote tab changes, allows a
  successful empty catalog to clear stale local rows, and broadcasts after backend-confirmed End. Initial
  mount still distinguishes fetch failure from empty catalog to preserve dev/test local sessions.
  Verification metadata pinned until closeout stamps the task-22 follow-up code commit.
- 2026-06-27T01:03+02:00 — Task 22 follow-up: `Chats` now marks a backend-confirmed End action as
  `terminated` before removing the row locally, so the session store releases that label while Hide keeps
  live hidden labels reserved.
- 2026-06-27T00:25+02:00 — Task 22 follow-up: `Chats` now mounts restored sessions on first selection
  and keeps visited terminals mounted while hidden; this avoids hidden initial hydration after refresh
  without losing xterm content when switching between chat tabs.
- 2026-06-26T23:05+02:00 — Task 22: `Chats` now hydrates backend terminal catalog rows on mount,
  remembers the last active session id in localStorage, renders exited/terminated rows as status panels
  instead of terminals, and routes SessionList Hide locally while Terminate waits for the backend
  terminate route before closing the row. Verification metadata pinned until closeout stamps the task-22
  code commit.
- 2026-06-23T13:45+02:00 — Task 11: added optional `selectedLifecycleId` from the cockpit shell. New
  terminal/harness sessions launched while a lifecycle is selected are tagged via `createSession(...,
  lifecycleId)`, and an active untagged session can be attached with the strip control. Verification
  metadata pinned until closeout stamps the task-11 code commit.
- 2026-06-23T04:20+02:00 — Slice 07b polish: the no-session empty state now renders inside the shared
  `EmptyStateBackdrop` — a faint, effects-gated **adjutant** boomerang-video atmosphere
  (`/assets/sc2-adjutant-boomerang.mp4`, aria-hidden, absent under calm-cockpit / reduced-motion) behind
  the "＋ Terminal opens a shell…" copy, replacing the bare `empty` hint. `terminalArea` already being a
  flex column lets the backdrop's `flex:1` canvas fill the slot. Added the `EmptyStateBackdrop`
  reference. Verification metadata pinned until closeout stamps the slice-07b code commit.
- 2026-06-19T15:59 — Task 6 slice 6f-1: connections now register into the `data/sessions` store (`registerConnection`) instead of a local `conns` ref, and `startSession` + the `SessionComposer` route through the shared `createSession` / `sendToSession` — so the cockpit-wide highlight composer shares the same inject seam. No behavior change to the Chats view itself. Verification metadata pinned until closeout stamps the 6f-1 code commit.
- 2026-06-19T14:05 — Task 6 slice 6e-4: moved the session registry into the `data/sessions` store (`useSessions`/`sessionStore`), and now mount **every** open session's `<Terminal>` (inactive ones `display:none` + `aria-hidden`) instead of a single `key={activeId}` terminal — switching tabs flips `display` rather than unmounting, so each session's xterm + WebSocket survive (fixes "tabbing away bricks the session"). The composer injects via a `conns` `Map` keyed by session id; added the persistence test in `Chats.test.tsx`. Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-19T05:48 — Task 6 slice 6e-3: docked a `SessionComposer` below the terminal for context injection — `<Terminal onConnection>` captures the live `TerminalConnection` in an `activeConn` ref; the composer's `onSend` writes to that session's stdin as a bracketed paste. Verification metadata pinned until closeout stamps the 6e-3 code commit.
- 2026-06-19T04:38 — Task 6 slice 6e-2c: replaced the horizontal session **tab strip** with a left-rail `SessionList` switcher (extracted to its own React Aria `GridList` component); the launch controls stay in the top strip and the harness buttons now share ＋ Terminal's golden `launchButton` look (the grey ones read as disabled). Verification metadata pinned until closeout stamps the 6e-2c code commit.
- 2026-06-18T21:27 — Task 6 slice 6e-2b: added per-harness launch buttons — `fetchHarnesses()` on mount → a button per **detected** harness (icon-left/name-right via `HarnessIcon`) beside ＋ Terminal; folded ＋ Terminal + harness opens into one `startSession(label, kind, harness?)`. Verification metadata pinned until closeout stamps the 6e-2b code commit.
- 2026-06-18T17:40 — Task 6 slice 6e-2a: reworked from "attach to a store lifecycle" to **create a dashboard-owned session** — "＋ Terminal" mints a UUID, `openTerminalSession` POSTs the opener (server spawns the shell), and a closable `Terminal N` tab + the xterm pane render. Dropped the zustand `lifecycles` dependency. Verification metadata pinned until closeout stamps the 6e-2a code commit.
- 2026-06-18T16:50 — Created for task 6 slice 6e-1: the Chats view — a lifecycle session tab strip + a lazy/Suspense-mounted full-bleed xterm terminal. Verification metadata pinned to the task base until closeout stamps the 6e-1 code commit.
