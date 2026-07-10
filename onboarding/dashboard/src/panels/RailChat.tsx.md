# dashboard/src/panels/RailChat.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/RailChat.tsx`              |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash | `e400ed0ce98752d1b65d00de97c9b84c7ea20814`       |
| lastVerifiedCommitDate | 2026-07-10T20:04:45+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels overview](overview.md)

## Purpose

The **single-instance right-rail chat** (slice L5): the surface the cockpit's `RailToggle` swaps in for
the Event River. It is anchored on the durable **qualified leaf id** (`leafKey` = `repo/master/leaf-id`),
not the enclosure, so it resolves with no live worktree and after finalize. It reuses the **same**
`Terminal` + `SessionComposer` and the shared `data/sessions` connection registry as the Chats page —
there is exactly one xterm/WebSocket per session, so the Chats-page row and this rail surface drive the
same live session. After the L5 fix pass a leaf has **two** distinct slots: a **chat** (an agent harness —
Claude Code / Codex / Pi.dev) and an optional **terminal** (a plain shell). When both exist they render as
a **vertical split** (chat on top, terminal below); when none exists the empty state offers a **harness
choice** to start a chat plus a separate **＋ Terminal** to open a shell. L6 adds the leaf-chat context
handoff: when an agent chat is created for the displayed leaf, or a free chat is attached to a picked
leaf, the rail builds a concise context package from the matching task document plus active process
projection and pastes it into that chat as **draft input**. It does not submit on the operator's behalf;
the operator can add an instruction and then press Enter manually. L9 keeps the attach picker visible for
an already-attached chat as a move control; a successful move updates the durable leaf binding and drafts
the newly selected leaf's context without respawning the terminal session.

## Code Commentary

### 260707-HFX2-L17 Role-Aware Rail Attach And Identity

Rail attach/move posts the selected role and applies the server-authoritative pair. The picker
preselects declared identity but requires a choice for a hand-opened generic chat, and pane headers
render current binding role before label. The focused rail still shows one chat plus optional
terminal; the complete multi-role fleet remains available in the session list.

### Logic

`RailChat({ leafKey, selectedLifecycleId, taskDocuments, engineProcesses, contextMaster })` reads
`sessions` from the `data/sessions` store and resolves the leaf's two slots independently by filtering
running sessions by `leafKey` and `sessionRole`: `chatSession` = the most recent running session on this
leaf whose role is `"chat"`, `terminalSession` = the running `"terminal"` one. With no viewed leaf, the
same resolver intentionally returns the latest unattached/free session of each role so an operator can
start a chat anywhere and attach it later. A `useEffect` fetches `fetchHarnesses()` once on mount and keeps
the detected set in state; `detected.length > 0` renders one
**`＋ {harness.name}`** start button per detected harness (testid `rail-start-chat-{id}`), else a passive
"No agent detected on PATH." note. A local `mountedSessionIds` set mirrors the Chats-page pattern: a
`useEffect` keeps every session id surfaced here (and still in the store) so switching leaves keeps a
previously-surfaced session **mounted but hidden** (a `display:none` + `aria-hidden` keep-alive layer that
re-mounts the lazy `Terminal` into the shared registry) rather than tearing down its xterm buffer / live
WebSocket; ids whose sessions have left the store are pruned.

`buildLeafContextPackage` is the L6 packet builder. It matches the selected/picked durable leaf key to a
`TaskDocNode` with `qualifiedLeafKey(doc)`, finds the corresponding `EngineProcessNode` by lifecycle id or
case-normalized leaf id, and renders task id/title/status, leaf key, task-document path, lifecycle id,
worktree group, code worktree, memory worktree, objective, requirements, and top-level steps. The package
ends with a direct instruction to attach to the lifecycle/leaf before working. `deliverLeafContext`
pastes that packet with `pasteDraftToSession`; an `"unconfirmed"` result surfaces a small
`rail-leaf-context-note` status instead of silently claiming delivery. Because this path is draft-only, it
does not call the submit-and-confirm delivery helper and does not press Enter.

`startChat(harness)` calls `createSession(harness.name, "harness", harness.id, selectedLifecycleId,
leafKey)` — an **agent chat** that claims the leaf's chat slot (and inherits the selected lifecycle tag)
when a leaf is being viewed, or a free unattached chat when no leaf is being viewed. If `leafKey` is
present, it immediately sends the context package to the created chat. `openTerminal()` calls
`createSession("Terminal", "terminal", undefined, selectedLifecycleId, leafKey)` for a plain shell on the
terminal slot and does **not** send leaf context. `attachChatToLeaf(sessionId, lk)` is the other L6/L9
timing point: after `attachSessionToLeaf` returns `"ok"`, the rail updates the local store, broadcasts the
`"leaf"` catalog change, and delivers the packet for the picked leaf. A `409 leaf-taken` attach/move never
mutates the store and never injects context.

Render branches: a leaf with neither slot filled shows the leaf empty state (`rail-chat-empty`) with the
harness-choice affordance + `rail-open-terminal`; no leaf shows the free-chat empty state and still offers
agent/terminal creation. When any chat is visible, a `LeafAttachPicker` drills the task tree (pre-drilled
by `contextMaster`) and attaches or moves that chat to the picked leaf. Otherwise each present slot renders a
`Pane` and each missing slot a thin `slotBar` affordance (start chat / ＋ Terminal) so the split can be
completed without leaving the rail. A `Pane` (`rail-pane-{role}`) is a header row — a **truncating**
`paneTitle` carrying the full `session.label` as a hover-reveal `title` (fix 4) and an **End** terminate
control (`rail-terminate-{role}`, fix 3) — over the `<Suspense>`-wrapped lazy `Terminal` registered through
`onConnection`, and that pane's `SessionComposer`, which injects into
*that* session's stdin via `sendToSession(session.id, bracketedPaste(sanitizeForInjection(text)))`.
`terminate(id)` awaits `terminateTerminalSession(id)`, then marks the row `terminated` + `close`s it
locally and posts a `notifySessionCatalogChanged("terminate", id)` broadcast — so ending one slot frees
only that slot. The heading shows `Chat · {leafIdFromKey(leafKey)}`.

### Conventions

Co-located Panda `css()`; the lazy `Terminal` import mirrors `Chats` (xterm is code-split — it probes the
canvas on import and cannot mount under jsdom). `data-testid`s: `rail-chat`, `rail-chat-heading`,
`rail-chat-empty`, `rail-start-chat` / `rail-start-chat-{id}`, `rail-no-harness`, `rail-open-terminal`,
`rail-attach-row`, `rail-attach-leaf-picker`, `rail-leaf-attach-error`, `rail-leaf-context-note`,
`rail-pane-{role}`, `rail-terminate-{role}`, `rail-chat-keepalive-{id}`. `isRunning` treats a missing
`status` as `"running"` (the optimistic default for a freshly created session).

### Invariants And Boundaries

- **Single instance, shared session:** the connection registry is shared with `Chats`, so this rail and
  the Chats page never open competing sockets for one leaf — they surface the same session.
- **Leaf-keyed, enclosure-independent:** binding is on the durable `leafKey`; it survives finalize and a
  missing worktree. Uniqueness is per **(leaf, role)** and server-authoritative (`409 leaf-taken`) — this
  component only *reads* the leaf's chat + terminal slots and *opens* sessions carrying the leaf, never
  arbitrating ownership.
- **Chat vs terminal are separate slots:** a chat is an agent harness; a terminal is a shell. They never
  conflict on one leaf and terminate independently — ending the chat leaves the terminal (and vice versa).
- **Mounted-not-unmounted on leaf switch:** surfaced sessions stay mounted while hidden so their xterm
  buffers survive a leaf switch; only a session that leaves the store is dropped.
- **Context delivery happens only at leaf bind time:** start-on-leaf and successful attach/move are the
  packet-delivery points. Free/off-leaf chat creation, plain terminal creation, and rejected attaches/moves
  do not inject leaf context. The packet is pasted as editable draft input, not submitted.
- **Context packet is projected-state only:** the rail reads `taskDocuments` and `engineProcesses`; it does
  not fetch task files, inspect worktrees, or invent missing worktree facts. A missing task document means
  no packet is sent.
- Presentational over the store + the lazy terminal; backend calls go through the openers
  (`createSession`) and the terminate client (`terminateTerminalSession`), never arbitrating ownership.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The rail builds the leaf context package, pastes it as draft input after start-on-leaf or successful attach/move, and surfaces unconfirmed delivery status. | L204-L243; L309-L315; L317-L353; L413-L423 | [RailChat.tsx](RailChat.tsx) |
| The session store it resolves the chat/terminal slots from + spawns/delivers through (`sessionRole`, `createSession`, `registerConnection`, `sendToSession`, `pasteDraftToSession`). | L112-L118; L302-L315; L340-L415; L418-L431 | [data/sessions.ts](../data/sessions.ts) |
| The harness-detection, opener, terminate, and attach clients the rail drives (`fetchHarnesses`, `openTerminalSession`, `terminateTerminalSession`, `attachSessionToLeaf`). | L252-L316; L318-L357 | [data/terminal.ts](../data/terminal.ts) |
| The durable leaf-key helpers and task tree builder used for packet lookup, heading labels, and the attach picker. | L60-L70; L102-L105; L126-L165 | [data/taskIdentity.ts](../data/taskIdentity.ts) |
| The lazy xterm terminal it mounts per pane (shared with Chats). | — | [Terminal.tsx](Terminal.tsx) |
| The composer docked below each pane that injects into that session's stdin. | — | [SessionComposer.tsx](SessionComposer.tsx) |
| The Chats page that surfaces the same leaf sessions via the shared registry + offers leaf attach. | — | [Chats.tsx](Chats.tsx) |
| The cockpit shell that toggles this in for the Event River and passes the displayed `leafKey`, `taskDocuments`, `engineProcesses`, `contextMaster`, and `selectedLifecycleId`. | L346-L356; L479-L485 | [cockpit/Cockpit.tsx](../cockpit/Cockpit.tsx) |

## Update History

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: made rail attach/move role-explicit, preserved
  pair-scoped local state, and displayed current seat identity in pane headers.

- 2026-07-02T17:04+02:00 — L9: kept the picker visible for attached chats as a move control. Successful
  moves use `applyLeafAssignment`, broadcast `"leaf"`, preserve the live terminal session, and draft the
  destination leaf's context; `leaf-taken` still avoids local mutation and context injection. Verification
  metadata pinned until closeout stamps the L9 commit.
- 2026-07-02T13:07+02:00 — Reopened L6 follow-up: changed leaf-context handoff from submit delivery to
  draft paste. `deliverLeafContext` now calls `pasteDraftToSession`, so the packet lands in the selected
  chat input without pressing Enter and the operator can add their own instruction before submitting.
  Verification metadata pinned until closeout stamps the follow-up commit.
- 2026-07-01T01:19+02:00 — L6: added bind-time leaf context handoff. `RailChat` now accepts
  `engineProcesses` beside `taskDocuments`, builds a projected leaf context packet from the selected/picked
  `leafKey`, and injects it through `deliverToSession` after start-on-leaf or a successful free-chat
  attach. Rejected attaches and free/off-leaf chat creation do not send a packet; unconfirmed delivery
  surfaces `rail-leaf-context-note`. Verification metadata pinned until closeout stamps the L6 commit.
- 2026-06-30T00:00:00+02:00 — L5 follow-up: reshaped the rail chat from a single per-leaf session into a **chat + terminal
  split**. The start affordance is now a **harness choice** (a `＋ {harness}` button per detected harness via
  `fetchHarnesses`, opening an agent chat with `createSession(…, "harness", …)`) plus a separate **＋ Terminal**
  (a `kind:"terminal"` shell); the leaf's slots resolve role-scoped via `findSessionForLeaf(leafKey, role)` /
  `sessionRole` and render as a vertical split (chat top, terminal below). Each `Pane` gained a **terminate**
  control (via `terminateTerminalSession`, broadcasting a catalog change) and a **truncating, `title`-bearing
  header** (hover reveal); hidden keep-alive layers survive leaf switches. Verification metadata pinned until
  closeout stamps the L5 commit.
- 2026-06-30T00:00:00+02:00 — L5 (Sidebar chat): created the single-instance right-rail leaf chat — resolves a leaf's
  bound running session by `leafKey`, reuses the shared `Terminal` + `SessionComposer` + connection
  registry so it surfaces the same session as the Chats page, keeps previously-surfaced sessions
  mounted-but-hidden across leaf switches, and offers "＋ Start chat for this leaf" (opening a session
  carrying the `leafKey`) when none is bound. Verification metadata pinned until closeout stamps the L5
  commit.
