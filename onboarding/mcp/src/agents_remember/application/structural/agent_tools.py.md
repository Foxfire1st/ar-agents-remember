# mcp/src/agents_remember/application/structural/agent_tools.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/structural/agent_tools.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:51+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
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

Since 260821-ARSPAWN-L1 `dispatch_agent_tool` resolves the caller by kind through
`_resolve_dispatch_caller`, which is AMBIENT-FIRST (fix round 3): `resolve_ambient_caller` decides
the branch from the same environ — no plane identity (`AR_HOSTED_SESSION_ID` absent) selects the
ambient branch, which still validates the role against the document altitude via
`topology.validate_role` (`seat-role-altitude-mismatch` / `seat-role-unsupported` survive) and
spawns with `SpawnedBy(caller_kind="ambient")`; with plane identity present the plane path runs
`resolve_ambient_seat` + `resolver.authorize_child` unchanged, and stale/invalid/mismatched/
unbound plane identity refuses — never a silent downgrade. The earlier both-fail defensive guard
was removed as dead code: the two resolutions read the same environ, so exactly one branch applies
and fail-closed behavior is unchanged. Plane spawns pass `caller_kind="plane"` explicitly. A failed ambient initial brief retires the
just-spawned child as a SYSTEM closure (`retire_entry` with `by_session=None`, edge
`ambient-dispatch-rollback`, actor `system`) — the child id is the spawn result, never caller
input, so an ambient caller cannot retire an arbitrary session; plane rollback stays
`session_retire_tool`-gated. `StructuralMessageContext.sender` is optional so the ambient brief
post carries no sender (`_signal_route`/`derive_signal_owner` tolerate a `None` sender;
dispatch-brief rows stay exact-pinned). `_level_for_role` maps
architect/orchestrator/strategist/designer/system-specialist to `portfolio`, so an ambient
architect spawn records `spawn_level=portfolio` (a vocabulary decision for the L3 leaf if the
l-01 doctrine wants sprint-level seats at another level).

### Conventions

Public results expose the structural target plus operation status or delivery detail. Runtime ids
stay local to the application transaction.

### Invariants And Boundaries

- Ambient evidence, never model input, identifies the caller.
- Dispatch-brief delivery is exact-pinned internally; ordinary messages are rebindable.
- A failed initial brief retires the unbriefed child instead of leaving a live unowned seat.
- Authorization follows architect→orchestrator→manager→leaf-role ownership.
- The atomic-sequential lane block is surfaced as an ordering payload, not an exception.
- No plane identity means an ambient caller, never a fallback: a stale, invalid, mismatched, or
  unbound plane identity refuses instead of silently downgrading.
- Ambient rollback is a system closure bounded to the spawn result — an ambient caller cannot
  retire an arbitrary session.

### Todos

None.

## Docs References

No Domain Documentation source is configured; repository tests and the approved L19 task are the evidence.


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Dispatch performs contained-seat authorization and exact initial brief handling, now by caller kind (plane vs ambient). | `dispatch_agent_tool`; `_resolve_dispatch_caller` | mcp/src/agents_remember/application/structural/agent_tools.py:338-487 |
| Manager series bootstrap gates on the effective nature and surfaces a lane-blocked bootstrap as a structural outcome. | `_manager_series_bootstrap_refusal` | mcp/src/agents_remember/application/structural/agent_tools.py:512-576 |
| Relationship messaging and lifecycle operations expose structural intent. | `message_parent_tool` | mcp/src/agents_remember/application/structural/agent_tools.py:692-697 |
| Focused tests exercise ambient routing, replacement, ambiguity, and exact-pin behavior. | `test_child_to_replacement_parent_is_resolved_by_task_containment` | mcp/tests/test_structural_agent_tools.py:169-194 |
| Rollback retires an unbriefed child as the authority-gated actor (plane) or a system closure (ambient). | `_retire_unbriefed_child` | mcp/src/agents_remember/application/structural/agent_tools.py:217-265 |

## Cross-Repo References


## 260815-DAG-L4 Authority Boundary

L4 routes this file's existing application, configuration, task, model, registration, or memory responsibility through the shared task-derived integration authority. The change preserves the file's owning altitude while ensuring protected code and external-memory refs cannot be mutated through an ordinary workbench or unjournaled helper.

## Update History

- 2026-08-24T00:51+02:00 — No content impact: 260821-CLIVE-L2 the source only repoints the startup import and extracts the existing post-spawn briefing statements into `_brief_spawned_child`; dispatch ordering and documented child-briefing behavior are unchanged. Verified at code commit `1d446724`.

- 2026-08-21T03:45+02:00 — 260821-ARSPAWN-L1 fix round 3: `_resolve_dispatch_caller` restructured ambient-first — `resolve_ambient_caller` decides the branch directly (no plane identity → ambient with role-altitude validation; plane identity → `resolve_ambient_seat` + `authorize_child`, any refusal never downgrades); the both-fail defensive guard was removed as dead code (same environ). Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1: `dispatch_agent_tool` resolves the caller by kind through `_resolve_dispatch_caller` — plane seats keep `resolve_ambient_seat` + `authorize_child` unchanged; only `ambient-seat-unavailable` downgrades to the ambient branch (role altitude still validated); stale/invalid/mismatched/unbound plane identity refuses instead of downgrading. Plane spawns pass `caller_kind="plane"`; ambient rollback retires the unbriefed child as a system closure (`retire_entry`, `by_session=None`, edge `ambient-dispatch-rollback`, actor `system`) bounded to the spawn result; `StructuralMessageContext.sender` is optional so the ambient brief post carries no sender. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: manager series bootstrap resolves the effective
  execution nature (nature-less masters default to atomic; organizational only under an authored
  graph), and an atomic-sequential lane-blocked bootstrap surfaces as a `StructuralOutcome`
  carrying the ordering payload instead of raising. Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.
- 2026-08-14T06:30+02:00 — L23 final candidate review: structural dispatch now fails closed on
  stale task-derived lineage and requires a current candidate-bound route-review record before
  curator host creation. Verification remains closeout-owned.

- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created for structural agent operations; replaces public exact-id orchestration operations rather than wrapping them as compatibility APIs.
