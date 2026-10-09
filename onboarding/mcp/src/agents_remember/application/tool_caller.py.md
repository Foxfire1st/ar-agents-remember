# mcp/src/agents_remember/application/tool_caller.py

## Governing Overview

[application overview](overview.md)

## Purpose

Snapshots who a tool server's Event River rows name as the caller (MIK-R114 rule 2).
The launch binding and its one task document are read once at server start, so a row is
whole without another read; an unreadable document falls back to its path, and a server
without a binding is a chat without a role, named with its harness.

## Code Commentary

`snapshot_tool_caller(binding, *, coordination_root, config_path)` never raises. It takes
the leaf, master or sprint reference from the binding in that order, resolves its document
for id and title, and keeps the reference key as `task_path` only when the document cannot
be read. `derive_harness(config_path)` names the harness from the settings file the server
started with: the directory owning its `mcp` folder, else the file stem, else nothing.

## Evidence

- The caller is snapshotted once from the launch binding and never raises. [1]
- The harness is named from the settings file path. [2]
