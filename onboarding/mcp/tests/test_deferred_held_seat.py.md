# mcp/tests/test_deferred_held_seat.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Unit-regression suite verifying `BUG-R58@v2` Rules 1, 2, 3, 5, 6, 7, and 8 for deferred held-seat reservation, verbatim `replayRequest` opening, zero-host-call readers, replacing-start predecessor debt, archived-parent bridge tolerance, and post-open provider-limit holds.

## Code Commentary

- **`TestDeferredHeldBridgeParent`:** Drives the real `paseo_bridge.mjs` script via `AgentCommandScriptTests` to prove `agent-create` with `allowMissingParent=True` omits `parent` from the public host creation options when `parentAgentId` is archived (`L58-R6`).
- **`TestDeferredHeldReservationAndOpening`:** Exercises `start_leaf_set`, `role_message`, `role_launch_liveness._refresh_execution`, `recount_waiting`, `retire_native_seat` (`open-children`), and `provider_limit_drain.pause_for_provider_limit` over `RoleToolsTestCase` to verify: MIK-R100 rule 9 duplicate-start refusal and authorized replacement with zero host calls; role+task opening setting `allowMissingParent=True` and returning live `recipientAgentId` + `bindingConfirmation`; verbatim `replayRequest` execution despite later settings changes with pre-open held messages delivered in the same turn; and all named readers keeping reserved seats live with zero host reads.
- **`TestDeferredHeldReplacementAndLimits`:** Verifies `L58-R5` replacing-start debt custody both when host `agent-archive` fails (`paseo_bridge_timeout`) and when `settle_confirmed_replacement` raises `OSError("disk full")` after host archival (asserting `202` / `status="unknown"` / `pendingArchiveAgentId` and retry recovery to `status="held"`), and `L58-R7` verifying a reserved seat's opening message is not held by a provider limit while a later message after opening is held with `provider-limit`.
- Registered in `mcp/tests/test-evidence-lanes.toml` (`unit-regression`) and `mcp/tests/evidence-lifecycle.toml`.

## Relationships

- **Code under test:** `cli/role_deferred_held.py`, `cli/role_held_opening.py`, `cli/paseo_bridge.mjs`, `cli/paseo_role_tools.py`, `cli/role_launch_liveness.py`, `cli/role_launch_routes.py`, `cli/role_message_delivery.py`, `cli/role_retire.py`, `cli/provider_limit_drain.py`, and `controlplane/held_store_layout.py`.
- **Support:** `paseo_role_tools_test_support.py`, `test_paseo_bridge_agents.py`, `test_paseo_launch.py`.

## Evidence

- Bridge test proves `agent-create` omits an archived parent when `allowMissingParent=True`. [1]
- Reservation, opening, and reader tests cover zero-host-call occupancy/replacement, role+task open with `allowMissingParent`, verbatim `replayRequest` with pre-open batch delivery, and live-seat readers (`_refresh_execution`, `recount_waiting`, `open-children`, `pause_for_provider_limit`). [2]
- Replacement and limit tests cover archive-failure and settlement-write-failure `pendingArchiveAgentId` debt recovery and pre-open vs post-open provider-limit behavior. [3]
