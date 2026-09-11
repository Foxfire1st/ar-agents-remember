# mcp/tests/fixtures/repository_profiles/node/scripts/coverage-check.mjs

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/repository_profiles/node/scripts/coverage-check.mjs` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `../../../../overview.md` |

## Governing Overview

[mcp/tests overview](../../../../overview.md)

## Purpose

The Gate-3 (post-suite quality) rail of the Node repository-profile fixture: it consumes the
Gate-2 coverage artifact and proves the declared coverage proof is complete before the gate may
pass. It exists so the fixture profile has a real suite-dependent quality consumer (Gate 3 must
consume a green Gate-2 certificate or its declared artifacts).

## Code Commentary

`coverage-check.mjs` takes the coverage path as its single argument, parses the JSON written by
`run-suite.mjs`, and requires `statementCoverage === 100` and `suiteResult ===
"node-suite.json"`. It is the fixture's Gate-3 rail and its inputs are exactly the Gate-2
artifacts the suite script declares.

## Invariants And Boundaries

- Gate-3 input discipline: the rail only reads artifacts declared by the Gate-2 suite script;
  no undeclared artifact is allowed by the profile.
- Deterministic fixture check: passes exactly when coverage is 100 and the suite proof names the
  canonical suite artifact.

## Docs References

CCR-R22@v1 classifies Gate 3 as containing only checks that consume a green Gate-2 certificate or
its declared artifacts; a Gate-3 rail without a Gate-2 input makes the profile invalid at
admission.

Gate 3 contains only checks that consume a green Gate-2 certificate or its declared artifacts.

The governing CCR-R22@v1 packet is a task artifact, so this requirement fact is
recorded as prose here (task artifact paths are not repo-relative citations).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture post-suite coverage proof over the suite artifact. | `statementCoverage` | mcp/tests/fixtures/repository_profiles/node/scripts/coverage-check.mjs:1-7; mcp/tests/fixtures/repository_profiles/node/scripts/run-suite.mjs:1-23 |

## Update History

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): created the sidecar for the new Node fixture post-suite coverage rail.
