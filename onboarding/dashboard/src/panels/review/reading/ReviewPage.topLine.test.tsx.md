# dashboard/src/panels/review/reading/ReviewPage.topLine.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Guard top-line status, historical comparison reads and the remembered code-context control.

## Code Commentary

### Logic

Exercises the status model's owner-supplied current/moved/not-measured/unavailable states and first-sentence reasons, then mounts its reading state and four-row popover. It pins reserved comparison/tray-control widths and the refresh notice's separate row without replacing the chip. Older selection sends its number on catalogue, summary, tree and file reads and suppresses fresh subject reads. The code-context switch persists across remount, controls unchanged-line folding and keeps its own selected style; width helpers select split layout at 1080px of content. Final cases assert comparison-menu labels/times and popover placement/declarations.

### Invariants And Boundaries

Times, request answers, element widths and control geometry are controlled. Class/DOM checks do not establish actual pixel positions, colour cascade or native browser width behavior.

## Evidence

- Status facts, stable chip/control slots, generation notice and subject-failure separation. [4]
- Older-number reads, code-context persistence and the mocked content-width threshold. [5]
- Comparison labels/times, shell inset declarations and status-popover structure. [6]
