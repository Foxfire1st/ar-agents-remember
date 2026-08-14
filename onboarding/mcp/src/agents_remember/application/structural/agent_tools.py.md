# mcp/src/agents_remember/application/structural/agent_tools.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/structural/agent_tools.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T06:47+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structural application services](overview.md)

## Purpose

Implements agent dispatch, parent/child messaging, retirement, and rename as structural operations.
It resolves trusted ambient caller identity and document+role targets before invoking existing
plane-owned lifecycle and inbox primitives.

## Code Commentary

### Logic

`dispatch_agent_tool` validates a contained child seat, opens and binds a hosted occupant, then posts
the internally exact-pinned initial brief. `_message_tool` persists ordinary structural traffic for
post-time and delivery-time rebinding. Retire and rename functions authorize only structural child
or self relationships. `UnbriefedChild` keeps spawn/brief cleanup explicit.

### Conventions

Public results expose the structural target plus operation status or delivery detail. Runtime ids
stay local to the application transaction.

### Invariants And Boundaries

- Ambient evidence, never model input, identifies the caller.
- Dispatch-brief delivery is exact-pinned internally; ordinary messages are rebindable.
- A failed initial brief retires the unbriefed child instead of leaving a live unowned seat.
- Authorization follows architect→orchestrator→manager→leaf-role ownership.

### Todos

None.

## Docs References

No Domain Documentation source is configured; repository tests and the approved L19 task are the evidence.


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Dispatch performs contained-seat authorization and exact initial brief handling. | `dispatch_agent_tool` | mcp/src/agents_remember/application/structural/agent_tools.py:205-368 |
| Relationship messaging and lifecycle operations expose structural intent. | `message_parent_tool` | mcp/src/agents_remember/application/structural/agent_tools.py:573-578 |
| Focused tests exercise ambient routing, replacement, ambiguity, and exact-pin behavior. | `test_child_to_replacement_parent_is_resolved_by_task_containment` | mcp/tests/test_structural_agent_tools.py:134-241 |

## Cross-Repo References


## Update History
- 2026-08-14T06:30+02:00 — L23 final candidate review: structural dispatch now fails closed on
  stale task-derived lineage and requires a current candidate-bound route-review record before
  curator host creation. Verification remains closeout-owned.

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created for structural agent operations; replaces public exact-id orchestration operations rather than wrapping them as compatibility APIs.
