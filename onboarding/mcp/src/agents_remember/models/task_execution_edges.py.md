# mcp/src/agents_remember/models/task_execution_edges.py

## Governing Overview

[models overview](overview.md)

## Purpose

The canonical endpoint and edge schemas of a sprint's execution graph, shared by the task-document model
(`tasks/document.py`) and the master-retirement proof (`models/task_retirement.py`). They live here so that the proof can
use them without importing the task-document module.

## Code Commentary

### Logic

`SprintExecutionEndpoint` is a bare master reference, or a reference with a `leafId` that samples the segment
containing that leaf; a blank `leafId` is refused, and resolution to a node happens in graph validation, never at
parse time. `SprintExecutionEdge` is a reasoned predecessor and successor pair with an optional `judgmentId`; a blank
reason or judgment id is refused, and an edge from a node to itself is refused.

### Conventions

- Both models extend a strict base (`extra="forbid"`, populate by name).
- `tasks/document.py` imports these models; their behavior is unchanged from when they were defined there.

### Invariants And Boundaries

- An edge cannot point a node at itself, and its reason cannot be blank.

## Evidence

- An endpoint is a reference with an optional non-blank leaf id. [1]
- An edge has a non-blank reason, an optional non-blank judgment id and distinct endpoints. [2]
