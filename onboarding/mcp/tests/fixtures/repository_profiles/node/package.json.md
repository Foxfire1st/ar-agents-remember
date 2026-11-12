# mcp/tests/fixtures/repository_profiles/node/package.json

## Governing Overview

[mcp/tests overview](../../../../overview.md)

## Purpose

Declares the non-Agents-Remember Node fixture repository `repository-profile-node-fixture` used
by the repository-certification tests to prove that two repositories with different languages,
commands, artifacts, and E2E tools complete the same Gate 1-4 protocol. It is ESM
(`"type": "module"`), private, and version 1.0.0; the lockfile mirrors it.

## Code Commentary

The manifest is deliberately minimal: name, privacy, ESM type, version. The executed rails live
in `scripts/*.mjs` and the tests in `test/*.test.mjs`; `package.json` exists so profile
fixtures can resolve a real, lockable Node module layout rather than a synthetic directory.

## Invariants And Boundaries

- This is a fixture, not application code: it must never be installed or imported by the product.
- It is one of the two required non-Agents-Remember fixture repositories (Node and Rust) named by
  CCR-R22's expected verification evidence.

## Evidence

### Docs References

CCR-R22@v1 requires two non-Agents-Remember fixture repositories with different languages,
commands, artifacts, and E2E tools to complete the same Gate 1-4 protocol.

Two non-Agents-Remember fixture repositories with different languages, commands, artifacts, and E2E tools complete the same Gate 1-4 protocol.

The governing CCR-R22@v1 packet is a task artifact, so this requirement fact is
recorded as prose here (task artifact paths are not repo-relative citations).

### Repo-Internal References

- The Node fixture manifest with its lockfile and ESM scripts/test layout. [1]
