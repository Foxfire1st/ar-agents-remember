# dashboard/scripts/require-dagger-test-environment.mjs

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

## Evidence

### Docs References

No external Domain Documentation governs this repository-owned admission contract.

No relevant external documentation was required.

### Repo-Internal References

- Token format, fixed attestation path, read failure, and exact-match outcomes share one validator. [1]
- The throwing facade only adds a subject label and Dagger guidance. [2]
- The changed-lines CLI invokes this owner as the first operation of direct `main()`. [3]

### Cross-Repo References

No cross-repository boundary is owned by this file.

No meaningful cross-repository references were found.
