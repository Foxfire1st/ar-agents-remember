# mcp/src/agents_remember/providers/lifecycle/state_files.py

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`state_files.py` owns JSON state file reads and writes for provider lifecycle
modules.

## Code Commentary

### Logic

The module returns an empty dict for absent JSON state files and writes
deterministic, sorted, indented JSON with a trailing newline.

### Invariants And Boundaries

- State file helpers do not interpret provider state.
- Callers own schema decisions and error handling around loaded data.

## Evidence

### Repo-Internal References

- CGC and GrepAI lifecycle modules use these helpers for provider state and image locks. [1]
- Provider settings reads reuse the JSON loader. [2]
