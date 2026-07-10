# mcp/src/agents_remember/controlplane/orphan_policy.py

| Field                  | Value                                                             |
| ---------------------- | ------------------------------------------------------------------ |
| repository             | agents-remember                                                    |
| path                   | `mcp/src/agents_remember/controlplane/orphan_policy.py`             |
| doc_type               | `file-level-onboarding`                                            |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash | `e400ed0ce98752d1b65d00de97c9b84c7ea20814`                           |
| lastVerifiedCommitDate | 2026-07-10T20:04:45+02:00|
| governingOverview      | `overview.md`                                                      |

## Governing Overview

[overview.md](overview.md)

## Purpose

R3 (260707-HFX2-L4): the orphan-workers detection hook for a dead manager's still-running workers.
Deliberately a stub/hook per this leaf's explicit scope allowance, not an auto-reparent action:
when a manager seat is respawned or found dead, its live worker seats do NOT auto re-parent to the
successor and do NOT absorb the manager's role (R4 doctrine, HFX-L6 capture hardening). This module
only finds and surfaces the orphaned set; the caller decides what happens to it.

## Code Commentary

### 260707-HFX2-L17 Binding-Role Worker Discovery

Orphan discovery now classifies current worker seats by `binding_role`, so a hand-opened session
explicitly attached as worker and a session rebound from stale provenance participate correctly.
Spawner provenance remains the parent edge used to identify the dead manager.

### Logic

`find_orphaned_workers(catalog, *, manager_agent_id)` — a pure catalog read: every catalog row with
`spawn_role == "worker"`, `spawned_by_session == manager_agent_id`, and `status == "running"`. No
mutation, no signal post — `serving/supervisor.py`'s `_respawn_suspect` is the caller that gathers
this list once a manager seat is confirmed suspect/retired and surfaces it in the respawn directive
event (`orphanedWorkers`).

### Conventions

Single pure function module, matching `signal_routing.py`'s "derivation only, no I/O" shape.

### Invariants And Boundaries

- **Detection/surfacing only — no re-parent action exists here or anywhere in this leaf.** The
  orchestrator receiving the respawn-directive signal (which carries the orphan list) decides
  whether to re-parent each worker to a respawned manager or let them run to their own
  turn-report/completion under no manager.
- Orphaned workers are never auto-absorbed into any other seat's role (R4 doctrine).
- A pure catalog read: never mutates the catalog, never posts a signal itself.

### Todos

A future leaf may wire an actual re-parent action on top of this detection hook (documented in the
module's own docstring as an explicit, not-yet-scoped follow-up) — not a defect in this leaf.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation; the leaf
task doc's R3 scope allowance ("a stub/hook is sufficient scope for this leaf") is the source of
truth for this module's deliberately narrow surface.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document defines orphan-worker policy; the leaf task doc's R3 scope note is authoritative. | L1-L32 | [orphan_policy.py](orphan_policy.py) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The sole caller: gathers the orphan list once a manager seat is retired as suspect and surfaces it in the respawn observer event. | `_respawn_suspect` | [../serving/supervisor.py](../serving/supervisor.py.md) |
| Unit test: running workers of the named manager are returned; a terminated sibling and another manager's worker are excluded. | `test_finds_running_workers_of_the_named_manager` | [test_escalation_ladder.py](../../../tests/test_escalation_ladder.py.md) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Same-repository control-plane logic only. | — | — |

## Update History

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: moved current worker classification to binding role
  while retaining spawned-by provenance for parentage.

- 2026-07-08T23:15+02:00 — Created for 260707-HFX2-L4 (R3, orphan policy): `find_orphaned_workers` —
  a pure catalog read for a dead/respawned manager's still-running worker seats, wired into
  `serving/supervisor.py::_respawn_suspect`'s respawn event (`orphanedWorkers`). Detection/surfacing
  only, per the leaf's explicit scope allowance — no auto-reparent action exists yet. Verification
  metadata pinned until closeout stamps the 260707-HFX2-L4 commit.
