# dashboard/src/panels/detail-panel/selection-state.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Pin document-local expansion state across task, master and sprint selection.

## Code Commentary

Switching documents closes the objective, note expansion and own view. Refreshing the same document preserves an opened objective while updating its status. These cases discriminate document identity from transient projection-object identity.

## Boundaries

This card describes the executable assertions and fixture seams of this module. It does not turn a mocked or seeded unit observation into system-wide acceptance. Keep fixture provenance, controlled time and actual producer opportunities explicit when extending the cases.

## Evidence

- The module owns the regression assertions and fixture boundaries described above. [1]
