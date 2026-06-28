# dashboard/src/panels/HighlightComposer.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/HighlightComposer.test.tsx`|
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-06-27T03:04+02:00                           |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`       |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels overview](overview.md)

## Purpose

Behavior tests for the slice-6f-1 highlight composer: a selection raises the **Add to chat** pill (not
the box); clicking it opens the composer; then the target rule — open chats + a create option per detected
harness; Enter sends to the default (an open chat, or the first detected harness — not a shell). Task 11
adds selected-lifecycle target filtering/tagging coverage.

## Code Commentary

### Logic

`vi.mock("../data/selection")` feeds a fixed `useSelectionCapture` (`{ selection, clear }`, or `null`);
`vi.mock("../data/sessions")` keeps the real `sessionStore`/`useSessions` but spies
`createSession`/`deliverToSession`; `vi.mock("../data/terminal")` stubs `fetchHarnesses` (claude+codex
detected, pi not). Seeds the store per case, renders `<HighlightComposer>`, and asserts: nothing renders
without a selection; a selection raises the **Add to chat** pill, then clicking it opens the composer;
the target control offers a create option per *detected* harness (＋ Claude Code / ＋ Codex / ＋ Terminal,
not pi); with **no** chat open Enter creates the default detected harness
(`createSession("Claude Code","harness","claude")`) and sends; picking ＋ Codex targets `codex`; with a
chat open Enter sends to it (and `setActive`s + `clear`s). Task 11 cases assert that a create target
receives the selected lifecycle id and that open-chat targets are filtered to the selected lifecycle.
The package arg is asserted via `stringContaining` the selection text.

### Conventions

`@testing-library/react` `render` + `fireEvent` (the repo idiom); the React Aria `Popover` portals the
dialog to `document.body`, found via `findByTestId`. Plain vitest assertions (no jest-dom). The store
is reset in `beforeEach`/`afterEach`.

### Invariants And Boundaries

Logic + render only — no real selection, no xterm, no backend (the session effects are spies). The
pure selection rules live in `data/selection.test.ts`.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The composer under test. | — | [HighlightComposer.tsx](HighlightComposer.tsx) |
| The mocked inject seam + create helper. | — | [data/sessions.ts](../data/sessions.ts) |

## Update History

- 2026-06-27T03:04+02:00 — No content impact: updated the store reset shape after Task 22 removed the
  hidden-label reservation state; HighlightComposer behavior and assertions are unchanged.
- 2026-06-27T01:03+02:00 — Task 22 label allocator follow-up: no behavior change to HighlightComposer
  coverage; store resets now include reserved labels so hidden-session label state cannot leak between
  cases.
- 2026-06-23T13:45+02:00 — Task 11: added coverage for `selectedLifecycleId` — create targets tag the
  new session and open-chat targets filter to matching lifecycle sessions. Verification metadata pinned
  until closeout stamps the task-11 code commit.
- 2026-06-19T15:59 — Created for task 6 slice 6f-1: covers the composer's raise-on-selection + the single/none/selector/＋new session-target behavior (selection + session helpers mocked). Verification metadata pinned until closeout stamps the 6f-1 code commit.
