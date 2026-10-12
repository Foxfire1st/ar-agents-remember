# dashboard/src/panels/detail-panel/order-block.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Pin inline sprint wave rows, whole graph navigation and shared delayed pointer marking.

## Code Commentary

Cases inspect server-projected wave/state rows, completed counts, target navigation and a whole graph with edge reasons one link away. Controlled time distinguishes pass-through pointers from rested selection; neighbor movement retains the prior mark until the next rest, keyboard focus marks immediately, and reduced motion removes the fade without removing the rest.

## Boundaries

This card describes the executable assertions and fixture seams of this module. It does not turn a mocked or seeded unit observation into system-wide acceptance. Keep fixture provenance, controlled time and actual producer opportunities explicit when extending the cases.

## Evidence

- The module owns the regression assertions and fixture boundaries described above. [1]
