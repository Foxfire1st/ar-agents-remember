# mcp/tests/test_kernel_pure_regressions.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Retains four small deterministic product regressions after Candidate A and its host runner were
removed. The retired route-normalization and provider-ID cases are absent; gate-kind and
decision-role assertions remain unchanged.

## Code Commentary

The retained tests cover known/unknown gate-kind and decision-role
coercion. They are ordinary pytest unit regressions in the explicit lane manifest; neither this
source inventory nor the removed route-normalization cases establish a fresh measurement run.

## Invariants And Boundaries

- These are real product assertions preserved from the retired experiment, not classifier fixtures.
- These are ordinary isolated pytest regressions; delivery certification uses the separate explicit Dagger route.
- No host wrapper, sealed cohort manifest, static closure analyzer, or compatibility entrypoint is
  retained.
- Retiring the route-normalization and provider-ID cases does not retire the four gate-kind and decision-role guards;
  this card does not renew any separate measurement cohort or execution result.

## Recorded Earlier Reference Account

The earlier card at memory snapshot `81cfe4a8` identified
`docs/design/python-test-evidence.md` as the Candidate A retirement and
replacement-measurement account. That is the earlier reference account;
the document's current role is described in Evidence below.

## Evidence

### Docs References

`docs/design/python-test-evidence.md` defines the current certification authority and
its distinction from ordinary isolated pytest.

### Repo-Internal References


- Four retained gate-kind and decision-role guards remain; the retired provider-ID and route-normalization cases are absent.


### Cross-Repo References

No cross-repository boundary applies.

### Repo-Internal References (continued)

- The `unit-regression` lane selects `mcp/tests/test_kernel_pure_regressions.py`. [2]
