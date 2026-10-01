# mcp/tests/test_signal_routing.py

## Governing Overview

[overview.md](../overview.md)

## Purpose

R4 (260707-HFX2-L1) unit tests for `controlplane/signal_routing.py`'s `derive_signal_owner` —
deriving the ONE-HOP owner address a signal should route to (worker's signal goes to its manager,
manager's goes to its orchestrator, a `decision-item` always goes to the architect) from the
terminal catalog's spawn provenance, entirely without a caller-supplied address. 260707-HFX2-L4
(R2/R4) adds coverage for the module's new two-hop, dead-node-skipping `derive_skip_level_owner`
and its `is_seat_dead` liveness helper.

## Code Commentary

### 260707-HFX2-L17 Pair Credit And Addressing At Scale

New cases exercise binding-role manager/architect discovery and prove a pair-bound worker credits
its leaf and resolves the correct manager at fleet sizes 3 and 30. Historical spawn-parent walking
remains separately tested.

### 260707-HFX2-L13 Manager Resolution And Chain Credit

New fixtures prove a reviewer signal with stale provenance resolves the current same-chain manager,
an ambiguous/stale manager binding falls back to the role-only manager mailbox rather than
orchestrator, and an unbound reviewer spawned by the manager in the subject worktree counts as leaf
progress. No test claims equivalent unbound-worker credit; the accepted exclusion remains HFX2-L14
S7 follow-up.

### Logic

Routing regressions now prove architect lookup and rebind traversal are bounded by the exact
repository+sprint identity. Concurrent sprint architects remain distinct, and absence of a
matching bound owner fails closed instead of selecting a global or merely role-matching row.

ARSPAWN-L5 proves one reviewer role routes to the current occupant of its plane-stamped manager,
architect, or orchestrator parent across master, plan, and super review contexts. An unstamped
master reviewer raises instead of manufacturing the manager parent; the bounded historical
unstamped route remains only the pre-polymorphic leaf-reviewer case.

**260707-HFX2-L15 coverage.** Production-shaped same-cwd fixtures prove a declared unbound
replacement with `replacementForLeaf` counts as this leaf's progress, while a worker for a parallel
leaf under the same manager never suppresses this leaf.

`SignalRoutingTests` seeds a temp `TerminalCatalog` and upserts entries carrying `spawn_role` +
`spawned_by_session`/`spawned_by_lifecycle` provenance. `test_worker_signal_routes_to_its_manager`
and `test_manager_signal_routes_to_orchestrator` each assert `derive_signal_owner` returns a
`RoutedOwner` naming the sender's immediate spawner (role/agent_id/lifecycle_id) — proving both
layers of the hierarchy resolve correctly, not just one hardcoded hop.
`test_no_layer_is_addressed_its_grandchildrens_noise` is the one-hop regression: with a worker
spawned by a manager which was itself spawned by an orchestrator, a worker signal resolves to the
manager, never chasing the provenance chain a second hop to the orchestrator.
`test_decision_item_routes_to_its_sprint_architect_with_an_exact_address` pins that a
`decision-item` resolves the architect bound to the sender's exact repository+sprint, including
its concrete `agent_id` and `lifecycle_id`; it never falls back to a global role-only architect.
Three negative cases close the surface: an unknown/unregistered sender, a sender with
no `spawned_by_session` provenance (e.g. an orchestrator's own signal — the caller's explicit
`recipient_role` stands instead), and a `None` `sender_agent_id` all derive an empty `RoutedOwner()`
rather than a wrong or partial address.

**`SkipLevelOwnerTests`** (260707-HFX2-L4) seeds a three-tier orchestrator/manager/worker chain via
`_chain(...)`. `test_live_chain_lands_on_the_owners_owner` proves the base two-hop case (worker ->
manager -> orchestrator). `test_dead_intermediate_manager_is_skipped_not_addressed` marks the
manager `terminated` and asserts the walk still lands on the orchestrator, never the dead manager
itself. `test_dead_grandparent_walks_further_but_hits_the_hierarchy_ceiling` marks the orchestrator
itself dead and proves the walk cannot climb past it either way — the orchestrator has no owner-role
mapping of its own, dead or alive, so the result is an empty `RoutedOwner()` (the developer, the top
rung, is never modeled in catalog provenance). `test_unknown_sender_derives_no_skip_level_route`
covers an unregistered sender. `test_no_second_hop_session_still_resolves_a_role_only_address`
proves a manager with no recorded `spawned_by_session` still yields a ROLE-only
`RoutedOwner(role="orchestrator")` rather than discarding the known role mapping.

**`IsSeatDeadTests`** (260707-HFX2-L4) pins the three `is_seat_dead` cases directly: an unknown
agent id, a `None` agent id, and a `running` catalog row (not dead) — the liveness primitive both
the ladder and the two-hop walk share.

### Conventions

A single `unittest.TestCase` with a local `_upsert(**overrides)` helper that layers overrides onto
a base `TerminalCatalogEntry` dict, matching the fixture style used across the terminal-catalog
test modules (`test_terminal_catalog.py`, `test_signal_routing.py`'s own module).

### Invariants And Boundaries

- Routing reads only the SENDER's own catalog provenance (one hop) — it never walks the spawn
  chain further, even when the intermediate owner's own provenance would resolve further up.
- `decision-item` is an exact-sprint architect route derived from persisted catalog provenance;
  every other message kind routes structurally off `spawn_role`.
- No sender id, an unknown sender, or a sender with no spawn provenance all derive an empty
  `RoutedOwner()` — the caller's own explicit addressing is the fallback, never a guessed owner.
- `SkipLevelOwnerTests` is a genuinely separate suite from `SignalRoutingTests` above — it never
  asserts anything about `derive_signal_owner`'s own one-hop behavior, only the new two-hop walker's
  dead-node-skipping and hierarchy-ceiling behavior.

### Todos

None.

## Evidence

### Docs References

No meaningful external design-doc references found yet (created this leaf).

### Repo-Internal References

- Worker-to-manager and manager-to-orchestrator one-hop routing resolves the current occupant from document-and-role identity without spawn ids. [1]
- One-hop-only regression: a missing manager never causes a worker signal to fall through to the orchestrator. [2]
- `decision-item` routing resolves the current architect on the sender's sprint document. [3]
- Sprint-level roles follow the approved direct-parent ladder rather than skipping levels. [4]
- The shared liveness primitive the rebind/dead-target and dead-upstream machinery reads. [5]

### Cross-Repo References

No meaningful cross-repo references found.

## 260713-TES-L5 Current Delta — Skip-Level Walk Tests Removed

The `derive_skip_level_owner`/`_derive_spawn_owner` coverage is deleted with the function:
no two-hop owner's-owner walk remains. One-hop `derive_signal_owner`, `is_seat_dead`, and the
scoped owner-derivation family stay covered as before.
