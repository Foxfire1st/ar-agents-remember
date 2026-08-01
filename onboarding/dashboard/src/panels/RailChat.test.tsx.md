# dashboard/src/panels/RailChat.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/RailChat.test.tsx`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-01T11:34+02:00 |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51`       |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `overview.md`                                    |

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
- **leaf context handoff (L6)** — `leafDoc()` carries the projected lifecycle id, objective,
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

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The suite mocks readiness/submission, supplies projected task/process fixtures, and verifies start-on-leaf, free-chat attach, attached-chat move, rejected attach, and non-accepted outcome behavior. | L14-L103; L147-L448 | [RailChat.test.tsx](RailChat.test.tsx) |
| `leafDoc`/`secondLeafDoc`/`leafProcess` — the mirror-typed fixtures (`taskDoc(...)` / `engineProcess(...)`, no casts), overriding only the fields the packet reads. | L28-L80 | [RailChat.test.tsx](RailChat.test.tsx) |
| `taskDoc` / `engineProcess` — the shared builders the local fixtures wrap. | L278-L290 | [test/fixtures/wire.ts](../test/fixtures/wire.ts) |
| `findLeafProcess`/`buildLeafContextPackage` — the only consumers of the process fixture; they read `worktreeGroup`, `codeWorktree.path`, `memoryWorktree?.path`, and match on `lifecycleId`/`leafId`. | L191-L245 | [RailChat.tsx](RailChat.tsx) |
| `RailChatImpl` builds and reliably submits the context package at leaf bind/move time. | L245-L330 | [RailChat.tsx](RailChat.tsx) |
| `sessionStore` / `findSessionForLeaf` — the accepted-row session store the rail resolves leaves through. | L271-L300; L477-L500 | [data/sessions.ts](../data/sessions.ts) |
| `submitSessionText` / `waitForSubmissionReady` — the reliable readiness/submission seam mocked by the suite. | L627-L660; L760-L784 | [data/submitClient.ts](../data/submitClient.ts) |
| `attachSessionToLeaf` — the attach client path whose 200/409 (`leaf-taken`) outcomes the tests mock. | L439-L470 | [data/terminal.ts](../data/terminal.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Reliable Submit Delta

RailChat tests now prove create-and-ready leaf-context submission, attach/move delivery through the
same reliable client, rejection honesty, and gate-only non-choice answers. They no longer model
bracketed paste or Enter as delivery authority.

## Update History

- 2026-08-01T11:34+02:00 — 260731-EFA-L4 curator: corrected the leaf-context bullet, which named
  `engineProcess()` as the local process fixture. That name now belongs to the shared builder imported
  from `test/fixtures/wire`; the local helper is `leafProcess()`. All three fixtures dropped their
  `as unknown as …` casts and delegate to the shared `taskDoc` / `engineProcess`, and `leafProcess()`
  shed ~18 boilerplate fields the base now supplies. Checked the thing that could have made that
  consequential — whether any dropped field is read on the packet path — and it is not:
  `findLeafProcess` matches on `lifecycleId`/`leafId` and `buildLeafContextPackage` reads only
  `worktreeGroup`, `codeWorktree.path` and `memoryWorktree?.path` (`RailChat.tsx` L191-L245), all of
  which the override still sets explicitly, so the assertions on task title / leaf key / lifecycle /
  code worktree / top-level step are untouched. Added the fixture-honesty boundary. Repaired six
  citations: the suite row L1-L30;L215-L445 → L14-L103;L147-L448, the component row L204-L243;L309-L365
  → the two named functions at L191-L245 and `RailChatImpl` L245-L330, `sessions.ts` L1-L180;L598-L621 →
  `sessionStore` L271-L300 + `findSessionForLeaf` L477-L500, `submitClient.ts` L1-L180 → L627-L660;
  L760-L784 (the old range contained neither mocked export), and `terminal.ts` L329-L357 →
  `attachSessionToLeaf` L439-L470.

- 2026-07-18T15:22+02:00 — FEUI MX-FIX-2: moved start fixtures to accepted server rows and proved
  a rejected harness creates no ghost row or context delivery while surfacing the typed error.
  Verification metadata remains pinned until closeout.

- 2026-07-17T21:39+02:00 — FEUI-L5: added reliable rail/context and sole-answer-channel coverage.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: covered role-explicit rail attachment and
  binding-first pane identity.

- 2026-07-02T17:04+02:00 — L9: added coverage that an attached chat still offers the picker as a move
  control, moves to another leaf on server `200`, and drafts the destination leaf context through
  `pasteDraftToSession`. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-02T13:07+02:00 — Reopened L6 follow-up: moved the rail-chat context handoff assertions to
  `pasteDraftToSession`. The packet content and delivery timing expectations stay the same, but the mocked
  seam now proves the rail uses draft paste rather than submit delivery. Verification metadata pinned until
  closeout stamps the follow-up commit.
- 2026-07-01T01:19+02:00 — L6: extended the rail-chat test sidecar for context handoff coverage. The suite
  now mocks `deliverToSession`, gives `leafDoc()`/`engineProcess()` enough projection data to build a packet,
  and asserts delivery on start-on-leaf and successful attach, no delivery for free/off-leaf create or
  rejected attach, and visible status on unconfirmed delivery. Verification metadata pinned until closeout
  stamps the L6 commit.
- 2026-06-30T00:00:00+02:00 — L5 follow-up: created the `RailChat.test.tsx` sidecar for the reshaped right-rail chat —
  harness-choice start (a button per detected harness + ＋ Terminal), the chat-over-terminal split when a
  leaf holds both, and role-independent terminate (ending the chat frees only the chat slot; ending the
  terminal leaves the chat alive). Verification metadata pinned until closeout stamps the L5 commit.
