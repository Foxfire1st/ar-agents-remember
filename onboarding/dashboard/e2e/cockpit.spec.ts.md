# dashboard/e2e/cockpit.spec.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/e2e/cockpit.spec.ts`                             |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-28T14:15+02:00                                      |
| lastVerifiedCommitHash | `a06d2ffcfae2c277f2ae19330c17d09c616b77e8`                  |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00                                   |
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
- 2026-08-28T14:15+02:00 — Reconciled the current 27-test cockpit contract after StatusLine
  removal: stage/inspector focus adjacency, exact landed-transcript layers, header state, queued-set
  chips, and inspector ledger evidence now replace the retired selectors. Stamped the landed PDLS
  code candidate.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the primary
  Playwright suite after the FL3 repair (27/27) and CI wiring. Verification pinned
  to the leaf base until closeout stamps the code commit.
