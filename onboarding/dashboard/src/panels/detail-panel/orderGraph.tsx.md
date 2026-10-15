# dashboard/src/panels/detail-panel/orderGraph.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Own shared sprint/master Order previews, the complete projected-graph own view and the ready-only Can start next display using producer-owned execution facts.

## Code Commentary

The inline block draws a now row when work is in flight, then unfinished units grouped by ascending server wave; ready units come first within a wave without reordering their peers. Landed and abandoned units are counts, not extra inline rows. Its link opens the whole existing SprintGraphView, retaining every unit and edge reason. A missing projected target keeps its graph mark/place but has no navigation. Task totals exclude abandoned rows; segmented nodes use their projected leaf IDs. An unfinished wave containing a cycle-marked node gets a cycle label naming every cycle-marked projected node in that wave, including completed members. Membership text reads the full supplied node list, while landed/abandoned nodes remain counts only and never regain inline marks. When all members are finished there is no unfinished wave row to label. This reads producer annotations; it does not recompute SCCs or confer readiness. Master mode labels the units as tasks and names their waitsFor fields as the supplied graph source; projected leaf targets show served stepsDone/stepsTotal rather than master task totals. CanStartNext renders only frontierState ready nodes and introduces no start action.

Both views share useRestHighlight and relation mappings from the graph owner. Pointer pass-through remains inert until the rest; moving to a neighbor retains the old highlight until the next rest. Keyboard focus marks at once. Reduced motion removes the fade, not the rest. Relation text omits finished predecessors/successors but does not change the authoritative graph.

## Boundaries

No front-end wave/frontier inference, native task edit, scheduler or new graph model is introduced. The all-graph view remains the existing producer projection consumer.

## Evidence


- Order renders supplied wave/frontier facts for sprint masters or master tasks; cycle labels read full marked membership while finished nodes remain counts only, and the own graph view retains the supplied graph. [1]

- OrderRowsView wires pointer rest and immediate focus to shared graph highlighting, with reduced motion disabling fade and relations omitting finished dependencies. [2]
