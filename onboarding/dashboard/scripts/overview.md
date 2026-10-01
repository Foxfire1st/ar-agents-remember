# dashboard/scripts/ — Dashboard Quality Scripts Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/scripts/`                             |

## Governing Overview

[agents-remember root overview](../../overview.md)

## Purpose

The dashboard quality-rail scripts route owns
`require-dagger-test-environment.mjs` (the canonical nonce/attestation validator), its
type declaration, `check-diff-coverage.mjs` (the per-diff changed-lines coverage diagnostic
mirroring the Python `diff_coverage.py` report), its contract test, and
`check-bundle-size.mjs` (the 32 MiB bundle budget wired into `npm run build`). The route also owns `write-suite-result.mjs`, which writes the CCR dashboard-suite result
after a successful coverage command. Vitest
collects `scripts/**/*.test.mjs` from `dashboard/vitest.config.ts`. Direct targeted
Vitest runs are supported diagnostic loops; the changed-lines CLI itself and all
acceptance remain Dagger-only.

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

`daggerTestEnvironmentError` validates one lowercase 32-hex token, reads the fixed
in-container attestation path, and requires an exact byte-for-byte match.
`requireDaggerTestEnvironment` turns that result into the route's fail-loud refusal and
accepts only a subject label for the message. `check-diff-coverage.mjs` calls it as the
first operation of direct `main()` while leaving exported pure scoring helpers open to
diagnostic imports.

### Conventions

Scripts are standalone Node ESM with pure exported helpers and a `main()` runner;
the diff pipe uses a 256 MiB buffer so series-fork diffs cannot ENOBUFS.

### Invariants And Boundaries

The admission, coverage-scoring, and bundle-budget scripts read and report facts without
writing coverage, configuration, or Git state. `write-suite-result.mjs` is the explicit
report writer: `test:coverage` invokes it only after Vitest exits successfully. It writes
`dashboard-suite-result.json` beside `AR_QUALITY_PROGRESS_REPORT`, or in the current directory
when that variable is absent. The script records `passed: true` from that command-chain
assumption; direct execution does not independently prove a test passed. Missing or unreadable
coverage leaves `totals` empty and does not suppress the suite-result file.
No changed-coverage percentage floor is enforced. No code here
writes a nonce, accepts a fake token, bypasses attestation, shadows configuration, or
falls back to a host acceptance executor.

`write-suite-result.mjs` records the coverage path and rounds numeric `coverage.total`
percentages when that optional object exists; ordinary per-file Istanbul coverage need
not contain that summary object. The suite-result record is one artifact, not independent
certification or proof that all required Gate-4 artifacts were produced.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this route.

No relevant domain documentation was found.

### Repo-Internal References

- The canonical admission validator checks token shape, fixed-path readability, and exact nonce equality. [1]
- The declaration mirrors the validator's runtime exports and optional diagnostic subject. [2]
- The changed-line scorer is importable for diagnostic callers. [3]
- The executable-statement contract suite proves both CLI refusal and pure accounting. [4]
- Vitest collects the route’s script tests. [5]

### Cross-Repo References

No cross-repository implementation source governs this route.

No applicable cross-repository source was found.


## Integrated IAS Recovery Contract

Changed-production coverage is diagnostic: `check-diff-coverage.mjs` reports executable changed lines and uncovered lines without a percentage floor. Its direct CLI retains genuine Dagger admission; malformed or missing coverage remains an execution failure. Bundle-size enforcement and suite-result command-chain provenance are unchanged.
