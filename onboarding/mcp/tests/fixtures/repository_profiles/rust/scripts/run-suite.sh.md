# mcp/tests/fixtures/repository_profiles/rust/scripts/run-suite.sh

## Governing Overview

[mcp/tests overview](../../../../overview.md)

## Purpose

The Gate-2 ordinary-suite rail of the Rust repository-profile fixture: runs `cargo test --locked
--test <name>` and publishes the suite result and proof artifacts. Proves the generic executor
invokes a repository-owned Rust command for the configured ordinary test suite.

## Code Commentary

`set -eu`; takes `suite_path`, `proof_path`, `test_name`; runs
`cargo test --locked --test "$test_name"`; then writes
`{"status":"passed","selectedTest":"<name>"}` to the suite path and
`{"suiteResult":"rust-suite.json","verified":true}` to the proof path. The post-suite script
consumes the proof path as the Gate-3 rail.

## Invariants And Boundaries

- Gate-2 artifact set is exactly the suite result and the proof; `--locked` requires the
  checked-in lockfile.
- Fixture-only; no product path invokes the shell script.

## Evidence

### Docs References

CCR-R22@v1: Gate 2 is the configured ordinary test suite publishing complete exact-candidate
result artifacts.

Gate 2 contains the configured ordinary test suite and publishes its complete exact-candidate result artifacts.

The governing CCR-R22@v1 packet is a task artifact, so this requirement fact is
recorded as prose here (task artifact paths are not repo-relative citations).

### Repo-Internal References

- Fixture suite rail invoking cargo --locked and publishing artifacts. [1]
