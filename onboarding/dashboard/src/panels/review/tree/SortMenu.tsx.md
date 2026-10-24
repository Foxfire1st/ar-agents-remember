# dashboard/src/panels/review/tree/SortMenu.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

One persisted sort menu with deterministic, memory and supplied judgment-category sections.

## Code Commentary

### Logic

Render the persisted sort menu with separate Always available, Memory and conditional Explainer’s judgment sections. Judgment sorts are filtered out of the deterministic section and drawn in their own group only when supplied. The four memory sorts retain their existing missing-value reason and Priority fallback; the requested preference is not discarded. This menu only presents supplied SortOption values and changes the existing preference owner; it does not calculate grades or start an explainer.

### Invariants And Boundaries

This file consumes comparison and owner state; it does not author knowledge or decide task acceptance.

## Evidence







- Render the persisted sort menu with separate Always available, Memory and conditional Explainer’s judgment sections. Judgment sorts are filtered out of the deterministic section and drawn in their own group only when supplied. The four memory sorts retain their existing missing-value reason and Priority fallback; the requested preference is not discarded. This menu only presents supplied SortOption values and changes the existing preference owner; it does not calculate grades or start an explainer. [4]

- SortItem renders one supplied deterministic or judgment option with its chosen mark and its hint or explicit unavailable reason. [1]

- memoryHint reports the first unavailable memory-sort reason or says values come from the after-side index; it does not describe judgment-category availability. [2]

- SortMenu renders Always available and Memory facts groups plus a conditional Explainer’s judgment group, disables supplied unavailable options and keeps the requested preference distinct from the applied sort. [3]
