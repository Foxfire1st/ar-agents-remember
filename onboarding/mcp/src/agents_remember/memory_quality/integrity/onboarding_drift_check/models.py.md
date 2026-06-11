# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-29T12:10+02:00                     |
| lastVerifiedCommitHash | `12737deaac2fd75563ca1e3037cdac911023cf93` |
| lastVerifiedCommitDate | 2026-05-29T12:28:42+02:00|
| governingOverview      | `../../../../../overview.md`               |

## Purpose

`models.py` holds the shared data records and constants for onboarding drift
detection. It is the foundational module of the `onboarding_drift_check` package
and carries no behavior, so every classifier and reporter can depend on it
without import cycles.

## Code Commentary

### Logic

Defines the `DriftRow` result record returned by every classifier, the
`EntityFingerprint` row model, and the `InlineBlock` parse result. Also defines
the module constants: `CLASSIFICATIONS`, `ACTIONABLE_CLASSIFICATIONS`, the inline
markers, `GIT_BLOB_SET_ALGORITHM`, `SIDECAR_DOC_TYPES`, `COMMON_BLOCK_DELIMITERS`,
and the `repo_root_placeholder()` helper.

### Invariants And Boundaries

- Behavior-free: dataclasses and constants only; no I/O, git, or policy.
- Imported by `git_ops`, `discovery`, `report`, `entities`, `inline`, and
  `sidecar`; it must not import from them (keeps the package acyclic).

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The drift facade re-exports these models/constants for backward-compatible imports. | [drift.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py) |

## Update History

- 2026-05-29T12:10+02:00: Created when `drift.py` was split into focused modules; metadata pending closeout refresh to the split commit.
