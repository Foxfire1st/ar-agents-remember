# dashboard/scripts/ — Dashboard Quality Scripts Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `dashboard/scripts/`                             |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-08-24T13:51:26+02:00                       |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb`       |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview      | `../../overview.md`                              |

## Governing Overview

[agents-remember root overview](../../overview.md)

## Purpose

The dashboard quality-rail scripts route owns
`require-dagger-test-environment.mjs` (the canonical nonce/attestation validator), its
type declaration, `check-diff-coverage.mjs` (the per-diff changed-lines coverage floor
mirroring the Python `diff_coverage.py` gate), its contract test, and
`check-bundle-size.mjs` (the 32 MiB bundle budget wired into `npm run build`). Vitest
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

The route is read-only reporting: it never writes coverage, config, or git state.
The floor defaults to 90% (`AR_DASHBOARD_DIFF_COVERAGE_FLOOR` override). No code here
writes a nonce, accepts a fake token, bypasses attestation, shadows configuration, or
falls back to a host acceptance executor.

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
| The canonical admission validator checks token shape, fixed-path readability, and exact nonce equality. | `daggerTestEnvironmentError`; `requireDaggerTestEnvironment` | dashboard/scripts/require-dagger-test-environment.mjs:3-34 |
| The declaration mirrors the validator's runtime exports and optional diagnostic subject. | `daggerTestEnvironmentError`; `requireDaggerTestEnvironment` | dashboard/scripts/require-dagger-test-environment.d.mts:1-9 |
| The changed-lines floor keeps pure scoring importable but guards direct `main()` before base resolution. | `measureDiffCoverage`; `main`; direct-file guard | dashboard/scripts/check-diff-coverage.mjs:14-80; dashboard/scripts/check-diff-coverage.mjs:213-220 |
| The executable-statement contract suite proves both CLI refusal and pure accounting. | "describe(\"check-diff-coverage executable-statement semantics\", () => {" | dashboard/scripts/check-diff-coverage.test.mjs:15-110 |
| Vitest collects the route's script tests and loads the shared test setup. | `include`; `setupFiles` | dashboard/vitest.config.ts:27-33; dashboard/vitest.config.ts:57-59 |

## Cross-Repo References

No cross-repository implementation source governs this route.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-24T13:51:26+02:00 — 260821-DAGQC-L4: onboarded the canonical
  Dagger admission validator and declaration, the direct-main changed-lines guard, and the
  supported diagnostic-only targeted Vitest route. Playwright, pytest, changed-lines CLI,
  direct Python wrapper, and acceptance remain Dagger-attested; acceptance verification is
  pending and closeout-owned.
- 2026-08-14T05:26Z — L23 final curator: re-read the Dagger-environment guard script and its
  collection path; retained the route contract and repaired the exact Vitest anchors. Verification
  remains closeout-owned.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator (round 8 delta): created this route
  overview for the dashboard quality scripts after the executable-statement
  diff-coverage unit and its contract test landed. Verification pinned to `cf5ef50`
  until closeout stamps the code commit.
