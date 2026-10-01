# mcp/src/agents_remember/providers/cgc/lifecycle/__init__.py

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`cgc.py` is the CodeGraphContext lifecycle export facade. It groups the split
CGC implementation modules behind one import surface for `providers.lifecycle`.

## Code Commentary

### Logic

The module re-exports CGC backend, core settings/layout, runner, installation,
process-control, refresh, and query lifecycle functions. It intentionally
contains no behavior beyond those exports.

### Invariants And Boundaries

- Keep this module import-only.
- Put CGC implementation in the focused `cgc_*` modules.

## Evidence

### Repo-Internal References

- The parent lifecycle facade imports this CGC facade. [1]
- The CGC core module in the exported surface. [2]
- The CGC backend module in the exported surface. [3]
- The CGC runner module in the exported surface. [4]
- The CGC installation module in the exported surface. [5]
- The CGC process-control module in the exported surface. [6]
- The CGC refresh module in the exported surface. [7]
- The CGC query module in the exported surface. [8]
