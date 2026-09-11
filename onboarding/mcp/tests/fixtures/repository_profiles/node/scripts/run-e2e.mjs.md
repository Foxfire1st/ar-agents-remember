# mcp/tests/fixtures/repository_profiles/node/scripts/run-e2e.mjs

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/repository_profiles/node/scripts/run-e2e.mjs` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `../../../../overview.md` |

## Governing Overview

[mcp/tests overview](../../../../overview.md)

## Purpose

The Gate-4 (clean-room integration/E2E) rail of the Node repository-profile fixture: it runs the
e2e test through `node --test` and publishes the e2e result artifact. It proves the generic
executor can run a repository-owned clean-room/E2E scenario for a non-Agents-Remember repository
without any Codex or Python scenario in framework code.

## Code Commentary

`run-e2e.mjs` requires a result path argument, runs `node --test test/e2e.test.mjs` with
inherited stdio, exits with the spawned status on failure, then writes
`{"status": "passed", "tool": "node:test"}` to the result path.

## Invariants And Boundaries

- Gate-4 rail: runs only after Gates 1-3 in the profile's declared order; the framework never
  reorders integration ahead of cheaper gates.
- Fixture-only; the clean-room boundary is represented but no real isolation environment is spun
  up by the product.
- The e2e test asserts a "clean-room service flow" composes repository behavior.

## Docs References

CCR-R22@v1 classifies Gate 4 as clean-room or external/runtime integration and E2E certification;
the profile must not merge Gate 2 and Gate 3 or move Gate 4 ahead of cheaper gates.

Gate 4 contains clean-room or external/runtime integration and E2E certification.

The governing CCR-R22@v1 packet is a task artifact, so this requirement fact is
recorded as prose here (task artifact paths are not repo-relative citations).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture E2E rail publishing the e2e result artifact. | `spawnSync` | mcp/tests/fixtures/repository_profiles/node/scripts/run-e2e.mjs:1-13; mcp/tests/fixtures/repository_profiles/node/test/e2e.test.mjs:1-9 |

## Update History

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): created the sidecar for the new Node fixture E2E rail.
