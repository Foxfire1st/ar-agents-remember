# mcp/tests/test_kernel_pure_regressions.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Retains five small deterministic product regressions after Candidate A and its host runner were
removed. The two exclusively retired route-normalization cases are absent; provider-ID and
gate/decision-role assertions remain unchanged.

## Code Commentary

The retained tests cover provider-ID normalization and known/unknown gate and decision-role
coercion. They are ordinary pytest unit regressions in the explicit lane manifest; neither this
source inventory nor the removed route-normalization cases establish a fresh measurement run.

## Invariants And Boundaries

- These are real product assertions preserved from the retired experiment, not classifier fixtures.
- They execute only through pytest inside the pinned Dagger evidence environment.
- No host wrapper, sealed cohort manifest, static closure analyzer, or compatibility entrypoint is
  retained.
- Retiring the two route-normalization cases does not retire provider-ID or gate/role guards;
  this card does not renew any separate measurement cohort or execution result.

## Evidence

### Docs References

The Candidate A retirement and replacement measurement are described in
`docs/design/python-test-evidence.md`.

### Repo-Internal References


- Five retained provider-ID and gate/decision-role guards remain; the two retired route-normalization cases are not replaced by whole-file assertions. [1]



### Cross-Repo References

No cross-repository boundary applies.



- The explicit unit lane owns the module.  Anchor: "mcp/tests/test_kernel_pure_regressions.py" [2]
