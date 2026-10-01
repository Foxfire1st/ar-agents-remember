# dashboard/src/panels/session-cockpit/sessionRailStyles.ts

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Defines the one-line visual grammar for the structural Chats hierarchy and its live occupant rows.

## Code Commentary

### Logic

Sprint, master, leaf, and row styles preserve nesting while `rowShell`, `rowLabelGroup`, and
`rowTitle` constrain live labels. The title uses hidden overflow, ellipsis, and no wrapping so a
replacement or long label cannot expand the rail row vertically.

### Conventions

Structural indentation belongs to sprint/master/leaf containers; runtime state appears as compact
chips inside the row.

### Invariants And Boundaries

- Live row labels are single-line CSS ellipsis.
- Structural nesting must remain visible independently of occupant status.
- Styling must not encode an alternate identity or hierarchy.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

### Repo-Internal References

- Master and leaf containers express real task nesting. [1]
- Row layout constrains identity and action segments. [2]
- The live title is clipped to a single ellipsized line. [3]

### Cross-Repo References

No cross-repository implementation dependency governs this file.

## L23 Final Candidate Disposition

Master, leaf-group, and outer group boxes constrain their grid tracks with `minmax(0, 1fr)`,
`minWidth: 0`, and `maxWidth: 100%`. Long labels or nested task rows can shrink inside the rail and
cannot visually flatten or erase the sprint/master grouping.
