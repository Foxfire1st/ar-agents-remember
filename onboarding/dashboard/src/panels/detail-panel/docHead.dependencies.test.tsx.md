# dashboard/src/panels/detail-panel/docHead.dependencies.test.tsx

## Governing Overview

[Area overview](../overview.md)

## Purpose

Declare mounted head assertions for both preprojected dependency directions and navigation of addressable targets.

## Code Commentary

Supplied waitsForTasks/neededByTasks assert direction labels, state wording, selection-key navigation and a disabled gone target without a document path. A separate case omits absent/empty directions.

The fixture already contains the direction arrays: it does not derive reverse links, validate dependency writes or exercise body/corpus schema admission. Reading these assertions is not an executed test or live producer result.

## Evidence


- Preprojected dependency-head cases assert direction/state/navigation and absent/empty omission, not backend derivation. [1]
