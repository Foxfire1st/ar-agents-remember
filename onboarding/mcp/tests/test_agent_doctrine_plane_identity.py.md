# mcp/tests/test_agent_doctrine_plane_identity.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/tests/test_agent_doctrine_plane_identity.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-30T12:34+02:00 |
| lastVerifiedCommitHash |  `f9f92ca793811b6cb738d7e302dfecdf8636e96e`|
| lastVerifiedCommitDate |  2026-08-30T14:26:46+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Machine-enforces the ban on agent instructions that require models to retain or submit
control-plane identifiers, rejects caller-facing advertisement of the internal spawn primitive,
requires every role table to state its dispatch caller context, forces the launcher matrix across
canonical surfaces, and pins packaged lifecycle doctrine to the canonical source exactly.

## Code Commentary

### Logic

The test enumerates all agent instruction files, rejects forbidden id-addressing phrases, scans
caller-facing roots for `spawn_agent_session`, compares the packaged lifecycle tree byte-for-byte
with the canonical skill tree, and checks all nine role tables against the adopted plane/ambient/
target-only context matrix. A parameterized launcher check requires `dispatch_agent`, plane,
ambient, brief, and an explicit no-fallback statement in each canonical advertisement surface.
Additional forcing rows require ordinary architect bootstrap to remain distinct from explicit
task-seat takeover, make source-lineage conflict continuation visible, and prevent dispatch/tools
authority rows from being presented as settings keys.

### Conventions

The phrase set is intentionally narrow and architectural; legitimate plane-internal source and
historical provenance are outside this agent-instruction scan.

### Invariants And Boundaries

- Public doctrine cannot regress to exact agent/session/lifecycle targeting.
- Packaged runtime doctrine cannot drift from the canonical source.
- The internal primitive cannot reappear as caller guidance, and no role may omit its caller
  context or blur a plane refusal into ambient authority.

### Todos

None.

## Docs References


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The tests scan canonical instructions and compare packaged copies. | `test_agent_doctrine_contains_no_control_plane_address_instructions` | mcp/tests/test_agent_doctrine_plane_identity.py:74-81 |
| Caller-facing instructions reject the internal primitive and every role table carries its exact caller context. | `test_caller_facing_instructions_never_advertise_internal_spawn_primitive`; `test_every_role_tool_table_states_its_dispatch_caller_context` | mcp/tests/test_agent_doctrine_plane_identity.py:99-118 |

## Cross-Repo References


## 260815-DAG-L2 Doctrine Forcing

The suite now forces the complete dependency-aware doctrine across the canonical lifecycle root,
roles, criteria, and dispatch/handover/verdict templates. It asserts organizational/atomic lineage,
architect plan ownership, explicit fact/judgment registers, ready-frontier authority, pre-landing
master gates, leaf-only repair routing, and every installed/runtime copy's exact parity. A retired-
phrase sweep rejects the fixed-master/workbench topology, and a delimiter check keeps the changed
Markdown templates rectangular.

## 260815-DAG Master Full-Gate Repair

`test_execution_topology_doctrine_assigns_fact_judgment_and_queue_ownership` was restructured
into per-doctrine-file assertion helpers (`_assert_architect_doctrine`,
`_assert_strategist_doctrine`, `_assert_orchestrator_doctrine`, `_assert_manager_doctrine`,
`_assert_reviewer_doctrine`, `_assert_orchestration_task_doctrine`,
`_assert_manager_brief_doctrine`) that the test composes; the asserted term sets and the
lifecycle/worker/handover/verdict/criteria checks are unchanged. Import paths are untouched.

## PDLS Reconciliation

Doctrine-plane assertions now reflect the current lifecycle skill and role ownership without preserving superseded task/orchestration aliases.

The test continues to exercise production-owned behavior. No diagnostic result is treated as
certifying evidence and no fallback or threshold exception was introduced.

## Update History

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 added forcing coverage for the public vocabulary
  purge, ordinary-bootstrap-versus-takeover split, resumable lineage conflicts, fixed structural
  rows, and the complete caller-kind matrix. Verification remains closeout-owned.

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: refactored the topology doctrine
  test into per-file assertion helpers with identical asserted terms. Verified at code commit
  e5cb139f.

- 2026-08-19T22:32+02:00 — No content impact: 260815-DAG-L13 re-pointed one expected doctrine
  string from `migrate_execution_topology` to `author_execution_graph`; the scan and parity
  contract this card documents are unchanged. Verification remains closeout-owned.

- 2026-08-18T09:10+02:00 — No content impact: renamed the atomic 'barrier' concept to 'blocker' throughout; behavior unchanged. Verification remains closeout-owned.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: expanded doctrine-plane forcing to cover topology,
  authority, sync parity, retired phrases, and rectangular templates. Verification remains
  closeout-owned.

- 2026-08-12T08:41+02:00 — No content impact: 260731-EFA-L20 replaced the temporary findings accumulator with direct per-file assertions; the doctrine and canonical/package identity contract documented above is unchanged.
- 2026-08-11T06:47+02:00 — 260731-EFA-L19: created for the public doctrine/runtime-id machine guard.
