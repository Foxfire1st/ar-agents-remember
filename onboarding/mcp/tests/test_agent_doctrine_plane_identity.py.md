# mcp/tests/test_agent_doctrine_plane_identity.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `mcp/tests/test_agent_doctrine_plane_identity.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash |  `e5cb139f66abbd6502d4dcc4be883eb5f49770fe`|
| lastVerifiedCommitDate |  2026-08-21T00:28:23+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Machine-enforces the ban on agent instructions that require models to retain or submit
control-plane identifiers, and pins packaged lifecycle doctrine to the canonical source exactly.

## Code Commentary

### Logic

The test enumerates all agent instruction files, rejects forbidden id-addressing phrases, and
compares the packaged lifecycle tree byte-for-byte with the canonical skill tree.

### Conventions

The phrase set is intentionally narrow and architectural; legitimate plane-internal source and
historical provenance are outside this agent-instruction scan.

### Invariants And Boundaries

- Public doctrine cannot regress to exact agent/session/lifecycle targeting.
- Packaged runtime doctrine cannot drift from the canonical source.

### Todos

None.

## Docs References


## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The tests scan canonical instructions and compare packaged copies. | `test_agent_doctrine_contains_no_control_plane_address_instructions` | mcp/tests/test_agent_doctrine_plane_identity.py:37-63 |

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

## Update History

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
