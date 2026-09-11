# mcp/tests/fixtures/repository_profiles/node/test/unit.test.mjs

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/repository_profiles/node/test/unit.test.mjs` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `../../../../overview.md` |

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

## Docs References

CCR-R22@v1 requires fixture repositories with different ordinary suites completing the same Gate 1-4 protocol.

Fixture repositories with different languages, commands, artifacts, and E2E tools complete the same Gate 1-4 protocol.

The governing CCR-R22@v1 packet is a task artifact, so this requirement fact is
recorded as prose here (task artifact paths are not repo-relative citations).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture unit test selected by the suite rail. | `test("adds two values")` | mcp/tests/fixtures/repository_profiles/node/test/unit.test.mjs:1-8; mcp/tests/fixtures/repository_profiles/node/scripts/run-suite.mjs:1-23 |

## Update History

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): created the sidecar for the new Node fixture unit test.
