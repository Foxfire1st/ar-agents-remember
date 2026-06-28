# dashboard/src/panels/SessionComposer.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/SessionComposer.tsx`       |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-19T05:48                                 |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels overview](overview.md)

## Purpose

The **context composer** (slice 6e-3): a docked input that injects a block of text into the **active**
session's stdin — "send to session" / "pass any amount of context into the chat", the on-ramp to 6f
(highlight→feedback). Presentational + controlled — it owns only the draft text and reports `onSend`;
`Chats` wires that to the active `TerminalConnection` and wraps it as a bracketed paste.

## Code Commentary

### Logic

A React Aria `TextField` (`value`/`onChange`) wrapping a `TextArea` + a `Button`. `submit()` trims the
draft, no-ops when empty, calls `onSend(value)`, and clears. Send fires on the `Button` `onPress` **or**
⌘/Ctrl+Enter (a `TextArea` `onKeyDown`; plain Enter stays a newline). The `Button` is `isDisabled` while
the trimmed draft is empty.

### Conventions

React Aria primitives (coding-guidelines: don't hand-roll interactive widgets); Panda `css()` keyed on
`_focusVisible` / `_disabled`. The Send button reuses ＋ Terminal's golden look; the textarea
`color: inherit`s the cockpit fg (form controls don't inherit colour by default).

### Invariants And Boundaries

Presentational + controlled: no backend, no WebSocket, no xterm — so it is unit-tested directly
(`SessionComposer.test.tsx`). It only *reports* the draft; `Chats` owns the bracketed-paste wrap, the
write to the active session's stdin, and the **no-auto-submit** decision (injected text lands as a
paste; the operator submits in the terminal).

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The view that mounts this + wires `onSend` to the active session's stdin. | — | [Chats.tsx](Chats.tsx) |
| The connection whose `sendInput` receives the bracketed-paste injection (+ the `bracketedPaste` helper). | — | [data/terminal.ts](../data/terminal.ts) |
| The render + interaction tests for this composer. | — | [SessionComposer.test.tsx](SessionComposer.test.tsx) |

## Update History

- 2026-06-19T05:48 — Created for task 6 slice 6e-3: the context composer (React Aria `TextField`/`TextArea` + `Button`) that reports a draft for `Chats` to inject into the active session's stdin as a bracketed paste (no auto-submit). Verification metadata pinned until closeout stamps the 6e-3 code commit.
