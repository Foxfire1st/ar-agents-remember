# mcp/tests/test_agent_notifier_ladder.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Task-topology builders shared by notifier consumers.

## Code Commentary

### Logic

_write_topology writes a sprint, one master and sixty real leaf documents beneath the supplied temporary root. _task_doc validates model inputs and _leaf_ref returns exact document references. No ladder-walk tests remain in this file.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The historical ladder filename does not establish escalation behavior or authorize restoring retired ladder tests.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Task doc. [1]
- Write topology. [2]
- Leaf ref. [3]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
