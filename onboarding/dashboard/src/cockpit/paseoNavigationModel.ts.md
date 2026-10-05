# dashboard/src/cockpit/paseoNavigationModel.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The model places non-archived native chats under validated current canonical AR sprint/master/task scope.

## Code Commentary

Canonical slash labels resolve against task docs and series topology. Groups use repository/path keys and current document titles. Unbound taskless chats stay in Projects; task-bound/partial inconsistent refs stay unresolved. Native workspace membership and parentAgentId do not infer scope.

## Invariants And Boundaries

The model filters archives but does not move native placement, change native selection or launch actors.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `canonicalScopes` | `dashboard/src/cockpit/paseoNavigationModel.ts:47-77` |
| Current source owner or exact assertion described above. | `groupPaseoChats` | `dashboard/src/cockpit/paseoNavigationModel.ts:77-131` |
| Conflicting legacy native membership and duplicate display titles leave canonical sprint/master/leaf groups distinct, with Projects first. | `keeps Projects first and separates duplicate titles by canonical sprint/master/task despite legacy memberships` | `dashboard/src/cockpit/paseoNavigationModel.test.ts:70-100` |
