# mcp/src/agents_remember/worktrees/modules/kept_tool_calls.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Exports the leaf’s tool calls before terminal enclosure removal.

## Code Commentary

It reads leaf-scoped calls from LF-delimited JSON, removes `detail` and replaces removed workspace/outside-scratch paths with the leaf ID. The export merges with a prior result on retry and writes atomically. `keep_tool_calls_for_group(contract, *, dry_run)` runs or previews the move-out before whole-folder removal, checking target path safety and writability (`_check_keep_target`) in dry-run as well as apply; any failure returns a `tool-calls-not-kept` blocker before deletion and leaves the source log available.

## Evidence


- Terminal removal depends on a successful export and retries merge kept and current lines. [1]
