# mcp/tests/test_kernel_pure_regressions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_kernel_pure_regressions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

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

## Docs References

The Candidate A retirement and replacement measurement are described in
`docs/design/python-test-evidence.md`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Seven exact tests preserve the former cohort's unique product assertions. | `test_stable_provider_id_never_returns_empty`; gate/role coercion tests; route-normalization tests | mcp/tests/test_kernel_pure_regressions.py:24-54 |
| Representative measurement names these seven exact nodes as its pure cohort. | `COHORTS` | mcp/test_support/agents_remember_test_support/testing/route_measurement.py:79-112 |
| The explicit unit lane owns the module. | "mcp/tests/test_kernel_pure_regressions.py" | mcp/tests/test-evidence-lanes.toml:123-123 |

## Cross-Repo References

No cross-repository boundary applies.

## Update History

- 2026-08-28T05:10+02:00 — Renamed and rewritten after deleting Candidate A while preserving its
  seven unique product regressions as ordinary explicit-lane pytest evidence.
- 2026-08-24T21:23+02:00 — Created as the original seven-node Candidate A cohort.
