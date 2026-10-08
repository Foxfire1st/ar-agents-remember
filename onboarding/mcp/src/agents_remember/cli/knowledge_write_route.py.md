# mcp/src/agents_remember/cli/knowledge_write_route.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

The converted knowledge CLI's file-write routes share admission, owner identity, decision inputs and report rendering.

## Code Commentary

Leaf writes use the supplied enclosure and its leaf owner; named waves use their admitted repository root. Crossing writes retain their separately admitted crossing owner. Each delegates to the file writer rather than selecting a canonical database. `unconverted_write_refusal` supplies the typed legacy/cutover refusal. Database-publication arguments are refused by their CLI front door, not accepted here as an alternative destination. The removed `_file_route_refusal` and legacy dataset writer dispatch are not current routes.

## Evidence

### Repo-Internal References

- `run_leaf_write` owns the current boundary described above. [17]
- `run_wave_write` owns the current boundary described above. [18]
- `run_crossing_write` owns the current boundary described above. [19]
- `unconverted_write_refusal` owns the current boundary described above. [20]
