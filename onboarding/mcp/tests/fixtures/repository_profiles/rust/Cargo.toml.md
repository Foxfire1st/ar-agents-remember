# mcp/tests/fixtures/repository_profiles/rust/Cargo.toml

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

## Evidence

### Docs References

CCR-R22@v1 requires two non-Agents-Remember fixture repositories with different languages,
commands, artifacts, and E2E tools to complete the same Gate 1-4 protocol.

Two non-Agents-Remember fixture repositories complete the same Gate 1-4 protocol.

The governing CCR-R22@v1 packet is a task artifact, so this requirement fact is
recorded as prose here (task artifact paths are not repo-relative citations).

### Repo-Internal References

- Rust fixture manifest with its lockfile and test layout. [1]
