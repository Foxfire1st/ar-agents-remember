# dashboard/src/data/sessions.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/sessions.ts`                 |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash | `0d5ce6784930aa4e9006ab4bbf2b788a3296abce`       |
| lastVerifiedCommitDate | 2026-07-10T22:30:19+02:00|
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
`gate.lifecycleId` resolve back to one hosted chat via `findSessionForLifecycle`. Slice L5 adds the
parallel **leaf identity**: an `OpenSession` may carry a durable `leafKey` (the qualified leaf id
`repo/master/leaf-id`), so one chat is bound to a leaf and `findSessionForLeaf(leafKey)` resolves the
shared session both the Chats page row and the right-rail `RailChat` render. Task 22 extends this
store into the hydrated dashboard view of the backend catalog: sessions can carry kind/harness/status,
catalog rows can be merged in after a refresh, exited/landed/terminated rows are not used for lifecycle
injection, chat labels reuse released ordinals after destructive termination, and backend-persisted
create/terminate changes are broadcast to other browser tabs as catalog invalidation events that include
the changed session id. The reopened L6 follow-up separates **draft paste** from confirmed submit:
leaf-context handoff uses `pasteDraftToSession` to place the context package in the chat input without
pressing Enter — delivery is confirmed via the paste's own echo and retried through the harness boot
window (`pasteAndConfirm` in `data/terminal.ts`) — while existing highlight/gate delivery keeps the
submit-and-confirm path. L9 extends the
catalog invalidation contract with a `"leaf"` reason so hosted chat leaf moves made by another tab or the
agent-facing MCP tool can rehydrate open dashboard stores without a full page refresh.

## Code Commentary

### 260707-HFX2-L17 Binding Role In The Client Registry

`OpenSession.seatRole` is current leaf-seat identity; `spawnRole` remains origin provenance.
`sessionSeatRole` prefers binding, then provenance, then transport fallback for legacy rows, while
`attachSeatRole` intentionally leaves an untyped generic chat unselected so the operator must
choose. Local uniqueness and `applyLeafAssignment` compare the selected seat role, clearing only a
same-role owner and preserving different roles on the leaf. Catalog hydration carries `seatRole`.

### Logic

`sessionStore = createStore<SessionState>(...)` (zustand vanilla) holds `sessions: OpenSession[]`
(`{id, label, kind?, harness?, lifecycleId?, leafKey?, spawnRole?, status?, landedAt?,
landedReason?, landedEdge?}`), `activeId: string |
null`, a coarse `count`, the highest live ordinal retained for coarse inspection. 260703-L14 adds
`OpenSession.spawnRole?` — the AR_SPAWN_ROLE the backend recorded on the catalog row at spawn
(orchestrator/strategist/manager/worker/reviewer…), read-only provenance this store merely carries:
it is the Chats command-tree grouping key (`data/sessionGroups` decks command roles) and the
`SessionList` role chip, mapped in by `fromTerminalSessionInfo` (set only when present, like
`leafKey`).
`add(prefix, id, lifecycleId?)` appends a session labelled with the lowest available live ordinal for
that prefix, optionally tags it with a lifecycle, updates the tracked ordinal, and makes it active.
`upsert(session, activate=true)` inserts/replaces a server-owned session row while clearing any older
owner of the same lifecycle, and `hydrate(sessions, preferredActiveId?)` replaces local rows with
catalog rows, restores the preferred or current active live session when possible, and recomputes the
tracked ordinal from live rows. Live means `status` absent/`running`; `landed` is intentionally
non-live, so it releases labels, lifecycle routing, and leaf lookup while remaining renderable.
`setStatus` updates a row and moves focus away from the active session when it stops running.
`fromTerminalSessionInfo` converts the API shape from `data/terminal.ts` into an `OpenSession`,
including landed provenance when present.
`close(id)` drops the local row and clears `activeId` **only if** it was the one removed. It never kills
tmux by itself; destructive termination is the caller-owned backend route through `data/terminal.ts`
and `serving.app`.
`setActive(id)` moves the active pointer.
`setLifecycle(id, lifecycleId|null)` attaches or clears the lifecycle tag; when a tag is set, any
other session that previously owned that lifecycle is cleared, so `findSessionForLifecycle(lifecycleId)`
has a single **live** target for gate-response delivery.
A session's leaf-uniqueness **role** mirrors the backend: `SessionRole = "chat" | "terminal"` and
`sessionRole(session)` returns `"terminal"` for a `kind === "terminal"` shell, else `"chat"` (any agent
harness). `setLeaf(id, leafKey|null)` (slice L5) binds or clears a session's durable `leafKey`. The
non-null bind carries a **role-scoped advisory uniqueness guard** (L5 fix 2): it looks up the binding
session's role and treats the bind as a no-op only if another *live* session **of the same role** already
owns that leaf — so a chat and a terminal can both bind one leaf without blocking each other, and a second
same-role claim loses. It is purely a local convenience, since the server's `409 leaf-taken` is the real
arbiter; clearing routes through a `clearLeaf` helper (the `clearLifecycle` mirror, `delete`s the key so an
absent leaf is truly unset). L9 adds `applyLeafAssignment(id, leafKey|null)` for server/catalog-authoritative
updates after a successful attach/move: it assigns the target session and clears any same-role local owner
of the destination leaf because the backend result has already won. `findSessionForLeaf(leafKey, role?)` returns the single **live** session
bound to a leaf (mirrors `findSessionForLifecycle`); the optional `role` filter resolves the leaf's chat
vs. its terminal independently. `createSession(prefix, kind?, harness?, lifecycleId?, leafKey?)` takes a
`leafKey` it sends to the opener and stamps on the new running row. `fromTerminalSessionInfo` maps the
catalog row's `leafKey` onto the store row alongside harness/lifecycle.
`useSessions(selector)` is the React seam — `useStore(sessionStore, selector)` so components subscribe
to a slice; non-React callers (`Chats` event handlers) read `sessionStore.getState()` directly.

Task 22 follow-up adds a `BroadcastChannel` catalog-sync seam, extended by L9 for leaf moves:
`notifySessionCatalogChanged(reason, sessionId?)` posts `"create"`/`"terminate"`/`"leaf"` events after a
backend catalog mutation succeeds, and `subscribeSessionCatalogChanges(callback)` receives events from
other tabs while ignoring this tab's own source id. The channel carries invalidation plus the changed
session id; receivers still re-fetch `/api/terminal/sessions` instead of trusting another tab's local
store state.

Slice 6f adds a non-reactive **connection registry** beside the store (module-level maps, so a
registration never re-renders): `registerConnection(id, conn|null)` — called by `<Chats>` via
`onConnection` — records each live `TerminalConnection`; `sendToSession(id, text)` injects into it, or
**queues** the text in `pending` when the session's terminal has not registered yet (the
create-then-send race; the connection itself buffers anything sent before its WebSocket opens, see
`data/terminal.ts`), flushed on register. `createSession(prefix, kind?, harness?, lifecycleId?)` mints a UUID,
posts the opener with the generated label/lifecycle, upserts the running local row, and broadcasts
`"create"` only if the backend opener persisted the catalog row — the shared spawn used by both the
Chats launch buttons and the highlight composer's create-a-chat path. `pasteDraftToSession(id,
packageText)` is the leaf-context draft path: it waits for the session's terminal to register (bounded by
`CONNECTION_TIMEOUT_MS`), then delegates to `data/terminal.ts`'s `pasteAndConfirm` — quiet-gated paste
attempts confirmed by the draft's own echo and retried through a ~30s harness boot deadline, because a
booting Claude Code discards stdin until its composer mounts. It returns `"delivered"` only once an
attempt echoed, else `"unconfirmed"`, and never calls the submit/confirm loop (no Enter). `deliverToSession(id, packageText)` remains the create-then-send delivery path for
surfaces that intentionally submit: it waits for the session's terminal to register **and** its harness to
look ready (`conn.whenReady()`), injects one sanitized bracketed paste, and submits/observes the response
loop so callers can surface `"delivered"` vs `"unconfirmed"` instead of silently dropping a package.

### Conventions

zustand vanilla `createStore` + a `useStore` selector hook (mirrors `data/store.ts`). State is a flat
object with the action methods on it, not a separate actions slice.

### Invariants And Boundaries

- Ephemeral UI state only — never persisted, never the projected lifecycle truth (`data/store.ts`).
- Labels allocate per prefix from live rows only. End/terminated, landed, and exited rows release labels so a
  fresh chat can become `Claude Code 1` again once prior Claude chats are gone.
- Closing a local row forgets it here but does **not** kill the backend tmux session; explicit terminate
  goes through `data/terminal.ts` + `serving.app`.
- Owns the *registry*, not terminal lifetime: tmux/catalog own durability, and `<Chats>` owns which
  selected/visited rows currently have live xterm + WebSocket attachments.
- Cross-tab sync is catalog invalidation, not shared local state. Backend-persisted create/terminate/leaf
  broadcasts tell other tabs which session changed, then those tabs re-fetch the durable catalog.
- `lifecycleId` is a routing tag for AR-hosted chats only. It is not projected truth, and external
  non-hosted chats use the task-10 operator inbox path outside this store. Exited/landed/terminated sessions
  must not receive lifecycle-routed injection.
- `leafKey` is the durable chat⇄leaf binding (qualified leaf id), enclosure-independent so it survives
  finalize. Uniqueness is **server-authoritative** and per **(leaf, role)** (`409 leaf-taken`,
  running-only); `setLeaf`'s local guard is advisory and role-scoped (a chat and a terminal never block
  each other on one leaf). L9 moves use `applyLeafAssignment` and mutate the store only after the backend
  accepts the catalog change or after catalog rehydration observes the new binding. `findSessionForLeaf` resolves only **live** sessions
  (optionally filtered by role), so an exited/landed/terminated session frees its slot for a new claim.
- Draft paste and submitted delivery are intentionally separate seams. Leaf-context handoff must not press
  Enter on the operator's behalf; highlight/gate delivery can still call `deliverToSession` when the UI
  action is explicitly a send.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The Chats view that reads this store + drives session actions including server-confirmed leaf moves. | — | [panels/Chats.tsx](../panels/Chats.tsx) |
| The right-rail leaf chat resolves sessions via leaf role and now uses `pasteDraftToSession` for bind-time context after start, attach, or move. | L309-L315; L317-L353 | [panels/RailChat.tsx](../panels/RailChat.tsx) |
| The session switcher that renders `sessions` + reports select/close. | — | [panels/SessionList.tsx](../panels/SessionList.tsx) |
| The leaf-identity helper that mints the qualified `leafKey` this store binds. | — | [data/taskIdentity.ts](taskIdentity.ts) |
| The gate responder that resolves `gate.lifecycleId` through `findSessionForLifecycle`. | — | [panels/GateResponder.tsx](../panels/GateResponder.tsx) |
| The projection store this mirrors in pattern but stays separate from. | — | [data/store.ts](store.ts) |
| The terminal client types/source that provide catalog rows and terminate/open/attach helpers. | L228-L315 | [terminal.ts](terminal.ts) |
| Catalog-change messages accept the L9 `"leaf"` reason and carry the changed session id for out-of-band reassignment invalidation. | L32-L85 | [sessions.ts](sessions.ts) |
| The label allocator derives the next label from live rows and releases labels when rows are no longer live. | L127-L148; L209-L230 | [sessions.ts](sessions.ts) |
| `setLeaf` keeps role-scoped advisory uniqueness local, while `applyLeafAssignment` applies successful server moves and clears stale same-role local owners. | L104-L114; L270-L317 | [sessions.ts](sessions.ts) |
| `pasteDraftToSession` waits for the live connection and delegates to the confirmed `pasteAndConfirm` draft loop (echo-confirmed, boot-deadline retries, no Enter); `deliverToSession` keeps the submit-and-confirm path. | L433-L459 | [sessions.ts](sessions.ts) |
| The backend tmux session that persists after `close` and is killed only by explicit terminate. | L330-L347 | [serving/terminal.py](../../../mcp/src/agents_remember/serving/terminal.py) |

## Update History

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: added authoritative binding-role state and helpers,
  made advisory/apply assignment pair-scoped, preserved different-role owners, and required
  explicit role choice for an untyped hand-opened chat.

- 2026-07-09T13:07+02:00 — 260707-HFX2-L11 (landed chat archive): `OpenSession` and
  `fromTerminalSessionInfo` now carry landed provenance, and live-session tests treat
  `status:"landed"` as non-live. Landed rows remain in the store for inspection but release labels,
  lifecycle routing, and leaf ownership like exited rows. Verification metadata remains pinned until
  closeout stamps the HFX2-L11 commit.

- 2026-07-06T23:56:54+02:00 — 260703-L14 (visual hierarchy + chat grouping): `OpenSession` gained
  `spawnRole?` (the AR_SPAWN_ROLE recorded on the backend catalog row — the command-tree grouping
  key + role chip), carried through `fromTerminalSessionInfo` when present; no store action reads
  or mutates it. Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-02T17:04+02:00 — L9: added `"leaf"` as a first-class terminal-catalog invalidation reason and
  clarified that hosted chat leaf moves update this store only after server success or catalog rehydrate.
  The `leafKey` uniqueness guard remains advisory and role-scoped, while `applyLeafAssignment` applies
  server-confirmed moves so stale local owners cannot veto the accepted catalog result. Verification
  metadata pinned until closeout stamps the L9 commit.
- 2026-07-02T16:35+02:00 — Reopened L6 paste-loss fix: `pasteDraftToSession` no longer fire-and-forgets —
  it delegates to `data/terminal.ts`'s `pasteAndConfirm` (echo-confirmed, quiet-gated attempts retried
  over a 30s boot deadline) so a draft dropped into a booting Claude Code is retried instead of silently
  lost, and `"delivered"` is only reported once the composer echoed the paste. Verification metadata
  pinned until closeout stamps the follow-up commit.
- 2026-07-02T13:07+02:00 — Reopened L6 follow-up: added the draft-paste delivery seam for leaf-context
  handoff. `pasteDraftToSession` uses the existing connection wait and sanitizing bracketed-paste path but
  deliberately does not call the submit/confirm loop, so an operator can append their own instruction
  before pressing Enter. Verification metadata pinned until closeout stamps the follow-up commit.
- 2026-06-30T00:00:00+02:00 — L5 follow-up: leaf uniqueness is now per **(leaf, role)**. Added `SessionRole` +
  `sessionRole(session)` (a `kind:"terminal"` shell is a terminal, any harness is a chat, mirroring the
  backend `role_for_kind`); the `setLeaf` advisory guard is role-scoped (a chat and a terminal can both
  bind one leaf), and `findSessionForLeaf(leafKey, role?)` gained an optional role filter so the leaf's chat
  and terminal resolve independently. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-30T00:00:00+02:00 — L5 (Sidebar chat): added durable leaf identity to the session registry. `OpenSession`
  gained an optional `leafKey` (qualified leaf id); `setLeaf(id, leafKey|null)` binds/clears it with an
  advisory local-uniqueness guard (server `409 leaf-taken` is the real arbiter) and a `clearLeaf` helper;
  `findSessionForLeaf(leafKey)` returns the single live bound session; `fromTerminalSessionInfo` maps
  `leafKey`; and `createSession` takes a `leafKey` it forwards to the opener and stamps on the row.
  Verification metadata pinned until closeout stamps the L5 commit.
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
