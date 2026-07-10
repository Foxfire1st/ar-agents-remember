# dashboard/src/panels/RailChat.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/RailChat.test.tsx`         |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash | `fdff55f2921d7aaa8ba240c11087d02c15a170d7`       |
| lastVerifiedCommitDate | 2026-07-10T15:53:23+02:00|
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
off-leaf chat creation and rejected attaches do not. The reopened L6 follow-up pins that handoff to the
draft-paste helper rather than the submit-and-confirm delivery helper. L9 adds coverage for moving an
already-attached chat to another leaf, including drafting the destination leaf's context after the move.

## Code Commentary

### 260707-HFX2-L17 Rail Seat Identity Proof

Rail tests select an explicit role during attach/move, assert the role-bearing request and local
assignment, and verify pane headings prefer binding identity over stale spawn provenance.

### Logic

Like the sibling `Chats.test.tsx`, the lazy `./Terminal` is mocked to a jsdom-safe stub
(`vi.mock("./Terminal")` → a `<div data-testid="term-{sessionId}">`) so opening a session never pulls
xterm (a canvas probe) into jsdom; the stub marks its `sessionId` so a test can assert which session's
terminal mounted. `pasteDraftToSession` is mocked at module load while preserving the rest of
`data/sessions`, so the suite can inspect draft packet text without requiring a live terminal connection. A
`FakeBroadcastChannel` records the catalog-change broadcasts the terminate path posts.

- **start affordances (L5 fix 2)** — one case stubs `fetch` to return three harnesses (claude + codex
  detected, pi not) and asserts (via `findByTestId`, awaiting the async `fetchHarnesses` detection) that
  `rail-start-chat-claude` / `-codex` render while `rail-start-chat-pi` does not, and `rail-open-terminal`
  is present. A second case uses a URL-aware `fetch` mock (`/api/harnesses` returns one harness, the
  opener POST returns ok), clicks `rail-start-chat-claude`, and asserts `findSessionForLeaf(LEAF_KEY,
  "chat")` resolves a `kind: "harness"`, `harness: "claude"` session — i.e. the start button spawns an
  **agent chat keyed to the leaf**, not a bare shell.
- **leaf context handoff (L6)** — `leafDoc()` now carries the projected lifecycle id, objective,
  requirements, and steps that `RailChat` serializes, while `engineProcess()` supplies worktree facts from
  the process map. Starting a harness chat on the viewed leaf asserts `pasteDraftToSession("chat-id",
  packet)` and checks the packet for task title, leaf key, lifecycle, code worktree, and a top-level step. The
  off-leaf create-from-anywhere case asserts no delivery. The attach-picker success case binds a free chat,
  then asserts delivery and the memory worktree line; the `409 leaf-taken` case asserts no delivery after a
  rejected bind. L9 adds a second leaf fixture, keeps the attach picker visible for an already-bound chat,
  moves it on a stubbed `200`, and asserts the drafted packet names the destination leaf. A final case makes
  `pasteDraftToSession` return `"unconfirmed"` and expects
  `rail-leaf-context-note`.
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
`count`), clears mocks (including `pasteDraftToSession`), and resets the test `FakeBroadcastChannel`.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The suite mocks `pasteDraftToSession`, supplies projected task/process fixtures, and verifies start-on-leaf, free-chat attach, attached-chat move, rejected attach, and unconfirmed delivery behavior. | L10-L13; L17-L67; L95-L105; L153-L181; L202-L256; L258-L304 | [RailChat.test.tsx](RailChat.test.tsx) |
| The right-rail chat under test builds and pastes the context package at leaf bind/move time. | L204-L243; L309-L315; L317-L353 | [RailChat.tsx](RailChat.tsx) |
| The session store it resolves leaves through and the draft-paste helper being mocked. | L329-L342; L433-L443 | [data/sessions.ts](../data/sessions.ts) |
| The attach client path whose 200/409 outcomes the tests mock. | L329-L357 | [data/terminal.ts](../data/terminal.ts) |

## Update History

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
