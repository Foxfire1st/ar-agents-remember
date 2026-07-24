# dashboard/src/cockpit/Cockpit.memo.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/cockpit/Cockpit.memo.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:50Z |
| lastVerifiedCommitHash |  `842b487b854503d95c9c2d9dce1841198ba93c7d`|
| lastVerifiedCommitDate |  2026-07-24T17:08:25+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Render-count regression coverage for the cockpit's persistent, hidden-not-unmounted layers.

## Code Commentary

### Logic

Memoized probes wrap real persistent panels and count parent-driven renders. The suite sweeps cockpit
views, preserves DOM identity and ARIA/display visibility, checks real prop changes still pass the memo
gate, and confirms the right-rail River/Chat switch remains interactive.

### Conventions

Mocks preserve the production export shape and use React's ordinary shallow memo comparison; store-driven
updates inside a panel are intentionally outside these parent-render counts.

### Invariants And Boundaries

The test guards tab-switch reconciliation cost without accepting unmount/remount as an optimization.

### Todos

None.

## Docs References

No Domain Documentation entries are configured in this memory worktree's source registry; no external
documentation was invented.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is configured. | Source discovery checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Probes prove memo behavior and keep-alive DOM identity. | L11-L324 | [Cockpit.memo.test.tsx](Cockpit.memo.test.tsx) |
| The production shell owns the persistent layers under test. | L263-L760 | [Cockpit.tsx](Cockpit.tsx) |

## Cross-Repo References

No meaningful cross-repository references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This is dashboard-local test coverage. | L1-L324 | [Cockpit.memo.test.tsx](Cockpit.memo.test.tsx) |

## Update History

- 2026-07-24T13:17:50Z — Created for persistent cockpit-layer memoization and keep-alive regression
  coverage. Verification hash/date remain pinned to the pre-commit source stamp.
