# dashboard/src/cockpit/role-launcher/useLauncherSelectionRepair.test.ts

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Specify repair payloads, first-invalid priority and selected hook scheduling cases.

## Code Commentary

Document cases retain the reset payloads and first-invalid sprint/master/task order. Hook cases check repair when task entries arrive and quiescence for valid document selections. Catalog override-pruning cases were removed with their production helpers.

## Boundaries

The tests do not prove catalog override repair or a combined effect arbitration contract. StrictMode and every catalog-arrival sequence are not implied.

## Evidence


- The test file asserts seeded document correction payloads, first-invalid document order, document-arrival scheduling and quiescent valid selections; catalog override-pruning cases are removed. [1]
