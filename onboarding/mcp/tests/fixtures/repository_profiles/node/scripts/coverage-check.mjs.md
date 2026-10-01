# mcp/tests/fixtures/repository_profiles/node/scripts/coverage-check.mjs

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

## Evidence

### Docs References

CCR-R22@v1 classifies Gate 3 as containing only checks that consume a green Gate-2 certificate or
its declared artifacts; a Gate-3 rail without a Gate-2 input makes the profile invalid at
admission.

Gate 3 contains only checks that consume a green Gate-2 certificate or its declared artifacts.

The governing CCR-R22@v1 packet is a task artifact, so this requirement fact is
recorded as prose here (task artifact paths are not repo-relative citations).

### Repo-Internal References

- Fixture post-suite coverage proof over the suite artifact. [1]
