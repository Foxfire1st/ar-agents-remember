# dashboard/src/panels/RailChat.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/RailChat.test.tsx`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-18T15:22+02:00 |
| lastVerifiedCommitHash | `31f58834f86c0d98e26b0896e099a2403a8729ee`       |
| lastVerifiedCommitDate | 2026-07-18T15:41:39+02:00|
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
- **leaf context handoff (L6)** — `leafDoc()` now carries the projected lifecycle id, objective,
  requirements, and steps that `RailChat` serializes, while `engineProcess()` supplies worktree facts from
  the process map. Starting a harness chat on the viewed leaf asserts readiness followed by
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
session rely on the `./Terminal` stub, the same posture as `Chats.test.tsx`. `afterEach` runs `cleanup`
+ `vi.unstubAllGlobals`, resets the `sessions` store to its current shape (`sessions`, `activeId`,
`count`), clears reliable-submit mocks, and resets the test `FakeBroadcastChannel`.

### Invariants And Boundaries

The suite replaces xterm and adapter transport only. It still crosses the real session-store
mutation boundary, proves exact-one accepted open, and proves rejected opens never submit leaf
context.

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
| The suite mocks readiness/submission, supplies projected task/process fixtures, and verifies start-on-leaf, free-chat attach, attached-chat move, rejected attach, and non-accepted outcome behavior. | L1-L30; L215-L445 | [RailChat.test.tsx](RailChat.test.tsx) |
| The right-rail chat under test builds and reliably submits the context package at leaf bind/move time. | L204-L243; L309-L365 | [RailChat.tsx](RailChat.tsx) |
| The accepted-row session store the rail resolves leaves through. | L1-L180; L598-L621 | [data/sessions.ts](../data/sessions.ts) |
| The reliable readiness/submission seam mocked by the suite. | L1-L180 | [data/submitClient.ts](../data/submitClient.ts) |
| The attach client path whose 200/409 outcomes the tests mock. | L329-L357 | [data/terminal.ts](../data/terminal.ts) |

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
