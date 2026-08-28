# mcp/test_support/agents_remember_test_support/testing/route_measurement.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/testing/route_measurement.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python test evidence infrastructure](overview.md)

## Purpose

Measures exact representative pure, integration, and durability cohorts under Dagger-admitted
serial and repository-default xdist topologies on one complete Git candidate.

## Code Commentary

### Logic

The CLI runs repeated paired cold and warm observations per cohort/topology, alternating which
topology leads each pair. It records exact commands, subprocess wall time, admission/bootstrap,
collection, first-node, execution and reporting phases, selected/deselected population digests, and
content-addressed raw logs. It verifies all exact node outcomes and refuses if the Git candidate,
lane ownership, population, or topology changes.

### Conventions

The route is a non-accepting Dagger comparison. “Cold” means a new pytest-owned cache and basetemp
pair; shared immutable image/dependency layers and uncontrolled kernel page cache are explicit
limitations, not described as cold hardware.

### Invariants And Boundaries

- Serial/default-xdist comparisons use the same exact nodes and candidate for each cohort.
- Unknown/missing timing or outcome evidence fails the report.
- Measurements cannot mint quality acceptance.
- At least two cold and two warm observations are required for every median and range.

### Todos

None.

## Docs References

The measurement contract is explained in `docs/design/python-test-evidence.md`.

## Repo-Internal References

`.dagger/src/agents_remember_quality/main.py` owns the route container; `COHORTS`, `TOPOLOGIES`,
and `measure_representative_routes` own the exact measurement design.

## Cross-Repo References

No cross-repository boundary applies.

## Update History

- 2026-08-28T04:37+02:00 — Replaced the retired direct/pure-only comparison with repeated
  pure/integration/durability serial/default-xdist evidence and content-addressed raw runs.
- 2026-08-27T11:08+02:00 — Created for comparable same-candidate route evidence.
