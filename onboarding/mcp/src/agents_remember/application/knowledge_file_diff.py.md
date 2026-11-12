# mcp/src/agents_remember/application/knowledge_file_diff.py

## Governing Overview

[mcp/src/agents_remember/application/overview.md](overview.md)

## Purpose

The bounded Git diff of knowledge files that knowledge_diff serves.

## Code Commentary

The module computes the diff between the recorded and working knowledge files, cuts it at the shared knowledge-read token threshold and names the omitted files and cuts so a caller never reads a silent truncation.

## Evidence

No separate reference list: the file's sidecar carries the realization entries this leaf re-anchored.
