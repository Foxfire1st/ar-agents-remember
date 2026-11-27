# mcp/src/agents_remember/cli/role_deferred_held.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Owns deferred held-seat reservation (`status: "held"`, `hostAgentExists: false`, `execution: {}`), predecessor archive and settlement custody before reserving a replacement held seat, retried agent-ID lookup for concurrent-close fencing, public leaf-holder/closing-mark projection helpers, and the `role_message` opened-seat answer builder (`BUG-R58@v2`).

## Code Commentary

- **Deferred held predicate (`is_deferred_held_receipt`):** Returns `True` exactly when `status == "held"`, `hostAgentExists is False`, and `agentId` is a non-empty string. All seat readers (`role_message_delivery`, `role_launch_liveness`, `shared_held_store_reconciliation`, `provider_limit_drain`, `paseo_role_tools`, `role_retire`, `role_launch_archive`, `role_held_opening`) rely on this single predicate so reserved seats are never treated as gone for lacking a host agent.
- **Deferred reservation (`defer_held_launch`):** Publishes a held seat without making any host `agent-create` call, retaining `replayRequest` verbatim, `status="held"`, `hostAgentExists=False`, and `execution={}`. When the launch replaces a live predecessor (`archiveAgentId`), `_archive_predecessor` archives that predecessor via `agent-archive` before taking the receipt lock; inside the lock, `finish_replacing_predecessor` settles the prior receipt and held store. If either host archival or the local predecessor-settlement write fails (`not archive_ok` or `not settled.predecessor_settled`), `_publish_unsettled_predecessor` keeps `pendingArchiveAgentId` debt, refuses a concurrent closing mark if present, and otherwise publishes `status="unknown"` (`202`) without reserving the new held seat. If the leaf is closing before reservation, `defer_held_launch` persists the receipt and delegates to `_refuse_closing_launch(..., creation_returned=False)`.
- **Opened answer (`opened_held_seat_answer`):** Constructs the `role_message` response for `outcome == "opened"`, naming `drain["execution"]["agentId"]` (falling back to `fallback_agent_id`) as `recipientAgentId` so a BUG-R51 retry returns the live agent ID, setting `openedHeldSeat=True`, and attaching `bindingConfirmation` when present.
- **Projection and retry-ID helpers:** `apply_leaf_holder` exposes `agentId` and `holderAgentId` on `_public_execution` for deferred held seats even while `execution` is empty; `apply_leaf_closing` projects closing-mark refusal fields (`startRefused`, `canStart=False`, `canRevive=False`, `canRetry=False`, and `status="rejected"` once own outcome is `archived`/`gone`); `public_instruction_fields` normalizes `choices`, `sessionOptions.choices`, and `instructionComposition`; `retried_outcome_agent_id` extracts any newly minted retry agent ID (from `outcome.execution`, `outcome.effective_launch_call`, or `outcome.lost_agent_id`) distinct from `current["agentId"]` so mid-retry closing marks archive the orphan too.

## Relationships

- **Callers:** `cli/role_launch_receipts.py` (`_run_prepared_launch`, `_public_execution`), `cli/role_held_opening.py` (`open_held_seat`, `_run_held_open_call`), `cli/paseo_role_tools.py` (`_deliver_or_hold`, `_held_then_delivered`), `cli/role_launch_liveness.py`, `cli/role_message_delivery.py`, `cli/role_retire.py`, `cli/role_launch_archive.py`, `cli/shared_held_store_reconciliation.py`, and `cli/provider_limit_drain.py`.
- **Dependencies:** `cli/paseo_launch.py` (`bridge_call`, `LaunchOutcome`), `cli/role_retirement_receipt.py` (`finish_replacing_predecessor`), `cli/role_held_store.py` (`settle_held_store`), `cli/role_step_up_decisions.py` (`record_step_up`), `cli/role_instructions.py`, `kernel/file_lock.py`, and lazy imports of `cli/role_launch_receipts.py` and `cli/role_launch_outcome.py`.
- **Tests:** `mcp/tests/test_deferred_held_seat.py`, `mcp/tests/test_deferred_held_seat_closing.py`, `mcp/tests/test_deferred_held_seat_archive.py`, `mcp/tests/test_launch_identity_confirmation.py`, and `mcp/tests/test_role_start_set.py`.

## Evidence

- `is_deferred_held_receipt` defines the reserved held-seat predicate (`status == "held"`, `hostAgentExists is False`, non-empty `agentId`). [1]
- `retried_outcome_agent_id` extracts a BUG-R51 retried agent ID distinct from the recorded receipt ID for closing-mark archival. [2]
- `opened_held_seat_answer` names the live `execution.agentId` as `recipientAgentId` and attaches `bindingConfirmation` on opened held-seat answers. [3]
- `apply_leaf_holder` and `apply_leaf_closing` project deferred held-seat holder identity and leaf closing-mark refusal fields onto public execution views. [4]
- `defer_held_launch` archives any live predecessor via `_archive_predecessor`, preserves `pendingArchiveAgentId` debt via `_publish_unsettled_predecessor` on archive or settlement-write failure, fences closing marks, and reserves `status="held"` with `hostAgentExists=False` and `execution={}`. [5]
