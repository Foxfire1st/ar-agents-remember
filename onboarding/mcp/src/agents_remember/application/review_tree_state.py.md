# mcp/src/agents_remember/application/review_tree_state.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Own per-side currentness and governing history-row projection extracted from review_tree_knowledge.

## Code Commentary

`side_currentness` checks every invariant/family against its own side’s code tree through the shared currentness function, while serializing only non-current entries; index state and unreadable-side reasons remain explicit. `history_rows` reads after-index rows for each item subject and facts.row. `_governing` keeps each owner’s latest attempt among those rows; older frozen attempts stay in history and the selected subject judgment pane may show them all. These are display/currentness projections, not the gate’s item verdict or a new row-satisfaction rule.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. Requirement packets are task authority, not an implementation proof or a fresh acceptance.

### Repo-Internal References

- Each side’s full currentness check is retained while current entries are omitted from the response list. [1]
- Item-related after-tree rows are projected from their actual history sources. [2]
- The latest attempt is selected independently per owner, not by row recency. [3]
