# dashboard/src/panels/HighlightComposer.test.tsx

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

### Pre-Projection Snapshot Regression

The first case explicitly clears dashboard analytics before rendering the composer and spies on
`console.error`. It proves the selection pill still renders while React does not emit its
"getSnapshot should be cached" warning. This pins the module-level stable empty task-document
fallback that production needs before the first dashboard projection arrives.

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
endgame states preserve prior route, selection, and operator draft. The pre-projection case sets
`analytics: null` and asserts the selector does not produce React's uncached-snapshot diagnostic.

### Conventions

`@testing-library/react` `render` + `fireEvent` (the repo idiom); the React Aria `Popover` portals the
dialog to `document.body`, found via `findByTestId`. Plain vitest assertions (no jest-dom). The store
is reset in `beforeEach`/`afterEach`.

### Invariants And Boundaries

Logic + render only — no real selection, no xterm, no backend (the session effects are spies). The
pure selection rules live in `data/selection.test.ts`.

### Todos

No task-independent technical debt was identified during MX-FIX-2 review.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

No configured live domain-documentation source was available.

### Repo-Internal References

- The composer under test. [1]
- The accepted-row create helper and routed session store. [2]
- The mocked reliable readiness, submission, retry, and reconcile seam. [3]
- The stable-snapshot regression clears analytics, renders the composer, and refuses React's uncached-snapshot warning. [4]

### Cross-Repo References

No meaningful cross-repo references found.

This file implements a repository-local contract.

## 260715-FEUI-L5 Reliable Submit Delta

The suite now covers existing-session and create-then-ready reliable highlight submission, stable
request correlation, ambiguous endgame copy, and the absence of PTY paste fallback. It verifies that
highlight provenance never clears or restores the operator's composer draft.

## FEUI-L8 Reviewed Candidate Delta

Pins commit-point routing: accepted/queued existing and new targets invoke `onSent(id)` and become active; rejected, blocked, route-error, and unresolved endgame outcomes preserve prior route, focus, view, draft, and selection.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.
