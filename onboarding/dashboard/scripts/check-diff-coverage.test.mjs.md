# dashboard/scripts/check-diff-coverage.test.mjs

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/scripts/check-diff-coverage.test.mjs`            |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-24T13:51:26+02:00                                  |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb`                  |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[dashboard/scripts overview](overview.md)

## Purpose

The contract suite for the executable-statement diff-coverage accounting, added by
the round-8 metric fix. It pins what v8 records as an executable changed line, what
counts as covered, the exclusion set, and `dashboard/` key normalization.

## Code Commentary

### Logic

One subprocess test removes the Dagger attestation and proves the direct changed-lines
CLI refuses before it reads Git or coverage. Five further tests drive the pure helpers
with synthetic v8 entries: statement-range spanning, executed-only spanning,
denominator semantics (a changed line with no statement contributes nothing), no-entry
files, and the test/dev/types exclusions with `dashboard/`-prefixed key normalization.

### Conventions

Vitest collects `scripts/**/*.test.mjs` via `dashboard/vitest.config.ts`; the suite
is logic-only (no DOM).

### Invariants And Boundaries

The suite must stay aligned with the Python gate's accounting intent: a changed
comment/blank/continuation line is never in the denominator. Running these pure
Vitest assertions directly is diagnostic only; it does not turn the refused CLI into
a host acceptance or changed-lines evidence path.

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
| The direct CLI refusal occurs before base-resolution output. | "the direct changed-lines CLI refuses before reading Git or coverage" | dashboard/scripts/check-diff-coverage.test.mjs:15-27 |
| The pure executable-statement helpers remain directly importable and tested. | `executableStatementLines`; `measureDiffCoverage` | dashboard/scripts/check-diff-coverage.test.mjs:29-110; dashboard/scripts/check-diff-coverage.mjs:14-76 |
| The Vitest setup and include list collect this logic-only suite. | `setupFiles`; `scripts/**/*.test.mjs` | dashboard/vitest.config.ts:27-33; dashboard/vitest.config.ts:57-59 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-24T13:51:26+02:00 — 260821-DAGQC-L4: recorded the split contract:
  direct targeted Vitest may run the pure diagnostic suite, while direct changed-lines CLI
  execution refuses before Git/coverage work. Dagger acceptance remains pending.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator (round 8 delta): created this sidecar
  for the new contract test. Verification pinned to the leaf base until closeout
  stamps the code commit (the file has no commit yet).
