# mcp/tests/fixtures/repository_profiles/rust/scripts/select-tests.sh

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/repository_profiles/rust/scripts/select-tests.sh` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | db57101a9001ede8c681ff9de4eb0147d8b636bc |
| lastVerifiedCommitDate | 2026-09-02T16:49:50+02:00|
| governingOverview | `../../../../overview.md` |

## Governing Overview

[mcp/tests overview](../../../../overview.md)

## Purpose

The non-Python fixture selector for the Rust repository-profile fixture: it emits a complete
`repository-selector-result/v2` JSON result selecting the `unit@@ Rust binary population with a
self-computed selection digest. It proves the selector contract is language-agnostic (CCR-R19@v2).

## Code Commentary

### Logic

The script reads eight arguments — output path, mode, diff base, candidate kind/value, selector
id/version, and configuration digest — and builds the v2 payload with the matching dependency
reason (`declared-consumer` for `tests/unit.rs` into output value `unit@@), population equal to
the declared mode, and `globalInvalidators=["declared-full-mode"]` when mode is full. The digest
is computed over the payload bytes with `sha256sum` and reinserted as `selectionDigest`
before writing the result file.

### Invariants And Boundaries

- The fixture result is complete and digest-consistent with its own payload.
- The emitted schema is exactly `repository-selector-result/v2`; v1 output is no longer
  produced (L19).
- A fixture script never changes its declared population regardless of inputs.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this verification fixture.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The emitted population and digest are bound to the exact declared input identity. | `selected-tests`; `selectionDigest` | mcp/tests/fixtures/repository_profiles/rust/scripts/select-tests.sh:20-21 |
| The v2 result contract the fixture emits. | `RepositorySelectionResult` | mcp/src/agents_remember/certification/repository_profiles/selection_results.py:89-130 |
| The profile test binds this fixture's configuration digest to its selector declaration. | `test_non_python_selector_fixture_emits_the_canonical_generic_result` | mcp/tests/test_repository_certification_profiles.py:651-684 |

## Cross-Repo References

None; the fixture is repository-local verification data.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): created the card and recorded the
  L19 upgrade to `repository-selector-result/v2` with self-computed selection digest and
  mode/candidate/selector identity arguments. Verification is pinned to the owning commit.
