# mcp/test_support/agents_remember_test_support/testing/pytest_phase_reporter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/testing/pytest_phase_reporter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python testing boundary](overview.md)

## Purpose

Produces the common route-neutral node/outcome, population, and phase-timing record used for
Dagger evidence without granting acceptance authority.

## Code Commentary

### Logic

One mutable `_PhaseState` records session, collection, first-node, outcomes, and xdist worker
collection identities. The controller learns the actual worker count from `pytest_xdist_setupnodes`
and closes collection only after every worker's `pytest_xdist_node_collection_finished` callback.
Serial collection uses the same completion helper. Session finish writes a total JSON report and
measures its own reporting duration. Population evidence includes selected/deselected/reported
counts, content digests for node identities, actual xdist worker count, and worker-collection
consistency without duplicating thousands of node ids in every summary artifact.

### Conventions

xdist hooks are optional so the same plugin runs serially. Missing phases serialize as `null` and
never mask pytest's original exit.

### Invariants And Boundaries

- Worker node identities are counted once; the controller alone publishes.
- Collection cannot close on the first xdist worker.
- The recorded exit code remains pytest's original status.
- Phase/node observations carry no acceptance authority by themselves.

### Todos

None.

## Docs References

Pytest-xdist hook semantics were checked against its official plugin API during implementation;
the durable behavior is encoded in focused tests.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| State includes expected and collected xdist worker identities. | `_PhaseState` | mcp/test_support/agents_remember_test_support/testing/pytest_phase_reporter.py:15-43 |
| Serial and xdist collection close through one helper. | `pytest_xdist_setupnodes` | mcp/test_support/agents_remember_test_support/testing/pytest_phase_reporter.py:45-105 |
| Final payload keeps nullable phases and exact outcomes. | `_payload` | mcp/test_support/agents_remember_test_support/testing/pytest_phase_reporter.py:107-198 |

## Cross-Repo References

No adjacent repository supplies the report.

## Update History

- 2026-08-28T04:37+02:00 — Added selected/deselected population digests and explicit xdist
  collection-consistency evidence for candidate-bound comparison artifacts.
- 2026-08-25T01:56+02:00 — Added all-worker xdist collection ownership after the initial full gate
  exposed a missing collection phase.
- 2026-08-24T21:23+02:00 — Created for 260824-PDLS; curator recorded the total-report and
  single-state-object repair.
