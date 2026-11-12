# mcp/test_support/agents_remember_test_support/testing/pytest_phase_reporter.py

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

## Evidence

### Docs References

Pytest-xdist hook semantics were checked against its official plugin API during implementation;
the durable behavior is encoded in focused tests.

### Repo-Internal References

- State includes expected and collected xdist worker identities. [1]
- Serial and xdist collection close through one helper. [2]
- Final payload keeps nullable phases and exact outcomes. [3]

### Cross-Repo References

No adjacent repository supplies the report.
