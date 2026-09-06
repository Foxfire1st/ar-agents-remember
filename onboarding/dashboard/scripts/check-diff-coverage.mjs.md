# dashboard/scripts/check-diff-coverage.mjs

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/scripts/check-diff-coverage.mjs`                 |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated | 2026-09-06T21:51:32+00:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`                  |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[dashboard/scripts overview](overview.md)

## Purpose

Reports diagnostic changed-line dashboard coverage from the existing v8 artifact. Changed executable statement lines contribute to the denominator; positive execution contributes to the numerator. Missing lines remain visible, but no mandatory percentage or 90% floor can fail delivery. The CLI retains its Dagger admission and missing/malformed artifact failures.

## Code Commentary

### Logic

The pure helpers separate the accounting from the runner:
`executableStatementLines` spans every statement range in `statementMap`;
`coveredStatementLines` spans only ranges with a positive execution count;
`measureDiffCoverage` normalizes `dashboard/` keys, drops test/dev/types files,
and tallies `{covered, total, missing}` per changed line that carries an
executable statement (round-8 ruling OPTION 1). `resolveBase` mirrors the Python
resolver order — `AR_GATE_DIFF_BASE` → `GITHUB_BASE_REF` (`origin/<ref>` then
`<ref>`) → `@{upstream}` → `origin/HEAD` → `main` → empty tree (F9 parity) — and
`main()` first invokes the canonical Dagger-environment validator, then runs the
diff with a 256 MiB pipe buffer so series-fork diffs cannot ENOBUFS. The guard is
inside `main`, not module import: Vitest can import and exercise the pure scoring
helpers directly, while invoking the changed-lines CLI remains Dagger-only.

### Conventions

Node ESM, pure exported helpers, `#!/usr/bin/env node` runner; read-only.

### Invariants And Boundaries

Only `src/` production lines count; tests, `src/test`, `src/dev`, `src/types` are
excluded. Files without a v8 entry contribute nothing. The script never modifies
coverage or git state. Direct targeted Vitest may import the pure helpers for
diagnostic unit tests, but direct CLI execution cannot score or publish changed-lines
evidence outside a matching nonce-attested Dagger run. There is no bypass, shadow
configuration, fallback executor, or compatibility reader.

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
| Executable statement-line accounting | `executableStatementLines` | dashboard/scripts/check-diff-coverage.mjs:14-22 |
| Covered statement ranges | `coveredStatementLines` | dashboard/scripts/check-diff-coverage.mjs:25-36 |
| Production filtering and changed-line tally | `measureDiffCoverage` | dashboard/scripts/check-diff-coverage.mjs:43-76 |
| Dagger admission and comparison-base selection | `main` | dashboard/scripts/check-diff-coverage.mjs:78-132 |
| Required coverage artifact and diagnostic result without a floor | `coverage` | dashboard/scripts/check-diff-coverage.mjs:172-204 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-09-06T21:51:32+00:00 — Reconciled the retained IAS implementation and diagnostic testing policy with current source citations; prior verification provenance is retained and no new test or review result is claimed.

- 2026-08-24T13:51:26+02:00 — 260821-DAGQC-L4: documented the direct-main-only
  Dagger guard. Pure scoring imports remain available to diagnostic Vitest; direct changed-lines
  CLI execution and its evidence remain Dagger-only. Verification and acceptance stay
  closeout-owned.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator (round 8 delta): created this sidecar
  for the executable-statement diff-coverage unit (architect ruling OPTION 1) and
  its base-resolution runner. Verification pinned to `cf5ef50` until closeout
  stamps the code commit.
