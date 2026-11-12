# dashboard/src/explainer/ExplainerTaskDocument.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Retire on the leaf task document: the same control and the same two-list confirmation as the chat header, reading the leaf's authoritative explainer state when the document is opened cold.

## Code Commentary

- A cold task document reads the leaf's state once when no seat is known, and shows nothing at all when the leaf has no explainer.
- Publication is the one truth the review column and the task document share, held by reference so an external-store snapshot compares by identity rather than by value.
- The seat cache is bounded, and every publication also registers the target for the tray's archived lookups, marking the seat active only while it is live or closed.
- Retire posts once with a stable receipt id; an unfinished retirement keeps the confirmation open so a retry finishes under the same receipt, and the remaining pids are named.
- The control appears only for a leaf entry: a master or sprint entry never shows it, and a control whose seat ended still names what the last explainer was.

## Evidence

- Publishing a seat registers its agent and marks it active only while that seat is live or closed [1]
- A leaf entry is a task, a subtask, or an entry with no children, never a master or sprint [2]
- The viewed leaf document is resolved to its repository, master folder and leaf id before the control mounts [3]
- The known seats and their listeners can be emptied between tests [4]
