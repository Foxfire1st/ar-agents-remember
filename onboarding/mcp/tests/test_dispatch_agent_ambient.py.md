# mcp/tests/test_dispatch_agent_ambient.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_dispatch_agent_ambient.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T16:03+02:00 |
| lastVerifiedCommitHash |  `c51373425be3e3f488590ad2f444810df89b4ffb`|
| lastVerifiedCommitDate |  2026-08-26T19:22:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The ambient caller-mode test cohort for `dispatch_agent`: proves that a caller with NO
plane-injected hosted identity (`AR_HOSTED_SESSION_ID` absent) spawns on a canonical task document
in ambient mode, that refusals stay intact, that provenance distinguishes ambient from plane, that
rollback fires only when the just-created generation is positively proven unbriefed, and that the
ambient brief post carries no plane sender. The suite was extracted verbatim from
`test_structural_agent_tools.py` by the
260821-ARSPAWN-L1 file-size fix (that suite had crossed the 1,200-line rail); the shared fixtures
came with it. Fix round 3 added a real-path cohort: direct `resolve_ambient_caller` unit tests, a
real spawn+brief success through the production primitive with a substituted host, a real rollback,
and the rollback failure-branch seams. Fix round 4 wired the real-path cohort to a real
settings-owned architect launch selection and asserted the terminated-row listing after rollback.
ARSPAWN-L2 additionally proves that a successful brief binds its durable receipt to the exact
catalog generation and that observer-log failure remains secondary after catalog retirement has
already fenced a failed spawn. The rollback test now injects failure at the actual
`OperatorInboxStore.append` persistence boundary, avoiding an obsolete filesystem-layout assumption.

## Code Commentary

The module keeps the `MCP_SRC` sys.path pin idiom used by the sibling structural suites so the
worktree package under test is importable regardless of the installed runtime.

The module-level fixtures are copied verbatim from `test_structural_agent_tools.py`: `_config`
(33) builds an isolated `McpRuntimeConfig` over a temporary root, `_task_doc` (43) constructs
minimal `TaskDocument` rows, `_write_topology` (57) materializes a real sprint/master/leaf task tree
(organizational sprint graph + atomic master + leaf), and `_seat` (111) builds a harness catalog
row for the plane-provenance and rollback cases. The real-path cohort adds three fixtures of its
own: `_detected` (137) stubs harness detection, `_write_architect_settings` (141) writes a
settings-owned architect launch selection (`orchestration.roles.architect` → claude /
claude-fable-5 / max) to the temp root's `system/settings.json` so the real spawn resolves
settings-owned knobs, and `_FakeHost` (163) records spawns and terminations without ever owning a
real tmux session.

`DispatchAgentAmbientTests` (194) drives `dispatch_agent_tool` directly. The original six
mock-based tests (moved verbatim from the structural suite):

- Ambient spawn on the canonical document without hosted env (203) — asserts `status=dispatched`,
  the `AR_SPAWN_ROLE` env, and `SpawnedBy.caller_kind == "ambient"` with no spawning session.
- Unknown task reference refuses BEFORE any spawn (237) — `task-document-not-found`, spawn not
  called.
- Role-altitude mismatch refuses BEFORE any spawn (256) — `seat-role-altitude-mismatch`, spawn not
  called; the ambient branch still validates role altitude via `topology.validate_role`.
- Plane dispatch keeps structural caller provenance (273) — with `AR_HOSTED_SESSION_ID` present,
  the structural path runs and records `caller_kind == "plane"` with the caller session.
- Ambient persistence-failure rollback (309) — when the exact initial brief cannot persist and the
  catalog positively identifies the matching ambient generation as still unbriefed, the
  just-spawned child is retired as a SYSTEM closure (`retire_entry` with edge
  `ambient-dispatch-rollback`) and `session_retire_tool` is never called.
- Ambient brief post without a plane sender (346) — the inbox poster carries no sender id/role and
  the dispatch-brief row stays exact-pinned to the spawned session.

The fix-round-3 real-path cohort (8 tests):

- `resolve_ambient_caller` unit tests (383, 387): plane identity present returns `None`; no plane
  identity returns `AmbientCaller` — pinning the ambient-first branch decider directly.
- Real spawn + brief success (394): the REAL spawn primitive and brief post run with the
  `_FakeHost` substituted host and the `_write_architect_settings`-backed settings (no
  primitive/brief mocks), proving the ambient path end to end.
- Real rollback (421): brief persistence failure retires the just-spawned child through
  `retire_entry` as a system closure; the assertion reads the catalog with
  `include_terminated=True` and requires exactly one row left, `status="terminated"`, matching the
  fake host's terminated list — the terminated-row listing after rollback.
- Recovery failure-branch seams (449, 473, 498, 528): a missing child row or already-terminated row
  leaves durable brief state unknown and refuses reconciliation without retiring anything;
  retirement raising or racing (`retire_entry` returning `None`) reports the narrower rollback
  failure after the matching unbriefed generation was positively identified.

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
- Missing, terminated, mismatched, or otherwise ambiguous catalog evidence never authorizes
  cleanup; only a faithfully attributed current generation with positive no-brief evidence may be
  retired by rollback.
- Durable catalog retirement is the rollback authority; a later observer-log failure cannot revive
  the generation.

## Docs References

No external domain source governs this repository-local test contract.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite materializes the same real task topology the structural suite uses. | `_write_topology` | mcp/tests/test_dispatch_agent_ambient.py:57-110 |
| The ambient caller-mode cohort (original six + real-path and receipt/recovery evidence). | `DispatchAgentAmbientTests` | mcp/tests/test_dispatch_agent_ambient.py:194-597 |
| The real-path fixtures: harness detection stub, settings-owned architect launch selection, and the recording fake host. | `_detected`; `_write_architect_settings`; `_FakeHost` | mcp/tests/test_dispatch_agent_ambient.py:137-140; mcp/tests/test_dispatch_agent_ambient.py:141-162; mcp/tests/test_dispatch_agent_ambient.py:163-193 |
| Ambient spawn without hosted env records `caller_kind="ambient"` with no session. | `test_ambient_dispatch_spawns_on_the_canonical_document_without_hosted_env` | mcp/tests/test_dispatch_agent_ambient.py:203-236 |
| Unknown ref and altitude-mismatch refusals fire before any spawn. | `test_ambient_dispatch_refuses_unknown_task_reference_before_spawn`; `test_ambient_dispatch_refuses_role_altitude_mismatch_before_spawn` | mcp/tests/test_dispatch_agent_ambient.py:237-255; mcp/tests/test_dispatch_agent_ambient.py:256-272 |
| The plane structural path keeps `caller_kind="plane"` provenance. | `test_plane_dispatch_keeps_structural_caller_provenance` | mcp/tests/test_dispatch_agent_ambient.py:273-308 |
| Brief-persistence failure retires a positively identified unbriefed child as a system closure. | `test_ambient_dispatch_persistence_failure_retires_the_unbriefed_child` | mcp/tests/test_dispatch_agent_ambient.py:309-345 |
| The ambient brief post carries no plane sender and binds its durable receipt. | `test_ambient_dispatch_persists_the_brief_without_a_plane_sender` | mcp/tests/test_dispatch_agent_ambient.py:346-382 |
| `resolve_ambient_caller` is unit-tested both ways (plane-present → None; ambient). | `test_resolve_ambient_caller_returns_none_when_plane_identity_is_present`; `test_resolve_ambient_caller_returns_ambient_without_plane_identity` | mcp/tests/test_dispatch_agent_ambient.py:383-386; mcp/tests/test_dispatch_agent_ambient.py:387-393 |
| The real spawn+brief path runs through the production primitive with a substituted host and settings-owned knobs. | `test_ambient_dispatch_runs_the_real_spawn_and_persists_the_brief` | mcp/tests/test_dispatch_agent_ambient.py:394-420 |
| Real rollback forces the actual inbox append seam, asserts the terminated-row listing, and keeps observer failure secondary after durable retirement. | `test_ambient_dispatch_rolls_back_via_system_closure_when_brief_persistence_fails`; `test_ambient_dispatch_rollback_preserves_an_observer_log_failure_as_secondary` | mcp/tests/test_dispatch_agent_ambient.py:421-451; mcp/tests/test_dispatch_agent_ambient.py:561-600 |
| Missing or already-terminal catalog evidence refuses reconciliation; rollback failures are reported only after positive unbriefed-generation proof. | `test_ambient_dispatch_refuses_rollback_when_the_child_row_is_missing`; `test_ambient_dispatch_refuses_rollback_when_the_child_is_already_terminated`; `test_ambient_dispatch_rollback_reports_when_retirement_raises`; `test_ambient_dispatch_rollback_reports_when_retirement_races` | mcp/tests/test_dispatch_agent_ambient.py:449-472; mcp/tests/test_dispatch_agent_ambient.py:473-497; mcp/tests/test_dispatch_agent_ambient.py:498-527; mcp/tests/test_dispatch_agent_ambient.py:528-557 |

## Cross-Repo References

No cross-repository boundary participates in this suite.

## Update History

- 2026-08-26T16:03+02:00 — Post-failure repair: rebound ambient rollback forcing to the real
  `OperatorInboxStore.append` commit boundary; removed reliance on an obsolete log path. No
  certifying test execution is claimed.


- 2026-08-25T22:27+02:00 — 260821-ARSPAWN-L2 final curation: corrected the recovery
  contract so unknown durable state refuses reconciliation and only positively proven unbriefed
  generations authorize rollback; refreshed final-candidate anchors. No test execution is claimed.

- 2026-08-25T19:51+02:00 — 260821-ARSPAWN-L2: successful ambient dispatch now proves receipt
  binding, and rollback proves observer-log failure is secondary after durable retirement.
  Verification remains closeout-owned.

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
