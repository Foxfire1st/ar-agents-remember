# mcp/tests/test_spawn_agent_session.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_spawn_agent_session.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-31T12:00+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

This suite covers the trusted low-level hosted-session spawn primitive with fake hosts, runner logs,
and task topology. It proves spawn/binding behavior without granting model-facing access to the
runtime-id operation.

## Code Commentary

The `call_spawn` shim constructs the typed internal seat, provenance, retired-input, and override
objects used by `spawn_agent_session_payload`. Successful harness spawn requires a real canonical
task-document reference and role, binds the seat, and makes no brief-readiness claim. Task content
and submit requests are refused at this primitive because the public `dispatch_agent` transaction
owns exact-pinned brief delivery. The refusal points callers to that one public transaction and
does not expose the old multi-step readiness, inbox-message, or adapter-delivery recipe.

The suite also covers seat conflict without takeover, missing/invalid task documents before spawn,
settings-owned harness/model/effort resolution, plain-terminal separation, log-confirmed session
commands, and stored private provenance. No test turns the primitive into an advertised agent tool.
260821-ARSPAWN-L1 extends `_SPAWNED_BY_FIELDS` with the caller-kind field and adds
`test_spawn_records_caller_kind_provenance`, which runs the REAL primitive with a substituted host
and asserts the payload carries `spawnedByKind` ("ambient") plus the catalog caller-kind row — the
provenance the public `dispatch_agent` sets by caller kind.
Reviewer forcing supplies both settings-owned launch selection and the exact manager parent pair,
while the stale-super matrix confirms lineage refusal wins before a missing reviewer-parent or
launch-selection error and before host creation.

## Invariants And Boundaries

- Harness spawn requires canonical task-document identity and a role-compatible seat.
- A live document+role occupant is never silently replaced.
- Spawn does not deliver task content or claim readiness.
- Caller-supplied spend/launch overrides fail before side effects.
- Tests use fakes and temporary roots; no real tmux, daemon, or sleep is involved.

## Docs References

No external domain source governs this repository-local test contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite exercises the internal typed spawn composition. | `call_spawn` | mcp/tests/test_spawn_agent_session.py:89-109 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| A successful spawn binds a seat without delivering a brief or claiming readiness. | `test_spawns_bound_seat_without_brief_or_readiness_claim` | mcp/tests/test_spawn_agent_session.py:318-339 |
| The spawn payload and catalog row carry caller-kind provenance. | `test_spawn_records_caller_kind_provenance` | mcp/tests/test_spawn_agent_session.py:555-561 |
| Canonical task-document identity is persisted and missing documents refuse before spawn. | `test_spawn_persists_canonical_task_document_reference`; `test_spawn_rejects_missing_task_document_before_spawning` | mcp/tests/test_spawn_agent_session.py:383-389; mcp/tests/test_spawn_agent_session.py:402-409 |
| Context and submit inputs are rejected at the spawn primitive. | `test_context_including_empty_string_refuses_before_every_spawn_side_effect`; `test_submit_true_refuses_before_spawn_even_without_context` | mcp/tests/test_spawn_agent_session.py:449-470; mcp/tests/test_spawn_agent_session.py:472-476 |
| Occupied structural seats refuse without takeover. | `test_seat_taken_is_surfaced_never_overridden` | mcp/tests/test_spawn_agent_session.py:484-518 |

## L23 Pre-Host Spawn Refusal

Spawn fixtures now use a current contract chain, and the dedicated stale-super
case advances the real repository before requesting each leaf role: worker, reviewer, and curator.
Every role receives the public `source-lineage-stale` projection while host creation and catalog
insertion remain untouched. This is the control-plane race closure behind the manager's pre-curator
status check: dispatch re-proves lineage rather than trusting a brief-carried snapshot.

## Update History

- 2026-08-31T12:00+02:00 — A005 repair aligned reviewer fixtures with mandatory explicit parent
  provenance and settings ownership while preserving stale-lineage as the first actionable refusal.
  Verification remains closeout-owned.

- 2026-08-31T09:02+02:00 — 260821-ARSPAWN-L5 A005 citation reconciliation refreshed
  source ranges after the reviewed spawn suite moved; no semantic onboarding claim changed.
  Verification remains closeout-owned.

- 2026-08-30T13:59+02:00 — 260821-ARSPAWN-L3 replaced the stale low-level brief-delivery recipe
  assertion with forcing proof that the internal primitive refuses before side effects and directs
  callers to the one public `dispatch_agent` transaction. Verification remains closeout-owned.

- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1: `_SPAWNED_BY_FIELDS` + `test_spawn_records_caller_kind_provenance` prove the real primitive writes the `spawnedByKind` payload and the catalog caller-kind row. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-16T04:06+02:00 — Dagger fixture repair: stale-lineage session forcing advances the exact sprint-super ref, then restores the ambient main checkout before role launch.
- 2026-08-13T12:53+02:00 — No content impact: the stabilized daemon-root derivation reads
  `sys.modules["agents_remember"].__file__` after normal package submodule imports. Spawn and
  all-leaf-role lineage assertions are unchanged, and no Ruff config exception remains. This
  supersedes the 12:26 import-shape note; provenance stays closeout-owned.

- 2026-08-13T12:26+02:00 — No content impact: the final Ruff-safe form imports
  `agents_remember.__file__` directly as `agents_remember_file` when deriving the same daemon
  package root. The already-documented all-leaf-role lineage refusal and every spawn assertion are
  unchanged; verification provenance remains closeout-owned.
- 2026-08-13T08:47+02:00 — L23 integration-gate repair: expanded the pre-host stale-super refusal across worker, reviewer, and curator, proving curator dispatch cannot create a process after lineage moves. Verification metadata remains closeout-owned.

- 2026-08-12T20:10+02:00 — L23 curator: documented real-Git pre-host lineage refusal coverage; verification remains closeout-owned.

- 2026-08-12T08:41+02:00 — No content impact: 260731-EFA-L20 removed redundant task-reference inference from the helper whose callers already supply canonical references; spawn behavior and assertions are unchanged.
- 2026-08-11T12:15+02:00 — Reframed the suite around the current trusted spawn primitive,
  task-document binding, and separate exact-pinned brief delivery. Verification remains pinned
  pending governed closeout.
- 2026-07-04T11:10+02:00 — Through 2026-08-08, coverage accumulated for settings-owned launch selection,
  capture/log evidence, binding conflicts, role provenance, plain terminals, and typed helpers.
