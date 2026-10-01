# mcp/tests/test_operation_certification_selection.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Builds production-shaped closeout operation records and published certification generations to exercise initial certification selection and protected-generation reuse. Report payloads remain explicit fixture observations.

## Code Commentary

### Logic

`_Fixture` holds the contract, operation input, store, record, and frozen admission. `_fixture` prepares and optionally selects the initial certification. `_publish` writes declared artifacts through the real profile and publication owners, then records terminal generations for green, interrupted, or red outcomes.

### Invariants And Boundaries

- Selection consumes the exact task-addressed lifecycle store and prepared candidate.
- Published generations are immutable evidence; a red or interrupted outcome does not manufacture green certificates.
- The helper is preparation/test fixture code, not a standalone certification authority.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies.

- Operation selection fixture behavior is local test evidence. [1]

### Repo-Internal References

- Fixture state binds the exact operation and frozen admission. [2]
- Publication records artifact identities and terminal outcomes through production owners. [3]

### Cross-Repo References

None; the fixtures use local lifecycle and certification owners.
