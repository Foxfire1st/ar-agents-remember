# dashboard/scripts/check-diff-coverage.test.mjs

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/scripts/check-diff-coverage.test.mjs`            |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `cf5ef507f2542d6cd2f9d37a6b72148d3b91b340`                  |
| lastVerifiedCommitDate | 2026-08-06T13:55:47+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[dashboard/scripts overview](overview.md)

## Purpose

The contract suite for the executable-statement diff-coverage accounting, added by
the round-8 metric fix. It pins what v8 records as an executable changed line, what
counts as covered, the exclusion set, and `dashboard/` key normalization.

## Code Commentary

### Logic

Five tests drive the pure helpers with synthetic v8 entries: statement-range
spanning, executed-only spanning, denominator semantics (a changed line with no
statement contributes nothing), no-entry files, and the test/dev/types exclusions
with `dashboard/`-prefixed key normalization.

### Conventions

Vitest collects `scripts/**/*.test.mjs` via `dashboard/vitest.config.ts`; the suite
is logic-only (no DOM).

### Invariants And Boundaries

The suite must stay aligned with the Python gate's accounting intent: a changed
comment/blank/continuation line is never in the denominator.

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
| The executable-statement semantics suite. | "describe(\"check-diff-coverage executable-statement semantics\", () => {" | dashboard/scripts/check-diff-coverage.test.mjs:12-12 |
| The helpers under test. | `executableStatementLines`; `measureDiffCoverage` | dashboard/scripts/check-diff-coverage.mjs:14-14; dashboard/scripts/check-diff-coverage.mjs:43-43 |
| The Vitest include that runs this file. | "include: [\"src/**/*.{ts,tsx}\"],"; "setupFiles: [\"./src/test/setup.ts\"]," | dashboard/vitest.config.ts:58-58; dashboard/vitest.config.ts:35-35; dashboard/vitest.config.ts:32-32 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator (round 8 delta): created this sidecar
  for the new contract test. Verification pinned to the leaf base until closeout
  stamps the code commit (the file has no commit yet).
