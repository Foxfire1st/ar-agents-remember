# dashboard/src/data/sessions.test.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/data/sessions.test.ts`            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-27T03:04+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                                 |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Unit tests for the `sessions` store (slice 6e-4): they pin the registry contract the Chats view
depends on — `add` labels by lowest available per-prefix ordinal and activates, `close` forgets and
clears the active pointer only when the closed id was active, `setActive` repoints.
Task 11 adds lifecycle identity tests for attach, clear, uniqueness, and lookup by lifecycle id. Task 22
adds catalog-hydration tests for server-owned sessions, live-only lifecycle routing, status-driven
focus changes, API-row conversion, and `createSession` sending label/lifecycle metadata to the opener.
It also covers the tab-sync helpers that broadcast id-bearing catalog invalidations after persisted
backend changes.

## Code Commentary

### Logic

Drives `sessionStore.getState()` directly (no React): asserts `add(prefix, id)` appends
`{id, label: "${prefix} ${n}"}` using the lowest available live ordinal for that prefix, and sets
`activeId`; that `close` removes the session and nulls `activeId` only when the closed id was active;
and that `setActive` repoints. Task 11 cases assert `add(prefix, id, lifecycleId)`, `setLifecycle`,
clearing, duplicate lifecycle ownership, and `findSessionForLifecycle`. Resets the store between cases.
Task 22 cases assert `hydrate` preserves a preferred live active id
and updates `count`, exited rows do not resolve through `findSessionForLifecycle`, `setStatus` moves
focus away from an exited active session, terminated rows release their chat labels after local removal,
`fromTerminalSessionInfo` maps API rows to store rows, and `createSession` POSTs the generated
label/lifecycle before registering a running
session. The catalog-sync suite stubs `BroadcastChannel` with `FakeBroadcastChannel`, asserts subscribers
receive another tab's `"terminate"` event with its `sessionId` while ignoring this tab's own `"create"`
broadcast, and asserts `createSession` broadcasts `"create"` with the generated id only when
`openTerminalSession` reports backend persistence. A
second suite
(slice 6f) covers the **connection
registry + delivery**: with a controllable fake `TerminalConnection`, `sendToSession` queues into
`pending` and flushes in order on `registerConnection`; `deliverToSession` waits for a late
registration (the create-then-send race), then injects exactly ONE
`bracketedPaste(sanitizeForInjection(text))` (sanitized AND wrapped) and resolves `"delivered"` once
the fake's output clock advances past the post-CR-echo baseline; and a never-registering session
resolves `"unconfirmed"` (never hangs) after the connection timeout (driven with fake timers).

### Conventions

Vanilla-store testing — exercise `getState()` actions and assert the next state, no renderer.

### Invariants And Boundaries

Pure state tests; no DOM, no real backend. `BroadcastChannel` and `fetch` are stubbed when catalog-sync
or opener behavior is under test. The terminal-persistence behavior (mounted-but-hidden layers) is
covered in `panels/Chats.test.tsx`, not here.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The store under test. | — | [data/sessions.ts](sessions.ts) |
| The view-level persistence test (mounted-but-hidden terminals). | — | [panels/Chats.test.tsx](../panels/Chats.test.tsx) |

## Update History

- 2026-06-27T03:04+02:00 — Task 22 follow-up: removed hidden-live reservation coverage with the Hide
  state, and updated catalog-sync assertions to require `sessionId` on create/terminate broadcasts.
- 2026-06-27T01:25+02:00 — Task 22 follow-up: added `BroadcastChannel` fake coverage for catalog-change
  subscription/broadcast behavior and for `createSession` broadcasting `"create"` only after the backend
  opener succeeds. Verification metadata pinned until closeout stamps the task-22 follow-up code commit.
- 2026-06-27T01:03+02:00 — Task 22 follow-up: changed session-label tests from monotonic/global ordinal
  coverage to per-prefix lowest-available allocation, including terminated rows releasing labels and
  hidden live rows reserving labels until hydration.
- 2026-06-26T23:05+02:00 — Task 22: added catalog hydration, live-only lifecycle lookup, status focus
  handoff, API-row conversion, and createSession opener-metadata coverage. Verification metadata pinned
  until closeout stamps the task-22 code commit.
- 2026-06-23T13:45+02:00 — Task 11: added lifecycle identity tests for route lookup, one owning session
  per lifecycle, and explicit tag clearing. Verification metadata pinned until closeout stamps the
  task-11 code commit.
- 2026-06-19T20:30 — Task 6 slice 6f: added the connection-registry + `deliverToSession` suite (a fake `TerminalConnection`: `sendToSession` pending-queue flush on register, the create-then-send race resolving once registered with one sanitized+wrapped paste injected, and the bounded-wait timeout resolving `"unconfirmed"` instead of hanging). Verification metadata pinned until closeout stamps the 6f code commit.
- 2026-06-19T14:05 — Created for task 6 slice 6e-4: unit tests for the new session store (add/close/setActive + ordinal stability). Verification metadata pinned until closeout stamps the 6e-4 code commit.
