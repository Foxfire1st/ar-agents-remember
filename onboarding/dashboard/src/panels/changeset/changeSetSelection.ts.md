# dashboard/src/panels/changeset/changeSetSelection.ts

## Governing Overview

[overview](overview.md)

## Purpose

Builds the selected change set's diff request and media selector.

## Code Commentary

Numbered comparison takes precedence before leaf, master and enclosure scope. Leaf requests default to committed mode. Master requests retain supplied generation pins. Both text diff and media presentation receive the selected range's identity.

## Relationships

ChangeSetViewer supplies the current target. This module renders no UI, changes no history and reads no file bytes.

## Evidence

- Builds the selected change set's diff request and media selector. [1]
