# dashboard/src/data/taskDocumentBodyCurrentness.test.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

Pin current-summary facts and matching-body preview restoration in the task-body hook.

## Code Commentary

Mocked fetches settle before newer summary delivery. Cases distinguish fresh status/header/type/step/review facts from body-provided long content, then restore truncated strings and larger collections only for a matching revision. A changed revision preserves its immediate newer summary while the next request is pending.

## Boundaries

This card describes the executable assertions and fixture seams of this module. It does not turn a mocked or seeded unit observation into system-wide acceptance. Keep fixture provenance, controlled time and actual producer opportunities explicit when extending the cases.

## Evidence

- The module owns the regression assertions and fixture boundaries described above. [1]
