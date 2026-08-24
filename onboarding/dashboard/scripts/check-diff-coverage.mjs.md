# dashboard/scripts/check-diff-coverage.mjs

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/scripts/check-diff-coverage.mjs`                 |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-24T13:51:26+02:00                                  |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb`                  |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The executable-statement scoring helpers. | `executableStatementLines`; `coveredStatementLines`; `measureDiffCoverage` | dashboard/scripts/check-diff-coverage.mjs:14-14; dashboard/scripts/check-diff-coverage.mjs:25-25; dashboard/scripts/check-diff-coverage.mjs:43-43 |
| The Dagger admission check is the first operation of the direct CLI runner, while pure scoring helpers stay importable. | `requireDaggerTestEnvironment`; `function main()`; direct-file guard | dashboard/scripts/check-diff-coverage.mjs:12-12; dashboard/scripts/check-diff-coverage.mjs:79-80; dashboard/scripts/check-diff-coverage.mjs:213-220 |
| The Python-parity base resolution remains inside the guarded runner. | "const resolveBase = () => {" | dashboard/scripts/check-diff-coverage.mjs:107-132 |
| The contract suite pins both direct-CLI refusal and pure accounting. | "the direct changed-lines CLI refuses before reading Git or coverage" | dashboard/scripts/check-diff-coverage.test.mjs:15-27 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-24T13:51:26+02:00 — 260821-DAGQC-L4: documented the direct-main-only
  Dagger guard. Pure scoring imports remain available to diagnostic Vitest; direct changed-lines
  CLI execution and its evidence remain Dagger-only. Verification and acceptance stay
  closeout-owned.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator (round 8 delta): created this sidecar
  for the executable-statement diff-coverage unit (architect ruling OPTION 1) and
  its base-resolution runner. Verification pinned to `cf5ef50` until closeout
  stamps the code commit.
