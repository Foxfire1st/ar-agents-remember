# dashboard/src/cockpit/paseoNavigationModel.test.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The fixtures establish canonical AR group identity independently of mutable titles and native placement.

## Code Commentary

Duplicate sprint/master/leaf titles and old native workspace membership keep separate slash-reference group keys and Projects first. Malformed aliases, missing docs and conflicting topology stay unresolved. Controller altitude, archive exclusion and current display-title updates are explicitly checked.

## Invariants And Boundaries

The fixture matrix launches no actors; titles/native folders do not substitute for canonical scope.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `keeps Projects first` | `dashboard/src/cockpit/paseoNavigationModel.test.ts:70-100` |
| Current source owner or exact assertion described above. | `does not invent scope` | `dashboard/src/cockpit/paseoNavigationModel.test.ts:99-129` |
| Current source owner or exact assertion described above. | `places sprint and master` | `dashboard/src/cockpit/paseoNavigationModel.test.ts:111-129` |
| Builds groups from resolved repository/path references and current sprint/master/leaf topology, placing archived and unresolved agents according to the claim. | `groupPaseoChats` | `dashboard/src/cockpit/paseoNavigationModel.ts:77-131` |
