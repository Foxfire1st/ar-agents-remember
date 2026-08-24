# dashboard/scripts/require-dagger-test-environment.mjs

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/scripts/require-dagger-test-environment.mjs` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T13:51:26+02:00 |
| lastVerifiedCommitHash |  `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate |  2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[dashboard quality-scripts overview](overview.md)

## Purpose

Own the dashboard-side admission check for Dagger-attested browser, integration, and
changed-lines execution. It translates one fixed nonce-and-file contract into a reusable,
fail-loud error without creating a host acceptance path.

## Code Commentary

### Logic

`daggerTestEnvironmentError` reads `AR_DAGGER_TEST_ATTESTATION`, accepts exactly 32
lowercase hexadecimal characters, reads `/tmp/ar-quality/dagger-test-attestation`, and
returns a reason unless the file bytes exactly equal the environment token.
`requireDaggerTestEnvironment` throws with Dagger-only guidance when that validator returns
an error. Its optional `subject` changes only the refusal message; it does not change
authority, token shape, path, or comparison.

### Conventions

The validator accepts injected environment and reader arguments so pure unit tests can
exercise every outcome without minting an attestation. Production callers use the defaults.

### Invariants And Boundaries

- This module validates attestation; it never writes a nonce or attestation file.
- Exact equality follows format validation. Missing/unreadable/mismatched evidence fails loud.
- There is no fake nonce, bypass flag, shadow configuration, host fallback, or compatibility route.
- Direct targeted Vitest diagnostics do not call this helper merely by importing guarded modules;
  guarded direct CLIs and browser/integration entrypoints call it at execution time.

### Todos

None.

## Docs References

No external Domain Documentation governs this repository-owned admission contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation was required. | _None._ | _No external source._ |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Token format, fixed attestation path, read failure, and exact-match outcomes share one validator. | L3-L24 | [require-dagger-test-environment.mjs](dashboard/scripts/require-dagger-test-environment.mjs) |
| The throwing facade only adds a subject label and Dagger guidance. | L26-L34 | [require-dagger-test-environment.mjs](dashboard/scripts/require-dagger-test-environment.mjs) |
| The changed-lines CLI invokes this owner as the first operation of direct `main()`. | L12-L12; L79-L80 | [check-diff-coverage.mjs](dashboard/scripts/check-diff-coverage.mjs) |

## Cross-Repo References

No cross-repository boundary is owned by this file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repository references were found. | _None._ | _No cross-repository source._ |

## Update History

- 2026-08-24T13:51:26+02:00 — Created for 260821-DAGQC-L4. The source owner is
  present in the uncommitted candidate; verification and Dagger acceptance remain closeout-owned.
