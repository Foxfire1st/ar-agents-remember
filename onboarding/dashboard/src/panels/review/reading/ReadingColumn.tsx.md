# dashboard/src/panels/review/reading/ReadingColumn.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Render sticky reading head plus permanently mounted notes, active subjects, lane, retained canvas slot and provenance.

## Code Commentary

### Logic

Render sticky reading head plus permanently mounted notes, active subjects, lane, retained canvas slot and provenance. One remembered code-context switch. Measure head for scroll padding; page-level pending reads do not tear down the column. Worklist replaces summary/subjects/lane when selected.

### Invariants And Boundaries

This file consumes comparison and owner state; it does not author knowledge or decide task acceptance.

## Evidence

- Render sticky reading head plus permanently mounted notes, active subjects, lane, retained canvas slot and provenance. [1]
- Render sticky reading head plus permanently mounted notes, active subjects, lane, retained canvas slot and provenance. [2]
- Render sticky reading head plus permanently mounted notes, active subjects, lane, retained canvas slot and provenance. [3]
