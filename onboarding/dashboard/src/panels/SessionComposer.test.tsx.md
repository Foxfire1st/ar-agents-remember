# dashboard/src/panels/SessionComposer.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/SessionComposer.test.tsx`  |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-19T05:48                                 |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels overview](overview.md)

## Purpose

Vitest render + interaction tests for `SessionComposer` (slice 6e-3). The composer is pure +
presentational (React Aria, no backend/xterm), so the tests drive it directly.

## Code Commentary

### Logic

Three cases via `fireEvent` on the `<textarea>`: (1) typing + `Send` reports the **trimmed** draft and
clears the field; (2) ⌘/Ctrl+Enter sends; (3) an empty / whitespace-only draft never sends (the Send
button is disabled and the keystroke no-ops). `fireEvent.change` / `fireEvent.keyDown` is the repo idiom
for driving React Aria interaction.

### Invariants And Boundaries

Render + interaction only; no backend, no WebSocket, no xterm. Asserts the reported value + the cleared
field, not the stdin write (that wiring lives in `Chats`).

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The component under test. | — | [SessionComposer.tsx](SessionComposer.tsx) |

## Update History

- 2026-06-19T05:48 — Created for task 6 slice 6e-3: render + interaction tests for the context composer (trimmed send + clear; ⌘/Ctrl+Enter; empty no-op). Verification metadata pinned until closeout stamps the 6e-3 code commit.
