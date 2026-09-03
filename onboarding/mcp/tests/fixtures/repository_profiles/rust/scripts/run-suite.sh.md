# mcp/tests/fixtures/repository_profiles/rust/scripts/run-suite.sh

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/repository_profiles/rust/scripts/run-suite.sh` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `../../../../overview.md` |

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

## Docs References

CCR-R22@v1: Gate 2 is the configured ordinary test suite publishing complete exact-candidate
result artifacts.

| Finding | Anchor | Source |
| --- | --- | --- |
| Gate 2 contains the configured ordinary test suite and publishes its complete exact-candidate result artifacts. | `## Framework-Owned Classification Rules` | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R22-v1-repository-owned-certification-gate-profiles.md |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture suite rail invoking cargo --locked and publishing artifacts. | `run-suite.sh` | mcp/tests/fixtures/repository_profiles/rust/scripts/run-suite.sh; mcp/tests/fixtures/repository_profiles/rust/scripts/post-suite.sh; mcp/tests/fixtures/repository_profiles/rust/Cargo.lock |

## Update History

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): created the sidecar for the new Rust fixture suite rail.
