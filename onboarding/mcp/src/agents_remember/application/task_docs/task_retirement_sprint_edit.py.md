# mcp/src/agents_remember/application/task_docs/task_retirement_sprint_edit.py

## Governing Overview

[task_docs overview](overview.md)

## Purpose

The sprint edit of a retirement: one validated candidate that no longer commands the master. Pure candidate construction: it removes the master's membership entry, its graph node and every edge touching it, and leaves one plain row that records the retirement.

## Code Commentary

`retirement_sprint_edit` removes the membership, removes the node (refusing a graph whose only node is the master through `_require_graph_keeps_a_node`), removes the touching edges (`_remove_edges`) and writes the retirement row. The row takes the place of the master's typed row, or of the one legacy seat row that correlates with the master; a sprint that holds no row for the master gains the row at the end of its list with a free number (`_free_row_number`). `new_proof` builds the proof record with the reason, time, removed membership, node count, removed edges, affirmed edges and source digests.

## Evidence

- The sprint edit removes the master's membership, graph node and touching edges and leaves one plain retirement row. [1]
- A new retirement row never takes a number that is in use. [2]
- A sprint that holds no row for the master gains the retirement row at the end of its list. [3]
