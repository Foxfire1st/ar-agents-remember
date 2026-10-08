# mcp/tests/test_global_state_isolation.py

## Governing Overview

[overview](overview.md)

## Purpose

The suite identifies the test that leaks an explicitly-owned mutable global.
The expected owner is the kernel checkout-execution declaration, whose normal pytest baseline is
`{"mode": "test"}`; a leaked dashboard/MCP role is restored to that explicit mode before failure.

## Code Commentary

### Logic

`GlobalStateLeakDetectionTests` deliberately leaks the checkout role, then observes both the named
leak and restoration to test mode before failure. It verifies that only restored rows enter
per-test snapshots, that reset never imports unloaded owners, and that a subsequently loaded cache
is cleared. The actual ambient heartbeat is stopped and joined. Each other reset row exercises its
declared cleanup through a local owner double; each restored row keeps its original table while
reporting the leaked addition.

`test_tmux_cleanup_failures_do_not_skip_existing_pytest_teardown` drives the actual unconfigure
hook with both timeout and spawn errors. It observes private server targeting, the shared guard,
and environment, lease and temporary cleanup before the original error propagates.

### Invariants And Boundaries

This suite runs under the ordinary shared pytest bootstrap as well as admitted certifying routes.
The bootstrap's explicit test-mode baseline is required; a raw import without that composition is
not an independent proof. Registry-row doubles and the actual heartbeat establish different cleanup
boundaries and must not be described as full native-service execution.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- GlobalStateLeakDetectionTests checks named leak restoration and the loaded-owner reset register. [1]

## Bootstrap Ownership

The state owner lives in `agents_remember_test_support.testing.global_state`. Both ordinary and
certifying pytest use its reusable bootstrap. No Dagger-only requirement belongs to these state
restoration assertions.


- Every loaded reset row participates in its declared cleanup proof. [2]
- Each restored table is repaired and its leak named. [3]
- Private tmux failure preserves all existing later teardown. [4]
