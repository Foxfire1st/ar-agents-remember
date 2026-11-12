# mcp/tests/fixtures/repository_profiles/node/test/unit.test.mjs

## Governing Overview

[mcp/tests overview](../../../../overview.md)

## Purpose

Unit test of the Node repository-profile fixture source (`add(2, 3) === 5`), run by the Gate-2
suite rail via `node --test`. Part of the two foreign fixture repositories proving
repository-owned test populations.

## Code Commentary

A single `node:test` case asserts `add(2, 3)` equals 5 with `node:assert/strict`. The suite
rail's selected-tests argument passes this file as one of the exact selected tests.

## Invariants And Boundaries

- Fixture test only; not part of the product suite or pytest.
- Must stay clean (no tabs/`var`) so the lint rail passes.

## Evidence

### Docs References

CCR-R22@v1 requires fixture repositories with different ordinary suites completing the same Gate 1-4 protocol.

Fixture repositories with different languages, commands, artifacts, and E2E tools complete the same Gate 1-4 protocol.

The governing CCR-R22@v1 packet is a task artifact, so this requirement fact is
recorded as prose here (task artifact paths are not repo-relative citations).

### Repo-Internal References

- Fixture unit test selected by the suite rail. [1]
