# mcp/src/agents_remember/application/knowledge_gate/candidate_parses.py

## Governing Overview

[Application overview](../overview.md)

## Purpose

Keeps reusable parses of exact candidate memory snapshots for the leaf knowledge gate.

## Code Commentary

The shared memo retains up to eight entries under a combined 256 MiB budget for reachable Python objects. Each key combines the snapshot location and tree identity. Insertion checks the graph weight before copying a parse into the memo. Oversized parses remain available to the current gate evaluation.

## Relationships

The gate snapshots the candidate memory tree for each evaluation. It reuses a deep copy when the stored files match the current snapshot and still opens the candidate code tree.

## Evidence

- Candidate parse insertion uses the retained graph budget. [1]
