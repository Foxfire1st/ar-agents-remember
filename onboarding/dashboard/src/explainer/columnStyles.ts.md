# dashboard/src/explainer/columnStyles.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The column's styles in one place, drawn from by the shell, the header, the placeholder, the first request's form, the build panel and Retire's confirmation.

## Code Commentary

- The column is a flex column that does not scroll; each block scrolls inside its own body so a long build or a long reference list stays contained.
- Buttons are quiet by default, primary for Send and danger for Retire's confirm, and a disabled primary dims rather than disappearing.
- Notices are amber and failures take the danger colour, so a read problem and a failed step are distinguishable at a glance.
- Every block shares the same monospace scale, muted second lines and card framing, so a phase change does not change the column's shape.

## Evidence

- The block body scrolls inside a column that does not [1]
- Each block is framed as a card over the panel background [2]
- The primary Send button dims and stops taking a press while disabled [3]
- A notice is amber, distinct from a failure line [4]
- Failures are drawn in the danger colour [5]
