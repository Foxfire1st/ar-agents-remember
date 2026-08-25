# mcp/src/agents_remember/testing/cadence_runner.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/testing/cadence_runner.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Runs scheduled stress, provider-bump, and migration-window evidence in the pinned Dagger
environment without creating a second acceptance route.

## Code Commentary

### Logic

`run_cadence_evidence` requires Dagger admission, validates the lifecycle catalog, selects one
closed trigger expression, forces serial pytest, and writes a structured non-accepting result plus
phase/event artifacts. An empty migration population produces a loud not-applicable result.

### Conventions

The Dagger module owns container construction; this module owns only the in-container cadence
command and result schema.

### Invariants And Boundaries

- Host execution refuses before inventory or pytest.
- Release and diagnostic triggers are rejected so this cannot shadow full quality or the direct
  exact-node route.
- Every result says `acceptanceEligible=false` and `certifying=false`.

### Todos

None.

## Docs References

No external domain documentation governs the local cadence command.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Only scheduled, provider-bump, and migration triggers can execute. | `run_cadence_evidence` | mcp/src/agents_remember/testing/cadence_runner.py:23-113 |
| The Dagger public route remains explicitly non-accepting. | `cadence_evidence` | .dagger/src/agents_remember_quality/main.py:273-342 |
| Focused tests force host refusal, serial stress, provider selection, and not-applicable migration. | `test_host_process_is_refused_before_inventory_or_execution` | mcp/tests/test_cadence_runner.py:36-119 |

## Cross-Repo References

No cross-repository cadence authority is owned here.

## Update History

- 2026-08-25T01:56+02:00 — Created for separated stress/provider/migration evidence cadence.
