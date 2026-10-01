# dashboard/src/panels/session-cockpit/sessionRailParts.tsx

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Contains the row, master block, attention, and rail-body renderers for the structural Chats tree.

## Code Commentary

### Logic

`RailMasterBlock` renders master and leaf containment, while `RailBody` walks sprint sections and
their current occupants. `RailRow` treats the occupant id as an action/focus target but renders task
and role identity supplied by the model.

### Conventions

Structure is passed in; this module does not infer parentage from spawn ids or labels.

### Invariants And Boundaries

- One structural row remains stable when its occupant changes.
- Row actions target the currently rendered occupant only.
- Empty and attention states do not manufacture a fallback seat.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Individual rows separate structural label from occupant actions. [1]
- Master blocks render the supplied task containment. [2]
- The rail body renders sprint/master/leaf sections. [3]

### Cross-Repo References

No cross-repository implementation dependency governs this file.
