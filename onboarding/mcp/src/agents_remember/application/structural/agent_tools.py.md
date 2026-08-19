# mcp/src/agents_remember/application/structural/agent_tools.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/structural/agent_tools.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-19T22:32+02:00 |
| lastVerifiedCommitHash |  `b523f53b193e9783e7c7e6410c772e7d64d8df17`|
| lastVerifiedCommitDate |  2026-08-19T21:54:50+02:00|
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
or self relationships. `UnbriefedChild` keeps spawn/brief cleanup explicit. Since 260815-DAG-L13 the
manager-dispatch series bootstrap gates on the *effective* execution nature (a nature-less master is
atomic by default; organizational semantics exist only under an authored graph), and a bootstrap
blocked by the atomic-sequential landing lane surfaces as a failed `StructuralOutcome` whose detail
carries the blocked payload — lane owner plus legal next operations — instead of a raised refusal.

### Conventions

Public results expose the structural target plus operation status or delivery detail. Runtime ids
stay local to the application transaction.

### Invariants And Boundaries

- Ambient evidence, never model input, identifies the caller.
- Dispatch-brief delivery is exact-pinned internally; ordinary messages are rebindable.
- A failed initial brief retires the unbriefed child instead of leaving a live unowned seat.
- Authorization follows architect→orchestrator→manager→leaf-role ownership.
- The atomic-sequential lane block is surfaced as an ordering payload, not an exception.

### Todos

None.

## Docs References

No Domain Documentation source is configured; repository tests and the approved L19 task are the evidence.


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Dispatch performs contained-seat authorization and exact initial brief handling. | `dispatch_agent_tool` | mcp/src/agents_remember/application/structural/agent_tools.py:299-389 |
| Manager series bootstrap gates on the effective nature and surfaces a lane-blocked bootstrap as a structural outcome. | `_manager_series_bootstrap_refusal` | mcp/src/agents_remember/application/structural/agent_tools.py:419-484 |
| Relationship messaging and lifecycle operations expose structural intent. | `message_parent_tool` | mcp/src/agents_remember/application/structural/agent_tools.py:599-605 |
| Focused tests exercise ambient routing, replacement, ambiguity, and exact-pin behavior. | `test_child_to_replacement_parent_is_resolved_by_task_containment` | mcp/tests/test_structural_agent_tools.py:169-194 |

## Cross-Repo References


## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## Update History

- 2026-08-19T22:32+02:00 — 260815-DAG-L13: manager series bootstrap resolves the effective
  execution nature (nature-less masters default to atomic; organizational only under an authored
  graph), and an atomic-sequential lane-blocked bootstrap surfaces as a `StructuralOutcome`
  carrying the ordering payload instead of raising. Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.
- 2026-08-14T06:30+02:00 — L23 final candidate review: structural dispatch now fails closed on
  stale task-derived lineage and requires a current candidate-bound route-review record before
  curator host creation. Verification remains closeout-owned.

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created for structural agent operations; replaces public exact-id orchestration operations rather than wrapping them as compatibility APIs.
