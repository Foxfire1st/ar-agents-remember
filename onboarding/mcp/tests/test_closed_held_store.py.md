# mcp/tests/test_closed_held_store.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Integration test suite pinning closed-receipt fencing, waiting-text settlement, concurrency serialization, no-create read/count helpers, and generation rollover for held-message stores.

## Code Commentary

- `ClosedHeldStoreTests` (subclass of `RoleToolsTestCase`, marked `pytest.mark.integration`) verifies that a closing leaf receipt with a removed workspace refuses late `role_message`, `developer_delivery.deliver_or_hold`, `_app_lifespan._held_delivery_tick`, `sweep_held_messages`, repeat `retire`, and `provider_limit_drain.claim_ended_stamp` without recreating the workspace folder.
- Verifies that read-only counters (`waiting_total`, `recount_waiting_for`, `_read_store_counts`) create no store or lock files when the store is absent.
- Verifies live/stoppable boundaries: a cancelled turn (`stopped` receipt alone) never settles or fences held writes; replacement settles the predecessor only after `_agent_archive` executes; first send to a timed-out unregistered prepared launch holds with `start-unfinished`.
- Verifies concurrency and generation fencing: `test_close_serializes_with_an_admitted_writer` proves closure waits for an admitted writer and records its text in `heldStoreClosures["0"]`, while `test_public_send_refuses_its_generation_after_same_id_restart` and `test_same_request_restart_refuses_the_previous_generation` prove stale generations fail with `generation-changed` / `recipient-archived` after `begin_held_generation`.

## Relationships

- Exercises `cli/role_held_store.py`, `cli/role_held_messages.py`, `cli/paseo_role_tools.py`, `cli/developer_delivery.py`, `cli/provider_limit_drain.py`, `controlplane/held_store_layout.py`, and `serving/_app_lifespan.py`.
- Registered in `mcp/tests/test-evidence-lanes.toml`.

## Evidence

- Verifies late `role_message` against a closing leaf receipt returns `recipient-archived` without recreating the removed workspace folder. [1]
- Proves replacement preserves the predecessor's held store until `_agent_archive` executes, then records waiting text in `heldStoreClosures["0"]` in history and unlinks the store. [2]
- Uses threads around `open_held_store` and `refresh` to prove closure serializes behind an admitted writer, preserves its text in `heldStoreClosures["0"]`, removes the store, and rejects subsequent opens with `HeldSeatClosed`. [3]
- Proves `begin_held_generation` keeps the same request ID while causing both `open_held_store` and `reconcile_held_store` to reject the prior generation with `reason == "generation-changed"`. [4]
