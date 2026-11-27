# mcp/tests/test_deferred_held_seat_closing.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Unit-regression suite verifying `BUG-R58@v2` Rule 4 and D1046 Sites 7–8: host-free explicit retirement of reserved held seats, public holder projection, shared held-store reconciliation preservation, unentered opening meeting a closing mark, and archiving a BUG-R51 retried agent ID when a closing mark lands mid-retry.

## Code Commentary

- `test_retire_deferred_held_seat_sends_zero_host_calls_and_records_caller_and_reason` verifies `retire_native_seat` retires an uncreated deferred held seat with zero host calls while recording `retiredBy.callerAgentId`, `retiredBy.reason`, `status="stopped"`, and `hostAgentExists=False`.
- `test_d1046_site7_site8_and_closing_retry_race` verifies `_public_execution` exposes `agentId` and `holderAgentId` (Site 8), `_reconcile_agent` preserves an unclosed deferred held seat with zero host calls (Site 7), and `refuse_retired_start(..., retried_agent_id=...)` archives a retried agent ID on a closing leaf.
- `test_rule4_unentered_opening_meets_closing_mark_and_closing_during_retry_archives_orphan` exercises two closing-mark races through `role_held_messages.drain_held`: (4a) an unentered opening meeting a closing mark makes zero `agent-create` calls and settles waiting messages undelivered (`recipient-archived`, `heldWaiting == 0`); (4b) a closing mark landing during a BUG-R51 confirmation retry archives both the original and retried agent IDs with zero orphans.
- Registered in `mcp/tests/test-evidence-lanes.toml` (`unit-regression`) and `mcp/tests/evidence-lifecycle.toml`.

## Relationships

- **Code under test:** `cli/role_retire.py`, `cli/role_launch_receipts.py`, `cli/role_deferred_held.py`, `cli/shared_held_store_reconciliation.py`, `cli/role_launch_archive.py`, `cli/role_held_messages.py`, `cli/role_held_opening.py`, and `cli/role_launch_confirmation.py`.
- **Support:** `paseo_role_tools_test_support.py` and `test_paseo_launch.py`.

## Evidence

- `TestDeferredHeldSeatRetirementAndClosing` covers host-free retirement, D1046 Sites 7–8 (`_public_execution` and `_reconcile_agent`), unentered closing-mark refusal, and mid-BUG-R51-retry orphan archival. [1]
