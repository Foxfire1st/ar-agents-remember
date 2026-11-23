# mcp/tests/mcp_memory_bounded_corpus.py

## Governing Overview

[MCP Tests](overview.md)

## Purpose

Generates deterministic synthetic code and converted memory for the native stdio memory regression.

## Code Commentary

The code generator creates paired sample modules, tests, guide documents and the observation symbol used by write calls. The memory generator anchors cards and sidecars to committed fixture code, then creates routes, invariants, families, dependent links and closed histories. Fixed seeds support the repeated paging workload.

## Relationships

The fixture builder calls both generators. The stdio driver imports the read selectors.

## Evidence

- Sample code and guides provide the replay's source paths. [1]
- The memory generator builds the converted corpus against the committed fixture. [2]
