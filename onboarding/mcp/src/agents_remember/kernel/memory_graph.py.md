# mcp/src/agents_remember/kernel/memory_graph.py

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Charges bounded memo entries for reachable Python data.

## Code Commentary

The traversal adds each Python object's size once by identity and stops when the charge exceeds the supplied ceiling. It keeps one iterator per active branch and skips shared interpreter definitions such as classes, modules and functions. The charge covers Python objects.

## Relationships

A byte-bounded memo charges its key and value together. A shared object within that entry contributes once.

## Evidence

- Graph charging counts object identities and stops past the ceiling. [1]
