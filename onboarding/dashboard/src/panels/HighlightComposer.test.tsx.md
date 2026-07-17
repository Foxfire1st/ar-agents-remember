# dashboard/src/panels/HighlightComposer.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/HighlightComposer.test.tsx`|
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `f8196d98982f834d68152d307ff8025ea69440d5`       |
| lastVerifiedCommitDate | 2026-07-17T22:08:10+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels overview](overview.md)

## Purpose

Behavior tests for the slice-6f-1 highlight composer: a selection raises the **Add to chat** pill (not
the box); clicking it opens the composer; then the target rule — open chats + a create option per detected
harness; Enter sends to the default (an open chat, or the first detected harness — not a shell). Task 11
adds selected-lifecycle target filtering/tagging coverage. L8 (as corrected by L8-r1) covers the direct
leaf-chat branch as a pill-click behavior: the pill stays visible and nothing pastes on selection alone;
clicking it draft-pastes into the matching leaf session without showing the generic picker, an
unconfirmed direct paste opens the composer, and off-leaf selections still fall back to the picker.

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
L8 cases mock `pasteDraftToSession`, hydrate a leaf-keyed session, and assert that matching
`selection.leafKey` + `viewedLeafKey` + `leafChatActive` bypasses `deliverToSession`, hides
`highlight-add-to-chat`, draft-pastes the context block, and clears only after confirmation. A paired
mismatch case proves the generic composer remains available when selected text belongs to another leaf.
The package arg is asserted via `stringContaining` the selection text.

### Conventions

`@testing-library/react` `render` + `fireEvent` (the repo idiom); the React Aria `Popover` portals the
dialog to `document.body`, found via `findByTestId`. Plain vitest assertions (no jest-dom). The store
is reset in `beforeEach`/`afterEach`.

### Invariants And Boundaries

Logic + render only — no real selection, no xterm, no backend (the session effects are spies). The
pure selection rules live in `data/selection.test.ts`.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The composer under test. | — | [HighlightComposer.tsx](HighlightComposer.tsx) |
| The mocked inject seam, draft-paste seam, and create helper. | — | [data/sessions.ts](../data/sessions.ts) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Reliable Submit Delta

The suite now covers existing-session and create-then-ready reliable highlight submission, stable
request correlation, ambiguous endgame copy, and the absence of PTY paste fallback. It verifies that
highlight provenance never clears or restores the operator's composer draft.

## Update History

- 2026-07-17T21:39+02:00 — FEUI-L5: added reliable highlight delivery, readiness, endgame, and
  non-composer draft-provenance regression coverage.

- 2026-07-02T20:55+02:00 — L8-r1 correction: the direct-branch cases now pin click semantics — the pill
  renders and nothing pastes on selection alone; the pill click draft-pastes without the
  selector/composer stage and dismisses only after a confirmed paste; a new case pins that an
  unconfirmed direct paste opens the generic composer. Verification metadata pinned until closeout
  stamps the L8-r1 commit.
- 2026-07-02T16:18+02:00 — L8: mocked `pasteDraftToSession` and added direct leaf-chat coverage for
  matching `selection.leafKey`/`viewedLeafKey` with an active rail chat, plus a mismatch case that keeps
  the generic Add-to-chat fallback. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-06-27T03:04+02:00 — No content impact: updated the store reset shape after Task 22 removed the
  hidden-label reservation state; HighlightComposer behavior and assertions are unchanged.
- 2026-06-27T01:03+02:00 — Task 22 label allocator follow-up: no behavior change to HighlightComposer
  coverage; store resets now include reserved labels so hidden-session label state cannot leak between
  cases.
- 2026-06-23T13:45+02:00 — Task 11: added coverage for `selectedLifecycleId` — create targets tag the
  new session and open-chat targets filter to matching lifecycle sessions. Verification metadata pinned
  until closeout stamps the task-11 code commit.
- 2026-06-19T15:59 — Created for task 6 slice 6f-1: covers the composer's raise-on-selection + the single/none/selector/＋new session-target behavior (selection + session helpers mocked). Verification metadata pinned until closeout stamps the 6f-1 code commit.
