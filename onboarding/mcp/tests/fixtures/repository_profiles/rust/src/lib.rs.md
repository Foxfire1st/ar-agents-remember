# mcp/tests/fixtures/repository_profiles/rust/src/lib.rs

## Governing Overview

[mcp/tests overview](../../../../overview.md)

## Purpose

The source module of the Rust repository-profile fixture: a single `add(left: u32, right: u32)
-> u32` public function imported by `tests/unit.rs` and `tests/service.rs`. It exists so the
fixture has a real Rust source file for the second-language repository proof.

## Code Commentary

`pub fn add(left: u32, right: u32) -> u32 { left + right }`. The fixture tests assert
`add(2, 3) == 5` (unit) and compose `add(20, 22)` into a `{"total":42}` JSON string
(service/E2E).

## Invariants And Boundaries

- Fixture source only; not part of the product crate.
- The function is used by both fixture test targets, so both suite and E2E rails exercise it.

## Evidence

### Docs References

CCR-R22@v1 verifies cross-language repository configurability through two foreign fixture
repositories.

Fixture repositories with different languages complete the same Gate 1-4 protocol.

The governing CCR-R22@v1 packet is a task artifact, so this requirement fact is
recorded as prose here (task artifact paths are not repo-relative citations).

### Repo-Internal References

- Rust fixture source consumed by unit and service tests. [1]
