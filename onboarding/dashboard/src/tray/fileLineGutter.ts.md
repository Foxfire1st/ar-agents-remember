# dashboard/src/tray/fileLineGutter.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Adds accessible line/range picks to the dashboard file viewer.

## Code Commentary

### Logic

One line control is keyboard reachable; pointer/keyboard additions form scoped file-line references; Shift extends the remembered anchor and replaces that anchored range; existing covered lines reflect in-tray state.

### Invariants And Boundaries

Plain repeat additions inside an existing range do nothing. Scope/path/range, not visible text, identify the file pick. Viewer navigation stays with CodeMirror.

## Evidence

- Adds accessible line/range picks to the dashboard file viewer. [1]
- Adds accessible line/range picks to the dashboard file viewer. [2]
- Adds accessible line/range picks to the dashboard file viewer. [3]
