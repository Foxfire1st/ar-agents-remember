# dashboard/src/panels/detail-panel/orderGraph.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Own the sprint Order preview and its whole-graph own view using producer-owned execution facts.

## Code Commentary

The inline block draws a now row, then unfinished units grouped by ascending server wave; ready units come first within a wave without reordering their peers. Landed and abandoned units are counts, not extra inline rows. Its link opens the whole existing SprintGraphView, retaining every unit and edge reason. A missing projected master keeps its graph mark/place but has no navigation. Task totals exclude abandoned rows; segmented nodes use their projected leaf IDs.

Both views share useRestHighlight and relation mappings from the graph owner. Pointer pass-through remains inert until the rest; moving to a neighbor retains the old highlight until the next rest. Keyboard focus marks at once. Reduced motion removes the fade, not the rest. Relation text omits finished predecessors/successors but does not change the authoritative graph.

## Boundaries

No front-end wave/frontier inference, native task edit, scheduler or new graph model is introduced. The all-graph view remains the existing producer projection consumer.

## Evidence

- The Order preview preserves projected wave/frontier facts and keeps the complete graph one link away. [1]
- The shared rest/focus/reduced-motion behavior governs inline relations. [2]
