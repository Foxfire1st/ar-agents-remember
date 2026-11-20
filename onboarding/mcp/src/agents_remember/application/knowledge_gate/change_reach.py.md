# mcp/src/agents_remember/application/knowledge_gate/change_reach.py

## Governing Overview

[Governing overview](../overview.md)

## Purpose

Determines whether changes reach a dependent document through its file, anchor or stable record links.

## Evidence

- The path reader identifies record IDs from knowledge record filenames. [1]
- The reach check compares file and anchor paths and record-link IDs with the changed sets. [2]
