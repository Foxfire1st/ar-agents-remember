# mcp/tests/fixtures/repository_profiles/node/src/math.mjs

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/repository_profiles/node/src/math.mjs` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview | `../../../../overview.md` |

## Governing Overview

[mcp/tests overview](../../../../overview.md)

## Purpose

The single source module of the Node repository-profile fixture: an ESM `add(left, right)`
function imported by the unit and e2e fixture tests. It gives the fixture a real source file the
Gate-1 lint rail and the Gate-2 suite can operate on without any Python or Agents Remember
assumption.

## Code Commentary

`export function add(left, right) { return left + right; }` is the entire module. The lint
script checks it (along with the tests) for tabs and `var` usage; the suite script runs
`node --test` over the selected fixture tests; the e2e script runs the e2e test naming a
"clean-room service flow".

## Invariants And Boundaries

- Fixture source only; not part of the product or test-support package.
- Must stay free of tabs/`var` so the fixture's own lint rail passes deterministically.

## Docs References

CCR-R22@v1 verifies repository configurability through two foreign fixture repositories with
different languages, commands, artifacts, and E2E tools.

Two non-Agents-Remember fixture repositories complete the same Gate 1-4 protocol.

The governing CCR-R22@v1 packet is a task artifact, so this requirement fact is
recorded as prose here (task artifact paths are not repo-relative citations).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Source module exercised by the fixture lint/suite/e2e rails. | `add` | mcp/tests/fixtures/repository_profiles/node/src/math.mjs:1-3 |

## Update History

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): created the sidecar for the new Node fixture source module.
