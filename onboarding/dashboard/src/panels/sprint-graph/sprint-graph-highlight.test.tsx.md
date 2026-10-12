# dashboard/src/panels/sprint-graph/sprint-graph-highlight.test.tsx

## Governing Overview

[Route overview](overview.md)

## Purpose

Pin controlled rest, neighbor continuity, focus and reduced-motion behavior of the sprint graph.

## Code Commentary

A passing pointer leaves no marks; a rested pointer marks the selected node and relations, and crossing to a neighbor does not blank the graph. Leaving clears after the shared rest. Keyboard focus marks without advancing time; reduced motion drops fade but preserves the rest boundary.

## Boundaries

This card describes the executable assertions and fixture seams of this module. It does not turn a mocked or seeded unit observation into system-wide acceptance. Keep fixture provenance, controlled time and actual producer opportunities explicit when extending the cases.

## Evidence

- The module owns the regression assertions and fixture boundaries described above. [1]
