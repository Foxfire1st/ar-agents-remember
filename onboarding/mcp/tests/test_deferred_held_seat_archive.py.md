# mcp/tests/test_deferred_held_seat_archive.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Integration test suite verifying `BUG-R58@v2` Rule 4 task-end archive boundaries for deferred held seats across `finalize`, `cleanup`, `abandon`, and `dry_run` preview when the Paseo host is unreachable.

## Code Commentary

- Subclasses `LeafAgentArchiveTests` (`pytest.mark.integration`) and converts a leaf receipt to a deferred held seat (`status="held"`, `hostAgentExists=False`, `execution={}`, optional `heldOpenPending=True`) while patching `role_launch_archive.bridge_call` to raise `DAEMON_UNREACHABLE`.
- `test_deferred_held_seat_ends_without_host_on_finalize_cleanup_abandon_and_preview` verifies that an uncreated deferred held seat settles as `gone` with zero host calls, zero owed debt, `LeafAgentArchive` retirement attribution, and waiting held messages recorded in `heldStoreClosures` across `finalize`, `cleanup` dry-run preview and apply, and forced `abandon`.
- `test_entered_deferred_held_open_settles_through_host_and_reports_debt` verifies that a deferred held seat with `heldOpenPending=True` still queries `agent-state` on preview and attempts `agent-archive` on apply, blocking removal with `owed` debt when the host is unreachable.
- Registered in `mcp/tests/test-evidence-lanes.toml` (`integration`) and `mcp/tests/evidence-lifecycle.toml`.

## Relationships

- **Code under test:** `cli/role_launch_archive.py`, `worktrees/modules/finalize.py`, and `application/worktree_tools.py`.
- **Support:** `test_leaf_agent_archive.py` and `test_lifecycle_finalize.py`.

## Evidence

- `DeferredHeldSeatArchiveTests` verifies uncreated deferred held seats settle as `gone` with zero host calls across finalize/cleanup/abandon/preview, while `heldOpenPending=True` seats settle through the host and record `owed` debt when unreachable. [1]
