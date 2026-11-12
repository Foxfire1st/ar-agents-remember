# dashboard/scripts/ — Dashboard Quality Scripts Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/scripts/`                             |

## Governing Overview

[agents-remember root overview](../../overview.md)

## Purpose

`dashboard/scripts/` provides the dashboard's Dagger admission check, changed-production coverage diagnostic, build bundle budget, and dashboard-suite result writer. It contains `require-dagger-test-environment.mjs` and its type declaration and tests, `check-diff-coverage.mjs` and its contract test, `check-bundle-size.mjs`, and `write-suite-result.mjs`.

Direct targeted Vitest runs support diagnostic loops. The changed-lines CLI requires Dagger admission, and acceptance certification belongs to the pinned Dagger graph.

## Hot Path Summary

The changed-lines CLI checks Dagger admission before any Git/coverage read. The build invokes the bundle-budget checker after compilation. The successful coverage command chain invokes the suite-result writer; that record is not acceptance authority by itself.

## How It Is Built

The scripts use Node ESM. The admission validator and changed-line scorer export helpers that diagnostic tests can import; the scorer runs its Git and coverage operations only on direct CLI invocation. The bundle checker and suite-result writer execute at module top level.

`check-diff-coverage.mjs` tries diff-base candidates in the Python resolver's environment-candidate order: `AR_GATE_DIFF_BASE`, `GITHUB_BASE_REF` as `origin/<ref>` then `<ref>`, `@{upstream}`, `origin/HEAD`, and `main`. The first resolvable merge base wins; otherwise it uses Git's empty tree. Its Git subprocess buffer is 256 MiB to accommodate large series-fork diffs.

The scorer compares added or modified dashboard TypeScript lines with `coverage/coverage-final.json`. It normalizes `dashboard/` prefixes in changed-file keys and `/src/` paths in coverage keys, excludes test files and the `src/test/`, `src/dev/`, and `src/types/` routes, and counts only changed lines inside recorded statement ranges. A line is covered when it lies within a statement range with a positive execution count. Comments, blanks, or continuations outside those ranges contribute nothing; lines inside a multi-line statement range can count. Files without a coverage entry contribute no executable lines. The contract test covers CLI refusal, statement-range accounting, absent entries, exclusions, and key normalization.

`daggerTestEnvironmentError` checks a lowercase 32-hex token in `AR_DAGGER_TEST_ATTESTATION`, reads `/tmp/ar-quality/dagger-test-attestation`, and requires exact string equality. `requireDaggerTestEnvironment` throws the refusal message when validation fails; its sole argument is an optional subject label. The declaration mirrors the runtime exports. The changed-lines CLI calls this guard before reading Git or coverage.

`dashboard/vitest.config.ts` collects `scripts/**/*.test.mjs`. The package's build command runs `check-bundle-size.mjs` after code generation, type checking, and Vite build. The checker recursively totals emitted `dist` file bytes, reports the largest asset, and fails when the total exceeds the default 32 MiB budget or the value supplied through `AR_DASHBOARD_BUNDLE_BUDGET_BYTES`.

The package's `test:coverage` command runs `write-suite-result.mjs` only after Vitest exits successfully. The writer places `dashboard-suite-result.json` beside `AR_QUALITY_PROGRESS_REPORT`, or in the current directory when that variable is absent. It records the relative coverage path and, when an optional `coverage.total` object exists, rounds finite numeric percentages to three decimal places and records other percentage values as `null`. Ordinary per-file Istanbul coverage need not contain that summary object.

## Invariants And Boundaries

Changed-production coverage is diagnostic: the scorer reports covered and uncovered executable changed lines without enforcing a percentage floor. Missing, unreadable, or syntactically invalid coverage JSON fails the CLI; removing percentage enforcement does not remove execution failures or Dagger admission.

The admission validator, coverage scorer, and bundle checker read and report facts without writing coverage, configuration, or Git state. The suite-result script is the explicit report writer. It records `passed: true` from the successful command-chain assumption; direct execution does not independently establish that tests passed. Missing, unreadable, or syntactically invalid coverage leaves `totals` empty and does not suppress the result-file write.

The runtime guard reads the nonce and attestation rather than creating them. The pinned Dagger graph supplies the attempt nonce and matching attestation file. These dashboard scripts provide no runtime attestation bypass or host acceptance executor. Injectable inputs to the diagnostic validator helper support isolated tests; they do not change the CLI guard's default environment and fixed-path read.

The suite-result file is one report artifact, not independent certification or proof that every required acceptance artifact was produced. Bundle-budget enforcement and the writer's command-chain provenance remain separate from diagnostic coverage percentages.

The memory layer's `system/sources.md` has no configured Domain Documentation entries. No applicable cross-repository implementation source was identified for this route.

## Evidence

- The canonical admission validator checks token shape, fixed-path readability, and exact nonce equality; its throwing wrapper accepts only an optional diagnostic subject. The pinned Dagger graph supplies the matching attempt token and attestation file. [1]
- The declaration mirrors the validator's runtime exports and optional diagnostic subject. [2]
- The changed-line scorer is importable for diagnostic callers. It counts changed lines within recorded statement ranges, excludes the specified test/dev/types paths, normalizes dashboard keys, and ignores files without coverage entries. Its direct CLI guards admission first, resolves the base in the Python environment-candidate order, uses a 256 MiB Git buffer, reads coverage, and reports uncovered lines without a percentage floor. [3]
- The executable-statement contract suite proves both CLI refusal and pure accounting, including multi-line statement ranges, absent coverage entries, exclusions, and dashboard key normalization. [4]

- Vitest collects the route's script tests. The build chain runs the bundle checker, which fails above the default 32 MB raw-byte budget (or `AR_DASHBOARD_BUNDLE_BUDGET_BYTES`), and a successful coverage run writes `dashboard-suite-result.json` with the pass fact, the coverage path and rounded coverage totals. [5]
