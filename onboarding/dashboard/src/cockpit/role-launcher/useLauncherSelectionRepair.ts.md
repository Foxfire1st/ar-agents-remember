# dashboard/src/cockpit/role-launcher/useLauncherSelectionRepair.ts

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Repair seeded document references against served task entries.

## Code Commentary

Pure functions validate seeded sprint, master and task references against served TaskEntry options and reset the first invalid document tier. The remaining document effect runs when task entries arrive; valid selections remain quiescent and callbacks stay live. Catalog-based agent/model/effort override pruning was removed by R214, so unavailable choices are left intact for the launcher validation boundary.

## Boundaries

This module repairs document scope only. It neither prunes catalog overrides nor owns permissions, options loading or Start readiness.

## Evidence


- repairedSeededSelection is a current owner of the behavior described above. [1]



- repairedSeededSelection returns the first invalid seeded document correction, without catalog override pruning. [2]



- usePruneSeededSelection is a current owner of the behavior described above. [3]


- usePruneSeededSelection is the retained document repair effect; its dependencies contain no catalog or options-readiness input. [4]
