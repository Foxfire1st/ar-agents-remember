# dashboard/src/cockpit/role-launcher/useLauncherSelectionRepair.ts

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Repair seeded document references and stale explicit overrides against current catalogs.

## Code Commentary

Pure functions choose the first invalid document/override tier and produce its existing reset payload. The document effect runs before the override effect at the launcher call site. Override repair waits for optionsReady; valid selections remain quiescent and callbacks stay live.

## Boundaries

Two independent effects, not a combined callback arbiter. Explicit model/effort UI changes retain feature values; inherited invalid-catalog model/effort repair drops them. No new permissions, option loading or Start gate.

## Evidence

- repairedSeededSelection is a current owner of the behavior described above. [1]
- repairedOverride is a current owner of the behavior described above. [2]
- usePruneSeededSelection is a current owner of the behavior described above. [3]
- usePruneStaleOverride is a current owner of the behavior described above. [4]
