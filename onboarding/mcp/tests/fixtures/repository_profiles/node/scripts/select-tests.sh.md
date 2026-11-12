# mcp/tests/fixtures/repository_profiles/node/scripts/select-tests.sh

## Governing Overview

[mcp/tests overview](../../../../overview.md)

## Purpose

The non-Python fixture selector for the Node repository-profile fixture: it emits a complete
`repository-selector-result/v2` JSON result selecting `test/unit.test.mjs` with a
self-computed selection digest. It proves the selector contract is language-agnostic (CCR-R19@v2).

## Code Commentary

### Logic

The script reads eight arguments — output path, mode, diff base, candidate kind/value, selector
id/version, and configuration digest — and builds the v2 payload with the matching dependency
reason (`declared-consumer` for `test/unit.test.mjs`), population equal to the declared mode,
and `globalInvalidators=["declared-full-mode"]` when mode is full. The digest is computed over
the payload bytes with `sha256sum` and reinserted as `selectionDigest` before writing the
result file.

### Invariants And Boundaries

- The fixture result is complete and digest-consistent with its own payload.
- The emitted schema is exactly `repository-selector-result/v2`; v1 output is no longer
  produced (L19).
- A fixture script never changes its declared population regardless of inputs.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies to this verification fixture.

### Repo-Internal References

- The emitted population and digest are bound to the exact declared input identity. [1]
- The v2 result contract the fixture emits. [2]

### Cross-Repo References

None; the fixture is repository-local verification data.
