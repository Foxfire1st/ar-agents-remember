# dashboard/vitest.config.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/vitest.config.ts`                                |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../../overview.md`                                         |

## Governing Overview

[agents-remember root overview](../../overview.md)

## Purpose

The standalone Vitest configuration for the dashboard (260731-EFA-L8 R7/R10). It
keeps Vite and Vitest instances separate, runs jsdom logic tests, wires the
unhandled-error trap setup, caps workers, configures v8 coverage thresholds, and
collects the dashboard quality scripts' contract tests.

## Code Commentary

### Logic

`maxWorkers: 2` keeps config-backed runs at the measured safe ceiling;
`setupFiles` installs `src/test/setup.ts` (the unhandled-error trap); the coverage
block uses v8 with `src/**/*.{ts,tsx}` include and test/dev/types exclusions and
thresholds below the measured baseline (lines 85 / statements 82 / functions 82 /
branches 70) — the strict gate is the `coverage:diff` changed-lines floor.
`include` collects `src/**/*.{test,spec}.{ts,tsx}` plus
`scripts/**/*.test.mjs` (round-8 addition so the diff-coverage contract suite runs
in CI and hooks).

### Conventions

The `react-resizable-panels` alias forces the browser development build under
Vitest so layout effects reach the panels.

### Invariants And Boundaries

Playwright specs under `e2e/` are never collected here; the coverage exclusions
must stay aligned with what `check-diff-coverage.mjs` excludes.

### Todos

None recorded.

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The coverage thresholds and provider. | "coverage: {"; "thresholds: {" | dashboard/vitest.config.ts:36-36; dashboard/vitest.config.ts:50-50 |
| The test include that now collects the scripts contract suite. | "include: [\"src/**/*.{test,spec}.{ts,tsx}\"" | dashboard/vitest.config.ts:61-61 |
| The worker ceiling and setup trap wiring. | `maxWorkers`; `setupFiles` | dashboard/vitest.config.ts:34-35 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator (round 8 delta): created this sidecar
  for the dashboard rail's Vitest config, including the round-8
  `scripts/**/*.test.mjs` include. Verification pinned to `cf5ef50` until closeout
  stamps the code commit.
