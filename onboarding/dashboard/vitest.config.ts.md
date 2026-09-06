# dashboard/vitest.config.ts

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/vitest.config.ts`                                |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated | 2026-09-06T21:51:32+00:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb`                  |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview      | `../overview.md`                                            |

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

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

The exact source declarations below establish the current behavior; this inventory is not execution evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| Separate diagnostic Vitest configuration | `defineConfig` | dashboard/vitest.config.ts:4-12 |
| Browser-build alias preserves layout effects | `alias` | dashboard/vitest.config.ts:13-25 |
| Worker cap, setup, coverage scope and diagnostic reporters | `test` | dashboard/vitest.config.ts:27-47 |
| Source/script unit tests, excluding Playwright collection | `include` | dashboard/vitest.config.ts:49-52 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-09-06T21:51:32+00:00 — Reconciled the retained IAS implementation and diagnostic testing policy with current source citations; prior verification provenance is retained and no new test or review result is claimed.

- 2026-08-24T13:51:26+02:00 — 260821-DAGQC-L4: recorded the deliberate direct-targeted
  Vitest diagnostic route and its strict non-certifying boundary. Dagger acceptance remains
  pending and closeout-owned; verification metadata stays pinned.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator (round 8 delta): created this sidecar
  for the dashboard rail's Vitest config, including the round-8
  `scripts/**/*.test.mjs` include. Verification pinned to `cf5ef50` until closeout
  stamps the code commit.
