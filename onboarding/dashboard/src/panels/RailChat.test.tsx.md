# dashboard/src/panels/RailChat.test.tsx

## Governing Overview

[panels overview](overview.md)

## Purpose

Vitest + Testing Library coverage for the single-instance right-rail `RailChat` after the L5 fix pass
reshaped it. It pins the three behaviours the rewrite introduced: the **start affordance is a harness
choice** (an agent chat per detected harness — Claude Code / Codex / Pi.dev — plus a separate
**＋ Terminal**), a leaf surfaces a **chat-over-terminal vertical split** when it holds both, and each
pane has an **independent terminate** so ending the chat frees only the chat slot and ending the terminal
leaves the chat alive. The leaf binding is keyed on a constant qualified leaf id
(`agents-remember/260628_operations-integration/260628-L5`); per-(leaf, role) uniqueness itself is
covered server-side and in `data/sessions.test.ts`. L6 extends this coverage to the bind-time context
handoff: start-on-viewed-leaf and successful free-chat attach inject a leaf context package, while
off-leaf chat creation and rejected attaches do not. FEUI-L5 moves that handoff to the reliable submit
client with `leaf-context` provenance. L9 adds coverage for moving an already-attached chat to another
leaf, including submitting the destination leaf's context after the move.

## Code Commentary

### FEUI MX-FIX-2 Contextual Caller Proof

Start fixtures now return request-matched accepted harness rows. The new rejected-harness case
asserts visible failure copy, zero session rows, zero leaf-context submit, and exactly one open POST.
This pins RailChat behind the same authority gate as canonical Chats.

### 260707-HFX2-L17 Rail Seat Identity Proof

Rail tests select an explicit role during attach/move, assert the role-bearing request and local
assignment, and verify pane headings prefer binding identity over stale spawn provenance.

### Logic

Like the sibling `Chats.test.tsx`, the lazy `./Terminal` is mocked to a jsdom-safe stub
(`vi.mock("./Terminal")` → a `<div data-testid="term-{sessionId}">`) so opening a session never pulls
xterm (a canvas probe) into jsdom; the stub marks its `sessionId` so a test can assert which session's
terminal mounted. `waitForSubmissionReady` and `submitSessionText` are mocked so the suite can inspect
the reliable context packet and result grammar without a native adapter. A `FakeBroadcastChannel`
records the catalog-change broadcasts the terminate path posts.

- **start affordances (L5 fix 2)** — one case stubs `fetch` to return three harnesses (claude + codex
  detected, pi not) and asserts (via `findByTestId`, awaiting the async `fetchHarnesses` detection) that
  `rail-start-chat-claude` / `-codex` render while `rail-start-chat-pi` does not, and `rail-open-terminal`
  is present. A second case uses a URL-aware `fetch` mock (`/api/harnesses` returns one harness, the
  opener POST returns ok), clicks `rail-start-chat-claude`, and asserts `findSessionForLeaf(LEAF_KEY,
  "chat")` resolves a `kind: "harness"`, `harness: "claude"` session — i.e. the start button spawns an
  **agent chat keyed to the leaf**, not a bare shell.
- **leaf context handoff** — `leafDoc()` carries the projected lifecycle id, objective,
  requirements, and steps that `RailChat` serializes, while the process fixture supplies worktree facts
  from the process map. That process fixture is now named **`leafProcess()`**, not `engineProcess()`:
  `engineProcess` is the shared builder imported from `test/fixtures/wire`, and the local helper wraps
  it. All three fixtures (`leafDoc`, `secondLeafDoc`, `leafProcess`) dropped their
  `as unknown as …` casts and delegate to `taskDoc(...)` / `engineProcess(...)`, so they are checked
  against the mirror. `leafProcess()` also shed ~18 hand-written boilerplate fields (`phase`, `health`,
  `codeSource`, `memoryMode`, `ledgerRows`, `providers`, `edges`, `actions`, `summary`, `sourceFiles`, …)
  that the shared base now supplies; it keeps explicit overrides for exactly the fields the packet path
  reads — `worktreeGroup`, `leafId`, `lifecycleId`, `codeWorktree`, `memoryWorktree`. Starting a harness
  chat on the viewed leaf asserts readiness followed by
  `submitSessionText("chat-id", packet, {source: "leaf-context", clearDraftOnAccept: false})` and checks
  the packet for task title, leaf key, lifecycle, code worktree, and a top-level step. Off-leaf creation
  asserts no submission. Successful attach/move submits the destination packet; `409 leaf-taken` submits
  nothing. Blocked and non-accepted lifecycle records surface `rail-leaf-context-note` honestly.
- **chat + terminal split (L5 fix 2)** — `fetch` is rejected (no backend) and the `sessions` store is
  `hydrate`d directly. With a running `harness` chat **and** a running `terminal` on the same leaf, the
  render shows both `rail-pane-chat` and `rail-pane-terminal` plus both `term-*` stubs (the vertical
  split). With only a chat, `rail-pane-chat` renders, `rail-open-terminal` is offered beside it, and
  `rail-pane-terminal` is absent.
- **terminate (L5 fix 3)** — a URL-aware `fetch` returns ok only for the relevant
  `/api/terminal/{id}/terminate`. Clicking `rail-terminate-chat` ends the chat through the backend,
  `findSessionForLeaf(LEAF_KEY, "chat")` becomes undefined, the chat pane disappears (the start
  affordance returns), and an id-bearing `terminal-catalog-changed` / `terminate` broadcast is posted.
  A paired case hydrates a chat + terminal, clicks `rail-terminate-terminal`, and asserts the terminal
  slot frees (`findSessionForLeaf(LEAF_KEY, "terminal")` undefined) while the chat pane survives —
  proving the two slots terminate independently.
- **lifecycle-free non-choice answers (260713-TES-L5F2)** — a rail-bound hosted session with no
  lifecycle id answers through `/api/terminal/{session}/interaction-response`. The case pins the
  bridge epoch and scalar response body and proves the reliable `/submit` path is not used.

### Conventions

The start-affordance cases that don't open a session never Suspense-load xterm; the cases that surface a
session rely on the `./Terminal` stub, the same posture as `Chats.test.tsx`. `afterEach` runs `cleanup` +
`vi.unstubAllGlobals`, resets the `sessions` store to its current shape (`sessions`, `activeId`,
`count`), clears reliable-submit mocks, and resets the test `FakeBroadcastChannel`.

### Invariants And Boundaries

The suite replaces xterm and adapter transport only. It still crosses the real session-store
mutation boundary, proves exact-one accepted open, and proves rejected opens never submit leaf
context.

Fixtures are mirror-typed, not cast. A `as unknown as TaskDocNode` / `as unknown as EngineProcessNode`
here would let a seed keep a shape the server can no longer send, which is precisely the failure mode
a context-packet suite cannot afford: the packet's whole claim is that it serialises PROJECTED facts.
Override only the fields the assertions read; let the shared base carry the rest, so a contract change
fails the file instead of being absorbed by a stale literal.

### Todos

No task-independent technical debt was identified during MX-FIX-2 review.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

No configured live domain-documentation source was available.

### Repo-Internal References

- The suite mocks the lazy `Terminal` module. [1]
- The rejected attach case uses the 409 outcome. [2]
- `leafDoc` is the local mirror-typed fixture entry point. [3]
- `leafProcess` explicitly supplies the packet's `worktreeGroup` fixture field. [4]
- The shared `taskDoc` builder is defined here for the local fixture wrappers. [5]
- The shared `engineProcess` builder is defined here for the local fixture wrappers. [6]
- `findLeafProcess` is the leaf-identity lookup used by context construction. [7]
- `buildLeafContextPackage` is the context-package builder. [8]
- The context package reads the process `worktreeGroup`. [9]
- The context package reads `codeWorktree.path`. [10]
- The context package reads the optional `memoryWorktree.path`. [11]
- `RailChatImpl` builds and reliably submits the context package at leaf bind/move time. [12]
- `sessionStore` is declared here. [13]
- `findSessionForTask` is the structural task-document lookup entry. [14]
- `submitSessionText` is part of the reliable submission seam mocked by the suite. [15]
- `waitForSubmissionReady` is the readiness entry. [16]
- `attachSessionToTask` is the attach client path whose 200/409 (`seat-taken`) outcomes the tests mock. [17]
- The rail's lifecycle-free answer case targets its exact session and never `/submit`. [18]

### Cross-Repo References

No meaningful cross-repo references found.

This file implements a repository-local contract.

## 260715-FEUI-L5 Reliable Submit Delta

RailChat tests now prove create-and-ready leaf-context submission, attach/move delivery through the
same reliable client, rejection honesty, and session-direct non-choice answers. They no longer model
bracketed paste, Enter, or lifecycle gates as adapter-answer authority.
