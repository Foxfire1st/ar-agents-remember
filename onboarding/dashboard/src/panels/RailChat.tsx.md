# dashboard/src/panels/RailChat.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/RailChat.tsx`              |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-18T07:22+02:00                           |
| lastVerifiedCommitHash | `e3f94568a0f5f78efc5ce7c26d94e6d103caae5f`       |
| lastVerifiedCommitDate | 2026-07-18T07:47:42+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[panels overview](overview.md)

## Purpose

The single contextual right-rail chat surface beside Operations. It is anchored on durable qualified
leaf identity and shares the same catalog, reliable composer, and connection registry as the full-page
Chats cockpit. A leaf may expose an agent chat plus optional raw terminal, with keep-alive panes and
server-first leaf attachment/context handoff. It is deliberately not another full-page destination
and does not own a second conversation/session index.

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
Since 260715-FEUI-L6 (review F6) BOTH `Terminal` mounts — the chat slot and the split terminal
`Pane` — pass ``ariaLabel={`terminal: ${session.label}`}`` so each pane's `role="group"` landmark
carries a real name in the rail surface (`Terminal.tsx` additionally guarantees a
`terminal session <sessionId>` fallback, so the landmark can never be unnamed); this is the ONLY
L6 change to this file — pane behavior, registries, and every other Terminal prop are
byte-unchanged.
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

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The rail builds the leaf context package, pastes it as draft input after start-on-leaf or successful attach/move, and surfaces unconfirmed delivery status. | L204-L243; L309-L315; L317-L353; L413-L423 | [RailChat.tsx](RailChat.tsx) |
| The session store it resolves the chat/terminal slots from + spawns/delivers through (`sessionRole`, `createSession`, `registerConnection`, `sendToSession`, `pasteDraftToSession`). | L112-L118; L302-L315; L340-L415; L418-L431 | [data/sessions.ts](../data/sessions.ts) |
| The harness-detection, opener, terminate, and attach clients the rail drives (`fetchHarnesses`, `openTerminalSession`, `terminateTerminalSession`, `attachSessionToLeaf`). | L252-L316; L318-L357 | [data/terminal.ts](../data/terminal.ts) |
| The durable leaf-key helpers and task tree builder used for packet lookup, heading labels, and the attach picker. | L60-L70; L102-L105; L126-L165 | [data/taskIdentity.ts](../data/taskIdentity.ts) |
| The lazy xterm terminal it mounts per pane (shared with Chats). | — | [Terminal.tsx](Terminal.tsx) |
| The composer docked below each pane that injects into that session's stdin. | — | [SessionComposer.tsx](SessionComposer.tsx) |
| The canonical Chats duty bar and view surface the same registry and authoritative leaf attach. | — | [ChatContextBar.tsx](session-cockpit/ChatContextBar.tsx) · [SessionsView.tsx](session-cockpit/SessionsView.tsx) |
| The cockpit shell that toggles this in for the Event River and passes the displayed `leafKey`, `taskDocuments`, `engineProcesses`, `contextMaster`, and `selectedLifecycleId`. | L346-L356; L479-L485 | [cockpit/Cockpit.tsx](../cockpit/Cockpit.tsx) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Reliable Submit Delta

RailChat now uses the same reliable `SessionComposer` as the full Chats view. Automatic leaf-context
delivery carries `leaf-context` provenance through epoch-bound submission, so it cannot clear or
restore the visible composer draft. Neither path uses terminal paste or a native hidden queue.

## FEUI-L8 Reviewed Candidate Delta

Updates contextual-chat ownership language for the one-roof cutover: RailChat shares the canonical Chats connection/session registry and keep-alive semantics. It remains a task-side contextual surface, not a second destination.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Update History

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T21:39+02:00 — FEUI-L5: migrated rail composition and leaf-context delivery to the
  shared reliable client with source-aware draft boundaries.

- 2026-07-17T04:20+02:00 — 260715-FEUI-L6 (review finding F6, one-prop call-site change): both
  `<Terminal>` mounts (the chat slot and the split terminal `Pane`) now pass
  ``ariaLabel={`terminal: ${session.label}`}`` so the terminal's `role="group"` landmark carries
  a real name in the rail surface (Terminal.tsx also guarantees a sessionId fallback). No other
  rail behavior changed. Verification metadata pinned to the leaf base until closeout stamps the
  L6 code commit.
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
