# mcp/src/agents_remember/memory/conversion/state_files.py

## Governing Overview

[Governing overview](../overview.md)

## Purpose

Reads conversion inputs and publishes the planned report and memory files with recovery on failure.

## Evidence

- The input reader detects an unsuccessful knowledge JSON load. [1]
- Publication checks the planned inputs and reports any targets changed after failed rollback. [2]
