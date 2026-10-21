# dashboard/src/panels/review/reading/pageParts.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Wire page model into tree, context, subject slot, notes and top-line controls.

## Code Commentary

### Logic

Wire page model into tree, context, subject slot, notes and top-line controls. Use projection title, served repository id, model-order family roster; orphan selected subject gets own visible slot. Worklist count/status stay typed. Latest task context supplies status independently from selected-subject failures. Crumb follows selection, not scroll.

### Invariants And Boundaries

This file consumes comparison and owner state; it does not author knowledge or decide task acceptance.

## Evidence

- Wire page model into tree, context, subject slot, notes and top-line controls. [1]
- Wire page model into tree, context, subject slot, notes and top-line controls. [2]
- Wire page model into tree, context, subject slot, notes and top-line controls. [3]
