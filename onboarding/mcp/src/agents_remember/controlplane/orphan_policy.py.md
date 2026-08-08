# mcp/src/agents_remember/controlplane/orphan_policy.py

| Field                  | Value                                                             |
| ---------------------- | ------------------------------------------------------------------ |
| repository             | agents-remember                                                    |
| path                   | `mcp/src/agents_remember/controlplane/orphan_policy.py`             |
| doc_type               | `file-level-onboarding`                                            |
| lastUpdated            | 2026-08-02T01:42+02:00 |
| lastVerifiedCommitHash | `1c1629fc97dd4daf352cf9b3529d210be167d2af`                           |
| lastVerifiedCommitDate | 2026-08-08T22:29:45+02:00|
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
mutation, no signal post — `serving/agent_notifier.py`'s `_respawn_suspect` is the caller that gathers
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

No external requirement or design document is represented here.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The sole caller: gathers the orphan list once a manager seat is retired as suspect and surfaces it in the respawn observer event. | "def _respawn_suspect(  # pragma: no cover" | mcp/src/agents_remember/serving/_agent_notifier_actions.py:621-621 |
| Unit test: running workers of the named manager are returned; a terminated sibling and another manager's worker are excluded. | `test_finds_running_workers_of_the_named_manager` | mcp/tests/test_escalation_ladder.py:237-254 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-repository control-plane logic only. | — | — |

## Update History

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-02T20:45:43+02:00 — L6 W2-B02 curator: removed the whole unsupported task-authority claim, including its prose and table row, under the 2026-08-02 17:45 ruling; the two repository-internal references were already exact and unchanged; final scoped result 0 (checker-clean).

- 2026-08-02T01:42+02:00 — No content impact: re-derived line range(s) that ended past the end of the file the row names (`memory_quality/style/citations`, `citation_range_out_of_bounds`). Each range was rewritten by reading the cited construct at its current location; no claim was changed to fit a range, and no range was interpolated. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: moved current worker classification to binding role
  while retaining spawned-by provenance for parentage.

- 2026-07-08T23:15+02:00 — Created for 260707-HFX2-L4 (R3, orphan policy): `find_orphaned_workers` —
  a pure catalog read for a dead/respawned manager's still-running worker seats, wired into
  `serving/supervisor.py::_respawn_suspect`'s respawn event (`orphanedWorkers`). Detection/surfacing
  only, per the leaf's explicit scope allowance — no auto-reparent action exists yet. Verification
  metadata pinned until closeout stamps the 260707-HFX2-L4 commit.
