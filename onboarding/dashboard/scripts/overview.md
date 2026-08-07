# dashboard/scripts/ — Dashboard Quality Scripts Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/scripts/`                             |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-08-07T08:19Z                                |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`       |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
| governingOverview      | `../../overview.md`                              |

## Governing Overview

[agents-remember root overview](../../overview.md)

## Purpose

The dashboard quality-rail scripts route, created by 260731-EFA-L8 (R7/R9). It owns
`check-diff-coverage.mjs` (the per-diff changed-lines coverage floor mirroring the
Python `diff_coverage.py` gate), its contract test
`check-diff-coverage.test.mjs`, and `check-bundle-size.mjs` (the 32 MiB bundle
budget wired into `npm run build`). Vitest collects `scripts/**/*.test.mjs` from
`dashboard/vitest.config.ts`, so this route is part of the enforced dashboard rail,
not decoration.

## Code Commentary

### Logic

`check-diff-coverage.mjs` resolves the diff base in the Python resolver's candidate
order (`AR_GATE_DIFF_BASE` → `GITHUB_BASE_REF` origin/<ref> then <ref> →
`@{upstream}` → `origin/HEAD` → `main` → empty tree), diffs changed lines, and
scores them against the v8 coverage JSON using executable-statement semantics
(round-8 architect ruling OPTION 1): the denominator counts only changed lines v8
records as executable statements; comments/blanks/continuations contribute nothing.
The contract test pins that accounting plus the test/dev/types exclusions and
`dashboard/` key normalization.

### Conventions

Scripts are standalone Node ESM with pure exported helpers and a `main()` runner;
the diff pipe uses a 256 MiB buffer so series-fork diffs cannot ENOBUFS.

### Invariants And Boundaries

The route is read-only reporting: it never writes coverage, config, or git state.
The floor defaults to 90% (`AR_DASHBOARD_DIFF_COVERAGE_FLOOR` override).

### Todos

None recorded.

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this route.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The changed-lines floor and its base resolution. | `measureDiffCoverage`; `resolveBase` | dashboard/scripts/check-diff-coverage.mjs:43-43; dashboard/scripts/check-diff-coverage.mjs:108-108 |
| The executable-statement contract suite. | "describe(\"check-diff-coverage executable-statement semantics\", () => {" | dashboard/scripts/check-diff-coverage.test.mjs:12-12 |
| The Vitest include that collects this route's tests. | "include: [\"src/**/*.{ts,tsx}\"],"; "setupFiles: [\"./src/test/setup.ts\"]," | dashboard/vitest.config.ts:58-58; dashboard/vitest.config.ts:35-35; dashboard/vitest.config.ts:32-32 |

## Cross-Repo References

No cross-repository implementation source governs this route.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator (round 8 delta): created this route
  overview for the dashboard quality scripts after the executable-statement
  diff-coverage unit and its contract test landed. Verification pinned to `cf5ef50`
  until closeout stamps the code commit.
