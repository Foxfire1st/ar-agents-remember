# dashboard/src/panels/detail-panel/orderGraph.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Own shared sprint/master Order previews, the complete projected-graph own view and the ready-only Can start next display using producer-owned execution facts.

## Code Commentary

The inline block resolves graph targets through the shared task-entry map. Its now row contains entries whose activity is works; other unfinished entries stay in ascending producer wave order, ready graph units first within each wave. Completed and aborted entries are excluded using their entry stage. The separate done/abandoned graph totals are removed, not substituted for Completed-list counts. Its link opens the whole existing SprintGraphView, retaining every unit and edge reason. A missing projected target keeps its graph mark/place but has no navigation. Task totals exclude abandoned rows; segmented nodes use their projected leaf IDs. An unfinished wave containing a cycle-marked node gets a cycle label naming every cycle-marked projected node in that wave, including completed members. Cycle-membership text reads the full supplied node list even when a finished member has no inline mark. When all members are finished there is no unfinished wave row to label. This reads producer annotations; it does not recompute SCCs or confer readiness. Master mode labels the units as tasks and names their waitsFor fields as the supplied graph source; projected leaf targets show served stepsDone/stepsTotal rather than master task totals. CanStartNext renders only graph-ready nodes resolving to planned entries and introduces no start action. Task words use taskStatusKey/statusLabel/StatusWord from pageParts. A started graph target gets the restored golden work border even when host activity is paused or unavailable; remaining targets use the producer's ready/waits distinction. The border and its in-work legend do not assert that the host is currently working. Graph readiness remains a separate dependency annotation, not a second task-stage word.

Both views share useRestHighlight and relation mappings from the graph owner. Pointer pass-through remains inert until the rest; moving to a neighbor retains the old highlight until the next rest. Keyboard focus marks at once. Reduced motion removes the fade, not the rest. Relation text omits finished predecessors/successors but does not change the authoritative graph.

## Boundaries

Order targets resolve canonical references in the shared tasks map and use entry major-step/child counts. Missing targets stay inert. No front-end wave/frontier inference, native task edit, scheduler or new graph model is introduced. The all-graph view remains the existing producer projection consumer.

## Evidence

- The graph restores the work border for started task entries independently of host activity, using readiness only for other targets. [3]


- Order uses entry stage/activity and the shared status presentation while retaining producer dependency waves/readiness; graph-derived done/abandoned totals are absent, and the own graph view retains the supplied graph. [1]

- OrderRowsView wires pointer rest and immediate focus to shared graph highlighting, with reduced motion disabling fade and relations omitting finished dependencies. [2]
