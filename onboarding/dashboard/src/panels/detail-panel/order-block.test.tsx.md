# dashboard/src/panels/detail-panel/order-block.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Pin inline sprint wave rows and master task Order/ready-next rows, whole graph navigation and shared delayed pointer marking.

## Code Commentary

Cases inspect server-projected wave/state rows, completed counts, target navigation and a whole graph with edge reasons one link away. Controlled time distinguishes pass-through pointers from rested selection; neighbor movement retains the prior mark until the next rest, keyboard focus marks immediately, and reduced motion removes the fade without removing the rest. The added master case requires Order immediately after Now, only ready L2 under Can start next, one landed item counted rather than drawn, waiting L3 with projected `1/5`, and the exact leaf `taskdoc:` navigation key. Controlled `GRAPH_REST_MS - 1` then one millisecond asserts no mark before rest, L3 self/L1 related after rest, and fade retained. The master assertion also pins the relation text with no open successor. A separate two-state legacy cycle control supplies completed and unfinished/all-completed marked members: it asserts completed counts, no drawn completed node, no ready-next block, both member titles in the remaining cycle-wave label, and no wave row when all members are complete. These are source-inspected component assertions over made-up graph rows, not a native SCC producer opportunity or a fresh test run.

## Boundaries

This card describes the executable assertions and fixture seams of this module. It does not turn a mocked or seeded unit observation into system-wide acceptance. Keep fixture provenance, controlled time and actual producer opportunities explicit when extending the cases.

## Evidence

- Sprint display/whole-graph and rest/focus/reduced-motion assertions remain; the seeded master case pins placement, ready-only next tasks, projected progress, relation text and exact navigation. Source inspection only. [1]

- Seeded mixed/all-completed cycle assertions name both legacy members where a wave remains, retain completed nodes as counts only, and omit an all-completed wave and ready-next block. This is not a native SCC producer opportunity or new execution. [2]
