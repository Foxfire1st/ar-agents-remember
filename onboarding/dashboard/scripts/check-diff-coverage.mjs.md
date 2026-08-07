# dashboard/scripts/check-diff-coverage.mjs

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/scripts/check-diff-coverage.mjs`                 |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `cf5ef507f2542d6cd2f9d37a6b72148d3b91b340`                  |
| lastVerifiedCommitDate | 2026-08-06T13:55:47+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[dashboard/scripts overview](overview.md)

## Purpose

The dashboard per-diff coverage floor (260731-EFA-L8 R7), mirroring the Python
changed-lines gate. It scores every changed line the v8 report records as an
executable statement against the Vitest run and fails when the covered share is
below the floor (default 90%).

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
`main()` runs the diff with a 256 MiB pipe buffer so series-fork diffs cannot
ENOBUFS.

### Conventions

Node ESM, pure exported helpers, `#!/usr/bin/env node` runner; read-only.

### Invariants And Boundaries

Only `src/` production lines count; tests, `src/test`, `src/dev`, `src/types` are
excluded. Files without a v8 entry contribute nothing. The script never modifies
coverage or git state.

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
| The executable-statement scoring helpers. | `executableStatementLines`; `coveredStatementLines`; `measureDiffCoverage` | dashboard/scripts/check-diff-coverage.mjs:14-14; dashboard/scripts/check-diff-coverage.mjs:25-25; dashboard/scripts/check-diff-coverage.mjs:43-43 |
| The Python-parity base resolution and runner. | "const resolveBase = () => {"; "function main() {" | dashboard/scripts/check-diff-coverage.mjs:108-108; dashboard/scripts/check-diff-coverage.mjs:78-78 |
| The contract suite pinning the accounting. | "describe(\"check-diff-coverage executable-statement semantics\", () => {" | dashboard/scripts/check-diff-coverage.test.mjs:12-12 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator (round 8 delta): created this sidecar
  for the executable-statement diff-coverage unit (architect ruling OPTION 1) and
  its base-resolution runner. Verification pinned to `cf5ef50` until closeout
  stamps the code commit.
