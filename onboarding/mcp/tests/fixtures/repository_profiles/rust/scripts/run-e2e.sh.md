# mcp/tests/fixtures/repository_profiles/rust/scripts/run-e2e.sh

## Governing Overview

[mcp/tests overview](../../../../overview.md)

## Purpose

The Gate-4 clean-room/E2E rail of the Rust repository-profile fixture: runs
`cargo test --locked --test service` and publishes the e2e result artifact. Proves the generic
executor runs a repository-owned Rust integration scenario in Gate 4.

## Code Commentary

`set -eu`; takes `result_path`; runs `cargo test --locked --test service`; then writes
`{"status":"passed","tool":"cargo-test"}` to the result path. The service test target is
`tests/service.rs`.

## Invariants And Boundaries

- Gate-4 rail runs only after Gates 1-3 in the declared profile order; no reordering by the
  framework.
- Fixture-only; the clean-room boundary is represented, not spun up by the product.

## Evidence

### Docs References

CCR-R22@v1: Gate 4 contains clean-room or external/runtime integration and E2E certification.

Gate 4 contains clean-room or external/runtime integration and E2E certification.

The governing CCR-R22@v1 packet is a task artifact, so this requirement fact is
recorded as prose here (task artifact paths are not repo-relative citations).

### Repo-Internal References

- Fixture E2E rail invoking cargo --locked service tests. [1]
