# dashboard/src/cockpit/roleChatOptionsLoader.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Load options/catalog data and restore exact saved request selection.

## Code Commentary

The effect and manual Refresh own scoped catalogue metadata and receipt restoration. Each load asks for the disk snapshot alongside fresh metadata without sending `agentId`. The effect depends on `hasBoundSelection = Boolean(args.boundSelection)` rather than the `boundSelection` object reference, so unrelated SSE task updates that replace `boundSelection` with an equal selection do not abort or refire launcher reads. A one-shot `resultReadRef` marker from a settled dispatch (consumed on non-retry, non-catalog-refresh loads for the same document scope) preserves `executionState` for that `requestId` and skips a duplicate `POST /api/role-launch/result` read in `adoptRequestExecutionState`. The snapshot is accepted while the matching metadata is pending and cleared when it settles. A fresh metadata success acknowledges its generation before the pane requests features for the shown model. The page remembers the last settled role defaults for each role and document scope, so the snapshot can be offered with those defaults rather than empty ones; inventories are still never merged. Abort, active-lifetime, canonical-scope and completion guards reject stale answers; periodic refresh cleans up its timer. Saved request and retry restoration retain exact UUID and references. A singular failure-only execution updates the failure channel without replacing an already selected Result receipt.

## Boundaries

Automatic refresh and an explicit successful action have distinct sticky-error clearing rules. Role and document references define options scope, not agent overrides, native chat ownership or task acceptance.

## Evidence

- useRoleChatOptionsLoader is a current owner of the behavior described above. [1]

- applyOptionsSuccess is a current owner of the behavior described above.
