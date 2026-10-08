# mcp/tests/test_dispatch_agent_ambient.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Ambient versus hosted dispatch identity, role and rollback contracts.

## Code Commentary

### Logic

Unknown task and role-altitude mismatch refuse before spawn. Missing or broken hosted identity cannot downgrade into ambient dispatch. The real spawn primitive with a host double records an ambient architect and durable brief; persistence failure retires the newly created child through system closure. Unauthorized structural children refuse.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Only a proven unbriefed child is eligible for rollback. Host doubles create no real tmux session, and fixture launch settings do not override real authority.

### Todos

No file-local implementation change is requested by this reconciliation.

The successful ambient spawn case gives dispatch-brief readiness a zero wait and injects a sleeper whose call is an assertion failure. It retains real spawn and durable-brief assertions without a fixture-side readiness delay.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Ambient dispatch refuses unknown task reference before spawn. [1]
- Ambient dispatch refuses role altitude mismatch before spawn. [2]
- Role without hosted identity never falls back to ambient dispatch. [3]
- Ambient dispatch runs the real spawn and persists the brief. [4]
- Ambient dispatch rolls back via system closure when brief persistence fails. [5]
- Plane dispatch refuses broken plane identity without downgrading. [6]
- Plane dispatch refuses an unauthorized child role. [7]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.

- Ambient spawn and brief persistence use zero readiness wait and never sleep. [8]
