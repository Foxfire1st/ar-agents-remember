# dashboard/src/panels/review/reading/pageParts.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Wire page model into tree, context, subject slot, notes and top-line controls.

## Code Commentary

### Logic

Wire page model into tree, context, subject slot, notes and top-line controls. The notes area also carries the delivered line: `PageNotes` renders `DeliveredLine` from the page's own delivered value and its delivered action, so the notice adds no surface and no layout of its own. Use projection title, served repository id, model-order family roster; an orphan selected subject gets its own visible slot. Worklist count/status stay typed. The resolved task context supplies status independently from selected-subject failures. Crumb follows selection, not scroll.

The older-comparison note names the comparison the page resolved rather than the highest record, and the slot's own older state uses the same resolved figure. The top-line controls receive both the resolved comparison and the delivered value so the selector can offer the delivered row and mark the number that holds it. The selector gets two callbacks: a numbered row chooses a number and keeps a recorded frame, while the delivered row asks for the page's delivered action, which leaves that frame; the older-comparison note's own control chooses the resolved number, so it keeps the frame as well.

### Invariants And Boundaries

This file consumes comparison and owner state; it does not author knowledge or decide task acceptance.

## Evidence

- Wire page model into tree, context, subject slot, notes and top-line controls. [1]
- Wire page model into tree, context, subject slot, notes and top-line controls. [2]
- Wire page model into tree, context, subject slot, notes and top-line controls. [3]

- The delivered line sits in the page's existing note area, from the page's own delivered value. [4]
