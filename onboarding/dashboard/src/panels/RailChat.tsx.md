# dashboard/src/panels/RailChat.tsx

## Governing Overview

[panels overview](overview.md)

## Purpose

Hosts Chats over the task-document hierarchy. It selects the current occupant of a structural
document-and-role seat, supports task assignment, and keeps free-chat/terminal behavior outside the
task hierarchy.

## Code Commentary

### Logic

The session hook joins a selected `TaskDocumentRef` to live catalog sessions and role. Task-bound
launches pass that reference into the opener; assignment resolves the selected leaf document and
posts the reference plus role. Leaf keys remain only for legacy context-package content and display.
The rendered panel uses the current occupant id for transport after structural selection.

### Conventions

Task-document selection comes from the projected real document. Free chat is represented by an
unbound chat session, not by a manufactured task address.

### Invariants And Boundaries

- Task-bound chat selection never searches globally by role.
- Replacement keeps the same task-document-and-role selection.
- Free chat and shell terminal affordances are not inserted into the structural task tree.
- Runtime ids remain behind the selected occupant/transport seam.

### Todos

Leaf-key context packaging remains a non-addressing presentation path and should stay clearly
separated from structural seat lookup.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Selected structural identity resolves the current live chat occupant. [1]
- Task assignment derives and sends a real task-document reference. [2]
- The panel accepts structural task identity separately from leaf display context. [3]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
