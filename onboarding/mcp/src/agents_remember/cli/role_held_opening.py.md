# mcp/src/agents_remember/cli/role_held_opening.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Owns held-seat opening (`open_held_seat`) and its concurrent leaf-closing fence (`_run_held_open_call`): restores saved handover artifacts, enforces message-limit batch offload, inserts product start notices, runs the stored `replayRequest` verbatim in `create` mode for deferred held seats (or `open-held` for legacy pre-created held seats) under BUG-R51 binding confirmation, and settles delivered or seat-lost outcomes.

## Code Commentary

- **Opening flow (`open_held_seat`):** Validates `replayRequest` and `heldOpeningPrompt` (releasing the claim with `cannot-open` if absent), runs `_restore_launch_handover` under `open_held_store` (propagating `HeldSeatClosed`, returning `cannot-open` on `ValueError`), bounds waiting messages via `prepare_held_opening_batch` (returning `open-failed` on settings/OS/value errors without calling the host), and composes `opening`, `product_start_message.held_seat_opening(...)`, and `bounded_batch` into `prompt`.
- **Parent tolerance and confirmation mode:** Whenever `agent_call` carries `parentAgentId`, sets `allowMissingParent = True` so `paseo_bridge.mjs` omits a reloaded or archived Manager parent while keeping `parentAgentId` on the receipt (`BUG-R58@v2` rule 6). Publishes receipt role identity via `publish_receipt_role_agent` before launch and selects `LaunchExecutionPolicy(mode="create")` when `is_deferred_held_receipt(batch.receipt)` is true (creating and confirming exclusive seat binding on first message) or `mode="open-held"` for legacy pre-created held seats, with `on_retry_agent` republishing any freshly minted retry `agentId`.
- **Leaf closing-mark fence (`_run_held_open_call`):** For leaf roles, passes `before_create=lambda: _leaf_before_create(batch.path, batch.receipt, opening_held=True)` so an already-closing leaf is refused before host creation and an entered opening marks `heldOpenPending` on disk. After `run_launch_call`, re-reads the receipt; if `_leaf_is_closing(current)` became true concurrently, invokes `_refuse_closing_launch` with `retried_agent_id=retried_outcome_agent_id(outcome, current)` so both original and retried agents are archived, then raises `HeldSeatClosed`. On non-`no-answer` completion without close, clears `heldOpenPending`.
- **Settlement:** On `outcome.kind == "created"`, stages `_END_DELIVERED` metadata before `_remove_ids` (preserving crash-recovery end staging) and returns `execution`, `applied`, and `held_open_outcome_extras(outcome)`. On `is_held_seat_lost(outcome)`, settles waiting messages undelivered via `held_seat_lost_settlement` and `_end_batch(..., "rejected")`. Otherwise releases the claim and returns `open-failed`.

## Relationships

- **Callers:** `cli/role_held_messages.py` (`_open_held_seat` delegates directly to `open_held_seat`).
- **Dependencies:** `cli/paseo_launch.py` (`run_launch_call`, `LaunchExecutionPolicy`), `cli/role_deferred_held.py` (`is_deferred_held_receipt`, `retried_outcome_agent_id`), `cli/role_launch_confirmation.py` (`held_open_outcome_extras`, `is_held_seat_lost`, `held_seat_lost_settlement`), `cli/role_launch_receipts.py` (`_leaf_before_create`, `_leaf_is_closing`, `_refuse_closing_launch`, `_restore_launch_handover`, `_read_receipt`, `_write_receipt`), `cli/role_opening_offload.py`, `cli/product_start_message.py`, `cli/role_held_store.py`, and `cli/role_activity.py`.
- **Tests:** `mcp/tests/test_deferred_held_seat.py`, `mcp/tests/test_deferred_held_seat_closing.py`, `mcp/tests/test_launch_identity_confirmation.py`, and `mcp/tests/test_product_start_messages.py`.

## Evidence

- `_run_held_open_call` fences leaf held-seat openings via `_leaf_before_create(..., opening_held=True)`, archives both original and retried IDs on concurrent close via `_refuse_closing_launch`, and clears `heldOpenPending` on completion. [1]
- `open_held_seat` restores handover artifacts, bounds waiting batches, sets `allowMissingParent=True`, runs `mode="create"` for deferred held receipts (or `"open-held"` for legacy), stages delivery ends before removal, and settles seat-lost outcomes. [2]
