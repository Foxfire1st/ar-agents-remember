# dashboard/src/cockpit/roleChatOptionsLoader.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Load options/catalog data and restore exact saved request selection.

## Code Commentary

The effect and manual refresh own the current scoped options answer and a presentation-only saved catalog snapshot. Each load asks for the disk snapshot alongside fresh options; the snapshot is accepted only while that fresh request remains pending and is cleared when it settles. There is no process-held role-default cache or inventory merge. Abort, active-lifetime, canonical-scope and completion guards reject stale answers; periodic refresh cleans up its timer. Saved request and retry restoration retain exact UUID and references. A singular failure-only execution updates the failure channel without replacing an already selected Result receipt.

## Boundaries

Automatic refresh and an explicit successful action have distinct sticky-error clearing rules. Agent and catalog values are options scope, not native chat ownership or task acceptance.

## Evidence

- useRoleChatOptionsLoader is a current owner of the behavior described above. [1]

- applyOptionsSuccess is a current owner of the behavior described above. [2]
