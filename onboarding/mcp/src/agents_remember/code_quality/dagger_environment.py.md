# mcp/src/agents_remember/code_quality/dagger_environment.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/code_quality/dagger_environment.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-14T11:20+02:00 |
| lastVerifiedCommitHash | `a89a6fc88d9330eb2749c87b3dcc3f6c4e46c4bd` |
| lastVerifiedCommitDate | 2026-08-14T12:44:51+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

`dagger_environment.py` is the single production validator for every Python test-capable entry
point. It proves that the process is inside the pinned Dagger quality graph before pytest
collection, direct wrapper parsing, targeted planning, or retry-proof selection can begin.

## Code Commentary

### Logic

`dagger_test_environment_error` requires `AR_DAGGER_TEST_ATTESTATION` to be exactly 32 lowercase
hexadecimal characters, reads the fixed in-container attestation file, and compares the two nonce
values byte-for-byte. Missing, malformed, unreadable, or mismatched evidence returns a precise
refusal reason.

`require_dagger_test_environment` binds that validator to the current process by default and raises
`DaggerEnvironmentError` with the Dagger-only command guidance. Callers may inject an environment
and attestation path only for deterministic tests; production callers use the fixed environment
variable and `/tmp/ar-quality/dagger-test-attestation` path.

### Invariants And Boundaries

- An environment variable alone is not authority; the graph must also write the matching file.
- Validation happens before any test-capable planning, so host execution cannot reach a cached
  proof, an empty targeted selection, or ordinary pytest collection.
- The validator owns environment authorization only. Candidate selection, diff-base proof, and
  lifecycle acceptance remain with the closeout/integration Dagger adapters.
- There is no host diagnostic or compatibility fallback.

### Todos

None recorded.

## Docs References

The repository-local Dagger-only execution contract is recorded in `system/tools.md` and
`system/git-workflow.md` in the resolved memory layer.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The validator requires a 32-hex nonce and a byte-identical attestation file before authorizing the environment. | `dagger_test_environment_error` | mcp/src/agents_remember/code_quality/dagger_environment.py:17-34 |
| The raising boundary supplies the shared Dagger-only refusal and live command guidance. | `require_dagger_test_environment` | mcp/src/agents_remember/code_quality/dagger_environment.py:36-48 |
| The quality wrapper invokes the validator before parser construction or planning. | `main` | mcp/src/agents_remember/code_quality/check.py:990-1000 |
| Pytest collection delegates to the same production validator instead of carrying a second implementation. | `require_dagger_test_environment` | mcp/tests/conftest.py:46-51 |

## Cross-Repo References

No external repository supplies or overrides this attestation contract.

## Update History

- 2026-08-14T11:20+02:00 — Created for the R39 final candidate. Documented the shared nonce/file
  guard and its before-planning fail-closed boundary. Verification remains closeout-owned.
