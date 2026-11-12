# dashboard/src/panels/review/reading/ReviewPage.selection.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Guard review-page selection, URL restore, keyboard routing and selected-content composition.

## Code Commentary

### Logic

Checks one subject read and one post-answer column landing, cancelled by reader scrolling, while tree nodes and scroll position survive. URL cases restore entry, lane and hunk selections, reject foreign trees or unowned spans, and let an explicit reader choice supersede a pending restore without another landing. Keyboard cases cover block j/k, body j, ignored field j/[ and Ctrl+j, plus bracket sidebar wiring. Selected-subject cases check text IDs and quiet absent-family state; heading/meta/word-diff/steps/judgment precede code, remaining content follows it, provenance stays in Technical details, and carried revisions name their source writer.

### Invariants And Boundaries

Transport and scroll geometry are stubbed, and selected answers are deliberately rebased/edited fixture data. Composition checks establish DOM order and state attributes, not rendered typography or native viewport behavior.

## Evidence

- Subject-read/landing ownership, URL restore admission and reader-choice precedence. [4]
- Keyboard routing and text IDs without synthesized raw state tokens. [5]
- Selected content order, measure state, provenance placement and carried-writer chip. [6]
