# mcp/src/agents_remember/application/task_docs/task_sprint_candidates.py

## Governing Overview

[task_docs overview](overview.md)

## Purpose

The pure sprint detachment candidate, shared by `detach_master` and by explicit master retirement, and the
`SprintLinkageError` family of the sprint linkage operations. It reads and writes nothing; callers validate and publish
what it builds.

## Code Commentary

### Logic

`_detach_candidate(sprint, master_ref, master)` returns the sprint document with the master removed, the removed
`orchestrates` entries and the number of removed graph nodes. On a graphed sprint it first refuses while an edge still
touches the master (`_require_no_touching_edges`, status `task-sprint-linkage-node-in-use`), and refuses when removing
the node would leave the graph empty (`task-sprint-linkage-graph-empty`). It drops the master's typed rows, removes the
`orchestrates` aliases that name the master (its folder name, and its id and title when the document resolved), and
rebuilds the graph from the remaining nodes and the untouched edges. The result is re-validated as a `TaskDocument`.

Retirement removes the master's edges first, then calls `_detached_data` directly and installs the retained retirement
row before validating the final document. Ordinary detachment uses `_detach_candidate`, which validates the raw data.
This ordering preserves sprint identity when retirement removes the last graphless commanded master.

### Conventions

- `SprintLinkageError` extends `AgentsRememberError`; statuses are `task-sprint-linkage-*`.

### Invariants And Boundaries

- Detaching never deletes files and never leaves an edge pointing at a removed node.
- The graph cannot be emptied by a detachment; the message says the graph has no retire operation, and retirement of a
  sprint's only graphed master is refused separately with its own message.

## Evidence

- The detach candidate removes the rows, aliases and node, refuses to empty the graph and rebuilds a valid document. [1]
- A node with a touching edge cannot be detached. [2]
- The error family of the linkage operations. [3]
