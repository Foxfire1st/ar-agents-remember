# mcp/tests/test_dispatch_agent_ambient.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_dispatch_agent_ambient.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T04:00+02:00 |
| lastVerifiedCommitHash | `3eafc555c848ac45a07a07720641f1735f8df0eb` |
| lastVerifiedCommitDate | 2026-08-21T05:15:52+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The ambient caller-mode test cohort for `dispatch_agent`: proves that a caller with NO
plane-injected hosted identity (`AR_HOSTED_SESSION_ID` absent) spawns on a canonical task document
in ambient mode, that refusals stay intact, that provenance distinguishes ambient from plane, that
rollback fires when the initial brief cannot persist, and that the ambient brief post carries no
plane sender. The suite was extracted verbatim from `test_structural_agent_tools.py` by the
260821-ARSPAWN-L1 file-size fix (that suite had crossed the 1,200-line rail); the shared fixtures
came with it. Fix round 3 added a real-path cohort: direct `resolve_ambient_caller` unit tests, a
real spawn+brief success through the production primitive with a substituted host, a real rollback,
and the rollback failure-branch seams. Fix round 4 wired the real-path cohort to a real
settings-owned architect launch selection and asserted the terminated-row listing after rollback.

## Code Commentary

The module keeps the `MCP_SRC` sys.path pin idiom used by the sibling structural suites so the
worktree package under test is importable regardless of the installed runtime.

The module-level fixtures are copied verbatim from `test_structural_agent_tools.py`: `_config`
(33) builds an isolated `McpRuntimeConfig` over a temporary root, `_task_doc` (43) constructs
minimal `TaskDocument` rows, `_write_topology` (57) materializes a real sprint/master/leaf task tree
(organizational sprint graph + atomic master + leaf), and `_seat` (111) builds a harness catalog
row for the plane-provenance and rollback cases. The real-path cohort adds three fixtures of its
own: `_detected` (135) stubs harness detection, `_write_architect_settings` (139) writes a
settings-owned architect launch selection (`orchestration.roles.architect` → claude /
claude-fable-5 / max) to the temp root's `system/settings.json` so the real spawn resolves
settings-owned knobs, and `_FakeHost` (161) records spawns and terminations without ever owning a
real tmux session.

`DispatchAgentAmbientTests` (192) drives `dispatch_agent_tool` directly. The original six
mock-based tests (moved verbatim from the structural suite):

- Ambient spawn on the canonical document without hosted env (201) — asserts `status=dispatched`,
  the `AR_SPAWN_ROLE` env, and `SpawnedBy.caller_kind == "ambient"` with no spawning session.
- Unknown task reference refuses BEFORE any spawn (235) — `task-document-not-found`, spawn not
  called.
- Role-altitude mismatch refuses BEFORE any spawn (254) — `seat-role-altitude-mismatch`, spawn not
  called; the ambient branch still validates role altitude via `topology.validate_role`.
- Plane dispatch keeps structural caller provenance (271) — with `AR_HOSTED_SESSION_ID` present,
  the structural path runs and records `caller_kind == "plane"` with the caller session.
- Ambient persistence-failure rollback (307) — when the exact initial brief cannot persist, the
  just-spawned child is retired as a SYSTEM closure (`retire_entry` with edge
  `ambient-dispatch-rollback`) and `session_retire_tool` is never called.
- Ambient brief post without a plane sender (344) — the inbox poster carries no sender id/role and
  the dispatch-brief row stays exact-pinned to the spawned session.

The fix-round-3 real-path cohort (8 tests):

- `resolve_ambient_caller` unit tests (375, 379): plane identity present returns `None`; no plane
  identity returns `AmbientCaller` — pinning the ambient-first branch decider directly.
- Real spawn + brief success (386): the REAL spawn primitive and brief post run with the
  `_FakeHost` substituted host and the `_write_architect_settings`-backed settings (no
  primitive/brief mocks), proving the ambient path end to end.
- Real rollback (413): brief persistence failure retires the just-spawned child through
  `retire_entry` as a system closure; the assertion reads the catalog with
  `include_terminated=True` and requires exactly one row left, `status="terminated"`, matching the
  fake host's terminated list — the terminated-row listing after rollback.
- Rollback failure-branch seams (441, 465, 490, 520): missing child row, already-terminated child,
  retirement raising, and retirement racing (`retire_entry` returning `None`) each report
  "child retirement also failed" without crashing the dispatch.

## Invariants And Boundaries

- Tests use fakes, a substituted host, and temporary roots only; no real tmux, daemon, or hosted
  session is involved.
- Ambient spawns assert `caller_kind="ambient"` and no spawning session; the plane case asserts
  `caller_kind="plane"` with the caller session — the provenance distinction L1-R6 requires.
- Refusal paths assert `spawn.assert_not_called()` so a fail-open regression cannot pass silently.
- The rollback case asserts `session_retire_tool.assert_not_called()` — ambient rollback must stay a
  system closure, never an authority-gated actor retire.
- The real-path cohort keeps the same temporary-root confinement while exercising the production
  primitive through the substituted host and a settings-owned architect launch selection.

## Docs References

No external domain source governs this repository-local test contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite materializes the same real task topology the structural suite uses. | `_write_topology` | mcp/tests/test_dispatch_agent_ambient.py:57-110 |
| The ambient caller-mode cohort (original six + real-path cohort). | `DispatchAgentAmbientTests` | mcp/tests/test_dispatch_agent_ambient.py:192-549 |
| The real-path fixtures: harness detection stub, settings-owned architect launch selection, and the recording fake host. | `_detected`; `_write_architect_settings`; `_FakeHost` | mcp/tests/test_dispatch_agent_ambient.py:135-138; mcp/tests/test_dispatch_agent_ambient.py:139-160; mcp/tests/test_dispatch_agent_ambient.py:161-191 |
| Ambient spawn without hosted env records `caller_kind="ambient"` with no session. | `test_ambient_dispatch_spawns_on_the_canonical_document_without_hosted_env` | mcp/tests/test_dispatch_agent_ambient.py:201-234 |
| Unknown ref and altitude-mismatch refusals fire before any spawn. | `test_ambient_dispatch_refuses_unknown_task_reference_before_spawn`; `test_ambient_dispatch_refuses_role_altitude_mismatch_before_spawn` | mcp/tests/test_dispatch_agent_ambient.py:235-253; mcp/tests/test_dispatch_agent_ambient.py:254-270 |
| The plane structural path keeps `caller_kind="plane"` provenance. | `test_plane_dispatch_keeps_structural_caller_provenance` | mcp/tests/test_dispatch_agent_ambient.py:271-306 |
| Brief-persistence failure retires the unbriefed child as a system closure. | `test_ambient_dispatch_persistence_failure_retires_the_unbriefed_child` | mcp/tests/test_dispatch_agent_ambient.py:307-343 |
| The ambient brief post carries no plane sender. | `test_ambient_dispatch_persists_the_brief_without_a_plane_sender` | mcp/tests/test_dispatch_agent_ambient.py:344-374 |
| `resolve_ambient_caller` is unit-tested both ways (plane-present → None; ambient). | `test_resolve_ambient_caller_returns_none_when_plane_identity_is_present`; `test_resolve_ambient_caller_returns_ambient_without_plane_identity` | mcp/tests/test_dispatch_agent_ambient.py:375-378; mcp/tests/test_dispatch_agent_ambient.py:379-385 |
| The real spawn+brief path runs through the production primitive with a substituted host and settings-owned knobs. | `test_ambient_dispatch_runs_the_real_spawn_and_persists_the_brief` | mcp/tests/test_dispatch_agent_ambient.py:386-412 |
| Real rollback asserts the terminated-row listing via `include_terminated=True`; its failure-branch seams report cleanly. | `test_ambient_dispatch_rolls_back_via_system_closure_when_brief_persistence_fails`; `test_ambient_dispatch_rollback_reports_a_missing_child_row`; `test_ambient_dispatch_rollback_accepts_an_already_terminated_child`; `test_ambient_dispatch_rollback_reports_when_retirement_raises`; `test_ambient_dispatch_rollback_reports_when_retirement_races` | mcp/tests/test_dispatch_agent_ambient.py:413-440; mcp/tests/test_dispatch_agent_ambient.py:441-464; mcp/tests/test_dispatch_agent_ambient.py:465-489; mcp/tests/test_dispatch_agent_ambient.py:490-519; mcp/tests/test_dispatch_agent_ambient.py:520-549 |

## Cross-Repo References

No cross-repository boundary participates in this suite.

## Update History

- 2026-08-21T04:00+02:00 — 260821-ARSPAWN-L1 fix round 4: the real-path cohort now runs against a
  settings-owned architect launch selection (`_write_architect_settings` → temp `system/settings.json`)
  with the `_FakeHost`/`_detected` fixtures, and the real rollback asserts the terminated-row
  listing (`catalog.list(include_terminated=True)`, exactly one `terminated` row matching the fake
  host); reference ranges refreshed for the shifted layout (552 lines). Verification metadata pinned
  until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-21T03:45+02:00 — 260821-ARSPAWN-L1 fix round 3: the suite grew to 526 lines with the
  real-path cohort — `resolve_ambient_caller` unit tests, real spawn+brief success, real rollback,
  and the rollback failure-branch seams; reference ranges refreshed for the shifted layout.
  Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-21T03:15+02:00 — 260821-ARSPAWN-L1 fix round 1: created for the new source file after
  the file-size fix moved the six ambient dispatch tests verbatim out of
  `test_structural_agent_tools.py`; the structural suite's card records the relocation. Verification
  metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.