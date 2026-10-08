# mcp/src/agents_remember/memory/conversion/crossing_sync.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Plans a converted/unconverted memory crossing from the actual three input trees before the transaction applies it.

## Code Commentary

`cross` classifies the three sides by their markers. Three converted sides use structural merge without a conversion; mixed sides use pinned conversion and marker/history ownership before merge and validation. Three unconverted sides do not enter this crossing route. The plan carries files, conflicts and counts; the transaction owner applies and stages it. The removed is_crossing helper is not a current classifier or alternate writer. This module's plan is not an acceptance or a grant to mutate a repository.

## Evidence

### Repo-Internal References

- `cross` owns the current boundary described above. [11]
- `_convert_sides` owns the current boundary described above. [12]
- `next_crossing_owner` owns the current boundary described above. [13]
