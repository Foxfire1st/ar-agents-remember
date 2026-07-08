# mcp/tests/test_signal_routing.py

| Field                  | Value                                       |
| ---------------------- | ---------------------------------------------|
| repository             | agents-remember                               |
| path                   | `mcp/tests/test_signal_routing.py`            |
| doc_type               | `file-level-onboarding`                       |
| lastUpdated            | 2026-07-08T16:15+02:00                        |
| lastVerifiedCommitHash | `45708bbddf1ddb8a2045faa9fad88fe72603b674`|
| lastVerifiedCommitDate | 2026-07-08T05:51:44+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

R4 (260707-HFX2-L1) unit tests for `controlplane/signal_routing.py`'s `derive_signal_owner` —
deriving the ONE-HOP owner address a signal should route to (worker's signal goes to its manager,
manager's goes to its orchestrator, a `decision-item` always goes to the architect) from the
terminal catalog's spawn provenance, entirely without a caller-supplied address.

## Code Commentary

### Logic

`SignalRoutingTests` seeds a temp `TerminalCatalog` and upserts entries carrying `spawn_role` +
`spawned_by_session`/`spawned_by_lifecycle` provenance. `test_worker_signal_routes_to_its_manager`
and `test_manager_signal_routes_to_orchestrator` each assert `derive_signal_owner` returns a
`RoutedOwner` naming the sender's immediate spawner (role/agent_id/lifecycle_id) — proving both
layers of the hierarchy resolve correctly, not just one hardcoded hop.
`test_no_layer_is_addressed_its_grandchildrens_noise` is the one-hop regression: with a worker
spawned by a manager which was itself spawned by an orchestrator, a worker signal resolves to the
manager, never chasing the provenance chain a second hop to the orchestrator.
`test_decision_item_routes_to_architect_regardless_of_provenance` pins that a `decision-item`
message kind always routes to the reserved `architect` role (no `agent_id`/`lifecycle_id`,
since the architect is not a spawned catalog entry) regardless of the sender's own catalog
provenance. Three negative cases close the surface: an unknown/unregistered sender, a sender with
no `spawned_by_session` provenance (e.g. an orchestrator's own signal — the caller's explicit
`recipient_role` stands instead), and a `None` `sender_agent_id` all derive an empty `RoutedOwner()`
rather than a wrong or partial address.

### Conventions

A single `unittest.TestCase` with a local `_upsert(**overrides)` helper that layers overrides onto
a base `TerminalCatalogEntry` dict, matching the fixture style used across the terminal-catalog
test modules (`test_terminal_catalog.py`, `test_signal_routing.py`'s own module).

### Invariants And Boundaries

- Routing reads only the SENDER's own catalog provenance (one hop) — it never walks the spawn
  chain further, even when the intermediate owner's own provenance would resolve further up.
- `decision-item` is a reserved-role route (architect) independent of catalog provenance; every
  other message kind routes structurally off `spawn_role`.
- No sender id, an unknown sender, or a sender with no spawn provenance all derive an empty
  `RoutedOwner()` — the caller's own explicit addressing is the fallback, never a guessed owner.

### Todos

None.

## Docs References

No meaningful external design-doc references found yet (created this leaf).

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Worker-to-manager and manager-to-orchestrator one-hop routing from catalog spawn provenance. | L42-L61 | [test_signal_routing.py](agents-remember/mcp/tests/test_signal_routing.py) |
| One-hop-only regression: a worker's signal never chases the chain past its manager. | L64-L82 | [test_signal_routing.py](agents-remember/mcp/tests/test_signal_routing.py) |
| `decision-item` reserved-role routing and the three no-route negative cases. | L84-L104 | [test_signal_routing.py](agents-remember/mcp/tests/test_signal_routing.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Update History

- 2026-07-08T16:15+02:00 — Created for 260707-HFX2-L1 (curator delta round 2, closeout-preview
  gap): one-hop hierarchical routing derivation coverage for the R4 signal-routing module.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
