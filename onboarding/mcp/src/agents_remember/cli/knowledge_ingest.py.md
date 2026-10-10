# mcp/src/agents_remember/cli/knowledge_ingest.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Contract-addressed CLI entry for curator knowledge-file writing.

## Code Commentary

### Logic

add_arguments requires contract, list and authorization-ref. commit writes knowledge files; absent commit plans/validates and writes nothing. json emits the report, config supplies task-question authority when needed, and crossing selects master-line conflict history. Candidate-directory, baseline, expected-destination and publication options were removed. [1]

run loads the contract once, dispatches crossing to run_crossing_write, converted memory to run_leaf_write, and refuses unconverted memory with the conversion route. [2]

### Invariants And Boundaries

- The contract fixes source and memory scope.
- The commit word writes knowledge, never Git history or acceptance.
- There is no canonical database fallback.

### Conventions

Module-level definitions follow the package conventions, matching its seven sibling CLI adapters; names
prefixed with `_` are private to this module. Argument declaration and dispatch are split the same way
they are in `memory_citations.py` and `memory_backfill.py`: `add_arguments` owns the parser surface and
`run` owns the behaviour, so the parser can be exercised without running the operation.

## Evidence

### Repo-Internal References


- Current file-writer arguments. [1]


- File-only dispatch. [2]


- The admitted CLI dispatches crossing and refuses unconverted memory by name. [33]


### Cross-Repo References

No cross-repository contract is established by this file.
