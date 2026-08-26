# dashboard/scripts/require-dagger-test-environment.d.mts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/scripts/require-dagger-test-environment.d.mts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T13:51:26+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[dashboard quality-scripts overview](overview.md)

## Purpose

Declare the TypeScript surface of the dashboard's canonical Dagger-environment validator.
This is a type companion only; it owns no runtime authority or fallback behavior.

## Code Commentary

### Logic

The declaration mirrors the two string constants, the pure validator returning
`string | null`, its optional environment/reader injections, and the throwing facade with
an optional subject label.

### Conventions

Keep this declaration byte-for-contract aligned with the ESM implementation's exports.

### Invariants And Boundaries

- The optional parameters exist for typing the implementation's test seams; they do not weaken
  production admission.
- The file declares no nonce writer, alternate path, bypass, configuration owner, or executor.
- Runtime truth remains in `require-dagger-test-environment.mjs`.

### Todos

None.

## Docs References

No external Domain Documentation governs this repository-owned declaration.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation was required. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The declaration exposes the constants, pure validator, and throwing facade. | `DAGGER_TEST_ATTESTATION_ENV`; `DAGGER_TEST_ATTESTATION_PATH`; `daggerTestEnvironmentError`; `requireDaggerTestEnvironment` | dashboard/scripts/require-dagger-test-environment.d.mts:1-2; dashboard/scripts/require-dagger-test-environment.d.mts:4-7; dashboard/scripts/require-dagger-test-environment.d.mts:9-9 |
| Runtime validation and refusal behavior live in the paired ESM file. | `DAGGER_TEST_ATTESTATION_ENV`; `DAGGER_TEST_ATTESTATION_PATH`; `daggerTestEnvironmentError`; `requireDaggerTestEnvironment` | dashboard/scripts/require-dagger-test-environment.mjs:3-4; dashboard/scripts/require-dagger-test-environment.mjs:6-24; dashboard/scripts/require-dagger-test-environment.mjs:26-34 |

## Cross-Repo References

No cross-repository boundary is owned by this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository references were found. | n/a | n/a |

## Update History

- 2026-08-24T13:51:26+02:00 — Created for 260821-DAGQC-L4 alongside the canonical
  ESM validator. Verification and Dagger acceptance remain closeout-owned.
