# mcp/tests/test_route_measurement.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_route_measurement.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Forces the representative non-accepting route measurement to use a balanced cold/warm matrix over
explicit pure, integration, and durability populations under serial and repository-default xdist,
with exact outcome parity and content-addressed raw evidence.

## Code Commentary

### Logic

Synthetic phase reports and run results let the suite verify the full matrix without executing the
expensive populations. It checks alternating topology order, exact passed-node/topology validation,
raw run retention plus per-cohort distributions and limitations, confined content-addressed
artifact references, and refusal of too few repetitions before Dagger admission.

### Conventions

The tests inspect internal matrix/payload helpers because those structures are the durable evidence
contract exported by the public Dagger route. They never treat this focused test as acceptance
evidence itself.

### Invariants And Boundaries

- Every cohort/topology has paired cold and warm samples; topology lead alternates by pair.
- Selected nodes, outcomes, and actual worker topology must match the declared run exactly.
- Raw phase/log artifacts remain confined below the report root and content-addressed.
- The result is non-accepting and records its limitations; fewer than two repetitions are invalid.

### Todos

None.

## Docs References

No Domain Documentation source is configured; this is a repository-owned measurement contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is required for the representative matrix. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The matrix covers every cohort/topology/cache state and alternates ordering. | `test_measurement_matrix_repeats_cold_and_warm_for_every_exact_population` | mcp/tests/test_route_measurement.py:50-69 |
| Validation requires exact passed-node parity and actual topology. | `test_run_validation_requires_exact_passed_nodes_and_actual_topology` | mcp/tests/test_route_measurement.py:72-80 |
| Payloads retain raw runs, distributions, non-accepting authority, and limitations. | `test_measurement_payload_keeps_raw_runs_distributions_and_limitations` | mcp/tests/test_route_measurement.py:83-104 |
| Artifact references are content-addressed/confined and undersized repetition sets fail early. | `test_artifact_reference_is_content_addressed_and_confined`; `test_repetitions_below_two_are_refused_before_admission` | mcp/tests/test_route_measurement.py:107-126 |

## Cross-Repo References

No meaningful cross-repository boundary applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| Measurement execution stays within the admitted repository candidate. | — | — |

## Update History

- 2026-08-28T06:28+02:00 — PDLS wave 005 curator: created the missing sidecar for the redesigned
  representative pure/integration/durability measurement matrix.
