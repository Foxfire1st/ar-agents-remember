# dashboard/e2e/cockpit.spec.ts

## Governing Overview

[agents-remember root overview](../../overview.md)

There is no route-local overview for `dashboard/e2e/`, so the repository root
overview is the nearest governing ancestor (same resolution as the
`dashboard/e2e-production/` sidecar). The sibling suite
[dashboard/e2e-chats overview](../e2e-chats/overview.md) drives the real composed
app against real installed harnesses; this suite is the primary Playwright suite for
the cockpit against the dev server and `/dev/bench` fixture gallery.

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

The suite is the 27-test primary Playwright acceptance surface. Its current focus assertions follow
the base rail → stage → inspector DOM order: traversal from the stage-header toggle remains in the
stage, while the inspector handle owns adjacency to inspector content. Landed transcripts are
asserted through their exact hidden/visible `pty-layer-*` identity. After removal of the StatusLine,
the suite proves queued settings through the queued chip, effective state through the header, and
the recorded set ledger through the opened inspector rather than retaining dead selectors. The
terminal-continuity test asserts the stable DOM contract instead of a parallel-load-sensitive scroll
position.

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

- The primary cockpit e2e suite (202 expectations at fix-round verify). [1]
- The dev fixture gallery and scenarios the suite drives. [2]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
