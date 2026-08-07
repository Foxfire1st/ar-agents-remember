# dashboard/src/panels/HighlightComposer.test.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/HighlightComposer.test.tsx`|
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-18T15:22+02:00                           |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`       |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[panels overview](overview.md)

## Purpose

Behavior tests for the slice-6f-1 highlight composer: a selection raises the **Add to chat** pill (not
the box); clicking it opens the composer; then the target rule — open chats + a create option per detected
harness; Enter sends to the default (an open chat, or the first detected harness — not a shell). Task 11
adds selected-lifecycle target filtering/tagging coverage. L8 (as corrected by L8-r1) covers the direct
leaf-chat branch as a pill-click behavior: the pill stays visible and nothing pastes on selection alone;
clicking it reliably submits to the matching leaf session without showing the generic picker, a
non-accepted result opens/retains the composer, and off-leaf selections still fall back to the picker.

## Code Commentary

### FEUI MX-FIX-2 Failed-Create Regression

Create mocks now return an accepted server-row result rather than a bare id. The added network
failure case proves visible `session open network` copy and zero readiness or submit calls, so a
failed create cannot be treated as a deliverable target.

### Logic

`vi.mock("../data/selection")` feeds a fixed `useSelectionCapture` (`{ selection, clear }`, or `null`);
`vi.mock("../data/sessions")` keeps the real `sessionStore`/`useSessions` but spies
`createSession`; `vi.mock("../data/submitClient")` controls readiness, submit, retry, and reconcile;
`vi.mock("../data/terminal")` stubs `fetchHarnesses` (claude+codex
detected, pi not). Seeds the store per case, renders `<HighlightComposer>`, and asserts: nothing renders
without a selection; a selection raises the **Add to chat** pill, then clicking it opens the composer;
the target control offers a create option per *detected* harness (＋ Claude Code / ＋ Codex, not pi or
a raw terminal); with **no** chat open Enter creates the default detected harness, waits for submission
readiness, and submits with `source: "highlight"`; picking ＋ Codex targets `codex`; an existing chat
submits directly. Task 11 cases assert lifecycle-tagged creation and target filtering. Direct-branch
cases hydrate a leaf-keyed harness, assert the pill click calls `submitSessionText` with the context
package, and prove only accepted/queued truth clears and routes; rejected, route-error, and unresolved
endgame states preserve prior route, selection, and operator draft.

### Conventions

`@testing-library/react` `render` + `fireEvent` (the repo idiom); the React Aria `Popover` portals the
dialog to `document.body`, found via `findByTestId`. Plain vitest assertions (no jest-dom). The store
is reset in `beforeEach`/`afterEach`.

### Invariants And Boundaries

Logic + render only — no real selection, no xterm, no backend (the session effects are spies). The
pure selection rules live in `data/selection.test.ts`.

### Todos

No task-independent technical debt was identified during MX-FIX-2 review.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The composer under test. | "export const HighlightComposer = memo(HighlightComposerImpl)" | dashboard/src/panels/HighlightComposer.tsx:1178-1178 |
| The accepted-row create helper and routed session store. | "export async function createSession(" | dashboard/src/data/sessions.ts:767-767 |
| The mocked reliable readiness, submission, retry, and reconcile seam. | "export async function executeReliableSubmit(" | dashboard/src/data/submitClient.ts:567-567 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Reliable Submit Delta

The suite now covers existing-session and create-then-ready reliable highlight submission, stable
request correlation, ambiguous endgame copy, and the absence of PTY paste fallback. It verifies that
highlight provenance never clears or restores the operator's composer draft.

## FEUI-L8 Reviewed Candidate Delta

Pins commit-point routing: accepted/queued existing and new targets invoke `onSent(id)` and become active; rejected, blocked, route-error, and unresolved endgame outcomes preserve prior route, focus, view, draft, and selection.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Update History

- 2026-08-02T22:10:00+02:00 — 260731-EFA-L6 W2-B05 curator: anchored 3 citation items; scoped citation check now passes.

- 2026-07-18T15:22+02:00 — FEUI MX-FIX-2: updated create mocks to the authoritative result and
  pinned visible failed-create handling with no readiness wait or submission. Verification metadata
  remains pinned until closeout.

- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

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
