# mcp/tests/test_kernel_pure_regressions.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Retains seven small deterministic product regressions after Candidate A and its host runner were
removed.

## Code Commentary

The tests cover provider-ID normalization, known and unknown gate/decision-role coercion, and route
normalization. They are ordinary pytest unit-regression evidence in the explicit lane manifest.
`route_measurement.py` also uses their exact node IDs as its representative pure cohort, but that
measurement ownership does not turn this module into a separate diagnostic runner.

## Invariants And Boundaries

- These are real product assertions preserved from the retired experiment, not classifier fixtures.
- They execute only through pytest inside the pinned Dagger evidence environment.
- No host wrapper, sealed cohort manifest, static closure analyzer, or compatibility entrypoint is
  retained.
- The representative measurement must use these exact nodes or change its explicit cohort contract.

## Evidence

### Docs References

The Candidate A retirement and replacement measurement are described in
`docs/design/python-test-evidence.md`.

### Repo-Internal References

- Seven exact tests preserve the former cohort's unique product assertions. [1]
- The explicit unit lane owns the module. [2]

### Cross-Repo References

No cross-repository boundary applies.
