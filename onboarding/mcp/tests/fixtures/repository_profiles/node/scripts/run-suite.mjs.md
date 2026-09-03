# mcp/tests/fixtures/repository_profiles/node/scripts/run-suite.mjs

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/repository_profiles/node/scripts/run-suite.mjs` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `../../../../overview.md` |

## Governing Overview

[mcp/tests overview](../../../../overview.md)

## Purpose

The Gate-2 ordinary-suite rail of the Node repository-profile fixture: it runs the selected tests
through `node --test`, publishes the suite result artifact, and publishes the coverage artifact
consumed by the Gate-3 rail. It proves the generic executor can run a repository-owned Node test
command for the configured ordinary test suite.

## Code Commentary

`run-suite.mjs` requires `[suitePath, coveragePath, ...selectedTests]` arguments, refuses when
any is empty, runs `node --test` over the selected tests with inherited stdio, exits with the
spawned status on failure, then writes the suite artifact
(`{"status": "passed", "selectedTests": [...]}`) and the coverage artifact
(`{"statementCoverage": 100, "suiteResult": <suite basename>}`).

## Invariants And Boundaries

- Gate-2 artifacts are exactly the suite result and the coverage proof; the Gate-3 rail consumes
  only these declared artifacts.
- The rail runs only the exact selected tests the profile passes; there is no fallback suite.
- Fixture-only; no product code path invokes it.

## Docs References

CCR-R22@v1 classifies Gate 2 as the configured ordinary test suite publishing its complete
exact-candidate result artifacts; prerequisites and artifact flow cannot point backward.

| Finding | Anchor | Source |
| --- | --- | --- |
| Gate 2 contains the configured ordinary test suite and publishes its complete exact-candidate result artifacts. | `## Framework-Owned Classification Rules` | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R22-v1-repository-owned-certification-gate-profiles.md |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture suite rail publishing suite and coverage artifacts. | `run-suite.mjs` | mcp/tests/fixtures/repository_profiles/node/scripts/run-suite.mjs; mcp/tests/fixtures/repository_profiles/node/scripts/coverage-check.mjs |

## Update History

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): created the sidecar for the new Node fixture suite rail.
