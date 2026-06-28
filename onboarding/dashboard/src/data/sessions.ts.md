# dashboard/src/data/sessions.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/sessions.ts`                 |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-27T03:04+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

The open-terminal/chat **session registry** for the Chats view (slice 6e-4): a module-level zustand
store holding which sessions exist and which one is active. Same store pattern as the observer
projection store (`data/store.ts`) but deliberately **separate** — ephemeral client UI state, not
projected truth — so the Chats surface and its tests share one source of session state instead of
`Chats` local `useState`. Terminal persistence across refresh, view switches, and session switches is
owned by the backend catalog + tmux; this store tracks the list + active id while `<Chats>` mounts a
row's terminal on first selection and keeps visited terminals mounted while hidden. Slice 6f also makes it the
**cockpit-wide inject seam**: it holds
the live per-session `TerminalConnection`s plus a `sendToSession` / `createSession` API, so a surface
outside `<Chats>` (the highlight composer) can inject into — or spawn — a session.
Task 11 adds the AR-hosted gate-response route: an `OpenSession` may carry `lifecycleId`, letting
`gate.lifecycleId` resolve back to one hosted chat via `findSessionForLifecycle`. Task 22 extends this
store into the hydrated dashboard view of the backend catalog: sessions can carry kind/harness/status,
catalog rows can be merged in after a refresh, exited/terminated rows are not used for lifecycle
injection, chat labels reuse released ordinals after destructive termination, and backend-persisted
create/terminate changes are broadcast to other browser tabs as catalog invalidation events that include
the changed session id.

## Code Commentary

### Logic

`sessionStore = createStore<SessionState>(...)` (zustand vanilla) holds `sessions: OpenSession[]`
(`{id, label, kind?, harness?, lifecycleId?, status?}`), `activeId: string | null`, a coarse
`count`, the highest live ordinal retained for coarse inspection.
`add(prefix, id, lifecycleId?)` appends a session labelled with the lowest available live ordinal for
that prefix, optionally tags it with a lifecycle, updates the tracked ordinal, and makes it active.
`upsert(session, activate=true)` inserts/replaces a server-owned session row while clearing any older
owner of the same lifecycle, and `hydrate(sessions, preferredActiveId?)` replaces local rows with
catalog rows, restores the preferred or current active live session when possible, and recomputes the
tracked ordinal from live rows. `setStatus` updates a row and moves focus away from the active session
when it stops running. `fromTerminalSessionInfo` converts the API shape from `data/terminal.ts` into an
`OpenSession`.
`close(id)` drops the local row and clears `activeId` **only if** it was the one removed. It never kills
tmux by itself; destructive termination is the caller-owned backend route through `data/terminal.ts`
and `serving.app`.
`setActive(id)` moves the active pointer.
`setLifecycle(id, lifecycleId|null)` attaches or clears the lifecycle tag; when a tag is set, any
other session that previously owned that lifecycle is cleared, so `findSessionForLifecycle(lifecycleId)`
has a single **live** target for gate-response delivery.
`useSessions(selector)` is the React seam — `useStore(sessionStore, selector)` so components subscribe
to a slice; non-React callers (`Chats` event handlers) read `sessionStore.getState()` directly.

Task 22 follow-up adds a `BroadcastChannel` catalog-sync seam:
`notifySessionCatalogChanged(reason, sessionId?)` posts `"create"`/`"terminate"` events after a backend
catalog mutation succeeds, and `subscribeSessionCatalogChanges(callback)` receives events from other
tabs while ignoring this tab's own source id. The channel carries invalidation plus the changed session
id; receivers still re-fetch `/api/terminal/sessions` instead of trusting another tab's local store
state.

Slice 6f adds a non-reactive **connection registry** beside the store (module-level maps, so a
registration never re-renders): `registerConnection(id, conn|null)` — called by `<Chats>` via
`onConnection` — records each live `TerminalConnection`; `sendToSession(id, text)` injects into it, or
**queues** the text in `pending` when the session's terminal has not registered yet (the
create-then-send race; the connection itself buffers anything sent before its WebSocket opens, see
`data/terminal.ts`), flushed on register. `createSession(prefix, kind?, harness?, lifecycleId?)` mints a UUID,
posts the opener with the generated label/lifecycle, upserts the running local row, and broadcasts
`"create"` only if the backend opener persisted the catalog row — the shared spawn used by both the
Chats launch buttons and the highlight composer's create-a-chat path. `deliverToSession(id, packageText)`
is the create-then-send
delivery path: it waits for the session's terminal to register **and** its harness to look ready
(`conn.whenReady()`), injects one sanitized bracketed paste, and submits/observes the response loop so
callers can surface `"delivered"` vs `"unconfirmed"` instead of silently dropping a package.

### Conventions

zustand vanilla `createStore` + a `useStore` selector hook (mirrors `data/store.ts`). State is a flat
object with the action methods on it, not a separate actions slice.

### Invariants And Boundaries

- Ephemeral UI state only — never persisted, never the projected lifecycle truth (`data/store.ts`).
- Labels allocate per prefix from live rows only. End/terminated and exited rows release labels so a
  fresh chat can become `Claude Code 1` again once prior Claude chats are gone.
- Closing a local row forgets it here but does **not** kill the backend tmux session; explicit terminate
  goes through `data/terminal.ts` + `serving.app`.
- Owns the *registry*, not terminal lifetime: tmux/catalog own durability, and `<Chats>` owns which
  selected/visited rows currently have live xterm + WebSocket attachments.
- Cross-tab sync is catalog invalidation, not shared local state. Backend-persisted create/terminate
  broadcasts tell other tabs which session changed, then those tabs re-fetch the durable catalog.
- `lifecycleId` is a routing tag for AR-hosted chats only. It is not projected truth, and external
  non-hosted chats use the task-10 operator inbox path outside this store. Exited/terminated sessions
  must not receive lifecycle-routed injection.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The Chats view that reads this store + drives `add`/`close`/`setActive`. | — | [panels/Chats.tsx](../panels/Chats.tsx) |
| The session switcher that renders `sessions` + reports select/close. | — | [panels/SessionList.tsx](../panels/SessionList.tsx) |
| The gate responder that resolves `gate.lifecycleId` through `findSessionForLifecycle`. | — | [panels/GateResponder.tsx](../panels/GateResponder.tsx) |
| The projection store this mirrors in pattern but stays separate from. | — | [data/store.ts](store.ts) |
| The terminal client types/source that provide catalog rows and terminate/open helpers. | L228-L315 | [terminal.ts](terminal.ts) |
| The label allocator derives the next label from live rows and releases labels when rows are no longer live. | L127-L148; L209-L230 | [sessions.ts](sessions.ts) |
| The backend tmux session that persists after `close` and is killed only by explicit terminate. | L330-L347 | [serving/terminal.py](../../../mcp/src/agents_remember/serving/terminal.py) |

## Update History

- 2026-06-27T03:04+02:00 — Task 22 follow-up: removed the hidden-live label reservation state now that
  the UI no longer exposes Hide, and extended catalog-change broadcasts with `sessionId` so other tabs
  can remove the terminated row deterministically before rehydrating.
- 2026-06-27T01:25+02:00 — Task 22 follow-up: added `BroadcastChannel` catalog-change helpers and made
  `createSession` broadcast a `"create"` invalidation only after the backend opener succeeds. Other tabs
  subscribe through `Chats` and re-fetch the durable catalog instead of sharing local store state.
  Verification metadata pinned until closeout stamps the task-22 follow-up code commit.
- 2026-06-27T01:03+02:00 — Task 22 follow-up: replaced the old monotonic/global label-counter model
  with per-prefix lowest-available labels. Locally hidden live rows reserve their label until refresh,
  while terminated/exited rows release it so new Claude chats can restart at `Claude Code 1`.
- 2026-06-27T00:25+02:00 — Task 22 follow-up: updated the store comments/docs for mount-on-first-selection
  terminal attachment; restored inactive rows wait until visible, while visited rows remain mounted.
- 2026-06-26T23:05+02:00 — Task 22: extended `OpenSession` with kind/harness/status, added
  `upsert`/`hydrate`/`setStatus` and catalog-row conversion, made lifecycle lookup ignore
  exited/terminated rows, and changed `createSession` to send the generated label/lifecycle to the
  backend opener before registering a running row. Verification metadata pinned until closeout stamps
  the task-22 code commit.
- 2026-06-23T15:05+02:00 — Task 10 dashboard fallback: corrected the external-chat boundary now that non-hosted chats use the operator inbox path instead of a future inbox/poll placeholder. No source change in `sessions.ts`; this is current-state memory correction after task 10 completed the fallback.
- 2026-06-23T13:45+02:00 — Task 11: added hosted chat ⇄ lifecycle identity. `OpenSession` now carries
  optional `lifecycleId`; `add`/`createSession` accept it, `setLifecycle` attaches/clears it, and
  `findSessionForLifecycle` gives the Gate Respond path one chat target per lifecycle. Also refreshed
  the delivery commentary to describe `deliverToSession`'s confirmed bracketed-paste path. Verification
  metadata pinned until closeout stamps the task-11 code commit.
- 2026-06-19T15:59 — Task 6 slice 6f-1: made the store the cockpit-wide **inject seam** — added a non-reactive connection registry (`registerConnection` / `sendToSession`, with a `pending` queue for the create-then-send race), `createSession` (the shared spawn), and `sendWhenReady` (waits for the connection + the harness's `whenReady` before injecting, so a fresh agent doesn't drop the package mid-boot). `<Chats>` now registers connections here instead of a local ref. Verification metadata pinned until closeout stamps the 6f-1 code commit.
- 2026-06-19T14:05 — Created for task 6 slice 6e-4: the session registry extracted from `Chats` local state into a module-level zustand store (`sessions`/`activeId`/`count` + `add`/`close`/`setActive`, `useSessions` selector hook) so the session list is shared + testable and `Chats` can keep every session's terminal mounted. Verification metadata pinned until closeout stamps the 6e-4 code commit.
