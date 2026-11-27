# mcp/src/agents_remember/cli/held_reset_delivery.py

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Connects native held-message admission and drain execution to `HeldResetIndex` and builds the `ResetDeliveryPorts` collaborator passed into serving's reset scheduler.

## Code Commentary

`hold_at_receipt(config, receipt_path, workspace_path, agent_id, message)` wraps `hold_message` with a `before_commit` callback that publishes a `ResetTarget` to `HeldResetIndex(config.coordination_root).schedule(target)` whenever `message.limited_until` is set. Because `hold_message` invokes `before_commit` under the store lock before writing the store file, a durable reset-index entry exists before the limited hold lands on disk; `note_held_receipt(config, receipt_path)` follows the store write.

`drain_reset_entry(config, entry)` delivers one due `ResetEntry` through the ordinary ordered claim path: it re-reads `target.receipt_path` via `_read_receipt`, marks the attempt `gone=True` when the receipt is absent or `_store_endpoints(receipt)` no longer matches `(str(target.workspace_path), target.agent_id)`, otherwise calls `drain_held` and applies terminal/delivery outcomes (`delivered`, `opened`, `recipient-gone`, `seat-lost`, `partially-delivered`) through `apply_drain_to_receipt`. `OSError`, `ValueError`, and `HTTPException` are logged without raising so one recipient failure does not abort the pass.

`finish_reset_entry(index, entry, result, retry_at)` retires or defers the observed generation. When `result.gone` is true, it calls `index.finish(entry, None)`. Otherwise it acquires `exclusive_file_lock` on `store_path_for(target.workspace_path, target.agent_id)` — the same lock used by admission — reads the store file, and retires the entry (`retry_at=None`) only when both `messages` and `pendingLines` are empty; if messages or pending terminal lines remain (or if reading fails with `(OSError, ValueError)`), it defers the generation to `retry_at`.

`reset_delivery_ports(config)` binds `adopt_held_resets` and `_attempt` (which runs `drain_reset_entry` then `finish_reset_entry`) into `ResetDeliveryPorts` for serving composition.

## Boundaries

Reset delivery reuses `drain_held` and `apply_drain_to_receipt` rather than introducing a second delivery protocol or bypassing FIFO claims, permission guards, or provider-limit checks. Lock-bounded store inspection before `index.finish` prevents retiring a recipient whose store still holds waiting messages or received a new admission.

## Evidence

- `hold_at_receipt` schedules a known reset in `HeldResetIndex` via `hold_message(..., before_commit=schedule)` before committing the held store file and then calls `note_held_receipt`. [1]
- `drain_reset_entry` verifies receipt endpoints, runs `drain_held` and `apply_drain_to_receipt`, and contains `(OSError, ValueError, HTTPException)` failures. [2]
- `finish_reset_entry` retires gone entries directly and otherwise checks `messages` and `pendingLines` under `exclusive_file_lock` before retiring or deferring the generation; `reset_delivery_ports` constructs `ResetDeliveryPorts`. [3]
