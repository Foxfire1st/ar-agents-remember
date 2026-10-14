# dashboard/e2e/cockpit.spec.ts

## Current A10 retained-source account

The retained Playwright source checks attention queue ranking/empty views, task-rail grouping and cross-origin Role chats clipboard policy. The old PTY/stage/inspector/set/composer contract and removed chats-E2E sibling supplies no current proof. Fixture gallery and mocked route assertions are not a fresh run or native-host acceptance.

- The retained Playwright source checks attention queue ranking/empty views, task-rail grouping and cross-origin Role chats clipboard policy. The old PTY/stage/inspector/set/composer contract and removed chats-E2E sibling supplies no current proof. Fixture gallery and mocked route assertions are not a fresh run or native-host acceptance. [3]



## Governing Overview

[agents-remember root overview](../../overview.md)

This suite is governed by the root overview; removed chats/production suites are not current proof consumers.

## Historical pre-retirement source account — not current proof

## Purpose

The primary Playwright end-to-end suite for the cockpit, wired into CI by
260731-EFA-L8 (R8). It serves the leaf worktree through Playwright's own dev server
(`reuseExistingServer` handling), drives the fixture gallery scenarios, and asserts
the real DOM contract: rail → stage → inspector order, stage-header and inspector-handle focus
adjacency, `pty-layer-*` surfaces, header state, queued-set chips and inspector evidence, end-confirm
geometry, sprint bulk confirm/cancel, and terminal continuity (same host/viewport/instance,
retained pre-cleanup rows, typing pulls the viewport to the live bottom).

## Code Commentary

### Logic

The suite is the primary Playwright acceptance surface. Static source inspection finds 25 literal test declarations and 28 registrations after the two width loops expand; this is not executed Playwright collection or a passing run. Its current focus assertions follow
the base rail → stage → inspector DOM order: traversal from the stage-header toggle remains in the
stage, while the inspector handle owns adjacency to inspector content. Landed transcripts are
asserted through their exact hidden/visible `pty-layer-*` identity. After removal of the StatusLine,
the suite proves queued settings through the queued chip, effective state through the header, and
the recorded set ledger through the opened inspector rather than retaining dead selectors. The
terminal-continuity test asserts the stable DOM contract instead of a parallel-load-sensitive scroll
position.

The attention cases explicitly open attention-bell before reading the queue layer. Empty reads nothing waiting/no item; Escape closes the modal before querying Detail. These three edited browser tests have same-gallery/test-id unit mirrors in Cockpit.test.tsx, not a Playwright execution claim.

### Conventions

Specs assert the shipped DOM contract with stable selectors; never the first-render
ideal that predates the DOM.

### Invariants And Boundaries

The suite runs against the dev server in worktrees; `npm run e2e:production` reads a
packaged fingerprint that worktrees do not carry (pre-existing packaging-owned gap,
recorded in the L8 reviewer verdict as D-3).

### Todos

Optional hardening (a later leaf): generate the dashboard fingerprint in worktrees
or make the production spec skip explicitly when the artifact is absent.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References


- The primary cockpit e2e source; the earlier 202-expectations fix-round caption is historical, not a current reached-assertion count. [1]

- The dev fixture gallery and scenarios the suite drives. [2]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
