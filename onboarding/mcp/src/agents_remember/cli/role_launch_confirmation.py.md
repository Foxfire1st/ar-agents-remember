# mcp/src/agents_remember/cli/role_launch_confirmation.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Implements three-step launch-time server-binding confirmation, single-retry recovery under the same `requestId`, and held-seat re-confirmation before sending the opening message. Ensures eager harnesses run a live bound `agents-remember-task` server matching the seat's `(agentId, requestId)` with no foreign or unreadable bindings under the same harness before any work starts.

## Code Commentary

- **Constants and skip gating:** `BINDING_CONFIRM_WAIT_S = 5.0`, `BINDING_CONFIRM_POLL_S = 0.1`, `BINDING_CONFIRMATION_FAILED_CODE = "binding_confirmation_failed"`. `confirmation_skip_reason(call)` skips Step 2 with `"existing-only-reconcile"` when `agent.get("existingOnly") is True`, `"no-task-tool-server"` when `agents-remember-task` is absent, or `"provider-starts-server-after-create"` when `provider_starts_tool_server_at_create(provider)` (from `agents_remember.cli.paseo_seat_policy`) returns `False` (lazy `claude` or native `antigravity`), returning a single-call `agent-create` with `bindingConfirmation.status == "skipped"`.
- **Polling and ancestry evaluation:** `confirm_seat_binding` polls `live_server_bindings` and `harness_root_pids` until confirmed, immediately failed, or timed out (`"binding-not-registered"`):
  - When `roots is None` (`/proc` absent): confirms by `(agentId, requestId)` only, recording `ancestry_checked=False` and `ancestry_skipped_reason="proc-unavailable"`.
  - When `roots` is non-empty (`_evaluate_under_roots`): inspects `bound` and `unreadable` records whose `(parentPid, ancestors)` intersect `roots` via PID and `processStart` matching; fails immediately on `"unreadable-binding"`, `"foreign-binding"`, or `"multiple-bound-servers"`, ignores `"unbound"` records, and confirms when only own bound server(s) exist (`ancestry_checked=True`).
  - When `roots == []` (`_evaluate_without_roots`): once an own match exists, checks sibling `bound` and `unreadable` records sharing `match.parentPid` and `parentProcessStart` (`> 0`), failing on `"unreadable-binding"` or `"multiple-bound-servers"`, and otherwise confirms with `ancestry_checked=False` and `ancestry_skipped_reason="harness-root-not-found"`.
- **Three-step create, open-held, and single retry:** `execute_confirmed_launch` handles `mode="create"` (create without prompt, confirm binding, send prompt with `skipToolServerWait=True`) and `mode="open-held"` (re-confirm existing seat, then send prompt with `skipToolServerWait=True`). On confirmation failure, `_retry_after_failure` archives attempt 1 via `agent-archive` (refusing immediately with `lost_agent_id` if archiving fails), mints a fresh `agentId` under the same `requestId`, clones the call via `_retry_launch_call` (`:retry-1` or `:open-retry-1` `idempotencyKey`, dropping `archiveAgentId`, updating `agentId` and `AR_PASEO_AGENT_ID`), calls `on_retry_agent(retry_agent_id)`, and runs `_create_confirm_and_send`. A second failure archives attempt 2 and refuses with `code="binding_confirmation_failed"`, `lost_agent_id=None`, and both archived IDs in the 800-character-capped refusal message.
- **Held-seat receipt helpers:** `held_open_outcome_extras`, `is_held_seat_lost`, `held_seat_lost_detail`, `held_seat_lost_settlement`, and `apply_held_open_confirmation` propagate `bindingConfirmation`, `effectiveLaunchCall` (updating `agentId`, `applied_to_agent`, and prompt-stripped `replayRequest`), `hostAgentExists` (clearing `replayRequest` when `False`), and settlement tuples `(detail, receipt_updates, remove_fields, result_extras)` for `settle_held_store`.

## Relationships

- **Callers:** `mcp/src/agents_remember/cli/paseo_launch.py` (`run_launch_call` delegates to `execute_confirmed_launch`); `mcp/src/agents_remember/cli/role_launch_outcome.py` (imports `BINDING_CONFIRMATION_FAILED_CODE`); `mcp/src/agents_remember/cli/role_held_opening.py` (uses `LaunchExecutionPolicy(mode="create", ...)` for deferred held seats and `mode="open-held"` for legacy pre-created held seats, plus the held-seat confirmation helpers); `mcp/src/agents_remember/cli/role_launch_receipts.py` (passes `on_retry_agent` via `LaunchExecutionPolicy`).
- **Dependencies:** `agents_remember.cli.paseo_seat_policy` (`provider_starts_tool_server_at_create`), `agents_remember.serving.server_bindings` (`live_server_bindings`, `harness_root_pids`, `ProcessAncestor`, `ServerBindingRecord`), `agents_remember.cli.paseo_launch` (lazy imports for outcome/mint/create helpers), `agents_remember.cli.paseo_bridge` (`PaseoBridgeFailure`, `AGENT_WITHOUT_MESSAGE_LOST`, `BRIDGE_REFUSED`), `agents_remember.application.agent_binding`.
- **Tests:** `mcp/tests/test_launch_identity_confirmation.py`.

## Evidence


- Polling defaults (5 s / 0.1 s), refusal code, and `confirmation_skip_reason` (gating `existingOnly` reconciles, absent task tool server, and `provider_starts_tool_server_at_create` fail-closed eager classification) govern Step 2 gating. [1]

- Snapshot evaluation enforces harness-root ancestry, refuses unreadable, foreign, or multiple bound servers immediately, permits unbound servers, and handles `/proc`-absent and rootless sibling fallbacks. [2]
- Single retry clones the call with a fresh `agentId`, same `requestId`, and `:retry-1` / `:open-retry-1` idempotency key, archives failed attempts, and refuses with zero live seats on double failure. [3]
- Main launch entry executes the skip path, `open-held` re-confirmation with `skipToolServerWait=True`, or three-step create-confirm-send. [4]
- Held-seat receipt helpers carry `bindingConfirmation` and `effectiveLaunchCall`, classify lost seats, and rewrite receipt `agentId`, `replayRequest`, and `hostAgentExists`. [5]
