# mcp/tests/test_mcp_stdio_transport.py

## Governing Overview

[overview.md](../overview.md)

## Purpose

End-to-end stdio transport tests for hang-prone MCP tools: spawns the real
server over real pipes (the same topology as a harness) and asserts tool calls
complete within a bound. Born from GitHub #49, where `memory_carryover_plan`
hung 6–8 minutes via MCP while the identical function ran in 2.6s directly.

## Code Commentary

### Logic

`call_tool_over_stdio` launches `python -m agents_remember.mcp --config <tmp
settings>` through `mcp.client.stdio`, initializes a `ClientSession`, and calls
the tool under `asyncio.wait_for` bounds. `build_carryover_fixture` reuses the
worktree-support git helpers to build a code repo with a landed branch, an
official memory repo, and an in-coordination source memory tree, so the plan
has a real auto-carry candidate. A `ping` test proves the harness itself.

### Invariants And Boundaries

- This harness is the regression proof for #49: pre-fix it reproduced the hang
  (120s timeout, server stuck after `CallToolRequest`); post-fix it passes in
  ~3.4s. Keep it wired to real subprocess pipes — an in-process client would
  not exercise the inherited-descriptor failure mode.
- `source_memory` must live inside the coordination root
  (`require_within_coordination`).

## Evidence

### Repo-Internal References

- The fixed subprocess boundary used by carryover. [1]

## 260815-DAG-L4 Integration-Authority Forcing

This task extends this suite's production-bound fixtures or assertions for task-derived protected-ref ownership, durable closeout/integration authority, external-memory parity, and fail-closed recovery. The suite continues to exercise the real owner named in its existing purpose; the L4 delta adds exact negative or crash/retry evidence rather than a test-only bypass.
