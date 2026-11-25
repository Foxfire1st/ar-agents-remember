# mcp/src/agents_remember/application/memory_checkout_state.py

## Governing Overview

[Governing overview](overview.md)

## Purpose

Reports the memory checkout's observed Git commit and whether it has working-tree changes.

## Evidence

- The dirtiness observation reads the selected checkout. [1]
- The commit observation names the selected memory checkout's HEAD when it can be resolved. [2]
