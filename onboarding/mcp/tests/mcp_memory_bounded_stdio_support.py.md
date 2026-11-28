# mcp/tests/mcp_memory_bounded_stdio_support.py

## Governing Overview

[MCP Tests](overview.md)

## Purpose

Drives a fixed native stdio workload and captures Linux memory readings after each reply.

## Code Commentary

The driver pins the child by registry, process identity and cgroup and checks its build and fixture roots against the server report. One SDK session runs three cycles of 28 calls. The read plan sends actual returned cursors at the expected continuation positions and starts the retained-dependent selection with a fresh read. The child entry point suppresses the installation-level outside-scratch discovery sweep.

## Relationships

The driver consumes the synthetic leaf fixture, imports paging seeds from the corpus and emits captures for the receipt reader.

## Evidence

- The read plan requires real prior cursors at the continuation positions. [2]
- One session runs the complete fixed selection. [3]

- Server binding verifies the selected build and fixture scope. [1]
