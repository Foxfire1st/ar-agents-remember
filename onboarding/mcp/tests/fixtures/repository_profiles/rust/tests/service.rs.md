# mcp/tests/fixtures/repository_profiles/rust/tests/service.rs

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/repository_profiles/rust/tests/service.rs` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `../../../../overview.md` |

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

## Docs References

CCR-R22@v1: Gate 4 contains clean-room or external/runtime integration and E2E certification.

Gate 4 contains clean-room or external/runtime integration and E2E certification.

The governing CCR-R22@v1 packet is a task artifact, so this requirement fact is
recorded as prose here (task artifact paths are not repo-relative citations).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture service/E2E test target driven by the e2e script. | `clean_room_service_flow_composes_repository_behavior` | mcp/tests/fixtures/repository_profiles/rust/tests/service.rs:1-7; mcp/tests/fixtures/repository_profiles/rust/scripts/run-e2e.sh:1-6 |

## Update History

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): created the sidecar for the new Rust fixture service/E2E test.
