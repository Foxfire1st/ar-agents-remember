# mcp/tests/test_seat_independent_execution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_seat_independent_execution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

End-to-end behavioral test suite for the L16 seat-independent task-execution fallback
(L16-R2/R3/R4/R5): an ambient-context closeout declare/grade/select/closeout lifecycle drives the
real public production boundary over a real coordination root, and the structural gate-tools
fallback branches are exercised at the `_context` level.

## Code Commentary

### Logic

`AmbientCloseoutQueueTests` drives the real `closeout_queue` boundary through
`closeout_queue_tool` with an ambient (non-seat) caller: a full declare → set-grade → select →
closeout lifecycle works (`test_ambient_declared_caller_runs_declare_grade_select_closeout`); an
ambient declared orchestrator acquires an atomic blocker
(`test_ambient_declared_caller_acquires_an_atomic_blocker`); the declared identity is validated
like a seat (`test_ambient_declared_identity_is_validated_like_a_seat`); a missing declared caller
refuses `closeout-queue-caller-required`; a hosted seat still wins over a matching declared caller;
and a non-`ambient-seat-unavailable` seat error reraises wrapped.
`DeclaredCallerModelTests` pin the blank-role refusal and role stripping.

`AmbientStructuralGateFallbackTests` (the wave-2 F1 fix) drive the real `_context` fallback
branches of `application/structural/gate_tools.py`: missing caller → `structural-caller-required`;
seat contradiction → `structural-caller-conflict`; the duck-typed `DeclaredGateCaller` passes
`_authorize_gate_target` → `authorize_child` (an orchestrator on a manager doc passes, a worker is
refused); `structural_lifecycle_gate_tool` raises on the declared document; non-unavailable seat
errors reraise; a hosted seat without a declared caller is unchanged. `_decide_context` and
`structural_gate_decide_tool`/`structural_gate_list_tool` cover the decide/list full branches via
declared callers.

### Conventions

Behavioral tests, not wiring-only: they exercise the fallback decision branches (absent caller,
conflict, duck-typed authorization) rather than patching payload builders. Uses real scratch
coordination roots (git repos, contracts, registers, worktree trees).

### Invariants And Boundaries

- The closeout lifecycle end-to-end proof uses the real production boundary (L16-R5).
- Seat-path regressions stay covered by the unchanged suite family (e.g.
  `test_closeout_queue_forcing.py`); this file covers the ambient path.
- Tests never mutate a real coordination root.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The ambient closeout lifecycle end-to-end. | `test_ambient_declared_caller_runs_declare_grade_select_closeout` | mcp/tests/test_seat_independent_execution.py:89-132 |
| Declared identity is validated like a seat. | `test_ambient_declared_identity_is_validated_like_a_seat` | mcp/tests/test_seat_independent_execution.py:159-176 |
| Gate fallback behavioral branches (required/conflict/authorize). | `AmbientStructuralGateFallbackTests` | mcp/tests/test_seat_independent_execution.py:222-343 |
| The fallback under test. | `_context`; `_declared_queue_actor` | mcp/src/agents_remember/application/structural/gate_tools.py:48-71; mcp/src/agents_remember/application/closeout_queue.py:61-71 |

## Cross-Repo References

No meaningful cross-repository reference applies.

## 260815-DAG Master Full-Gate Repair

The 260815-DAG master full-gate repair moved the queue imports under `worktrees/queue/`
(`closeout_queue`, `closeout_queue_lifecycle`). `AmbientCloseoutQueueTests` gained
`test_ambient_declared_caller_acquires_an_atomic_blocker`, proving an ambient declared orchestrator
can acquire an atomic blocker with a rationale after its predecessor master completes (the ready
lane then carries the blocked leaf), and the `_ambient` payload builder now forwards `rationale`.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: queue imports moved under
  `worktrees/queue/`; `AmbientCloseoutQueueTests` gained the ambient atomic-blocker acquisition test
  and the payload builder forwards `rationale`. Verified at code commit e5cb139f.
- 2026-08-20T09:35+02:00 — 260815-DAG-L16: created for L16-R5 (ambient end-to-end lifecycle)
  and the wave-2 F1 fold (real behavioral gate fallback tests). Verified at code commit a9d50e08.
