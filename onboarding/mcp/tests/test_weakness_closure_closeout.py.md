# mcp/tests/test_weakness_closure_closeout.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Checks a deferred weakness closure through the application closeout route and both public knowledge-read payload views, preserving the reviewed record bytes and the judged memory tree.

## Code Commentary

### Logic

The converted closeout fixture creates an isolated code/memory leaf. `_weakness` authors the open record and then its task/reason closure; `_write` uses the real knowledge writer and includes the changed source's no-impact trace. `_assert_public_closure` calls the public payload function for both weakness and record views with a captured code tree and closed records enabled.

The test removes the obsolete source marker, writes the deferred closure, retains its exact bytes and reads the pending closeout note. A wrapper calls the native closeout memory judge and records every judged tree. `worktree_closeout_apply_tool` then performs the application transaction. The test compares the resulting memory commit's tree with all judged trees, checks its code attribution, and compares the committed weakness blob with both the reviewed bytes and the remaining worktree file. Both public views then return the completed code commit; the stored closure is unchanged.

### Boundaries

This integration source uses application/payload entry points; it does not register a FastMCP closeout call. The judge wrapper retains the native judge. The assertions concern the fixture's paired closeout, exact record bytes and exact memory tree. They establish no live record settlement or execution result by this card's author.

## Evidence

### Repo-Internal References

- The fixture writes an open or deferred record through the real writer with its source trace. \[1] [1]
- The public weakness and record payloads are compared against one expected closure at the captured code tree. \[2] [2]
- Application closeout retains native judging, commits the judged tree, preserves reviewed record bytes and exposes the actual closing code commit. \[3] [3]
