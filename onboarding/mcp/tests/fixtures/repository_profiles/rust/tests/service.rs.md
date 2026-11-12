# mcp/tests/fixtures/repository_profiles/rust/tests/service.rs

## Governing Overview

[mcp/tests overview](../../../../overview.md)

## Purpose

The clean-room service-flow integration test target of the Rust repository-profile fixture, run
by the Gate-4 e2e script (`cargo test --locked --test service`). It composes repository
behavior into a `{"total":42}` JSON response, representing the fixture's integration/E2E
certification.

## Code Commentary

One `#[test]` function, `clean_room_service_flow_composes_repository_behavior`, building
`format!("{{\\"total\\":{}}}", add(20, 22))` and asserting it equals `{"total":42}`. The e2e
script publishes `{"status": "passed", "tool": "cargo-test"}` when it passes.

## Invariants And Boundaries

- Fixture-only integration scenario; no real clean-room isolation is launched by the product.
- Part of the Rust fixture profile's Gate-4 applicability.

## Evidence

### Docs References

CCR-R22@v1: Gate 4 contains clean-room or external/runtime integration and E2E certification.

Gate 4 contains clean-room or external/runtime integration and E2E certification.

The governing CCR-R22@v1 packet is a task artifact, so this requirement fact is
recorded as prose here (task artifact paths are not repo-relative citations).

### Repo-Internal References

- Fixture service/E2E test target driven by the e2e script. [1]
