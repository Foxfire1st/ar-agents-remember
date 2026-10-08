# mcp/tests/test_series_finalize_rules.py

## Governing Overview

[tests overview](overview.md)

## Purpose

What finalizing a master decides again, reads, and refuses by name. Finalization completes a master's document and its sprint row; it decides once more that no abandoned row has landed, it reports an unreadable sibling as a fact only when that sibling's canonical identity is established, it refuses an unbound title with a named unresolved identity and the canonical-folder repair, it does not finalize a task whose own document cannot be read, and it refuses a master that several sprints command with the edit that works on each of them.

## Code Commentary

`_finalize` and `_blocked` drive the finalize route and read its refusal. The cases cover an abandoned row that landed and one that did not, an unreadable enclosure of an abandoned row, another unreadable member reported by file, a seat row found by its file, a missing member, canonical identity for an unreadable member, a readable admitted title member, a missing admitted canonical member, duplicate and foreign typed refs, an unreadable own document, and several commanding sprints.

## Evidence

- Finalization refuses an abandoned row that landed and names the row, for masters of either nature. [1]
- A proven canonical unreadable sibling is reported as a fact; an unbound title and a missing member refuse by name. [2]
- An unreadable proven canonical sibling is reported as a fact without changing its membership, row, node or bytes; an unbound title is a named unresolved identity. [3]
