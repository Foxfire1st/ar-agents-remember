# mcp/tests/fixtures/repository_profiles/rust/tests/unit.rs

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/repository_profiles/rust/tests/unit.rs` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `../../../../overview.md` |

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

## Docs References

CCR-R22@v1: Gate 2 contains the configured ordinary test suite and publishes complete
exact-candidate result artifacts.

Gate 2 contains the configured ordinary test suite and publishes its complete exact-candidate result artifacts.

The governing CCR-R22@v1 packet is a task artifact, so this requirement fact is
recorded as prose here (task artifact paths are not repo-relative citations).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture unit test target driven by the suite script. | `adds_two_values` | mcp/tests/fixtures/repository_profiles/rust/tests/unit.rs:1-6; mcp/tests/fixtures/repository_profiles/rust/scripts/run-suite.sh:1-9 |

## Update History

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): created the sidecar for the new Rust fixture unit test.
