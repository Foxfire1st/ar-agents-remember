# mcp/tests/test_signal_routing.py

| Field                  | Value                                       |
| ---------------------- | ---------------------------------------------|
| repository             | agents-remember                               |
| path                   | `mcp/tests/test_signal_routing.py`            |
| doc_type               | `file-level-onboarding`                       |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash | `79b2fd6c4da73c7845406f6c68b947b8bd0e1009`|
| lastVerifiedCommitDate | 2026-07-10T22:22:16+02:00|
| governingOverview      | `../overview.md`                              |

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
`test_decision_item_routes_to_architect_regardless_of_provenance` pins that a `decision-item`
message kind always routes to the reserved `architect` role (no `agent_id`/`lifecycle_id`,
since the architect is not a spawned catalog entry) regardless of the sender's own catalog
provenance. Three negative cases close the surface: an unknown/unregistered sender, a sender with
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
- `decision-item` is a reserved-role route (architect) independent of catalog provenance; every
  other message kind routes structurally off `spawn_role`.
- No sender id, an unknown sender, or a sender with no spawn provenance all derive an empty
  `RoutedOwner()` — the caller's own explicit addressing is the fallback, never a guessed owner.
- `SkipLevelOwnerTests` is a genuinely separate suite from `SignalRoutingTests` above — it never
  asserts anything about `derive_signal_owner`'s own one-hop behavior, only the new two-hop walker's
  dead-node-skipping and hierarchy-ceiling behavior.

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
| Two-hop, dead-node-skipping owner derivation: live chain, dead intermediate, dead-ceiling, unknown sender, and role-only-address cases. | `SkipLevelOwnerTests` | [test_signal_routing.py](agents-remember/mcp/tests/test_signal_routing.py) |
| The shared liveness primitive both the ladder and the two-hop walk read. | `IsSeatDeadTests` | [test_signal_routing.py](agents-remember/mcp/tests/test_signal_routing.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Update History

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: added pair-bound chain-credit/manager-addressing proof
  at two fleet sizes and current-role discovery coverage.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: added positive and parallel-leaf-negative regressions
  for explicit replacement-leaf chain credit. Verification metadata remains pinned until closeout
  stamps the eventual L15 code commit.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 round 2: added current-manager, no-direct-skip, and
  unbound-reviewer chain-progress regressions; preserved the explicit unbound-worker S1 follow-up.
  Verification metadata remains pinned until closeout stamps the eventual L13 code commit.

- 2026-07-08T23:15+02:00 — 260707-HFX2-L4 (R2/R4, escalation ladder + dead-upstream detection):
  added `SkipLevelOwnerTests` (live two-hop chain, dead-intermediate skip, dead-hierarchy-ceiling,
  unknown sender, role-only-address-with-no-session cases) and `IsSeatDeadTests` (unknown/`None`/
  running-agent liveness cases) for the module's new `derive_skip_level_owner`/`is_seat_dead`.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L4 commit.
- 2026-07-08T16:15+02:00 — Created for 260707-HFX2-L1 (curator delta round 2, closeout-preview
  gap): one-hop hierarchical routing derivation coverage for the R4 signal-routing module.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L1 commit.
