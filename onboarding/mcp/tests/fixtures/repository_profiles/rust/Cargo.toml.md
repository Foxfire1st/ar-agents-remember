# mcp/tests/fixtures/repository_profiles/rust/Cargo.toml

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/repository_profiles/rust/Cargo.toml` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `../../../../overview.md` |

## Governing Overview

[mcp/tests overview](../../../../overview.md)

## Purpose

Manifest of the non-Agents-Remember Rust fixture repository `repository-profile-rust-fixture`
(edition 2021, no external dependencies). Together with `Cargo.lock` (lockfile format version 3)
it gives profile consumers a real, lockable Rust runtime identity for the second foreign fixture
repository, proving Gate 1-4 protocol portability to a second language.

## Code Commentary

A minimal `[package]` block (name, version 1.0.0, edition 2021) with an empty
`[dependencies]` table. The crate's single function lives in `src/lib.rs`; the fixture tests
live in `tests/unit.rs` and `tests/service.rs`.

## Invariants And Boundaries

- Fixture data only; never built or installed by the product's own build.
- The lockfile must stay consistent with this manifest so `--locked` invocations resolve.

## Docs References

CCR-R22@v1 requires two non-Agents-Remember fixture repositories with different languages,
commands, artifacts, and E2E tools to complete the same Gate 1-4 protocol.

| Finding | Anchor | Source |
| --- | --- | --- |
| Two non-Agents-Remember fixture repositories complete the same Gate 1-4 protocol. | `## Expected Verification Evidence` | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R22-v1-repository-owned-certification-gate-profiles.md |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Rust fixture manifest with its lockfile and test layout. | `[package]` | mcp/tests/fixtures/repository_profiles/rust/Cargo.toml; mcp/tests/fixtures/repository_profiles/rust/Cargo.lock |

## Update History

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): created the sidecar for the new Rust fixture manifest.
