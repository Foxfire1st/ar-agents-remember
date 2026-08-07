# dashboard/e2e/cockpit.spec.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/e2e/cockpit.spec.ts`                             |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `cf5ef507f2542d6cd2f9d37a6b72148d3b91b340`                  |
| lastVerifiedCommitDate | 2026-08-06T13:55:47+02:00|
| governingOverview      | `../../overview.md`                                         |

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
the real DOM contract: rail → stage → inspector focus order, `pty-layer-*` surfaces,
statusline/status-state/pending-set selectors, end-confirm geometry, sprint bulk
confirm/cancel, and terminal continuity (same host/viewport/instance, retained
pre-cleanup rows, typing pulls the viewport to the live bottom).

## Code Commentary

### Logic

The suite was repaired to green 27/27 in the L8 fix round (FL3): focus expectations
use the real DOM order (the old Shift+Tab expectations contradicted the pre-existing
inspector-after-stage order); the terminal-continuity test asserts the stable DOM
contract instead of a parallel-load-sensitive scroll position. Two genuine app
defects surfaced and were fixed (Terminal headless-focus delegation; ChatsStageBody
keep-alive), and fixtures/scenarios gained `RAW_TERMINAL_ROW` and the
`terminal-focus` scenario.

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

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The primary cockpit e2e suite (202 expectations at fix-round verify). | "import { expect, test } from \"@playwright/test\";"; `import { expect, test } from ` | dashboard/e2e/cockpit.spec.ts:1-700 |
| The dev fixture gallery and scenarios the suite drives. | `cockpitScenarios` | dashboard/src/dev/scenarios.ts:214-257 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the primary
  Playwright suite after the FL3 repair (27/27) and CI wiring. Verification pinned
  to the leaf base until closeout stamps the code commit.
