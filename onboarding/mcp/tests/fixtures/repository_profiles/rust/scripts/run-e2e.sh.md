# mcp/tests/fixtures/repository_profiles/rust/scripts/run-e2e.sh

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/repository_profiles/rust/scripts/run-e2e.sh` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `../../../../overview.md` |

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

## Docs References

CCR-R22@v1: Gate 4 contains clean-room or external/runtime integration and E2E certification.

| Finding | Anchor | Source |
| --- | --- | --- |
| Gate 4 contains clean-room or external/runtime integration and E2E certification. | `## Framework-Owned Classification Rules` | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R22-v1-repository-owned-certification-gate-profiles.md |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture E2E rail invoking cargo --locked service tests. | `run-e2e.sh` | mcp/tests/fixtures/repository_profiles/rust/scripts/run-e2e.sh; mcp/tests/fixtures/repository_profiles/rust/tests/service.rs |

## Update History

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): created the sidecar for the new Rust fixture E2E rail.
