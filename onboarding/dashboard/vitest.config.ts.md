# dashboard/vitest.config.ts

## Governing Overview

[agents-remember root overview](../overview.md)

## Purpose

The standalone Vitest configuration for the dashboard. It keeps Vite and Vitest
instances separate, runs jsdom logic tests, wires the unhandled-error trap setup,
caps workers, configures diagnostic v8 coverage, and collects the dashboard quality
scripts' contract tests. Direct targeted unit/component runs are supported as fast
diagnostics; only the pinned Dagger graph can certify acceptance.

## Code Commentary

### Logic

`maxWorkers: 2` keeps config-backed runs at the measured safe ceiling;
`setupFiles` installs `src/test/setup.ts` (the unhandled-error trap); the coverage
block uses v8 with `src/**/*.{ts,tsx}` include and test/dev/types exclusions and
text/JSON/HTML reporters without thresholds. Both aggregate and changed-line coverage are
diagnostic; metric percentages cannot block delivery.
`include` collects `src/**/*.{test,spec}.{ts,tsx}` plus
`scripts/**/*.test.mjs` (round-8 addition so the diff-coverage contract suite runs
in CI and hooks).

### Conventions

The `react-resizable-panels` alias forces the browser development build under
Vitest so layout effects reach the panels.

### Invariants And Boundaries

Playwright specs under `e2e/` are never collected here; the coverage exclusions
must stay aligned with what `check-diff-coverage.mjs` excludes.

The Vitest configuration itself carries no Dagger admission guard. This is intentional:
targeted direct Vitest is non-certifying diagnostic evidence. Playwright acceptance, the
changed-lines CLI, the direct Python certification wrapper, and broad acceptance remain behind
the nonce-attested Dagger boundary. A direct Vitest pass must never be recorded as
acceptance, changed-lines coverage, or lifecycle evidence.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

The exact source declarations below establish the current behavior; this inventory is not execution evidence.

- Separate diagnostic Vitest configuration [1]
- Browser-build alias preserves layout effects [2]
- Worker cap, setup, coverage scope and diagnostic reporters [3]
- Source/script unit tests, excluding Playwright collection [4]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.


### Clock And Settlement Evidence

- The configuration owns the shared `testTimeout` and `hookTimeout`, both 120,000 ms. They bound hung tests and hooks rather than asserting machine speed; the separate Testing Library condition guard is set by the shared setup. [5]
