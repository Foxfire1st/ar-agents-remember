# mcp/tests/mcp_memory_bounded_fixture.py

## Governing Overview

[MCP Tests](overview.md)

## Purpose

Builds private paired Git repositories, a leaf and server settings for the native stdio memory regression.

## Code Commentary

The fixture commits the corpus, records its paired code commit in memory history, and creates linked leaf worktrees and canonical task documents. Its settings select fixture roots and logs, configure the test certification profile, and disable dashboard auto-start. A separate process warms the index with the selected checkout and interpreter before measurement.

## Relationships

The fixture builder calls the corpus generator and gives the driver its settings, code tree, roots and task reference.

## Evidence

- The Git pair records the memory commit's code attribution. [1]
- Index warming runs before the measured server starts. [2]

- The builder returns the configuration and identities used by the driver. [3]
