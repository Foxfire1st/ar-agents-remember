# mcp/tests/fixtures/repository_profiles/rust/tests/unit.rs

## Governing Overview

[mcp/tests overview](../../../../overview.md)

## Purpose

Unit test target of the Rust repository-profile fixture, run by the Gate-2 suite script
(`cargo test --locked --test ""`), asserting `add(2, 3) == 5`. Part of the foreign
fixture repository's ordinary test suite.

## Code Commentary

One `#[test]` function, `adds_two_values`, asserting equality. The suite script receives the
test name as its third argument and passes it to `cargo test --locked`, then writes the suite
proof artifact.

## Invariants And Boundaries

- Fixture test only; not part of the product's Rust or Python suites.
- Must pass deterministically so the fixture's Gate-2 rail stays green.

## Evidence

### Docs References

CCR-R22@v1: Gate 2 contains the configured ordinary test suite and publishes complete
exact-candidate result artifacts.

Gate 2 contains the configured ordinary test suite and publishes its complete exact-candidate result artifacts.

The governing CCR-R22@v1 packet is a task artifact, so this requirement fact is
recorded as prose here (task artifact paths are not repo-relative citations).

### Repo-Internal References

- Fixture unit test target driven by the suite script. [1]
