# mcp/tests/fixtures/repository_profiles/node/test/e2e.test.mjs

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/repository_profiles/node/test/e2e.test.mjs` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `../../../../overview.md` |

## Governing Overview

[mcp/tests overview](../../../../overview.md)

## Purpose

The clean-room service-flow E2E test of the Node repository-profile fixture, run by the Gate-4
rail (`node --test test/e2e.test.mjs`). It composes repository behavior (JSON with
`add(20, 22)` = 42) to represent an integration scenario for the foreign fixture repository.

## Code Commentary

A single `node:test` case serializes `{ total: add(20, 22) }` and asserts it deep-equals
`{ total: 42 }`. The Gate-4 rail publishes an `{"status": "passed", "tool": "node:test"}`
result when it passes.

## Invariants And Boundaries

- Fixture-only integration scenario; the product never launches a real Codex or clean-room
  environment from framework code.
- Part of the Node fixture profile's Gate-4 applicability.

## Docs References

CCR-R22@v1: Gate 4 contains clean-room or external/runtime integration and E2E certification;
repositories may choose tools and populations but not the ordering contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| Gate 4 contains clean-room or external/runtime integration and E2E certification. | `## Framework-Owned Classification Rules` | ar-coordination/tasks/agents-remember/260831_closeout-certification-reform/requirements/CCR-R22-v1-repository-owned-certification-gate-profiles.md |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture e2e scenario executed by the Gate-4 rail. | `test("the clean-room service flow composes repository behavior")` | mcp/tests/fixtures/repository_profiles/node/test/e2e.test.mjs; mcp/tests/fixtures/repository_profiles/node/scripts/run-e2e.mjs |

## Update History

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): created the sidecar for the new Node fixture E2E test.
