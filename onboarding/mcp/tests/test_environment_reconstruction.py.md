# mcp/tests/test_environment_reconstruction.py

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

## Evidence

### Docs References

No configured Domain Documentation source applies.

- The suite's refusal claims are backed by its retained tests. [1]

### Repo-Internal References

- The owner and bounded reconstruction request are loaded from the real source contract. [2]
- Controlled roots include both scopes and a symlink. [3]
- Every listed corruption and an in-flight mutation must refuse. [4]

### Cross-Repo References

None; the suite uses the local environment census owner.
