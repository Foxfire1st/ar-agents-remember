# mcp/tests/test_environment_reconstruction.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_environment_reconstruction.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-09 |
| lastVerifiedCommitHash | `602143bd1d48226f4d53b83ff7c5002a695dcdff` |
| lastVerifiedCommitDate | 2026-09-09T00:26:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Tests the environment-dependency census identity and fail-closed reconstruction contract. Byte, mode, missing, extra, symlink, omitted-row, mutation, and malformed-proof changes cannot be accepted as the original census.

## Code Commentary

### Logic

`_owner` loads the actual environment census owner, `_request` constructs the bounded typed request, and `_tree` builds controlled dependency/generated roots with a symlink. The parametrized corruption test mutates one identity dimension and requires refusal; the mutation test changes file mode during read and requires failure.

### Invariants And Boundaries

- Reconstruction compares exact bytes, modes, membership, symlink shape, and digest rows.
- A file mutation during census cannot become certifying evidence.
- The suite provides local contract proof; it is not a Dagger execution record.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite's refusal claims are backed by its retained tests. | `test_missing_corrupt_or_different_reconstruction_never_matches_original` | mcp/tests/test_environment_reconstruction.py:71-105 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The owner and bounded reconstruction request are loaded from the real source contract. | `_owner`; `_request` | mcp/tests/test_environment_reconstruction.py:18-46 |
| Controlled roots include both scopes and a symlink. | `_tree` | mcp/tests/test_environment_reconstruction.py:49-55 |
| Every listed corruption and an in-flight mutation must refuse. | `test_missing_corrupt_or_different_reconstruction_never_matches_original`; `test_file_mutation_during_census_cannot_be_certified` | mcp/tests/test_environment_reconstruction.py:71-126 |

## Cross-Repo References

None; the suite uses the local environment census owner.

## Update History

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited-source reconciliation: created the previously absent test sidecar from source bytes matching code commit `8133b6a9de2f787cb6c4527621a70123357aff31` (candidate-tree source SHA-256 `361f0feab875d266dc189f056330e116f0497025b2ad4a24b2955c7fdda5b311`). No test execution or future candidate verification stamp is claimed.
