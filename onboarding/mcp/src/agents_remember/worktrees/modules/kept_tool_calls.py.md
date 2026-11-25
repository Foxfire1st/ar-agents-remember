# mcp/src/agents_remember/worktrees/modules/kept_tool_calls.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Exports the leaf’s tool calls before terminal enclosure removal.

## Code Commentary

It reads leaf-scoped calls from LF-delimited JSON, removes detail and replaces removed workspace paths with the leaf ID. The export merges with a prior result on retry and writes atomically. Failure leaves the source log available.

## Evidence

- Terminal removal depends on a successful export and retries merge kept and current lines. [1]
