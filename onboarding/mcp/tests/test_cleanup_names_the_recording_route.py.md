# mcp/tests/test_cleanup_names_the_recording_route.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Cleanup guidance distinguishes master recording from leaf integration.

## Code Commentary

The test calls _cleanup_integration_refusal with a real series-contract fixture and asserts integration-incomplete plus worktree_record_landing in the reason and next tool. Replacing only the contract kind/leaf identity checks that a leaf still names worktree_integrate. This is helper-level guidance evidence; it performs no cleanup or recording transaction and supplies no acceptance.

## Evidence

### Repo-Internal References

These tests establish the assertions below; their definitions are separate from retained execution receipts.

- The refusal helper directs series cleanup to worktree_record_landing and leaf cleanup to worktree_integrate; it executes no cleanup or recording transaction. [1]
